---
name: universe
description: >-
  Build or redesign cinematic landing pages for brands, products, places, and
  services from a brief, existing project, or a Maps, Instagram, or website link.
  Use for art direction, storyboards, scroll-driven storytelling, GSAP and
  ScrollTrigger, motion with video or 3D, and verified browser previews.
metadata:
  version: "2.0.0"
---

# Universe

Entregue uma página autoral com uma cena que faça o visitante **entender, ver ou escolher algo que ainda não estava disponível no quadro inicial**. Continuidade de imagem, forma, câmera ou objeto deve conectar a cena ao próximo passo. Para construção ou redesign completo, trabalhe até provar esse resultado no navegador. Em ajustes pontuais, aplique ao escopo pedido.

## 1. Escolha o que a cena revela

Em repo existente, leia layout, stack, fontes e assets. Preserve identidade, conteúdo verificado e fluxos. Para entrada por link, confirme empresa, unidade, oferta, prova e CTA pelo [guia de marca e mídia](references/marca-e-midia.md). Avance com escolhas reversíveis. Pergunte só se sobrar ambiguidade que mude a entidade, a ação ou o acesso necessário.

Abra o [atlas visual](references/atlas.md). Escolha um caso cujo **gesto serve à oferta** e outro que esclareça composição, ritmo ou implementação. Abra as pranchas locais com a ferramenta de imagem e confira as notas de técnica. Com visão indisponível, leia o quadro comentado e registre o alcance. Os materiais já incluem tokens, sequência, decisões de produção e bibliotecas identificadas. Reabra a fonte original quando precisar resolver uma dúvida específica.

Forme uma direção visual própria a partir da marca. Use a lógica de composição, material, harmonia tipográfica e passagem entre cenas das referências. Crie uma nova silhueta, layout, mídia e copy. Consulte [direção e motion](references/direcao-e-motion.md) para decisões de grid, tipo, cor e ritmo. As pranchas do atlas são material de estudo.

## 2. Prove o trecho crítico primeiro

Preencha o [contrato da cena](references/contrato-de-cena.md). Descreva 0%, transformação, revelação e saída. Dê ao objeto, texto ou máscara posição e papel em cada estado. Defina versões móvel, reduzida e com mídia indisponível, e a ação que o visitante pode tomar depois.

Prove cedo a mecânica com o material disponível. Defina enquadramento, continuidade e procedência dos ativos finais. Use material real autorizado para produto, equipe, local e outras provas. Busque stock licenciado ou gere planos de conceito quando couber à direção e houver ferramenta e autorização. Siga [marca e mídia](references/marca-e-midia.md).

Abra a receita relevante em [implementação e componentes](references/receitas.md). Use CSS e JavaScript nativo quando sustentarem o efeito. Use GSAP e ScrollTrigger para sincronizar vários beats, pin e saída quando uma timeline ajudar. Escolha vídeo por tempo, seek, frames ou 3D conforme o controle que a cena exige. Comece do componente executável adequado e adapte suas medidas ao projeto. Preserve rolagem nativa, foco, links e HTML útil em fallback.

## 3. Termine a página e verifique em ciclos

Aplique a mesma direção à prova, às seções e ao CTA. Harmonize as passagens. Use a rotina local da stack do projeto e mantenha a entrega em preview privado ou local quando o pedido não autorizar publicação.

Execute [verificação](references/verificacao.md). Capture 0%, transformação, revelação, saída e chegada à seção seguinte no desktop. Capture também a ordem e o recorte equivalentes no celular. Examine as imagens como quadros de uma edição. Teste avanço, reversão, flique ou salto, preferência reduzida, teclado e falha de mídia. Confirme o destino comercial pelo caminho real sem enviar dados reais. Use o [verificador Playwright](scripts/provar-cena.mjs) quando disponível. Ele mede estados. Faça também a leitura visual e comercial.

**Critério de conclusão.** A cena principal passa quando os quadros mostram uma transformação e uma entrega visíveis, vinculadas à oferta, e o percurso funciona nos modos exigidos. Testes de deslocamento, opacidade ou presença de animação por si só deixam a cena sem comprovação. Se a passagem continuar genérica, volte a enquadramento, arte, hierarquia ou estrutura. Corrija e recapture antes da entrega. Se houver dependência bloqueada, entregue a melhor alternativa funcional executável e diga qual evidência ficou pendente.

Entregue código editável, preview, destino da ação e a evidência do que funcionou. Use [prompts](prompts/prompts.md) para chamadas reutilizáveis e [avaliações](evaluations/cenarios.md) para testar a skill em outras entradas.
