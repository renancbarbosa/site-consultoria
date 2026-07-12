'use strict';
const fs = require('fs');
const path = require('path');

const BASE = path.resolve(__dirname, '..');

const BUSINESS = {"@type":["ProfessionalService","LocalBusiness"],"@id":"https://rcbseo.com.br/#business","name":"RCB Consultoria - SEO Local e Google Meu Negócio","description":"Consultoria especializada em SEO Local e Google Meu Negócio para clínicas, dentistas, profissionais de saúde, advogados e profissionais liberais em Goiânia e Brasil.","url":"https://rcbseo.com.br/","telephone":"+5562991161040","email":"contato@rcbseo.com.br","image":"https://rcbseo.com.br/renan-carvalho-barbosa-consultor-seo-local-goiania.jpg","logo":"https://rcbseo.com.br/logo.png","priceRange":"$$","founder":{"@id":"https://rcbseo.com.br/#renan"},"serviceType":["SEO Local","Google Meu Negócio","Google Business Profile","Sites otimizados para clínicas","Estratégia de presença digital"],"address":{"@type":"PostalAddress","addressLocality":"Goiânia","addressRegion":"GO","addressCountry":"BR"},"areaServed":[{"@type":"City","name":"Goiânia","containedInPlace":{"@type":"State","name":"Goiás"}},{"@type":"City","name":"Aparecida de Goiânia","containedInPlace":{"@type":"State","name":"Goiás"}},{"@type":"City","name":"Trindade","containedInPlace":{"@type":"State","name":"Goiás"}},{"@type":"City","name":"Senador Canedo","containedInPlace":{"@type":"State","name":"Goiás"}},{"@type":"Country","name":"Brasil"}],"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"}],"sameAs":["https://www.instagram.com/rcbseo"],"contactPoint":{"@type":"ContactPoint","telephone":"+5562991161040","contactType":"customer service","areaServed":"BR","availableLanguage":"Portuguese"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"3","bestRating":"5","worstRating":"1"},"review":[{"@type":"Review","author":{"@type":"Person","name":"Marcius Fleury"},"reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"reviewBody":"Serviço impecável, ágil e direto ao ponto. Um parceiro estratégico confiável que cumpre os prazos e garante a eficiência necessária para o fluxo da nossa operação. Atendimento altamente profissional. Recomendo fortemente."},{"@type":"Review","author":{"@type":"Person","name":"Laís Breitenbach Simão"},"reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"reviewBody":"Excelente trabalho de otimização do perfil Google. A consultoria ajudou minha confeitaria a aparecer muito melhor nas buscas e hoje consigo ver minha confeitaria no topo em várias pesquisas da região. O que mais gostei foi a forma clara e objetiva de explicar tudo sobre Google Meu Negócio e SEO local, sem promessas fáceis ou milagrosas."},{"@type":"Review","author":{"@type":"Person","name":"Fátima Isabel Breitenbach Simão"},"reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"reviewBody":"A consultoria que fez meu comércio local aparecer no Google Maps em Goiânia. Serviço excelente."}]};

const PERSON = {"@type":"Person","@id":"https://rcbseo.com.br/#renan","name":"Renan Carvalho Barbosa","jobTitle":"Consultor de SEO Local e Google Meu Negócio","url":"https://rcbseo.com.br/","image":"https://rcbseo.com.br/renan-carvalho-barbosa-consultor-seo-local-goiania.jpg","email":"contato@rcbseo.com.br","telephone":"+5562991161040","alumniOf":[{"@type":"EducationalOrganization","name":"FIAP"}],"knowsAbout":["SEO Local","Google Meu Negócio","Google Business Profile","Sites otimizados","Marketing digital para clínicas"]};

function isLegacyService(node) {
  if (node['@type'] !== 'Service') return false;
  const id = node['@id'] || '';
  if (!id) return true;
  if (id.endsWith('#service-nicho')) return false;
  if (id.endsWith('#service')) return true;
  return false;
}

function updateProvider(node) {
  if (node.provider && node.provider['@id'] === 'https://rcbseo.com.br/#localbusiness') {
    node.provider['@id'] = 'https://rcbseo.com.br/#business';
  }
}

const LD_RE = /<script type="application\/ld\+json">([\s\S]*?)<\/script>/g;

// ── @graph files ─────────────────────────────────────────────────────────────
const GRAPH_FILES = [
  'seo-para-dentistas/index.html',
  'seo-para-medicos/index.html',
  'seo-para-clinicas-de-estetica/index.html',
  'seo-para-clinicas-de-emagrecimento/index.html',
  'seo-para-clinicas/index.html',
  'google-meu-negocio-para-clinicas/index.html',
  'seo-local-goiania/index.html',
];

for (const rel of GRAPH_FILES) {
  const fp = path.join(BASE, rel);
  let html = fs.readFileSync(fp, 'utf8');

  html = html.replace(LD_RE, (fullMatch, jsonStr) => {
    let data;
    try { data = JSON.parse(jsonStr); } catch(e) { return fullMatch; }
    if (!data['@graph']) return fullMatch;

    // Remove legacy Service nodes
    data['@graph'] = data['@graph'].filter(n => !isLegacyService(n));

    // Update provider in remaining Service nodes
    data['@graph'].forEach(n => { if (n['@type'] === 'Service') updateProvider(n); });

    // Add canonical nodes if missing
    if (!data['@graph'].some(n => n['@id'] === 'https://rcbseo.com.br/#business')) {
      data['@graph'].push(BUSINESS);
    }
    if (!data['@graph'].some(n => n['@id'] === 'https://rcbseo.com.br/#renan')) {
      data['@graph'].push(PERSON);
    }

    return '<script type="application/ld+json">' + JSON.stringify(data) + '</script>';
  });

  fs.writeFileSync(fp, html, 'utf8');
  console.log('graph OK: ' + rel);
}

// ── /para-*/ isolated-script files ───────────────────────────────────────────
const PARA_FILES = [
  'para-advogados/index.html',
  'para-comercios-locais/index.html',
  'para-profissionais-liberais/index.html',
];

for (const rel of PARA_FILES) {
  const fp = path.join(BASE, rel);
  let html = fs.readFileSync(fp, 'utf8');

  // 1. Remove old LocalBusiness/ProfessionalService script block (and preceding HTML comment)
  html = html.replace(
    /[ \t]*<!--[^>]*(?:ProfessionalService|LocalBusiness)[^>]*-->\s*<script type="application\/ld\+json">[\s\S]*?<\/script>/,
    ''
  );

  // 2. Replace isolated Service script with @graph (Service + #business + #renan)
  html = html.replace(LD_RE, (fullMatch, jsonStr) => {
    let data;
    try { data = JSON.parse(jsonStr); } catch(e) { return fullMatch; }
    if (data['@type'] !== 'Service') return fullMatch;

    updateProvider(data);
    // Strip @context from Service node (will live under @graph)
    delete data['@context'];

    const graph = {
      "@context": "https://schema.org",
      "@graph": [data, BUSINESS, PERSON]
    };

    return '<script type="application/ld+json">' + JSON.stringify(graph) + '</script>';
  });

  fs.writeFileSync(fp, html, 'utf8');
  console.log('para  OK: ' + rel);
}

console.log('\nDone.');
