(function() {
  'use strict';
  var STORAGE_KEY = 'rcb_cookie_consent';
  var CONSENT_VERSION = '1';

  function getStoredConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (parsed.version !== CONSENT_VERSION) return null;
      return parsed;
    } catch (e) { return null; }
  }

  function setConsent(decision) {
    var record = { version: CONSENT_VERSION, decision: decision, timestamp: new Date().toISOString() };
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(record)); } catch (e) {}
    applyConsent(decision);
  }

  function applyConsent(decision) {
    if (typeof window.gtag !== 'function') return;
    if (decision === 'accept') {
      window.gtag('consent', 'update', {
        'analytics_storage': 'granted',
        'ad_storage': 'denied',
        'ad_user_data': 'denied',
        'ad_personalization': 'denied'
      });
    } else {
      window.gtag('consent', 'update', {
        'analytics_storage': 'denied',
        'ad_storage': 'denied',
        'ad_user_data': 'denied',
        'ad_personalization': 'denied'
      });
    }
  }

  function showBanner() {
    var banner = document.getElementById('cookie-banner');
    if (!banner) return;
    banner.hidden = false;
  }

  function hideBanner() {
    var banner = document.getElementById('cookie-banner');
    if (!banner) return;
    banner.hidden = true;
  }

  function init() {
    var stored = getStoredConsent();
    if (stored) {
      applyConsent(stored.decision);
      return;
    }
    showBanner();
    document.querySelectorAll('[data-cookie-action]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var action = btn.getAttribute('data-cookie-action');
        setConsent(action);
        hideBanner();
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.rcbReopenCookieBanner = function() {
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
    location.reload();
  };
})();
