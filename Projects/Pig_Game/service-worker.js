// Increment VERSION to force a fresh cache on deploys.
const VERSION = 'v1';
const CACHE_NAME = `soundstage-${VERSION}`;
const ASSETS = [
  './',
  './index.html',
  './starting.mp3',
  './winning.mp3',
  './boom.mp3'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((c) => c.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
  notifyClients();
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  const url = new URL(req.url);

  // Only handle our own folder scope (works on GitHub Pages)
  if (!url.pathname.startsWith(new URL(self.registration.scope).pathname)) return;

  e.respondWith(
    caches.match(req).then(cached => {
      if (cached) return cached;
      // Network then cache a copy
      return fetch(req).then(res => {
        const resClone = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(req, resClone)).catch(()=>{});
        return res;
      }).catch(() => {
        // Offline fallback: return index.html for navigations
        if (req.mode === 'navigate') return caches.match('./index.html');
        return new Response('Offline', { status: 503, statusText: 'Offline' });
      });
    })
  );
});

function notifyClients(){
  self.clients.matchAll({ includeUncontrolled: true, type: 'window' })
    .then(clients => clients.forEach(c => c.postMessage('CACHE_UPDATED')));
}
