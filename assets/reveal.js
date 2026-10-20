// Mobile-Nav: Burger-Toggle, Body-Scroll-Lock, ✕-Icon, ESC-Close, Nav-Höhe messen
(function () {
  const nav = document.getElementById('navV3');
  if (!nav) return;
  const burger = nav.querySelector('.burger');
  if (!burger) return;

  const setNavHeight = () => {
    document.documentElement.style.setProperty('--nav-height', nav.offsetHeight + 'px');
  };
  setNavHeight();
  window.addEventListener('resize', setNavHeight);
  window.addEventListener('load', setNavHeight);

  const openMenu = () => {
    nav.classList.add('open');
    document.body.style.overflow = 'hidden';
    burger.textContent = '✕';
    burger.setAttribute('aria-expanded', 'true');
  };
  const closeMenu = () => {
    nav.classList.remove('open');
    document.body.style.overflow = '';
    burger.textContent = '☰';
    burger.setAttribute('aria-expanded', 'false');
  };

  // Inline-onclick entfernen, eigenen Handler dranhängen
  burger.onclick = null;
  burger.addEventListener('click', function (e) {
    e.preventDefault();
    nav.classList.contains('open') ? closeMenu() : openMenu();
  });

  // ESC schließt
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) closeMenu();
  });

  // Tap auf einen Link schließt (bei Hash-Links passiert sonst nichts)
  nav.querySelectorAll('a[href]').forEach(a => a.addEventListener('click', closeMenu));

  // Beim Resize auf Desktop schließen
  window.addEventListener('resize', function () {
    if (window.innerWidth > 1200 && nav.classList.contains('open')) closeMenu();
  });
})();

(function () {
  // Fallback für ältere Browser ohne IntersectionObserver: alle .reveal sofort sichtbar machen
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    return;
  }

  const selectors = [
    'section h2', 'section .lead', 'section .display', 'section h1',
    '.editorial-card', '.img-block', '.full-image', '.pullquote',
    '.chapter-mark', '.timeline-item', '.eyebrow', '.thema-card',
    '.grid-2 > *', '.grid-3 > *', '.grid-hero > *'
  ];

  // Automatische .reveal-Klasse für die Selektoren setzen
  document.querySelectorAll(selectors.join(',')).forEach(el => el.classList.add('reveal'));

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  // ALLE .reveal-Elemente beobachten (auch manuell gesetzte, z.B. Formulare)
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

  // Zusätzlicher Fallback: nach 2 Sekunden alle noch unsichtbaren .reveal zwangs-anzeigen
  // (falls Observer aus irgendeinem Grund nicht triggert, z.B. bei lang gescrollten Seiten)
  setTimeout(() => {
    document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight) el.classList.add('visible');
    });
  }, 2000);
})();
