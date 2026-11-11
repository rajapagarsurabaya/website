"""Bagian-bagian baru ala Bravo: header, beranda. Dipakai oleh gen.py."""

KECAMATAN = ["Asemrowo","Benowo","Bubutan","Bulak","Dukuh Pakis","Gayungan","Genteng","Gubeng","Gunung Anyar","Jambangan","Karang Pilang","Kenjeran","Krembangan","Lakarsantri","Mulyorejo","Pabean Cantian","Pakal","Rungkut","Sambikerep","Sawahan","Semampir","Simokerto","Sukolilo","Sukomanunggal","Tambaksari","Tandes","Tegalsari","Tenggilis Mejoyo","Wiyung","Wonocolo","Wonokromo"]
ADA_PROYEK = {"Benowo","Genteng","Gunung Anyar","Kenjeran","Semampir","Tambaksari"}

OWNER = ("Kami percaya pagar bukan sekadar besi, tapi pelindung pertama bagi keluarga di dalam rumah. Karena itu setiap pagar kami kerjakan seperti untuk rumah sendiri. Terima kasih sudah memercayakan rumah Anda kepada Raja Pagar.",
         "Rachmad Dwi Prasojo", "Owner Raja Pagar Surabaya")

ALASAN = [
 ("Berpengalaman sejak 1985", "Lebih dari 500 proyek pagar, kanopi, dan railing di Surabaya.", '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>'),
 ("Harga bersahabat", "Satu desain tersedia dalam paket Ekonomis, Standar, dan Premium.", '<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>'),
 ("Owner dan tim ramah", "Hal yang paling sering disebut pelanggan di ulasan Google.", '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/>'),
 ("Tepat waktu", "Rata-rata 14 hari kerja dari DP sampai pagar siap dipasang.", '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 ("Kualitas bergaransi", "Pengelasan bergaransi 1 tahun setelah serah terima.", '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'),
 ("Desain custom", "Ukuran, motif, dan warna disesuaikan dengan rumah Anda.", '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>'),
]

FAQ = [
 ("Apakah survei dikenakan biaya?", "Tidak. Survei dan konsultasi gratis untuk seluruh 31 kecamatan di Surabaya."),
 ("Berapa harga pagar per meter?", "Harga dihitung per meter persegi dan tergantung desain, bahan, dan sistem bukaan. Kirim ukuran dan contoh desain lewat WhatsApp, lalu kami beri penawaran untuk paket Ekonomis, Standar, dan Premium."),
 ("Berapa lama pagar selesai dibuat?", "Rata-rata 14 hari kerja sejak DP diterima, tergantung ukuran dan desain."),
 ("Bagaimana sistem pembayarannya?", "DP 50% saat pesanan disetujui, sisanya dibayar di hari pemasangan. Pembayaran bisa lewat transfer bank, tunai, atau QRIS."),
 ("Apa yang dicakup garansi?", "Pengelasan bergaransi 1 tahun sejak pagar terpasang."),
 ("Lebih baik besi galvanis atau besi hitam?", "Hollow galvanis lebih tahan karat untuk pagar yang terkena hujan langsung. Hollow hitam bisa dibuat lebih tebal dengan harga lebih hemat. Tim kami akan menyarankan saat survei."),
 ("Bisa memperbaiki pagar buatan bengkel lain?", "Bisa. Kirim foto pagar dan bagian yang bermasalah lewat WhatsApp untuk perkiraan awal."),
 ("Apakah melayani di luar Surabaya?", "Saat ini kami fokus melayani Surabaya. Untuk Sidoarjo, Gresik, dan sekitarnya, chat kami dulu untuk cek jadwal."),
]

CSS = r"""
.topbar{background:var(--navy-deep);color:var(--on-navy-muted);font-size:.82rem;border-bottom:1px solid rgba(255,255,255,.08)}
.topbar .wrap{display:flex;align-items:center;gap:18px;padding-block:6px;flex-wrap:wrap}
.topbar a{color:var(--on-navy);text-decoration:none}
.topbar a:hover{color:var(--yellow)}
.topbar .tb-item{display:inline-flex;align-items:center;gap:6px}
.topbar .tb-item svg{width:14px;height:14px}
.topbar .socials{margin-left:auto}
.topbar .socials a{width:28px;height:28px}
.topbar .socials svg{width:14px;height:14px}
@media (max-width:760px){.topbar .tb-hide{display:none}}
header{background:var(--navy)}
.hdr{gap:16px}
.nav-cta{margin-left:8px;padding:10px 16px;white-space:nowrap}
nav.main{overflow:visible;align-items:center}
.dd{position:relative}
.dd-btn{background:none;border:0;color:var(--on-navy-muted);font:inherit;font-size:.92rem;padding:8px 10px;border-radius:4px;cursor:pointer;display:inline-flex;align-items:center;gap:4px}
.dd-btn:hover,.dd.open .dd-btn,.dd-btn[aria-current="page"]{color:var(--on-navy);background:rgba(255,255,255,.08)}
.dd-btn svg{width:12px;height:12px;transition:transform .2s}
.dd.open .dd-btn svg{transform:rotate(180deg)}
.dd-menu{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%);background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:var(--r);box-shadow:0 18px 40px rgba(0,0,40,.25);padding:20px;display:none;grid-template-columns:repeat(3,minmax(170px,1fr));gap:20px;width:max-content;max-width:min(720px,calc(100vw - 32px));z-index:40}
.dd.open .dd-menu{display:grid}
.dd-menu h4{margin:0 0 8px;font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:500}
nav.main .dd-menu a{display:block;color:var(--ink);background:none;text-decoration:none;padding:6px 8px;border-radius:4px;font-size:.92rem;white-space:normal}
nav.main .dd-menu a:hover{background:var(--bg);color:var(--link)}
.menu-btn{display:none;margin-left:auto;background:rgba(255,255,255,.1);color:var(--on-navy);border:0;border-radius:4px;padding:9px 12px;font:600 .9rem var(--body);cursor:pointer;align-items:center;gap:6px}
.menu-btn svg{width:18px;height:18px}
@media (max-width:980px){
  .hdr{flex-wrap:nowrap}
  .menu-btn{display:inline-flex}
  .nav-cta{display:none}
  nav.main{display:none;position:absolute;left:0;right:0;top:100%;background:var(--navy);flex-direction:column;align-items:stretch;padding:8px max(16px,env(safe-area-inset-right,0px)) 16px max(16px,env(safe-area-inset-left,0px));max-height:calc(100vh - 120px);overflow:auto;border-top:1px solid rgba(255,255,255,.1);box-shadow:0 18px 30px rgba(0,0,40,.3)}
  header.nav-open nav.main{display:flex}
  nav.main > a,.dd-btn{padding:12px 8px;font-size:1rem;width:100%;justify-content:space-between}
  .dd-menu{position:static;transform:none;width:auto;max-width:none;box-shadow:none;grid-template-columns:1fr;gap:12px;margin:4px 0 8px;padding:14px}
  nav.main .nav-cta-m{display:flex;justify-content:center;margin-top:10px}
}
@media (min-width:981px){nav.main .nav-cta-m{display:none}}
header .wrap.hdr{position:relative}
.hero h1{text-transform:none}
.hero h1 .h1-brand{display:block;text-transform:uppercase;font-size:1em}
.hero h1 .h1-kw{display:block;font-size:.42em;font-weight:700;font-stretch:90%;letter-spacing:.01em;margin-top:10px;color:var(--on-navy)}
.hero .tagline{font-family:var(--display);font-style:italic;font-weight:700;font-stretch:90%;color:var(--yellow);font-size:clamp(1.1rem,2.2vw,1.45rem);margin-top:16px}
.pay{background:var(--navy-deep);color:var(--on-navy-muted);font-size:.86rem}
.pay .wrap{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;padding-block:12px;border-top:1px solid rgba(255,255,255,.12)}
.pay b{color:var(--on-navy);font-weight:600}
.pay .pill{border:1px solid rgba(255,255,255,.25);color:var(--on-navy);border-radius:999px;padding:3px 12px;font-size:.8rem}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;text-decoration:none;color:var(--ink);display:grid;grid-template-rows:auto 1fr;transition:border-color .2s,transform .2s}
.card:hover{border-color:var(--navy);transform:translateY(-3px)}
.card img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;max-width:100%;transition:transform .5s}
.card:hover img{transform:scale(1.04)}
.card .ci{overflow:hidden}
.card div.cb{padding:14px 16px;display:grid;gap:6px;align-content:start}
.card p{color:var(--muted);font-size:.9rem}
.card .more{font-weight:600;font-size:.88rem;color:var(--link)}
@media (max-width:900px){.cards{grid-template-columns:1fr 1fr}}
@media (max-width:440px){.cards{grid-template-columns:1fr}}
.chiplinks{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:20px;font-size:.9rem;color:var(--muted)}
.chiplinks a{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:6px 14px;text-decoration:none}
.chiplinks a:hover{border-color:var(--navy);color:var(--link)}
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.why-item{display:grid;grid-template-columns:48px 1fr;gap:14px;align-items:start;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:18px}
.why-ic{width:48px;height:48px;border-radius:50%;background:var(--navy);display:grid;place-items:center}
.why-ic svg{width:22px;height:22px;stroke:var(--yellow);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.why-item p{color:var(--muted);font-size:.9rem;margin-top:4px}
@media (max-width:900px){.why{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.why{grid-template-columns:1fr}}
.owner{background:var(--navy);color:var(--on-navy)}
.owner blockquote{margin:0 auto;max-width:860px;display:grid;gap:22px;text-align:left;position:relative;padding-left:64px}
.owner blockquote::before{content:"\201C";position:absolute;left:0;top:-18px;font-family:var(--display);font-size:6rem;line-height:1;color:var(--yellow)}
.owner blockquote p{font-family:var(--display);font-weight:600;font-stretch:92%;font-size:clamp(1.25rem,2.6vw,1.8rem);line-height:1.35;text-wrap:balance}
.owner footer{font-size:.95rem;color:var(--on-navy-muted)}
.owner footer b{display:block;color:var(--yellow);font-size:1.05rem}
@media (max-width:560px){.owner blockquote{padding-left:0;padding-top:40px}.owner blockquote::before{top:-20px}}
.split{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.seg{position:relative;border-radius:var(--r);overflow:hidden;min-height:340px;display:flex;align-items:flex-end;color:#fff;text-decoration:none;background:#111}
.seg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .6s}
.seg:hover img{transform:scale(1.04)}
.seg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,40,.05) 20%,rgba(0,0,40,.88))}
.seg .sb{position:relative;z-index:1;padding:22px;display:grid;gap:8px}
.seg h3{font-size:1.6rem;font-stretch:85%;font-weight:800}
.seg ul{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:6px}
.seg li{font-size:.8rem;background:rgba(255,255,255,.14);padding:3px 10px;border-radius:999px}
.seg .more{color:var(--yellow);font-weight:600;font-size:.92rem}
@media (max-width:760px){.split{grid-template-columns:1fr}.seg{min-height:280px}}
.repair{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
.repair img{width:100%;height:100%;object-fit:cover;display:block;max-height:420px;max-width:100%}
.repair .rb{padding:28px;display:grid;gap:14px;min-width:0}
.repair ul{margin:0;padding-left:18px;color:var(--muted);display:grid;gap:4px}
.repair .actions{display:flex;flex-wrap:wrap;gap:10px}
@media (max-width:760px){.repair{grid-template-columns:1fr}.repair .rb{padding:20px}}
.gal8{grid-template-columns:repeat(4,1fr)}
@media (max-width:900px){.gal8{grid-template-columns:repeat(2,1fr)}}
.areas{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:8px;margin-top:4px}
.areas li{list-style:none;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:9px 12px;font-size:.92rem;display:flex;align-items:center;gap:8px}
.areas li::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--line);flex:none}
.areas li.done::before{background:var(--yellow);box-shadow:0 0 0 2px var(--navy)}
.areas-wrap{padding:0;margin:0}
.area-note{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;margin-top:18px;font-size:.88rem;color:var(--muted)}
.area-note .lg{display:inline-flex;align-items:center;gap:6px}
.area-note .lg i{width:8px;height:8px;border-radius:50%;background:var(--yellow);box-shadow:0 0 0 2px var(--navy);display:inline-block}
.area-cta{margin-top:18px;background:var(--navy);color:var(--on-navy);border-radius:var(--r);padding:18px 20px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}
.area-cta p{color:var(--on-navy-muted)}
.area-cta b{color:var(--on-navy)}
"""

JS = r"""
  // Menu HP dan dropdown layanan
  (function(){
    var hd=document.querySelector("header"),mb=document.querySelector(".menu-btn");
    if(mb)mb.addEventListener("click",function(){var o=hd.classList.toggle("nav-open");mb.setAttribute("aria-expanded",o)});
    var dd=document.querySelector(".dd"),db=dd&&dd.querySelector(".dd-btn");
    if(db){
      db.addEventListener("click",function(e){e.stopPropagation();var o=dd.classList.toggle("open");db.setAttribute("aria-expanded",o)});
      document.addEventListener("click",function(e){if(!dd.contains(e.target)){dd.classList.remove("open");db.setAttribute("aria-expanded",false)}});
      document.addEventListener("keydown",function(e){if(e.key==="Escape"){dd.classList.remove("open");db.setAttribute("aria-expanded",false)}});
      var hov=window.matchMedia("(hover:hover) and (min-width:981px)");
      dd.addEventListener("mouseenter",function(){if(hov.matches){dd.classList.add("open");db.setAttribute("aria-expanded",true)}});
      dd.addEventListener("mouseleave",function(){if(hov.matches){dd.classList.remove("open");db.setAttribute("aria-expanded",false)}});
    }
  })();
"""
