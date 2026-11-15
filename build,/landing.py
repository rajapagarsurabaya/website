"""Landing page khusus: Pagar Laser Cutting Surabaya.

Menggantikan halaman layanan biasa di alamat /pagar-laser-cutting-surabaya
(alamat lama dipertahankan supaya nilai SEO-nya tidak hilang).
Halaman ini dipakai untuk Google sekaligus tujuan iklan dan link bio IG/TikTok.

Dipanggil dari gen.py:  import landing; landing.buat(globals())
"""
import json, urllib.parse

SLUG = "pagar-laser-cutting-surabaya"

TITLE = "Pagar Laser Cutting Surabaya, Motif Custom | Raja Pagar"
DESC = ("Jasa pagar laser cutting Surabaya sejak 1985. Motif daun, bunga, geometris, atau custom. "
        "Survei gratis di 31 kecamatan, garansi las 1 tahun. Chat WhatsApp sekarang.")

APA = [
    "Pagar laser cutting adalah pagar besi yang isiannya berupa plat besi berpola. Polanya dipotong dengan mesin laser, "
    "jadi garisnya presisi dan rapi, sesuatu yang sulit didapat kalau dipotong manual.",
    "Kelebihannya, rumah jadi lebih tertutup dari pandangan orang di jalan, tapi cahaya dan udara tetap bisa masuk lewat celah motifnya. "
    "Tampilannya juga langsung terlihat mewah dan beda dari pagar jeruji biasa.",
    "Panel laser bisa dipasang penuh dari bawah sampai atas, atau dikombinasikan dengan jeruji dan plat polos supaya lebih hemat. "
    "Semua sistem bukaan bisa: sliding, sliding ganda, sliding swing, kupu tarung, maupun lipat.",
]

POIN = [
    ("Motif bebas pilih", "Daun, bunga, geometris, kaligrafi, atau gambar dari Anda sendiri."),
    ("Privasi tetap terjaga", "Pandangan dari luar terhalang, sirkulasi udara tetap jalan."),
    ("Plat 1,2 mm sampai 2 mm", "Ketebalan plat menyesuaikan paket dan ukuran panel."),
    ("Warna bisa dikombinasi", "Panel bisa dicat beda dari rangka, misalnya hijau dengan aksen kuning."),
]

SPEK = ["Rangka pipa kotak 40x80 mm atau 50x100 mm",
        "Plat laser cutting 1,2 mm atau 2 mm",
        "Bingkai panel pipa kotak 15x35 mm",
        "Pilihan besi galvanis atau besi hitam",
        "Cat dasar epoxy filler, lalu cat akhir Nippe 2000"]

FAQ = [
    ("Bisa pakai motif sendiri?",
     "Bisa. Kirim gambar atau foto motif yang Anda suka lewat WhatsApp, nanti tim kami sesuaikan dengan ukuran panel pagar Anda."),
    ("Apakah plat laser cutting mudah berkarat?",
     "Plat diberi cat dasar epoxy filler sebelum cat akhir untuk menahan karat. Perawatannya cukup dibersihkan rutin dan dicat ulang kalau warnanya mulai kusam."),
    ("Apakah pagar laser cutting lebih mahal dari pagar minimalis?",
     "Umumnya sedikit lebih tinggi karena ada biaya potong laser. Kabar baiknya, satu desain bisa dibuat dalam paket Ekonomis, Standar, atau Premium, jadi bisa disesuaikan dengan anggaran. Kirim ukuran dan motif lewat WhatsApp untuk penawarannya."),
    ("Sistem bukaan apa saja yang bisa dipakai?",
     "Semua sistem bisa: sliding, sliding ganda, sliding swing, kupu tarung, dan lipat. Tim kami akan menyarankan yang paling pas saat survei."),
    ("Berapa lama pagar laser cutting selesai dibuat?",
     "Rata-rata 14 hari kerja sejak DP diterima, tergantung ukuran dan tingkat kerumitan motif."),
    ("Apakah survei dikenakan biaya?",
     "Tidak. Survei dan konsultasi gratis untuk seluruh 31 kecamatan di Surabaya."),
    ("Bagaimana sistem pembayarannya?",
     "DP 50% saat pesanan disetujui, sisanya dibayar di hari pemasangan. Bisa lewat transfer bank, tunai, atau QRIS."),
    ("Apa garansinya?",
     "Pengelasan bergaransi 1 tahun sejak pagar terpasang."),
]

CAP = {"tim-04": "Panel laser cutting setelah dicat, siap dipasang",
       "tim-08": "Tim kami memasang pagar laser cutting"}


def buat(g):
    E, L, WA = g["E"], g["L"], g["WA"]
    P, sec, consult, photo_block, fname = g["P"], g["sec"], g["consult"], g["photo_block"], g["fname"]
    bravo, BASE, BYSLUG = g["bravo"], g["BASE"], g["BYSLUG"]
    p = BYSLUG[SLUG]
    g["CAP"].update(CAP)

    def wa(teks):
        return f"https://wa.me/{WA}?text=" + urllib.parse.quote(teks)
    wa_utama = wa("Halo Raja Pagar Surabaya, saya tertarik pagar laser cutting. Boleh minta info dan jadwal survei?")
    wa_motif = wa("Halo Raja Pagar Surabaya, saya mau kirim contoh motif pagar laser cutting. Berikut gambarnya:")

    proyek = [x for x in p["photos"] if isinstance(x, int)]
    foto = proyek + ["tim-04", "tim-08"]
    if proyek:
        k = proyek[0]
        hero_img = f'img/{fname(k)}.webp'
        hero_alt = f"{P[k][0]} di {P[k][2]}, buatan Raja Pagar Surabaya"
        hero_cap = f"{P[k][0]} · {P[k][2]}"
    else:
        hero_img, hero_alt, hero_cap = "img/tim-04.webp", CAP["tim-04"], CAP["tim-04"]

    poin = "".join(f'<div class="point"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in POIN)
    why = "".join(f'<div class="why-item"><div class="why-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ic}</svg></div><div><h3>{E(t)}</h3><p>{E(d)}</p></div></div>' for t, d, ic in bravo.ALASAN)
    faq = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
    areas = "".join(f'<li>{E(k)}</li>' for k in bravo.KECAMATAN)
    rel = "".join(f'<a class="svc" href="{L(r)}"><h3>{E(BYSLUG[r]["h1"])}</h3><p>{E(BYSLUG[r]["short"])}</p><span class="more">Selengkapnya →</span></a>' for r in p["related"])

    paket = sec("paket").replace("Tanyakan detail dan harga tiap paket lewat WhatsApp.",
                                 "Berlaku juga untuk pagar laser cutting. Tanyakan detail dan harga tiap paket lewat WhatsApp.")
    form = consult(p["form"], p.get("bukaan", ""), "Konsultasi pagar laser cutting").replace(
        'placeholder="Style yang diinginkan, waktu survei, dll."></textarea>',
        'placeholder="Motif yang diinginkan, waktu survei, dll.">Style: laser cutting. Motif: </textarea>')

    body = f'''<section class="hero" id="beranda">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><a href="{L("layanan")}">Layanan</a><span>›</span><span>Pagar Laser Cutting</span></nav>
      <p class="kicker">Sejak 1985 · Motif custom · Survei gratis</p>
      <h1>Pagar Laser Cutting Surabaya</h1>
      <p class="sub">Pagar berpola presisi yang bikin rumah tampil mewah dan tetap terjaga privasinya. Motif bebas pilih, satu desain tersedia dalam tiga paket harga, dan pengelasan bergaransi 1 tahun.</p>
      <div class="actions">
        <a class="btn btn-cta" href="{wa_utama}" target="_blank" rel="noopener">Konsultasi Gratis via WhatsApp</a>
        <a class="btn btn-ghost" href="#galeri">Lihat Hasil Kerja</a>
      </div>
    </div>
    <figure class="hero-photo">
      <img src="{hero_img}" alt="{E(hero_alt)}" width="888" height="624" fetchpriority="high">
      <figcaption>{E(hero_cap)}</figcaption>
    </figure>
  </div>
</section>
<div class="facts"><div class="wrap"><div class="fact"><b>1985</b><span>Berdiri di Surabaya</span></div><div class="fact"><b>500+</b><span>Proyek selesai</span></div><div class="fact"><b>Gratis</b><span>Survei &amp; konsultasi</span></div><div class="fact"><b>1 tahun</b><span>Garansi pengelasan</span></div></div></div>

<section id="apa-itu"><div class="wrap detail">
  <div><p class="eyebrow">Kenalan dulu</p><h2>Apa itu pagar laser cutting?</h2></div>
  <div class="prose">{"".join(f"<p>{E(x)}</p>" for x in APA)}</div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="points">{poin}</div></div></section>

<section id="kenapa" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Kenapa Raja Pagar</p><h2>Pagar kokoh, harga bersahabat</h2></div>
    <div class="why">{why}</div>
  </div>
</section>

{paket}

<section id="galeri" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Hasil kerja kami</p><h2>Pagar laser cutting buatan Raja Pagar</h2><p class="lead">Ketuk foto proyek untuk melihat daftar bahan yang dipakai.</p></div>
  {photo_block(foto)}
  <div class="more-link"><a class="btn btn-ghost" style="color:var(--link)" href="{L("galeri")}">Lihat semua proyek di galeri</a></div>
</div></section>

<section id="spesifikasi" style="padding-top:0"><div class="wrap detail">
  <div><p class="eyebrow">Detail bahan</p><h2>Spesifikasi yang sering dipakai</h2><p class="lead">Bahan pasti tertulis jelas di penawaran, sesuai paket yang Anda pilih.</p><div class="actions" style="margin-top:14px"><a class="btn btn-line" href="{wa_motif}" target="_blank" rel="noopener">Kirim contoh motif via WA</a></div></div>
  <ul>{"".join(f"<li>{E(x)}</li>" for x in SPEK)}</ul>
</div></section>

{sec("proses")}

{sec("testimoni")}

<section id="faq" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Pertanyaan umum</p><h2>Seputar pagar laser cutting</h2></div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section id="area" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Area layanan</p><h2>Survei gratis di 31 kecamatan Surabaya</h2></div>
    <ul class="areas areas-wrap">{areas}</ul>
    <div class="area-cta"><p><b>Lokasi Anda di luar Surabaya?</b> Chat kami dulu untuk cek jadwal di Sidoarjo, Gresik, dan sekitarnya.</p><a class="btn btn-cta" href="{wa_utama}" target="_blank" rel="noopener">Chat WhatsApp</a></div>
  </div>
</section>

{form}

<section><div class="wrap"><div class="sec-head"><p class="eyebrow">Layanan terkait</p><h2>Mungkin Anda juga butuh</h2></div><div class="related">{rel}</div></div></section>'''

    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": p["h1"], "serviceType": "Pagar laser cutting",
              "description": DESC, "areaServed": {"@type": "City", "name": "Surabaya"},
              "provider": {"@type": "HomeAndConstructionBusiness", "name": "Raja Pagar Surabaya", "telephone": "+6285607988227", "url": BASE + "/"},
              "url": BASE + "/" + SLUG}
    lds = [svc_ld, g["ld_faq"](FAQ), g["ld_crumb"]([("", "Beranda"), ("layanan", "Layanan"), (SLUG, p["h1"])])]
    g["pages"][SLUG] = g["page"](SLUG, TITLE, DESC, body, lds, has_lb=bool(proyek), og_img=hero_img)
