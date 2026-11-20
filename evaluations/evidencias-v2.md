# Evidências da revisão 2.0

## Corpus

- A extração indexou 25.241 quadros de 35 arquivos, preservando timestamp e ordem. Cada quadro tem miniatura de 192 px no acervo. Diferença de luminância ajuda a localizar passagens. A leitura narrativa humana fica nas seleções e nas notas do atlas.
- A skill contém 39 pranchas. Incluem os oito anexos, 26 clipes únicos da Profitize, o WebM Secret e quatro páginas navegadas. O legado da Universe Digital tem estudo por CSS, HTML e JS distribuídos. [Índice de pranchas](../references/corpus/indice-visual.md)
- O inventário leu 24 folhas CSS e registrou 1.978 regras relevantes de layout e estados. As 24 amostras de Chromium documentam valores efetivos em larguras de 1440 e 390 px. [Inventário CSS](../references/corpus/tokens-css.json) · [Layout e estados](../references/corpus/layout-e-estados-css.json) · [Valores renderizados](../references/corpus/tokens-renderizados.json)

## Ensaios executados

| Mecanismo | Resultado em Chromium |
| --- | --- |
| Abertura nativa e ScrollTrigger | Marcos 0%, 35%, 70% e saída. Verificação de recorte e revelação. Reversão ao quadro intermediário. Chegada à seção seguinte, CTA por toque, preferência reduzida e página sem JS. |
| Controle de regressão | Uma variante preservou a entrada e aplicou zoom contínuo ao objeto. Reprovou no marco de abertura da composição, antes da aceitação de revelação e saída. |
| Vídeo controlado por scroll | Intervalo avançou de 0 s a 2,641 s, voltou a 0,630 s e chegou ao último quadro validado, 2,958 s. Poster e ação disponíveis com MP4 bloqueado. Em redução, arquivo removido. Servidor local respondeu HTTP 206 e Content-Range. |
| Sequência controlada por scroll | Canvas chegou aos índices exatos 0, 23, 62, 13 e 71, incluindo reversão. Em redução, o canvas foi ocultado. |
| Objeto 3D | O canvas só apareceu depois da ação explícita. O botão atualizou a perspectiva e o estado acessível. A perda de contexto devolveu o poster. |
| Acervo de quadros | O navegador carregou as 35 referências e acessou o fim de todas por loopback. A leitura de arquivos também verificou integridade dos 228 mosaicos. |

As capturas suportam o exame de hierarquia e passagem. Os ensaios mecânicos de laboratório usam Chromium com mídia original e pequenos arquivos. Equipamentos reais, Safari e disponibilidade de mídia comercial dependem de testes no projeto de produção. [Quadros do ensaio de abertura](prova-abertura.jpg)

## Prova independente com outro briefing

Um agente recebeu a skill e um briefing curto de uma oficina fictícia de luminárias. Usou a continuidade de sujeito observada em Fermento e a chegada do recorte à próxima seção observada em Veio. O resultado manteve o contorno da peça, revelou a fibra depositada e apresentou dois níveis de brilho. O recorte de saída reapareceu na seção seguinte como comparação. As versões móveis e reduzidas apresentaram os três estados em fluxo. O teste percorreu o pedido simulado por toque e teclado com bloqueio de mídia. [Fermento](../references/visual/fermento.jpg) · [Veio](../references/visual/profitize-159d6961.jpg)

A primeira rodada técnica passou embora parte da mídia estivesse deformada no celular. A inspeção de capturas revelou o problema, a proporção foi corrigida e os testes foram repetidos. A verificação da skill agora pede comparação explícita de proporção e ponto focal entre modos. [Quadros do teste independente](prova-nascente.jpg)
