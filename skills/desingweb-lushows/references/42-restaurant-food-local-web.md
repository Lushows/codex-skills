# 42 — Restaurante, gastronomía & negocio local (web + pedidos)

Playbook conversión + WhatsApp ordering para gastronomía/food (incl. agente de pedidos por WhatsApp) en LatAm/Colombia. **Léelo para cualquier web de restaurante/comida/local o flujo de pedidos.** Mapea a GASTROWHATS. Pareja de 11, 17, 21, 31, 22.

## 1. Estructura: "dónde, cuándo, qué, cómo pedir"

En los **primeros 3 segundos** el visitante hambriento debe saber *qué vendes, dónde estás y cómo pedir*. El éxito se mide en **órdenes, no estética**; +60% del tráfico es móvil (más en delivery LatAm). Mobile-first obligatorio.
**Estructura que convierte (one-pager/home):**
1. **Hero con appetite appeal** — foto/video del plato estrella full-screen (NO el logo ni el local vacío) + nombre + 1 línea de propuesta + **"Pedir por WhatsApp" sticky**.
2. **CTA dual sticky** — "Pedir" + "Reservar/Cómo llegar"; en móvil barra inferior fija (thumb-zone, ≥44px). Botones de orden bien dimensionados +34% conversión.
3. **Menú embebido** (HTML, no PDF — §2).
4. **Horarios + ubicación + mapa** prominentes (no en footer), estado en vivo ("Abierto · cierra 11pm").
5. **Prueba social** (reseñas Google, "recomendado por", fotos reales).
6. **Footer** — dirección, click-to-call, WhatsApp, zonas de domicilio.
**Velocidad = dinero:** <2s convierte mucho más; móvil optimizado +42% de pedidos. WebP/AVIF, lazy, hero <200KB, sin frameworks pesados para un menú.

## 2. Digital menu UX (a fondo)

El menú es un **motor de ventas**, no una lista de precios.
- **Categorías navegables** con anclas sticky (chips horizontales en móvil que saltan a secciones).
- **Items escaneables:** nombre + descripción sensorial corta + precio claro + foto. Tarjeta, no párrafo.
- **Descripciones que venden:** apela a vista/olfato/gusto, verbos de preparación ("horneado a la leña", "marinado 24h"). 1-2 líneas.
- **Tags dietéticos** con badge alto contraste + **ícono + texto** (🌱 vegano, GF, 🌶️ picante, alérgenos — nunca solo color).
- **Filtros** (vegetariano/vegano/picante/sin gluten) + **destacados/"más pedidos"** + **combos/upsell** arriba (suben el ticket).
- **El debate fotos:** **fast-casual/QSR/delivery → SÍ** (75% dicen que las fotos influyen; items con foto hasta +44% ventas; +35% órdenes en apps; 43% de Gen Z elige por fotos). **Fine dining → NO** (abaratan; mandan tipografía/espacio/copy; la foto vive en la galería).
- **Performance:** **JAMÁS un PDF** (lento, no-móvil, no indexable, inaccesible). HTML embebido → rápido, accesible, indexable, alimenta el schema Menu.

## 3. Online ordering & WhatsApp commerce (food)

**Flujo:** browse → customize (modificadores) → cart → checkout (delivery/pickup + datos) → pago/COD → confirmación → tracking.
**Customización** (crítico en comida): tamaños, modifiers (término, sin cebolla), extras (+queso $3.000), salsas — cada uno refleja precio + resumen del carrito.
**El patrón WhatsApp ordering (el más relevante LatAm):**
- **A) Catálogo web → WhatsApp pre-rellenado** (estilo BIO-SETA, para comida): el cliente arma el carrito → al confirmar abre WhatsApp con el pedido **ya redactado** vía `https://wa.me/57XXXX?text=<pedido URL-encoded>`. Plantilla:
```
🍔 *PEDIDO #[auto]*
2x Hamburguesa Doble (sin cebolla) — $24.000
1x Papas grandes — $8.000
--------------------------------
Subtotal: $32.000 · Domicilio (Norte): $5.000
*TOTAL: $37.000*
Entrega: 🛵 Domicilio · 📍 Dirección: ___ · 💳 Pago: Nequi / contraentrega
```
  Elimina ambigüedad: el operador recibe un pedido estructurado, no un chat caótico.
- **B) Ordering conversacional en WhatsApp** (el agente IA): saludo + menú (link o lista interactiva) → IA arma carrito en lenguaje natural → confirma modificadores + total → domicilio vs recoger (valida zona + cobra flete) → recolecta nombre/dirección/pago → confirma + ETA + tracking → notifica al operador.
**LatAm (Colombia):** **contraentrega** (efectivo/datáfono — dominante, sin pasarela) · **Nequi/Daviplata** (transferencia + captura como comprobante) · Bancolombia/MercadoPago/tarjeta. **Domicilio por zonas** (geocerca: Centro $0, Norte $5.000, ETA 30-45min). **Apps locales (Rappi/Didi) cobran 20-30%** → el pedido directo por WhatsApp conserva 100% del margen + los datos del cliente (el argumento de venta del agente). Valida cobertura antes de tomar el pedido.

## 4. Food photography & appetite appeal

- **Luz lateral o contraluz** revela textura/vapor/brillo/capas (modela el apetito más que nada; evita flash frontal plano).
- **Appetite appeal** (el arma secreta): frescura visible, vapor, queso fundido, condensación en la bebida fría, el corte que muestra el interior jugoso. Vende el deseo.
- **Consistencia** (misma temperatura de color/ángulo/estilo) = premium; inconsistencia = barato.
- **Autenticidad 2026:** la foto se ve **como la comida real que recibirás** (no idealizada decepcionante). Lo sobre-editado luce falso.
- **Premium/gourmet:** dark & moody, alto contraste, fondo oscuro. **Casual/QSR:** brillante, colorido, saturado, fondos claros.
- **Estrategia por capas:** hero shots pro (pocos, buena luz) anclan la identidad; contenido ligero de celular (luz natural) para redes/novedades.
- **Video "the sizzle":** background hero <6s, loop, mudo, peso bajo + fallback a imagen.
- **AI food imagery:** OK para mood/ambientación, **NUNCA para el plato real** (rompe confianza, roza publicidad engañosa). Si solo tienes fotos malas → mejor sin fotos.

## 5. Trust local & conversión

"Voy a meterme esto al cuerpo" → la confianza pesa más que en cualquier e-commerce.
- **Reseñas Google** embebidas + rating + "recomendado por", arriba del fold.
- **Ubicación:** mapa embebido, "Cómo llegar" (Google/Waze), parqueadero. **Horarios** con estado en vivo.
- **Click-to-call y WhatsApp** en todas partes (`tel:`, `wa.me`). **Reservas** (OpenTable/Resy o WhatsApp/formulario en LatAm).
- **Local SEO:** Google Business Profile consistente con el sitio (inconsistencia de horarios GBP↔schema = Google descuenta tu data).
- **Schema JSON-LD** subtipo `Restaurant` (desbloquea features de menú/reservas, ~30% más CTR):
```json
{"@context":"https://schema.org","@type":"Restaurant","name":"La Brasa","servesCuisine":"Colombian","priceRange":"$$",
 "telephone":"+57-300-000-0000","address":{"@type":"PostalAddress","streetAddress":"Cra 7 #80-20","addressLocality":"Bogotá","addressCountry":"CO"},
 "geo":{"@type":"GeoCoordinates","latitude":4.66,"longitude":-74.05},"acceptsReservations":"True",
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday"],"opens":"12:00","closes":"23:00"}],
 "hasMenu":{"@type":"Menu","hasMenuSection":[{"@type":"MenuSection","name":"Hamburguesas",
   "hasMenuItem":[{"@type":"MenuItem","name":"Doble Carne","description":"Dos carnes, cheddar, salsa de la casa","offers":{"@type":"Offer","price":"24000","priceCurrency":"COP"}}]}]}}
```

## 6. Estética & tendencias 2026

- **Fine dining/experiencia:** editorial, full-bleed photography, tipografía refinada, mucho aire, paleta cálida sosegada (Noma/Atomix). El sitio es atmósfera + storytelling, reserva discreta.
- **Casual/QSR/delivery:** utilidad de pedido rápido, brillante/colorido/app-like, CTA gigantes, menú-primero, fricción cero.
- **Paletas apetitosas:** cálidas/terrosas (tostado, terracota, mostaza, oliva, crema, chocolate, toques rojo/naranja que estimulan apetito; negro+dorado premium). **Evita azul/púrpura frío como protagonista** (suprime el apetito).
- **Tipografía:** serif editorial (fine dining); sans geométrica legible + display con personalidad (casual).
- **Vigente:** background video, scroll storytelling, micro-interacciones, modo app móvil, menú personalizado por hora del día.

## Restaurant-web anti-patterns — blacklist
**menú en PDF** (el pecado #1: lento, no-móvil, no indexable, inaccesible) · sin precios · no mobile/responsive · sitio lento (>3s) · hero con logo o local vacío en vez de comida · fotos amateur (flash plano, platos marchitos) · **AI imagery del plato real** (engañoso) · horarios/ubicación escondidos · CTA de pedido débil o sin click-to-call/WhatsApp · clipart cursi/stock genérico · menú oscuro ilegible (texto sobre foto sin overlay) · tags dietéticos solo por color · forzar app/registro antes de ver el menú · inconsistencia de horarios GBP↔schema↔sitio · carrusel auto rápido + pop-ups que tapan el menú en móvil · pedido que obliga a pasarela sin contraentrega/Nequi.

## Aplicación al agente WhatsApp (Addrian → comida)
Menú web HTML + schema `Restaurant`/`Menu` · carrito web → deep link `wa.me?text=` pre-rellenado · IA conversacional (arma carrito, confirma modificadores, valida zona, cobra flete, recolecta dirección+pago Nequi/contraentrega, da ETA, notifica operador) · fotos hero apetitosas + tags con ícono+texto · CTA sticky "Pedir por WhatsApp" + click-to-call + horario en vivo + reseñas Google.
