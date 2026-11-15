"""Landing page khusus per style pagar.

Setiap landing page menggantikan halaman layanan biasa di alamat yang sama
(alamat lama dipertahankan supaya nilai SEO-nya tidak hilang).
Halaman ini dipakai untuk Google sekaligus tujuan iklan dan link bio IG/TikTok.

Dipanggil dari gen.py:  import landing; landing.buat(globals())
Menambah landing page baru: tambahkan satu dict ke LANDING di bawah.
"""
import urllib.parse

FAQ_UMUM = [
    ("Apakah survei dikenakan biaya?",
     "Tidak. Survei dan konsultasi gratis untuk seluruh 31 kecamatan di Surabaya."),
    ("Bagaimana sistem pembayarannya?",
     "DP 50% saat pesanan disetujui, sisanya dibayar di hari pemasangan. Bisa lewat transfer bank, tunai, atau QRIS."),
    ("Apa garansinya?",
     "Pengelasan bergaransi 1 tahun sejak pagar terpasang."),
]

LANDING = [
 dict(
  slug="pagar-laser-cutting-surabaya",
  nama="pagar laser cutting",
  title="Pagar Laser Cutting Surabaya, Motif Custom | Raja Pagar",
  desc="Jasa pagar laser cutting Surabaya sejak 1985. Motif daun, bunga, geometris, atau custom. Survei gratis di 31 kecamatan, garansi las 1 tahun. Chat WhatsApp sekarang.",
  kicker="Sejak 1985 · Motif custom · Survei gratis",
  sub="Pagar berpola presisi yang bikin rumah tampil mewah dan tetap terjaga privasinya. Motif bebas pilih, satu desain tersedia dalam tiga paket harga, dan pengelasan bergaransi 1 tahun.",
  apa_h2="Apa itu pagar laser cutting?",
  apa=["Pagar laser cutting adalah pagar besi yang isiannya berupa plat besi berpola. Polanya dipotong dengan mesin laser, "
       "jadi garisnya presisi dan rapi, sesuatu yang sulit didapat kalau dipotong manual.",
       "Kelebihannya, rumah jadi lebih tertutup dari pandangan orang di jalan, tapi cahaya dan udara tetap bisa masuk lewat celah motifnya. "
       "Tampilannya juga langsung terlihat mewah dan beda dari pagar jeruji biasa.",
       "Panel laser bisa dipasang penuh dari bawah sampai atas, atau dikombinasikan dengan jeruji dan plat polos supaya lebih hemat. "
       "Semua sistem bukaan bisa: sliding, sliding ganda, sliding swing, kupu tarung, maupun lipat."],
  poin=[("Motif bebas pilih", "Daun, bunga, geometris, kaligrafi, atau gambar dari Anda sendiri."),
        ("Privasi tetap terjaga", "Pandangan dari luar terhalang, sirkulasi udara tetap jalan."),
        ("Plat 1,2 mm sampai 2 mm", "Ketebalan plat menyesuaikan paket dan ukuran panel."),
        ("Warna bisa dikombinasi", "Panel bisa dicat beda dari rangka, misalnya hijau dengan aksen kuning.")],
  pilihan=None,
  spek=["Rangka pipa kotak 40x80 mm atau 50x100 mm",
        "Plat laser cutting 1,2 mm atau 2 mm",
        "Bingkai panel pipa kotak 15x35 mm",
        "Pilihan besi galvanis atau besi hitam",
        "Cat dasar epoxy filler, lalu cat akhir Nippe 2000"],
  faq=[("Bisa pakai motif sendiri?",
        "Bisa. Kirim gambar atau foto motif yang Anda suka lewat WhatsApp, nanti tim kami sesuaikan dengan ukuran panel pagar Anda."),
       ("Apakah plat laser cutting mudah berkarat?",
        "Plat diberi cat dasar epoxy filler sebelum cat akhir untuk menahan karat. Perawatannya cukup dibersihkan rutin dan dicat ulang kalau warnanya mulai kusam."),
       ("Apakah pagar laser cutting lebih mahal dari pagar minimalis?",
        "Umumnya sedikit lebih tinggi karena ada biaya potong laser. Kabar baiknya, satu desain bisa dibuat dalam paket Ekonomis, Standar, atau Premium, jadi bisa disesuaikan dengan anggaran. Kirim ukuran dan motif lewat WhatsApp untuk penawarannya."),
       ("Sistem bukaan apa saja yang bisa dipakai?",
        "Semua sistem bisa: sliding, sliding ganda, sliding swing, kupu tarung, dan lipat. Tim kami akan menyarankan yang paling pas saat survei."),
       ("Berapa lama pagar laser cutting selesai dibuat?",
        "Rata-rata 14 hari kerja sejak DP diterima, tergantung ukuran dan tingkat kerumitan motif.")],
  foto_tambahan=["tim-04", "tim-08"],
  cap={"tim-04": "Panel laser cutting setelah dicat, siap dipasang",
       "tim-08": "Tim kami memasang pagar laser cutting"},
  wa_utama="Halo Raja Pagar Surabaya, saya tertarik pagar laser cutting. Boleh minta info dan jadwal survei?",
  wa_kirim=("Kirim contoh motif via WA", "Halo Raja Pagar Surabaya, saya mau kirim contoh motif pagar laser cutting. Berikut gambarnya:"),
  catatan="Style: laser cutting. Motif: ",
  catatan_ph="Motif yang diinginkan, waktu survei, dll.",
  related=None,
 ),

 dict(
  slug="pagar-industrial-surabaya",
  nama="pagar industrial",
  title="Pagar Industrial Surabaya, Expanded Metal & Perforated",
  desc="Jasa pagar industrial Surabaya sejak 1985: isian expanded metal atau perforated plat, rangka kokoh. Survei gratis di 31 kecamatan, garansi las 1 tahun.",
  kicker="Sejak 1985 · Expanded metal & perforated · Survei gratis",
  sub="Pagar bergaya pabrik yang kokoh dan modern, dengan isian expanded metal atau perforated plat. Cocok untuk rumah modern, ruko, dan kafe. Satu desain tersedia dalam tiga paket harga, dan pengelasan bergaransi 1 tahun.",
  apa_h2="Apa itu pagar industrial?",
  apa=["Pagar industrial adalah pagar besi yang sengaja menonjolkan karakter materialnya, bukan ditutupi ornamen. "
       "Garisnya tegas, warnanya biasanya gelap seperti hitam atau abu-abu doff, dan kesannya kokoh seperti bangunan pabrik atau gudang.",
       "Isian utamanya ada dua: expanded metal yang berbentuk jaring belah ketupat, dan perforated plat atau plat berlubang. "
       "Keduanya bisa dipadukan dengan strep pipih, garis horizontal, atau aksen emas supaya tampil lebih mewah.",
       "Gaya ini cocok untuk rumah modern, ruko, kafe, dan tempat usaha. "
       "Semua sistem bukaan bisa: sliding, sliding ganda, sliding swing, kupu tarung, maupun lipat."],
  poin=[("Dua pilihan isian", "Expanded metal atau perforated plat, sesuai kebutuhan privasi."),
        ("Rangka tebal", "Hingga pipa kotak 50x100 mm tebal 2 mm untuk pagar besar."),
        ("Aksen opsional", "Strep pipih, garis horizontal, atau aksen emas metalik."),
        ("Cocok untuk usaha", "Kesan kokoh untuk ruko, kafe, dan gudang.")],
  pilihan=dict(
    h2="Expanded metal atau perforated plat?",
    lead="Dua isian utama pagar industrial. Bingung pilih yang mana? Kirim foto rumah Anda lewat WhatsApp, tim kami bantu sarankan.",
    item=[("Expanded metal", "Lembaran besi yang dipotong lalu direnggangkan sehingga membentuk jaring belah ketupat.",
           ["Kesan industrial paling kental", "Sirkulasi udara dan cahaya maksimal", "Pandangan dari luar masih sedikit tembus"]),
          ("Perforated plat", "Plat besi berlubang kecil yang rapi dan berjajar, biasanya lubang bulat.",
           ["Lebih tertutup, privasi lebih terjaga", "Udara dan cahaya tetap bisa lewat", "Tampilan bersih dan modern"])]),
  spek=["Rangka pipa kotak 40x80 mm atau 50x100 mm",
        "Isian expanded metal atau perforated plat",
        "Strep 2,5 cm x 4 mm atau garis horizontal sebagai aksen",
        "Pilihan besi galvanis atau besi hitam",
        "Cat dasar epoxy filler, cat akhir doff, aksen emas metalik bila diinginkan"],
  faq=[("Apa itu expanded metal?",
        "Lembaran besi yang dipotong dan direnggangkan sehingga membentuk jaring belah ketupat. Kuat, tembus udara, dan memberi kesan industrial."),
       ("Apa itu perforated plat?",
        "Plat besi yang dilubangi rapi dengan pola berulang, biasanya lubang bulat. Hasilnya lebih tertutup dari expanded metal, tapi tetap tembus udara dan cahaya."),
       ("Lebih baik expanded metal atau perforated plat?",
        "Pilih expanded metal kalau ingin kesan industrial yang kuat dan sirkulasi udara maksimal. Pilih perforated plat kalau privasi lebih penting, misalnya rumah yang menghadap jalan ramai. Tim kami bisa menyarankan saat survei."),
       ("Apakah pagar industrial cepat berkarat?",
        "Isian dan rangka diberi cat dasar epoxy filler sebelum cat akhir. Untuk ketahanan lebih, rangka bisa memakai besi galvanis. Perawatannya cukup dibersihkan rutin dan dicat ulang kalau warnanya mulai kusam."),
       ("Cocok untuk ruko atau kafe?",
        "Sangat cocok. Kesan kokohnya pas untuk tempat usaha, dan bisa dipadukan dengan sistem lipat supaya bukaan ruko bisa dibuka penuh."),
       ("Sistem bukaan apa saja yang bisa dipakai?",
        "Semua sistem bisa: sliding, sliding ganda, sliding swing, kupu tarung, dan lipat. Tim kami akan menyarankan yang paling pas saat survei."),
       ("Berapa lama pagar industrial selesai dibuat?",
        "Rata-rata 14 hari kerja sejak DP diterima, tergantung ukuran dan desain.")],
  foto_tambahan=[],
  cap={},
  wa_utama="Halo Raja Pagar Surabaya, saya tertarik pagar industrial. Boleh minta info dan jadwal survei?",
  wa_kirim=("Kirim contoh desain via WA", "Halo Raja Pagar Surabaya, saya mau kirim contoh desain pagar industrial. Berikut gambarnya:"),
  catatan="Style: industrial. Isian: expanded metal / perforated plat. ",
  catatan_ph="Isian yang diinginkan, waktu survei, dll.",
  related=["pagar-laser-cutting-surabaya", "pagar-lipat-surabaya", "pagar-sliding-surabaya"],
 ),

 dict(
  slug="pagar-minimalis-surabaya",
  nama="pagar minimalis",
  title="Pagar Minimalis Surabaya, 3 Pilihan Paket | Raja Pagar",
  desc="Jasa pagar minimalis Surabaya sejak 1985. Sliding, lipat, kupu tarung, isian jeruji atau plat. Survei gratis di 31 kecamatan, garansi las 1 tahun.",
  kicker="Sejak 1985 · Paling banyak dipesan · Survei gratis",
  sub="Pagar dengan garis tegas dan rapi yang cocok untuk hampir semua rumah, dari rumah di gang sampai rumah dua lantai di perumahan. Satu desain tersedia dalam tiga paket harga, dan pengelasan bergaransi 1 tahun.",
  apa_h2="Apa itu pagar minimalis?",
  apa=["Pagar minimalis adalah pagar besi dengan bentuk sederhana: rangka pipa kotak, isian jeruji vertikal atau horizontal, "
       "tanpa banyak ukiran. Justru karena sederhana, tampilannya bersih, modern, dan tidak cepat ketinggalan zaman.",
       "Ini jenis pagar yang paling banyak dipesan di Raja Pagar. Tingkat privasinya bisa diatur, mulai dari jeruji terbuka "
       "sampai plat penuh, dan bisa ditambah ornamen kecil sebagai pemanis.",
       "Pagar minimalis cocok untuk rumah tipe kecil, rumah di perumahan, sampai rumah dua lantai. "
       "Semua sistem bukaan bisa: sliding, sliding ganda, sliding swing, kupu tarung, maupun lipat."],
  poin=[("Bisa semua sistem bukaan", "Sliding, sliding ganda, sliding swing, kupu tarung, atau lipat."),
        ("Isian sesuai privasi", "Jeruji terbuka, plat setengah, atau plat penuh."),
        ("Spek jelas di penawaran", "Ukuran dan ketebalan besi tertulis jelas sesuai paket, jadi Anda tahu persis apa yang dibayar."),
        ("Finishing rapi", "Cat dasar epoxy filler lalu cat akhir, warna bisa dipilih.")],
  pilihan=[
    dict(eyebrow="Pilihan isian", h2="Seberapa tertutup pagar yang Anda mau?",
         lead="Desainnya tetap minimalis, tingkat privasinya bisa disesuaikan dengan kebutuhan rumah Anda.",
         item=[("Jeruji terbuka", "Jeruji vertikal atau horizontal dari atas sampai bawah.",
                ["Halaman terlihat lega dan terang", "Sirkulasi udara paling lancar", "Tampilan paling ringan dan simpel"]),
               ("Plat setengah", "Jeruji di bagian atas, plat penutup di bagian bawah.",
                ["Kendaraan dan teras lebih tertutup", "Hewan kecil tidak mudah masuk", "Seimbang antara privasi dan sirkulasi udara"]),
               ("Plat penuh", "Plat menutup hampir seluruh daun pagar, bisa diberi ornamen.",
                ["Privasi paling terjaga", "Cocok untuk rumah di pinggir jalan ramai", "Bisa ditambah ornamen bunga, daun, atau wajik"])]),
    dict(id="galvanis-hitam", eyebrow="Pilihan bahan", h2="Hollow galvanis atau hollow hitam?",
         lead="Dua jenis besi yang paling sering dipakai untuk pagar minimalis. Jenis dan ukurannya ditulis jelas di penawaran.",
         item=[("Hollow galvanis", "Besi berlapis seng yang warnanya keperakan.",
                ["Lebih tahan karat", "Cocok untuk pagar yang terkena hujan langsung", "Perawatan lebih ringan"]),
               ("Hollow hitam", "Besi tanpa lapisan seng yang dilindungi cat dasar dan cat akhir.",
                ["Bisa memakai ukuran lebih tebal", "Harga lebih hemat", "Perlu dicat ulang secara berkala"])]),
  ],
  spek=["Rangka pipa kotak 40x80 mm atau 50x100 mm",
        "Jeruji pipa 15x35 mm atau 20x20 mm, jarak rapat atau renggang",
        "Plat galvanis penutup bagian bawah atau penuh",
        "Pengaku tengah horizontal agar daun pagar lebih kaku",
        "Cat dasar epoxy filler, lalu cat akhir sesuai warna pilihan"],
  faq=[("Berapa harga pagar minimalis per meter di Surabaya?",
        "Harga dihitung per meter persegi dan tergantung desain, bahan, dan sistem bukaan. Kirim ukuran dan contoh desain lewat WhatsApp, lalu kami beri penawaran untuk paket Ekonomis, Standar, dan Premium."),
       ("Apa beda paket Ekonomis, Standar, dan Premium?",
        "Desainnya sama, yang berbeda adalah spek bahannya. Rincian tiap paket kami jelaskan lewat WhatsApp dan tertulis di penawaran, supaya Anda bisa membandingkan dengan tenang."),
       ("Lebih baik hollow galvanis atau hollow hitam?",
        "Hollow galvanis lebih tahan karat, cocok untuk pagar yang terkena hujan langsung. Hollow hitam bisa lebih tebal dengan harga lebih hemat. Tim kami akan menyarankan saat survei."),
       ("Bisa ditambah ornamen?",
        "Bisa. Ornamen bunga, daun, atau wajik bisa ditambahkan sebagai aksen, misalnya dicat emas, tanpa menghilangkan kesan minimalisnya."),
       ("Sistem bukaan apa saja yang bisa dipakai?",
        "Semua sistem bisa: sliding, sliding ganda, sliding swing, kupu tarung, dan lipat. Tim kami akan menyarankan yang paling pas dengan lebar dan bentuk halaman Anda saat survei."),
       ("Berapa lama pembuatan pagar minimalis?",
        "Rata-rata 14 hari kerja sejak DP diterima.")],
  foto_tambahan=[],
  cap={},
  wa_utama="Halo Raja Pagar Surabaya, saya tertarik pagar minimalis. Boleh minta info dan jadwal survei?",
  wa_kirim=("Kirim contoh desain via WA", "Halo Raja Pagar Surabaya, saya mau kirim contoh desain pagar minimalis. Berikut gambarnya:"),
  catatan="Style: minimalis. Isian: ",
  catatan_ph="Isian (jeruji terbuka / plat setengah / plat penuh), waktu survei, dll.",
  hero=0,  # foto pembuka: proyek-01 (Semampir)
  related=["pagar-sliding-surabaya", "pagar-lipat-surabaya", "pagar-kupu-tarung-surabaya"],
 ),
]


def buat(g):
    for c in LANDING:
        if c["slug"] in g["BYSLUG"]:
            _satu(g, c)


def _satu(g, c):
    E, L, WA = g["E"], g["L"], g["WA"]
    P, sec, consult, photo_block, fname = g["P"], g["sec"], g["consult"], g["photo_block"], g["fname"]
    bravo, BASE, BYSLUG = g["bravo"], g["BASE"], g["BYSLUG"]
    SLUG = c["slug"]
    p = BYSLUG[SLUG]
    g["CAP"].update(c["cap"])
    nama = c["nama"]
    Nama = nama[:1].upper() + nama[1:]

    def wa(teks):
        return f"https://wa.me/{WA}?text=" + urllib.parse.quote(teks)
    wa_utama = wa(c["wa_utama"])
    kirim_label, kirim_teks = c["wa_kirim"]

    proyek = [x for x in p["photos"] if isinstance(x, int)]
    foto = proyek + [x for x in p["photos"] if isinstance(x, str)] + c["foto_tambahan"]
    if proyek:
        k = c["hero"] if c.get("hero") in proyek else proyek[0]
        hero_img = f'img/{fname(k)}.webp'
        hero_alt = f"{P[k][0]} di {P[k][2]}, buatan Raja Pagar Surabaya"
        hero_cap = f"{P[k][0]} · {P[k][2]}"
    else:
        s = c["foto_tambahan"][0]
        hero_img, hero_alt, hero_cap = f"img/{s}.webp", c["cap"].get(s, p["h1"]), c["cap"].get(s, "")

    poin = "".join(f'<div class="point"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in c["poin"])
    why = "".join(f'<div class="why-item"><div class="why-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ic}</svg></div><div><h3>{E(t)}</h3><p>{E(d)}</p></div></div>' for t, d, ic in bravo.ALASAN)
    faq_list = c["faq"] + FAQ_UMUM
    faq = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in faq_list)
    areas = "".join(f'<li>{E(k)}</li>' for k in bravo.KECAMATAN)
    rel = "".join(f'<a class="svc" href="{L(r)}"><h3>{E(BYSLUG[r]["h1"])}</h3><p>{E(BYSLUG[r]["short"])}</p><span class="more">Selengkapnya →</span></a>' for r in (c["related"] or p["related"]) if r in BYSLUG)

    pilihan = ""
    pls = c["pilihan"] or []
    if isinstance(pls, dict):
        pls = [pls]
    for n, pl in enumerate(pls):
        kartu = "".join(
            f'<div class="point"><h3>{E(t)}</h3><p>{E(d)}</p><ul style="margin:10px 0 0;padding-left:18px;display:grid;gap:4px;color:var(--muted);font-size:.94rem">{"".join(f"<li>{E(x)}</li>" for x in li)}</ul></div>'
            for t, d, li in pl["item"])
        sid = pl.get("id", "pilihan-isian" if n == 0 else f"pilihan-{n + 1}")
        pilihan += f'''<section id="{sid}" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">{E(pl.get("eyebrow", "Pilihan isian"))}</p><h2>{E(pl["h2"])}</h2><p class="lead">{E(pl["lead"])}</p></div>
  <div class="points" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))">{kartu}</div>
</div></section>
'''

    paket = sec("paket").replace("Tanyakan detail dan harga tiap paket lewat WhatsApp.",
                                 f"Berlaku juga untuk {nama}. Tanyakan detail dan harga tiap paket lewat WhatsApp.")
    form = consult(p["form"], p.get("bukaan", ""), "Konsultasi " + nama).replace(
        'placeholder="Style yang diinginkan, waktu survei, dll."></textarea>',
        f'placeholder="{E(c["catatan_ph"])}">{E(c["catatan"])}</textarea>')
    label_crumb = p["h1"].replace(" Surabaya", "")

    body = f'''<section class="hero" id="beranda">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <nav class="crumb" aria-label="Breadcrumb"><a href="{L("")}">Beranda</a><span>›</span><a href="{L("layanan")}">Layanan</a><span>›</span><span>{E(label_crumb)}</span></nav>
      <p class="kicker">{E(c["kicker"])}</p>
      <h1>{E(p["h1"])}</h1>
      <p class="sub">{E(c["sub"])}</p>
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
  <div><p class="eyebrow">Kenalan dulu</p><h2>{E(c["apa_h2"])}</h2></div>
  <div class="prose">{"".join(f"<p>{E(x)}</p>" for x in c["apa"])}</div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="points">{poin}</div></div></section>

{pilihan}

<section id="kenapa" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Kenapa Raja Pagar</p><h2>Pagar kokoh, harga bersahabat</h2></div>
    <div class="why">{why}</div>
  </div>
</section>

{paket}

<section id="galeri" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><p class="eyebrow">Hasil kerja kami</p><h2>{E(Nama)} buatan Raja Pagar</h2><p class="lead">Ketuk foto proyek untuk melihat daftar bahan yang dipakai.</p></div>
  {photo_block(foto)}
  <div class="more-link"><a class="btn btn-ghost" style="color:var(--link)" href="{L("galeri")}">Lihat semua proyek di galeri</a></div>
</div></section>

<section id="spesifikasi" style="padding-top:0"><div class="wrap detail">
  <div><p class="eyebrow">Detail bahan</p><h2>Spesifikasi yang sering dipakai</h2><p class="lead">Bahan pasti tertulis jelas di penawaran, sesuai paket yang Anda pilih.</p><div class="actions" style="margin-top:14px"><a class="btn btn-line" href="{wa(kirim_teks)}" target="_blank" rel="noopener">{E(kirim_label)}</a></div></div>
  <ul>{"".join(f"<li>{E(x)}</li>" for x in c["spek"])}</ul>
</div></section>

{sec("proses")}

{sec("testimoni")}

<section id="faq" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Pertanyaan umum</p><h2>Seputar {E(nama)}</h2></div>
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

    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": p["h1"], "serviceType": Nama,
              "description": c["desc"], "areaServed": {"@type": "City", "name": "Surabaya"},
              "provider": {"@type": "HomeAndConstructionBusiness", "name": "Raja Pagar Surabaya", "telephone": "+6285607988227", "url": BASE + "/"},
              "url": BASE + "/" + SLUG}
    lds = [svc_ld, g["ld_faq"](faq_list), g["ld_crumb"]([("", "Beranda"), ("layanan", "Layanan"), (SLUG, p["h1"])])]
    g["pages"][SLUG] = g["page"](SLUG, c["title"], c["desc"], body, lds, has_lb=bool(proyek), og_img=hero_img)
