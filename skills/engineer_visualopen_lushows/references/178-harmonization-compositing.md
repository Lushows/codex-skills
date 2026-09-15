# 178 · Harmonization de compositing (color/luz match de un sujeto pegado en otro fondo)

> Pegaste un cutout en un fondo nuevo y "canta": color, exposición y tono no casan.
> Harmonization = ajustar SOLO la apariencia del foreground (color/luz global) para que pertenezca a la escena, sin tocar su forma ni identidad.

## Harmonization ≠ relight
No confundir: **relight** (IC-Light, [[177-ic-light-relight-serving]]) recalcula iluminación direccional y sombras propias del sujeto. **Harmonization** es más superficial: alinea estadísticas globales de color/luminancia foreground↔background (white balance, exposición, contraste, tinte). Composite creíble = harmonization **+** relight **+** sombra, en ese orden conceptual. Harmonization sola arregla el "recorte pegado de Photoshop", no la dirección de luz incoherente.

## El estado del arte (2026)
- **Encoder-decoder pixel-to-pixel** (la línea clásica desde Deep Image Harmonization, CVPR'17) — aprende la transformación composite→armonizado [verificado].
- **Dual color space** (RGB + Lab desacoplado) — separa luminancia/cromaticidad, alivia el trabajo del RGB enredado; fuerte en color cast [verificado, ACM MM'23].
- **Difusión**: DiffHarmony++ (Harmony-VAE) y zero-shot con prior de difusión — calidad alta, más caro [verificado].
- **Adaptive-Interval Color Transformation** — harmonization de **alta resolución** vía curvas de color aprendidas (barato a 4K, no a nivel-píxel) [verificado, NeurIPS'24].
- **Painterly** (ProPIH/FreePIH): caso aparte — pegar foto real en pintura/ilustración, matchea *estilo* no solo color.

## Pipeline de producción
1. **Cutout con alpha** + máscara del foreground (la harmonization necesita saber QUÉ región ajustar).
2. **Estima estadísticas del background** alrededor de la zona de pegado (no la imagen entera — la luz es local).
3. **Modelo de harmonization** sobre el composite + máscara → foreground re-coloreado. A alta-res usa el de curvas (color transform) para no perder detalle.
4. **Match de grano/ruido y blur de lente**: el harmonizer no lo hace; añade grano del background y DoF coherente o el tell persiste.
5. **Feather del borde + pasada low-denoise** en la costura.

## Atajos sin red neuronal (cuando el sujeto es simple)
- **Reinhard color transfer** (transferir media/desv de color del bg al fg en Lab) — rápido, decente para casos suaves; rompe en sujetos con color propio fuerte.
- **Match de histograma por canal** limitado a la máscara.
- **Curva de exposición/WB manual** guiada por un parche neutro del bg.
Úsalos como baseline; sube a red aprendida cuando canta.

## Serving / costo
- Modelos de harmonization son **ligeros** (encoder-decoder pequeño) → corren en CPU/GPU modesta, sub-segundo. No necesitas A100.
- Los basados en difusión SÍ pesan; resérvalos para hero shots, no para catálogo masivo.
- Pipeline típico: matting (escala) → harmonization barata (escala) → relight+difusión solo en hero.

## Gotchas
1. **Sin máscara precisa** el harmonizer sangra el ajuste al fondo o deja halo — depende del alpha (basura entra, basura sale).
2. **Estadísticas globales ≠ luz local**: si el sujeto está en una esquina sombreada, promediar todo el bg lo deja sobre-iluminado; muestrea local.
3. **Harmonization no arregla dirección de luz** — un sujeto iluminado por la izquierda sobre fondo iluminado por la derecha seguirá mal; eso es relight.
4. **Color transfer clásico mata el color de marca** (un frasco rojo se "lava" hacia el bg) → protege la zona de identidad con máscara.
5. **Alta-res a nivel-píxel** es lento y artefacta; usa curvas/color-transform aprendido para 4K.

Cruza con [[177-ic-light-relight-serving]] y [[60-edicion-imagen-avanzada-ia]].
