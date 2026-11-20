# Universe

Universe is an Agent Skill for building cinematic landing pages. It turns a brief, a business link, or an existing site into a visual direction, a scroll-driven scene, and an editable preview tested in a browser.

## Install

```bash
npx skills add https://github.com/miguelzacca/universe --skill universe
```

Paste the repository link into an agent that supports Agent Skills and ask it to install Universe. For manual installation, place the full **universe** folder in your agent's skill directory, such as **~/.agents/skills/** or **.agents/skills/** for Codex. Keep **SKILL.md** with its reference files and examples. [Agent Skills format](https://agentskills.io/specification) · [Codex skills](https://developers.openai.com/codex/skills/) · [Skills CLI](https://github.com/vercel-labs/skills)

```text
$universe
Build a cinematic landing page for this business: <link>.
Use the visual atlas, build the main scene, and verify the transition
on desktop and mobile. Deliver editable code and a working preview.
```

## Inside

- [Skill instructions](SKILL.md) and [reusable prompts](prompts/prompts.md)
- [Visual atlas](references/atlas.md) with research boards, design tokens, and scene notes
- [Optional two-frame AI video](references/video-por-scroll.md) with storyboard approval, shot direction, a cost estimate, and OpenRouter setup
- [Scene contract](references/contrato-de-cena.md) and [runnable examples](references/receitas.md) for CSS, GSAP, video, canvas, and Three.js
- [Browser verification](references/verificacao.md) and [evaluation evidence](evaluations/evidencias-v2.md)

The detailed guides are written in Brazilian Portuguese. The atlas credits the original visual references. Its boards are included for study. The runnable labs use original examples.

## Uso em português

Instale pelo link acima e invoque `$universe` com o link da empresa ou do projeto. Para uma execução completa, use [o prompt Modo GO](prompts/prompts.md#criação-completa-com-iteração), que orienta o agente a implementar, inspecionar as cenas e corrigir falhas de transição antes da entrega.
