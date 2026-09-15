# 70 — Eventos, ticketing & experiencias en vivo

Un sitio de eventos no vende un producto reabastecible: vende **un momento irrepetible con cupo finito**. Por eso el FOMO y la scarcity NO son trucos de growth — son la verdad del negocio (los asientos se agotan, la fecha pasa). **Léelo para conciertos, festivales, conferencias, fiestas, lanzamientos** (Bendita Pola podría correr eventos). Pareja de 46 (booking/fechas), 44 (mapas/venue), 29 (pricing), 31 (urgencia honesta). Regla de oro: **las 4 W (What/When/Where/Who) visibles sin scroll + fees incluidos desde el inicio.**

## 1. El género: vender una experiencia + una fecha

**Tipos** (UX distinta): concierto/festival (multi-día, multi-stage, el **lineup ES el producto**), conferencia (speakers + agenda filtrable), deportes (asiento reservado, seat map duro), club night/fiesta (cover, lista, RSVP), evento local/comunitario (informal, cash-on-site), virtual/híbrido. Para un cliente como Bendita Pola: *club night / lanzamiento / festival cervecero local* = hype visual + RSVP/boletería ligera + WhatsApp.
**Lo que la UX debe hacer:** transmitir la *energía/identidad de ESTE evento* en 2 seg · responder las 4 W instantáneas · crear anticipación (countdown, lineup por fases) · convertir con fricción mínima · entregar el ticket al teléfono. El hype se construye en oleadas: *save the date → lineup fase 1 → early-bird → lineup completo → última tanda → día del evento*.

## 2. El event landing & diseño de hype

**El hero** no es un hero de SaaS — es un **poster de festival hecho web**: foto/video full-bleed con la energía del evento, tipografía expresiva oversized (tendencia 2026: texto enorme + contenido mínimo), las 4 W incrustadas (**NOMBRE · FECHA · CIUDAD/VENUE**) y un CTA único ("Comprar boletas"). El **aftermovie** de ediciones pasadas en loop = combustible de hype.
**El lineup como producto:** grid de artistas/speakers con **jerarquía de headliner clara** (el cabeza de cartel ocupa más espacio/peso tipográfico — réplica de la jerarquía del poster). Revelado por fases para sostener anticipación.
**El programa/agenda** (multi-día/multi-stage es UX real): tabs por día, columnas por escenario, filtro por género/track, "agregar a mi agenda".
**Resto:** venue + mapa + cómo llegar · FAQ (edad, qué llevar, reembolsos, lluvia) · **social proof = ediciones pasadas** (galería, nº asistentes, aftermovie) · **countdown timer real** · franja de patrocinadores. **>65% del tráfico es mobile** → single-scroll responsive primero.

## 3. Ticketing & checkout (el núcleo)

**Tiers:** GA/VIP/Early-bird/Palco en tabla comparativa con qué incluye. Early-bird con cupo visible ("quedan 30 a este precio") = scarcity honesta. **Regla anti-backlash: el precio mostrado incluye los fees desde el inicio** — el drip pricing es el pecado capital del ticketing.
**Seat map (el problema difícil):** mapa interactivo **particionado por sección** (zoom a tu sección, no cargar 20.000 asientos). Reto crítico: el mapa se vuelve *stale* en segundos en alta demanda → **actualización en tiempo real** (pub/sub por sección) para no hacer clic en un asiento ya vendido. Metas: <200ms cargar, <500ms reservar. Para eventos sin numerar (la mayoría de fiestas/festivales LatAm): saltarse el seat map, solo selector de cantidad (más simple = más conversión).
**Carrito + timer de retención:** al reservar, los asientos se **bloquean con countdown** ("tienes 8:00") — ansiedad funcional que evita overselling. Checkout de 30-90s.
**El on-sale de alta demanda (Taylor Swift problem):** **waiting room/cola virtual** con posición *aleatoria* entre los primeros (mata la ventaja del bot, percibe justicia) + estado transparente ("eres #12.000, ~5 min"); **página estática de holding** por CDN antes del on-sale; **anti-bot en capas** (rate limiting, CAPTCHA conductual, login, fingerprinting, límite 4-6 boletas/cuenta); **cache de inventario en memoria** (3-5s) + gateways de pago con failover.

## 4. Pago LatAm, ticket digital, entrada & on-site

**Pago LatAm (clave para Colombia):** no basta tarjeta → **PSE** (transferencia ACH, el dominante), **Nequi** (billetera, 18M+ usuarios), tarjeta. Pasarelas: **Wompi** (grupo Bancolombia, PSE+Nequi+tarjetas nativo) o **Bold**. Eventos informales: pago contra-entrega/efectivo en puntos (modelo TuBoleta con red de puntos físicos).
**El ticket digital:** QR/barcode que vive en el teléfono; estándar 2026 = **Apple/Google Wallet**. El **enfoque DICE anti-scalping** es la referencia: el ticket vive *dentro de la app*, el QR **solo se genera/rota el día del evento** (sin PDF ni screenshot revendible), ligado al número de teléfono.
**Entrada & on-site:** escaneo rápido (el QR rotativo evita duplicados), cashless **wristband NFC** recargable, app del evento (mapa de stages/baños/comida + horarios push). **Reventa controlada** (único canal = dentro de la plataforma, a precio cara o tope, recolocando al siguiente en lista — modelo DICE "waiting list" / TuBoleta "Pásala"): mata al scalper sin castigar al fan.

## 5. Discovery, marketing & realidad LatAm

**Discovery:** browse/búsqueda por fecha/ciudad/género; tarjetas con fecha+venue+precio desde+thumbnail del poster; filtros "este finde / cerca de mí". **Marketing viral:** botón compartir nativo, "1.2k van" (FOMO social), agregar al calendario, emails escalonados (compraste → 1 semana antes → día de → "puertas abren").
**El ángulo LatAm (donde se vuelve local):** **WhatsApp ES el canal** (info, atención *y venta de boletas* — TuBoleta ya vende por WA). Para Bendita Pola: el landing termina en CTA de WhatsApp que dispara un bot (tipo Addrian) que cotiza, cobra por PSE/Nequi/link de pago (Wompi/Bold) y envía el QR — flujo 100% conversacional sin checkout web complejo. **Eventos informales:** flyer-landing + RSVP/lista + cover en puerta o link de pago (no sobre-ingenierizar). El promotor local maneja la lista por WA/IG DM; el sitio complementa, no reemplaza.

## 6. Mobile, virtual/híbrido & 2026

**Mobile-first absoluto:** el ticket vive en el teléfono y se usa *el día del evento* (puerta, mapa, horarios) — diseñar para esa mano, de noche, poca batería, mala señal (QR offline-friendly). **Virtual/híbrido:** "venue online" con streaming, chat en vivo, salas, tier de boleto digital. **A11y:** seat map navegable por teclado/screen-reader, contraste, baja carga cognitiva.
**Tendencias 2026 (con honestidad):** **dynamic pricing** (sube ingresos pero riesgo de *backlash* feroz — si se usa: caps claros + explicación visible, o se lee como avaricia) · **AI** (chatbots de asistencia, recomendaciones, predicción de demanda) · **NFT tickets** (sirve para ticket verificable + anti-fraude + coleccionable, pero el branding "NFT/cripto" está quemado → vende el beneficio, no el buzzword).

## Eventos/ticketing anti-patterns — blacklist
**drip pricing / fees ocultos** al final del checkout (el #1 destructor de confianza) · **sin claridad de urgencia** (scarcity falsa o ninguna señal de cuántas quedan) · **seat map malo** (lento, no se actualiza, sin zoom por sección, ilegible en mobile) · **sin ticket mobile / solo PDF por email** (invita al fraude/scalping) · **on-sale que se cae** (sin cola virtual, CDN, cache de inventario, failover de pago) · **sin countdown / sin fecha-lugar** en el hero · **diseño genérico no tematizado** (template de SaaS en vez del poster del evento) · **scalping no abordado** (sin reventa controlada ni QR rotativo) · **LatAm: solo tarjeta** sin PSE/Nequi/efectivo, e ignorar WhatsApp como canal de venta · **registro obligatorio** en checkout normal (matar guest checkout fuera de on-sales).
