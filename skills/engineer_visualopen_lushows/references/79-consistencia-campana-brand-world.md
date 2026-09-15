# 79 — Consistencia de campaña / brand world (a escala de producción)

La consistencia de UN personaje es lo mínimo; una campaña necesita un **brand world** entero que se sostenga en
decenas de assets, formatos y semanas.

## El look bible (el doc del brand world)
El universo visual codificado: **palette** (BIO-SETA: verdes bosque, marfil micelio, ámbar) · **type system** ·
**photographic style** · una **lighting signature** (ej. luz suave de ventana norte, un solo key, falloff gentil) ·
**world rules** (texturas = madera cruda, lino, vidrio; nunca plástico, nunca neón). **Es la constitución que todo asset obedece.**

## Vende el look antes de producirlo
Pipeline **mood board → style frames → animatic**. **Style frames** = imágenes hero únicas que prueban el grade, el
lente y el mood; el cliente aprueba el *look*, no una promesa vaga. El **animatic** secuencia frames para testear el
ritmo antes de gastar en renders finales. **Aprobar style frames primero evita el error más caro: producir 40 assets off-brand.**

## El sistema de dirección de arte (receta repetible)
**Mismo lente (ej. look 50mm), mismo grade (LUT), misma dirección de luz, mismas reglas de composición (ritual
centrado, producto en rule-of-thirds)** — escrito y aplicado a cada asset. **La consistencia es un sistema, no un vibe que reinvocas cada vez.**

## Consistencia IA a escala de campaña
Lockea el estilo con **Midjourney `--sref`** (o un seed `--sref` que congelas y reúsas en todo el set) + **`--cref`**
para personajes. Para más control, **entrena un style LoRA** (Flux/SDXL) sobre tus frames aprobados → cada generación
hereda grade y textura. Mantén un **master prompt template** — un bloque fijo (luz, lente, paleta, world rules) en el
que solo cambias el sujeto. Lockea **seeds/style tokens** para que personaje + producto + mundo queden coherentes en
el **set de imágenes Y el de video** (en video, mismo start-frame de referencia; Runway Gen-4 References, Kling, Veo con stills idénticos).

## Design system para contenido & multi-formato
Templates, **title system**, **logo lockup**, **safe areas** por formato. **Multi-formato:** una campaña renderizada
a **9:16 / 1:1 / 16:9** — hero film + cutdowns + stills + banners — todos sintiéndose como UNA cosa; diseña la
composición hero con centros reframe-safe para que los crops no la rompan.

## Asset management & governance
**Naming** estricto (`BIOSETA_Q3_MelenaFoco_HERO_9x16_v03`), un **master** por asset, log de **approvals/versioning**.
**Tone of voice:** copy y visual alineados (un mundo visual calmado/científico exige copy calmado/preciso, no hype-bro). **Governance:** un **brand guidelines doc** vivo que todos (y cada prompt IA) referencian.

## Gotchas
1. **Drift en un set grande** — para el asset #30 el verde derivó a azul y la luz cambió de lado; re-ancla a los style frames cada batch.
2. **Outputs off-brand colándose** — gate cada generación contra el look bible antes de entrar al master folder.
3. **Uncanny consistency** — la IA puede hacer un set *demasiado* idéntico/plástico-perfecto, leyéndose fake; varía framing/grano intencionalmente para mantenerlo humano.
4. **Inconsistencia inducida por formato** — un hero 16:9 cropeado a 9:16 pierde el logo o decapita el producto; diseña safe areas up-front.
5. **Churn de versión de seed/sref** — una tool actualiza su modelo y tu `--sref` lockeado renderiza distinto a mitad de campaña; pinea versiones de modelo y re-bakea referencias.
6. **Mismatch tono-visual** — imágenes calmadas hermosas con copy "BUY NOW 50% OFF" agresivo rompe el brand world; gobierna copy y arte juntos.

**Fuentes:** docs.midjourney.com/docs/style-reference · replicate.com/blog (fine-tune flux) · runwayml.com/research (Gen-4 References).
