# Plano pós-publicação: conversão e autoridade

Este arquivo reúne as ações que dependem de contas externas. O código do site já envia eventos consistentes; os passos abaixo precisam ser feitos nos painéis do Google e no provedor do domínio.

## 1. Google Analytics 4 — fazer no dia da publicação

1. Abra a propriedade que usa o ID `G-K644KXR38G`.
2. Acesse **Administrador > Exibição de dados > Eventos**.
3. Crie ou localize o evento `generate_lead` e marque a estrela para torná-lo um evento principal.
4. Não marque `cta_click`, `contato_whatsapp`, `contato_email` ou `contato_telefone` como conversão. Eles medem intenção; `generate_lead` mede o envio válido de formulário.
5. No relatório em tempo real, teste:
   - um clique no CTA principal da home (`cta_click` + `contato_whatsapp`);
   - um envio válido do formulário (`generate_lead`);
   - um clique em telefone e e-mail, quando existirem.
6. Aguarde até 24 horas para os relatórios padrão. Eventos em tempo real costumam aparecer antes.

Referências oficiais: [eventos principais do GA4](https://support.google.com/analytics/answer/13128484) e [evento recomendado `generate_lead`](https://support.google.com/analytics/answer/9267735).

## 2. Search Console — fazer no dia da publicação

1. Inspecione e solicite indexação para:
   - `https://rcbseo.com.br/`
   - `https://rcbseo.com.br/diagnostico-presenca-digital/`
   - `https://rcbseo.com.br/cases/`
   - as 10 páginas de cidade que já têm mais impressões.
2. Reenvie `https://rcbseo.com.br/sitemap.xml`.
3. Exporte o relatório de desempenho em 28 dias e compare por página e consulta.
4. Não crie novas páginas de cidade até identificar quais URLs já recebem impressões. O gerador agora exige `RCB_EXPANDIR_CIDADES=1` para expandir a lista de propósito.

Referência oficial: [criar e enviar sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).

## 3. Domínio antigo `renancbarbosa.com.br` — prioridade alta

O domínio antigo ainda pode aparecer no índice, mas não respondeu durante a auditoria. Isso impede uma migração adequada de sinais.

1. Renovar ou reativar o domínio antigo no registrador, se ainda estiver sob controle.
2. Configurar redirecionamento HTTP 301 de cada URL antiga para a equivalente em `https://rcbseo.com.br/`. Se não houver equivalente, redirecionar para a página temática mais próxima; não mandar tudo automaticamente para a home.
3. Validar as propriedades antiga e nova na mesma conta do Search Console.
4. Só depois dos 301 estarem funcionando, usar **Alteração de endereço** na propriedade antiga.
5. Manter os 301 por pelo menos 180 dias e, de preferência, o domínio registrado por um ano ou mais.

Referência oficial: [ferramenta Alteração de endereço](https://support.google.com/webmasters/answer/9370220?hl=pt).

## 4. Distribuição e autoridade — ciclo inicial de 30 dias

O site já tem conteúdo suficiente para teste. Agora precisa de exposição e sinais externos reais, não de novos textos em massa.

### Semana 1

- Completar o Google Perfil da Empresa e apontar o link principal para a home.
- Publicar um post no Perfil da Empresa levando ao diagnóstico, com UTM: `?utm_source=google_business_profile&utm_medium=organic&utm_campaign=diagnostico`.
- Atualizar LinkedIn e Instagram com `https://rcbseo.com.br/`.
- Pedir a clientes reais autorização para transformar resultados em estudos de caso verificáveis.

### Semana 2

- Distribuir o melhor case no LinkedIn e em contatos profissionais relevantes.
- Solicitar inclusão em associações, parceiros e diretórios locais legítimos que aceitem negócios de Goiânia.
- Corrigir nome, endereço e telefone onde houver divergência. Usar sempre: **Renan Carvalho Barbosa / RCB Consultoria**, Rua 18-A, nº 256, Goiânia-GO, (62) 99116-1040.

### Semana 3

- Publicar uma análise útil derivada de um case, apontando para a página original.
- Contatar cinco parceiros complementares — web designers, agências, contadores e consultores — propondo conteúdo conjunto ou indicação, sem compra de links.
- Responder dúvidas reais no Google Perfil da Empresa e redes sociais; transformar as recorrentes em melhorias nas páginas existentes.

### Semana 4

- Comparar no Search Console: impressões, cliques, CTR e posição por página.
- Comparar no GA4: `cta_click`, contatos e `generate_lead` por página e origem.
- Reescrever títulos e primeiras dobras das páginas com muitas impressões e CTR baixo.
- Manter, consolidar ou retirar do sitemap páginas de cidade apenas com base em dados de cobertura e desempenho.

## 5. Critério de sucesso do primeiro ciclo

- Mensuração: eventos visíveis no GA4 e `generate_lead` configurado como evento principal.
- Descoberta: crescimento de impressões e de consultas nas posições 11–30.
- Conversão: pelo menos cliques qualificados em WhatsApp/formulário, mesmo antes do primeiro contrato.
- Autoridade: novas menções ou links legítimos de parceiros, diretórios ou perfis reais.

Evitar compra de links, redes privadas, conteúdo copiado, spam em comentários e páginas locais sem evidência. Essas ações podem gerar pico curto, perda de confiança e ação manual; não corrigem o problema de oferta, rastreamento ou autoridade real.
