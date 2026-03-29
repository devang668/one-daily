---
---
const CACHE_NAME = "one-daily-v{{ site.time | date: '%Y%m%d%H%M%S' }}";
const OFFLINE_URL = "{{ '/offline/' | relative_url }}";
const PRECACHE_URLS = [
  "{{ '/' | relative_url }}",
  "{{ '/about' | relative_url }}",
  "{{ '/offline/' | relative_url }}",
  "{{ '/manifest.webmanifest' | relative_url }}",
  "{{ '/assets/styles.css' | relative_url }}",
  "{{ '/assets/app.js' | relative_url }}",
  "{{ '/assets/icons/app-icon.svg' | relative_url }}",
{% for post in site.posts %}
  "{{ post.url | relative_url }}",
{% endfor %}
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") {
    return;
  }

  const requestUrl = new URL(event.request.url);
  if (requestUrl.origin !== self.location.origin) {
    return;
  }

  if (event.request.mode === "navigate") {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, responseClone));
          return response;
        })
        .catch(async () => {
          const cachedPage = await caches.match(event.request);
          return cachedPage || caches.match(OFFLINE_URL);
        })
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const networkResponse = fetch(event.request)
        .then((response) => {
          if (response && response.ok) {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, responseClone));
          }
          return response;
        })
        .catch(() => cachedResponse);

      return cachedResponse || networkResponse;
    })
  );
});
