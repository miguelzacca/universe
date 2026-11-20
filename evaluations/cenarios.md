# Cenários de avaliação

Use estes casos para verificar mudanças no fluxo da skill. Controle a identidade e os fatos esperados antes de rodar. Para comparar versões, reutilize as mesmas entradas e guarde console, screenshots e destinos resolvidos.

## Casos

| Entrada | Deve entregar | Sinal de falha |
| --- | --- | --- |
| URL abreviada do Maps para empresa com duas unidades e horários diferentes | Canonicalização do link, prova da unidade, fatos correspondentes e destino comercial correto. CTA testado. | A página mistura fotos, rota ou horário entre unidades. |
| Reel de perfil oficial com conta parcialmente visível e mídia sem direitos presumidos | Correspondência pelo autor e site vinculado ou por fonte alternativa. Conceito autoral executável com mídia que possa integrar o site. | Copia o Reel ou inventa dados a partir de legenda ou snippet. |
| Produto físico com fotos próprias e vontade de usar 3D | Direção baseada em atributo do produto. Animação progressiva que ajude a demonstração. Formato estático acessível. | Um modelo 3D pesa na primeira carga e fica girando sem função ou substitui prova real. |
| Serviço de software local com breves insumos e sem vídeo | Demonstração funcional ou convincente em HTML ou mídia de prova autorizada. Evidências distinguem exemplo, proposta e fatos. | Interface falsa apresentada como prova, CTA desconectado ou vídeo decorativo obscurece a promessa. |
| Oferta visual com vídeo grande e mídia indisponível em móvel | Estados-chave alcançáveis em ambas as direções, controle de memória e requisições, poster e percurso completo sem mídia. | Área vazia, seek preso, scroll interceptado ou conteúdo dependente do vídeo. |
| Empresa de serviço local sem fotos publicáveis e com geração indisponível | Tipografia, composição e apoio licenciado ou CSS. Proposta, prova verificável e ação permanecem úteis. | Entrega apenas roteiro ou exige um briefing desnecessário para montar preview. |
| Hamburgueria pede montagem e caixa, aceita vídeo e pede uma mudança no storyboard | Pergunta de rota e ideia, guia físico do movimento, dois quadros finais coerentes e até dois de direção. Mostra preço e recebe aprovação dos quadros revisados antes de uma única geração. | Chama o provedor com trabalho pago antes da aprovação, gera de novo sem autorização, ou o vídeo termina sem ligação à ação. |
| Projeto novo recusa vídeo IA | Usa mídia própria, licenciada ou composição original. Scroll suavizado e microinterações cobrem o percurso completo. | Sem acabamento de scroll ou controles, ou chave de provedor vira dependência da página. |

## Critérios

Atribua 0 [ausente], 1 [parcial] ou 2 [verificado] a cada item.

1. Entidade, unidade e CTA certos, com fontes rastreáveis.
2. Benefício legível na abertura e prova específica no percurso.
3. Identidade coerente do hero até a ação e composição diferenciada.
4. Transformação visual com função narrativa, ritmo e acabamento observáveis.
5. Variante móvel, teclado, reduced motion e falha de mídia funcionais.
6. Direitos, origem, uso ilustrativo e decisões visuais registrados.
7. Preview editável, CTA acionável, console limpo para o fluxo e verificação reproduzível.

Use 12/14 como referência para revisão e reprove qualquer execução com CTA errado, prova inventada, mídia sem permissão adequada, perda de conteúdo em reduced motion ou bloqueio do fluxo principal. Reexecute o teste que falhou depois da correção. Um caso simulado pode verificar a lógica de produção. Busca em rede, autoplay móvel, aquisição de direitos e geração em provedores específicos precisam de testes próprios para serem declarados verificados.

Execute `python -m unittest discover -s evaluations` para verificar o contrato do cliente OpenRouter com respostas simuladas. A suíte cobre os papéis dos quadros, limite de custo, apenas um POST por registro, interrupção sem ID e download por retomada.

## Regressões de direção cinematográfica

| Pedido | Primeira prova esperada | Reprove quando |
| --- | --- | --- |
| “Crie uma página para uma oficina de cerâmica que tem três acabamentos. O visitante precisa entender a diferença antes de pedir amostras.” | Em quadros claros, a peça abre caminho à comparação. A ação e a explicação existem com o efeito desativado. | Todas as capturas mostram as mesmas informações. Só muda tamanho, opacidade ou posição de um ativo isolado. |
| “Crie abertura cinematográfica para uma visita de arquitetura. Temos uma foto da entrada e outra da sala de leitura.” | Continuidade aproximada de eixo, luz e ponto focal, com passagem da escala externa à experiência interna. Teste estático também. | Dois ativos independentes entram com fade e o conteúdo visível não explica a visita. |
| “Deixe a demo de software mais expressiva. Pode usar movimento contido.” | Arte prepara a chegada a uma tarefa do produto. O visitante encontra uma prova ou fluxo real. | Loading, partículas ou animações de entrada atrasam o conteúdo sem facilitar entendimento. |

Avalie primeiro o efeito em browser, no percurso direto e no reverso. Depois julgue a leitura sem recorrer ao briefing. Para o teste negativo, uma cena que move a foto de 1 para 1,13 de escala sobre a mesma composição deve ficar sem aprovação de transformação. O teste técnico pode verificar esse movimento. A evidência visual deve verificar seu papel na página.

Os métodos de autoria combinam núcleo curto, recursos roteados, exemplos executáveis e testes por resultado. [Criar skills no Codex](https://developers.openai.com/codex/skills/) · [Skill Creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md) · [Avaliações de skills](https://developers.openai.com/blog/eval-skills/) · [Especificação Agent Skills](https://agentskills.io/specification)
