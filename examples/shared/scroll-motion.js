// Mantenha um scroll nativo como base. GSAP lê a posição e Lenis suaviza a roda.
export async function loadScrollMotion({ smooth = true } = {}) {
  let gsap, ScrollTrigger;
  try {
    const [core, plugin] = await Promise.all([
      import("../node_modules/gsap/index.js"),
      import("../node_modules/gsap/ScrollTrigger.js"),
    ]);
    gsap = core.gsap;
    ScrollTrigger = plugin.ScrollTrigger;
    gsap.registerPlugin(ScrollTrigger);
  } catch {
    return { dispose() {} };
  }

  const motion = { driver: ScrollTrigger, dispose() {} };
  if (!smooth) return motion;
  let Lenis;
  try {
    ({ default: Lenis } = await import("../node_modules/lenis/dist/lenis.mjs"));
  } catch {
    return motion;
  }

  const preference = matchMedia("(prefers-reduced-motion: no-preference) and (hover: hover) and (pointer: fine)");
  let lenis;
  const tick = time => lenis.raf(time * 1000);
  const scrollKeys = new Set(["ArrowUp", "ArrowDown", "PageUp", "PageDown", "Home", "End", " "]);

  function releaseWheel(event) {
    if (lenis.isScrolling === "smooth" && scrollKeys.has(event.key)) {
      lenis.scrollTo(window.scrollY, { immediate: true });
    }
  }

  function stop() {
    if (!lenis) return;
    gsap.ticker.remove(tick);
    window.removeEventListener("keydown", releaseWheel);
    lenis.destroy();
    lenis = undefined;
  }

  function sync() {
    if (!preference.matches) {
      stop();
    } else if (!lenis) {
      lenis = new Lenis({
        autoRaf: false,
        smoothWheel: true,
        lerp: 0.105,
        syncTouch: false,
        anchors: { immediate: true },
        stopInertiaOnNavigate: true,
      });
      lenis.on("scroll", ScrollTrigger.update);
      gsap.ticker.add(tick);
      window.addEventListener("keydown", releaseWheel);
    }
    ScrollTrigger.refresh();
  }

  preference.addEventListener("change", sync);
  sync();
  motion.dispose = () => {
    preference.removeEventListener("change", sync);
    stop();
  };
  return motion;
}
