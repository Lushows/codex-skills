# 90 — PWA & offline-first

## Anatomía
PWA = web normal + **service worker** (proxy de red que intercepta fetches y sirve del cache) + **web app manifest**
(instalabilidad) + HTTPS. Offline-first = tratar la red como *enhancement*, no requisito — renderiza del cache/DB local primero, sync en background.

## Service workers + Workbox
Escribirlos a mano es propenso a error (versioning, lifecycle). **Workbox 7** es el estándar (precache manifest, runtime routing, integra con Vite/webpack/Next). **3 estrategias de caching:**
- **Cache-first** — assets estáticos inmutables (JS/CSS hasheados, fonts).
- **Network-first** — data dinámica fresh-critical (API), con cache de fallback offline.
- **Stale-while-revalidate** — respuesta cacheada instantánea + update en background. Mejor default UX para semi-dinámico.
```js
registerRoute(({request})=>request.destination==='image', new CacheFirst({cacheName:'images'}))
registerRoute(({url})=>url.pathname.startsWith('/api/'), new StaleWhileRevalidate({cacheName:'api'}))
```

## Data estructurada / sync / push
**Cache API** = para *responses*; data estructurada (records, queues) va en **IndexedDB** (usa **Dexie.js** — schema
tipado, promises, live queries). Patrón 2026: **Dexie + Workbox Background Sync**. **Background Sync** reintenta
mutaciones fallidas al volver la conectividad — pero **solo Chrome/Edge/Opera/Samsung, NO Firefox ni Safari** → ~mitad de móviles (todo iOS) necesita fallback manual que flushea en el evento `online`. **Web Push:** Chrome/Edge/Firefox y, desde iOS 16.4, en PWAs iOS instaladas (home-screen, user-gesture).

## Instalabilidad / iOS
Chromium dispara `beforeinstallprompt` → captúralo, muestra tu CTA, llama `prompt()`. iOS no tiene prompt
programático ("Add to Home Screen" manual). **Estado iOS de PWA:** funciona instalada PERO **storage (caches +
IndexedDB) se evicta tras ~7 días de inactividad** salvo persistent storage; sin Background Sync; push solo instalada. **Diseña para eviction** — re-fetch/re-hidrata con gracia.

## Gotchas
1. **Eviction iOS 7 días** — nunca asumas que el cache/IndexedDB sobrevive; re-sync al arrancar.
2. Background Sync es Chromium-only — siempre ship fallback de flush en evento `online`.
3. Cache-first en tu app shell sirve código stale para siempre tras un deploy — versiona caches y usa `skipWaiting`/`clientsClaim` con cuidado.
4. Service workers requieren HTTPS y están scoped a su path — un SW mal ubicado controla el scope equivocado.
5. No guardes blobs grandes en Cache API esperando persistencia — pide `navigator.storage.persist()` y revisa quota.
6. Push en iOS solo funciona instalada en home-screen y necesita gesto directo del usuario.

**Fuentes:** magicbell.com/blog (offline-first caching) · wellally.tech/blog (React+Dexie+Workbox) · digitalapplied.com (PWA 2026).
