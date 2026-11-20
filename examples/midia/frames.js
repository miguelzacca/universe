export function mountFrames(canvas, count, frameUrl) {
  const context = canvas.getContext("2d");
  const controller = new AbortController();
  const { signal } = controller;
  const cache = new Map();
  const pending = new Set();
  const windowSize = 5;
  let wanted = 0;
  let visible;

  if (!context) return { render() {}, dispose() {} };

  function draw() {
    const candidates = [...cache.keys()].sort((a, b) => Math.abs(a - wanted) - Math.abs(b - wanted));
    const index = candidates[0];
    if (index === undefined || index === visible) return;
    context.drawImage(cache.get(index), 0, 0, canvas.width, canvas.height);
    visible = index;
    canvas.hidden = false;
    canvas.dataset.frame = index;
  }

  function cleanup() {
    for (const [index, bitmap] of cache) {
      if (Math.abs(index - wanted) <= windowSize) continue;
      bitmap.close();
      cache.delete(index);
    }
  }

  function requestNear() {
    const candidates = [wanted, wanted + 1, wanted - 1, wanted + 2, wanted - 2];
    for (const index of candidates) {
      if (pending.size >= 3) break;
      if (index < 0 || index >= count || cache.has(index) || pending.has(index)) continue;
      pending.add(index);
      fetch(frameUrl(index), { signal })
        .then(response => {
          if (!response.ok) throw new Error("Frame indisponível");
          return response.blob();
        })
        .then(blob => createImageBitmap(blob))
        .then(bitmap => {
          if (signal.aborted || Math.abs(index - wanted) > windowSize) {
            bitmap.close();
          } else {
            cache.set(index, bitmap);
            draw();
          }
          return true;
        })
        .catch(() => false)
        .then(success => {
          pending.delete(index);
          if (success && !signal.aborted) requestNear();
        });
    }
  }

  return {
    render(progress) {
      wanted = Math.round(progress * (count - 1));
      draw();
      cleanup();
      requestNear();
    },
    dispose() {
      controller.abort();
      for (const bitmap of cache.values()) bitmap.close();
      cache.clear();
      delete canvas.dataset.frame;
      canvas.hidden = true;
    },
  };
}
