/**
 * Small identity-layer interactions. No decorative motion.
 */
(function () {
  function menu() {
    return document.querySelector('.main-menu-wrap');
  }

  function nav() {
    return document.querySelector('.header-wrap .navbar');
  }

  function toBody() {
    var wrap = menu();
    if (wrap && wrap.parentElement !== document.body) {
      document.body.appendChild(wrap);
    }
  }

  function toHeader() {
    var wrap = menu();
    var host = nav();
    if (wrap && host && wrap.parentElement === document.body) {
      host.appendChild(wrap);
    }
  }

  function closeMenu() {
    var wrap = menu();
    if (wrap) wrap.classList.remove('open');
    document.body.classList.remove('acf-nav-open');
    document.body.style.overflow = '';
    document.querySelectorAll('.nav-submenu-toggle').forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'false');
    });
    toHeader();
  }

  function openMenu(e) {
    if (e) e.preventDefault();
    if (!window.matchMedia('(max-width: 991px)').matches) return;
    toBody();
    var wrap = menu();
    if (!wrap) return;
    wrap.classList.add('open');
    wrap.classList.remove('collapse');
    document.body.classList.add('acf-nav-open');
    document.body.style.overflow = 'hidden';
  }

  window.addEventListener('resize', function () {
    if (!window.matchMedia('(max-width: 991px)').matches) closeMenu();
  });

  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('.mobile-menu a, .mobile-menu')) {
      openMenu(e);
      return;
    }
    if (e.target.closest && e.target.closest('.menu-close')) {
      closeMenu();
      if (e.preventDefault) e.preventDefault();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });

  document.addEventListener('click', function (e) {
    var link = e.target.closest && e.target.closest('.main-menu-wrap .navbar-nav a.nav-link');
    if (!link) return;
    if (window.matchMedia('(max-width: 991px)').matches) {
      if (link.classList.contains('nav-link-parent')) return;
      closeMenu();
    }
  });
})();
