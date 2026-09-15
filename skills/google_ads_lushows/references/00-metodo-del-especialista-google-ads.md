# 00 — Método del especialista en Google Ads

Este es el sistema operativo de la skill: cómo piensa un especialista de élite antes de tocar un solo botón. Google Ads no es "poner anuncios"; es **capturar demanda que ya existe** (gente buscando con intención) y convertirla en ventas medibles. Google NO genera deseo de la nada — eso es trabajo de Meta o de Demand Gen (rutea a `facebook_ads_lushows`, ver 03 y 41). Lee este módulo cuando empieces CUALQUIER proyecto de Google Ads, cuando no sepas por dónde arrancar, o cuando quieras entender cómo se conectan los otros 99 módulos.

## La pregunta que va primero: ¿la gente BUSCA esto?

Antes de gastar un peso, responde esto con honestidad brutal. Google es un buscador: solo funciona si hay **volumen de búsqueda con intención comercial**. Si nadie escribe tu categoría en Google, Google Search NO es tu canal — tu problema es *generar* demanda, y eso vive en Meta (rutea a `facebook_ads_lushows`) o en Demand Gen/YouTube (ver 41).

| Señal | Google Search SÍ | Google Search NO (usa Meta/Demand Gen) |
|---|---|---|
| Categoría conocida | "plomero Bogotá", "curso de Excel" | producto nuevo que nadie nombra todavía |
| El cliente busca solución | "calculadora costos restaurante" | impulso visual (moda, decoración bonita) |
| Demanda medible | Keyword Planner muestra volumen | volumen ~0 búsquedas/mes |
| Intención comercial vs informacional | "comprar / precio / cerca de mí" | "qué es / cómo funciona" (hoy se la come AI Overviews, ver 92) |

Verifícalo en **Keyword Planner** (Herramientas → Planificación). Si hay volumen → Search-first (ver 11). Si no hay → no fuerces Google; generas demanda en Meta y *después* capturas a quien ya te busca por marca (ver 39). En 2026 hay un matiz nuevo: las búsquedas **informacionales** ("qué es food cost") cada vez las responde **AI Overviews** sin clic, pero las **comerciales** ("comprar plantilla food cost", "calculadora costos restaurante Colombia") siguen clickeando anuncios (ver 92). Prioriza siempre intención comercial.

## El proceso completo: 4 fases

| Fase | Qué haces | Módulos |
|---|---|---|
| **1. Diagnóstico** | ¿Hay búsqueda? ¿Cuánto presupuesto real? ¿Cuál es el CAC/LTV que aguanta? ¿La venta cierra por WhatsApp/llamada? | 00, 03, 07, → `economist_lushows` |
| **2. Setup / cimientos** | Cuenta + MCC, verificación de anunciante, Google tag + GA4, conversiones, Enhanced Conversions, Consent Mode v2, OCI/gclid si cierra offline | 04, 05, 06, 53 |
| **3. Estructura + lanzamiento** | Elegir tipo de campaña, keywords, concordancia, negativas, RSA, landing, Smart Bidding | 10–32, 33 (→`desingweb-lushows`) |
| **4. Optimización + escala** | Search terms, negativas, reglas, kill, escalar tCPA/tROAS sin romper aprendizaje | 60–74 |

La regla de oro: **nadie pasa a la fase 3 sin la fase 2 cerrada.** Lanzar sin conversiones bien medidas es tirar plata y, peor, le da datos basura al Smart Bidding (ver 13). En la era post-cookie esto es más cierto que nunca: sin Enhanced Conversions + Consent Mode v2 ves menos conversiones de las reales y la IA puja por debajo de lo óptimo (ver 06).

## Los 6 modos de la skill

Cuando Lushows te pida algo, ubícate en uno de estos modos y entra por el módulo correcto:

| Modo | Cuándo | Entrada |
|---|---|---|
| **Diagnóstico** | "¿me sirve Google?", "¿cuánto necesito?" | 00, 03, 07 |
| **Setup** | cuenta nueva, no mide conversiones | 04, 05, 06 |
| **Construcción** | armar campañas desde cero | 10, 11, 20, 30 |
| **Optimización** | "el CPA subió", "no convierte" | 60, 61, 68, 70 |
| **Escala** | "funciona, quiero más" | 72, 73, 74 |
| **Rescate** | cuenta suspendida, política | 08, 93 |

## El checklist mental del especialista (antes de cada decisión)

Un especialista de élite no improvisa. Antes de tocar la cuenta corre esta secuencia de 5 preguntas:

1. **¿Hay demanda capturable?** Keyword Planner. Si no → no es Google (ver 03).
2. **¿La medición está limpia?** ¿Una sola fuente de conversión por acción, Enhanced Conversions activo, OCI montado si cierra por WhatsApp? Si no → arregla esto antes de optimizar nada (ver 05, 06, 53).
3. **¿El número aguanta?** ¿CPA estimado < CAC máximo del negocio? Si no → es problema de unit economics, no de pauta (ver 07 → `economist_lushows`).
4. **¿El presupuesto da ~15–30 conversiones/mes?** Si no → concentra en una sola campaña Search o no lances (ver 07).
5. **¿Qué señal voy a leer y cuándo?** Define la métrica (CPA/ROAS, no CPC) y el plazo (30 días, no 3) ANTES de lanzar, para no apagar por pánico (ver 60, 07).

## Cómo cruza con las otras skills

Esta skill es **paid search** (pauta pagada en Google). NO hace SEO orgánico — el posicionamiento orgánico es otra disciplina fuera de esta skill. Rutea fuera cuando el problema no es la pauta:

| Necesidad | Va a |
|---|---|
| Generar demanda / pauta en Meta / Instagram | `facebook_ads_lushows` |
| Descubrimiento / video corto / audiencias frías visuales | `tiktok_ads_lushows` |
| Cerrar la venta (guion WhatsApp, objeciones) | `ventas_lushows` |
| Landing / web / CRO / velocidad | `desingweb-lushows` |
| Marca, logo, identidad, creativo de video | `directorcreativo_lushows` |
| ¿Es viable? pricing, CAC/LTV, punto de equilibrio | `economist_lushows` |

En LatAm el patrón típico es: **Google captura la intención → manda el lead al WhatsApp → la venta la cierra un humano.** Esa venta real hay que devolvérsela a Google con **Offline Conversion Import (OCI)** vía gclid (ver 53), o el algoritmo optimiza hacia clics baratos en vez de ventas reales. OCI es el equivalente Google del `ctwa_clid` que en Meta cierra el clic-a-WhatsApp.

## Honestidad data-driven (la voz de la skill)

Esta skill no vende humo. Si los números no cierran, lo dice. Tres compromisos:

- **Anti-hype:** "Google Ads garantiza ventas" es mentira. Garantiza *exposición a intención*; el cierre depende de oferta, landing y vendedor. Si el producto no se vende, la pauta solo acelera la quema de plata.
- **COP siempre:** todos los números van en pesos colombianos, con benchmarks LatAm jun-2026, no dólares de blogs gringos.
- **Jerga explicada:** cada sigla (CPA, tROAS, Ad Rank, gclid, OCI) se traduce a humano la primera vez (ver glosario, 09). El dueño no técnico tiene que entender qué está pagando.

## Errores comunes — blacklist

- **Lanzar Google porque "todo el mundo pauta en Google", sin verificar volumen de búsqueda.** Si nadie busca tu categoría, quemas presupuesto en Display/PMax que es interrupción disfrazada. Fix: Keyword Planner primero; si hay 0 búsquedas, es trabajo de Meta (ver 03).
- **Empezar por las campañas y dejar la medición "para después".** El Smart Bidding aprende de tus conversiones; sin conversiones aprende de nada. Fix: cierra la fase 2 (04–06) antes de gastar.
- **Medir el "contacto de WhatsApp" como venta.** Un clic a WhatsApp NO es una venta; el algoritmo te llenará de curiosos. Fix: importa la venta real cerrada vía OCI (ver 53).
- **Tocar los targets de puja cada 2 días.** Reinicias el aprendizaje y nunca estabiliza. Fix: deja ~2 semanas tras cualquier cambio de tCPA/tROAS (ver 13, 15).
- **Confundir Google (captura) con Meta (genera) y esperar que Google "haga conocer la marca".** Google no crea deseo de la nada. Fix: divide el funnel — Meta arriba, Google abajo (ver 03, 97).
- **No definir el CAC máximo que el negocio aguanta antes de pautar.** Sin ese número no sabes si un CPA es bueno o un desastre. Fix: pásalo por `economist_lushows` primero (ver 07).
- **Creer que esta skill hace SEO.** No. Es paid search. El orgánico es otra disciplina. Fix: no mezcles tácticas orgánicas con presupuesto de pauta.
- **Juzgar la cuenta por CPC barato.** CPC barato que no convierte es plata perdida más lento. Fix: la métrica norte es CPA/ROAS sobre venta real (ver 60, 64).
