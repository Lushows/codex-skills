# ⏱️ Actualización Google Ads — snapshot 13-jun-2026 (LEER PRIMERO si dudas si algo cambió)

Changelog fechado de lo que cambió en Google Ads en 2024–2026. La subasta (Ad Rank/Quality Score) y "captura
de intención" siguen igual; lo que cambió son **features de IA, medición y tipos de campaña concretos**. Cada
ítem dice **[CONFIRMADO]** (bien establecido) o **[RODANDO/verificar]** (reciente o fecha aproximada — confirma
en TU cuenta). Cruza con el módulo de fondo indicado. Re-verifica trimestral: en Google la IA mueve esto rápido.

## 1. Búsqueda con IA — AI Max for Search (lo más nuevo, ver 90, 21, 22)
- **[CONFIRMADO] AI Max for Search (2025):** suite de un toggle que enciende, en campañas de Search,
  **expansión tipo broad-match** ("search term matching"), **automatización/generación de assets** del RSA y
  **final URL expansion** (Google manda a la URL más relevante de tu sitio). Sube alcance, pero **EXIGE
  negativos a nivel cuenta/campaña y exclusiones de marca** o se va a búsquedas basura. Trátalo como "broad con
  esteroides": enciéndelo en una campaña, vigílalo en el reporte de términos (ver 22), no a ciegas.
- **[CONFIRMADO] Concordancia:** broad + Smart Bidding sigue siendo el default moderno; exact/phrase para
  control. AI Max difumina aún más la frontera → tus **negativos son más importantes que nunca** (ver 21, 22).

## 2. AI Overviews y AI Mode — cómo cambió el SERP (ver 92, 03, 39)
- **[CONFIRMADO] AI Overviews** (respuestas generadas por IA arriba del SERP, 2024→expansión 2025) y **AI Mode**
  (búsqueda conversacional tipo chat, 2025→2026): Google empezó a **mostrar ANUNCIOS dentro de las respuestas
  IA** (en/US primero, expandiéndose). Efecto práctico: **los clics informacionales bajan** (la IA responde
  arriba), pero la **intención comercial/transaccional sigue clickeando** y tus ads pueden aparecer dentro del
  AI Overview. Qué hacer hoy: enfócate en keywords transaccionales (comprar/precio/cerca de mí), refuerza marca,
  y mide CVR (no solo CTR). No entres en pánico: quien quiere comprar, sigue haciendo clic.
- **[RODANDO/verificar]** El alcance exacto de "ads dentro de AI Overviews" por país/idioma cambia mes a mes; en
  LatAm verifica si ya aparece en tu vertical antes de asumir.

## 3. Performance Max maduró (ver 12, 35, 90)
- **[CONFIRMADO] Reporte y controles por canal (channel-level reporting, 2025):** ahora ves y, en parte,
  controlas cómo PMax reparte entre Search/Shopping/YouTube/Display/Demand-Gen/Maps — antes era una caja negra.
- **[CONFIRMADO] Exclusión de marca (brand exclusions) y negativos a nivel campaña en PMax:** úsalos SIEMPRE para
  que PMax **no canibalice tu Search de marca** ni se vaya a términos basura (ver 35).
- **[CONFIRMADO] PMax con objetivos de tienda/local** (store goals) integrado.

## 4. Demand Gen reemplazó a Discovery (ver 41, 46, 40)
- **[CONFIRMADO] Discovery murió; Demand Gen es su reemplazo (migración forzada 2024, maduro 2025-26):** corre en
  **YouTube, Shorts, Gmail y Discover**, con product feeds, audiencias "lookalike-like" (segmentos similares) y
  controles de canal. Es la campaña de Google **más parecida a Meta** (visual, generación de demanda dentro de
  Google) → tu opción para complementar a Meta con destino lead/WhatsApp/llamada en LatAm (ver 46).

## 5. 🔴 Medición — el piso post-cookie (ver 05, 06, 16, 62)
- **[CONFIRMADO] GA4 es la ÚNICA analítica.** Universal Analytics dejó de procesar datos (jul-2023 estándar,
  jul-2024 hasta 360). Si alguien te habla de "vistas de UA", está en el pasado.
- **[CONFIRMADO] Consent Mode v2 (obligatorio para tráfico EEA desde mar-2024):** sin él, pierdes remarketing y
  medición en Europa; con él, Google **modela** las conversiones de quien no consintió. Para Colombia no es
  obligatorio por ley europea, pero el patrón (consentimiento + modeling) es el estándar técnico (ver 06, 29).
- **[CONFIRMADO] Enhanced Conversions (web y for leads):** manda datos first-party hasheados (email/teléfono) con
  la conversión → recupera señal que la cookie perdió. **Es el piso 2026**, casi tan importante como el tag mismo.
- **[CONFIRMADO] Atribución data-driven (DDA) por DEFAULT:** los modelos basados en reglas (last-click,
  posición, lineal, time-decay) se retiraron como opción principal (2023-24); DDA reparte el crédito con ML.
  Last-click sigue disponible como elección, pero ya no es el default.

## 6. 🔴 OCI — el loop Search→WhatsApp/llamada (clave LatAm, ver 53, 28, 96)
- **[CONFIRMADO] Offline Conversion Import (OCI)** sigue siendo el upgrade #1 para un negocio que **captura por
  Search y cierra por WhatsApp/llamada**: capturas el **`gclid`** (click id) en el formulario/chat, y cuando el
  lead califica/compra **subes esa conversión con su valor** a Google → Smart Bidding aprende a traer
  COMPRADORES, no curiosos. Es el equivalente Google del `ctwa_clid` de Meta (facebook_ads 50/53). Hoy puedes
  alimentarlo vía Customer Match/Enhanced Conversions for leads o subida directa/API. **Sin esto, optimizas por
  formularios llenos, no por ventas.**

## 7. IA generativa en la creación (ver 91, 31, 42)
- **[CONFIRMADO] Gemini en Google Ads:** creación conversacional de campañas, **generación de assets** (titulares,
  descripciones, imágenes, y **image-to-video** para Demand Gen/YouTube). Útil para volumen de variantes; **revisa
  TODO** (Google autogenera assets dentro de RSA/PMax salvo que lo desactives — pueden cambiar claims, riesgo
  policy en salud/finanzas, ver 44/08). Declara visuales generados por IA donde aplique.

## 8. Cuenta, políticas y verificación (ver 04, 08, 93)
- **[CONFIRMADO] Verificación de anunciante obligatoria** (identidad/negocio): sin completarla, Google limita o
  pausa la entrega. Hazla apenas creas la cuenta.
- **[CONFIRMADO] Enforcement de "circumventing systems" y "misrepresentation"** sigue siendo la causa #1 de
  suspensión evitable (cloaking, landing inestable, claims falsos). Salud/finanzas/pérdida de peso = alto riesgo
  (ver 44, 93). Cuenta nueva = caliéntala (no $0→$5M en un día).
- **[CONFIRMADO] Reporte de términos de búsqueda** muestra más términos que en 2020 (cambio de privacidad de
  2020 se relajó parcialmente), pero sigue ocultando los de bajo volumen → los **negativos por n-gram** (ver 68)
  siguen siendo necesarios.

## 9. Tipos/herramientas que conviene saber (ver 11, 50, 89)
- **[CONFIRMADO] Local Services Ads (LSA)** — pago por LEAD + insignia Google Guaranteed/Screened, arriba del
  SERP; **verifica disponibilidad en Colombia/tu país y vertical** antes de prometerlo (ver 50, 81).
- **[CONFIRMADO] App campaigns (AC)** automatizadas (tCPA/tROAS de instalación/evento) — antes UAC (ver 89).
- **[RODANDO/verificar]** Google sigue empujando "todo a PMax/AI": cada trimestre aparece un toggle nuevo de
  automatización en Search. La regla no cambia: **enciéndelo en una campaña, mídelo, no en toda la cuenta a ciegas.**

## Cómo usar este módulo
Es la **capa de actualidad** sobre los módulos de fondo. Si un módulo viejo y este snapshot chocan en un dato
fechado (un tipo de campaña, una opción de atribución, un feature de IA), **manda este**. Re-verifica con
búsqueda fresca cada trimestre — y cuando un cambio de Google cueste plata o confunda, agrega su fila aquí con
fecha y fuente. Hermana de pauta: lo de **Meta** vive en `facebook_ads_lushows` (su propio `actualizacion-2026-06`).
