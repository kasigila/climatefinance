/**
 * Small identity-layer interactions. No decorative motion.
 */
(function () {
  function closeMenu() {
    var wrap = document.querySelector('.main-menu-wrap');
    if (wrap) wrap.classList.remove('open');
    document.querySelectorAll('.nav-submenu-toggle').forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'false');
    });
  }

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
