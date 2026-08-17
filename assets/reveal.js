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
