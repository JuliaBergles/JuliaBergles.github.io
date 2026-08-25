// Mobile-Nav: Klick auf ein Dropdown-Label toggelt das Untermenü
(function () {
  document.addEventListener('click', function (e) {
    const link = e.target.closest('.nav-v3 .has-dropdown > .nav-link');
    if (!link) return;
    const parent = link.parentElement;
    // Nur im mobilen Zustand (wenn Nav "open" ist) toggeln
    if (!document.getElementById('navV3') || !document.getElementById('navV3').classList.contains('open')) return;
    e.preventDefault();
    e.stopPropagation();
    // Andere geöffnete Dropdowns zuklappen
    parent.parentElement.querySelectorAll('.has-dropdown.open').forEach(function (li) {
      if (li !== parent) li.classList.remove('open');
    });
    parent.classList.toggle('open');
  });
})();

(function () {
  if (!('IntersectionObserver' in window)) return;

  const selectors = [
    'section h2', 'section .lead', 'section .display', 'section h1',
    '.editorial-card', '.img-block', '.full-image', '.pullquote',
    '.chapter-mark', '.timeline-item', '.eyebrow', '.thema-card',
    '.grid-2 > *', '.grid-3 > *', '.grid-hero > *'
  ];

  const els = document.querySelectorAll(selectors.join(','));
  els.forEach(el => el.classList.add('reveal'));

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  els.forEach(el => obs.observe(el));
})();
