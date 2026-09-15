# 68 — SEO técnico & GEO (Generative Engine Optimization)

El SEO 2026 tiene dos frentes: que Google **rankee** tu página y que los LLMs (ChatGPT/Perplexity/Gemini/AI
Overviews) te **citen**. El tráfico se desplaza de clics a citaciones.

## SEO técnico — fundamentos
- **Crawlability:** `robots.txt` (no bloquees JS/CSS que el render necesita); `sitemap.xml` con URLs canónicas.
- **Canonical:** `<link rel="canonical">` absoluto a la URL preferida (evita duplicados).
- **Meta:** `<title>` ~60 chars, `<meta description>` ~155 (CTR, no ranking).
- **Rendering:** Google rinde JS con retraso/costo. **SSR/SSG** (Next.js/Astro) = HTML completo → indexación fiable. CSR puro arriesga contenido no indexado. Para SEO crítico: SSR.
- **Mobile-first indexing:** Google indexa la versión móvil; si tiene menos contenido, pierdes ranking.

## Core Web Vitals (ranking factor, al percentil 75 de datos REALES de campo)
- **LCP** (carga): bueno <2.5s; **2026 endureció a ~2.0s.**
- **INP** (responsividad, reemplazó FID en 2024): bueno <200ms; **el más fallado (43% de sitios), promovido a señal primaria 2026.**
- **CLS** (estabilidad): bueno <0.1. Los tres deben pasar a la vez. Optimiza: imágenes con `width/height`, `font-display: swap`, code splitting, evitar JS bloqueante para INP.

## Structured data (schema.org JSON-LD)
Marca entidades (`Organization`, `Product`, `FAQPage`, `Article`). Habilita rich results y ayuda a LLMs a entender entidades.
```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Product","name":"Melena de León 120 cáps","brand":"BIO-SETA",
 "offers":{"@type":"Offer","price":"89000","priceCurrency":"COP"}}</script>
```

## GEO / AEO
- **`llms.txt`** — hype 2025. **Realidad verificada: ningún sistema de AI search lo usa** (Mueller confirmó que AI
  Overviews lo ignora; sin correlación con citaciones). Único uso real: herramientas de dev (Cursor/Copilot/Claude) que ingieren tus docs. **NO es la palanca de visibilidad AI.**
- **Lo que SÍ funciona para ser citado:** autoridad genuina del tema, menciones consistentes en fuentes externas de
  calidad, contenido estructurado que responde preguntas directamente (encabezados como preguntas, respuesta en el primer párrafo, listas, tablas), señales de entidad y **E-E-A-T**.
- **i18n SEO:** `hreflang` recíproco para variantes idioma/región + `x-default`.

## Medición
Google Search Console (impresiones/posición/CWV). AI-referral: filtra `referrer` de `chatgpt.com`/`perplexity.ai`/`gemini.google.com`; LLMrefs/Profound rastrean menciones en respuestas AI.

## Gotchas
1. CWV se mide en **campo (CrUX)**, no en lab — un Lighthouse 100 puede fallar en campo.
2. Invertir en `llms.txt` esperando citaciones = desperdicio; invierte en autoridad + estructura.
3. `hreflang` no recíproco (A→B pero B no→A) → Google lo ignora todo.
4. CSR puro: Googlebot indexa tarde o nunca el contenido inyectado por JS.
5. Bloquear bots AI (GPTBot, PerplexityBot) en robots.txt = invisibilidad en AI search; decide conscientemente.
6. Canonical apuntando a `http` o a página `noindex` = señales contradictorias.

**Fuentes:** developers.google.com/search/docs (core-web-vitals) · digitalapplied.com (CWV 2026) · searchsignal.online (llms.txt 2026) · searchengineland.com (GEO).
