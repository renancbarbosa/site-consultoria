'use strict';
const fs = require('fs');
const path = require('path');

const BASE = path.resolve(__dirname, '..');

const EXCLUDE_FILES = new Set([
  path.join(BASE, 'diagnostico-gratuito', 'exemplo', 'index.html'),
]);

const INLINE_INSERT =
  '<div class="footer-secondary-niches">' +
  '<p>Outros nichos atendidos: ' +
  '<a href="/para-advogados/">Advogados</a> · ' +
  '<a href="/para-comercios-locais/">Comércios locais</a> · ' +
  '<a href="/para-profissionais-liberais/">Profissionais liberais</a>' +
  '</p></div>';

function findHtmlFiles(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir)) {
    const full = path.join(dir, entry);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (['node_modules', '.git', 'scripts'].includes(entry)) continue;
      results.push(...findHtmlFiles(full));
    } else if (entry.endsWith('.html')) {
      results.push(full);
    }
  }
  return results;
}

const allFiles = findHtmlFiles(BASE);
const updated = [];
const skipped = [];

for (const file of allFiles) {
  if (EXCLUDE_FILES.has(file)) {
    skipped.push({ file, reason: 'excluded' });
    continue;
  }

  let content = fs.readFileSync(file, 'utf8');

  if (content.includes('footer-secondary-niches')) {
    skipped.push({ file, reason: 'already present' });
    continue;
  }

  if (!content.includes('<div class="footer-bottom">')) {
    skipped.push({ file, reason: 'no footer-bottom div' });
    continue;
  }

  content = content.replace(
    '<div class="footer-bottom">',
    INLINE_INSERT + '<div class="footer-bottom">'
  );

  fs.writeFileSync(file, content, 'utf8');
  updated.push(file.replace(BASE + path.sep, '').replace(/\\/g, '/'));
}

console.log('Updated (' + updated.length + '):');
updated.sort().forEach(f => console.log('  ✓', f));
if (skipped.length) {
  console.log('\nSkipped (' + skipped.length + '):');
  skipped.forEach(s => console.log('  -', s.file.replace(BASE + path.sep, '').replace(/\\/g, '/'), '(' + s.reason + ')'));
}
