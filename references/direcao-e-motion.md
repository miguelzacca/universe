# Direção de arte e motion

Use este guia depois de verificar a marca e a oferta. Traduza o briefing em um sistema visual, um roteiro de cenas e uma escolha de implementação por cena. Prove o trecho mais exigente antes de desenvolver a página inteira.

## Da marca ao sistema visual

1. Encontre a ação, a pergunta ou a prova que deve orientar a página. Exemplo para uma marcenaria autoral. A sequência aproxima o público do material, mostra a precisão do encaixe e deixa o próximo passo visível quando o móvel está montado.
2. Escolha uma imagem-chave e duas ou três propriedades visuais da marca que têm base verificável. Observe cor, material, enquadramento, gestual, contraste e vocabulário. Crie o restante da direção com base nessas propriedades, no setor e no briefing. Preserve a identidade fornecida. Compare a silhueta da primeira dobra, ordem das cenas, tratamento tipográfico e mídia com as referências para manter a composição própria.
3. Forme uma paleta por papel. Registre superfícies, texto, texto secundário, cor de ação, linha e cores contextuais das cenas. Teste o menor contraste ao longo de um vídeo. Quando a imagem varia muito, use composição reservada, tratamento tonal consistente ou fundo de texto medido.
4. Defina papéis tipográficos para título, intertítulo, corpo e interação. Faça quebras e escala fluidas em cima do texto real e valide acentos, números, legibilidade de botões e fontes de fallback. Use _clamp()_ com limites em rem. Carregue somente pesos e alfabetos necessários e preserve as quebras importantes após o carregamento.
5. Defina largura de leitura, grid, margens e proporções da mídia. Um ponto de partida pode usar 12 colunas na tela larga, quatro na estreita, 24–80 px de margem conforme largura e 45–70 caracteres em parágrafos longos. A estrutura final vem da composição e do conteúdo. Defina um enquadramento de retrato que preserve o assunto e a área de leitura.
6. Defina as superfícies que fazem a página parecer uma sequência contínua. Use um eixo de composição, cor de passagem, linha de horizonte, textura ou silhueta que conecte cenas. Escolha uma camada protagonista por momento. Reserve o maior contraste ou movimento para uma mudança de informação, uma demonstração ou a ação principal.

Registre tokens de composição junto de cores e tipos. Inclua escala de distância, profundidade, nível de sobreposição, duração, aceleração e um papel para o tratamento de mídia. Mantenha as camadas do layout como DOM semântico, com visual independente de leitura, foco e SEO.

## Roteiro e transições

Leia a página em três velocidades. No primeiro olhar, a oferta e a ação ficam claras. Em uma passada por títulos, cenas e CTAs contam a história. Na exploração, o motion revela matéria, funcionamento, transformação ou prova. Variações válidas incluem abrir com uma evidência ou transformar a cena principal em um índice de serviços.

Para cada cena, anote o objetivo, conteúdo visível, arquivo e recorte, entrada, pausa, virada e saída. Descreva o que muda quando o usuário volta a rolar para cima. Separe eventos discretos de progresso contínuo. Se uma cena sofre mudanças automáticas com o tempo e também responde à rolagem, dê a cada propriedade um único controlador e teste como os ritmos se combinam.

| Campo | Registro de exemplo para uma cena original |
| --- | --- |
| Função | Mostrar como um encaixe cria a aparência final do móvel. |
| Plano | Close lateral da madeira e título alinhado com a emenda. |
| Gatilho | Topo da seção alcança o topo da viewport. |
| Fonte de progresso | Posição de rolagem dentro da trilha da cena, clamp entre 0 e 1. |
| 0–0,16 | Imagem aberta e pergunta legível. |
| 0,16–0,60 | A seção já fixou. A câmera se aproxima da emenda. |
| 0,60–0,83 | O enquadramento pausa para a leitura da prova. |
| 0,83–1 | A seção seguinte ganha a tela pela mesma borda da emenda. |
| Reversão | A transformação acompanha o gesto. A prova permanece no fluxo de leitura. |
| Mobile | Dois recortes em sequência, com a prova junto ao detalhe correspondente. |
| Movimento reduzido e falha | Foto do móvel montado, detalhe e prova em uma sequência estática. |
| Ação | CTA acessível após a prova e no final. |

Faça a primeira passagem do storyboard nos estados 0%, 25%, 50%, 75% e 100% da cena. Veja também onde a cena anterior libera a viewport e onde a seguinte começa. Verifique a versão estreita com texto real antes de definir câmera e margem. Use amostras de vídeo com proporção e movimento próximos dos finais ao medir o gesto.

Use padrões de composição que tenham uma função observável.

| Passagem | Uso | Implementação provável |
| --- | --- | --- |
| Corte | Troca firme de assunto ou escala. | Seções em fluxo, alinhamento de arestas e mudança de fundo. |
| Dissolução | Unir dois estados semelhantes com composição alinhada. | Duas camadas confinadas à cena, opacidade de uma delas ligada ao progresso. |
| Mudança de escala | Mostrar detalhe, depois restabelecer contexto. | Um contêiner de recorte e transform sobre a mídia. |
| Cortina ou máscara | Mostrar um detalhe por continuidade de direção. | Recorte limitado à cena. Meça o custo de pintura ao usar _clip-path_ ou máscaras. |
| Objeto que atravessa a dobra | Conectar capítulos pelo mesmo elemento visual. | Um palco compartilhado com camadas no DOM e conteúdo textual livre. |
| Transformação com pausa | Explicar processo ou configuração. | Trilha mais longa, palco sticky e intervalos de progresso para ações e leitura. |

Pontos de partida para ajustar em dispositivo real.

- Microinteração de 120–220 ms. Entrada editorial de 280–550 ms com 40–75 ms entre poucos elementos relacionados. Reverta o estado imediatamente quando o usuário repetir a ação durante a transição.
- Trilha de 1,6–2,4 alturas de viewport para uma transformação curta em tela larga, contando a altura do próprio palco. Dê mais tempo somente se o conteúdo precisar. Inclua uma pausa legível antes de liberar o palco. No mobile, encurte o trecho ou faça a cena correr no fluxo.
- Use deslocamentos menores para elementos de leitura. Um parallax de apoio pode começar entre 8 e 24 px em viewport média. Nas cenas atreladas ao gesto, use progressão linear na base e easing nos subintervalos que precisam de antecipação ou repouso.

## Escolha de implementação

Preserve a stack do projeto quando ela sustentar a experiência. Uma landing com HTML estático ou Astro pode entregar o conteúdo renderizado e hidratar o palco. Use React/Next quando a stack já existir ou o produto precisar do seu modelo de componentes. Escolha os mecanismos pelo problema de cada cena.

| Necessidade | Primeira escolha | Motivo para ampliar |
| --- | --- | --- |
| Entrada discreta, revelar apoio ou carregar mídia perto do uso | CSS com classes de estado e IntersectionObserver | Mais de uma fase temporal compartilhando gatilho. |
| Progresso de uma leitura ou elemento local | CSS scroll timeline com melhoria progressiva | Dependência de sincronizar várias cenas ou lacuna no navegador-alvo. |
| Palco fixo com narrativa linear | Wrapper no fluxo e _position: sticky_ | Pinos encadeados, direção variável ou controle coordenado de múltiplas trilhas. |
| Transformação sincronizada por intervalos | Timeline GSAP com ScrollTrigger | Meça se o custo e a complexidade compensam o resultado. |
| Profundidade de câmera predefinida | Vídeo ou sequência de quadros | Interação real de ponto de vista, estado ou configuração que a mídia filmada não representa. |
| Rotação explorável de um objeto | GLB com visualizador sob demanda | Cena com câmera, iluminação ou interação específica, que justifica Three.js ou React Three Fiber. |

Trate a suavização como parte do acabamento de LPs cinematográficas. Preserve roda, toque, teclado, histórico, âncoras, busca e restauração de posição. Escreva um único progresso por cena. Use o suavizador da stack ou escolha Lenis + ScrollTrigger. Com palco sticky em CSS, use Lenis + ScrollTrigger sem pin adicional. ScrollSmoother é uma alternativa para projetos que já usam o wrapper do GSAP. Quando o wrapper for transformado, use pin do ScrollTrigger e revise a posição de elementos fixos. Use um único suavizador por página. [Lenis](https://github.com/darkroomengineering/lenis) · [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) · [ScrollSmoother](https://gsap.com/docs/v3/Plugins/ScrollSmoother/)

## Microinterações dos controles

Percorra a página inteira e dê resposta a cada botão, link, item de menu, card clicável, seletor e controle de formulário. Defina transições a partir da marca. Comece com 160–240 ms e ajuste a curva até a resposta parecer imediata no clique e leve na volta. Use mudanças de cor, borda, posição de um ícone ou pressão de 1 px sem mover a caixa clicável no layout. Reserve tratamentos maiores para mudanças de navegação ou estado.

| Controle | Resposta |
| --- | --- |
| CTA e link | Acento, sublinhado ou deslocamento contido de ícone no hover. Estado de pressão no toque e contorno de foco visível. |
| Card clicável | Um gesto discreto da moldura ou da imagem, com o mesmo alvo semântico em teclado e toque. |
| Menu, acordeão e escolha | Estado expandido ou selecionado inequívoco. Sincronize classe, foco e `aria-expanded` ou `aria-pressed` com a ativação. Anime conteúdo interno sem atrasar a ação. |
| Formulário | Foque o campo, informe validação, envio, sucesso ou erro quando pertinentes e preserve o acesso à mensagem. |

Restrinja hover, magnetismo e inclinação ao mouse preciso. Preserve estado, contraste e foco em modo reduzido, com transições de movimento desligadas. Use semântica nativa e trate conteúdo estático como leitura. Teste controles em headers sobre cenas, menus móveis, modais e conteúdo fora da primeira dobra. [CSS adaptável de microinterações](../examples/shared/microinteracoes.css)

### CSS e JavaScript nativo

- Construa um wrapper que define a distância da cena e um filho sticky que define o palco. Lembre que _overflow_ dos ancestrais pode mudar o scroll container de referência do sticky. Use _min-height_ e um tamanho estável de cena em mobile. Teste _svh_ para cenas com leitura e variação da barra do navegador. Use _dvh_ quando a cena precisar acompanhar essa variação e verifique a estabilidade.
- Use _view()_ para acompanhar a passagem do elemento pela área rolável e _scroll()_ para progresso de um scroller. Aplique sob _@supports_ e dentro de _prefers-reduced-motion: no-preference_. Em CSS, declare _animation-timeline_ após a shorthand _animation_, que restaura o valor da timeline. Mantenha a posição visual e a ação essenciais estáticas como base.
- Use IntersectionObserver para marcar entradas ou saídas, pausar mídia e acionar carregamento próximo. Ele entrega interseções em limiares, adequadas para estados discretos. Para comportamento contínuo em navegadores que precisam de alternativa, derive progresso de coordenadas de scroll e atualize a cena ativa uma vez por frame, agrupando leituras e escritas. Recalcule medidas em layout e tamanho alterados.
- Restrinja mudanças por frame a _transform_ e _opacity_ sempre que viável. Meça recortes, sombra difusa, blur, filtros e superfícies grandes em movimento. Remova _will-change_ quando o efeito termina e preserve ordem de foco independente de posição visual.
- Uma entrada não deve depender de ocultar informação antes da inicialização. Aplique o estado decorativo após criar o observador. Remova observadores e eventos, cancele RAF e restaure classes/estilos próprios quando a cena sai de uso.

[CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) · [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) · [Performance de animações](https://web.dev/articles/animations-guide)

### Timelines GSAP

- Prepare o HTML e a versão de movimento reduzido antes da timeline. Se houver controle de pausa ou modo estático, deixe-o operável desde o início. Registre ScrollTrigger na montagem e delimite os seletores ao contêiner. Em interfaces com rotas, faça cada componente controlar suas instâncias.
- Para iniciar a calibração, teste _start: "top top"_, _end_ calculado a partir do comprimento necessário e _scrub: true_. Um _scrub_ numérico entre 0,2 e 0,5 s de partida pode amortecer irregularidade. Verifique se a mídia acompanha o gesto com o atraso escolhido. Registre fases em labels para posicionar mídias e textos de forma legível.
- Faça desktop, mobile e movimento reduzido em condições _gsap.matchMedia()_. Quando o _pin_ for necessário, teste o espaço reservado no fluxo, mudanças de rota e navegação direta até a próxima seção. Ancestrais transformados alteram o contexto de posicionamento. Em palcos já presos por CSS, use ScrollTrigger só para a timeline.
- Reserve geometria das mídias e dê dimensões aos elementos para evitar releituras após a montagem. Quando fontes, imagens ou um painel mudarem a geometria, revise se o refresh automático cobre o caso e atualize de forma agrupada quando necessário. Use _invalidateOnRefresh_ junto de valores recalculáveis.
- Ao desmontar, faça _revert()_ do matchMedia/contexto e remova listeners, timers, instâncias e recursos externos criados pelo componente. Teste entrada, saída e segunda entrada na rota e garanta uma instância por cena.
- Use _markers_ no diagnóstico local. Em produção, teste ida e volta, scroll brusco, mudança de orientação, zoom e deep link sem depender do editor.

[ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) · [gsap.matchMedia()](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/)

### Cenas com vídeo

| Técnica | Use quando | Controle e alternativa |
| --- | --- | --- |
| Loop ambiente | A luz, matéria ou lugar ajuda a reconhecer a marca. | _muted_, _playsinline_, controle de pausa quando aplicável e poster. Pause fora de vista e em aba oculta. |
| Reprodução por entrada | O usuário precisa ver uma sequência na ordem. | Inicie quando a cena for visível. Resolva rejeição de _play()_ e ofereça replay quando fizer diferença. |
| Vídeo ligado a rolagem | Cada momento da mídia corresponde a uma etapa da cena. | Derive o tempo pelo progresso e teste latência de seek no celular. Mantenha os quadros que explicam a etapa. |
| Sequência de quadros | O gesto exige posicionamento fino e reversão precisa. | Carregue o primeiro quadro e poucos vizinhos sob demanda. Limite fila, janela de cache e DPR do canvas. |
| Vídeo informativo com som | Explicação, depoimento ou demonstração com fala. | Ação explícita para áudio, controles, legendas e resumo ou transcrição conforme o conteúdo. |

Defina qual quadro é o poster e o que o navegador mostra quando o vídeo demora ou está indisponível. Quando o poster for a imagem principal, reserve sua geometria e meça o LCP antes de definir prioridade. Mídia abaixo da dobra pode entrar por proximidade. Meça se o codec web, a variante mobile e os recortes atendem aos navegadores-alvo. Evite carregar duas variantes para esconder uma com CSS.

Para controlar vídeo por scroll, aguarde metadados e uma faixa reproduzível antes de mapear o tempo. Restrinja o alvo a uma faixa válida e teste o último quadro. Agrupe atualizações e mantenha o último tempo desejado enquanto um seek estiver em curso. Reaplique o último alvo relevante em _seeked_. Use _requestVideoFrameCallback_ quando precisar observar o quadro apresentado e um fallback para o navegador-alvo. Remova callbacks na desmontagem. Quando o fluxo engasgar, teste intervalo menor entre keyframes e compare bytes e tempo de seek, ou troque por poucos estados com poster/swaps. _fastSeek()_ é aproximação, com suporte variável. [requestVideoFrameCallback](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/requestVideoFrameCallback) · [fastSeek()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/fastSeek) · [Vídeo na web](https://web.dev/articles/video-and-source-tags) · [LCP](https://web.dev/articles/lcp)

Para sequência, calcule memória decodificada antes do protótipo. A aproximação de largura × altura × 4 bytes por imagem coloca 90 quadros RGBA de 1920 × 1080 em cerca de 712 MiB, sem o restante do app. Cache curto, resolução por dispositivo, cancelamento de buscas antigas e descarte de _ImageBitmap_ são parte do desenho. Mantenha quadro vizinho ou poster até o desejado estar pronto. Ao redimensionar, restaure o recorte e desenhe o quadro vigente. Teste ida e volta sem flashes.

### Cenas com 3D

Escolha um efeito 3D quando o usuário puder entender algo novo ao girar, explorar, desmontar, mudar configuração ou observar parallax real. Prove primeiro a silhueta, a textura e a leitura com um render fixo. Para câmera dirigida, considere pré-render. Para visualização simples de um objeto, considere _model-viewer_. Para controle de cena, escolha Three.js ou R3F conforme o projeto.

- Prepare um GLB com escala, pivô, materiais e orientação documentados e render estático correspondente. Comprima geometria ou textura conforme compatibilidade e custo de decodificação. Prove a leitura em um celular real antes de aumentar resolução, luzes ou pós-processamento.
- Preserve informações, CTAs e controles semânticos em HTML. Para objetos que informam escolha, dê alternativa de seleção acessível. Canvas decorativo não precisa capturar gestos nem foco.
- Em cenas sob demanda, limite DPR e desenhe quando o estado mudar. Use _frameloop="demand"_ e _invalidate()_ em R3F quando controles ou timeline mudarem a câmera fora do React. Suspenda atualização quando fora de vista, em aba oculta ou no modo estático. Em animações por frame, atualize o objeto ou uniforms e evite render React por frame.
- Para troca de rota, descarte renderizador e recursos que a cena criou conforme a biblioteca. Trate geometria, texturas, materiais e render targets com propriedade clara, preservando os compartilhados. Trate falha ou perda de contexto WebGL com o render estático. Teste a alternativa também em conexão lenta e com movimento reduzido.
- Comece com orçamento conservador compatível com a página. Exemplos iniciais são DPR 1–1,5 em mobile, texturas de 1K–2K, um único canvas ativo e uma cena simples. Ajuste por evidência de tempo de quadro, memória, bytes e legibilidade.

[model-viewer](https://modelviewer.dev/docs/) · [Three.js cleanup](https://threejs.org/manual/#en/cleanup) · [R3F performance](https://r3f.docs.pmnd.rs/advanced/scaling-performance)

## Prove a cena e seus modos

Construa primeiro o palco mais delicado com o conteúdo real. Garanta que os estados produzam um começo, uma transformação e uma saída visíveis. Use captura nos marcos do storyboard e teste com gesto real, teclado e toque. Inclua o salto para um link interno enquanto o palco está ativo. Trate a barra de endereço móvel e a passagem para rolagem normal.

- **Modo completo.** Compare a primeira dobra e os marcos de scroll em desktop e mobile. Verifique retorno rápido, pulo de seção, resizes e desmontagem. Um elemento essencial que se esconde entre marcos exige correção.
- **Modo de movimento reduzido.** Respeite _prefers-reduced-motion_, incluindo alteração durante a sessão. Faça a versão que preserva a narrativa por cortes, quadros e hierarquia. Encurte ou remova pin, suavização, movimentos ampliados, reprodução automática e parallax conforme o caso. Ofereça mecanismo para pausar, interromper ou ocultar conteúdo animado em paralelo que dura mais de cinco segundos quando aplicável.
- **Modo de falha.** Force mídia indisponível, JS atrasado ou desativado em uma entrada renderizada no servidor, autoplay negado e contexto 3D ausente quando houver 3D. Confirme títulos, âncoras, oferta, preço ou prova quando verificados, e CTA principal utilizáveis.
- **Acessibilidade.** Passe a sequência pelo teclado, leia a ordem dos headings, teste redução, contraste e zoom de 200%. Dê foco visível, use _scroll-margin-top_ quando há cabeçalho fixo e certifique-se de que o palco e os overlays nunca bloqueiam a interação que aparece por baixo.
- **Desempenho.** Inspecione a build de produção com cache frio e condições móveis. Meça o custo da primeira dobra e de uma sessão de scroll. Verifique rede, long tasks, camadas, repetição de decodes e recolhimento depois da navegação. Como ponto de partida, procure manter a cena fluida perto do orçamento de 16,7 ms por quadro a 60 Hz em dispositivo-alvo. Valide com dados de campo ou rotule medições locais como laboratório.

[Preferência de movimento reduzido](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) · [WCAG Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) · [WCAG Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)


## Alinhe texto, máscaras e hotspots aos planos

Mantenha overlays informativos em HTML. Quando uma chamada precisa acompanhar um ponto dentro de imagem, normalize suas coordenadas no arquivo, guarde as posições nos instantes chave e interpole pelo progresso da mídia. Para uma mídia de largura `w` e altura `h` centralizada em um palco `W × H` com `object-fit: cover`, calcule `s = max(W / w, H / h)`. Para coordenadas normalizadas `u, v`, a projeção é `x = (W - w × s) / 2 + u × w × s` e `y = (H - h × s) / 2 + v × h × s`. Se o projeto usa outra âncora, aplique o mesmo deslocamento do recorte à mídia e à UI. Faça o cálculo novamente após resize e fonte pronta. Oculte o marcador gráfico quando ficar fora da área segura e preserve a informação no fluxo. Na versão vertical, valide posições contra o recorte real.

Para uma passagem de objeto sobre título, componha fundo, texto e recorte do objeto. Planeje o quanto o texto pode ser coberto em cada viewport e mantenha um título semântico legível. Em um match cut entre vídeo e DOM, estabeleça a mesma pose, silhueta, cor e ponto focal nos dois lados. Mostre o segundo plano após a imagem estar pronta. Evite um corte que dependa de uma espera impossível de controlar em rede lenta.

Para uma sequência curta com sticky nativo, a extensão percorrível do wrapper é sua altura menos a altura do palco. Normalize o deslocamento do topo do wrapper por essa extensão e limite o resultado a 0–1. Defina um estado estático quando a extensão não for positiva. Ligue esse progresso ao wrapper da cena para preservar o timing da demonstração quando o conteúdo ao redor mudar.
