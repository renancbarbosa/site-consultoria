// Responde 410 (removida de vez) para as paginas de IPTV e apostas da divisao
// "mercados competitivos", revertida em 08/08/2026. Decisao do Renan (04/10/2026):
// avisar o Google que nao voltam. Etapa 1 do docs/plano-nichos-2026-10.md.
// Roda em TODOS os enderecos (/_routes.json = "/*") desde 05/10/2026: com a lista de caminhos no
// _routes.json, um endereco disfarçado (/%43LAUDE.md, //CLAUDE.md, /d%61ta/...) escapava da lista e o
// servidor estatico entregava o arquivo interno. Aqui o caminho e decodificado e normalizado ANTES de
// comparar. Para qualquer outro endereco o middleware so chama context.next() (custo de milissegundos).
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

// Arquivos INTERNOS do projeto (05/10/2026): o Cloudflare Pages publica a pasta inteira do repositorio,
// entao anotacoes, scripts e dados do Search Console estavam abertos (ex.: /CLAUDE.md, /data/audit/...).
// Respondem 404 como se nao existissem. Nenhuma pagina do site usa nada daqui (conferido em 05/10/2026).
// Pasta ou arquivo novo de uso interno? Acrescente aqui (o _routes.json ja cobre tudo com "/*").
const PASTAS_INTERNAS = ["/scripts", "/docs", "/data", "/reports", "/.github", "/functions"];
const ARQUIVOS_INTERNOS = new Set([
  "/CLAUDE.md",
  "/ROTEIRO-CONTEXTO.md",
  "/ROTEIRO-PUBLICACAO-EXTERNA.md",
  "/AUDITORIA-CONSULTORIA.md",
  "/package.json",
  "/package-lock.json",
  "/.gitignore",
]);

const HTML_404 = `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>Página não encontrada</title></head><body style="font-family:system-ui,sans-serif;max-width:560px;margin:15vh auto;padding:0 16px;line-height:1.6">
<h1>Página não encontrada</h1><p>O endereço que você procurou não existe neste site.</p>
<p><a href="/">Ir para a página inicial</a></p></body></html>`;

function interno(caminho) {
  if (ARQUIVOS_INTERNOS.has(caminho)) return true;
  return PASTAS_INTERNAS.some((p) => caminho === p || caminho.startsWith(p + "/"));
}

// Decodifica (inclusive codificacao dupla), troca "\" por "/", junta barras repetidas e resolve "." e "..".
function normalizar(bruto) {
  let c = bruto;
  for (let i = 0; i < 3; i++) {
    let d;
    try { d = decodeURIComponent(c); } catch (e) { break; }
    if (d === c) break;
    c = d;
  }
  const partes = [];
  for (const seg of c.replace(/\\/g, "/").split("/")) {
    if (seg === "" || seg === ".") continue;
    if (seg === "..") { partes.pop(); continue; }
    partes.push(seg);
  }
  return "/" + partes.join("/");
}

export async function onRequest(context) {
  const bruto = new URL(context.request.url).pathname;
  if (interno(normalizar(bruto))) {
    return new Response(HTML_404, {
      status: 404,
      headers: {
        "content-type": "text/html; charset=utf-8",
        "cache-control": "no-store",
        "x-robots-tag": "noindex",
      },
    });
  }
  const caminho = normalizar(bruto).replace(/\/index\.html$/, "");
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
