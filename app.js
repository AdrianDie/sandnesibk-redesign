/* Sandnes IBK – meny, scroll-reveal og samtykke-banner */

// Mobilmeny
(function () {
  var btn = document.querySelector('.menu-btn');
  var drawer = document.getElementById('drawer');
  var scrim = document.querySelector('.scrim');
  var close = document.querySelector('.drawer-close');
  if (!btn || !drawer) return;
  function setOpen(open) {
    drawer.classList.toggle('open', open);
    scrim.hidden = false;
    requestAnimationFrame(function () { scrim.classList.toggle('open', open); });
    drawer.setAttribute('aria-hidden', String(!open));
    btn.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) close.focus();
  }
  btn.addEventListener('click', function () { setOpen(true); });
  close.addEventListener('click', function () { setOpen(false); btn.focus(); });
  scrim.addEventListener('click', function () { setOpen(false); });
  drawer.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && drawer.classList.contains('open')) setOpen(false); });
})();

// Scroll-reveal (threshold 0 så høye elementer også trigges)
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
})();

// Samtykke-banner (samme tekst og valg som originalen på sandnesibk.no)
(function () {
  var KEY = 'sibk_cookie_consent';
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, JSON.stringify({ value: v, date: new Date().toISOString() })); } catch (e) {} }

  var chevron = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M5.2 8l4.8 4.8L14.8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var el;

  function build() {
    el = document.createElement('aside');
    el.className = 'cookies';
    el.setAttribute('aria-label', 'Informasjonskapsler');
    el.innerHTML =
      '<h2>Vi bruker informasjonskapsler</h2>' +
      '<p>Dette nettstedet bruker informasjonskapsler for å forbedre brukeropplevelsen.</p>' +
      '<p>Se vår <a href="cookies.html">informasjonskapselpolicy</a> for mer informasjon.</p>' +
      '<div class="cookies-actions">' +
        '<button type="button" class="btn btn--line" data-c="essentials">Kun nødvendige</button>' +
        '<button type="button" class="btn btn--ink" data-c="all">Godta alle</button>' +
      '</div>' +
      '<button type="button" class="cookies-toggle" aria-expanded="false" aria-controls="cookies-panel"><span>Tilpass</span>' + chevron + '</button>' +
      '<div class="cookies-panel" id="cookies-panel" hidden>' +
        '<label class="cookies-cat"><input type="checkbox" checked disabled><span><strong>Nødvendige informasjonskapsler</strong>' +
        'Det finnes noen informasjonskapsler som vi må inkludere for at enkelte nettsider skal fungere. Av den grunn krever de ikke ditt samtykke.</span></label>' +
        '<button type="button" class="cookies-more" aria-expanded="false">Flere detaljer</button>' +
        '<ul class="cookies-defs" hidden><li><p class="n">sibk_cookie_consent</p><p>1 år</p><p>Brukes til å lagre brukerens samtykkeinnstillinger for informasjonskapsler.</p></li></ul>' +
        '<button type="button" class="btn btn--ink" data-c="custom">Lagre innstillinger</button>' +
      '</div>';
    document.body.appendChild(el);

    el.querySelectorAll('[data-c]').forEach(function (b) {
      b.addEventListener('click', function () { set(b.getAttribute('data-c')); hide(); });
    });
    var toggle = el.querySelector('.cookies-toggle');
    var panel = el.querySelector('.cookies-panel');
    toggle.addEventListener('click', function () {
      var open = panel.hidden;
      panel.hidden = !open;
      toggle.setAttribute('aria-expanded', String(open));
    });
    var more = el.querySelector('.cookies-more');
    var defs = el.querySelector('.cookies-defs');
    more.addEventListener('click', function () {
      defs.hidden = !defs.hidden;
      more.setAttribute('aria-expanded', String(!defs.hidden));
    });
  }
  function show() { if (!el) build(); el.hidden = false; }
  function hide() { if (el) el.hidden = true; }

  document.querySelectorAll('.cookie-reopen').forEach(function (b) { b.addEventListener('click', show); });
  if (!get()) show();
})();
