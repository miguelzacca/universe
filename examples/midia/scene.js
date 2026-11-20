import { mountScrub } from "../shared/scrub.js";
import { mountVideo } from "./video.js";
import { mountFrames } from "./frames.js";

const track = document.querySelector("[data-track]");
const stage = track.querySelector("[data-stage]");
const visible = new IntersectionObserver(([entry]) => { near = entry.isIntersecting; if (near) render(progress); });
const useFrames = new URLSearchParams(location.search).get("motor") === "frames";
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

mountScrub({
  track, stage, render,
  reset() { renderer?.dispose(); renderer = undefined; },
  query: "(min-width: 50rem) and (min-height: 38rem) and (prefers-reduced-motion: no-preference)",
});
visible.observe(stage);
