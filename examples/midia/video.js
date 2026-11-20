export function mountVideo(video, fps) {
  const controller = new AbortController();
  const { signal } = controller;
  let wanted = 0;
  let broken = false;

  function flush() {
    if (broken || video.seeking || video.readyState < HTMLMediaElement.HAVE_METADATA) return;
    const time = wanted * Math.max(0, video.duration - 1 / fps);
    if (Number.isFinite(time) && Math.abs(video.currentTime - time) >= .5 / fps) {
      video.currentTime = time;
    } else if (video.readyState >= HTMLMediaElement.HAVE_CURRENT_DATA) {
      video.hidden = false;
    }
  }

  video.addEventListener("loadeddata", flush, { signal });
  video.addEventListener("loadedmetadata", flush, { signal });
  video.addEventListener("seeked", flush, { signal });
  video.addEventListener("error", () => {
    broken = true;
    video.hidden = true;
  }, { signal });
  video.src = video.dataset.src;
  video.preload = "auto";

  return {
    render(progress) { wanted = progress; flush(); },
    dispose() {
      controller.abort();
      video.hidden = true;
      video.removeAttribute("src");
      video.load();
    },
  };
}
