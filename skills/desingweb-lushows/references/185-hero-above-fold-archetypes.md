# 185 — Hero sections & above-the-fold archetypes

**CRAFT + conversión.** El primer pantallazo. Pareja de 20 (layout/hero archetypes), 17 (copy/CTA), 10 (art direction), 40 (LCP). Regla de oro: **el hero tiene UN trabajo — comunicar qué/para quién/por qué + una acción en ~5 segundos; clarity > cleverness; la tríada value-prop + visual + CTA; el hero suele ser el LCP.**

## 1. El trabajo del hero

Comunicar *qué es, para quién, por qué importa* + ofrecer *una acción* en **~5 segundos** (la ventana se acortó). El "above the fold" sigue mandando (la mayoría nunca scrollea, sobre todo en mobile). Anatomía mínima 2026: **5 elementos** — headline, subhead, CTA primario, visual de producto, **una** señal de confianza (cada extra es carga cognitiva, el enemigo #1 de conversión). **5-second test:** muestra el hero 5s, ocúltalo, pregunta "¿qué hace y para quién?" — si no responde, falló.

## 2. El catálogo de arquetipos (con cuándo)

| Arquetipo | Comunica | Cuándo |
|---|---|---|
| **Centered** | Foco, claridad | SaaS — **el de mayor conversión** para software. Default seguro |
| **Split/asymmetric** | "Te digo + te muestro" | Tienes screenshot/demo. El caballo de batalla B2B (50/50 o 60/40) |
| **Full-bleed image/video** | Emoción, marca | Brand-led, hospitality, fashion. Riesgo: el texto compite |
| **Product-shot** | "Esto recibes" | E-commerce físico, hardware |
| **Big-type/editorial** | Voz, actitud | Agencias, portfolios. 2026 = "confidence in type" |
| **Bento** | Multi-feature de un vistazo | SaaS multi-feature (cards modulares, popularizado por Apple) |
| **Illustration** | Calidez, anti-genérico | Productos abstractos (fintech, dev tools) |
| **Interactive/WebGL** | Inmersión | **Solo** agencias creativas/fashion (§4 — costo de perf brutal) |
| **"Show the product" (screenshot)** | Prueba tangible | SaaS — la demo es el argumento |
| **Embedded-input** | Fricción cero | Search/prompt/email — la acción dentro del hero |

## 3. El copy

**Headline** (la palanca de mayor impacto): comunica el **outcome del usuario**, no el feature. Patrón Problem→Outcome→Proof ("Build beautiful landing pages in minutes without code"). Evita el vago ("La plataforma para equipos modernos" no dice nada). **Subhead** (el cómo + credibilidad: "Usado por 12.000 equipos", "Sin tarjeta"). **CTA** outcome-focused en 1ª persona ("Start building free" > "Submit"; "Trial for free" subió trial-start **104%** vs "Sign up"). **Social proof** (logos/rating/users, una señal prominente en el primer pantallazo).

## 4. El visual

Jerarquía: **product screenshot** (máxima prueba, SaaS) > lifestyle/emoción (brand) > 3D/abstract (diferenciación) > stock genérico (a evitar siempre — mata credibilidad). Craft 2026: **dashboard-tilt/perspective** (UI inclinada en 3D), **looping demo**, **annotated UI**. **Performance crítico:** el hero suele ser el **LCP** → imagen optimizada/responsive, `fetchpriority="high"`, no lazy-load del asset principal. **WebGL/Spline prohibido salvo brand-led** (una escena Spline carga 800KB-2MB de JS, colapsa Lighthouse, mata mobile 4G; el patrón que sí se shippea: **lazy-load del canvas detrás de un poster estático**).

## 5. Layout & responsive

**Un solo focal point** (jerarquía: headline → subhead → CTA → visual; whitespace aislando el CTA). **El fold en mobile manda** (headline + value-prop + CTA primario deben caber sin scroll; si el CTA cae bajo el fold pierdes conversiones). **Scroll cue** sutil si el hero ocupa el viewport. **Sticky CTA** en mobile. **Motion con restricción** (entrance choreography stagger 60-120ms para guiar la lectura, *no* animaciones que retrasen el LCP).

## 6. Conversion craft & tendencias 2026

Patrones A/B-proven: value-prop clarísimo, **un solo CTA primario** (múltiples/en conflicto pueden bajar conversión hasta -266%), reducir carga cognitiva. Landing dedicada convierte 5-15% vs 2-3% de sitios completos. Secuencia de testing por impacto: **headline > CTA copy > CTA color**. Tendencias: bold/expressive type + variable fonts, bento grids, 3D selectivo, "information density" (mostrar la solución de inmediato), hero AI-personalizado por segmento/fuente.

## Hero anti-patterns — blacklist
**headline vago/abstracto** ("Reimagina lo posible") · **carousel/slider hero** (nadie espera la rotación; mata densidad y LCP — muerto en 2026) · **dos CTAs compitiendo** con igual peso (-266%) · **CTA bajo el fold en mobile** · **stock photography genérica** (handshakes, "diverse team laughing") · **WebGL/Spline pesado sin poster fallback** · **cleverness sobre clarity** · **hero que esconde el valor** tras una imagen bonita sin copy legible · **"Submit"/"Sign up"** genérico en vez de outcome-focused · **sobrecarga** (>5 elementos compitiendo).
