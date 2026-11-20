# Sondagem dos oito deploys da Universe Digital

Usei Playwright e Chromium 156 em 1440 × 900 e 390 × 844. O contexto estreito simulou viewport móvel e toque. Para cada URL e modo de movimento, coletei resposta inicial, viewport, fontes declaradas, títulos, elementos de mídia e possíveis excessos horizontais. Percorri 11 posições, incluindo o final e o retorno de 100% a 26%. Total de 32 sessões e 352 amostras de posição. A sondagem mede presença, estado e navegação por scroll. O teste de ações comerciais reais está fora deste recorte.

| Projeto | Fontes declaradas no navegador | Observação do deploy |
| --- | --- | --- |
| [Arbo](https://universedigital.com.br/portfolio/arbo) | Instrument Serif, Inter | A fachada e a área de máscara aparecem como canvas. Os controles dos andares têm rótulos com unidade, área e estado. Dois elementos de vídeo no DOM ficaram sem `currentSrc` nas amostras de rolagem. A leitura de código localiza seu uso em um fluxo acionado pela seleção da cobertura. |
| [Aroeira](https://universedigital.com.br/portfolio/aroeira) | Archivo Variable, JetBrains Mono Variable | O palco inicial em canvas aparece nos dois tamanhos. A área de reserva oferece formulário e ação local. A composição mobile muda a relação entre palco, texto de apoio e bloco de reserva. |
| [Fermento](https://universedigital.com.br/portfolio/fermento) | Clash Display, Gambetta, Cabinet Grotesk | Nenhum elemento de vídeo foi encontrado. A área de cardápio expõe ação de girar prato. A abertura mostra uma contagem temática de fermentação enquanto carrega. |
| [Grau](https://universedigital.com.br/portfolio/grau) | Satoshi, Optician Sans | Um palco permanece presente ao longo da rolagem. O primeiro clique no seletor de armação excedeu o timeout de 3 s no contexto móvel enquanto a abertura estava sobre a cena. A leitura de código e os quadros anexados sustentam a análise da ótica. |
| [Prado](https://universedigital.com.br/portfolio/prado) | Newsreader Variable, Geist Variable, Geist Mono Variable | Nenhum elemento de vídeo foi encontrado. O salto visual até o produto no móvel expôs controles Pix, Boleto, Copiar e Agendar. A área de demonstração está em HTML. |
| [Sereno](https://universedigital.com.br/portfolio/sereno) | Archivo Variable, Geist Variable, Geist Mono Variable | A sondagem encontrou canvas no mergulho. A extensão rolável inicial em movimento reduzido caiu de 14.059 para 12.079 px em desktop, e de 13.215 para 11.358 px no móvel. A diferença é compatível com a redução de trilhas animadas identificada no código. |
| [Sulko](https://universedigital.com.br/portfolio/sulko) | Krona One, Hanken Grotesk Variable | O palco em canvas permaneceu central em boa parte do percurso. A seção de variante expôs três nomes de acabamento. Em outro acesso móvel, a abertura apareceu antes da cena de condução. |
| [Torra](https://universedigital.com.br/portfolio/torra) | Geist Variable, Playfair Display Variable, Geist Mono Variable | A sondagem encontrou a composição em canvas e nenhum elemento de vídeo. Em novo acesso móvel, um indicador de temperatura deu lugar à abertura. |

As oito rotas responderam HTTP 200 e tiveram zero excesso de largura do documento na primeira leitura em ambos os contextos. Os oito HTML contêm `noindex, follow`, adequado à política de demonstração do portfólio no momento observado. A skill orienta a decidir indexação e canonical conforme a finalidade real da publicação.

## Aberturas e variação no tempo

Novos acessos estreitos em seis páginas amostraram elementos no centro e camadas de abertura em 1,5 s, 5,5 s e 14 s após `DOMContentLoaded`. Os acessos foram paralelos e rodaram no Chromium do ambiente, com SwiftShader autorizado. Os tempos descrevem aquelas sessões e variam com rede, cache e execução.

- Arbo e Sereno já expunham seus palcos principais na amostra de 5,5 s.
- Fermento e Sulko ainda tinham camadas de abertura na amostra de 5,5 s e expunham o conteúdo em 14 s.
- Em Torra a camada de carregamento estava desaparecendo na amostra de 14 s.
- Em Grau a camada de carregamento permanecia visível na amostra de 14 s. A auditoria não atribui a espera a um subsistema específico. O teste desta sessão comprova a utilidade de detectar inicialização demorada e manter uma rota acessível à oferta durante falhas.

As sondagens não mediram Core Web Vitals de campo, Safari/iOS real, todas as combinações de interação ou finalização de formulário. Compare implementação, PNG capturado, DOM e registro do projeto conforme a pergunta. Os achados de preload, modos reduzidos e custo de ativos informam os casos de verificação da skill. [Código e dados do portfólio](universe.md) · [Quadros das prévias](anexos.md)
