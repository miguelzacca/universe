# Vídeo por scroll

Use quando uma tomada dirigida puder demonstrar o produto, atravessar um espaço ou transformar a composição até a próxima ação. A mesma rota vale para vídeo captado ou licenciado. Para criar a tomada sob medida, separe a escolha inicial da aprovação do storyboard.

## 1. Escolha a rota e a ideia no chat

Em uma nova LP ou redesign cinematográfico completo, abra uma pergunta com as opções **Gerar vídeo com IA via OpenRouter** e **Construir com mídia disponível e animação própria**. Pergunte também que objeto, processo ou passagem a pessoa quer ver. Aceite a ideia já indicada e proponha uma a partir da pesquisa se ela deixar a decisão em aberto. Guarde a preferência na execução. Com resposta pendente, avance em pesquisa e no protótipo com mídia disponível.

Na segunda opção, procure primeiro material autorizado do negócio. Use busca de vídeo ou imagem para localizar estoque licenciado pelo gesto, enquadramento, luz e duração. Trate resultados do YouTube e vídeos de portfólio como referências até verificar a permissão de incorporação ou reaproveitamento. Um embed de plataforma pode exibir o conteúdo, mas um scrub preciso pede mídia que o próprio site possa servir. Se faltar uma tomada aproveitável, desenhe a cena com fotocomposição, máscaras, WebP sequenciais ou 3D. Preserve o acabamento de scroll e dos controles em qualquer rota.

## 2. Transforme o briefing numa tomada que vale um job

Cruze nicho, produtos, prova e CTA com as mídias autorizadas do negócio. Deixe o usuário orientar o gesto. A partir dele, nomeie **um sujeito**, **uma transformação principal** e **uma coisa que a seção seguinte recebe**. Escolha uma passagem com leitura própria em ida e volta. As referências ensinam como o movimento entrega o objeto. Abra as [leituras de continuidade do atlas](corpus/estudo-scroll-video.md) para escolher um mecanismo.

| O que a oferta precisa tornar visível | Quadro inicial e final | Ligação com a próxima seção |
| --- | --- | --- |
| Camadas e montagem de um hambúrguer | Ingredientes suspensos no eixo de baixo para cima → sanduíche montado dentro da caixa aberta, visto pelo mesmo ângulo. | Assente a caixa na metade da imagem reservada à oferta. Use sua pose ou recorte no card com composição, preço confirmado e pedido. |
| Encaixe entre partes de um motor | Carcaça em vista de três quartos com as peças explodidas no eixo correto → conjunto montado no mesmo suporte. | Preserve a posição da carcaça para passar à vista de detalhes ou especificação. Use render técnico verificado ou 3D controlado quando dimensões e encaixes forem prova. |
| Entrada a um espaço que se quer visitar | Vista externa identificável → visão interior voltada ao ponto de interesse. | Use o portal como guia, mantenha a altura de câmera e passe da vista final ao mapa ou à escolha. Para retratar um lugar real, priorize tomada própria ou fotografias autorizadas. |

Trave a identidade do sujeito, quantidade de peças, lados, formato, direção da luz e materiais. Escolha lente, escala, altura e eixo que a IA consiga interpolar sem trocar o produto. Reserve área de copy e defina o recorte vertical. Guarde números, marcas tipográficas, rótulos, botões e interface em HTML ou em ativos aprovados. Se a imagem for conceitual e puder ser confundida com o produto ou espaço real, identifique-a no site.

## 3. Faça um storyboard aprovável

1. Produza **dois quadros finais de direção** a partir de ativos existentes, geração de imagem ou render local. Quando faltar o enquadramento, use ImageGen ou o gerador de imagem disponível para criar primeiro o quadro que mais define o produto. Derive o outro extremo editando esse quadro ou usando-o como referência visual autorizada. Preserve eixo, lente, luz, fundo e características do objeto. Exporte imagens na mesma proporção e orientação, sem texto de interface.
2. Se o trajeto, a ordem das peças ou a emenda forem difíceis de inferir por dois extremos, faça mais um ou dois quadros de guia. Um storyboard de quatro costuma cobrir abertura, começo do gesto, revelação e chegada. Verifique escala, mãos, reflexos, número de partes, recorte mobile e onde a seção seguinte herda o objeto. Use crop e composição reais do site. Quando a identidade entre quadros falhar, ajuste os stills primeiro.
3. Mostre os quadros no chat ou por um link de preview renderizado. Escreva em uma frase o que acontece em cada um, quais atributos permanecem e como o último chega à próxima seção. Inclua a proposta de tomada, o modelo, duração, resolução, par de arquivos que será enviado e o custo estimado do único job. Pergunte **Aprovar storyboard e gerar uma tomada** ou **Ajustar os quadros antes de gerar**. Se o usuário pedir ajuste, atualize o storyboard e mostre novamente. Use a aprovação do storyboard com valor e escopo para executar o job. Se a seleção ou o custo mudar além do aprovado, apresente a mudança antes de submeter.

Os quadros intermediários servem à aprovação e à direção de tempos no prompt. O Veo recebe os papéis `first_frame` e `last_frame`. Envie outras imagens só por um recurso do modelo que possa coexistir com esses dois papéis. A API normalizada dá precedência a `frame_images` sobre `input_references`. [Campos de imagem no OpenRouter](https://openrouter.ai/docs/guides/overview/multimodal/video-generation#using-images)

## 4. Dirija a tomada no prompt

Redija para o modelo uma direção específica da cena. Use verbos físicos, posições e tempos proporcionais. Para Veo, escreva a direção em inglês e apresente ao usuário a descrição no idioma da conversa. Diga que o resultado é um plano contínuo, especifique a ação de câmera ou sua imobilidade, identifique os objetos que se movem e descreva o que assenta. O final deve ter composição de saída deliberada. Faça a rolagem e as camadas de interface no navegador. [Especificações do Veo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate)

```text
Single continuous {duration}-second shot, {aspect}, no audio.
Opening frame: {recognizable subject, visible parts, pose and negative space}.
Keep {identity, part count, sides, materials and colors}. {Lens, camera height,
direction of light and camera trajectory or locked camera}. Keep {HTML-safe
zone and mobile-safe crop} clear and stable.
0–20%: {readable initial pose and precise first movement}.
20–70%: {one physical transformation, order, axis and speed of the elements}.
70–90%: {visible proof and the subject's approach to the destination}.
90–100%: {settle into the exact end-frame scale, pose, crop and placement}.
{Prohibit only likely problems: cuts, geometry morphing, added objects,
duplicate pieces, camera drift, flicker, captions, invented logos}.
```

### Exemplo de direção para hamburgueria

**Intenção.** Mostrar a composição do sanduíche e passar o mesmo objeto à área de pedido. Use só os ingredientes e a embalagem que a pesquisa ou a pessoa confirmarem. Neste exemplo o sanduíche e a caixa são conceituais.

**Storyboard.** Sanduíche montado acima da caixa aberta, em vista de três quartos → camadas se separam verticalmente e ficam visíveis → sanduíche se recompõe no mesmo eixo e desce para a caixa → caixa aberta em repouso à direita, com a esquerda reservada ao CTA.

```text
One continuous silent 6-second tabletop shot. Locked camera at 35 degrees
with a 50 mm lens. On the right, a single burger hovers just above the open
kraft box on one vertical axis. Preserve the same bun halves, one grilled
patty, one slice of cheese and lettuce. Soft warm sidelight from camera left.
Background, box hinge and camera stay fixed.
0–15%: hold the recognizable silhouette. 15–45%: lift each layer along the same
axis, keeping order, orientation and distinct spacing. Pause briefly with
the layers visible. 45–72%: reassemble from bottom to top with each layer
intact. 72–93%: lower the burger as a unit into the box and keep it upright.
93–100%: hold the exact scale and position of the second image. Keep the left
third quiet and both burger and box inside the agreed safe crop. Stable shadows.
No cuts, zoom, ingredient swaps, morphing, people, text or extra packaging.
```

Para uma tomada mais curta, parta das camadas separadas e concentre o tempo na montagem e na descida. Se a pessoa quiser batata frita, fixe-a na caixa desde o começo ou represente-a na seção de pedido. A passagem usa a caixa do quadro final, com texto e ação conectados ao canal oficial.

## 5. Escolha, autorize e gere

- Consulte `python scripts/video-openrouter.py planejar` com a proporção, duração e resolução do storyboard. Comece pelo **Google Veo 3.1 Lite**, normalmente em 720p sem áudio. Use a menor duração compatível que mantenha a ação legível. Compare os modelos que declaram os dois papéis e o preço total da configuração. Troque se outro modelo for adequado à cena, aceitar os dois extremos e tiver custo favorável e verificável. Se o catálogo deixar a cotação em aberto, calcule pela tarifa oficial da configuração. Registre a origem do cálculo na aprovação e informe `--estimate-usd`. O catálogo e as tarifas variam. [Catálogo de vídeo](https://openrouter.ai/api/v1/videos/models) · [Veo 3.1 Lite](https://openrouter.ai/google/veo-3.1-lite)
- Use a chave `OPENROUTER_API_KEY` já configurada no ambiente. Quando faltar, indique `python scripts/video-openrouter.py configurar`. O comando usa entrada oculta e guarda a chave em `~/.universe/.env` para reutilização, fora do site e do Git. Use uma entrada de segredo da própria plataforma se disponível. A conversa serve à autorização e ao storyboard. Mantenha a chave no ambiente local e fora de mensagens, código de frontend, logs e previews.
- Prepare o prompt em UTF-8 e os dois quadros aprovados. O script aceita arquivos locais JPEG, PNG ou WebP inline e URLs HTTPS autorizadas de imagem. Prefira arquivos locais com proporção idêntica e peso reduzido. Se o provedor rejeitar o envio inline, use URLs diretas acessíveis pelo provedor em armazenamento já autorizado ou prossiga com os dois stills locais. Autorização de envio ao OpenRouter cobre os quadros aprovados. Confirme autorização distinta se for preciso transferir mídia privada para outro serviço.
- Após a aprovação, submeta **um** job e use uma trilha local por cena. Passe o teto autorizado em dólares. O helper confere o preço publicado e recusa acima do teto. O valor é uma estimativa da API. A chave nunca passa ao runtime. Evite novos posts em timeout ou falha de download e retome o mesmo ID. Se a resposta for ambígua e faltar o ID, consulte a conta antes de considerar outro job. Um clipe reprovado pode ser recuperado por recorte, reenquadramento, ponte com os quadros ou HTML. Uma geração adicional precisa de autorização.

```bash
python scripts/video-openrouter.py planejar --duration 4 --resolution 720p --aspect 16:9
python scripts/video-openrouter.py configurar
python scripts/video-openrouter.py gerar --first abertura.jpg --last chegada.jpg --prompt tomada.txt --job .universe/hero.json --max-usd 0.12
python scripts/video-openrouter.py retomar --job .universe/hero.json --output media-local/hero-master.mp4 --wait
```

O valor no exemplo ilustra uma cotação de 4 s. Use o valor aprovado e passe as mesmas opções do planejamento se mudar os padrões. Execute a partir da pasta do projeto com o caminho do script na skill. O job, a chave e o master em preparação ficam fora da pasta servida. Rode a implementação enquanto o vídeo processa. [API de envio](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request) · [API de download](https://openrouter.ai/docs/api/api-reference/video-generation/download-generated-video-content)

## 6. Leve a tomada inteira ao navegador

1. Abra o vídeo e revise primeiro, meio e último quadro em ida e volta. Compare os extremos com os aprovados e confira a continuidade, partes adicionadas, estabilidade do ponto focal, recorte móvel e leitura da prova. Se o conteúdo for informativo, confirme a precisão da demonstração. Extraia poster e quadro de chegada do arquivo aceito para fazer a emenda visual.
2. Preserve o master e prepare MP4 H.264, YUV 4:2:0, sem áudio, taxa constante e GOP curto. Comece testando 24 fps e um quadro-chave a cada 12 frames. Ajuste peso, qualidade e resolução pelo resultado em scroll real. Confira HTTP Range e resposta 206. Se o seek ficar irregular no dispositivo-alvo, derive sequência WebP do **mesmo** master e use um cache limitado. Use o recorte do mesmo vídeo ou quadros estáticos no celular quando funcionar com a composição.

```bash
ffmpeg -i hero-master.mp4 -map 0:v:0 -an -vf "fps=24,setsar=1" -c:v libx264 -pix_fmt yuv420p -crf 23 -g 12 -keyint_min 12 -sc_threshold 0 -movflags +faststart hero.mp4
ffmpeg -i hero.mp4 -frames:v 1 -c:v libwebp -quality 82 poster.webp
ffmpeg -sseof -1 -i hero.mp4 -vf reverse -frames:v 1 -c:v libwebp -quality 82 chegada.webp
```

3. Monte a cena a partir do [ensaio executável de mídia](../examples/midia/index.html). Uma única trilha de ScrollTrigger ou o driver da stack informa o progresso. Atualize seek e beats de HTML pela mesma posição. O primeiro quadro corresponde a 0%, o último decodificável a 100%. Limite a um seek ativo e conserve o alvo mais recente. Faça a saída receber o próprio quadro final no grid, num card ou na seção de prova. Mantenha oferta e CTA acessíveis no início, durante a tomada e depois dela.
4. Use Lenis para a roda de desktop quando a stack precisar de um suavizador e atualize ScrollTrigger pelo mesmo relógio. Preserve toque, teclado e âncoras, e desligue suavização e pin com movimento reduzido. Verifique rolagem lenta e rápida, retorno, troca de orientação, poster e falha do arquivo. Se o motor ou o vídeo falhar, mantenha a comparação ou demonstração compreensível em HTML. [Receitas](receitas.md) · [Verificação](verificacao.md)
