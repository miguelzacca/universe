import { mountScrub } from "../shared/scrub.js";
import { loadScrollMotion } from "../shared/scroll-motion.js";
import { mountVideo } from "./video.js";
import { mountFrames } from "./frames.js";

const track = document.querySelector("[data-track]");
const stage = track.querySelector("[data-stage]");
const params = new URLSearchParams(location.search);
const motion = params.get("motor") === "native"
  ? { dispose() {} }
  : await loadScrollMotion({ smooth: params.get("suave") !== "0" });
const useFrames = params.get("motor") === "frames";
const visible = new IntersectionObserver(([entry]) => {
  near = entry.isIntersecting;
  if (near) render(progress);
});
let near = false;
let progress = 0;
let renderer;

function render(value) {
  progress = value;
  if (!near || !track.hasAttribute("data-scrub")) return;
  if (!renderer) {
    renderer = useFrames
      ? mountFrames(stage.querySelector("canvas"), 72, index => "./frames/" + String(index).padStart(3, "0") + ".webp")
      : mountVideo(stage.querySelector("video"), 24);
  }
  renderer.render(value);
}

const disposeScrub = mountScrub({
  track, stage, render,
  reset() { renderer?.dispose(); renderer = undefined; },
  query: "(min-width: 50rem) and (min-height: 38rem) and (prefers-reduced-motion: no-preference)",
  driver: motion.driver,
});
visible.observe(stage);

addEventListener("pagehide", event => {
  if (event.persisted) return;
  visible.disconnect();
  disposeScrub();
  motion.dispose();
});
