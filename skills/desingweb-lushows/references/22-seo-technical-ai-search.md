# 22 — SEO técnico, metadata, schema & AI-search (GEO/AEO)

Playbook de implementación 2026 para cuando despliegas un sitio: que rankee en Google Y sea citado por IA (AI Overviews, ChatGPT Search, Perplexity, Gemini). **Léelo al cerrar cualquier sitio público.** Estado real 2026: **FAQ/HowTo rich results murieron (may-2026)**, INP es Core Web Vital, y el giro hacia AI-search.

## 1. On-page que SIGUE importando

- **Title:** 50-60 car (~600px; Google trunca por píxeles). Formato: `Keyword | Beneficio | Marca`. No es ranking factor directo, pero un title truncado mata el CTR. Uno por página, único.
- **Meta description:** ya NO es ranking factor; es copy de venta para el snippet (CTR). 150-160 car. Google la reescribe ~60% — escríbela bien sin obsesión.
- **Headings:** un solo `<h1>` = tema. `<h2>/<h3>` jerárquicos. En 2026 sirven doble: estructura para Google + *chunking* para LLMs (extraen respuestas por sección). H2 en forma de pregunta cuando aplique.
- **HTML semántico** (`header/nav/main/article/section/footer`, `<button>`/`<a>`, `alt` real) = piso para a11y y crawlers de IA.
- **Enlazado interno:** anchor descriptivo (no "click aquí"); *topic clusters* (pilar + satélites enlazados). De los factores más subestimados.
- **URLs:** cortas, minúscula, guiones, con keyword, sin parámetros basura.
- **Canonical** auto-referencial SIEMPRE (previene canibalización por http/https/www/trailing slash/UTM).
- **Factores reales 2026:** contenido con experiencia de primera mano (E-E-A-T), autoridad temática, CWV, profundidad, backlinks de calidad, estructura citable por IA.

## 2. `<head>` completo (copy-paste)

```html
<html lang="es-CO">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Melena de León en Cápsulas 250mg | Hongos Funcionales | BIO-SETA</title>
  <meta name="description" content="Melena de León (Hericium erinaceus) 250mg. Apoyo cognitivo. Envío a toda Colombia. Compra por WhatsApp.">
  <link rel="canonical" href="https://bioseta.co/hongos/melena-de-leon-capsulas">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <!-- Open Graph (FB, WhatsApp, LinkedIn) -->
  <meta property="og:type" content="product">
  <meta property="og:title" content="Melena de León en Cápsulas 250mg | BIO-SETA">
  <meta property="og:description" content="Hericium erinaceus 250mg. Apoyo cognitivo. Envío a toda Colombia.">
  <meta property="og:image" content="https://bioseta.co/img/melena-og.jpg">
  <meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
  <meta property="og:url" content="https://bioseta.co/hongos/melena-de-leon-capsulas">
  <meta property="og:locale" content="es_CO"><meta property="og:site_name" content="BIO-SETA">
  <!-- Twitter/X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Melena de León 250mg | BIO-SETA">
  <meta name="twitter:image" content="https://bioseta.co/img/melena-og.jpg">
  <!-- Favicons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png"><!-- 180x180 -->
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0f3d2e">
</head>
```
**og:image:** exactamente **1200×630px** (1.91:1), <8MB, texto legible, URL absoluta. Es lo que se ve al compartir en WhatsApp → mala imagen = menos clics.

## 3. Structured Data / JSON-LD (lo que dispara rich results en 2026)

**Disparan HOY:** Product (Merchant Listing), Review/AggregateRating, Article/BlogPosting, Video, Event, Breadcrumb, Organization (entidad/Knowledge Panel), LocalBusiness.
**YA NO disparan nada (deprecados may-2026):** **FAQPage** y **HowTo** (schema válido, cero lift visual — el contenido FAQ sigue sirviendo como material citable por IA).
**Producto e-commerce:**
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"Product",
  "name":"Melena de León en Cápsulas 250mg",
  "image":["https://bioseta.co/img/melena-1x1.jpg","...4x3.jpg","...16x9.jpg"],
  "description":"Hericium erinaceus, 120 cápsulas de 250mg.",
  "sku":"BS-MEL-120","brand":{"@type":"Brand","name":"BIO-SETA"},
  "offers":{"@type":"Offer","url":"https://bioseta.co/...","priceCurrency":"COP","price":"89000",
    "availability":"https://schema.org/InStock","itemCondition":"https://schema.org/NewCondition"},
  "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"37"} }
</script>
```
**LocalBusiness/Store:** `name, image, telephone, priceRange, address (PostalAddress CO), geo, openingHoursSpecification, sameAs[]`. Añade **Organization** (logo/url/sameAs) en la home y **BreadcrumbList** en internas. Valida en el **Rich Results Test**.

## 4. AI Search / GEO-AEO (el gran giro 2026)

Google (15-may-2026) publicó su guía de optimización para IA y **desmintió el "GEO de pago"**: llms.txt, *chunking* artificial, reescritura "AI-specific" y *schema overloading* **NO ayudan a AI Overviews/AI Mode**. Lo que SÍ:
- **Answer-first:** responde la pregunta en la 1ª frase de cada sección, luego desarrolla (los LLMs extraen el 1er párrafo conciso).
- **Claridad de entidad:** nombra marca/producto/atributos explícita y consistentemente (Organization + sameAs ayudan a desambiguar).
- **Citabilidad:** datos originales, cifras, comparaciones, experiencia de primera mano. El pool de citas va más allá del top 10.
- **Multimodal:** imágenes/video propios se surfacean.
- **Autoridad/menciones de marca** auténticas en sitios de confianza.
**Matiz `llms.txt`:** inútil para Google, pero **sí aporta a ChatGPT Search/Perplexity/Claude** — barato, ponlo (índice markdown en `/llms.txt`), sin esperar nada de Google. No existe "schema mágico para LLMs"; la base es contenido citable + hygiene técnica.

## 5. Fundación técnica

**robots.txt con directivas de IA** (consenso 2026 = "bloquea entrenamiento, permite búsqueda en vivo"):
```
User-agent: Googlebot
Allow: /
# Buscadores en vivo (PERMITIR — generan citas/tráfico)
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
# Scrapers de entrenamiento (BLOQUEAR si no quieres ceder data)
User-agent: GPTBot
Disallow: /
User-agent: Google-Extended
Disallow: /
User-agent: CCBot
Disallow: /
Sitemap: https://bioseta.co/sitemap.xml
```
(Decisión de negocio: dejar `GPTBot`/`ClaudeBot` en `Allow` cede más data pero puede aumentar conocimiento del modelo sobre tu marca.)
- **XML sitemap:** solo URLs canónicas indexables (200, sin noindex), `<lastmod>` real, en robots.txt + Search Console.
- **CWV (desempate de ranking):** LCP <2.5s, **INP <200ms** (reemplazó FID, mide TODAS las interacciones), CLS <0.1.
- **Mobile-first indexing:** Google indexa la versión móvil. Si no existe en móvil, no existe.
- **Render:** prefiere **SSR/SSG** para SEO. CSR puro (SPA sin prerender) llega tarde/vacío para crawlers de IA (no ejecutan JS pesado). Si usas SPA, prerenderiza.
- **hreflang** recíproco + `x-default` para i18n. **301** permanente (pasa equity), 302 temporal, sin cadenas de redirect.

## 6. SEO local + LatAm/Colombia

- **Google Business Profile** = activo local #1 (categoría correcta, fotos reales, horario, responde reseñas). Proximidad + reseñas dominan el local pack.
- **NAP consistente** (Nombre/Dirección/Teléfono idénticos en web/GBP/directorios).
- **Keywords locales en español** con ciudad/barrio ("hongos funcionales Bogotá"); variantes regionales (CO≠MX≠AR).
- **WhatsApp click-to-chat** como CTA: `https://wa.me/57...?text=Hola%20quiero%20info` + `contactPoint` en schema.
- **Directorios LatAm:** Páginas Amarillas CO, Google Maps, Waze, nichos del sector.

## SEO anti-patterns — blacklist
keyword stuffing · múltiples `<h1>` · contenido thin/duplicado o "AI-rewriting" sin valor · cloaking · texto oculto · comprar backlinks/PBNs · falsear AggregateRating (manual action) · og:image fuera de 1200×630 o ausente · canonical equivocado/ausente con duplicados · bloquear CSS/JS en robots.txt · CSR puro sin prerender para contenido que debe rankear · confiar en FAQ/HowTo schema para rich results (deprecados) · pop-ups intersticiales en móvil · cadenas de redirect.
