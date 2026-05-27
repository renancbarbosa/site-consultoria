'use strict';
const fs = require('fs');
const path = require('path');

const NEW_BLOCK =
  '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n' +
  '  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">\n' +
  '  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">\n' +
  '  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n' +
  '  <link rel="manifest" href="/site.webmanifest">';

const PATTERN = /<link rel="icon" type="image\/svg\+xml" href="[^"]*favicon\.svg">/g;

function findHtml(dir, results) {
  results = results || [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'node_modules') continue;
      findHtml(full, results);
    } else if (entry.name.endsWith('.html')) {
      results.push(full);
    }
  }
  return results;
}

const BASE = path.resolve(__dirname, '..');
const files = findHtml(BASE);
let updated = 0, skipped = 0;
const log = [];

for (const f of files) {
  const original = fs.readFileSync(f, 'utf8');
  PATTERN.lastIndex = 0;
  if (!PATTERN.test(original)) { skipped++; continue; }
  PATTERN.lastIndex = 0;
  const replaced = original.replace(PATTERN, NEW_BLOCK);
  if (replaced !== original) {
    fs.writeFileSync(f, replaced, 'utf8');
    updated++;
    log.push(f.replace(BASE + path.sep, ''));
  }
}

console.log('Updated: ' + updated + '  Skipped (no favicon link): ' + skipped);
log.forEach(function(l) { console.log('  ' + l); });
