# 16 — Atribución 2026

Lee este módulo cuando el panel de TikTok diga que generaste 40 ventas pero en tu banco solo veas 22, cuando no sepas qué ventanas de atribución elegir, o cuando quieras saber "¿en serio TikTok me trajo eso?". La atribución es **cómo TikTok decide qué ventas se cuelga como suyas** — y siempre, SIEMPRE, se cuelga de más. Entender esto te salva de escalar una campaña que en realidad no jala y de matar una que sí. La atribución no es contabilidad: es el cuento que cada plataforma se cuenta a sí misma sobre quién se merece el crédito.

## Las ventanas de atribución

Una **ventana de atribución** es el plazo dentro del cual TikTok se adjudica una venta después de que alguien vio o tocó tu anuncio.

| Ventana | Qué cuenta | Default 2026 |
|---|---|---|
| **7-day click (7d-click)** | Compró dentro de 7 días después de **hacer clic** | Sí (estándar) |
| **1-day view (1d-view)** | Compró dentro de 1 día después de **solo ver** el anuncio (sin clic) | Sí (configurable) |
| Click más largo / view más largo | Configurables según ciclo de compra | Según negocio |

- **Click** = la persona tocó el anuncio. Atribución más fuerte (mostró intención activa).
- **View-through (view)** = la persona solo VIO el video y no tocó nada, pero compró después. Atribución **débil y discutible** — ¿de verdad ese video la hizo comprar, o ya iba a comprar y lo vio de refilón?

El default 7d-click/1d-view es razonable, pero el **1d-view infla** tus números: TikTok se cuelga compras de gente que apenas vio el video de pasada. Para juzgar el impacto REAL, mira prioritariamente el **7d-click** y trata el view-through como un extra optimista. Si quieres ser duro, configura una vista de solo-click y compárala con la vista completa: la diferencia es cuánto crédito se está colgando TikTok del view-through.

## SKAN, iOS y los huecos en los datos

En iPhone (iOS), Apple limita el rastreo desde ATT. TikTok usa **SKAN** (*SKAdNetwork*, el sistema de medición privado de Apple): manda datos **agregados, con retraso y sin detalle por usuario**. Consecuencias prácticas:

- Las conversiones de iOS llegan **tarde** (hasta 24–72h después; no las veas en tiempo real) y **incompletas**.
- Parte de tus ventas reales de iPhone **no aparecen** en el panel → TikTok puede estar **sub-reportando** en iOS al mismo tiempo que **sobre-reporta** por view-through en general. El neto es impredecible por día.
- Por eso el número del panel es una **estimación**, no la verdad contable. En Colombia el peso de iOS es menor que en EE.UU., pero en públicos de poder adquisitivo alto (donde más vendes high-ticket) iPhone pesa más y el hueco crece.

Instalar el **Events API** (server-side, ver 57) recupera parte de la señal que el navegador pierde (bloqueadores, cookies, ITP) y mejora la calidad de la atribución Y de la optimización. En 2026 no es opcional: sin Events API estás optimizando y midiendo con un ojo tapado.

## La regla que te salva: cruza con tu backend / MER

Nunca tomes decisiones de plata solo con el ROAS del panel de TikTok. La verdad está en tu **backend** (tu Shopify/tu banco/tus pedidos reales) y en el **MER**.

**MER** = *Marketing Efficiency Ratio* = Ingresos TOTALES del negocio ÷ Gasto TOTAL en publicidad. Es el ROAS del negocio entero, no de una plataforma. No se puede inflar porque sale de tu facturación real, no del cuento de ningún panel.

| Métrica | De dónde sale | Confiabilidad |
|---|---|---|
| ROAS de TikTok (panel) | TikTok se lo adjudica | Optimista, infla |
| ROAS real por plataforma | Backend + parámetros UTM | Mejor |
| **MER** | Facturación total ÷ gasto total | **La verdad** |

Cómo usarlo en la práctica (el test de incrementalidad del pobre): si subes el gasto de TikTok $1.000.000 y tu **facturación total** sube $3.500.000, TikTok funciona — sin importar qué diga el panel. Si el panel grita ROAS 4 pero tu MER no se movió cuando prendiste/subiste TikTok, TikTok se está **robando crédito** de ventas que igual iban a pasar (ver 64). Mira el MER **semana a semana**, no día a día (varianza alta, ver 13).

Plantilla de seguimiento semanal (en una hoja simple):

| Semana | Gasto TikTok | Gasto total ads | Facturación total | MER | ROAS panel TikTok |
|---|---|---|---|---|---|
| 1 | $700k | $1.5M | $4.5M | 3.0 | 4.2 |
| 2 (subí TikTok) | $1.2M | $2.0M | $6.0M | 3.0 | 4.0 |

Si el MER se mantiene al subir TikTok, el gasto extra es incremental sano. Si el MER cae, estás comprando ventas que ya tenías.

## La superposición con Meta y Google

TikTok, Meta y Google **se cuelgan la misma venta** cada uno. Si sumas los ROAS de los tres paneles, "vendiste" más de lo que facturaste — imposible. El patrón típico en 2026: **TikTok descubre** (crea el deseo, la persona ve el producto por primera vez), luego esa persona busca tu marca en Google o la vuelve a ver en Meta, y la plataforma de abajo del funnel **se lleva el clic final** (ver `facebook_ads_lushows`, `google_ads_lushows`). Por eso TikTok suele mostrar ROAS de panel más bajo aunque sea el que prendió la chispa. El MER es el único árbitro que no miente porque mira la caja, no los paneles. Si apagas TikTok y tu búsqueda de marca en Google se desploma, ahí tienes la prueba de que TikTok sí generaba demanda (ver 97).

## Errores comunes — blacklist

1. **Creerle al ROAS del panel al pie de la letra.** TikTok infla; cruza con backend y MER siempre.
2. **Sumar los ROAS de TikTok + Meta + Google.** Cada uno se cuelga la misma venta; el total es ficción.
3. **Confiar en el 1d-view como si fuera venta causada.** El view-through es atribución débil; prioriza 7d-click.
4. **Esperar ver las ventas de iOS en tiempo real.** SKAN llega tarde e incompleta; no juzgues iPhone al instante.
5. **No instalar Events API.** Pierdes señal del navegador y empeoras la medición Y la optimización (ver 57).
6. **Tomar decisiones de escalar con datos de 1 día.** Varianza alta; mira ventanas de 7 días y MER semanal (ver 13).
7. **Matar TikTok porque "su ROAS de panel es bajo" cuando el MER subió al prenderlo.** TikTok descubre; otra plataforma se llevó el clic final. Mide el sistema, no el silo (ver 97).
8. **No tener una hoja de MER semanal.** Sin esa hoja decides con el cuento de los paneles; con ella decides con la caja.
9. **Cambiar ventanas de atribución a media campaña para "ver más ventas".** Cambiar la ventana no crea ventas, solo cambia el cuento; mantén una ventana fija y juzga el MER.
