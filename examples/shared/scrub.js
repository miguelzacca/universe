export const clamp = value => Math.max(0, Math.min(1, value));

export function segment(progress, start, end) {
  const t = clamp((progress - start) / (end - start));
  return t * t * (3 - 2 * t);
}

export function mountScrub({ track, stage, render, reset, driver, query }) {
  const preference = matchMedia(query);
  let active;
  let frame = 0;

  function draw(progress) {
    if (!active || active.progress === progress) return;
    active.progress = progress;
    render(progress);
  }

  function measure() {
    frame = 0;
    if (!active || document.hidden) return;
    const top = Number.parseFloat(getComputedStyle(stage).top) || 0;
    const bounds = track.getBoundingClientRect();
    const span = bounds.height - stage.offsetHeight;
    if (span > 0) draw(clamp((top - bounds.top) / span));
  }

  function schedule() {
    if (active && !frame && !document.hidden) frame = requestAnimationFrame(measure);
  }

  function enable() {
    cleanup();
    if (!preference.matches) return;
    track.setAttribute("data-scrub", driver ? "gsap" : "native");
    const controller = new AbortController();
    const { signal } = controller;
    active = { controller };
    if (driver) {
      const top = () => Number.parseFloat(getComputedStyle(stage).top) || 0;
      active.trigger = driver.create({
        trigger: track,
        start: () => "top " + top() + "px",
        end: () => "+=" + Math.max(1, track.offsetHeight - stage.offsetHeight),
        invalidateOnRefresh: true,
        onUpdate: self => draw(self.progress),
        onRefresh: self => draw(self.progress),
      });
      draw(active.trigger.progress);
    } else {
      const observer = new ResizeObserver(schedule);
      observer.observe(track);
      observer.observe(stage);
      active.observer = observer;
      addEventListener("scroll", schedule, { passive: true, signal });
      addEventListener("resize", schedule, { signal });
      addEventListener("pageshow", schedule, { signal });
      document.addEventListener("visibilitychange", schedule, { signal });
      schedule();
    }
  }

  function cleanup() {
    if (!active) return;
    active.controller.abort();
    active.observer?.disconnect();
    active.trigger?.kill();
    cancelAnimationFrame(frame);
    frame = 0;
    delete track.dataset.scrub;
    reset();
    active = undefined;
  }

  preference.addEventListener("change", enable);
  enable();
  return () => {
    preference.removeEventListener("change", enable);
    cleanup();
  };
}
