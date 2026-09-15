# 322 · SEO técnico a fondo (crawl, render, CWV, schema, GEO)

> [[68-seo-tecnico-geo]] da el mapa; esto baja a la sala de máquinas: presupuesto de
> rastreo, el render path, CWV de campo, schema avanzado e internal-linking que mueve autoridad.

## Crawl budget — el recurso que sí escasea
Google asigna **rastreo finito por sitio** (crawl rate × crawl demand). En sitios grandes la
arquitectura ineficiente hace que tu mejor contenido **nunca se indexe**. Palancas:
- **Poda lo thin/duplicado**: `noindex` o canonical libera capacidad de rastreo para lo que importa.
- **Cierra trampas de rastreo**: facetas, `?sort=`, paginación infinita, sesiones en URL → bloquea en
  `robots.txt` o usa `rel=canonical`. Cada URL basura es rastreo robado.
- **`sitemap.xml`** solo con canónicas 200; envía `<lastmod>` honesto (mentir lo degrada).
- **Logs del servidor** = la verdad: qué rastrea Googlebot, con qué frecuencia, qué 404/redirige. GSC
  Crawl Stats da la versión resumida.
- **Profundidad ≤3 clics** de home a página prioritaria; lo profundo se rastrea tarde o nunca.

## El render path (lo que decide si te indexan)
Googlebot hace **dos olas**: HTML crudo primero, render de JS después (cola, con retraso/costo). CSR
puro arriesga indexar tarde o vacío. Jerarquía: **SSG > SSR > hydration > CSR puro** para SEO crítico.
- Contenido y links en el **HTML inicial**, no inyectados por JS post-load.
- Evita bloquear JS/CSS en `robots.txt`: si Google no rinde, ve una página rota.
- `<link rel="canonical">` **absoluto**; nunca a `http`, a redirect, ni a `noindex` (señal contradictoria).

## Core Web Vitals — campo, no laboratorio (ver [[68-seo-tecnico-geo]])
Se miden en **CrUX (percentil 75 real)**, no en Lighthouse. Umbrales 2026 endurecidos:

| Métrica | Bueno | Nota 2026 |
|---|---|---|
| LCP | <2.5s | sitios con LCP >4s rinden peor en recuperación post-update |
| INP | <200ms | el más fallado; reemplazó FID, ahora señal primaria |
| CLS | <0.1 | `width/height` en img, reservar slots de ads/embeds |

Los tres pasan **a la vez** o no cuentan. INP: rompe tareas largas de JS (`scheduler.yield`), hidrata
lo crítico primero, baja main-thread work. LCP: preload del hero, `fetchpriority=high`, sin JS bloqueante.

## Schema avanzado (JSON-LD)
Más allá de `Product`: anida `BreadcrumbList`, `FAQPage`, `Organization` con `sameAs`, `Review`/
`AggregateRating`. El schema correcto da rich results **y** ayuda al LLM a parsear entidades para citarte.
Valida con Rich Results Test. Marca `Product` con `price`+`priceCurrency` (COP) para Merchant/AI.

## Internal linking que mueve autoridad
Modelo **pillar → cluster bidireccional**: la pillar (ej. "Melena de León") enlaza a cada sub-artículo
y cada uno devuelve a la pillar. Concentra autoridad temática y mantiene lo prioritario a ≤3 clics.
Anchor descriptivo (no "clic aquí"). Enlaza **desde** páginas con autoridad **hacia** las que quieres rankear.

## GEO — ser citado por la IA
31% usa AI search; las AI Overviews recortan CTR orgánico 30-50% pero el referido AI convierte 4-5×.
Lo que gana citación: **perspectiva propia / data propietaria / explicación más profunda**, respuesta
directa en el primer párrafo, encabezados-pregunta, tablas. `llms.txt` **sigue sin usarse** por AI search.

## Gotchas
1. Facetas/sort sin control = crawl budget evaporado en sitios e-commerce.
2. `<lastmod>` falso en sitemap → Google desconfía del sitemap entero.
3. Lighthouse 100 que falla en CrUX: optimizaste lab, no campo.
4. Canonical a `noindex` o cadena de redirects = señales que se anulan.
5. Bloquear JS/CSS "para ahorrar crawl" → render roto, contenido no indexado.

**Fuentes:** flewny.com (Google Jan 2026 update) · digitalapplied.com (internal linking 2026) ·
pageonepower.com (schema audit 2026) · clickrank.ai (site structure AI).

Cruza con [[68-seo-tecnico-geo]] y [[268-content-marketing-seo-writing]].
