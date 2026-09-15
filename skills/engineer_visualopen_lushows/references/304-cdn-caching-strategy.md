# 304 · Estrategia de CDN y caching: Cache-Control, SWR, purge, ISR

> El cache mal hecho sirve datos viejos o no sirve nada. La estrategia ganadora casi nunca es
> "invalidar": es versionar URLs y combinar TTL corto con stale-while-revalidate.

## Anatomía de `Cache-Control`
- `public` / `private`: ¿puede cachear la CDN o solo el navegador?
- `max-age=N`: frescura para el **navegador** (segundos).
- `s-maxage=N`: frescura para la **CDN/proxy compartido** (anula `max-age` en el edge).
- `stale-while-revalidate=N` (**SWR**): tras expirar, sirve **stale al instante** y revalida en background
  durante N segundos → el usuario nunca paga el miss.
- `stale-if-error=N`: sirve stale si el origen falla → resiliencia gratis.
- `no-store` (nunca cachea) vs `no-cache` (cachea pero revalida siempre con ETag).

## El patrón que querés casi siempre
```
Cache-Control: public, s-maxage=300, stale-while-revalidate=86400
```
Fresco 5 min; tras eso sirve stale hasta 24h mientras refresca atrás. Regla práctica: **SWR ≥ 5× el s-maxage**
en rutas de alto tráfico → minimiza miss-storms y golpes al origen.

## Versionado de assets (la mejor invalidación es no invalidar)
Estáticos (JS/CSS/imágenes/**media generada**) con hash en el nombre (`app.9f3a.js`, `avatar-<id>.mp4`):
```
Cache-Control: public, max-age=31536000, immutable
```
Cambia el contenido → cambia la URL → cache-busting automático, **cero purge**. Esto aplica directo a la media
del worker GPU: nombra por hash/id y cachéala para siempre ([[162-storage-cdn-media-generada]]).

## Purge / invalidación (cuando no podés versionar)
- **Por tag (recomendado)**: marca un tag como stale → las entradas asociadas revalidan en background al
  siguiente request. Sin latencia para el usuario. (Vercel: invalidate-by-tag, ~300ms en todas las regiones [verificado].)
- **Por path/URL**: granular, sirve para una página concreta.
- **Purge everything**: el martillo; provoca miss-storm global → evítalo.
- **Regla de oro**: **purga en el WRITE, no en el read** — dispara el purge desde el CMS/API cuando el contenido
  cambia, no cuando el usuario pide algo viejo.

## ISR (Incremental Static Regeneration)
Es SWR aplicado a páginas: sirve HTML estático cacheado + regenera en background por intervalo o por API.
El visitante recibe rápido; la página se regenera atrás. En Vercel, al revalidar, **todas las regiones
actualizan en ~300ms** y HTML+data se purgan juntos → consistencia entre full-load y navegación client-side [verificado].

## Capas de cache (de afuera hacia adentro)
1. Navegador (`max-age`) → 2. CDN/edge (`s-maxage` + SWR) → 3. Cache de runtime/app → 4. Origen/DB.
Cada capa absorbe carga de la siguiente. Detalle multicapa en [[358-caching-strategy-multilayer]].

## Trampas
- `max-age` alto en HTML dinámico → usuarios ven contenido viejo y no hay forma fácil de purgar el navegador.
  Cachea HTML en la **CDN** (`s-maxage`) que sí podés purgar, no en el navegador.
- Olvidar `Vary` (p.ej. `Accept-Encoding`, auth) → sirves la respuesta equivocada a otro usuario.
- Cachear respuestas con `Set-Cookie` o datos por-usuario → fuga de sesión entre clientes.

Cruza con [[22-caching-cdn]] y [[358-caching-strategy-multilayer]].
