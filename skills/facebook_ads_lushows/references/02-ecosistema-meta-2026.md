# 02 — El ecosistema Meta en 2026

Mapa del territorio: dónde puede aparecer tu anuncio, qué decide la máquina y qué sigue decidiendo el humano. Lee este módulo al empezar o cuando dudes entre placements automáticos y manuales, o cuando alguien te venda "trucos de segmentación" de 2019.

## Las superficies (dónde aparece tu ad)

| Superficie | Qué es | Para qué sirve mejor |
|---|---|---|
| Facebook Feed | El muro clásico | Audiencia 30+, compras consideradas, LatAm pyme |
| Instagram Feed | Muro de IG | Producto visual, 20-45 años |
| Stories (FB/IG) | Pantalla completa vertical, 15s | Ofertas directas, urgencia |
| Reels (FB/IG) | Video corto vertical | Volumen barato, descubrimiento, creativo nativo estilo UGC (contenido tipo usuario real) |
| Audience Network | Apps y sitios de terceros donde Meta revende inventario | Alcance barato, calidad de clic baja; el sistema lo dosifica solo |
| Messenger | Bandeja de Messenger | Anuncios que abren chat |
| WhatsApp | No muestra ads dentro del chat, pero sí en **WhatsApp Status** (novedad 2026) y es el **destino** #1: anuncios Click-to-WhatsApp (CTWA) desde FB/IG | El canal de cierre #1 en Colombia/LatAm (ver 50, 53 y ventas_lushows) |
| **Threads** | Feed de Threads, **ahora placement por DEFAULT (2026)** | Alcance incremental joven; ya entra automático, no lo apagues sin datos |

**Cambios de placement 2026 (importante):** Instagram **Explore** y los **Reels post-loop** fueron ELIMINADOS como placements. **Threads** entró por default. **WhatsApp Status** se sumó como inventario de anuncios. Si tienes campañas viejas con placements manuales fijos, revísalas: pueden estar apuntando a inventario que ya no existe (detalle en `actualizacion-2026-06`).

## Placements: Advantage+ por default (ya casi sin alternativa manual)

- **Advantage+ placements** (automático, default): Meta distribuye tu ad entre TODAS las superficies buscando el resultado más barato. El sistema usa inventario barato (Reels, Audience Network) para bajar tu costo promedio.
- **Manual**: con la unificación Advantage+ de feb-2026, el control manual es ahora *opt-out por sección* dentro de una campaña que nace AI-on. Solo desactivas placements con una razón concreta: branding que exige contexto premium, creativo que solo funciona en un formato, o compliance del vertical.

**Regla: automático por default.** Recortar placements "porque Audience Network se ve feo" sube tu CPA en la mayoría de cuentas: le quitas al sistema inventario barato para encontrar compradores. Si un placement de verdad quema plata, lo verás en el desglose (Breakdown → Placement) con datos, no con intuición.

Entrega un creativo por ratio: 1:1 o 4:5 para feeds, 9:16 para Stories/Reels/Status. Meta adapta automáticamente (Advantage+ Creative puede recortar, retocar e incluso generar **image-to-video**, ver 90, 91), pero el 9:16 nativo bien hecho rinde más que un cuadrado estirado.

## La era de la automatización: Advantage+, GEM y Andromeda

La dirección estratégica de Meta es clara: **menos palancas manuales, más máquina**. En 2026 esto dejó de ser tendencia y pasó a ser la única forma:

- **Unificación Advantage+ (feb-2026)**: la "campaña manual" desapareció como tipo. Toda campaña nace con AI activado; haces opt-out por sección. ASC ahora se llama **Advantage+ Sales**; existe **Advantage+ Leads** para captación (ver 12, 52).
- **Cap de clientes existentes (mar-2026)**: en Advantage+ Sales puedes limitar a 25-30% el gasto en clientes que ya te compraron, para forzar adquisición de nuevos. Combínalo con Value Rules (ver 01, 15, 24).
- **GEM (nov-2025)**: modelo generativo de Meta sobre Andromeda; mejora la predicción de qué ad le sirve a quién.
- **Andromeda**: el motor de retrieval de ML que, de millones de anuncios posibles, preselecciona cuáles compiten por cada impresión de cada usuario. Consecuencia práctica: **el creativo es el targeting**. Andromeda "lee" tu video/imagen/texto y decide a qué tipo de persona enseñárselo. Por eso la diversidad de creativos vale más que cualquier ajuste de audiencia: cada ángulo le abre al motor una población distinta. **Necesitas 10-15 creativos conceptualmente distintos** (no casi-duplicados, que colapsan en un mismo Entity ID), y su vida útil es **2-4 semanas** (ver 39, 92).
- Los objetivos de campaña siguen siendo los 6 de **ODAX**: Awareness, Traffic, Engagement, Leads, App promotion, Sales. Eliges el resultado de negocio; el sistema arma el resto (ver 11).

## Señal y medición en 2026 (lo que cambió)

- **"Píxel" → "Dataset"**: en Events Manager el Pixel ID ahora se llama Dataset ID (ver 05).
- **CAPI de un clic**: Meta puede levantar el server-side por ti; se amplió a anunciantes solo-píxel (ver 06).
- **EMQ piso 8**: la calidad de match de eventos subió de exigencia; <8 ya te deja en desventaja (ver 06).
- **Atribución solo-clic (ene-2026)**: Meta quitó las ventanas view-through 7d/28d del API; solo cuenta clic. Reporta menos, pero más honesto (ver 16).

## Meta Business Agent (3-jun-2026)

Meta lanzó un **bot de IA** que atiende conversaciones en WhatsApp/Instagram por el negocio. Relevante para CTWA: el clic del anuncio puede aterrizar en un agente que precalifica antes de pasar a humano (ver 50, 51 y ventas_lushows para el cierre). No reemplaza al cierre humano en high-ticket (ver 58), pero baja el costo de atender volumen.

## Qué controla el media buyer en 2026 vs qué cedió

| Sigue siendo tuyo | Lo cedió al algoritmo |
|---|---|
| La oferta y el precio | Placement fino (qué superficie, qué hora) |
| El creativo: ángulos, ganchos, VOLUMEN de variantes (10-15) | Micro-targeting (intereses apilados, edades exactas) |
| El objetivo ODAX y el evento de optimización | A quién exactamente le muestra cada ad |
| El presupuesto y el ritmo de escalado | La puja (automática) |
| La medición: dataset + CAPI + EMQ 8+ (ver 05, 06) | Las variaciones menores del creativo |
| Estructura de cuenta, Value Rules y compliance (ver 04, 08, 15) | El mix entre superficies |

Tu trabajo ya no es "encontrar la audiencia": es darle al sistema una oferta vendible, señal de conversión limpia y munición creativa variada. Lo demás es estorbar.

## Mapa rápido: dónde vive cada decisión en 2026

| Decisión | Quién la toma hoy | Tu palanca |
|---|---|---|
| A quién mostrarle el ad | Andromeda (lee el creativo) | Variedad creativa (ver 92) |
| En qué superficie aparece | Advantage+ placements | Dar 9:16 + 1:1 nativos (ver 33) |
| Cuánto pujar | Automático | Estrategia de puja + Value Rules (ver 15) |
| Cuánto gastar y a qué ritmo | Tú | Presupuesto + escalado 20-30% (ver 72) |
| Qué evento optimizar | Tú | Dataset + CAPI + EMQ 8+ (ver 05-06) |
| Qué oferta y qué decir | Tú | Oferta + copy + ángulos (ver 41, 40, 38) |
| Si pasa o no compliance | ML de revisión | Pre-flight del 08 |

La lectura honesta: en 2026 le cediste a Meta casi toda la "operación" y te quedaste con la "estrategia". Quien sigue tratando de microgestionar placements y audiencias está peleando una guerra que terminó; quien invierte esa energía en oferta y creativo gana.

## Receta: checklist de assets por campaña

1. **10-15 creativos con ángulos DISTINTOS** (no 3 colores del mismo ad): problema, prueba social, demostración, comparativa, UGC, oferta (ver 38).
2. Al menos un 9:16 nativo para Reels/Stories/Status y un 1:1 o 4:5 para feeds.
3. Copy primario en 2 longitudes (corto de 1-2 líneas y largo con historia): Meta rota y aprende cuál sirve por placement (ver 40).
4. Placements en Advantage+ (automático) salvo razón documentada.
5. Destino correcto para el negocio: web con dataset+CAPI (ver 05-06) o WhatsApp si el cierre es por chat (ver 50).

## Errores comunes — blacklist

- **Excluir Audience Network y Reels "por estética"**: le subes el costo promedio al sistema sin datos que lo justifiquen.
- **Dejar placements manuales viejos apuntando a Explore/Reels post-loop**: esos placements se eliminaron en 2026; revisa campañas heredadas.
- **Apilar 15 intereses como en 2019**: con Advantage+ audience tu segmentación es una sugerencia; el esfuerzo va al creativo.
- **Lanzar solo 3 creativos casi idénticos**: colapsan en un Entity ID; Andromeda no tiene de dónde elegir (ver 92).
- **Un solo creativo cuadrado para todos los placements**: en Stories/Reels/Status se ve ajeno y el EAR (ver 01) se hunde.
- **Ignorar WhatsApp como destino en LatAm**: si el negocio cierra por chat, la campaña CTWA suele ganarle a mandar tráfico a una web que nadie usa.
- **Pelear contra la automatización** (apagar todo lo Advantage+): tras la unificación de feb-2026 remas contra la única forma del sistema; pierdes inventario y optimización.
- **Confiar ciegamente en la automatización sin medir**: la máquina optimiza lo que le señalas; con dataset roto, optimiza basura (ver 05-06).
