'use strict';
const fs = require('fs');
const path = require('path');

const BASE = path.resolve(__dirname, '..');
const BASE_URL = 'https://rcbseo.com.br';

// ─── Helpers ────────────────────────────────────────────────────────────────

/** Normalize any internal href to an absolute path like "/sobre/" */
function normalizeHref(href, pageSlug) {
  if (!href) return null;
  href = href.trim();
  // Strip full domain
  href = href.replace(/^https?:\/\/rcbseo\.com\.br/, '');
  // Strip fragment and query
  href = href.replace(/[?#].*$/, '');
  // Relative: make absolute using page slug
  if (!href.startsWith('/')) {
    const dir = pageSlug.endsWith('/') ? pageSlug : pageSlug.replace(/\/[^/]+$/, '/');
    href = dir + href;
  }
  // Remove trailing .html for clean comparison
  href = href.replace(/\.html$/, '');
  // Ensure trailing slash on directory-style paths
  if (!href.endsWith('/') && !href.includes('.')) href += '/';
  return href || '/';
}

/** Is this href internal? */
function isInternal(href) {
  if (!href) return false;
  return href.startsWith('/') || href.startsWith(BASE_URL);
}

/** Map file path → canonical slug like "/sobre/" */
function fileToSlug(filePath) {
  const rel = filePath.replace(BASE + path.sep, '').replace(/\\/g, '/');
  if (rel === 'index.html') return '/';
  if (rel.endsWith('/index.html')) return '/' + rel.replace('/index.html', '') + '/';
  // e.g. para-clinicas.html → /para-clinicas/
  return '/' + rel.replace(/\.html$/, '') + '/';
}

// ─── HTML Stripping ──────────────────────────────────────────────────────────

/**
 * Remove blocks we must IGNORE for contextual link counting:
 * <nav>, <footer>, breadcrumb <ol>, #cookie-banner, <script type=ld+json>
 * Returns stripped HTML with only the <main> body kept.
 */
function extractContextualHtml(html) {
  // Keep only what's inside <main>...</main>
  const mainMatch = html.match(/<main[\s\S]*?<\/main>/i);
  if (!mainMatch) return '';
  let main = mainMatch[0];

  // Remove breadcrumb nav (nav.breadcrumb or ol.breadcrumb/nav aria-label breadcrumb)
  main = main.replace(/<nav[^>]*breadcrumb[\s\S]*?<\/nav>/gi, '');
  main = main.replace(/<ol[^>]*breadcrumb[\s\S]*?<\/ol>/gi, '');
  main = main.replace(/<nav[^>]*aria-label="Breadcrumb"[\s\S]*?<\/nav>/gi, '');
  // Remove any nested <nav> inside main (sub-menus etc.)
  main = main.replace(/<nav[\s\S]*?<\/nav>/gi, '');
  // Remove cookie banner
  main = main.replace(/<div[^>]*id="cookie-banner"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/gi, '');
  // Remove ld+json scripts
  main = main.replace(/<script[^>]*type="application\/ld\+json"[\s\S]*?<\/script>/gi, '');

  return main;
}

/** Extract all <a href> from HTML string */
function extractLinks(html) {
  const links = [];
  const re = /<a\s[^>]*href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    const href = m[1];
    // Anchor text: strip inner tags
    const anchor = m[2].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
    links.push({ href, anchor });
  }
  return links;
}

// ─── Main ────────────────────────────────────────────────────────────────────

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

const EXCLUDE = new Set(['/', '/404/', '/diagnostico-gratuito/exemplo/']);

const allFiles = findHtmlFiles(BASE);
const pages = {};  // slug → { file, outbound: [{to, anchor}], inbound: [{from, anchor}] }

// Pass 1: build slug map and collect outbound links
for (const file of allFiles) {
  const slug = fileToSlug(file);
  if (EXCLUDE.has(slug)) continue;
  const html = fs.readFileSync(file, 'utf8');
  const contextual = extractContextualHtml(html);
  const rawLinks = extractLinks(contextual);

  const outbound = [];
  for (const { href, anchor } of rawLinks) {
    if (!isInternal(href)) continue;
    const normalized = normalizeHref(href, slug);
    if (!normalized || normalized === slug) continue; // skip self-links
    outbound.push({ to: normalized, anchor });
  }

  pages[slug] = { file: file.replace(BASE + path.sep, '').replace(/\\/g, '/'), outbound, inbound: [] };
}

// Pass 2: build inbound from outbound
for (const [fromSlug, data] of Object.entries(pages)) {
  for (const { to, anchor } of data.outbound) {
    if (pages[to]) {
      pages[to].inbound.push({ from: fromSlug, anchor });
    }
  }
}

// Build report
const report = {};
for (const [slug, data] of Object.entries(pages)) {
  report[slug] = {
    file: data.file,
    inbound_count: data.inbound.length,
    outbound_count: data.outbound.length,
    inbound: data.inbound,
    outbound: data.outbound,
  };
}

const outPath = path.join(__dirname, 'interlinking-report.json');
fs.writeFileSync(outPath, JSON.stringify(report, null, 2), 'utf8');
console.log('Report written to ' + outPath);
console.log('Pages analyzed: ' + Object.keys(report).length);
