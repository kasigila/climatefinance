/**
 * Small identity-layer interactions. No decorative motion.
 */
(function () {
  function menu() {
    return document.querySelector('.main-menu-wrap');
  }

  function closeMenu() {
    var wrap = menu();
    if (wrap) wrap.classList.remove('open');
    document.body.style.overflow = '';
    document.querySelectorAll('.nav-submenu-toggle').forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'false');
    });
  }

  function openMenu(e) {
    if (e) e.preventDefault();
    var wrap = menu();
    if (!wrap) return;
    wrap.classList.add('open');
    wrap.classList.remove('collapse');
    document.body.style.overflow = 'hidden';
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('.mobile-menu a')) {
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
