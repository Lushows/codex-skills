# 66 — UTMs y analytics externo

Lee este módulo cuando no sepas qué ventas vinieron de TikTok de verdad, cuando los números de Ads Manager y los de tu Google Analytics no cuadren y creas que algo está roto, o antes de montar campañas para que cada clic deje rastro. Los **UTMs** son las etiquetas que pegas a tus enlaces para que tu analítica sepa de dónde llegó cada visita. Sin ellos, tu backend (ver 64) está ciego y no puedes triangular nada. Con ellos, tienes una segunda fuente de verdad independiente de lo que diga TikTok. Y sí: los números **nunca** van a coincidir exactamente — eso es normal y aquí aprendes a leerlo sin volverte loco.

## Qué son los UTMs y la convención que sirve

**UTM** = unos parámetros que se agregan al final de la URL (`?utm_source=...`) y que herramientas como GA4 leen para clasificar el tráfico. Son cinco; usa siempre los cuatro primeros como mínimo:

| Parámetro | Qué guarda | Ejemplo |
|---|---|---|
| `utm_source` | La plataforma | `tiktok` |
| `utm_medium` | El tipo de tráfico | `paid_social` o `cpc` |
| `utm_campaign` | Nombre de tu campaña | `gastro_oferta_jun` |
| `utm_content` | El creativo específico | `hook3_dolor_costos` |
| `utm_term` | Opcional (público/ángulo) | `broad` |

Regla de oro de la convención: **escoge un formato y NO lo cambies nunca**. Todo en minúsculas, sin tildes ni espacios (usa `_`), siempre los mismos valores. `tiktok` hoy y `TikTok` mañana son dos fuentes distintas para GA4 y te parten el reporte. Documenta tu convención en una hoja y que todo el equipo la use (ver 67). Si pautas en varias plataformas, mantén `utm_source` consistente entre todas (`tiktok`, `meta`, `google`) para que el reporte cruzado cuadre con `facebook_ads_lushows` y `google_ads_lushows`.

El `utm_content` con el nombre del creativo es **oro**: te deja cruzar qué video trajo qué venta en tu backend, no solo en TikTok (ver 68). Es el puente entre "thumbstop alto" (lo que ves en el panel) y "ventas reales" (lo que ves en tu tienda).

### URL de ejemplo bien etiquetada

```
https://gastrolatam.com/calculadora?utm_source=tiktok&utm_medium=paid_social&utm_campaign=gastro_oferta_jun&utm_content=__CID_NAME__&utm_term=broad
```

TikTok tiene **macros dinámicas** que rellenan los UTMs solos con el nombre real de la campaña/ad. Las más útiles: `__CAMPAIGN_NAME__`, `__AID_NAME__` (ad group), `__CID_NAME__` (anuncio/creativo), `__PLACEMENT__`. Úsalas en el campo "URL de tracking" del ad para no etiquetar a mano y no equivocarte. Si nombras tus creativos con su ángulo (ej. `hook3_dolor_costos`), la macro `__CID_NAME__` llena `utm_content` solo con ese nombre y el cruce en el backend queda automático.

## GA4 y la segunda fuente de verdad

**GA4** (Google Analytics 4) es la analítica gratis de Google. Lee tus UTMs y te dice, independiente de TikTok, cuántas sesiones y conversiones vinieron de `source = tiktok`. Por qué importa: es una fuente **no interesada** — a GA4 no le conviene inflar el aporte de TikTok, así que su número suele ser más conservador y honesto que el del panel (ver 64).

Configúralo así:

1. Pega UTMs (con macros) en TODOS los enlaces de tus ads.
2. En GA4 → Adquisición → Adquisición de tráfico → revisa por `Session source / medium` = `tiktok / paid_social`.
3. Marca tus conversiones clave (compra, lead) como "key events" en GA4 para verlas por fuente.
4. Cruza: GA4 (tiktok) vs backend (UTM) vs Ads Manager. La verdad vive entre los tres.

Detalle 2026: GA4 usa **Consent Mode v2** y modelado de datos para usuarios que rechazan cookies. Eso significa que parte del número de GA4 también es **estimado** (modelado), no medido al 100%. No es mentira, pero no es exacto — otra razón para triangular y no idolatrar a ninguna fuente. (Consent Mode y GA4 a fondo viven en `google_ads_lushows`.)

## Por qué los números NUNCA cuadran (y cómo leerlo)

Esto frustra a todo media buyer novato. **Ads Manager dirá más conversiones que GA4.** Casi siempre. Y está bien. Razones:

| Causa de la discrepancia | Efecto |
|---|---|
| **Modelo de atribución distinto** | TikTok usa 7d-click/1d-view (ver 64); GA4 usa data-driven/último clic. Cuentan diferente |
| **View-through** | TikTok cuenta a quien solo VIO el ad y no hizo clic; GA4 no |
| **Bloqueadores / consentimiento** | GA4 pierde usuarios que rechazan cookies; el píxel+Events API recupera algunos (ver 62) |
| **Ventana de tiempo** | Distintas ventanas = distintos totales |
| **iOS / SKAN** | Datos estimados y con retraso del lado TikTok |
| **Sesión vs persona** | GA4 cuenta sesiones; TikTok cuenta usuarios/eventos. Unidades distintas |

Cómo leerlo sin enloquecer: **no busques que coincidan, busca que se muevan juntos.** Calcula tu factor de correlación una vez:

```
Factor GA4/TikTok = conversiones GA4 (tiktok) ÷ conversiones panel TikTok
```

Si TikTok dice 100 conversiones y GA4 dice 65, tu factor es ~0,65. Lo importante es que cuando TikTok suba a 150, GA4 suba a ~98 (mismo factor). **Si TikTok sube y GA4 NO se mueve, ahí sí hay un problema real:** o atribución fantasma de TikTok o medición rota en GA4 (ver 62). Este factor GA4 suele parecerse a tu factor de backend (ver 64) — si difieren mucho, una de las dos mediciones está mal.

| Discrepancia Ads Manager vs GA4 | Lectura |
|---|---|
| 20–40% | Normal, no toques nada |
| 40–55% | Vigila; revisa UTMs y consentimiento |
| > 55% sostenido | Investiga: píxel, UTMs mal puestos o sobre-atribución (ver 62, 64) |
| Dejan de moverse juntos | Problema real, audita ya |

## Tabla de triangulación de las tres fuentes

| Fuente | Mide | Sesgo | Úsala para |
|---|---|---|---|
| TikTok Ads Manager | Conversiones atribuidas | Infla (view-through, 7d) | Comparar creativos (ver 68) |
| GA4 (UTMs) | Sesiones/eventos por fuente | Conservador, modela consentimiento | Segunda opinión independiente |
| Backend / tienda | Órdenes reales con UTM | Subcuenta (pierde sin-UTM) | Calcular factor real y MER (ver 64) |

La regla final: ninguna fuente es la verdad completa. La verdad es el **cruce de las tres + el banco** (ver 64). El UTM es lo que hace posible el cruce; sin él, vuelas a ciegas.

## Errores comunes — blacklist

- **No poner UTMs.** Tu backend y GA4 quedan ciegos; no puedes triangular nada (ver 64).
- **Cambiar la convención (mayúsculas un día, tildes otro).** Partes el reporte en fuentes basura. Fija el formato y respétalo.
- **Esperar que Ads Manager y GA4 coincidan.** Nunca lo harán; usan atribución distinta. Busca correlación, no igualdad.
- **Asustarte por una diferencia del 30%.** Es normal. Preocúpate si supera el 50% sostenido o si dejan de moverse juntos.
- **No etiquetar el creativo en `utm_content`.** Pierdes el cruce de qué video vendió en tu backend (ver 68).
- **Etiquetar a mano cada ad.** Te equivocas. Usa las macros dinámicas de TikTok (`__CID_NAME__`).
- **Creerle solo a GA4 o solo a TikTok.** Ninguno es la verdad completa; la verdad es el cruce + el banco (ver 64).
- **Usar `utm_source` distinto entre plataformas.** Rompe el reporte cruzado con Meta/Google. Mantén la convención.
