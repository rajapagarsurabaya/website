"""Membaca konten dari folder content/ (diedit lewat panel admin) dan mengolah foto proyek."""
import os, re, glob, datetime, shutil
import yaml, markdown
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
STATIC = os.path.join(ROOT, "static")
MEDIA = os.path.join(STATIC, "img", "proyek")

KECAMATAN = ["Asemrowo","Benowo","Bubutan","Bulak","Dukuh Pakis","Gayungan","Genteng","Gubeng","Gunung Anyar","Jambangan","Karang Pilang","Kenjeran","Krembangan","Lakarsantri","Mulyorejo","Pabean Cantian","Pakal","Rungkut","Sambikerep","Sawahan","Semampir","Simokerto","Sukolilo","Sukomanunggal","Tambaksari","Tandes","Tegalsari","Tenggilis Mejoyo","Wiyung","Wonocolo","Wonokromo"]

STYLE_CAT = {"Minimalis": "minimalis", "Lisplang": "lisplang", "Laser cutting": "laser", "Industrial": "industrial", "Kombinasi": "kombinasi"}
JENIS_CAT = {"Railing tangga": "railing", "Railing balkon": "railing", "Kanopi": "kanopi", "Teralis": "teralis", "Booth usaha": "booth", "Reparasi pagar": "reparasi"}
CAT_LABEL = {"minimalis": "Minimalis", "lisplang": "Lisplang", "laser": "Laser Cutting", "industrial": "Industrial", "kombinasi": "Kombinasi",
             "railing": "Railing", "kanopi": "Kanopi", "teralis": "Teralis", "booth": "Booth Usaha", "reparasi": "Reparasi"}
# halaman layanan yang otomatis menampilkan proyek baru
STYLE_PAGE = {"Minimalis": "pagar-minimalis-surabaya", "Lisplang": "pagar-lisplang-surabaya", "Laser cutting": "pagar-laser-cutting-surabaya",
              "Industrial": "pagar-industrial-surabaya", "Kombinasi": "pagar-industrial-surabaya"}
BUKAAN_PAGE = {"Sliding": "pagar-sliding-surabaya", "Sliding ganda": "pagar-sliding-surabaya", "Sliding swing": "pagar-sliding-surabaya",
               "Lipat": "pagar-lipat-surabaya", "Kupu tarung": "pagar-kupu-tarung-surabaya"}
JENIS_PAGE = {"Railing tangga": "railing-tangga-surabaya", "Railing balkon": "railing-balkon-surabaya", "Kanopi": "kanopi-surabaya",
              "Teralis": "teralis-surabaya", "Booth usaha": "booth-usaha-surabaya", "Reparasi pagar": "reparasi-pagar-surabaya"}


def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s or "foto"


def load_fm(path):
    txt = open(path, encoding="utf-8").read()
    if txt.startswith("---"):
        _, fm, body = txt.split("---", 2)
        return yaml.safe_load(fm) or {}, body.strip()
    return {}, txt


def as_date(v):
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.strftime("%Y-%m-%d")
    v = str(v or "")[:10]
    return v if re.match(r"\d{4}-\d{2}-\d{2}$", v) else datetime.date.today().isoformat()


# ---------- Foto: semua file di static/img/proyek diolah ke dist/img/<nama>.webp (+ -m.webp untuk HP)
STEM = {}     # path publik (/img/proyek/x.jpg) -> stem


def process_media(out_img):
    os.makedirs(out_img, exist_ok=True)
    for fp in sorted(glob.glob(os.path.join(MEDIA, "*"))):
        name = os.path.basename(fp)
        base, ext = os.path.splitext(name)
        if ext.lower() not in (".webp", ".jpg", ".jpeg", ".png", ".gif", ".heic"):
            continue
        stem = slugify(base)
        try:
            im = Image.open(fp)
            im = im.convert("RGB")
        except Exception as e:
            print("  ! foto tidak bisa dibuka:", name, e)
            continue
        main = os.path.join(out_img, stem + ".webp")
        if ext.lower() == ".webp" and im.width <= 1200:
            shutil.copy(fp, main)          # foto lama sudah dikompres, jangan dikompres ulang
        else:
            big = im.copy(); big.thumbnail((1200, 1600))
            big.save(main, "WEBP", quality=76, method=6)
        mw = Image.open(main)
        if mw.width > 700:
            sm = mw.convert("RGB"); sm.thumbnail((700, 1000))
            sm.save(os.path.join(out_img, stem + "-m.webp"), "WEBP", quality=72, method=6)
        STEM["/img/proyek/" + name] = stem
        STEM["img/proyek/" + name] = stem


def stem_of(path):
    path = (path or "").strip()
    if path in STEM:
        return STEM[path]
    return slugify(os.path.splitext(os.path.basename(path))[0])


# Nama foto deskriptif untuk Google: "38294.webp" -> "pagar-minimalis-sliding-mulyorejo-surabaya.webp"
_USED = set()
def descriptive(out_img, stem, text):
    src = os.path.join(out_img, stem + ".webp")
    if not os.path.exists(src):
        return stem
    base = slugify(text)[:70].strip("-")
    words = []
    for w in base.split("-"):          # buang kata ganda, mis. "surabaya-surabaya"
        if w not in words: words.append(w)
    base = "-".join(words)
    new, n = base, 2
    while new in _USED or (os.path.exists(os.path.join(out_img, new + ".webp")) and new != stem):
        new = f"{base}-{n}"; n += 1
    _USED.add(new)
    if new != stem:
        shutil.copy(src, os.path.join(out_img, new + ".webp"))
        if os.path.exists(os.path.join(out_img, stem + "-m.webp")):
            shutil.copy(os.path.join(out_img, stem + "-m.webp"), os.path.join(out_img, new + "-m.webp"))
    return new


# ---------- Proyek
def load_proyek(out_img=None):
    items = []
    for fp in glob.glob(os.path.join(CONTENT, "proyek", "*.yml")) + glob.glob(os.path.join(CONTENT, "proyek", "*.yaml")):
        try:
            d = yaml.safe_load(open(fp, encoding="utf-8")) or {}
        except Exception as e:      # satu file rusak tidak boleh menggagalkan seluruh website
            print("  ! proyek dilewati (file tidak terbaca):", os.path.basename(fp), e)
            continue
        if not isinstance(d, dict) or not d.get("judul") or not d.get("foto"):
            print("  ! proyek dilewati (judul/foto kosong):", os.path.basename(fp))
            continue
        d["_file"] = os.path.basename(fp)
        items.append(d)
    lama = sorted([d for d in items if d.get("urutan")], key=lambda d: int(d["urutan"]))
    baru = sorted([d for d in items if not d.get("urutan")], key=lambda d: (as_date(d.get("tanggal")), d["_file"]), reverse=True)
    P, META = [], []
    for d in lama + baru:
        jenis = d.get("jenis") or "Pagar"
        style = d.get("style") or "Tidak ada"
        bukaan = d.get("bukaan") or "Tidak ada"
        if jenis == "Pagar":
            cat = STYLE_CAT.get(style, "minimalis")
        else:
            cat = JENIS_CAT.get(jenis, "minimalis")
        kec = d.get("kecamatan") or ""
        lain = (d.get("lokasi_lain") or "").strip()
        if kec and kec in KECAMATAN:
            loc = f"{kec}, Surabaya"
        else:
            loc = lain or "Surabaya"
        bahan = [str(x).strip() for x in (d.get("bahan") or []) if str(x).strip()]
        stem = stem_of(d["foto"])
        if out_img and not os.path.exists(os.path.join(out_img, stem + ".webp")):
            print("  ! proyek dilewati (file foto tidak ditemukan):", d["_file"], d["foto"])
            continue
        if out_img and not d.get("urutan"):
            stem = descriptive(out_img, stem, f'{d["judul"]} {kec if kec in KECAMATAN else lain} surabaya' if kec in KECAMATAN else f'{d["judul"]} {lain}')
        P.append((str(d["judul"]).strip(), cat, loc, bahan, stem))
        pages = set()
        if jenis == "Pagar":
            if style in STYLE_PAGE: pages.add(STYLE_PAGE[style])
            if bukaan in BUKAAN_PAGE: pages.add(BUKAAN_PAGE[bukaan])
        elif jenis in JENIS_PAGE:
            pages.add(JENIS_PAGE[jenis])
        META.append({"urutan": d.get("urutan"), "baru": not d.get("urutan"), "tampil": d.get("tampilkan", True) is not False,
                     "tanggal": as_date(d.get("tanggal")), "pages": pages})
    return P, META


# ---------- Artikel
def load_artikel(out_img=None):
    out = []
    for fp in glob.glob(os.path.join(CONTENT, "artikel", "*.md")):
        try:
            fm, body = load_fm(fp)
        except Exception as e:
            print("  ! artikel dilewati (file tidak terbaca):", os.path.basename(fp), e)
            continue
        if not isinstance(fm, dict): continue
        cover = stem_of(fm.get("sampul") or "")
        if out_img and not os.path.exists(os.path.join(out_img, cover + ".webp")):
            cover = "proyek-17"      # sampul kosong atau hilang: pakai foto bawaan
        if fm.get("tampilkan") is False or not fm.get("judul"):
            continue
        slug = slugify(os.path.splitext(os.path.basename(fp))[0])
        words = len(re.findall(r"\w+", body))
        out.append({
            "slug": slug,
            "title": str(fm["judul"]).strip(),
            "h1": str(fm.get("judul_lengkap") or fm["judul"]).strip(),
            "desc": str(fm.get("deskripsi") or fm.get("ringkasan") or fm["judul"]).strip(),
            "excerpt": str(fm.get("ringkasan") or fm.get("deskripsi") or "").strip(),
            "cover": cover,
            "file": os.path.basename(fp),
            "date": as_date(fm.get("tanggal")),
            "menit": max(2, round(words / 180)),
            "related_svc": list(fm.get("layanan_terkait") or []),
            "ajakan": str(fm.get("ajakan") or "Konsultasi gratis lewat WhatsApp. Kirim foto lokasi dan ukuran pagar Anda.").strip(),
            "body": body,
        })
    out.sort(key=lambda a: (a["date"], a["slug"]), reverse=True)
    return out


MD = markdown.Markdown(extensions=["tables", "sane_lists"])


def render_md(body):
    MD.reset()
    h = MD.convert(body)

    def fig(m):
        attrs = m.group(1)
        src = re.search(r'src="([^"]+)"', attrs); alt = re.search(r'alt="([^"]*)"', attrs)
        src = src.group(1) if src else ""; alt = alt.group(1) if alt else ""
        if "/img/proyek/" in src or src.startswith("img/proyek/"):
            src = "img/" + stem_of(src) + ".webp"
        cap = f"<figcaption>{alt}</figcaption>" if alt else ""
        return f'<figure><img src="{src}" alt="{alt}" loading="lazy">{cap}</figure>'
    h = re.sub(r"<p>\s*<img ([^>]*?)\s*/?>\s*</p>", fig, h)
    h = re.sub(r"<img ((?![^>]*loading=)[^>]*?)\s*/?>", lambda m: fig(m).replace("<figure>", "").replace("</figure>", "") if "/img/proyek/" in m.group(1) else m.group(0), h)
    h = h.replace("<blockquote>", '<div class="tip">').replace("</blockquote>", "</div>")
    h = h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return h
