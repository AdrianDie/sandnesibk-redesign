"""Bygger alle sider for Sandnes IBK-redesignet med felles header/footer.
Kjør: python build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
ORIG = "https://sandnesibk.no"

NAV = [
    ("index.html", "Hjem"),
    ("treningstider.html", "Treningstider"),
    ("medlem.html", "Medlem"),
    ("elite.html", "Elite"),
    ("klubben.html", "Klubben"),
    ("sponsorer.html", "Sponsorer"),
    ("kontakt.html", "Kontakt"),
]

ARROW = '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21h3.1z"/></svg>'
IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'


def social(extra=""):
    return (f'<div class="social {extra}">'
            f'<a href="https://www.facebook.com/sandnesibk" target="_blank" rel="noopener" aria-label="Sandnes IBK på Facebook">{FB}</a>'
            f'<a href="https://www.instagram.com/sandnesibk/" target="_blank" rel="noopener" aria-label="Sandnes IBK på Instagram">{IG}</a>'
            '</div>')


def nav_links(current):
    return "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV
    )


def page(fname, title, desc, body):
    full_title = "Sandnes IBK" if fname == "index.html" else f"{title} | Sandnes IBK"
    html = f"""<!doctype html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0D0D0F">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="index.html" aria-label="Sandnes IBK, til forsiden"><img src="assets/logo-header.png" alt="Sandnes IBK" width="400" height="126"></a>
    <nav class="main-nav" aria-label="Hovedmeny">{nav_links(fname)}</nav>
    <a class="btn btn--ink nav-cta" href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">Bli medlem</a>
    <button class="menu-btn" type="button" aria-label="Åpne meny" aria-expanded="false" aria-controls="drawer">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>
<div class="scrim" hidden></div>
<aside class="drawer" id="drawer" aria-label="Meny" aria-hidden="true">
  <div class="drawer-top">
    <button class="drawer-close" type="button" aria-label="Lukk meny">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav aria-label="Mobilmeny">{nav_links(fname)}</nav>
  <a class="btn btn--neon" href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">Bli medlem {ARROW}</a>
  <div class="drawer-contact">
    <p>E-post: <a href="mailto:post@sandnesibk.no">post@sandnesibk.no</a><br>Daglig leder: <a href="tel:+4798829125">988 29 125</a></p>
    {social()}
  </div>
</aside>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="footer-logo" href="index.html"><img src="assets/logo-header.png" alt="Sandnes IBK" width="400" height="126" loading="lazy"></a>
        <p>Sandnes Innebandyklubb<br>Postadresse: Diamantveien 16, 4321 Sandnes<br>Org.nr: 983 729 096 · Vipps: 125960</p>
        {social()}
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="mailto:post@sandnesibk.no">post@sandnesibk.no</a></li>
          <li><a href="mailto:dagligleder@sandnesibk.no">dagligleder@sandnesibk.no</a></li>
          <li><a href="tel:+4798829125">988 29 125</a> (daglig leder)</li>
        </ul>
      </div>
      <div>
        <h4>Snarveier</h4>
        <ul>
          <li><a href="treningstider.html">Treningstider</a></li>
          <li><a href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">Bli medlem</a></li>
          <li><a href="elite.html">Billetter og sesongkort</a></li>
          <li><a href="medlem.html#skjema">Skjema for utgifter og utstyr</a></li>
          <li><a href="sponsorer.html">Sponsorer</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Sandnes IBK · <a href="cookies.html">Informasjonskapsler</a> · <button type="button" class="cookie-reopen" style="background:none;border:0;padding:0;color:inherit;font:inherit;cursor:pointer;text-decoration:underline">Cookie-innstillinger</button></span>
      <span>Nettside levert av <a href="https://dmarketing.no" target="_blank" rel="noopener">Dietrichs Marketing</a></span>
    </div>
  </div>
</footer>
<script src="app.js" defer></script>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")


def page_hero(eyebrow, h1, lead=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="page-hero"><div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  {lead_html}
</div></section>"""


# ---------- Forside ----------
NEWS = [
    ("elite.html", "billetter.webp", "A-lag herrer · Elite", "Billetter og sesongkort 2026/27"),
    (f"{ORIG}/lagene/a-lag-herrer-elite/neste-hjemmekamp-for-a-laget", "elitetroppen.webp", "A-lag herrer · Elite", "Elite troppen 2026/27"),
    ("treningstider.html", "treningstider.webp", "Treningstider", "Treningstider 2026/2027"),
    ("klubben.html#historie", "opprykk-2015.webp", "Klubben", "Sandnes IBK 35 år – fra gymsal til elitesatsing"),
    (f"{ORIG}/klubben/innkalling-til-arsmote-2026-i-sandnes-ibk", "arsmote.webp", "Klubben", "Innkalling til årsmøte 2026 i Sandnes IBK"),
    (f"{ORIG}/medlem/gratis-vinterferiecamper-muliggjort-av-stotte-fra-ildsjelfondet-2", "vinterferiecamp.webp", "Medlem", "Gratis vinterferiecamper muliggjort av støtte fra Ildsjelfondet"),
]

SPONSORS = [
    ("jaerensparebank", "Jæren Sparebank", "https://www.jaerensparebank.no/"),
    ("sandnesposten", "Sandnesposten", "https://www.sandnesposten.no/"),
    ("hydroscand", "Hydroscand", "https://hydroscand.no/nb-no/"),
    ("tpa", "TP Advokatfirma", "https://www.tpa.no/"),
    ("sandnesmarkise", "Sandnes Markise", "https://sandnes-markise.no/"),
    ("incon", "Incon", "https://incon.no/"),
    ("gsoi", "GSOI", "https://www.gsoi.no/"),
    ("jas", "JAS", "https://www.jas.com/"),
    ("kaihansen", "Kai Hansen", "https://www.kai-hansen.no/"),
    ("stena", "Stena Recycling", "https://www.stenarecycling.com/no/"),
    ("elitevinduspuss", "Elite Vinduspuss", "https://www.elite.no/"),
    ("proffsport", "Proff Sport", "https://proffsport.no/collections/sandnes-ibk-craft-kolleksjon"),
    ("craft", "Craft", "https://www.craft.no/"),
    ("balanz", "Balanz Treningssenter", "https://balanztreningssenter.no/balanz-hana/"),
    ("okristensen", "O. Kristensen Bygg AS", None),
    ("burgerking", "Burger King", "https://burgerking.no/"),
    ("rogalandtaxi", "Rogaland Taxi", None),
    ("masiv", "Masiv", "https://masiv.no/"),
    ("rema1000", "Rema 1000 Skaarlia", None),
    ("dnb", "DNB", None),
    ("sinuselektro", "Sinus Elektro", "https://sinus-elektro.no/hjem"),
    ("asbetong", "AS Betong", None),
    ("soiltech", "Soiltech", "https://soiltech.no/"),
]


def sponsor_grid():
    out = []
    for slug, name, url in SPONSORS:
        img = f'<img src="assets/sponsorer/{slug}.webp" alt="{name}" loading="lazy">'
        if url:
            out.append(f'<a class="sponsor" href="{url}" target="_blank" rel="noopener" title="{name}">{img}</a>')
        else:
            out.append(f'<div class="sponsor" title="{name}">{img}</div>')
    return '<div class="sponsors">' + "".join(out) + "</div>"


def ico(path):
    return f'<span class="shortcut-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>'


news_html = "".join(
    f'''<a class="card reveal" href="{h}"{' target="_blank" rel="noopener"' if h.startswith("http") else ""}>
  <div class="card-img"><img src="assets/{img}" alt="" width="890" height="500" loading="lazy"><span class="tag">{tag}</span></div>
  <h3>{t}</h3>
</a>'''
    for h, img, tag, t in NEWS
)

index_body = f"""
<section class="hero">
  <div class="hero-media"><img src="assets/hero-seier.webp" srcset="assets/hero-seier-960.webp 960w, assets/hero-seier.webp 1920w" sizes="100vw" alt="Sandnes IBK-spillere jubler etter seier mot GIF i kvartfinalen" width="1920" height="853" fetchpriority="high"></div>
  <div class="wrap hero-content">
    <span class="eyebrow">Innebandy i Sandnes siden 1991</span>
    <h1>Elite og bredde. <em>Én klubb.</em></h1>
    <p class="lead">Fra de yngste på barnehagetreningen til herrelaget i eliteserien. Sandnes IBK er en klubb for alle som vil spille innebandy, uansett nivå og erfaring.</p>
    <div class="hero-ctas">
      <a class="btn btn--neon" href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">Bli medlem {ARROW}</a>
      <a class="btn btn--ghost" href="treningstider.html">Se treningstider</a>
    </div>
  </div>
</section>

<section class="matchday">
  <div class="wrap matchday-inner">
    <h2><small>Kampdag i Kleivanehallen</small>Billetter 2026/27</h2>
    <ul class="prices">
      <li><b>120 kr</b><span>Voksne over 16 år</span></li>
      <li><b>50 kr</b><span>Ungdom 12–15 år</span></li>
      <li><b>Gratis</b><span>Barn under 12 år</span></li>
      <li><b>900 kr</b><span>Sesongkort</span></li>
    </ul>
    <a class="btn btn--ink" href="elite.html">Les mer {ARROW}</a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shortcuts">
      <a class="shortcut reveal" href="treningstider.html">{ico('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')}<div><h3>Treningstider</h3><p>Alle lag og haller, sesongen 2026/2027</p></div></a>
      <a class="shortcut reveal" href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">{ico('<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>')}<div><h3>Bli medlem</h3><p>Registrer deg eller barnet ditt via Spond</p></div></a>
      <a class="shortcut reveal" href="medlem.html#camper">{ico('<path d="M3 20l9-15 9 15z"/><path d="M12 20v-6"/>')}<div><h3>Innebandy camper</h3><p>Høst- og vinterferiecamper for barn og unge</p></div></a>
      <a class="shortcut reveal" href="kontakt.html">{ico('<path d="M4 6h16v12H4z"/><path d="M4 7l8 6 8-6"/>')}<div><h3>Kontakt</h3><p>Daglig leder, styret og nyttige adresser</p></div></a>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Siste nytt</span><h2>Fra klubben</h2></div>
      <a class="btn btn--line" href="https://www.facebook.com/sandnesibk" target="_blank" rel="noopener">Følg oss på Facebook {ARROW}</a></div>
    <div class="news">{news_html}</div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Om klubben</span>
        <h2>Fra gymsal til eliteserien</h2>
        <p class="lead">Det startet med en kompisgjeng i gymsalen på Soma skole på slutten av 80-tallet. I dag er Sandnes IBK en av de største innebandyklubbene i Norge, med lag fra barnehagealder til eliteserien.</p>
        <blockquote class="quote">«Elite og bredde hører sammen.»<cite>Trond Vervik</cite></blockquote>
        <p style="margin-top:36px"><a class="btn btn--neon" href="klubben.html">Les historien {ARROW}</a></p>
      </div>
      <div class="split-img reveal"><img src="assets/klubben.webp" alt="Sandnes IBK-spillere samlet i en klem" width="890" height="500" loading="lazy"></div>
    </div>
    <div class="facts">
      <div class="fact reveal"><b>1991</b><span>Sandnes Innebandyklubb stiftet 9. april</span></div>
      <div class="fact reveal"><b>2014/15</b><span>Første sesong i eliteserien for herrer</span></div>
      <div class="fact reveal"><b>50–100</b><span>nye medlemmer i året, med rekruttering fra 1. klasse</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grasrot reveal">
      <div>
        <img src="assets/grasrot.png" alt="Grasrotandelen" width="500" height="129" loading="lazy">
        <h2>Bli grasrotgiver i dag!</h2>
        <p>Du kan bli grasrotgiver i alle Norsk Tippings kanaler eller ved å sende SMS: <strong>Grasrotandelen 983729096</strong> til nummer <strong>60000</strong>.</p>
      </div>
      <div class="actions">
        <a class="btn btn--ink" href="https://www.norsk-tipping.no/grasrotandelen/din-mottaker/983729096" target="_blank" rel="noopener">Støtt Sandnes IBK {ARROW}</a>
        <a class="btn btn--line" href="https://www.norsk-tipping.no/grasrotandelen" target="_blank" rel="noopener">Les mer</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Takk for støtten</span><h2>Våre sponsorer</h2></div>
      <a class="btn btn--line" href="sponsorer.html">Alle sponsorer {ARROW}</a></div>
    {sponsor_grid()}
  </div>
</section>
"""
page("index.html", "Hjem", "Sandnes IBK er innebandyklubben i Sandnes, med lag fra barnehagealder til eliteserien. Treningstider, medlemskap, billetter og nyheter.", index_body)


# ---------- Treningstider ----------
HALLS = [
    ("Kleivanehallen", [
        ("Mandag", [("16:00–17:30", "G13 (f. 2013)"), ("17:30–18:30", "4. klasse jente og 4. klasse gutt"), ("18:30–20:00", "Elite"), ("20:00–22:00", "Sandnes 2 Herre")]),
        ("Tirsdag", [("16:00–17:30", "J13/J15"), ("17:30–18:30", "G15/G17"), ("18:30–19:30", "Sandnes 2 Herre"), ("19:30–21:00", "Elite"), ("21:00–22:30", "Sandnes 3 Mixlag")]),
        ("Onsdag", [("16:30–17:30", "Barnehage"), ("17:30–18:30", "1. klasse gutt, 1. klasse jente, 2. klasse gutt"), ("18:30–19:30", "G13"), ("19:30–21:00", "G15/17"), ("21:00–22:30", "Sandnes 4. Mix lag")]),
        ("Torsdag", [("16:00–17:30", "J11, G11"), ("17:30–18:30", "3. klasse gutt, 2. og 3. klasse jente"), ("18:30–19:30", "J13/J15 og 5. klasse gutt"), ("19:30–20:30", "Sandnes Damer"), ("20:30–22:00", "Elite")]),
    ]),
    ("Giskehallen 2", [
        ("Onsdag", [("17:30–18:45", "1. klasse gutt og jente, 2. klasse, 3.–4. klasse"), ("18:45–20:00", "G11")]),
    ]),
    ("Sørbøhallen", [
        ("Torsdag", [("17:30–18:30", "Siste års barnehage, 1. klasse gutt og jente, 2. klasse gutt og jente"), ("18:30–19:30", "3. klasse, 4. klasse, 5. klasse og 6. klasse"), ("19:30–20:30", "G13 Sørbø")]),
    ]),
    ("Lundehaugen gymsal", [
        ("Mandag", [("18:00–20:00", "G13 Sørbø")]),
        ("Onsdag", [("18:30–20:00", "6. klasse Sørbø")]),
    ]),
    ("Smeaheia gymsal", [("Tirsdag", [("17:00–18:30", "G11 Giske")])]),
    ("Sandved gymsal", [("Tirsdag", [("20:00–22:00", "Sandve damer")])]),
    ("Øygard gymsal", [("Treningstider", [("17:00–18:00", "1. og 2. klasse"), ("18:00–19:00", "3. og 4. klasse"), ("19:00–20:00", "Sandnes damer")])]),
]
AGES = [("J11", "Jenter f. 2016–2015"), ("G11", "Gutter f. 2016–2015"), ("G13", "Gutter f. 2014–2013"), ("J13", "Jenter f. 2014–2013"), ("G15", "Gutter f. 2012–2011"), ("J15", "Jenter f. 2012–2011"), ("G17", "Gutter f. 2010–2009")]

halls_html = ""
for hall, days in HALLS:
    days_html = "".join(
        f'<div class="day"><h3>{d}</h3><ul>' + "".join(f"<li><time>{t}</time><span>{g}</span></li>" for t, g in rows) + "</ul></div>"
        for d, rows in days)
    halls_html += f'<div class="hall reveal"><h2>{hall}</h2><div class="days">{days_html}</div></div>'

ages_html = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in AGES)
tren_body = page_hero("Sesongen 2026/2027", "Treningstider", "Her finner du når og hvor alle lagene trener. Usikker på hvilken gruppe du hører til? Ta kontakt med trener eller oppmann på laget.") + f"""
<section class="section"><div class="wrap">{halls_html}</div></section>
<section class="section section--ink"><div class="wrap"><div class="split" style="align-items:start">
  <div><span class="eyebrow">Aldersinndeling</span><h2>Hvilket lag passer?</h2><p class="lead">Lagene er delt inn etter fødselsår. Har du spørsmål, send en e-post til <a href="mailto:post@sandnesibk.no" style="color:#E6FF00">post@sandnesibk.no</a>.</p>
  <p style="margin-top:28px"><a class="btn btn--neon" href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">Bli medlem {ARROW}</a></p></div>
  <table class="age-table">{ages_html}</table>
</div></div></section>
"""
page("treningstider.html", "Treningstider", "Treningstider 2026/2027 for alle lag i Sandnes IBK: Kleivanehallen, Giskehallen, Sørbøhallen og gymsaler.", tren_body)


# ---------- Medlem ----------
FILES = [
    ("Honorarskjema SIBK 2022", "Honorarskjema SIBK 2022"),
    ("KM godtgjørelse skjema SIBK 2022", "KM godtgjørelse skjema SIBK 2022"),
    ("Reisegodtgjørelse skjema SIBK 2022", "Reisegodtgjørelse skjema SIBK 2022"),
    ("Utgiftsrefusjonsskjema SIBK", "Utgiftsrefusjonsskjema SIBK"),
]
from urllib.parse import quote
files_html = "".join(
    f'<li><a href="{ORIG}/storage/files/uploads/{quote(f + "." + ext)}" target="_blank" rel="noopener">{label}<small>{ext.upper()}</small></a></li>'
    for f, label in FILES for ext in ("pdf", "xlsx"))

medlem_body = page_hero("Medlem", "Bli en del av klubben", "Sandnes IBK bruker Spond Club som medlemsregister. Her finner du alt om medlemskap, utstyr, lisens, dugnad og camper.") + f"""
<section class="section"><div class="wrap">
  <div class="box box--ink reveal" style="display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));align-items:center">
    <div><span class="eyebrow">Bli medlem</span><h2 style="margin:0">Meld deg inn i Sandnes Innebandy Klubb</h2></div>
    <div><p style="color:#A9A9B2">Klikk på knappen under for å registrere deg eller ditt barn via Spond. Dersom du er i tvil om hvilken gruppe du skal søke medlemskap i, ta kontakt med trener eller oppmann på laget du hører til.</p>
    <a class="btn btn--neon" href="https://club.spond.com/landing/signup/sandnesibk" target="_blank" rel="noopener">Registrer deg {ARROW}</a></div>
  </div>
</div></section>

<section class="section section--paper"><div class="wrap">
  <div class="grid-2">
    <div class="box reveal" style="background:var(--white)" id="oppstartspakke">
      <span class="eyebrow">Oppstartspakke</span>
      <h3>800 kr, sterkt sponset av klubben</h3>
      <ul><li>Drikkeflaske</li><li>Beskyttelsesbriller</li><li>Kølle og ball</li><li>Oppbevaringspose</li></ul>
      <p>Du må ha betalt medlemsavgiften og oppstartspakken i Spond. Deretter kan du hente utstyret på utleveringsstedet som kommuniseres på Spond. Spørsmål sender du til <a href="mailto:materiell@sandnesibk.no">materiell@sandnesibk.no</a>.</p>
    </div>
    <div class="box reveal" style="background:var(--white)" id="utstyr">
      <span class="eyebrow">Utstyr og kolleksjon</span>
      <h3>Det eneste du trenger er innesko</h3>
      <p>Sandnes IBK stiller med utstyr til treningen som baller, vester, mål, vant og kjegler. Køller kan lånes på trening, men mange velger etter hvert å bruke sin egen.</p>
      <p>Klubbkolleksjonen med logo leveres av samarbeidspartneren vår Proffsport. Sandnes bruker gult på sort.</p>
      <a class="btn btn--ink" href="https://proffsport.no/collections/sandnes-ibk-craft-kolleksjon" target="_blank" rel="noopener">Se kolleksjonen {ARROW}</a>
    </div>
    <div class="box reveal" style="background:var(--white)" id="lisens">
      <span class="eyebrow">Priser og lisens</span>
      <h3>Generelle bestemmelser</h3>
      <p>Aldersbestemte spillere som deltar i seniorspill, må betale lisensen knyttet til den seniordivisjonen de deltar i. Aldersbestemte spillere som kun deltar i aldersbestemte kamper, betaler lisens ut fra fødselsår, uavhengig av hvilken av de aldersbestemte klassene det deltas i.</p>
      <p>Det kreves ikke lisens for deltakelse i minirunder.</p>
      <a class="btn btn--line" href="https://bandyforbundet.no/sorvest-bandyregion/?msswb-post=serieinformasjon-2022-2023" target="_blank" rel="noopener">Lisenser hos forbundet {ARROW}</a>
    </div>
    <div class="box reveal" style="background:var(--white)" id="dugnad">
      <span class="eyebrow">Dugnad og frivillige</span>
      <h3>Vi trenger deg</h3>
      <p>For å drive klubben trenger vi frivillige til forskjellige oppgaver. Styret, trenere og oppmenn er frivillige, men vi trenger også noen til minirunder og turneringer. Typiske oppgaver er kiosk og å sette opp vant. Disse organiseres fortløpende.</p>
      <a class="btn btn--line" href="mailto:leder@sandnesibk.no">Meld deg som frivillig {ARROW}</a>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Ingen skal stå utenfor</span>
      <h2>Støtte til deltakelse</h2>
      <p class="lead">Sandnes IBK har fått tildelt 10&nbsp;000 kroner i «For Alle»-midler fra Sparebankstiftelsen. Midlene skal gå til barn og ungdom som opplever økonomiske utfordringer med å delta i innebandy.</p>
      <p>Kjenner du noen som kunne hatt nytte av støtte, ta kontakt med <a href="mailto:dagligleder@sandnesibk.no">dagligleder@sandnesibk.no</a>. Foresatte kan også søke direkte via skjema.</p>
      <a class="btn btn--ink" href="https://docs.google.com/forms/d/e/1FAIpQLSdS7_zHsvBkyPjgFR87Fl1xVqSg3GecO1jXBVk4OLkw61y4-g/viewform?usp=header" target="_blank" rel="noopener">Søk om støtte {ARROW}</a>
    </div>
    <div class="box reveal" id="camper">
      <span class="eyebrow">Innebandy camper</span>
      <h3>Høstferie Camp U13–U17</h3>
      <p>Camp sammen med to av våre erfarne elitespillere, Andreas Mikalsen og Jacob Öberg. Åpen for alle spillere i alderen U13–U17, delt inn i grupper etter alder.</p>
      <ul><li><strong>Sted:</strong> Kleivanehallen</li><li><strong>Dato:</strong> 9.–10. oktober</li><li><strong>Deltakeravgift:</strong> 500 kr (+15 kr Spond-gebyr)</li></ul>
      <a class="btn btn--ink" href="https://spond.com/invite/FSVMI" target="_blank" rel="noopener">Meld deg på {ARROW}</a>
      <h3 style="margin-top:36px">Gratis vinterferiecamper</h3>
      <p>Takket være midler fra Ildsjelfondet arrangerer Sandnes IBK gratis vinterferiecamper for barn fra 2. klasse til U11, og for ungdom U13–U17. Åpent for både medlemmer og ikke-medlemmer.</p>
      <a class="btn btn--line" href="{ORIG}/innebandy-camper" target="_blank" rel="noopener">Alle camper {ARROW}</a>
    </div>
  </div>
</div></section>

<section class="section section--paper" id="skjema"><div class="wrap">
  <div class="split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Skjema</span>
      <h2>Utgifter og utstyr</h2>
      <p class="lead">Alle skjemaene ligger her i både PDF- og Excel-format, og er siste godkjente versjon for bruk ved for eksempel refusjoner.</p>
      <p><a class="btn btn--ink" href="https://form.jotform.com/242455135957362" target="_blank" rel="noopener">Bestill lagutstyr {ARROW}</a></p>
      <p><a class="btn btn--line" href="https://form.jotform.com/242456365106354" target="_blank" rel="noopener">Bestill draktsett {ARROW}</a></p>
    </div>
    <ul class="files reveal">{files_html}</ul>
  </div>
</div></section>
"""
page("medlem.html", "Medlem", "Bli medlem i Sandnes IBK via Spond. Oppstartspakke, utstyr, lisens, dugnad, camper og skjema.", medlem_body)


# ---------- Elite ----------
elite_body = page_hero("A-lag herrer · Elite", "Billetter og sesongkort 2026/27", "Vi gleder oss til en ny sesong i Kleivanehallen, og håper å se både kjente og nye ansikter på tribunen.") + f"""
<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal">
      <span class="eyebrow">Priser på inngang</span>
      <ul class="contact-list" style="font-size:19px">
        <li><span>Voksne over 16 år</span><strong>120 kr</strong></li>
        <li><span>Ungdom 12–15 år</span><strong>50 kr</strong></li>
        <li><span>Barn under 12 år</span><strong>Gratis</strong></li>
        <li><span>Medlemmer i Sandnes IBK under 18 år</span><strong>Gratis</strong></li>
        <li><span>Sesongkort</span><strong>900 kr</strong></li>
      </ul>
      <p style="margin-top:20px">Sesongkortet gir adgang til alle hjemmekamper gjennom sesongen, inkludert NM og sluttspill.</p>
    </div>
    <div class="split-img reveal"><img src="assets/billetter.webp" alt="Sandnes IBK Elite i Kleivanehallen" width="890" height="500"></div>
  </div>
</div></section>
<section class="section section--ink"><div class="wrap"><div class="grid-2">
  <div class="reveal"><span class="eyebrow">Praktisk informasjon</span><h2>Kjøp på kampdag</h2></div>
  <div class="reveal">
    <p class="lead">Det er ikke mulig å reservere eller kjøpe enkeltbilletter på forhånd. Billetter kjøpes ved inngangen på kampdag, så vi anbefaler å være ute i god tid før kampstart.</p>
    <p style="color:#A9A9B2">Sesongkort kan kjøpes fra serieåpningen i Kleivanehallen. Det blir satt opp egen kø for kjøp av sesongkort ved inngangen, slik at det går raskt og enkelt.</p>
  </div>
</div></div></section>
<section class="section"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Laget</span><h2>Elite troppen 2026/27</h2></div>
  <a class="btn btn--line" href="{ORIG}/lagene/a-lag-herrer-elite/neste-hjemmekamp-for-a-laget" target="_blank" rel="noopener">Se troppen {ARROW}</a></div>
  <div class="split-img reveal"><img src="assets/elitetroppen.webp" alt="Lagbilde av Sandnes IBK Elite 2026/27" width="890" height="500" loading="lazy" style="aspect-ratio:16/9"></div>
</div></section>
"""
page("elite.html", "Elite", "Billetter og sesongkort til Sandnes IBK Elite sine hjemmekamper i Kleivanehallen sesongen 2026/27.", elite_body)


# ---------- Klubben ----------
klubben_body = page_hero("Klubben", "Om klubben og sporten", "Sandnes IBK spiller i sorte drakter med gult i, samt sorte strømper.") + f"""
<section class="section"><div class="wrap"><div class="prose">
<p class="lead" style="color:var(--ink)">Sandnes IBK strekker seg helt tilbake til 1988, da klubben først startet opp under navnet Trones Innebandy.</p>
<p>De første årene bar preg av en idrett som tross alt var ganske ung i Norge. Innebandyseksjonen i Norges Bandyforbund ble etablert i 1988. Kampene ble spilt i små gymsaler 3 mot 3 utespillere pluss keeper, men uten vant. Enkelte gymsaler var så små at det kun var plass til 2+2 spillere. Sesongen 1992 ble det store endringer da kamper skulle spilles på stor bane som i dag, og klubben måtte denne sesongen snekre sitt eget vant av finerplater! I dag er det litt andre rammer. Innebandyseksjonen er den desidert største i bandyforbundet, med om lag ¾ av medlemmene, og innebandy er fortsatt en av de raskest voksende idrettene i Norge.</p>
<p>Sesongen 1989/90 var klubben for første gang med i ordinært seriespill. I 1991 slo Trones Innebandy seg sammen med Hana Hockeyboys. Sandnes Innebandyklubb ble stiftet 9. april 1991. I 1996 ble Aspervika Innebandyklubb en del av Sandnes IBK. Vi er i dag en klubb i sterk vekst med mange aldersbestemte lag og seniorlag. Det gleder oss spesielt at vi har klart å etablere et elitelag for herrer.</p>
<p>Sesongen 2013/2014 vant Sandnes IBK 1. divisjon for herrer, og da kom spørsmålet om elitesatsing. Vi valgte av flere grunner å takke nei, men bestemte oss for å prøve igjen sesongen etter, slik at vi fikk ett år ekstra til å planlegge. Det kreves mye for å etablere seg i den norske eliteserien i innebandy: økonomi, organisasjon og støttespillere er kanskje det viktigste. Fra sesongen 2014/2015 har herrelaget vårt spilt i eliteserien.</p>
<p>Fellesnevneren for samtlige lag fra Rogaland som har vært i eliteserien, er at man taper store penger. Det gir mindre midler til aldersbestemte lag, og går da ut over medlemmene i klubbene. Her ønsker Sandnes IBK å skille seg ut. Vi skal ikke bare bygge opp et A-lag i eliteserien, vi skal fortsette det gode arbeidet med å bygge en klubb. Rekruttering og aldersbestemte lag skal alltid være vårt hovedfokus.</p>
<h2>Barn og ungdom i Sandnes IBK</h2>
<p>Siden slutten av 90-tallet var det et mål å ha et aldersbestemt lag for å rekruttere nye spillere til A-laget, men det var først på midten av 2000-tallet at rekrutteringen og satsingen på barn og unge tok til for alvor. I 2006 hadde klubben i tillegg til A-laget et Gutter 15-lag og et U8-lag (1. og 2. klasse). Årene etter har vi etablert flere nye lag i ulike bydeler i Sandnes. I sesongen 14/15 var vi totalt 12 aldersbestemte lag som deltok i seriespill og på miniturneringer. Med fast årlig rekruttering fra 1. klasse i flere bydeler de siste årene vokser klubben med rundt 50–100 medlemmer årlig.</p>
</div></div></section>

<section class="section section--paper" id="historie"><div class="wrap"><div class="prose">
<span class="eyebrow">Publisert 9. april 2026</span>
<h2>Sandnes IBK 35 år – fra gymsal til elitesatsing</h2>
<p class="lead" style="color:var(--ink)">9. april markerer Sandnes IBK 35 år. En historie som startet i det små, og som i dag har vokst til å bli en av de største innebandyklubbene i Norge. Dette er historien om menneskene, valgene og fellesskapet som har formet klubben.</p>
<h3>Starten – bygget på engasjement</h3>
<p>Historien starter på slutten av 80-tallet. En kompisgjeng, en gymsal på Soma skole, og en nøkkel som egentlig ikke skulle vært brukt.</p>
<blockquote>«Vi lånte en nøkkel og kom oss ubemerket inn i gymsalen og fikk oss en treningsøkt.»</blockquote>
<p>Det forteller Geir Maldal, en av dem som var med fra starten og senere ble en av de viktigste personene i klubbens utvikling. Det som begynte som Trones Innebandy, vokste raskt. Flere miljøer i Sandnes fant veien til sporten, og i 1991 ble Sandnes IBK etablert.</p>
<p>De første årene var preget av en idrett i utvikling. Det ble spilt i små gymsaler, ofte 3 mot 3, noen ganger enda færre. Banene hadde ikke vant, og målgårder måtte teipes før kamp. Da innebandyen etter hvert gikk over til spill på full bane, måtte klubben selv finne løsninger.</p>
<blockquote>«Vi snekret vårt eget vant av finerplater i en garasje. Det kostet oss 16.000 kroner og ble gjort på dugnad.»</blockquote>
<p>Rammene var enkle. Men engasjementet var stort.</p>
<figure><img src="assets/avisartikkel.webp" alt="Avisartikkel om Sandnes IBK fra 90-tallet" width="720" height="900" loading="lazy" style="max-width:460px"><figcaption>Avisartikkel fra 90-tallet</figcaption></figure>
<h3>En klubb som holdt på å forsvinne – og ble bygget opp igjen</h3>
<p>Veien videre var ikke rett frem. På midten av 90-tallet opplevde klubben frafall av spillere, og på et tidspunkt var Sandnes IBK nær ved å forsvinne. Men klubben ble reddet.</p>
<blockquote>«Vi fikk bygget den opp igjen fra slutten av 90-tallet,» forteller Geir.</blockquote>
<p>Det ble starten på en ny fase. Med rekruttering, ungdomslag og et stadig sterkere klubbmiljø.</p>
<h3>Fellesskapet som fundament</h3>
<p>Gjennom alle år har én ting vært konstant: fellesskapet.</p>
<blockquote>«Innebandy var en idrett alle kunne være med på. Det var nok en av hovedgrunnene til at vi startet – og at det vokste.»</blockquote>
<p>Dette verdigrunnlaget har fulgt klubben videre. En lavterskelidrett. Et tilbud for alle. Et miljø der man blir sett. Geir har vært en bærebjelke i dette arbeidet gjennom mer enn 30 år, og ble tildelt frivillighetsprisen for sin innsats for innebandyen i Sandnes og regionen.</p>
<figure><img src="assets/geir-maldal.webp" alt="Geir Maldal mottar frivillighetsprisen" width="1200" height="672" loading="lazy"></figure>
<h3>Veien videre – en ny generasjon tar ansvar</h3>
<p>Blant dem som vokste opp i dette miljøet var Trond Vervik. Som 13-åring startet han i klubben, og opplevde raskt hva som gjorde Sandnes IBK spesielt.</p>
<blockquote>«Man følte seg som en del av hele klubben uansett hvilket lag man spilte på.»</blockquote>
<p>Han tok med seg denne erfaringen videre i karrieren, spilte på høyere nivå og opplevde blant annet å vinne NM. Men etter hvert kom et veivalg. Som 23-åring valgte han å flytte hjem igjen.</p>
<blockquote>«Uten Sandnes hadde jeg ikke vært der jeg er i dag – nå var det min tur å gi noe tilbake.»</blockquote>
<h3>Starten på elitesatsingen</h3>
<p>Da Trond kom tilbake i 2011, var ikke klubben der den er i dag. Resultatene var varierende, og rammene begrensede. Men ambisjonene begynte å vokse.</p>
<blockquote>«Det hadde vært kult med et elitelag i Sandnes.»</blockquote>
<p>Likevel var det tydelig at dette måtte gjøres riktig. Ikke på bekostning av klubben, men som en del av den.</p>
<blockquote>«Uten rekruttering er vi ingenting.»</blockquote>
<p>Klubben valgte derfor en retning der elite og bredde skulle utvikles parallelt.</p>
<blockquote>«Elite og bredde hører sammen.»</blockquote>
<p>Det ble opprettet egne strukturer rundt elitesatsingen, samtidig som klubben fortsatte å bygge tilbudet til barn og ungdom.</p>
<figure><img src="assets/opprykk-2015.webp" alt="Sandnes IBK rykker opp til eliten" width="890" height="500" loading="lazy"><figcaption>Året 2014/2015: Sandnes IBK rykker opp til eliten</figcaption></figure>
<h3>Utfordringer – og tydelige valg</h3>
<p>Arbeidet var krevende. Nivået i regionen var ikke alltid godt nok, og spillere måtte hentes utenfra for å kunne konkurrere. Samtidig var det utfordringer knyttet til samarbeid og spillerflyt mellom klubber. Men for Trond var én ting avgjørende: muligheter må gis.</p>
<blockquote>«Jeg byttet selv klubb som 15-åring. Hadde jeg ikke gjort det, hadde jeg aldri fått oppleve det jeg har i dag.»</blockquote>
<p>Han trekker frem hvordan han selv ble møtt da han dro videre:</p>
<blockquote>«Sandnes ønsket meg lykke til. Det var aldri noen som prøvde å stikke kjepper i hjulene.»</blockquote>
<p>Det er en holdning han mener flere kan lære av.</p>
<h3>En klubb for alle</h3>
<p>Gjennom hele utviklingen har ett prinsipp vært styrende: klubben skal være for alle.</p>
<blockquote>«Skal du ha et tilbud til alle, så må du faktisk ha det. Fra barn på 5–6 år – til de som vil spille på høyeste nivå.»</blockquote>
<p>Det handler ikke bare om å si det, men å gjøre det.</p>
<blockquote>«Har du ikke et godt nok tilbud selv, må du tørre å si det – og ønske spillere lykke til videre.»</blockquote>
<p>For i bunn ligger en erkjennelse:</p>
<blockquote>«Vi har ikke råd til å miste noen.»</blockquote>
<figure><img src="assets/hero-seier-960.webp" alt="Seier mot GIF i kvartfinale" width="960" height="426" loading="lazy"><figcaption>Seier mot GIF i kvartfinale</figcaption></figure>
<h3>I dag – og veien videre</h3>
<p>I dag er Sandnes IBK en klubb med sterk vekst, stort engasjement og et tilbud som favner bredt. Fra de yngste spillerne til eliteserien. Men kanskje er det viktigste ikke hvor klubben er, men hvordan den har kommet dit. Gjennom mennesker som har tatt ansvar. Gjennom valg som har vært gjort over tid. Gjennom et fellesskap som fortsatt står sterkt.</p>
<p>Når Trond ser tilbake på reisen, oppsummerer han det slik:</p>
<blockquote>«Magisk.»</blockquote>
</div></div></section>
"""
page("klubben.html", "Klubben", "Historien om Sandnes IBK: fra Trones Innebandy i 1988 til eliteserien. 35 år med innebandy i Sandnes.", klubben_body)


# ---------- Kontakt ----------
ROLES = [("Materialforvalter", "materiell@sandnesibk.no"), ("Spond-ansvarlig (medlemmer)", "spond@sandnesibk.no"),
         ("Lisenser", "lisens@sandnesibk.no"), ("Oppfølging av trenere og oppmenn/-kvinner", "tv@sandnesibk.no")]
BOARD = [("Styrets leder", "Stanley Benitez Jensen", "leder@sandnesibk.no"), ("Nestleder", "Trond Skjørestad Vervik", "trond@sandnesibk.no"),
         ("Styremedlem (kasserer)", "Anne Gjesdal Hansen", "kasserer@sandnesibk.no"), ("Styremedlem", "Kjartan Vold", "spond@sandnesibk.no"),
         ("Styremedlem", "Kjell Gunnar Vervik", None), ("Styremedlem", "Tommy Olsen Volden", "tv@sandnesibk.no"),
         ("Styremedlem", "Ingrid Øvregård Folkvord", None), ("Varamedlem", "Geir Maldal", None), ("Varamedlem", "Ellen Birkeland", None),
         ("Ungdomsrepresentant", "Tino Bach Bjørnlund", None)]
roles_html = "".join(f'<li><span>{r}</span><a href="mailto:{e}">{e}</a></li>' for r, e in ROLES)
board_html = "".join(
    f'<li><span>{t}</span>' + (f'<a href="mailto:{e}">{n}</a>' if e else f'<strong>{n}</strong>') + '</li>'
    for t, n, e in BOARD)
kontakt_body = page_hero("Kontakt", "Ta kontakt med oss", "Spørsmål om medlemskap, lag, utstyr eller sponsorat? Her finner du riktig person.") + f"""
<section class="section"><div class="wrap"><div class="grid-2">
  <div class="box box--ink reveal">
    <span class="eyebrow">Daglig leder</span>
    <h3>Linn Skjørestad Vervik</h3>
    <p><a class="big-link" href="tel:+4798829125">988 29 125</a></p>
    <p><a class="big-link" style="font-size:clamp(20px,2.4vw,28px)" href="mailto:dagligleder@sandnesibk.no">dagligleder@sandnesibk.no</a></p>
  </div>
  <div class="box reveal">
    <span class="eyebrow">Sandnes Innebandyklubb</span>
    <ul class="contact-list">
      <li><span>E-post</span><a href="mailto:post@sandnesibk.no">post@sandnesibk.no</a></li>
      <li><span>Org.nr</span><strong>983 729 096</strong></li>
      <li><span>Vipps</span><strong>125960</strong></li>
      <li><span>Postadresse</span><strong>Diamantveien 16, 4321 Sandnes</strong></li>
    </ul>
    <div style="margin-top:22px">{social("social--light")}</div>
  </div>
</div></div></section>
<section class="section section--paper"><div class="wrap"><div class="grid-2" style="align-items:start">
  <div class="reveal"><span class="eyebrow">Nyttige adresser</span><h2>Roller i klubben</h2><ul class="contact-list">{roles_html}</ul></div>
  <div class="reveal"><span class="eyebrow">Styret</span><h2>Styret</h2><ul class="contact-list">{board_html}</ul></div>
</div></div></section>
"""
page("kontakt.html", "Kontakt", "Kontakt Sandnes IBK: daglig leder, styret og nyttige e-postadresser. Org.nr 983 729 096.", kontakt_body)


# ---------- Sponsorer ----------
spons_body = page_hero("Samarbeidspartnere", "Våre sponsorer", "Tusen takk til alle som støtter Sandnes IBK. Sponsorene gjør det mulig å gi et godt tilbud til alle, fra de yngste til eliteserien.") + f"""
<section class="section"><div class="wrap">{sponsor_grid()}</div></section>
<section class="section section--ink"><div class="wrap"><div class="grid-2" style="align-items:center">
  <div class="reveal"><span class="eyebrow">Bli sponsor</span><h2>Vil bedriften din støtte klubben?</h2></div>
  <div class="reveal"><p class="lead">Ta kontakt med daglig leder for en prat om samarbeid og profilering, blant annet i Kleivanehallen.</p>
  <a class="btn btn--neon" href="mailto:dagligleder@sandnesibk.no">Kontakt daglig leder {ARROW}</a></div>
</div></div></section>
"""
page("sponsorer.html", "Sponsorer", "Sponsorer og samarbeidspartnere til Sandnes IBK.", spons_body)


# ---------- Informasjonskapsler ----------
cookies_body = page_hero("Personvern", "Informasjonskapsler") + """
<section class="section"><div class="wrap"><div class="prose">
<p>For at nettsiden skal fungere optimalt, bruker vi informasjonskapsler. Informasjonskapsler (cookies) er små tekstfiler som blir lagret på enheten din når du besøker siden vår.</p>
<h3>Nødvendige informasjonskapsler</h3>
<p>Det finnes noen informasjonskapsler som vi må inkludere for at enkelte nettsider skal fungere. Av den grunn krever de ikke ditt samtykke.</p>
<ul><li><strong>sibk_cookie_consent</strong> (1 år): Brukes til å lagre brukerens samtykkeinnstillinger for informasjonskapsler.</li></ul>
<p>Ønsker du ikke lagring av informasjonskapsler, kan du følge anvisningene her for å skru dem av i nettleseren din: <a href="https://nettvett.no/slik-administrer-du-informasjonskapsler" target="_blank" rel="noopener">nettvett.no/slik-administrer-du-informasjonskapsler</a>. Merk at noen funksjoner på nettsiden ikke fungerer om du ikke bruker informasjonskapsler.</p>
<p><button type="button" class="btn btn--ink cookie-reopen">Endre innstillinger</button></p>
</div></div></section>
"""
page("cookies.html", "Informasjonskapsler", "Informasjonskapsler og personvern hos Sandnes IBK.", cookies_body)

print("Bygget", len(NAV) + 1, "sider")
