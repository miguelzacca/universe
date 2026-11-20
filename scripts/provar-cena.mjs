import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

const [url, contractPath, output] = process.argv.slice(2);
if (!url || !contractPath || !output) {
  console.error("Uso: node provar-cena.mjs http://127.0.0.1:4173/cena/ contrato.json capturas");
  process.exit(2);
}

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "playwright");
const spec = JSON.parse(await readFile(contractPath, "utf8"));
assert(spec.marks.length >= 4, "Inclua início, transformação, revelação e saída");
for (const item of [...spec.marks, ...(spec.mobileSteps ?? [])]) {
  assert(/^[a-z0-9_-]+$/i.test(item.id), "Use um ID simples na captura.");
}
await mkdir(output, { recursive: true });
const browser = await chromium.launch(process.env.CHROMIUM_EXECUTABLE
  ? { executablePath: process.env.CHROMIUM_EXECUTABLE, args: ["--no-sandbox"] } : {});
const desktop = { width: 1440, height: 900 };
const phone = { width: 390, height: 844 };
const evidence = { url, browser: browser.version(), marks: [], mobileSteps: [] };

async function open(options) {
  const page = await browser.newPage(options);
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const response = await page.goto(url, { waitUntil: "domcontentloaded" });
  assert(response?.ok(), "A entrada do preview precisa responder.");
  await page.evaluate(() => document.fonts.ready.then(() => undefined));
  return { page, errors };
}

async function checkBase(page) {
  assert(await page.locator(spec.heading).first().isVisible(), "Título visível");
  assert(await page.locator(spec.cta).first().isVisible(), "Ação visível");
  assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), "Rolagem horizontal da página");
  const href = await page.locator(spec.cta).first().getAttribute("href");
  assert.equal(href, spec.destination, "Destino configurado");
}

async function seek(page, progress) {
  await page.evaluate(({ track, stage, progress }) => {
    const container = document.querySelector(track);
    const sticky = document.querySelector(stage);
    const length = container.offsetHeight - sticky.offsetHeight;
    if (length <= 0) throw new Error("A cena não tem percurso no viewport de teste.");
    const inset = Number.parseFloat(getComputedStyle(sticky).top) || 0;
    const start = container.getBoundingClientRect().top + scrollY - inset;
    scrollTo({ top: start + progress * length, behavior: "instant" });
  }, { track: spec.track, stage: spec.stage, progress });
}

async function mark(page, label, item) {
  await seek(page, item.position);
  const readings = await page.waitForFunction(checks => {
    const values = checks.map(({ selector, property }) => {
      const element = document.querySelector(selector);
      return element ? Number.parseFloat(getComputedStyle(element).getPropertyValue(property)) : NaN;
    });
    return values.every((value, index) => {
      const { min, max } = checks[index];
      return value >= (min ?? -Infinity) && value <= (max ?? Infinity);
    }) ? values : false;
  }, item.metrics, { timeout: 4000 });
  evidence.marks.push({ id: label, position: item.position, values: await readings.jsonValue() });
  await page.screenshot({ path: join(output, label + ".png") });
}

try {
  const wide = await open({ viewport: desktop });
  await checkBase(wide.page);
  await wide.page.waitForFunction(stage => getComputedStyle(document.querySelector(stage)).position === "sticky", spec.stage);
  for (const item of spec.marks) await mark(wide.page, item.id, item);
  await mark(wide.page, "reverse", spec.marks[1]);
  await wide.page.locator(spec.next).scrollIntoViewIfNeeded();
  await wide.page.screenshot({ path: join(output, "next.png") });
  await wide.page.emulateMedia({ reducedMotion: "reduce" });
  await wide.page.waitForFunction(stage => getComputedStyle(document.querySelector(stage)).position !== "sticky", spec.stage);
  assert.deepEqual(wide.errors, []);
  await wide.page.close();

  const mobile = await open({ viewport: phone, isMobile: true, hasTouch: true });
  await checkBase(mobile.page);
  const action = mobile.page.locator(spec.cta).first();
  assert((await action.boundingBox()).y < phone.height, "CTA móvel alcançável na abertura");
  await mobile.page.screenshot({ path: join(output, "mobile.png") });
  if (spec.destination.startsWith("#")) {
    await action.tap();
    await mobile.page.waitForURL(url => url.hash === spec.destination);
    await mobile.page.screenshot({ path: join(output, "mobile-next.png") });
  }
  let previousTop = -Infinity;
  for (const step of spec.mobileSteps ?? []) {
    const element = mobile.page.locator(step.selector).first();
    assert(await element.isVisible(), "Etapa móvel visível: " + step.id);
    const top = await element.evaluate(node => node.getBoundingClientRect().top + scrollY);
    assert(top > previousTop, "Ordem das etapas no fluxo móvel: " + step.id);
    previousTop = top;
    await element.scrollIntoViewIfNeeded();
    await mobile.page.screenshot({ path: join(output, "mobile-" + step.id + ".png") });
    evidence.mobileSteps.push(step.id);
  }
  assert.deepEqual(mobile.errors, []);
  await mobile.page.close();

  const reduced = await open({ viewport: desktop, reducedMotion: "reduce" });
  await checkBase(reduced.page);
  assert.notEqual(await reduced.page.locator(spec.stage).evaluate(e => getComputedStyle(e).position), "sticky");
  await reduced.page.screenshot({ path: join(output, "reduced.png") });
  await reduced.page.close();

  const fallback = await open({ viewport: phone, javaScriptEnabled: false });
  await checkBase(fallback.page);
  await fallback.page.getByRole("main").first().evaluate(element => {
    if (!element.textContent?.trim()) throw new Error("Conteúdo indisponível sem JS");
  });
  await fallback.page.screenshot({ path: join(output, "sem-js.png") });
  await fallback.page.close();
  evidence.checked = ["marks", "reverse", "next", "mobile", "reduced", "no-js", "cta-href"];
  await writeFile(join(output, "resultado.json"), JSON.stringify(evidence, null, 2) + "\n");
  console.log("Percurso técnico aprovado. Revise os quadros e a ação comercial antes de aprovar a cena.");
} finally {
  await browser.close();
}
