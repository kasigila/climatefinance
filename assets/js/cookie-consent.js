(function () {
  'use strict';
  var KEY = 'acf_cookie_consent';

  function loadGetButton() {
    if (window.__acfGetButtonLoaded) return;
    window.__acfGetButtonLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://static.getbutton.io/widget/bundle.js';
    s.onload = function () {
      if (typeof GetButton === 'function') {
        GetButton('on', {
          contactform: true,
          whatsapp: '+255 754 763 558',
          call_to_action: 'Message us',
          button_color: '#40865b',
          position: 'right',
          order: 'whatsapp,contactform'
        });
      }
    };
    document.body.appendChild(s);
  }

  function accept() {
    try { localStorage.setItem(KEY, 'accepted'); } catch (e) {}
    var el = document.getElementById('cookie-consent');
    if (el) el.remove();
    loadGetButton();
  }

  function decline() {
    try { localStorage.setItem(KEY, 'declined'); } catch (e) {}
    var el = document.getElementById('cookie-consent');
    if (el) el.remove();
  }

  function showBanner() {
    if (document.getElementById('cookie-consent')) return;
    var banner = document.createElement('div');
    banner.id = 'cookie-consent';
    banner.className = 'cookie-consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.innerHTML =
      '<div class="cookie-consent-inner">' +
        '<p>We use cookies and third-party widgets (WhatsApp chat) to improve your experience. ' +
        'See our <a href="privacy-policy.php.html">Privacy Policy</a>.</p>' +
        '<div class="cookie-consent-actions">' +
          '<button type="button" class="cookie-consent-btn cookie-consent-decline">Decline</button>' +
          '<button type="button" class="cookie-consent-btn cookie-consent-accept">Accept</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);
    requestAnimationFrame(function () { banner.classList.add('is-visible'); });
    banner.querySelector('.cookie-consent-accept').addEventListener('click', accept);
    banner.querySelector('.cookie-consent-decline').addEventListener('click', decline);
  }

  function init() {
    var stored = '';
    try { stored = localStorage.getItem(KEY) || ''; } catch (e) {}
    if (stored === 'accepted') {
      loadGetButton();
      return;
    }
    if (stored === 'declined') return;
    showBanner();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
