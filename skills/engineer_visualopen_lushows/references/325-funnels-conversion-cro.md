# 325 · Funnels & CRO (fricción, copy, optimización de conversión)

> [[101-growth-marketing-tecnico-2026]] dice "la landing es un funnel de decisión".
> Esto es el bisturí: dónde gotea, qué fricción quitar, qué probar primero y los números 2026.

## Benchmarks 2026 (para saber si vas mal o bien)
- **Mediana** de landing dedicada: **6.6%**; promedio cross-industry ~4%; **top 10%: ~11.45%**.
- Páginas web genéricas convierten ~2.35% → una landing **dedicada** casi duplica.
- La brecha mediana↔top **no es tráfico, es optimización sistemática**. CRO 90 días = 30-80% uplift.

## El funnel — encuentra el escalón que gotea
Instrumenta cada paso como evento ([[323-analytics-tracking-posthog-ga4]]): `view → cta_click →
form_start → form_submit → order_placed`. El paso con **mayor drop-off relativo** es tu prioridad #1,
no el que "intuyes". Segmenta el drop por dispositivo y fuente: a veces es solo móvil, o solo paid.

## Fricción — el enemigo medible
La fricción es la suma de esfuerzo + ansiedad + distracción. Recortes con ROI probado:

| Cambio | Efecto medido |
|---|---|
| Formulario 5→3 campos | **+50%** conversión |
| 3 campos vs 9 campos | 10.1% vs 3.6% |
| 11→4 campos | **+160%** |
| Cada campo >5 | **−20% a −30%** penalización |

Pide solo lo que necesitas AHORA (en LatAm: nombre + WhatsApp basta; dirección la pide el bot Addrian
después). Cada campo extra es un peaje. Quita navegación y links externos de la landing: **un goal, un CTA**.

## Above-the-fold — el 80% del peso de conversión
Los primeros 5 segundos deciden. Orden: **headline de beneficio** (no de feature) → subhead de value prop
→ visual del producto → **UN CTA primario** → **social proof a un scroll del CTA** (no enterrada abajo).
Velocidad de carga es parte del CRO: LCP lento mata conversión antes de leer (ver [[322-seo-tecnico-a-fondo]]).

## Copy que convierte (ver [[267-copywriting-redaccion-persuasiva]])
- **Beneficio sobre feature**: "duerme mejor en 2 semanas" > "200mg de Reishi".
- **Lenguaje simple = menor carga cognitiva = más conversión**. Frases cortas, sin jerga.
- **CTA en primera persona / acción concreta**: "Quiero mi frasco" > "Enviar".
- **Reduce ansiedad junto al CTA**: garantía, envío, "responde un humano por WhatsApp", reseñas reales.
- **Especificidad gana**: cifras, plazos, nombres de clientes reales > adjetivos vacíos.

## Qué probar primero (orden de impacto)
1. Headline / oferta (mueve más que cualquier color).
2. Número de campos del formulario.
3. Posición y copy del CTA + social proof adyacente.
4. Prueba social: **video 15-45s gana 30-50% a texto** ([[101-growth-marketing-tecnico-2026]]).
5. Velocidad de carga del fold.
Cada test con método de [[324-ab-testing-experiments]]: hipótesis, muestra, sin peeking.

## Gotchas
1. Optimizar color del botón antes que la oferta = mover sillas en cubierta.
2. Formulario largo "para calificar leads" → calificas matando volumen; califica después.
3. Social proof enterrada al fondo en vez de junto al CTA.
4. Múltiples CTAs/objetivos → conversión diluida (browsing, no decisión).
5. Declarar ganador con tráfico insuficiente o sin segmentar móvil.
6. Claims de salud agresivos = fricción legal en LatAm + rechazo de plataformas.

**Fuentes:** growthstackblog (LP benchmarks 2026) · digitalapplied.com (conversion benchmarks 2026) ·
almcorp.com (LP optimization) · colorlib.com (LP statistics 2026).

Cruza con [[267-copywriting-redaccion-persuasiva]] y [[328-pricing-page-packaging]].
