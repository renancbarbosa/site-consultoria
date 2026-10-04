// Responde 410 (removida de vez) para as paginas de IPTV e apostas da divisao
// "mercados competitivos", revertida em 08/08/2026. Decisao do Renan (04/10/2026):
// avisar o Google que nao voltam. Etapa 1 do docs/plano-nichos-2026-10.md.
// So roda nos enderecos listados em /_routes.json; o resto do site e estatico.
const REMOVIDAS = new Set([
  "/blog/backlinks-para-iptv-funcionam",
  "/blog/como-criar-paginas-de-avaliacao-de-casas-de-apostas",
  "/blog/como-criar-site-para-afiliado-de-apostas",
  "/blog/como-criar-site-para-iptv-do-zero",
  "/blog/como-posicionar-portal-de-jogos-online",
  "/blog/conteudo-autoridade-conversao-sites-de-apostas",
  "/blog/dominio-novo-ou-expirado-para-iptv",
  "/blog/estruturar-site-iptv-para-gerar-contatos",
  "/blog/iptv-primeira-pagina-3-4-meses",
  "/blog/link-building-para-bets-o-que-avaliar",
  "/blog/quanto-custa-seo-para-iptv",
  "/blog/quanto-custa-seo-para-sites-de-apostas",
  "/blog/quanto-investir-backlinks-iptv",
  "/blog/quanto-tempo-para-posicionar-uma-bet",
  "/blog/quanto-tempo-posicionar-site-iptv",
  "/blog/seo-nacional-para-iptv-o-que-muda",
  "/blog/seo-para-cassino-online-desafios",
  "/blog/site-para-revendedor-iptv-o-que-precisa-ter",
  "/criacao-de-site-para-afiliado-de-bet",
  "/criacao-de-site-para-iptv",
  "/dominio-expirado-para-iptv",
  "/link-building-para-bets",
  "/link-building-para-iptv",
  "/seo-para-afiliados-de-apostas",
  "/seo-para-bets",
  "/seo-para-iptv",
  "/seo-para-jogos-online",
  "/seo-para-revendedor-iptv"
]);

const HTML = `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>Página removida</title></head><body style="font-family:system-ui,sans-serif;max-width:560px;margin:15vh auto;padding:0 16px;line-height:1.6">
<h1>Esta página foi removida</h1><p>Este conteúdo não faz mais parte do site.</p>
<p><a href="/">Ir para a página inicial</a></p></body></html>`;

export async function onRequest(context) {
  const caminho = new URL(context.request.url).pathname
    .replace(/\/index\.html$/, "")
    .replace(/\/+$/, "");
  if (REMOVIDAS.has(caminho)) {
    return new Response(HTML, {
      status: 410,
      headers: {
        "content-type": "text/html; charset=utf-8",
        "cache-control": "no-store",
        "x-robots-tag": "noindex",
      },
    });
  }
  return context.next();
}
