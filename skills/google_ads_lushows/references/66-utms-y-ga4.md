# 66 — UTMs, gclid y GA4

Lee este módulo cuando tu tráfico de Google Ads aparece como "(not set)" o "directo" en GA4, cuando no sabes si poner UTMs a mano o dejar que Google los ponga, cuando tus reportes de GA4 no cuadran con los de Ads y crees que algo está roto, o cuando vas a armar un enlace de campaña y no sabes qué etiquetas usar. Este es el plomería del tracking: aburrido, pero si está mal, **todos tus reportes mienten** y diagnosticas sobre humo (ver 61, 62).

Dos conceptos base:
- **gclid** ("Google Click Identifier"): un código único que Google le pega automáticamente a cada clic de tus anuncios (ej. `?gclid=Cj0KCQ...`). Permite a Ads y GA4 unir el clic con la conversión sin que tú hagas nada. En 2026 convive con **gbraid/wbraid**, variantes que Google usa para iOS/apps cuando la privacidad impide el gclid clásico — no tienes que tocarlas, solo saber que existen y que también las pone el auto-tagging.
- **UTM**: parámetros que **tú** agregas a mano a una URL (`utm_source`, `utm_medium`, `utm_campaign`...) para decirle a GA4 de dónde vino el tráfico.

## Auto-tagging (gclid): por qué SIEMPRE

**Auto-tagging** = Google le agrega el `gclid` automáticamente a cada URL de tus anuncios. Es la forma correcta de que Google Ads y GA4 se entiendan, y la base de Enhanced Conversions y conversiones modeladas (ver 62). Déjalo **activado siempre** (Admin → Account settings → Auto-tagging: ON; viene activo por defecto, **no lo apagues**).

Por qué gclid le gana a UTMs manuales en Google Ads:

| | gclid (auto-tagging) | UTMs manuales |
|---|---|---|
| Quién lo pone | Google, automático | Tú, a mano |
| Detalle que captura | Campaña, grupo, keyword, dispositivo, search term, mucho más | Solo lo que escribiste |
| Errores | Casi cero | Altísimo (typos, mayúsculas, olvidos) |
| Conexión Ads↔GA4 | Perfecta | Parcial / se rompe |
| Enhanced Conversions / modeladas | Funcionan | No las alimenta bien |

Regla dura: **en Google Ads no necesitas UTMs manuales. El gclid ya hace todo.** Ponerle UTMs a mano a tus anuncios de Google encima del auto-tagging suele **romper** el tracking (el UTM mal puesto pisa la info del gclid y tu tráfico cae en "(not set)"). Si por reporting interno necesitas etiquetas legibles, usa **tracking templates** con value-track parameters (`{campaignid}`, `{keyword}`, `{device}`...) a nivel cuenta/campaña, **no** UTMs escritos a dedo. El value-track lo rellena Google sin errores.

## UTMs manuales: cuándo SÍ

Los UTMs son para tráfico que **NO es** anuncios de Google Ads y que GA4 no detecta solo:

| Fuente | ¿UTM? | Ejemplo de etiquetas |
|---|---|---|
| Google Ads | **No** (usa gclid/auto-tagging) | — |
| Link en tu bio de Instagram | **Sí** | `utm_source=instagram&utm_medium=bio&utm_campaign=lanzamiento` |
| Email / newsletter | **Sí** | `utm_source=email&utm_medium=newsletter&utm_campaign=junio` |
| Mensaje de WhatsApp con link | **Sí** | `utm_source=whatsapp&utm_medium=mensaje&utm_campaign=promo` |
| Publicación orgánica / influencer | **Sí** | `utm_source=influencer&utm_medium=post&utm_campaign=colab_chef` |
| QR en empaque / volante físico | **Sí** | `utm_source=empaque&utm_medium=qr&utm_campaign=offline` |
| Meta / TikTok Ads | Lo maneja la plataforma | ver `facebook_ads_lushows`, `tiktok_ads_lushows` |

Reglas para no romper tus UTMs manuales:
- **Todo en minúsculas, siempre.** GA4 distingue `Instagram` de `instagram`: te parte la fuente en dos filas y ensucia cada reporte.
- **Sé consistente:** decide `whatsapp` (no `wpp`, `wa`, `WhatsApp`) y úsalo igual siempre. Escribe un mini-diccionario de tus fuentes/medios y respétalo.
- **`utm_medium` con valores estándar** para que GA4 los agrupe bien: `cpc`, `email`, `social`, `referral`, `qr`. Inventar mediums raros rompe los canales por defecto de GA4.
- **Usa el constructor oficial** (Campaign URL Builder de Google) para no escribir el `?` y `&` mal.
- **`utm_source` y `utm_medium` son obligatorios**; los otros (`campaign`, `content`, `term`) opcionales pero útiles para distinguir variantes.

Convención recomendada (cópiala): `utm_source` = la plataforma (`instagram`, `email`, `whatsapp`); `utm_medium` = el tipo de canal (`social`, `email`, `qr`); `utm_campaign` = la iniciativa (`lanzamiento_calculadora`, `promo_junio`).

## Discrepancias Ads vs GA4: cómo leerlas sin volverte loco

Ya lo vimos en medición (ver 62), pero aquí desde el ángulo de fuentes: **Ads y GA4 te van a dar números distintos, y está bien.** Resumen para que no entres en pánico:

| Por qué difieren | Detalle |
|---|---|
| **Atribución distinta** | Ads usa data-driven a su modo; GA4 al suyo (ver 16) |
| **Día asignado** | Ads pone la conversión el día del **clic**; GA4 el día de la **compra** |
| **Qué cuenta cada uno** | Ads solo cuenta tráfico de Ads; GA4 cuenta TODAS las fuentes (orgánico, directo, social) |
| **Sesiones vs clics** | Un clic puede generar varias sesiones, o ninguna si el usuario rebota antes de cargar |
| **Modelado distinto** | Ambos modelan parte (Consent Mode), con métodos diferentes |

**Cuánto es normal:** 5–20% de diferencia entre Ads y GA4. Más de 2x = problema real (auto-tagging apagado, UTMs pisando el gclid, conversión mal configurada, o falta Consent Mode v2 — ver 62).

**Cómo leerlas sin enloquecer — quién manda para qué:**
- Usa **Ads** para optimizar pujas y campañas (es su universo, lo conoce mejor; el Smart Bidding vive de su propia señal, ver 13).
- Usa **GA4** para comparar canales entre sí (Google vs Meta vs orgánico) y ver el viaje completo del usuario (ver Customer Journey).
- Para la verdad financiera, **ninguna de las dos**: backend + banco + MER (ver 64).
- No persigas el cuadre perfecto. Persigue **tendencias consistentes**: si ambas suben, subes; si ambas caen, hay problema.

## El síntoma clásico de tracking roto

Tu tráfico de Google Ads aparece en GA4 como **"(not set)"**, **"direct"** o **"google / organic"** en vez de `google / cpc`. Checklist de causas, en orden:
1. Auto-tagging apagado → enciéndelo (Admin → Account settings).
2. UTMs manuales pisando los anuncios de Google → quítalos; deja solo gclid o tracking templates.
3. El gclid se pierde en un redirect (la landing redirige y bota el parámetro) → arregla el redirect para que conserve la query string.
4. GA4 mal vinculado a Ads → revisa el **link Google Ads ↔ GA4** (Admin → Product links → Google Ads).

Verifícalo en GA4 → Reports → Traffic acquisition, filtra por `google / cpc`: si tu inversión de Ads no aparece ahí, está roto y lo estabas reportando mal.

## Errores comunes — blacklist

1. **Apagar auto-tagging.** Sin gclid, Ads y GA4 dejan de entenderse, pierdes el 90% del detalle y rompes Enhanced Conversions. Déjalo ON siempre.
2. **Ponerle UTMs manuales a los anuncios de Google.** Encima del gclid suelen pisar la info y romper el tracking. En Google Ads: gclid sí, UTMs a dedo no; si necesitas etiquetas, tracking templates.
3. **UTMs con mayúsculas inconsistentes.** `Instagram` ≠ `instagram` en GA4: te parte la fuente. Todo minúscula.
4. **Inventar `utm_source`/`utm_medium` distintos cada vez** (`wpp`, `wa`, `whatsapp`). Define un estándar/diccionario y respétalo.
5. **Entrar en pánico porque Ads y GA4 no cuadran.** 5–20% es normal por atribución y ventanas. Solo investiga si es 2x+.
6. **Buscar la verdad financiera en GA4.** GA4 es analítica de comportamiento, no contabilidad. La plata real está en backend/banco (ver 64).
7. **No revisar que el tráfico de Ads salga como `google / cpc` en GA4.** Si sale como "(not set)" o "direct", tienes el tracking roto y no lo sabías.
8. **Perder el gclid en un redirect de la landing.** Si la página redirige y bota la query string, el clic llega "directo". Conserva los parámetros en cualquier redirect.
