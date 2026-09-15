# 66 — UTMs y analytics externo: ver tu tráfico fuera de Meta

Los UTM son etiquetas que agregas a la URL de destino de tus ads para que TU analytics (GA4, tu tienda, tu CRM) sepa exactamente de qué campaña/ad vino cada visita y cada venta — con una mirada independiente de la de Meta. Sin UTMs, todo tu tráfico pago aparece como "facebook / referral" o "directo" y no puedes auditar nada. Configúralo el día 1; lee este módulo al montar tu primera campaña o al heredar una cuenta desordenada. Actualizado jun-2026.

Por qué importa más en 2026: con Meta habiendo quitado las ventanas view-through del API (12-ene-2026) y empujando atribución incremental (reporta menos), tener una **segunda cámara independiente** (GA4/tu tienda) dejó de ser opcional. Cuando Meta y tu analytics no concuerdan, el backend desempata (ver 64).

## La convención UTM disciplinada

Cinco parámetros, siempre los mismos, siempre en minúsculas:
- `utm_source=facebook` (de dónde; usa "facebook" para todo Meta y deja que medium/campaign distingan)
- `utm_medium=paid` (tipo de tráfico)
- `utm_campaign={{campaign.name}}` (qué campaña)
- `utm_content={{ad.name}}` (qué ad exacto)
- opcional: `utm_term={{adset.name}}` (qué ad set/audiencia)

Los valores entre `{{ }}` son **parámetros dinámicos de Meta**: la plataforma los reemplaza sola por el nombre real de la campaña/ad set/ad al servir el anuncio. Escribes la plantilla UNA vez y sirve para todos los ads. (Si usas otra plataforma, su sintaxis cambia: TikTok usa `__CAMPAIGN_NAME__`, Google arma los suyos — ver tiktok_ads_lushows / google_ads_lushows; mantén el MISMO esquema de nombres para que tu GA4 sume parejo.)

### Receta exacta (pegar y listo)
En el editor del anuncio → sección **Seguimiento** → campo **Parámetros de URL** (sin `?` inicial):

```
utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}
```

Hazlo parte de tu checklist de publicación. Si duplicas ads, los parámetros viajan con el duplicado. Valida una vez: haz clic en tu propio ad y mira que la URL final lleve los UTMs poblados (no `{{campaign.name}}` literal — eso significa que pegaste mal el campo).

## Naming con sistema (los UTMs valen lo que valen tus nombres)

Como los parámetros dinámicos insertan los NOMBRES, nombra con estructura parseable:
- **Campaña**: `[objetivo]-[audiencia]-[fecha]` → `ventas-broad-2026-06` / `ctwa-retarget-2026-06`
- **Ad set**: `[audiencia/tipo]` → `broad` / `lookalike-compradores` / `retarget-7d`
- **Ad**: `[ángulo]-[formato]-[hook]` → `energia-video-pregunta` / `testimonio-imagen-antes-despues`
- Sin espacios ni tildes ni emojis (rompen URLs y filtros); separador único (`-` o `_`, elige uno y no lo cambies).

Beneficio doble: lees GA4 y el creative analytics (ver 68) sin abrir Meta, y filtras en Ads Manager por subcadenas (ver 63). El naming es la columna vertebral de TODO el bloque de medición: sin él, el desglose por ángulo del 68 es imposible y los UTMs heredan basura.

## GA4 básico para ads

(GA4 = Google Analytics 4, el analytics gratuito estándar; si usas Shopify/Woo, sus reportes nativos de fuentes sirven parecido.)
- **Informes → Adquisición → Adquisición de tráfico**: filtra por `facebook / paid` y agrega dimensión secundaria "Campaña de la sesión". Ves sesiones, engagement, conversiones y venta por campaña — con la atribución de GA4.
- Para qué sirve: comparar CALIDAD de tráfico entre campañas (¿cuál trae gente que navega y compra vs rebotes de 5 segundos?), detectar landings rotas, y auditar a Meta con un tercero.
- Qué esperar: GA4 (last-click, sin view-through) reportará **20–50% menos** conversiones de Meta que el propio Ads Manager. SIEMPRE. Las dos miden con reglas distintas; ninguna es "la verdad" — la verdad es el banco/backend (ver 64).
- Tip de calidad: en GA4 mira **engagement rate** y **conversiones por sesión** por campaña — una campaña con muchas sesiones y engagement bajo trae curiosos (problema de targeting/creativo); una con pocas sesiones pero alto engagement trae intención (escálala).

### Explicárselo a un cliente sin pánico
"Meta cuenta a quien clicó un anuncio en los últimos 7 días, aunque después haya entrado por Google. GA4 solo le da el punto al último clic. Por eso Meta dice 40 ventas y GA4 dice 24: son dos cámaras filmando el mismo partido desde ángulos distintos. El marcador oficial es el backend: vendimos 31, y la tabla semanal (ver 64) reconcilia los tres." Esta frase, dicha ANTES de que el cliente note la diferencia, te ahorra la conversación incómoda (ver 67).

## Para WhatsApp-first: tu "analytics externo" es el CRM de chat

Si el clic termina en WhatsApp, no hay GA4 que valga: el UTM no entra al chat. Equivalentes:
- El **referral de CTWA** llega con datos del ad que originó la conversación, incluido el **`ctwa_clid`** (visible vía API/CRM): guárdalo como "fuente" del contacto — es tu UTM nativo de WhatsApp y la llave para atribuir la venta por CAPI (ver 62).
- Alternativa simple: un **mensaje prellenado distinto por campaña** ("Hola, vi el video del combo energía") que actúa como UTM humano — defínelo por anuncio en el CTWA.
- Etiqueta cada chat con campaña/ángulo y su desenlace (pedido/no) en tu CRM (ver 53). Esa tabla ES tu adquisición externa: campaña → conversaciones → pedidos → venta. Para GASTROWHATS/AVISPA'O, esto vive en las etiquetas del bot.

### Plantilla de tabla de adquisición por chat
| Fecha | Campaña (referral/prellenado) | Ángulo | Conversaciones | Calificados | Pedidos | Venta COP |
|---|---|---|---|---|---|---|
| 8–14 jun | ctwa-broad-energia | dolor-cotidiano | 120 | 48 | 19 | 2.280.000 |
| 8–14 jun | ctwa-broad-ciencia | dato-ciencia | 90 | 22 | 6 | 720.000 |

Esa tabla te da CVR de chat por ángulo (pedidos ÷ conversaciones) — el equivalente WhatsApp del creative analytics (ver 68): aquí "energia" cierra 16% vs "ciencia" 7% → matas ciencia.

## Discrepancias esperables — chuleta

| Comparación | Diferencia normal | Alarma si… |
|---|---|---|
| Meta vs GA4 (conversiones) | Meta 20–50% más | Meta 3× GA4 sostenido → revisa deduplicación (ver 62) y peso de view-through residual |
| Clics (Meta) vs sesiones (GA4) | 10–30% menos sesiones (cierres antes de cargar, in-app browser) | >50% perdido → landing lenta o redirecciones que comen UTMs |
| Meta vs backend (ventas) | Meta 1.2–1.8× | ver 64, triangulación |
| CRM (chats) vs Ads Manager (conversaciones) | ±10% | 2× → referral/etiquetado roto (ver 53) |

## Errores comunes — blacklist
- Pautar sin UTMs y "después vemos" — el histórico perdido no se recupera.
- Escribir los parámetros a mano por ad (typos: `facebok`, `Paid` vs `paid` crean fuentes duplicadas en GA4).
- Nombres de campaña tipo "Campaña 3 FINAL (2)" — los UTMs heredan la basura.
- Cambiar la convención de naming a mitad de año: parte la serie histórica en dos.
- Entrar en pánico (o dejar que el cliente entre) por la discrepancia Meta vs GA4: es estructural, se explica, se reconcilia con el backend.
- En CTWA, no guardar la fuente del chat (`ctwa_clid` o prellenado): pierdes el único hilo entre el ad y la venta (ver 53, 62).
- Mezclar `utm_source` de varias plataformas con esquemas distintos: GA4 no suma parejo y comparas peras con manzanas (ver google_ads_lushows / tiktok_ads_lushows).
