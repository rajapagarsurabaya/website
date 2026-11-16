/* Kalkulator Pagar: service worker. Versi 20261114-045608
   Halaman: ambil dari internet dulu (supaya selalu versi terbaru), kalau gagal pakai simpanan (offline).
   Permintaan ke alamat lain (sinkron Google Sheet) tidak disentuh. */
var CACHE = 'kalkulator-pagar-v1';
var BERKAS = ['./', 'manifest.webmanifest', 'ikon-192.png', 'ikon-512.png', 'ikon-maskable-512.png'];
self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(BERKAS); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (ks) { return Promise.all(ks.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); })); }).then(function () { return self.clients.claim(); }));
});
self.addEventListener('fetch', function (e) {
  var r = e.request;
  if (r.method !== 'GET') return;
  var u = new URL(r.url);
  if (u.origin !== self.location.origin) return;
  var halaman = r.mode === 'navigate';
  var kunci = halaman ? './' : r;
  e.respondWith(
    fetch(r).then(function (res) {
      if (res && res.ok) { var salin = res.clone(); caches.open(CACHE).then(function (c) { c.put(kunci, salin); }); }
      return res;
    }).catch(function () {
      return caches.match(kunci).then(function (hit) { return hit || caches.match('./'); });
    })
  );
});
