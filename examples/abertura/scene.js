import { mountScrub, segment } from "../shared/scrub.js";
import { loadScrollMotion } from "../shared/scroll-motion.js";

const track = document.querySelector("[data-track]");
const stage = track.querySelector("[data-stage]");
const params = new URLSearchParams(location.search);
const motion = params.get("motor") === "gsap"
  ? await loadScrollMotion({ smooth: params.get("suave") !== "0" })
  : { dispose() {} };

const variableNames = [
  "--progress", "--cut-top", "--cut-right", "--cut-bottom", "--cut-left", "--curve",
  "--cover", "--wash", "--arc", "--shift", "--turn", "--zoom",
  "--sample-cut", "--sample-alpha", "--sample-rise",
  "--headline-top", "--headline-lift", "--headline-size",
];

function render(progress) {
  const opening = segment(progress, .12, .54);
  const reveal = segment(progress, .46, .88);
  const reframe = segment(progress, .37, .79);
  const drift = Math.sin(opening * Math.PI);

  const values = [
    progress.toFixed(4), 7 * (1 - opening) + "%", 7 * (1 - opening) + "%",
    8 * (1 - opening) + "%", 49 * (1 - opening) + "%",
    20 * (1 - opening) + "rem", (1 - reveal).toFixed(3), (.30 + .70 * opening).toFixed(3),
    1 - opening, -6 * opening + "%", -10 + 14 * opening + "deg", 1 + .32 * opening + .04 * drift,
    100 * (1 - reveal) + "%", reveal, 2 * (1 - reveal) + "rem",
    50 - 44 * reframe + "%", -50 * (1 - reframe) + "%", 7.5 - 3.45 * reframe + "vw",
  ];
  variableNames.forEach((name, index) => track.style.setProperty(name, values[index]));
}

const disposeScrub = mountScrub({
  track,
  stage,
  render,
  reset: () => variableNames.forEach(name => track.style.removeProperty(name)),
  query: "(min-width: 52rem) and (min-height: 40rem) and (prefers-reduced-motion: no-preference)",
  driver: motion.driver,
});

addEventListener("pagehide", event => {
  if (event.persisted) return;
  disposeScrub();
  motion.dispose();
});
