# Implementação da cena

Escolha a técnica pela transformação e pelo gesto do visitante. Use os ensaios como código original para estudar e adaptar. O atlas mostra sistemas e decisões das referências. O material de estudo fica fora do site final.

## Onde começar

| Necessidade | Referências | Código de partida |
| --- | --- | --- |
| Portal, máscara, plano que abre e entrega outro conteúdo | Uvra, Fermento, Maison, Veio | [HTML](../examples/abertura/index.html), [CSS das camadas](../examples/abertura/styles.css), [marcos e variáveis](../examples/abertura/scene.js), [controlador nativo/ScrollTrigger](../examples/shared/scrub.js) |
| Movimento liga vários beats e propriedades com tempos diferentes | KYVO, Aroeira, Torra | Ensaio de abertura com ScrollTrigger e a receita de timeline abaixo |
| Viagem pré-renderizada responde à posição | Aroeira, Torra, Sulko | [Ensaio de mídia](../examples/midia/index.html), [seek serializado](../examples/midia/video.js) |
| Um frame exato e ida/volta consistente são determinantes | Sereno, Torra, Sulko | Mesmo [ensaio de mídia](../examples/midia/index.html) com query motor=frames, [cache e desenho](../examples/midia/frames.js) |
| O visitante precisa mudar perspectiva por decisão própria | Arbo, Grau e os produtos que pedem inspeção | [Ensaio de objeto](../examples/objeto/index.html), [câmera e ciclo de vida Three.js](../examples/objeto/scene.js) |
| A cena envolve imagem, texto e interface real com movimentos pequenos | Prado, DigiGo, Tona | Use grid e z-index do ensaio. Limite progresso a propriedades que sustentam composição, legibilidade ou demonstração. Para entrada discreta, use IntersectionObserver e classes. |

Rode os ensaios por HTTP a partir da raiz da skill com **python scripts/servir-ensaios.py**. O [servidor local](../scripts/servir-ensaios.py) responde a HTTP Range no vídeo. Abra **/examples/abertura/** ou **/examples/midia/**. Para GSAP e Three.js, instale apenas no diretório dos exemplos com **npm install --prefix examples --ignore-scripts**. Abra **/examples/abertura/?motor=gsap** ou ative a vista em **/examples/objeto/**. A abertura padrão funciona sem instalações. A vista do objeto também funciona como página estática até a escolha do visitante.

## Arquitetura da passagem

1. Defina o wrapper de duração e o palco. Separe visual decorativo das áreas interativas. Evite a mesma propriedade de layout sendo escrita por dois controladores. Se o palco já usa sticky, ScrollTrigger pode dirigir o progresso sem pin adicional. Se o motor aplicar pin, teste a reserva de espaço, a passagem ao próximo heading e as âncoras.
2. Mantenha coordenadas do motivo consistentes. Se o recorte passa de uma janela para o quadro inteiro, preserve o ponto focal e altere a máscara. No assentamento, copie para a grade seguinte a regra de enquadramento, eixo ou posição do objeto que continua. As dimensões e proporções mobile podem pedir outro ativo.
3. Busque uma mudança clara por beat. Curvas podem ser mais elásticas na antecipação ou no assentamento de uma camada leve. Preserve controle direto em vídeo e 3D. Quando scroll reverso atropelar o estado atual, execute da posição vigente. Calibre aceleração e fade com o conteúdo final.
4. Trate conteúdo e ação como fluxo útil antes do enhancement. Faça a página abrir com título, prova suficiente e CTA em HTML. Se houver estados interativos dentro da animação, evite deixar foco em áreas visualmente inativas. Use alternativas em fluxo e o comportamento nativo do browser para teclado, toque e âncoras.

## GSAP com timeline de composição

Este recorte usa labels para programar uma máscara, a revelação de um painel e sua entrada em repouso. As proporções se referem ao storyboard deste exemplo. Em projeto com dependências, importe a cópia fixada de GSAP pelo bundler da aplicação. Contextualize instâncias à seção e descarte no teardown. O ensaio implementa a alternativa de ScrollTrigger lendo o mesmo progresso do controlador nativo.

```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);
const media = gsap.matchMedia();
media.add("(min-width: 52rem) and (prefers-reduced-motion: no-preference)", () => {
  const track = document.querySelector("[data-cena]");
  const stage = track.querySelector("[data-palco]");
  const mask = stage.querySelector("[data-mascara]");
  const proof = stage.querySelector("[data-prova-visual]");
  const timeline = gsap.timeline({
    scrollTrigger: {
      trigger: track,
      start: "top top",
      end: () => "+=" + Math.max(1, track.offsetHeight - stage.offsetHeight),
      scrub: 0.32,
      invalidateOnRefresh: true,
    },
  });

  timeline
    .addLabel("leitura", 0)
    .addLabel("abrir", 0.14)
    .addLabel("prova", 0.47)
    .addLabel("saída", 0.86)
    .fromTo(mask, { clipPath: "inset(8% 7% 9% 46% round 16rem)" },
      { clipPath: "inset(0% 0% 0% 0% round 0rem)", duration: 0.47, ease: "power2.inOut" },
      "abrir")
    .fromTo(proof, { opacity: 0, y: 46 },
      { opacity: 1, y: 0, duration: 0.40, ease: "power3.out" }, "prova");
});

// Na desmontagem da rota ou da seção.
const disposeScene = () => media.revert();
```

Mantenha os elementos do recorte como camadas de apresentação e a informação equivalente em HTML. Meça CLS e custo de pintura ao usar máscara grande. Prefira Transform/Opacity para deslocar camadas complementares. Use Lenis apenas se amortecimento resolver uma necessidade observada, com um dono para RAF e testes de modal, foco e toque. [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) · [gsap.matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/) · [Lenis](https://github.com/darkroomengineering/lenis)

## Vídeo, frames e 3D

- **Vídeo por tempo.** É bom para atmosfera, ações completas e loops com uma emenda planejada. Poster, descrição em HTML e controle de reprodução são parte da cena. Para autoplay decorativo, silencie, respeite prefers-reduced-motion, pause fora da tela e após rejeição mostre o poster.
- **Seek.** Use a faixa de tempo reproduzível e preserve o último alvo durante um seek. Teste arquivo com GOP pequeno e distribuição por HTTP Range. Evite buscar além do último quadro. Teste teclado, fast scroll, reverse, iOS/Safari e recuperação após erro. O ensaio usa H.264 a 24 fps e keyframe a cada 12 quadros. [MDN vídeo](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) · [FFmpeg](https://ffmpeg.org/ffmpeg.html)
- **Frames.** Projete nomeação e manifesto por viewport. Limite decodificação simultânea, janela de cache e tamanho da imagem decodificada. Execute um canvas visível e mantenha o quadro próximo até o correto chegar. Inspecione consumo real. Para sobrepor UI ao objeto, aplique o mesmo cálculo de cover aos pontos normalizados. Veja [direção e motion](direcao-e-motion.md).
- **3D.** Comece pelo valor de inspeção, como um contorno que aparece ao girar ou um hotspot de planta. A cena de exemplo só inicializa depois do clique, desenha sob demanda e libera geometria, material e renderer. Com GLB, exija acesso válido ao ativo, valide materiais, pivô, escala e Meshopt/KTX2 quando utilizados. Ofereça alternativa em texto, poster e ângulos estáticos. [Three.js cleanup](https://threejs.org/manual/#en/cleanup) · [model-viewer](https://modelviewer.dev/docs/)
