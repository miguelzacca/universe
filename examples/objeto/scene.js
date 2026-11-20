const view = document.querySelector("[data-view]");
const start = document.querySelector("[data-load]");
const poses = document.querySelector("[data-views]");
const status = document.querySelector("[data-status]");
const title = document.querySelector("#title");
const copy = {
  front: "Vista de frente.",
  angle: "Vista em três quartos. O recorte lateral está visível.",
};

start.hidden = false;
start.addEventListener("click", async () => {
  start.disabled = true;
  status.textContent = "Carregando a vista 3D.";
  try {
    const THREE = await import("../node_modules/three/build/three.module.js");
    const surface = mountSurface(THREE);
    start.hidden = true;
    poses.hidden = false;
    poses.querySelector("button").focus();
    status.textContent = copy.front;
    poses.addEventListener("click", event => {
      const button = event.target.closest("[data-pose]");
      if (!button) return;
      surface.orient(button.dataset.pose);
      for (const control of poses.querySelectorAll("button")) {
        control.setAttribute("aria-pressed", String(control === button));
      }
      status.textContent = copy[button.dataset.pose];
    }, { signal: surface.signal });
    view.querySelector("canvas").addEventListener("webglcontextlost", () => {
      if (poses.contains(document.activeElement)) title.focus({ preventScroll: true });
      surface.dispose();
      start.hidden = true;
      poses.hidden = true;
      status.textContent = "Vista estática disponível.";
    }, { once: true });
    addEventListener("pagehide", event => { if (!event.persisted) surface.dispose(); }, { once: true });
  } catch {
    status.textContent = "Vista estática disponível.";
  }
});

function mountSurface(THREE) {
  const control = new AbortController();
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "low-power" });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5));
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, .1, 50);
  const outline = [[0,.08],[.75,.08],[.9,.21],[1,.4],[1.1,.67],[1.2,1],[1.24,1.15],[1.14,1.17],[1.08,.94],[.93,.5],[.68,.32],[0,.3]];
  const geometry = new THREE.LatheGeometry(outline.map(([r,y]) => new THREE.Vector2(r,y)), 64, 0, Math.PI * 1.83);
  const material = new THREE.MeshStandardMaterial({ color: 0x87aa79, roughness: .36, side: THREE.DoubleSide });
  const vessel = new THREE.Mesh(geometry, material);
  vessel.position.y = -.6;
  scene.add(vessel, new THREE.HemisphereLight(0xf5d7aa, 0x334c36, 2.15));
  const key = new THREE.DirectionalLight(0xffe6c1, 3.25);
  key.position.set(3,4,3);
  scene.add(key);
  view.append(renderer.domElement);

  const render = () => renderer.render(scene, camera);
  function resize() {
    const { width, height } = view.getBoundingClientRect();
    if (!width || !height) return;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
    render();
  }
  function orient(pose) {
    camera.position.set(pose === "angle" ? 3.7 : 0, pose === "angle" ? 2.6 : 1.25, 5.1);
    camera.lookAt(0,0,0);
    vessel.rotation.y = pose === "angle" ? .8 : -.35;
    render();
  }
  orient("front");
  const observer = new ResizeObserver(resize);
  observer.observe(view);
  resize();
  view.querySelector(".poster").hidden = true;

  return {
    signal: control.signal,
    orient,
    dispose() {
      if (control.signal.aborted) return;
      control.abort();
      observer.disconnect();
      geometry.dispose();
      material.dispose();
      renderer.dispose();
      renderer.domElement.remove();
      view.querySelector(".poster").hidden = false;
    },
  };
}
