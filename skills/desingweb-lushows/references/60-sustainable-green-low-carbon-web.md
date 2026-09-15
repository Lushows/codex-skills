# 60 — Diseño web sostenible, verde & bajo en carbono

La industria digital genera **2-5% de las emisiones globales de CO2** (más que la aviación); los data centers consumieron ~536 TWh en 2025 (~2% de la electricidad mundial). Pero la idea-fuerza es liberadora: **sostenible = ligero = rápido = más barato de servir = mejor Core Web Vitals = mejor SEO y conversión.** No hay trade-off — el sitio más verde y el más rápido son casi siempre el mismo. **Léelo para construir sitios eficientes y como argumento de marca/ESG.** Pareja de 38 (performance — es la misma optimización vista desde la ética), 28 (ética).

## 1. El caso & la ciencia

**El reparto energético (SWDM v4):** dispositivos del usuario **54%**, redes **24%**, data centers **22%**. Implicación: más de la mitad del impacto ocurre en el teléfono del cliente — un sitio pesado castiga su batería y su plan de datos, no solo "la nube".
**Cómo se mide:** el estándar de facto es el **Sustainable Web Design Model (SWDM)**, actualizado a **v4 (jul 2025)**. Usa el *page weight* como proxy de energía: `CO2e = GB × 0.194 kWh/GB × 494 gCO2e/kWh` (494 = intensidad media de red global). v4 separa emisiones **operacionales** de **embodied** (fabricación de hardware) y rebaja estimaciones **40-50% vs v3**.
**Números de referencia:** media global **~0.36 g CO2e por pageview**; **página mediana 2.86 MB desktop / 2.56 MB mobile** (HTTP Archive 2025 — 5× más pesada que hace 15 años; el bloat es la norma). Un sitio con 10.000 visitas/mes emite ~31.5 kg CO2e/año; uno rating A+ solo ~3.5 kg — **-89% sin cambiar el contenido, solo la ingeniería.**
**Sustainable Web Manifesto** (Wholegrain Digital), los principios que firman las agencias serias: **Clean** (energía renovable), **Efficient** (mínima energía/recursos), **Open** (accesible a todos), **Honest** (transparencia del impacto), **Regenerative** (mejorar, no solo sostener), **Resilient**.

## 2. Reducir page weight & energía (la palanca práctica)

Los culpables del carbono son **idénticos a los de performance**: imágenes, video, fuentes, JS, third-party.
- **Imágenes** (mayor peso típico): **AVIF/WebP** (40-70% menos bytes), `srcset`/`sizes`, dimensionar al display real, **lazy-loading** below-the-fold, comprimir agresivo. Una hero de 2 MB puede ser el 60% del carbono de la página.
- **Video:** nunca **autoplay**; click-to-play, poster estático, `preload="none"`. El mayor multiplicador de transferencia.
- **Fuentes:** **system font stack** elimina descargas; si usas web fonts, solo **WOFF2**, subset, máx 2 pesos, `font-display:swap`.
- **JS** (el byte más caro — se transfiere Y se parsea/ejecuta en ese 54% del dispositivo): auditar bundle, tree-shaking, code-splitting, eliminar libs para lo que CSS/HTML nativo ya resuelve. Preferir **HTML estático + progressive enhancement** sobre SPAs pesadas.
- **Third-party:** cada tag (analytics, chat, ads) añade transferencia + ejecución fuera de tu control. Auditar con request map y eliminar sin piedad.
- **Reducir transferencia:** caching agresivo (`Cache-Control` largo + hashing — el repeat-visit no debe redescargar nada), HTTP/2-3, Brotli/gzip en lo textual, eliminar CSS/JS sin usar.
- **La auditoría "¿necesitas esto?":** el carbono más limpio es el que no se emite. Identifica las páginas más pesadas, los carruseles que nadie usa, la librería de iconos entera importada por 3 iconos. **Digital declutter:** cada feature tiene coste energético permanente.

## 3. Green hosting & infraestructura

El **mismo sitio** emite menos en hosting renovable (la fórmula aplica factor reducido). Pasos:
- **Verifica con Green Web Check** (thegreenwebfoundation.org) — testa si tu dominio corre en un proveedor del Green Web Dataset; si pasa, genera un badge.
- **Green Web Directory** (app.greenweb.org/directory): proveedores verificados, filtrable por país/servicio. Notables: Cloudflare Pages (100% renovable, partner GWF), GreenGeeks, Kualo, Krystal.
- **Ojo con CDN:** si pones un CDN delante, el check evalúa el CDN, no el origen — confirma ambos. **Edge/CDN bien usado** reduce distancia de red (ese 24%): servir desde el nodo más cercano = menos saltos.
- **Server-side:** SSG (Astro, Eleventy, Hugo) sobre rendering dinámico cuando se pueda; cada request desde caché es energía ahorrada.

## 4. UX & decisiones de diseño sostenibles

- **Eficiencia del user-journey:** ayudar a completar la tarea en menos pasos = menos pageviews = menos energía total. Buena IA, buscador que funciona, formularios cortos. El UX rápido *es* UX verde.
- **Dark mode en OLED:** píxeles negros apagados = ahorro real de energía del dispositivo. Ofrece `prefers-color-scheme`.
- **Estética "leaner-is-better":** system fonts, paletas sobrias, menos imágenes pero mejor elegidas, **SVG/CSS para decoración** en vez de PNG, vector sobre fotografía pesada.
- **Video bajo demanda, nunca autoplay**; fuera GIFs decorativos (un GIF puede pesar 10× un MP4 equivalente).
- **Diseño honesto / no manipulativo:** los **dark patterns** (scroll infinito, autoplay, infinite-feed adictivo) generan pageviews y consumo innecesarios. Sostenibilidad y ética de diseño convergen.

## 5. Medición & dev practices

**Herramientas:** **Website Carbon Calculator** (websitecarbon.com v4) — quick-check con rating **A+→F** (A+ = top más limpio; F = sobre la media de 0.36 g) · **Ecograder** (CO2.js + Lighthouse, lista priorizada de tareas) · **CO2.js** (Green Web Foundation, librería open-source: entran bytes, sale gCO2e; corre en Node/browser/edge — **lo que integras en tu pipeline**) · EcoPing / Carbon Badge.
**Carbon budget (igual que un performance budget):** (1) define objetivo, p.ej. **<0.5 g CO2e/pageview** y/o **<1 MB** en páginas clave; (2) integra CO2.js o sitespeed.io en **CI** — falla el build si excede, como Lighthouse CI; (3) trackea regresiones por PR. El carbono se gestiona como cualquier métrica de calidad: medido, presupuestado, en guardia automática.
**WSG — Web Sustainability Guidelines (W3C):** el "WCAG de la sostenibilidad". **First Public Draft 2025**, estructura calcada de WCAG (**92 guidelines, 254 success criteria**) cubriendo Planeta/Personas/Prosperidad, alineada con GRI (reporting corporativo). Aún no normativa; úsala hoy como checklist de madurez.

## 6. Negocio/marca & tendencias 2026

- **Green web como diferenciador:** badge de hosting verde + cifra de carbono publicada = credibilidad ante clientes y RFPs con criterios ESG.
- **Presión regulatoria:** **CSRD**, **EU Green Claims Directive** (anti-greenwashing); claims ambientales vagos ya no son seguros (CMA/ASA penalizan). Las WSG alineadas con GRI permiten meter el footprint digital en el reporting formal.
- **Carbon-aware / grid-aware computing** (la tendencia técnica 2026): el proyecto **Grid-aware Websites** del GWF + **Electricity Maps API** dejan que el frontend reaccione a la intensidad de carbono de la red en tiempo real (servir core cuando la red está "sucia", enriquecer con energía limpia).
- **Comunicación honesta:** publica el dato real medido, no claims inventados. Un badge verificado vale más que "100% carbon neutral" sin respaldo.

## Sustainability anti-patterns — blacklist
**autoplay** de video/audio y carruseles auto-rotando · **imágenes sin optimizar** (PNG/JPEG full-res, hero 2 MB+, sin lazy-load/`srcset`) · **GIFs decorativos** donde un MP4/CSS bastaría · **JS bloat** (SPA pesada para lo que sería HTML estático; librería entera por una función) · pila de **third-party sin auditar** · múltiples web fonts sin subset cuando system fonts servían · sin caching ni compresión (Brotli/gzip ausentes) · **hosting fósil** sin verificar en Green Web Check · **greenwashing** ("carbon neutral" sin medición ni offset verificable) · infinite scroll / dark patterns que inflan pageviews · **"heavy for no reason"** (WebGL/parallax puramente decorativo; ignorar el tema). **Idea-fuerza: cada gramo de CO2 que recortas recorta también tiempo de carga, coste y fricción.**
