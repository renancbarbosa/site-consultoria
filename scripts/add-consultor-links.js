'use strict';
const fs = require('fs');
const path = require('path');
const BASE = path.resolve(__dirname, '..');

const SKIP_DIRS = new Set(['node_modules', '.git', 'scripts', '.playwright-mcp']);
// Página com header próprio (demo) — não recebe o menu global
const SKIP_FILES = new Set([path.join('diagnostico-gratuito', 'exemplo', 'index.html')]);

function findIndexHtml(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir)) {
    const full = path.join(dir, entry);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (SKIP_DIRS.has(entry)) continue;
      out.push(...findIndexHtml(full));
    } else if (entry === 'index.html') {
      out.push(full);
    }
  }
  return out;
}

// --- MENU: novo item entre o logo e "SEO e Site" ---
const MENU_ANCHOR = 'id="navMenu" role="list"><li class="nav-nicho-group">';
const MENU_NEW = 'id="navMenu" role="list"><li><a href="/consultor-seo-goiania/" class="nav-link">Consultor SEO</a></li><li class="nav-nicho-group">';

// --- FOOTER: novo link logo após "Consultoria SEO Local" ---
// Variante home (lista com <li>)
const FOOT_LI_ANCHOR = '<li><a href="/consultoria-seo-local/">Consultoria SEO Local</a></li>';
const FOOT_LI_NEW = FOOT_LI_ANCHOR + '<li><a href="/consultor-seo-goiania/">Consultor de SEO em Goiânia</a></li>';
// Variantes serviço e blog (nav com <a> soltos)
const FOOT_A_ANCHOR = '<a href="/consultoria-seo-local/">Consultoria SEO Local</a>';
const FOOT_A_NEW = FOOT_A_ANCHOR + '<a href="/consultor-seo-goiania/">Consultor de SEO em Goiânia</a>';

const FOOT_ALREADY = '>Consultor de SEO em Goiânia</a>';

const files = findIndexHtml(BASE);
const report = [];

for (const file of files) {
  const rel = file.replace(BASE + path.sep, '');
  let html = fs.readFileSync(file, 'utf8');
  const before = html;
  const actions = [];

  // MENU
  if (!SKIP_FILES.has(rel)) {
    if (html.includes('href="/consultor-seo-goiania/" class="nav-link"')) {
      // já tem
    } else if (html.includes(MENU_ANCHOR)) {
      html = html.replace(MENU_ANCHOR, MENU_NEW);
      actions.push('menu');
    }
  }

  // FOOTER (idempotente)
  if (html.includes(FOOT_ALREADY)) {
    // já tem o link no footer
  } else if (html.includes(FOOT_LI_ANCHOR)) {
    html = html.replace(FOOT_LI_ANCHOR, FOOT_LI_NEW);
    actions.push('footer(li)');
  } else if (html.includes(FOOT_A_ANCHOR)) {
    html = html.replace(FOOT_A_ANCHOR, FOOT_A_NEW);
    actions.push('footer(a)');
  }

  if (html !== before) {
    fs.writeFileSync(file, html, 'utf8');
    report.push(rel + ' => ' + actions.join(', '));
  } else {
    report.push(rel + ' => (sem mudanca)');
  }
}

console.log(report.sort().join('\n'));
console.log('\nTotal de arquivos: ' + files.length);
