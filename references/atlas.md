# Atlas visual e técnico

Selecione um **gesto a transferir**. Leia a prancha, identifique o motivo preservado, a informação revelada e o que acontece após a saída. Passe para o [contrato da cena](contrato-de-cena.md). As folhas usam tempos da gravação ou posições de navegador. Em vídeo editado, use o tempo do preview para localizar o efeito.

Use [consultar-atlas.py](../scripts/consultar-atlas.py) com o nome do caso, por exemplo **python scripts/consultar-atlas.py Torra**. O comando devolve a prancha, os tempos e os arquivos exatos para abrir. Sem argumento, lista os casos.

Para planejar **primeiro quadro, gesto e chegada** de um vídeo, consulte [as leituras de continuidade](corpus/estudo-scroll-video.md). Para recuperar um clipe ou atualizar a análise, use o [manifesto com URLs diretas e SHA-256](corpus/fontes-video.json).

## Entre pelo problema

| Se o site precisa mostrar | Abra os quadros | Decisão prática |
| --- | --- | --- |
| Um lugar em escalas diferentes | [Aroeira](visual/aroeira.jpg), [Maison](visual/profitize-0d3e243d.jpg), [Arbo](visual/arbo.jpg) | Planeje escala inicial, limiar, ponto de interesse e parada. Uma câmera dirigida pode usar mídia pré-renderizada. Escolha de unidade ou ângulo livre pode exigir interação espacial. |
| Anatomia ou propriedade do produto | [Sereno](visual/sereno.jpg), [Grau](visual/grau.jpg), [Veio](visual/profitize-159d6961.jpg) | Progrida do geral ao detalhe. Mostre uma diferença e leve a mesma forma a uma prova ou ficha acionável. |
| Um processo em estados | [Fermento](visual/fermento.jpg), [Torra](visual/torra.jpg), [DigiGo](visual/digigo.jpg) | Dê a cada fase uma pose, texto e pausa. Repita geometria e eixo quando a passagem depender de continuidade. |
| Produto funcionando com estética contida | [Prado](visual/prado.jpg), [Pátio](visual/profitize-f7d5022a.jpg) | Fundo e entrada deixam a UI em posição legível. Use a transformação para preparar uma demonstração real. |
| Portal, enquadramento ou lente | [Uvra](visual/profitize-166b0578.jpg), [Alísio](visual/profitize-de13a9d1.jpg), [Secret](visual/figma-secret.jpg) | Alinhe borda e ponto de interesse entre duas composições. Guarde o estado final para a seção seguinte. |
| Material, retrato e marca em camadas | [Tona](visual/profitize-27deeb4c.jpg), [Kromo](visual/profitize-a2902fd4.jpg), [KYVO](visual/kyvo.jpg) | Use recorte + lettering ou regra geométrica derivada do assunto. Preserve título e ação em HTML. |
| Filmes em uma grade ou dentro do título | [Figma for Motion](visual/figma-motion.jpg), [Lusco](visual/profitize-a85a9ef4.jpg) | Prepare poster e recorte por breakpoint. Carregue perto da ação, pause fora e teste modal e foco separadamente. |
| Atributos que mudam no mesmo objeto | [Sulko](visual/sulko.jpg), [Pomo](visual/profitize-21f1ea16.jpg), [Vulto](visual/profitize-4c684458.jpg) | Mostre a diferença de pose, plano, textura ou material. Escolha vídeo ou geometria pelo controle necessário. |

## Anatomia das oito LPs do portfólio

| Caso | Sistema observado | Motion confirmado no código |
| --- | --- | --- |
| [Aroeira](visual/aroeira.jpg) | Archivo, mono de dados, papel/areia, tinta e terracota, navegação discreta em palco aberto. | ScrollTrigger + canvas de 160 WebP. Progresso remapeado sincroniza capítulos, texto, sombra e navegação. |
| [Arbo](visual/arbo.jpg) | Instrument Serif / Inter, pedra, creme e oliva. Interface de exploração sobre fachada axial. | Fachada navegável com canvas e máscaras. GLB na planta e MP4 de ida/volta sincronizam mudanças de escala. |
| [Fermento](visual/fermento.jpg) | Clash Display / Gambetta / Cabinet Grotesk, farinha, vermelho, brasa e kraft. | GSAP sincroniza poses de recortes HTML/CSS, polígonos e fundos. O prato tem interação por clique e teclado. |
| [Grau](visual/grau.jpg) | Satoshi / Optician Sans, preto e osso, texto como alvo óptico, armação como máscara. | Three.js/WebGL procedural com Worker para máscaras e distâncias. O objeto atravessa as fases. |
| [Prado](visual/prado.jpg) | Newsreader / Geist, papel cinza, verde, céu e vidro. Malha editorial preserva leitura da UI. | Camadas alinham crista da paisagem ao painel funcional. Gráficos e controles em SVG/HTML. |
| [Sereno](visual/sereno.jpg) | Archivo / Geist, preto azulado e âmbar, mono de dados, frasco central. | Duas resoluções de WebP, canvas e overlays rastreados em coordenadas normalizadas. Anatomia e notas têm timelines próprias. |
| [Sulko](visual/sulko.jpg) | Krona One / Hanken Grotesk, terra, areia e letras largas. Recorte próprio para retrato. | Sticky + Lenis + RAF mapeiam grupos de WebP a tempos do filme e estados de capítulo. |
| [Torra](visual/torra.jpg) | Playfair Display / Geist / Geist Mono, cobre, kraft e oliva. Arcos reaparecem entre conteúdos. | Canvas executa 365 quadros em três faixas de filme. A passagem conecta o mostrador de torra à curva de tempo. |

Para consultar paleta, proporções e transferência de cada caso lado a lado, abra [decisões de design e motion](corpus/decisoes.md). Os números, caminhos de arquivo, decisões de carregamento e limites estão no [estudo do código](corpus/universe.md). Abra [análise dos anexos](corpus/anexos.md) para os estados dos oito clipes. Use o [inventário CSS](corpus/tokens-css.json) para valores declarados, famílias, media queries e keyframes. Consulte [regras de layout e estados](corpus/layout-e-estados-css.json) por caso, arquivo, seletor e mídia. Use [medições no navegador](corpus/tokens-renderizados.json) quando viewport, cascata e clamp afetam o valor efetivo.

## Todo o corpus

- [Índice de pranchas](corpus/indice-visual.md) liga cada vídeo e página visualmente disponível a sua imagem e fonte. Os tons amostrados incluem cenário, fotografia e interface. O inventário CSS guarda valores declarados.
- [Profitize](corpus/profitize.md) detalha 26 casos, do quadro inicial ao fim. O código de playback confirmado pertence ao catálogo público. A ficha pode atribuir a técnica da demo. Um preview isolado deixa o motor, estado interativo e responsividade em aberto.
- [Universe Digital e legado](corpus/universe.md) documenta abertura, gravura, ASCII, cards e comportamento. A versão histórica tem leitura de fonte. Os quadros de KYVO documentam sua referência visual direta.
- [Kyvo, DigiGo, Figma for Motion e WebM Secret](corpus/externos.md) registram fontes publicadas, tecnologia, estados e QA. [Sondagem dos oito deploys](corpus/runtime.md) registra comportamento e limites.
- [Inventário por clipe](corpus/inventario-quadros.json) registra os quadros decodificados. As pranchas são a leitura rápida de produção.

O acervo inclui relações de origem entre demos, reconstruções e previews. As anotações distinguem código, runtime, descrição do autor e quadro observado. Use os princípios para compor de novo. Mantenha fotos e marcas das referências nos materiais de estudo.
