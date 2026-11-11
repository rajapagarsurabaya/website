"""Generator situs Raja Pagar Surabaya.
Dijalankan otomatis oleh Netlify: python3 build/gen.py prod  -> folder dist/
Konten (proyek, artikel) dibaca dari folder content/ yang diedit lewat panel admin /admin.
Ganti BASE saat pindah ke domain rajapagarsurabaya.com."""
import sys, os, re, json, html, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from konten import PAGES
import bravo
import data as DATA

MODE = sys.argv[1] if len(sys.argv) > 1 else "prod"
BASE = "https://rajapagarsurabaya.netlify.app"
OUT = os.path.join(DATA.ROOT, "dist" if MODE == "prod" else "preview")
SRC = open(os.path.join(HERE, "src_beranda.html"), encoding="utf-8").read()
TODAY = datetime.date.today().isoformat()

# ---------- Siapkan folder hasil: salin static/, olah foto proyek
if os.path.exists(OUT): shutil.rmtree(OUT)
shutil.copytree(DATA.STATIC, OUT, ignore=lambda d, names: ["proyek"] if os.path.abspath(d) == os.path.join(DATA.STATIC, "img") else [])
IMG = os.path.join(OUT, "img")
DATA.process_media(IMG)
P, META = DATA.load_proyek()
ARTIKEL = DATA.load_artikel()
URUT = {m["urutan"]: k for k, m in enumerate(META) if m["urutan"]}
def U(i):  # nomor lama (0-based, dari konten.py) -> indeks proyek sekarang
    return URUT.get(i + 1)
VIS = [k for k in range(len(P)) if META[k]["tampil"]]
BARU = [k for k in VIS if META[k]["baru"]]
for p in PAGES:
    ph = []
    for x in p["photos"]:
        if isinstance(x, int):
            k = U(x)
            if k is not None and META[k]["tampil"]: ph.append(k)
        else:
            ph.append(x)
    p["photos"] = [k for k in BARU if p["slug"] in META[k]["pages"]] + ph
WA = "6285607988227"
E = html.escape

def L(slug):
    if MODE == "prod":
        return "./" if slug == "" else slug
    return "index.html" if slug == "" else slug + ".html"

def cut(s, a, b):
    i = s.index(a); j = s.index(b, i) + len(b); return s[i:j]

CSS = cut(SRC, "<style>", "</style>")[7:-8]
CSS += r"""
.crumb{font-size:.82rem;color:var(--on-navy-muted);display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.crumb a{color:var(--on-navy-muted)}
.page-hero{background:var(--navy);color:var(--on-navy);padding-block:48px 56px}
.page-hero h1{font-size:clamp(2.1rem,5.4vw,3.6rem);font-weight:900;font-stretch:80%;text-transform:uppercase}
.page-hero .intro{display:grid;gap:12px;max-width:64ch;margin-top:16px;color:var(--on-navy-muted)}
.page-hero .actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.points{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.point{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:18px;display:grid;gap:6px;align-content:start}
.point p{color:var(--muted);font-size:.92rem}
@media (max-width:900px){.points{grid-template-columns:1fr 1fr}}
@media (max-width:480px){.points{grid-template-columns:1fr}}
.detail{display:grid;grid-template-columns:1fr 1.3fr;gap:32px;align-items:start}
.detail ul{margin:0;padding:0;list-style:none;display:grid;gap:10px}
.detail li{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:12px 14px;font-size:.95rem}
@media (max-width:760px){.detail{grid-template-columns:1fr}}
.photos{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
.photos figure{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
.photos figure img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;max-width:100%}
.photos figcaption{padding:10px 12px;font-size:.86rem;color:var(--muted)}
.related{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media (max-width:760px){.related{grid-template-columns:1fr}}
.svc-group{margin-top:36px}
.svc-group:first-of-type{margin-top:0}
.svc-group h2{font-size:1.4rem;margin-bottom:14px}
.prose{max-width:68ch;display:grid;gap:14px}
.prose p{color:var(--muted)}
.map-wrap{border-radius:var(--r);overflow:hidden;border:1px solid var(--line);aspect-ratio:16/9;max-width:100%}
.map-wrap iframe{width:100%;height:100%;border:0;display:block}
.more-link{margin-top:20px;display:flex;justify-content:flex-start}
nav.main a[aria-current="page"]{color:var(--on-navy);background:rgba(255,255,255,.1)}
"""
CSS += bravo.CSS
CSS += ".g-score{font-size:1rem;color:var(--muted)}.g-score b{font-family:var(--display);font-size:1.6rem;color:var(--ink);font-weight:800}.g-score .stars{margin:0 4px}.pack{display:flex;flex-direction:column}.pack .fit{flex:1}.pack .btn{align-self:flex-start;margin-top:4px}.pack .btn-line{padding:12px 20px;font-size:1rem;color:var(--link);border:2px solid currentColor;background:transparent}"
CSS = "[hidden]{display:none!important}\nimg{max-width:100%;height:auto}\nbody{margin:0}\n" + CSS

# ---------- JS: jaga agar aman di semua halaman
JS = cut(SRC, "<script>\n(function(){", "</script>")[len("<script>\n(function(){"):-9]
def wrap(js, start, end, cond):
    i = js.index(start); j = js.index(end) if end else js.rindex("})();")
    return js[:i] + "  if(" + cond + "){\n" + js[i:j] + "  }\n" + js[j:]
JS = wrap(JS, "  // Sistem bukaan demo", "  // Galeri filter", 'document.getElementById("gL")')
JS = wrap(JS, "  // Galeri filter", "  // Proses ke hasil", 'document.getElementById("lb")')
JS = wrap(JS, "  // Form ke WhatsApp", None, 'document.getElementById("f")')
JS = JS.replace("  update();\n", """  var fm=document.getElementById("f");
  if(fm.dataset.layanan)document.getElementById("layanan-in").value=fm.dataset.layanan;
  if(fm.dataset.bukaan)document.getElementById("bukaan-in").value=fm.dataset.bukaan;
  update();
""")
JS = bravo.JS + JS
JS = JS.replace('"Halo Raja Pagar Surabaya, saya ingin konsultasi.\\n\\n"', '"Halo Raja Pagar Surabaya, saya ingin konsultasi (dari website).\\n\\n"')

ICONS = cut(SRC, '<div class="socials">', '</div>')
FAB = cut(SRC, '<a class="fab"', '</a>')
LB = cut(SRC, '<div class="lb" id="lb"', '</div>\n</div>')
LD_BIZ = json.loads(cut(SRC, '<script type="application/ld+json">', '</script>')[35:-9])

NAV = [("", "Beranda"), ("layanan", "Layanan"), ("galeri", "Galeri"), ("blog", "Blog"), ("tentang-kami", "Tentang Kami"), ("kontak", "Kontak")]

WA_IC = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.8 4.9-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-2.9.8.8-2.8-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'
CLOCK_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
PIN_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
MENU_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
GROUP_TITLES = {"Style pagar":"Style Pagar","Sistem bukaan":"Sistem Bukaan","Layanan lain":"Layanan Lain"}

def header(cur):
    svc_slugs = {p["slug"] for p in PAGES} | {"layanan"}
    groups = {}
    for p in PAGES: groups.setdefault(p["group"], []).append(p)
    cols = ""
    for g, ps in groups.items():
        links = "".join(f'<a href="{L(p["slug"])}">{E(p["h1"].replace(" Surabaya",""))}</a>' for p in ps)
        if g == "Sistem bukaan":
            links += f'<a href="{L("layanan")}"><b>Semua layanan →</b></a>'
        cols += f'<div><h4>{GROUP_TITLES.get(g,g)}</h4>{links}</div>'
    def a(sl, n):
        return f'<a href="{L(sl)}"' + (' aria-current="page"' if sl == cur else "") + f'>{n}</a>'
    dd_cur = ' aria-current="page"' if cur in svc_slugs else ""
    return (f'<div class="topbar"><div class="wrap">'
      f'<a class="tb-item" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_IC}0856-0798-8227</a>'
      f'<span class="tb-item tb-hide">{CLOCK_IC}Senin–Sabtu, 08.00–16.00 WIB</span>'
      f'<span class="tb-item tb-hide">{PIN_IC}Survei gratis se-Surabaya</span>{ICONS}</div></div>\n'
      f'<header>\n  <div class="wrap hdr">\n'
      f'    <a class="logo" href="{L("")}" aria-label="Raja Pagar Surabaya, beranda"><img src="img/logo.png" alt="Logo Raja Pagar" width="260" height="63"><span class="city">SURABAYA</span></a>\n'
      f'    <nav class="main" id="nav" aria-label="Menu utama">{a("", "Beranda")}'
      f'<div class="dd"><button class="dd-btn" aria-expanded="false" aria-controls="ddm"{dd_cur}>Layanan {CHEV}</button><div class="dd-menu" id="ddm">{cols}</div></div>'
      f'{a("galeri", "Galeri")}{a("blog", "Blog")}{a("tentang-kami", "Tentang Kami")}{a("kontak", "Kontak")}'
      f'<a class="btn btn-cta nav-cta-m" href="#kontak">Survei Gratis</a></nav>\n'
      f'    <a class="btn btn-cta nav-cta" href="#kontak">Survei Gratis</a>\n'
      f'    <button class="menu-btn" aria-expanded="false" aria-controls="nav">{MENU_IC}Menu</button>\n'
      f'  </div>\n</header>')

def footer():
    svc = "".join(f'<li><a href="{L(p["slug"])}">{E(p["h1"])}</a></li>' for p in PAGES)
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="fgrid">
      <div><h3>Raja Pagar Surabaya</h3><p>Bengkel las pagar, kanopi, teralis, railing, dan booth usaha di Surabaya sejak 1985.</p><p style="margin-top:10px">Jl. Tanah Merah Utara 166 B, Surabaya<br>Senin–Sabtu, 08.00–16.00 WIB<br>WhatsApp 0856-0798-8227</p><p style="margin-top:10px">Pembayaran: transfer bank, tunai, QRIS</p></div>
      <div><h3>Layanan</h3><ul>{svc}</ul></div>
      <div><h3>Ikuti kami</h3><ul><li><a href="https://www.instagram.com/rajapagarsurabaya" target="_blank" rel="noopener">Instagram</a></li><li><a href="https://www.tiktok.com/@rajapagar_surabaya" target="_blank" rel="noopener">TikTok</a></li><li><a href="https://www.facebook.com/rajapagarsurabaya" target="_blank" rel="noopener">Facebook</a></li><li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li></ul>
      <h3 style="margin-top:18px">Halaman</h3><ul>{"".join(f'<li><a href="{L(s)}">{n}</a></li>' for s,n in NAV[1:])}</ul></div>
    </div>
    <p class="copy">© 2026 Raja Pagar Surabaya. Melindungi rumahmu, melindungi keluargamu.</p>
  </div>
</footer>'''

CONSULT = cut(SRC, '<section class="consult" id="kontak">', '</section>')
def consult(layanan="", bukaan="", heading=None):
    s = CONSULT.replace('<form id="f" novalidate>', f'<form id="f" novalidate data-layanan="{E(layanan)}" data-bukaan="{E(bukaan)}">')
    if heading: s = s.replace("<h2>Ceritakan pagar impian Anda</h2>", f"<h2>{E(heading)}</h2>")
    return s

def fname(k): return P[k][4]
def gal_button(k):
    if not META[k]["tampil"]: return ""
    t, c, loc = P[k][:3]
    return f'<button class="ph" data-c="{c}" data-i="{k}"><img src="img/{fname(k)}.webp" alt="{E(t)}, {E(loc)}" width="888" height="624" loading="lazy"><figcaption><b>{E(t)}</b><span>{E(loc)}</span><span class="spec-hint">Lihat bahan →</span></figcaption></button>'

CAP = {"tim-15":"Pemasangan pagar lipat lisplang oleh tim kami","tim-10":"Pemasangan rangka kanopi","tim-18":"Pemasangan tiang dan rangka kanopi",
       "ulasan-lina-1":"Kanopi pelanggan (foto dari ulasan Google Lina Y.)","ulasan-lina-2":"Atap kanopi pelanggan (foto dari ulasan Google Lina Y.)",
       "tim-16":"Contoh pagar lama yang perlu diperbaiki","tim-05":"Pengelasan ulang pagar di lokasi pelanggan"}

def photo_block(photos):
    nums = [p for p in photos if isinstance(p, int)]
    strs = [p for p in photos if isinstance(p, str)]
    out = ""
    if nums: out += '<div class="gal" id="gal">' + "".join(gal_button(k) for k in nums) + '</div>'
    if strs:
        out += ('<div class="photos" style="margin-top:14px">' if nums else '<div class="photos">') + "".join(
            f'<figure><img src="img/{s}.webp" alt="{E(CAP.get(s,"Pekerjaan Raja Pagar Surabaya"))}" loading="lazy"><figcaption>{E(CAP.get(s,""))}</figcaption></figure>' for s in strs) + '</div>'
    return out

def ld_faq(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
def ld_crumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+"/"+s} for i,(s,n) in enumerate(items)]}

G = [{"t": e[0], "l": e[2], "s": e[3], "n": fname(k)} for k, e in enumerate(P)]
JS = JS.replace('"img/proyek-"+d.n+".webp"', '"img/"+d.n+".webp"')
JS = re.sub(r"var G=\[.*?\];", "var G=" + json.dumps(G, ensure_ascii=False) + ";", JS, count=1, flags=re.S)

def responsive(h):
    from PIL import Image as _I0
    def f(m):
        name = m.group(1)
        if os.path.exists(os.path.join(IMG, name + "-m.webp")):
            W = _I0.open(os.path.join(IMG, name + ".webp")).width
            return f'<img src="img/{name}.webp" srcset="img/{name}-m.webp 700w, img/{name}.webp {W}w" sizes="(max-width:440px) 92vw, (max-width:900px) 46vw, 320px"'
        return m.group(0)
    h = re.sub(r'<img src="img/([a-z0-9-]+)\.webp"(?=[^>]*loading="lazy")(?![^>]*\bid=)', f, h)
    from PIL import Image as _I
    def dims(m):
        tag = m.group(0)
        if " width=" in tag: return tag
        fp = os.path.join(IMG, m.group(1))
        if not os.path.exists(fp): return tag
        w, hh = _I.open(fp).size
        return tag[:-1] + f' width="{w}" height="{hh}">'
    return re.sub(r'<img src="img/([a-z0-9.-]+)"[^>]*>', dims, h)

def page(slug, title, desc, body, lds=(), main_file=False, has_lb=False, og_img="img/og.jpg", og_type="website"):
    og_img = "img/og.jpg"
    url = BASE + "/" + slug
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    fonts = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">'
    head = f'''<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}"><meta property="og:locale" content="id_ID"><meta property="og:site_name" content="Raja Pagar Surabaya">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Raja Pagar Surabaya, jasa pagar dan bengkel las pagar">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#00005C">
<meta name="google-site-verification" content="XEkNs8iCqzq4z6C6NgqM39nXdRaJjo9ZIwRbkREuTw0">
<meta name="google-site-verification" content="6fdN-ZP9q03yXtiF5I26v_cpKBVvvsS5lZbcqPuyaT0">
<link rel="icon" href="favicon.png" type="image/png"><link rel="apple-touch-icon" href="apple-touch-icon.png">
{fonts}'''
    if MODE == "prod":
        style = '<link rel="stylesheet" href="assets/style.css">'
        script = '<script src="assets/main.js" defer></script>'
    else:
        style = "<style>" + CSS + "</style>"
        script = "<script>\n(function(){" + JS + "</script>"
    body = responsive(body)
    bodyhtml = f'''{header(slug)}
<main>
{body}
</main>
{footer()}
{LB if has_lb else ""}
{ld}
{FAB}
{script}'''
    if MODE == "preview" and main_file:
        return f'{head.split(chr(10))[0]}\n<meta name="claude:viewport-fit-sides" content="cover">\n{chr(10).join(head.split(chr(10))[1:])}\n{style}\n{bodyhtml}'
    return f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
{style}
</head>
<body>
{bodyhtml}
</body>
</html>'''

pages = {}

# ---------- Beranda (struktur ala Bravo)
HOME_GAL = []
for k in BARU + [U(i) for i in [16,0,1,5,14,12,7,9]]:
    if k is not None and META[k]["tampil"] and k not in HOME_GAL: HOME_GAL.append(k)
HOME_GAL = HOME_GAL[:8]
def sec(id_):
    return cut(SRC, f'<section id="{id_}"', '</section>')

CARDS = [("pagar-minimalis-surabaya","Pagar Minimalis","img/proyek-01.webp","Jeruji rapi dan plat sesuai kebutuhan privasi."),
         ("pagar-sliding-surabaya","Pagar Sliding","img/proyek-19.webp","Sliding biasa, ganda, dan swing untuk carport."),
         ("pagar-laser-cutting-surabaya","Pagar Laser Cutting","img/proyek-09.webp","Plat berpola potong laser, motif bisa custom."),
         ("pagar-lisplang-surabaya","Pagar Lisplang","img/proyek-16.webp","Bilah motif kayu di rangka besi."),
         ("pagar-industrial-surabaya","Pagar Industrial","img/proyek-15.webp","Expanded metal, strep, dan aksen emas."),
         ("pagar-lipat-surabaya","Pagar Lipat","img/proyek-08.webp","Hemat ruang untuk gang dan ruko."),
         ("kanopi-surabaya","Kanopi","img/tim-10.webp","Rangka besi untuk carport dan teras."),
         ("railing-tangga-surabaya","Railing Tangga & Balkon","img/proyek-10.webp","Pegangan kokoh, minimalis atau ornamen.")]
cards = "".join(f'<a class="card" href="{L(sl)}"><div class="ci"><img src="{im}" alt="{E(t)} Surabaya buatan Raja Pagar" loading="lazy" width="888" height="624"></div><div class="cb"><h3>{E(t)}</h3><p>{E(d)}</p><span class="more">Selengkapnya →</span></div></a>' for sl,t,im,d in CARDS)
why = "".join(f'<div class="why-item"><div class="why-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ic}</svg></div><div><h3>{E(t)}</h3><p>{E(d)}</p></div></div>' for t,d,ic in bravo.ALASAN)
DONE = ' class="done"'
areas = "".join(f'<li{DONE if k in bravo.ADA_PROYEK else ""}>{E(k)}</li>' for k in bravo.KECAMATAN)
faqh = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q,a in bravo.FAQ)
oq, on, orole = bravo.OWNER

bukaan = sec("bukaan").replace('<p class="lead">Ketuk salah satu sistem untuk melihat gerakannya. Pilihan terbaik bergantung pada lebar lahan dan ruang di depan rumah.</p>',
  f'<p class="lead">Ketuk salah satu sistem untuk melihat gerakannya. Pilihan terbaik bergantung pada lebar lahan dan ruang di depan rumah. Baca detailnya di halaman <a href="{L("pagar-sliding-surabaya")}">pagar sliding</a>, <a href="{L("pagar-lipat-surabaya")}">pagar lipat</a>, dan <a href="{L("pagar-kupu-tarung-surabaya")}">pagar kupu tarung</a>.</p>')
hero = cut(SRC, '<section class="hero" id="beranda">', '</section>')
hero = re.sub(r'<p class="kicker">.*?</p>\s*<h1>.*?</h1>',
  '<p class="kicker">Sejak 1985 · 500+ proyek · Survei gratis</p>\n      <h1><span class="h1-brand">Raja Pagar Surabaya</span><span class="h1-kw">Jasa Pagar &amp; Bengkel Las Pagar di Surabaya</span></h1>\n      <p class="tagline">Melindungi rumahmu, melindungi keluargamu.</p>', hero, count=1, flags=re.S)
hero = hero.replace('<a class="btn btn-ghost" href="#galeri">Lihat Hasil Kerja</a>', f'<a class="btn btn-ghost" href="https://wa.me/{WA}?text=Halo%20Raja%20Pagar%20Surabaya%2C%20saya%20ingin%20konsultasi%20pagar." target="_blank" rel="noopener">Chat WhatsApp</a>')
facts = cut(SRC, '<div class="facts">', '</div>\n</div>')

main = f'''{hero}
{facts}
<div class="pay"><div class="wrap"><b>Pembayaran mudah:</b><span class="pill">Transfer bank</span><span class="pill">Tunai</span><span class="pill">QRIS</span><span>· DP 50%, pelunasan di hari pemasangan</span></div></div>

<section id="layanan">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Ahli pagar Surabaya</p><h2>Layanan kami</h2><p class="lead">Fokus kami pembuatan pagar dengan berbagai style dan sistem bukaan. Kami juga mengerjakan kanopi, teralis, railing, booth usaha, dan reparasi pagar.</p></div>
    <div class="cards">{cards}</div>
    <div class="chiplinks"><span>Layanan lain:</span><a href="{L("pagar-kupu-tarung-surabaya")}">Pagar Kupu Tarung</a><a href="{L("teralis-surabaya")}">Teralis</a><a href="{L("booth-usaha-surabaya")}">Booth Usaha</a><a href="{L("reparasi-pagar-surabaya")}">Reparasi Pagar</a><a href="{L("layanan")}">Semua layanan →</a></div>
  </div>
</section>

<section id="kenapa" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Kenapa memilih kami</p><h2>Pagar kokoh, harga bersahabat</h2></div>
    <div class="why">{why}</div>
  </div>
</section>

<section class="owner" id="owner">
  <div class="wrap">
    <blockquote><p>{E(oq)}</p><footer><b>{E(on)}</b>{E(orole)}</footer></blockquote>
  </div>
</section>

<section id="segmen">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Untuk rumah dan usaha</p><h2>Apa yang ingin Anda lindungi?</h2></div>
    <div class="split">
      <a class="seg" href="{L("pagar-minimalis-surabaya")}"><img src="img/proyek-02.webp" alt="Pagar laser cutting putih untuk rumah tinggal" loading="lazy"><div class="sb"><h3>Rumah Tinggal</h3><p>Pagar depan, railing tangga dan balkon, teralis jendela, dan kanopi carport.</p><ul><li>Pagar</li><li>Railing</li><li>Teralis</li><li>Kanopi</li></ul><span class="more">Lihat pagar rumah →</span></div></a>
      <a class="seg" href="{L("booth-usaha-surabaya")}"><img src="img/proyek-21.webp" alt="Booth usaha buatan Raja Pagar" loading="lazy"><div class="sb"><h3>Usaha &amp; Ruko</h3><p>Pagar lipat untuk ruko, pagar industrial untuk kafe, booth jualan, dan kanopi area usaha.</p><ul><li>Pagar lipat</li><li>Pagar industrial</li><li>Booth usaha</li></ul><span class="more">Lihat booth usaha →</span></div></a>
    </div>
  </div>
</section>

{bukaan}

{sec("paket")}

<section id="reparasi" style="padding-top:0">
  <div class="wrap">
    <div class="repair">
      <img src="img/tim-16.webp" alt="Pagar lama yang perlu diperbaiki" loading="lazy">
      <div class="rb">
        <p class="eyebrow">Reparasi &amp; service pagar</p>
        <h2>Pagar lama berat didorong atau berkarat?</h2>
        <p class="lead" style="margin-top:0">Kami memperbaiki pagar besi, termasuk buatan bengkel lain.</p>
        <ul><li>Ganti roda dan rel pagar sliding</li><li>Las ulang sambungan retak dan engsel turun</li><li>Amplas, cat dasar epoxy, dan cat ulang</li></ul>
        <div class="actions"><a class="btn btn-cta" href="{L("reparasi-pagar-surabaya")}">Lihat layanan reparasi</a><a class="btn btn-line" href="https://wa.me/{WA}?text=Halo%20Raja%20Pagar%20Surabaya%2C%20saya%20ingin%20servis%20pagar.%20Berikut%20fotonya%3A" target="_blank" rel="noopener">Kirim foto via WA</a></div>
      </div>
    </div>
  </div>
</section>

{sec("proses")}

{sec("lapangan")}

<section id="galeri" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Galeri proyek</p><h2>Cari inspirasi pagar Anda</h2><p class="lead">Ketuk foto untuk melihat daftar bahan yang dipakai.</p></div>
    <div class="gal gal8" id="gal">{"".join(gal_button(k) for k in HOME_GAL)}</div>
    <div class="more-link"><a class="btn btn-ghost" style="color:var(--link)" href="{L("galeri")}">Lihat semua {len(VIS)} proyek</a></div>
  </div>
</section>

{sec("testimoni")}

<section id="area" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Area layanan</p><h2>Melayani 31 kecamatan di Surabaya</h2><p class="lead">Survei dan konsultasi gratis di seluruh kecamatan berikut.</p></div>
    <ul class="areas areas-wrap">{areas}</ul>
    <div class="area-note"><span class="lg"><i></i> Ada proyek kami di galeri</span></div>
    <div class="area-cta"><p><b>Lokasi Anda di luar Surabaya?</b> Chat kami dulu untuk cek jadwal di Sidoarjo, Gresik, dan sekitarnya.</p><a class="btn btn-cta" href="https://wa.me/{WA}?text=Halo%20Raja%20Pagar%20Surabaya%2C%20apakah%20bisa%20melayani%20lokasi%20saya%20di%20" target="_blank" rel="noopener">Tanya via WhatsApp</a></div>
  </div>
</section>

<section id="faq" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Pertanyaan umum</p><h2>Sebelum Anda bertanya</h2></div>
    <div class="faq">{faqh}</div>
  </div>
</section>

{consult()}'''
ld_home = dict(LD_BIZ); ld_home["url"] = BASE + "/"
ld_home["paymentAccepted"] = "Transfer bank, Tunai, QRIS"
ld_home["areaServed"] = [{"@type":"City","name":"Surabaya"}] + [{"@type":"AdministrativeArea","name":"Kecamatan " + k + ", Surabaya"} for k in bravo.KECAMATAN]
ld_home["hasMap"] = "https://maps.app.goo.gl/nuU3oVcy5RbrZWRW9"
ld_home["founder"] = {"@type":"Person","name":bravo.OWNER[1]}
pages[""] = page("", "Jasa Pagar Surabaya & Bengkel Las Pagar | Raja Pagar",
  "Raja Pagar Surabaya: jasa pembuatan pagar minimalis, sliding, lipat, laser cutting, lisplang, kanopi, teralis, dan railing sejak 1985. Survei gratis di 31 kecamatan, garansi las 1 tahun.",
  main, [ld_home, ld_faq(bravo.FAQ)], main_file=True, has_lb=True)

# ---------- Halaman layanan
BYSLUG = {p["slug"]: p for p in PAGES}
for p in PAGES:
    s = p["slug"]
    pts = "".join(f'<div class="point"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in p["points"])
    dh, dl = p["detail"]
    rel = "".join(f'<a class="svc" href="{L(r)}"><h3>{E(BYSLUG[r]["h1"])}</h3><p>{E(BYSLUG[r]["short"])}</p><span class="more">Selengkapnya →</span></a>' for r in p["related"])
    faq = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in p["faq"])
    gal = ""
    if p["photos"]:
        gal = f'''<section style="padding-top:0"><div class="wrap"><div class="sec-head"><p class="eyebrow">Contoh pekerjaan</p><h2>{E(p["h1"])} buatan kami</h2>{'<p class="lead">Ketuk foto untuk melihat daftar bahan.</p>' if any(isinstance(x,int) for x in p["photos"]) else ''}</div>{photo_block(p["photos"])}</div></section>'''
    body = f'''<section class="page-hero"><div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><a href="{L("layanan")}">Layanan</a><span>›</span><span>{E(p["h1"])}</span></nav>
  <h1>{E(p["h1"])}</h1>
  <div class="intro">{"".join(f"<p>{E(x)}</p>" for x in p["intro"])}</div>
  <div class="actions"><a class="btn btn-cta" href="#kontak">Konsultasi &amp; Survei Gratis</a><a class="btn btn-ghost" href="https://wa.me/{WA}?text={E(__import__("urllib.parse").parse.quote("Halo Raja Pagar Surabaya, saya ingin tanya tentang " + p["h1"].lower() + "."))}" target="_blank" rel="noopener">Chat WhatsApp</a></div>
</div></section>
<div class="facts"><div class="wrap"><div class="fact"><b>1985</b><span>Berdiri di Surabaya</span></div><div class="fact"><b>500+</b><span>Proyek selesai</span></div><div class="fact"><b>Gratis</b><span>Survei &amp; konsultasi</span></div><div class="fact"><b>1 tahun</b><span>Garansi pengelasan</span></div></div></div>
<section><div class="wrap"><div class="sec-head"><p class="eyebrow">Kenapa Raja Pagar</p><h2>Yang Anda dapatkan</h2></div><div class="points">{pts}</div></div></section>
{gal}
<section style="padding-top:0"><div class="wrap detail"><div><p class="eyebrow">Detail</p><h2>{E(dh)}</h2><p class="lead">Satu desain bisa dibuat dalam paket Ekonomis, Standar, atau Premium. Perbedaannya ada pada ketebalan besi, besi galvanis atau hitam, dan jenis cat.</p></div><ul>{"".join(f"<li>{E(x)}</li>" for x in dl)}</ul></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><p class="eyebrow">Pertanyaan umum</p><h2>Tentang {E(p["h1"].replace(" Surabaya",""))}</h2></div><div class="faq">{faq}<details><summary>Bagaimana sistem pembayarannya?</summary><p>DP 50% saat pesanan disetujui, sisanya dibayar di hari pemasangan. Pembayaran bisa lewat transfer bank, tunai, atau QRIS.</p></details></div></div></section>
{consult(p["form"], p.get("bukaan",""), "Konsultasi " + p["h1"].replace(" Surabaya","").lower())}
<section><div class="wrap"><div class="sec-head"><p class="eyebrow">Layanan terkait</p><h2>Mungkin Anda juga butuh</h2></div><div class="related">{rel}</div></div></section>'''
    svc_ld = {"@context":"https://schema.org","@type":"Service","name":p["h1"],"serviceType":p["h1"].replace(" Surabaya",""),"description":p["desc"],"areaServed":{"@type":"City","name":"Surabaya"},"provider":{"@type":"HomeAndConstructionBusiness","name":"Raja Pagar Surabaya","telephone":"+6285607988227","url":BASE+"/"},"url":BASE+"/"+s}
    og = f'img/{fname(p["photos"][0])}.webp' if p["photos"] and isinstance(p["photos"][0], int) else (f'img/{p["photos"][0]}.webp' if p["photos"] else "img/proyek-17.webp")
    pages[s] = page(s, p["title"], p["desc"], body, [svc_ld, ld_faq(p["faq"]), ld_crumb([("", "Beranda"), ("layanan", "Layanan"), (s, p["h1"])])], has_lb=any(isinstance(x,int) for x in p["photos"]), og_img=og)

# ---------- Layanan (hub)
groups = {}
for p in PAGES: groups.setdefault(p["group"], []).append(p)
hub = "".join(f'''<div class="svc-group"><h2>{E(g)}</h2><div class="svc-grid">{"".join(f'<a class="svc" href="{L(p["slug"])}"><h3>{E(p["h1"])}</h3><p>{E(p["short"])}</p><span class="more">Selengkapnya →</span></a>' for p in ps)}</div></div>''' for g, ps in groups.items())
body = f'''<section class="page-hero"><div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><span>Layanan</span></nav><h1>Layanan Raja Pagar Surabaya</h1><div class="intro"><p>Fokus kami pembuatan pagar dengan berbagai style dan sistem bukaan. Kami juga mengerjakan kanopi, teralis, railing tangga dan balkon, booth usaha, serta reparasi pagar.</p></div></div></section>
<section><div class="wrap">{hub}</div></section>
{consult()}'''
pages["layanan"] = page("layanan", "Layanan Pagar, Kanopi & Railing Surabaya | Raja Pagar",
  "Daftar layanan Raja Pagar Surabaya: pagar minimalis, sliding, lipat, kupu tarung, laser cutting, lisplang, industrial, kanopi, teralis, railing, booth usaha, dan reparasi pagar.",
  body, [ld_crumb([("", "Beranda"), ("layanan", "Layanan")])])

# ---------- Galeri
LAMA = [k for k in VIS if not META[k]["baru"]]
order = BARU + [k for k in LAMA if "Surabaya" in P[k][2]] + [k for k in LAMA if "Surabaya" not in P[k][2] and P[k][1] != "booth"] + [k for k in LAMA if P[k][1] == "booth"]
_cats = [c for c in DATA.CAT_LABEL if any(P[k][1] == c for k in VIS)]
filters = '<div class="filters" role="group" aria-label="Filter galeri"><button class="chip" data-f="all" aria-pressed="true">Semua</button>' + "".join(f'<button class="chip" data-f="{c}" aria-pressed="false">{DATA.CAT_LABEL[c]}</button>' for c in _cats) + '</div>' 
body = f'''<section class="page-hero"><div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><span>Galeri</span></nav><h1>Galeri Proyek Pagar Surabaya</h1><div class="intro"><p>{len(VIS)} proyek pagar, railing, dan booth usaha buatan Raja Pagar di Surabaya, Sidoarjo, dan Gresik. Ketuk foto untuk melihat daftar bahan yang dipakai.</p></div></div></section>
<section><div class="wrap">{filters}<div class="gal" id="gal">{"".join(gal_button(k) for k in order)}</div></div></section>
{consult()}'''
pages["galeri"] = page("galeri", "Galeri Proyek Pagar Surabaya | Raja Pagar Surabaya",
  f"Lihat {len(VIS)} proyek pagar minimalis, sliding, lipat, laser cutting, lisplang, industrial, railing, dan booth usaha buatan Raja Pagar Surabaya lengkap dengan spesifikasi bahan.",
  body, [ld_crumb([("", "Beranda"), ("galeri", "Galeri")])], has_lb=True)

# ---------- Tentang kami
team = ["tim-01","tim-02","tim-03","tim-04","tim-08","tim-10","tim-11","tim-13","tim-14","tim-15"]
tcap = {"tim-01":"Memasang daun pagar","tim-02":"Persiapan pengelasan di lokasi","tim-03":"Menyetel pagar dengan waterpass","tim-04":"Panel laser cutting setelah dicat","tim-08":"Pemasangan pagar laser cutting","tim-10":"Pemasangan rangka kanopi","tim-11":"Pemasangan rel pagar sliding","tim-13":"Pemasangan di Semampir","tim-14":"Mengebor dudukan tiang","tim-15":"Pemasangan pagar lipat lisplang"}
quotes = cut(SRC, '<div class="testi"', '</div>\n    <div class="g-rate">')[:-len('\n    <div class="g-rate">')]
body = f'''<section class="page-hero"><div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><span>Tentang Kami</span></nav><h1>Tentang Raja Pagar Surabaya</h1><div class="intro"><p>Berdiri sejak 1985, Raja Pagar Surabaya adalah bengkel las yang fokus pada pembuatan pagar rumah. Lebih dari 500 proyek sudah kami selesaikan, dari pagar minimalis di gang sampai pagar laser cutting untuk rumah dua lantai.</p></div></div></section>
<div class="facts"><div class="wrap"><div class="fact"><b>1985</b><span>Berdiri di Surabaya</span></div><div class="fact"><b>500+</b><span>Proyek selesai</span></div><div class="fact"><b>±14 hari</b><span>Rata-rata pengerjaan</span></div><div class="fact"><b>1 tahun</b><span>Garansi pengelasan</span></div></div></div>
<section><div class="wrap detail"><div><p class="eyebrow">Cara kami bekerja</p><h2>Melindungi rumahmu, melindungi keluargamu</h2></div><div class="prose">
<p>Pagar adalah pelindung pertama sebuah rumah. Karena itu kami mengerjakan setiap pagar seolah untuk rumah kami sendiri: diukur langsung saat survei, dilas di workshop oleh tenaga berpengalaman, lalu dipasang dan disetel di lokasi.</p>
<p>Kami percaya pagar yang bagus tidak harus mahal. Itulah sebabnya satu desain bisa dibuat dalam tiga paket, Ekonomis, Standar, dan Premium, dengan bahan yang tertulis jelas di penawaran.</p>
<p>Pelanggan kami paling sering menyebut tiga hal di ulasan Google: harga terjangkau, owner yang ramah, dan pengerjaan yang cepat. Itu yang terus kami jaga.</p>
<p>Workshop kami berada di Jl. Tanah Merah Utara 166 B, Surabaya. Saat ini kami fokus melayani Surabaya, dan juga pernah mengerjakan proyek di Sidoarjo dan Gresik.</p>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><p class="eyebrow">Tim di lapangan</p><h2>Rajapagar on duty</h2></div><div class="photos">{"".join(f'<figure><img src="img/{t}.webp" alt="Tim Raja Pagar Surabaya: {E(tcap[t].lower())}" loading="lazy" style="aspect-ratio:4/5"><figcaption>{E(tcap[t])}</figcaption></figure>' for t in team)}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><p class="eyebrow">Ulasan Google</p><h2>Kata pelanggan kami</h2></div>{quotes}<div class="g-rate"><p class="g-score"><b>5,0</b> <span class="stars" aria-hidden="true">★★★★★</span> dari 21 ulasan Google</p><a class="btn btn-ghost" style="color:var(--link)" href="https://maps.app.goo.gl/nuU3oVcy5RbrZWRW9" target="_blank" rel="noopener">Lihat semua ulasan di Google</a></div></div></section>
{consult()}'''
pages["tentang-kami"] = page("tentang-kami", "Tentang Raja Pagar Surabaya, Bengkel Las Pagar Sejak 1985",
  "Raja Pagar Surabaya berdiri sejak 1985 dengan lebih dari 500 proyek pagar, kanopi, dan railing. Kenali tim dan cara kerja kami.",
  body, [ld_crumb([("", "Beranda"), ("tentang-kami", "Tentang Kami")])], og_img="img/tim-08.webp")

# ---------- Kontak
mapblock = ('<div class="map-wrap"><iframe title="Lokasi workshop Raja Pagar Surabaya" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Jl.+Tanah+Merah+Utara+166+B+Surabaya&amp;output=embed"></iframe></div>'
            if MODE == "prod" else '<p class="lead">Peta Google Maps tampil di versi website asli.</p>')
body = f'''<section class="page-hero"><div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><span>Kontak</span></nav><h1>Kontak Raja Pagar Surabaya</h1><div class="intro"><p>Konsultasi dan survei gratis untuk area Surabaya. Cara tercepat menghubungi kami adalah lewat WhatsApp.</p></div><div class="actions"><a class="btn btn-cta" href="https://wa.me/{WA}?text=Halo%20Raja%20Pagar%20Surabaya%2C%20saya%20ingin%20konsultasi." target="_blank" rel="noopener">Chat WhatsApp 0856-0798-8227</a></div></div></section>
<section><div class="wrap detail"><div><p class="eyebrow">Workshop</p><h2>Jl. Tanah Merah Utara 166 B, Surabaya</h2><p class="lead">Buka Senin–Sabtu, 08.00–16.00 WIB.</p><p class="g-score" style="margin-top:10px"><b>5,0</b> <span class="stars" aria-hidden="true">★★★★★</span> dari 21 ulasan Google</p><div class="more-link"><a class="btn btn-ghost" style="color:var(--link)" href="https://maps.app.goo.gl/nuU3oVcy5RbrZWRW9" target="_blank" rel="noopener">Buka di Google Maps</a></div></div>{mapblock}</div></section>
{consult()}'''
pages["kontak"] = page("kontak", "Kontak Raja Pagar Surabaya | WA 0856-0798-8227",
  "Hubungi Raja Pagar Surabaya lewat WhatsApp 0856-0798-8227. Workshop di Jl. Tanah Merah Utara 166 B Surabaya, buka Senin–Sabtu 08.00–16.00 WIB.",
  body, [ld_home, ld_crumb([("", "Beranda"), ("kontak", "Kontak")])])

# ---------- Blog
CSS += r"""
.post-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
@media (max-width:760px){.post-grid{grid-template-columns:1fr}}
.post-card{display:grid;grid-template-columns:1fr;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;text-decoration:none;color:var(--ink);transition:border-color .2s,transform .2s}
.post-card:hover{border-color:var(--navy);transform:translateY(-3px)}
.post-card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.post-card .pb{padding:18px;display:grid;gap:8px}
.post-card p{color:var(--muted);font-size:.94rem}
.meta{font-family:var(--mono);font-size:.72rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase}
.page-hero .meta{color:var(--on-navy-muted)}
.article{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:48px;align-items:start}
@media (max-width:900px){.article{grid-template-columns:1fr}}
.prose-a{display:grid;gap:18px;font-size:1.05rem;line-height:1.75;min-width:0;max-width:70ch}
.prose-a h2{font-size:1.55rem;margin-top:18px}
.prose-a ul,.prose-a ol{margin:0;padding-left:22px;display:grid;gap:8px}
.prose-a figure{margin:6px 0;border-radius:var(--r);overflow:hidden;border:1px solid var(--line);background:var(--surface)}
.prose-a figure img{display:block;width:100%;aspect-ratio:888/624;object-fit:cover}
.prose-a figcaption{padding:10px 14px;font-size:.88rem;color:var(--muted)}
.prose-a .tip{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--yellow);border-radius:var(--r);padding:14px 18px;font-size:.98rem}
.prose-a .tbl{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r)}
.prose-a table{border-collapse:collapse;width:100%;min-width:520px;font-size:.94rem;background:var(--surface)}
.prose-a th,.prose-a td{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.prose-a th{background:var(--navy);color:var(--on-navy);font-weight:600}
.prose-a tr:last-child td{border-bottom:0}
.prose-a .cta-box{background:var(--navy);color:var(--on-navy);border-radius:var(--r);padding:22px;display:grid;gap:14px;margin-top:10px}
.prose-a .cta-box p{color:var(--on-navy)}
.prose-a .cta-box .btn{justify-self:start}
.aside{position:sticky;top:calc(90px + env(safe-area-inset-top,0px));display:grid;gap:14px}
@media (max-width:900px){.aside{position:static}}
.aside-box{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:18px;display:grid;gap:10px}
.aside-box h3{font-size:1rem}
.aside-box a{color:var(--link);font-size:.94rem}
.aside-box ul{margin:0;padding:0;list-style:none;display:grid;gap:8px}
"""

import urllib.parse
def render_article(a):
    h = DATA.render_md(a["body"])
    q = urllib.parse.quote(f"Halo Raja Pagar Surabaya, saya baru membaca artikel \"{a['title']}\" di website. Saya ingin konsultasi.")
    return h + f'<div class="cta-box"><p>{E(a["ajakan"])}</p><a class="btn btn-cta" href="https://wa.me/{WA}?text={q}" target="_blank" rel="noopener">Chat WhatsApp</a></div>'

def tgl(d):
    y, m, dd = d.split("-")
    return f"{int(dd)} {['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'][int(m)-1]} {y}"

for a in ARTIKEL:
    s = a["slug"]
    others = [x for x in ARTIKEL if x["slug"] != s]
    aside = f'''<aside class="aside">
  <div class="aside-box"><h3>Konsultasi gratis</h3><p style="color:var(--muted);font-size:.94rem">Survei gratis di 31 kecamatan Surabaya. Pengelasan bergaransi 1 tahun.</p><a class="btn btn-cta" href="https://wa.me/{WA}" target="_blank" rel="noopener" style="color:var(--on-yellow)">Chat WhatsApp</a></div>
  <div class="aside-box"><h3>Layanan terkait</h3><ul>{"".join(f'<li><a href="{L(r)}">{E(BYSLUG[r]["h1"])}</a></li>' for r in a["related_svc"] if r in BYSLUG)}</ul></div>
  <div class="aside-box"><h3>Artikel lainnya</h3><ul>{"".join(f'<li><a href="{L(o["slug"])}">{E(o["title"])}</a></li>' for o in others)}</ul></div>
</aside>'''
    body = f'''<section class="page-hero"><div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><a href="{L("blog")}">Blog</a><span>›</span><span>{E(a["title"].split(":")[0])}</span></nav>
  <p class="meta">{tgl(a["date"])} · {a["menit"]} menit baca · Tim Raja Pagar Surabaya</p>
  <h1 style="text-transform:none;font-size:clamp(1.9rem,4.4vw,3rem);margin-top:10px">{E(a["h1"])}</h1>
</div></section>
<section><div class="wrap article">
  <article class="prose-a">{render_article(a)}</article>
  {aside}
</div></section>'''
    ld_art = {"@context":"https://schema.org","@type":"BlogPosting","headline":a["h1"],"description":a["desc"],
              "image":f'{BASE}/img/{a["cover"]}.webp',"datePublished":a["date"],"dateModified":a["date"],
              "inLanguage":"id-ID","mainEntityOfPage":f"{BASE}/{s}",
              "author":{"@type":"Organization","name":"Raja Pagar Surabaya","url":BASE+"/"},
              "publisher":{"@type":"Organization","name":"Raja Pagar Surabaya","logo":{"@type":"ImageObject","url":BASE+"/img/logo.png"}}}
    pages[s] = page(s, a["title"] if len(a["title"]) <= 62 else a["title"][:62], a["desc"], body,
                    [ld_art, ld_crumb([("", "Beranda"), ("blog", "Blog"), (s, a["title"])])], og_type="article")

cards_b = "".join(f'''<a class="post-card" href="{L(a["slug"])}"><img src="img/{a["cover"]}.webp" alt="{E(a["title"])}" width="888" height="624" loading="lazy"><div class="pb"><p class="meta">{a["menit"]} menit baca</p><h2 style="font-size:1.3rem">{E(a["title"])}</h2><p>{E(a["excerpt"])}</p><span class="more" style="font-weight:600;color:var(--link)">Baca artikel →</span></div></a>''' for a in ARTIKEL)
body = f'''<section class="page-hero"><div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><span>Blog</span></nav><h1>Blog &amp; Tips Pagar</h1><div class="intro"><p>Panduan memilih, menghitung, dan merawat pagar besi dari tim Raja Pagar Surabaya, berdasarkan pengalaman sejak 1985.</p></div></div></section>
<section><div class="wrap"><div class="post-grid">{cards_b}</div></div></section>
{consult()}'''
pages["blog"] = page("blog", "Blog & Tips Pagar Besi | Raja Pagar Surabaya",
  "Tips dan panduan pagar dari Raja Pagar Surabaya: harga pagar minimalis per meter, model pagar terbaru, pagar sliding vs lipat, dan cara merawat pagar besi.",
  body, [ld_crumb([("", "Beranda"), ("blog", "Blog")])])


# ---------- 404
pages["404"] = page("404", "Halaman tidak ditemukan | Raja Pagar Surabaya", "Halaman yang Anda cari tidak ada.",
  f'<section class="page-hero"><div class="wrap"><h1>Halaman tidak ditemukan</h1><div class="intro"><p>Alamat yang Anda buka mungkin salah ketik atau sudah dipindah.</p></div><div class="actions"><a class="btn btn-cta" href="{L("")}">Kembali ke beranda</a><a class="btn btn-ghost" href="{L("layanan")}">Lihat layanan</a></div></div></section>')
pages["404"] = pages["404"].replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')

# galeri: foto teratas jangan lazy (LCP)
_g = pages["galeri"]; _i = _g.index('id="gal"')
pages["galeri"] = _g[:_i] + _g[_i:].replace('loading="lazy"', 'loading="eager"', 4)
# ---------- Tulis
os.makedirs(OUT + "/assets", exist_ok=True)
if os.path.isdir(os.path.join(DATA.ROOT, "admin")):
    shutil.copytree(os.path.join(DATA.ROOT, "admin"), os.path.join(OUT, "admin"))
for s, h in pages.items():
    open(os.path.join(OUT, ("index" if s == "" else s) + ".html"), "w", encoding="utf-8").write(h)
if MODE == "prod":
    open(OUT + "/assets/style.css", "w").write(CSS)
    open(OUT + "/assets/main.js", "w").write("(function(){" + JS)
    LASTMOD = {a["slug"]: a["date"] for a in ARTIKEL}
    urls = [""] + [p["slug"] for p in PAGES] + ["layanan", "galeri", "blog"] + [a["slug"] for a in ARTIKEL] + ["tentang-kami", "kontak"]
    open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{BASE}/{u}</loc><lastmod>{LASTMOD.get(u, TODAY)}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {BASE}/sitemap.xml\n")
    open(OUT + "/_headers", "w").write("/img/*\n  Cache-Control: public, max-age=604800\n/assets/*\n  Cache-Control: public, max-age=604800\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n")
    open(OUT + "/_redirects", "w").write("/service-pagar-surabaya  /reparasi-pagar-surabaya  301\n")
else:
    os.rename(os.path.join(OUT, "404.html"), os.path.join(OUT, "halaman-404.html"))
print(MODE, "->", OUT, len(pages), "halaman")
