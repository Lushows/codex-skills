# 02 — El ecosistema Google Ads en 2026

Google Ads ya no es solo "anuncios de texto en el buscador". Es una red de inventarios distintos (Search, YouTube, Gmail, Maps, Discover, millones de sitios y apps) gobernada cada vez más por IA (Gemini genera assets, modela conversiones y expande keywords). Lee este módulo cuando no sepas qué tipos de campaña existen, cuándo manda la máquina vs el humano, o para ubicar dónde encaja lo que quieres hacer antes de elegir tipo de campaña (ver 11).

## Los inventarios / tipos de campaña

| Tipo | Dónde aparece | Intención | Para qué sirve | Módulo |
|---|---|---|---|---|
| **Search** | resultados del buscador | ALTA (busca activamente) | capturar demanda, leads, ventas | 11, 30 |
| **Performance Max (PMax)** | TODO (Search, YouTube, Display, Gmail, Maps, Discover, Shopping) | mixta | e-commerce/leads cuando ya hay datos y assets | 12, 35 |
| **Shopping** | fichas con foto+precio en Search | alta comercial | e-commerce con Merchant Center | 34, 55 |
| **Demand Gen** | YouTube, Shorts, Gmail, Discover | baja/media (descubrimiento) | GENERAR demanda visual (reemplazó a Discovery en 2024) | 41, 46 |
| **YouTube/Video** | YouTube | baja-media | awareness, consideración | 40, 42 |
| **Display** | 2M+ sitios y apps | baja | remarketing barato, alcance | 43, 24 |
| **Local Services (LSA)** | arriba de Search, "Garantizado por Google" | alta local | servicios locales (pago por lead) | 50, 81 |
| **Apps** | todo el inventario | instalación | promocionar apps | 89 |

Para captura pura de intención en LatAm con presupuesto chico: **Search-first** (ver 07, 11). PMax y Demand Gen comen presupuesto y necesitan datos + buenos assets para no desperdiciar. Si vendes productos físicos con catálogo → Shopping/PMax retail (ver 34, 35); si vendes servicios locales → Search + LSA (ver 50).

## Qué decide la máquina vs el humano (era IA/Gemini)

La tendencia 2025–2026 es clara: Google automatiza la **ejecución** y deja al humano la **estrategia y los insumos**. Tu trabajo de élite es darle buenos insumos y buenos límites, no micro-gestionar pujas. La diferencia entre una cuenta mediocre y una de élite ya no es "quién ajusta mejor el CPC manual" — es **quién le da mejores señales, mejores negativas y mejor medición a la máquina.**

| La MÁQUINA decide | El HUMANO controla |
|---|---|
| Puja por subasta (Smart Bidding, ver 13) | El objetivo (tCPA/tROAS) y el presupuesto |
| Qué combinación de titulares/descripciones mostrar (RSA) | Los titulares, descripciones y assets que entran (ver 30, 32) |
| A quién y dónde mostrar en PMax | Las señales de audiencia, geos, negativas, exclusiones de marca |
| Qué keyword broad activar | La oferta, la landing, las **negativas** (palanca #1, ver 22) |
| Modelado de conversiones no observadas | La calidad de la medición (GA4 + Enhanced Conversions, ver 05, 06) |
| Generación de assets (Gemini) | Aprobar/editar lo que Gemini propone — no aceptes a ciegas |

Default moderno 2026: **Broad match + Smart Bidding + buenos negativos** (ver 21, 13, 22). El `manual CPC` ya casi no se usa. Pero "automático" no es "mágico": si tu medición es basura o tus negativas están vacías, la IA optimiza hacia clics inútiles. La regla del especialista: **la máquina amplifica lo que le das.** Buenas señales → escala; señales basura → desperdicio a escala.

## La era IA: AI Max, AI Overviews y reporte por canal

- **AI Max for Search** (2025+): trae la potencia de PMax/IA a las campañas de Search — **expansión de keywords broad**, automatización de **assets y URLs finales** (Google elige la mejor landing de tu sitio para cada búsqueda) y creatividad asistida, con más control y transparencia que PMax puro. **Exige negativos sólidos** porque expande consultas agresivamente. Útil para exprimir Search sin perder visibilidad de search terms (ver 90).
- **PMax con controles** (2025+): ya reporta **a nivel de canal** (ves qué pasó en Search vs YouTube vs Display), permite **exclusiones de marca**, **exclusiones de URL** y **negativas a nivel de campaña** — usa esos controles, antes era una caja negra que canibalizaba tráfico de marca (ver 12).
- **AI Overviews / AI Mode** (2025–26): Google responde con IA arriba de los resultados; hay anuncios **dentro** de esas respuestas generativas. Efecto: los clics **informacionales** bajan, pero la **intención comercial sigue clickeando** (quien quiere comprar, compra). No entres en pánico: refuerza intención comercial alta (ver 92).
- **Demand Gen** es el reemplazo de Discovery (desde 2024) y es lo más parecido a "pautar como en Meta" dentro de Google: creativos visuales en superficies de descubrimiento. Genera demanda, no la captura (ver 41).
- **GA4 es la única analítica** (Universal Analytics murió en 2023). Toda medición pasa por GA4 + Google tag (ver 05).
- **Atribución data-driven por default:** el modelo last-click fue retirado; Google reparte el crédito entre clics según su aporte real (ver 16).

## Cómo orquestar canales (no prendas todo a la vez)

| Etapa del funnel | Canal Google | Hermana que complementa |
|---|---|---|
| Generar demanda (frío) | Demand Gen / YouTube | `facebook_ads_lushows`, `tiktok_ads_lushows` |
| Capturar intención (caliente) | **Search** (genérico + marca) | — el corazón de esta skill |
| Re-impactar (tibio) | Display/Demand Gen remarketing | Meta retargeting |
| Cerrar | el lead va a WhatsApp | `ventas_lushows` |

La secuencia sana con poco presupuesto: **Search primero, valida, junta datos; luego suma remarketing barato; PMax/Demand Gen solo cuando hay caja y assets de calidad** (creativos los hace `directorcreativo_lushows`). La viabilidad de meterle más canales se valida en `economist_lushows`.

## Errores comunes — blacklist

- **Activar todos los tipos de campaña a la vez con poco presupuesto.** Diluyes y nada aprende. Fix: Search-first, suma canales cuando haya datos y caja (ver 07, 18).
- **Tratar PMax como "fácil, lo prendo y ya".** Sin exclusiones de marca ni señales, PMax canibaliza tráfico de marca y se infla solo robándole crédito a Search. Fix: usa los controles 2025 (reporte por canal, exclusiones, negativas de campaña) (ver 12).
- **Activar AI Max sin negativos.** La expansión de keywords te trae consultas irrelevantes y quema budget. Fix: lista de negativos robusta antes de prenderlo (ver 90, 22).
- **Buscar Discovery en el menú.** Ya no existe; lo reemplazó Demand Gen en 2024. Fix: usa Demand Gen (ver 41).
- **Usar Display/YouTube para "vender ya".** Es inventario de baja intención; vende poco directo. Fix: úsalo para remarketing/awareness, no para conversión inmediata (ver 43, 40).
- **Asumir que la IA suple la falta de medición.** El modelado necesita una base real de conversiones bien medidas. Fix: cimienta GA4 + Enhanced Conversions (ver 05, 06).
- **Creer que AI Overviews mató Google Ads.** Bajan clics informacionales, no los comerciales. Fix: prioriza keywords de alta intención de compra (ver 92, 20).
- **Aceptar a ciegas los assets que genera Gemini.** Puede inventar claims o sonar genérico/AI. Fix: revisa y edita; el arte fino lo dicta `directorcreativo_lushows`.
