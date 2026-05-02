'use strict';

// Ano atual no footer
document.getElementById('anoAtual').textContent = new Date().getFullYear();

// ============================================================
// NAVBAR — scroll e menu mobile
// ============================================================
const navbar = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navLinks = navMenu.querySelectorAll('.nav-link');

function handleScroll() {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
}

window.addEventListener('scroll', handleScroll, { passive: true });
handleScroll();

function toggleMenu(open) {
  const isOpen = typeof open === 'boolean' ? open : !navMenu.classList.contains('open');
  navMenu.classList.toggle('open', isOpen);
  navToggle.classList.toggle('active', isOpen);
  navToggle.setAttribute('aria-expanded', String(isOpen));
  document.body.style.overflow = isOpen ? 'hidden' : '';
}

navToggle.addEventListener('click', () => toggleMenu());

navLinks.forEach(link => {
  link.addEventListener('click', () => toggleMenu(false));
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && navMenu.classList.contains('open')) toggleMenu(false);
});

// Fechar menu ao clicar fora
document.addEventListener('click', e => {
  if (navMenu.classList.contains('open') && !navbar.contains(e.target)) toggleMenu(false);
});

// ============================================================
// ACTIVE NAV LINK — Intersection Observer por seção
// ============================================================
const sections = document.querySelectorAll('section[id]');

const sectionObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        link.classList.toggle('active', href === `#${id}`);
      });
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => sectionObserver.observe(s));

// ============================================================
// FADE-IN — Intersection Observer
// ============================================================
const fadeEls = document.querySelectorAll(
  '.servico-card, .paraquem-card, .diferencial-item, .metodo-step, .sobre-texto, .sobre-card, .contato-info, .contato-form-wrap, .section-header'
);

fadeEls.forEach(el => el.classList.add('fade-in'));

const fadeObserver = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, (entry.target.dataset.delay || 0));
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

// Adiciona delay escalonado para cards em grid
document.querySelectorAll('.servicos-grid .servico-card, .paraquem-grid .paraquem-card').forEach((el, i) => {
  el.dataset.delay = i * 80;
});

fadeEls.forEach(el => fadeObserver.observe(el));

// ============================================================
// FORMULÁRIO — validação e envio via WhatsApp
// ============================================================
const form = document.getElementById('contatoForm');

function getField(name) {
  return form.elements[name];
}

function showError(fieldName, msg) {
  const field = getField(fieldName);
  const errEl = document.getElementById(`${fieldName}-error`);
  if (field) field.classList.add('invalid');
  if (errEl) errEl.textContent = msg;
}

function clearError(fieldName) {
  const field = getField(fieldName);
  const errEl = document.getElementById(`${fieldName}-error`);
  if (field) field.classList.remove('invalid');
  if (errEl) errEl.textContent = '';
}

function validateForm() {
  let valid = true;

  clearError('nome');
  clearError('email');
  clearError('mensagem');

  const nome = getField('nome').value.trim();
  const email = getField('email').value.trim();
  const mensagem = getField('mensagem').value.trim();

  if (!nome) {
    showError('nome', 'Por favor, informe seu nome.');
    valid = false;
  } else if (nome.length < 3) {
    showError('nome', 'Nome muito curto.');
    valid = false;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email) {
    showError('email', 'Por favor, informe seu e-mail.');
    valid = false;
  } else if (!emailRegex.test(email)) {
    showError('email', 'E-mail inválido.');
    valid = false;
  }

  if (!mensagem) {
    showError('mensagem', 'Por favor, escreva sua mensagem.');
    valid = false;
  } else if (mensagem.length < 10) {
    showError('mensagem', 'Mensagem muito curta.');
    valid = false;
  }

  return valid;
}

if (form) {
  // Limpar erro ao digitar
  ['nome', 'email', 'mensagem'].forEach(name => {
    const field = getField(name);
    if (field) field.addEventListener('input', () => clearError(name));
  });

  form.addEventListener('submit', e => {
    e.preventDefault();

    if (!validateForm()) return;

    const nome = getField('nome').value.trim();
    const email = getField('email').value.trim();
    const telefone = getField('telefone').value.trim();
    const mensagem = getField('mensagem').value.trim();

    const texto = [
      `Olá Renan! Vim pelo seu site e gostaria de saber mais sobre consultoria digital.`,
      ``,
      `*Nome:* ${nome}`,
      `*E-mail:* ${email}`,
      telefone ? `*Telefone:* ${telefone}` : '',
      ``,
      `*Mensagem:*`,
      mensagem
    ].filter(l => l !== undefined).join('\n');

    const url = `https://wa.me/5562991161040?text=${encodeURIComponent(texto)}`;
    window.open(url, '_blank', 'noopener,noreferrer');

    // Feedback visual
    const btn = form.querySelector('button[type="submit"]');
    const originalHTML = btn.innerHTML;
    btn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Mensagem preparada!`;
    btn.disabled = true;
    btn.style.background = '#25D366';
    btn.style.color = '#fff';

    setTimeout(() => {
      btn.innerHTML = originalHTML;
      btn.disabled = false;
      btn.style.background = '';
      btn.style.color = '';
      form.reset();
    }, 3000);
  });
}

// ============================================================
// DROPDOWN "Para você"
// ============================================================
(function () {
  const dropToggle = document.querySelector('.nav-dropdown-toggle');
  const dropMenu   = document.querySelector('.nav-dropdown-menu');
  if (!dropToggle || !dropMenu) return;

  dropToggle.addEventListener('click', function (e) {
    e.stopPropagation();
    const isOpen = dropToggle.getAttribute('aria-expanded') === 'true';
    dropToggle.setAttribute('aria-expanded', String(!isOpen));
    dropMenu.classList.toggle('open', !isOpen);
  });

  document.addEventListener('click', function (e) {
    if (!dropToggle.contains(e.target) && !dropMenu.contains(e.target)) {
      dropToggle.setAttribute('aria-expanded', 'false');
      dropMenu.classList.remove('open');
    }
  });

  dropMenu.querySelectorAll('.nav-dropdown-item').forEach(function (item) {
    item.addEventListener('click', function () {
      toggleMenu(false);
    });
  });
})();

// ============================================================
// SMOOTH SCROLL para links âncora
// ============================================================
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    const target = document.querySelector(link.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = navbar.offsetHeight + 8;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});
