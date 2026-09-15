# 182 · Inpaint/Outpaint en producción (máscara, blend y borde sin costura)

> El modelo no es lo que falla en inpainting de producción: falla la **máscara** y la **costura**.
> Servir esto bien es geometría de máscara + composite-back + blend de borde, no solo un checkpoint.

## El pipeline real (no es "pasa imagen+mask al modelo")
1. **Mask**: binaria, alineada al pixel, con **feather** (Gaussian blur 4-12px en el borde). Mask dura de 1-bit = costura visible siempre.
2. **Crop a la región** (+ contexto): no denoises 2048² para tapar un objeto pequeño; recorta un bbox con padding (32-128px), inpaint en resolución nativa del modelo (1024² SDXL/FLUX), recompón. Más rápido y mejor calidad.
3. **Inpaint** con modelo dedicado (no el base).
4. **Composite-back**: pega SOLO la región generada en la original usando el mask feathered como alpha. Esto mata el drift global (el modelo recolorea zonas intactas; tú las descartas).
5. **Color-match** del borde: el tell #1 del seam es diferencia de color/exposición, no de contenido. Iguala medias por canal o pasada low-denoise sobre la costura.

## Modelos (verificado 2026)
| Modelo | Uso | Notas |
|---|---|---|
| **SDXL-Inpainting** (dedicado) | barato, ControlNet, LoRA | fine-tuned a la tarea → mejor blend que base SDXL. VRAM ~8-12GB |
| **FLUX.1 Fill [dev]** | SOTA calidad fill/expand | 12B, ~24GB; sigue instrucción de texto + mask; líder de coherencia |
| **FLUX.1 Fill [pro]** | API, sin VRAM propia | cuando no quieres servir 24GB |

Usar el base model con un mask **no** es inpainting real: los inpaint-finetunes aprenden a respetar el borde del mask. [no verificado: VRAM exacta varía por quant].

## Outpaint = inpaint del canvas extendido
- Extiende el lienzo, el área nueva es el mask, pasa el original como contexto.
- **Differential Diffusion** es la técnica clave 2026: en vez de mask binaria usa un **mapa de fuerza** continuo (denoise fuerte lejos del borde, suave cerca) → blend mucho mejor cuando original y extensión son muy distintos.
- Outpaint en **pasadas incrementales** (256-512px por vez), no un salto de 2x: cada paso ve más contexto real → menos alucinación e inconsistencia.

## Gotchas de borde (los que muerden)
1. **Seam por color, no por contenido** — con blur de 80-100px en outpaint el seam que queda es casi siempre diferencia de exposición/tinte. Color-match explícito, no más blur.
2. **Drift global** — aun "keep the rest" recolorea; SIEMPRE composite-back con el mask. A/B pixel-diff fuera del mask debe ser ~0.
3. **Mask sin feather** = línea dura. Mínimo 4px; pelo/vidrio/humo necesitan matting, no mask de 1-bit (ver [[60-edicion-imagen-avanzada-ia]] §matting).
4. **Resolución del mask ≠ imagen** — reescalar mask con interpolación bilineal introduce gris en el borde que el modelo trata como "edita a medias". Reescala con nearest o regenera el mask a resolución target.
5. **Outpaint de un salto grande** alucina (inventa edificios, manos): incremental siempre.
6. **VAE roundtrip recolorea** todo levemente en latent models (FLUX/SDXL) → otra razón para composite-back en pixel space, no en latent.

## Serving (handler de cola)
- Input: `image_url`, `mask_url` (o puntos/bbox → genera mask server-side con SAM, ver [[186-object-removal-replace]]), `prompt`, `feather_px`, `padding_px`.
- Crop→inpaint→composite-back→color-match dentro del worker; devuelve solo el resultado final.
- **Warm-state**: mantén el inpaint model en VRAM entre jobs (cold-start de 24GB FLUX-Fill es caro, ver [[113-network-volume-modelos-grandes]]).
- Idempotencia por hash(image+mask+prompt+seed) para no re-generar.

Cruza con [[60-edicion-imagen-avanzada-ia]], [[183-flux-kontext-editing-deep]] y [[186-object-removal-replace]].
