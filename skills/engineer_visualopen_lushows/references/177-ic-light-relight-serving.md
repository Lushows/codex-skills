# 177 · IC-Light relight en producción (foreground + condición de luz, consistencia, serving)

> Relight = re-iluminar un sujeto recortado para que case con una luz/fondo target SIN reinventar el sujeto.
> IC-Light lo logra inyectando el foreground como **condición fija**; el truco de prod es la consistencia de identidad y un serving caliente.

## Las tres variantes (elige por caso de uso)
IC-Light expone modelos distintos según de dónde sale la luz. No son intercambiables:

| Modelo | Entrada de luz | Caso |
|---|---|---|
| **text-conditioned** (FC) | prompt ("golden hour, left window") | no tienes fondo, describes la luz |
| **background-conditioned** (FBC) | imagen de fondo/escena | pegas el sujeto en una escena real → matchea su luz |
| **foreground-conditioned** (FC v2) | gradiente/mapa de luz | control fino de dirección, packshots |

V1 (SD1.5) es **comercial-OK**. **V2 es FLUX-based y NON-COMMERCIAL** [verificado, fal.ai/HF]: mejor preservación de detalle (VAE 16ch, alta-res nativa) pero NO la uses en producto pagado sin licencia. Para BIO-SETA / cliente pagado → V1 o licencia.

## Cómo funciona (el porqué del "no driftea")
El foreground entra como latente **concatenado**, no como prompt — el modelo no puede inventar el sujeto, solo redistribuir luz/sombra sobre los píxeles dados. Por eso preserva label/logo/forma mucho mejor que un img2img genérico. La luz target llega por el canal correspondiente (prompt, bg-latente, o light-map).

## Pipeline de relight (orden que importa)
1. **Matting limpio** → alpha de calidad (BiRefNet, ver [[137-matting-bg-removal-escala]]). Fringe en el cutout = halo iluminado falso.
2. **Normaliza el foreground**: aplana iluminación residual del original (su luz vieja "pelea" con la nueva). IC-Light asume foreground neutro-ish.
3. **Elige variante** según tengas fondo (FBC) o prompt (FC).
4. **Relight** a resolución de trabajo (1024). Genera el sujeto re-iluminado.
5. **Compositing + sombra**: IC-Light re-ilumina el sujeto pero **NO crea la sombra de contacto** en el plano nuevo → la añades aparte (ver [[179-shadow-generation]]).
6. Pasada final low-denoise sobre la costura para fundir borde.

## Consistencia de identidad (el problema #1)
- **Drift de color**: relight puede teñir el sujeto (sobre todo blancos/etiquetas). Mitiga con **mask + composite-back** de la zona crítica (label) y A/B pixel-diff.
- **Lotes de catálogo**: fija seed + mismo prompt de luz por colección → look coherente entre SKUs. Seed aleatorio = cada foto con luz distinta.
- **Material specular** (vidrio, frascos): IC-Light inventa highlights plausibles pero no físicamente fieles; valida a ojo o usa light-map (FC v2) para controlar dónde caen.

## Serving en GPU serverless
- **VRAM**: V1 (SD1.5) cabe holgado en 12-16GB; V2 (FLUX) pide ~24GB. Ada/Ampere bastan.
- **Warm-state**: carga el unet + VAE + el módulo IC-Light UNA vez en el handler global; no recargues por job (cold de 20-40s evitable). Ver patrón en [[113-network-volume-modelos-grandes]] para los pesos.
- **Batch**: agrupa relights del mismo lote en una sola invocación caliente; el cuello es la carga, no el step.
- **Salida**: devuelve PNG con alpha si vas a recomponer aguas abajo; no quemes el fondo todavía.

## Gotchas
1. **V2 non-commercial** — el error de licencia más caro; baked en producto = riesgo legal.
2. **Foreground con su luz vieja intacta** → resultado "doble luz" fantasma; aplana antes.
3. **Sin sombra de contacto** el relight más perfecto se ve flotando — siempre paso de sombra después.
4. **Specular/transparencias** → highlights inventados; no para joyería/vidrio fino sin revisión.
5. **Resolución baja** pierde el detalle que justifica V2; trabaja a ≥1024 y upscalea aparte.

Cruza con [[60-edicion-imagen-avanzada-ia]], [[193-product-photography-pipeline]] y [[179-shadow-generation]].
