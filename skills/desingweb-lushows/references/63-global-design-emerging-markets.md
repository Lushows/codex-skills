# 63 — Diseño global, mercados emergentes & el next billion

Construir desde LatAm con ambición *mundial* significa diseñar para gente que NO se parece al usuario default de Silicon Valley: no tiene desktop, no tiene fibra, no tiene tarjeta de crédito, a veces ni lee con fluidez. No es caridad de diseño — es el mercado de crecimiento. **Léelo para productos con ambición global, LatAm/África/India/SE Asia, comercio WhatsApp** (el playbook exacto de BIO-SETA/GASTROWHATS). Pareja de 32 (i18n), 16 (a11y), 38 (performance), 62 (marketplace). Regla mnemotécnica: **pesa cada KB, asume que la red se cae, mete todo en el chat, dibuja antes de escribir, deja que paguen al recibir, valida en el barrio.**

## 1. La realidad del next billion — quiénes son

Usuario **mobile-only** (no mobile-first): nunca tocó un desktop ni lo hará. Dispositivo = **Android de gama baja** ($40-60), 512MB-2GB RAM, pantalla chica de baja resolución, batería limitada. Conectividad que **switchea WiFi→3G→2G→nada** según dónde esté parado. El dato que reordena todas las prioridades: en ~95% de mercados emergentes la gente usa **datos prepago caros**, muchos solo pueden costear ~250MB/mes → **cada MB que tu producto consume es dinero real que le sacas del bolsillo.** Supuestos occidentales que fallan: "todos tienen WiFi", "la pantalla es grande", "saben leer", "tienen tarjeta", "confían en pagar antes de recibir", "actualizar la app es gratis".

## 2. Diseñar para constraints (el core práctico)

- **Data-awareness explícita:** muestra cuánto pesa cada acción. Patrón Google: "Data Saver"/modo lite que comprime imágenes, difiere descargas y avisa el costo. Google Play actualiza apps **solo por WiFi por default** porque los datos cuestan — replica esa lógica.
- **Lightweight de verdad:** presupuesta **KB, no MB**. Inspírate en la familia "Go" (YouTube Go, Maps Go, Google Go, Files Go) — features pesadas comprimidas a pocos MB.
- **Progressive loading:** carga primero texto/estructura, después imágenes; placeholders que no requieren red; nunca bloquees la pantalla esperando un asset pesado.
- **Offline-first como arquitectura, no feature:** la app debe ser usable sin conexión. Guarda estado local, **encola acciones, sincroniza cuando vuelva la red**.
- **Optimistic UI + sync:** cuando el usuario actúa (envía, compra, guarda), confírmalo **inmediatamente en local** y sincroniza en background. Nunca dejes la UI colgada esperando el servidor en 2G.
- **Tolerancia a la red caída:** reintentos automáticos, **resume de descargas** (no reiniciar el MB ya gastado), degradación elegante (si no carga la imagen, muestra texto y precio).
- **Sharing offline:** peer-to-peer local (enviar entre teléfonos cercanos sin gastar datos) es un patrón nativo de estos mercados.

## 3. Mobile-only, WhatsApp & la realidad de plataforma

En LatAm e India, **WhatsApp es el sistema operativo del comercio**, no una app de chat. Datos 2025-26: India ~532M usuarios, Brasil ~148M (~98% de smartphones). **Commerce conversacional LatAm ~$18.2B en 2025 (+35% YoY), ~72% por WhatsApp**; en Brasil **78% de negocios venden por WhatsApp**, catálogos +89% en 2025. Implicaciones:
- **El chat ES la interfaz.** No fuerces al usuario a salir de WhatsApp a un sitio web. El ciclo completo (descubrir, preguntar, elegir, pagar) vive en el chat (catálogos nativos, pagos embebidos vía Pix/Mercado Pago/PSE/UPI).
- **Agentic commerce 2026:** Meta declaró el shopping agéntico como pilar. WhatsApp 2026 está donde WeChat en 2017-18 pero con 3× el user base. Bot + IA + catálogo + pago en un hilo = el patrón ganador (exactamente BIO-SETA/Addrian).
- **PWA > app nativa pesada** para web: en gama baja, instalar/actualizar una nativa cuesta datos y RAM. Una PWA data-light (instalable, offline, pocos KB) suele ganar. Nativa solo si justificas el peso.
- **Pantalla chica y barata:** targets táctiles ≥48px, una columna, evita hover, evita gestos finos.

## 4. Alfabetización, lenguaje & diseño cultural

Para **baja alfabetización y first-time internet users**, la evidencia (Microsoft Research / HCI) es clara: las interfaces de **solo texto son inusables** para no-letrados y propensas a error para letrados novatos.
- **Iconos + texto SIEMPRE juntos**, nunca icono solo (un icono de descarga debe decir también "Descargar" — el par redunda y enseña).
- **Voz y audio:** IVR, notas de voz, búsqueda por voz reducen el tipeo. En WhatsApp las **notas de voz son nativas del comportamiento** — acéptalas y transcríbelas (GASTROWHATS ya usa Whisper, correcto).
- **Visual sobre textual:** imágenes, video corto, animaciones que muestran en vez de explicar.
- **Simplicidad radical:** una acción primaria por pantalla, jerarquía clara, cero jerga.
- **Idioma local, no el idioma "país":** español neutro falla; el colombiano, el portugués brasileño, el spanglish funcional importan. Localiza tono, no solo palabras.
- **Color y símbolos cargan cultura:** rojo = suerte (China) / peligro (Occidente); blanco = pureza o luto según región. Valida imágenes (gente, gestos, manos) con la audiencia local.

## 5. Pagos, confianza & comercio en emergentes

El supuesto más caro: "el usuario paga online con tarjeta antes de recibir". Falso.
- **Cash-on-delivery (COD) domina** y es el ancla de confianza: paga **cuando el producto llega a su mano**. Sin COD pierdes ventas reales.
- **Mobile money / transferencia instantánea local:** **Pix** (Brasil, gratis/instantáneo, vía banco), **Nequi/PSE** (Colombia), **Yape/PLIN** (Perú), **SPEI** (México), **UPI/WhatsApp Pay** (India), **M-Pesa** (África, vía SIM, sin banco). Nota: M-Pesa es para **unbanked** (el celular ES la cuenta); Pix/UPI/Yape son sobre cuenta bancaria.
- **La confianza es el producto:** señales locales pesan más que tu marca global. Respuesta humana rápida por WhatsApp, testimonios reales, COD, y aceptar el **método de pago del país** son las verdaderas trust signals.
- **Economía informal / social commerce:** muchas ventas son negocio-a-vecino vía status/grupos de WhatsApp, sin "tienda" formal. Diseña para ese flujo informal, no contra él.

## 6. Estrategia de producto global + LatAm 2026

- **Global-first desde la arquitectura, no localizar después:** separa contenido de código (i18n nativo), no hardcodees moneda/fecha/idioma, deja hooks de pago por país desde el día 1. Re-arquitecturar después cuesta 10×.
- **Localización ≠ traducción:** adapta lengua, cultura, técnica (red/dispositivo), legal y UX a la vez. Cuando un producto se *siente* local, genera confianza instantánea y convierte más rápido. **Valida con la audiencia real**, no con tu intuición de Bogotá/SF.
- **LatAm (Colombia como base):** mobile-only + WhatsApp + Nequi/PSE + COD + español colombiano. Lo que funciona en Colombia escala a México/Perú/Brasil con ajustes de pago/idioma, no rediseño.
- **Tendencias 2026:** crecimiento del Global South como mercado principal, **IA localizada** (bots que hablan el dialecto y conocen el pago local), super-apps y comercio agéntico sobre WhatsApp, accesibilidad por IA (voz/imagen para baja alfabetización) como default.

## Global-design anti-patterns — blacklist
**desktop-first / responsive como afterthought** (el usuario es mobile-only) · **data-heavy por default** (autoplay de video, imágenes sin comprimir, fuentes pesadas, hero de 5MB — cada MB es dinero del usuario) · **ignorar la conectividad intermitente** (UI que se cuelga sin red, sin offline/reintentos/optimistic UI) · **asumir gama alta** (animaciones costosas, JS pesado que traba un Android de 1GB) · app nativa pesada cuando una PWA basta · **solo-texto y jerga** (sin iconos+label, sin voz, sin visual — inusable para baja alfabetización) · **asumir tarjeta / pago anticipado** (sin COD, sin Pix/Nequi/UPI/M-Pesa) · **ceguera cultural** (colores/imágenes/gestos sin validar, "español neutro" como única lengua) · **sacar al usuario del chat** (forzar salir de WhatsApp a un sitio roto en 2G) · localizar al final (global como parche) · **diseñar desde la suposición** y no desde research inmersivo (el principio fundacional de Google NBU: pasar tiempo en la comunidad real antes de diseñar).
