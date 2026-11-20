# Verificação e entrega

## Plano de testes

Use o browser do ambiente ou Playwright. Rode o build e a prévia de produção quando o projeto oferecer ambos. Registre navegador, largura e execução que sustentam cada observação. Capture abertura, cena de assinatura durante o efeito, prova e CTA. Guarde screenshots e trace no local de trabalho quando forem úteis para revisão.

| Percurso | Execute | Critério de aceitação |
| --- | --- | --- |
| Primeira visita | 1440×900 e telefone de 390×844, com reload frio. Repita em 320 a 360 px. | H1 e CTA principal aparecem com contraste suficiente. Poster ou mídia tem dimensões definidas. Nenhuma rolagem horizontal na página. |
| Rolagem | Use roda real ou emulada, desça devagar, fligue, pule por âncora, retorne pelo scroll e redimensione no meio da cena. | Desktop tem amortecimento perceptível e alcança o destino sem travar. Vídeo e camadas respondem ao mesmo progresso nos dois sentidos. A entrada, o fim e o retorno são previsíveis. |
| Teclado e foco | Tab e Shift+Tab desde o topo até o CTA final. Teste Escape e retorno de foco em menus ou diálogos. | O foco nunca some sob overlays, passa por controles visíveis, chega ao CTA e segue a ordem de leitura. |
| Microinterações | Percorra todos os controles por mouse, teclado e toque. Inclua headers, rodapé e controles de erro, envio ou seleção presentes. | Hover, pressão, foco e estados da ação dão retorno consistente. Redução desliga deslocamento e preserva o feedback. |
| Móvel realista | Use contexto touch, área segura, retrato, paisagem e mudança de altura da viewport. Abra menu e acione CTA. | Texto e alvos preservam espaço. A abertura responde ao navegador móvel. O visitante consegue sair de qualquer cena, teclado ou modal. |
| Movimento reduzido | Emule `prefers-reduced-motion: reduce` e recarregue, inclusive com mídia disponível. Quando possível, alterne em tempo real. | Animações intensas cedem a estado estático ou troca simples. Conteúdo, CTA e ordem continuam disponíveis. Elementos obrigatórios iniciam visíveis. |
| Rede e mídia | Frio, rede limitada e acesso à mídia bloqueado no request. Desative JS e teste a informação central. Se houver 3D, simule ausência ou perda de contexto. | O poster e o HTML fazem sentido. A oferta segue acessível. A página não apresenta intervalo vazio, overlay persistente, spinner eterno ou erro que bloqueie a ação. |
| Conversão | Abra destino oficial do CTA. Se houver formulário em ambiente de teste, valide sucesso, erro, envio duplicado e retorno. | A ação chega à unidade/canal corretos. Botões têm nome acessível. Testes de formulário usam sandbox, interceptação ou endpoint de teste. |
| Fluxo de carregamento | Revise Console, waterfall e peso transferido. Repita no preview de produção e procure long tasks durante a cena. | Cada request essencial tem sucesso. Mídia fora da primeira cena entra mais tarde. Movimentos repetidos mantêm a interação responsiva. |

Para vídeo com seek, verifique `currentTime` e o quadro visível no começo, meio e fim com tolerância explícita. Use tempos proporcionais ao intervalo de scroll daquela cena. Faça scroll reverso, simule busca rápida e confirme que o frame final chega sem enfileirar seeks. Compare a imagem final com a que abre a prova. Teste iOS Safari ou dispositivo real quando a cena depender de autoplay, seek ou viewport móvel. Se o ambiente oferecer Chromium apenas, registre esse alcance.

Para canvas ou WebGL, confira pausa fora da viewport, fallback do poster, teardown ao desmontar, nenhum listener acumulado em remontagens e limites explícitos para DPR e texturas. Compare o resultado com a versão estática no aparelho de menor capacidade previsto para o projeto.

## Orçamento e qualidade percebida

- Meça o que o visitante baixa até a primeira pintura relevante e até o primeiro CTA funcional. Como ponto de partida, orce um poster móvel de até 200 KB, JS inicial comprimido de até 150 KB e evite baixar vídeos ou 3D pesados antes de serem necessários. Ajuste o orçamento por direção, rede e plataforma, com resultado medido. Em cenas de scrub, avalie em conjunto peso, resolução, GOP e latência dos seeks.
- Use os alvos de campo no percentil 75 como norte. LCP até 2,5 s, INP até 200 ms e CLS até 0,1. Trace, Lighthouse e DevTools ajudam a diagnosticar. Uma medição laboratorial isolada não equivale aos percentis reais. [Web Vitals](https://web.dev/articles/vitals)
- Faça o hero legível ainda no poster. Verifique contraste nos quadros claro, escuro e com a entrada do texto. Revise o contraste mínimo de 4,5:1 para texto comum e 3:1 para texto grande. Para mídia informativa com fala, entregue legendas e alternativa apropriada. Disponibilize controle para pausar ou ocultar movimento automático ou contínuo quando exigido. Teste o toque e procure alvos de 44 × 44 CSS px quando houver espaço. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- Use uma hierarquia reconhecível sem efeitos. Os três primeiros segundos já precisam informar quem oferece o quê. O visitante que avança depressa precisa encontrar prova e ação. O visitante que explora precisa descobrir contexto cujo valor justifique os movimentos.
- Em última revisão, compare os estados principais com o roteiro. Verifique dominância visual, alinhamento, contraste e ritmo. Troque texto decorativo por prova útil. Se o visual depender de uma composição reconhecível de referência, revise enquadramento, hierarquia, personagem visual e motivo de transição a partir da marca.

## Página publicável

Verifique título, descrição, idioma, favicon, cartão social, headings, OG, URLs de contato, consentimento aplicável e metadados estruturados sustentados pelo conteúdo visível. Aponte canonical para a URL final quando conhecida e confira a política de indexação de preview e produção. Em negócios locais, valide nome, endereço, horário e telefone pela unidade certa. [Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/local-business)

Entregue a instrução necessária para abrir o projeto, caminho ou URL do preview, o destino da ação principal, observações de direitos ou material ilustrativo e a lista curta do que foi testado. Identifique lacunas com impacto e qualquer decisão visual ou técnica importante tomada por inferência.

## Critério visual de conclusão

Antes de chamar a página de cinematográfica, inspecione os quadros 0%, 35%, 70%, 100% e a chegada à seção seguinte. Prove os três itens pela página.

1. **Silhueta e leitura.** O primeiro olhar mostra oferta, hierarquia e ação. As camadas continuam intencionais nas larguras testadas.
2. **Transformação e informação.** Ao comparar início e revelação, um revisor consegue apontar o que mudou e dizer qual escolha, detalhe ou prova apareceu. Zoom, fade e parallax podem apoiar a transformação.
3. **Passagem de seção.** O último estado prepara de forma visível o que vem depois. A próxima prova, escolha ou CTA fica acessível com scroll normal, toque, teclado e movimento reduzido.

Quando um quadro falhar, localize o problema em conteúdo, enquadramento, arte, hierarquia, controle ou layout. Corrija de volta à origem e compare os estados afetados. Abra as imagens. Use evidência técnica e julgamento visual.

Ao revisar mobile e movimento reduzido, compare também proporção e ponto focal do elemento persistente. Um recorte com proporção preservada pode mudar a área visível. Se a peça estiver esticada, cortada no atributo decisivo ou perder identidade entre as versões, ajuste o enquadramento ou produza outro plano. Um teste de largura sem overflow pode passar mesmo com a mídia distorcida.

### Verificador local

Use [provar-cena.mjs](../scripts/provar-cena.mjs) com Playwright disponível. Passe URL, JSON e pasta de saída. Adapte o [contrato de teste](../examples/abertura/contrato.json) a seletores, propriedades e graus de mudança da sua cena. O script verifica marcos, reversão, chegada, toque, movimento reduzido, ausência de JS e destino configurado. Para alternativas em fluxo no celular, preencha **mobileSteps** na ordem esperada. Cada item usa **id** e **selector** e gera uma captura. Complete com falha do ativo de produção, visita real ao CTA e leitura visual. A opção **CHROMIUM_EXECUTABLE** permite usar um Chromium instalado.
