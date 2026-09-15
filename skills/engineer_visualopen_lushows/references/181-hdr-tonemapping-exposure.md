# 181 · HDR / tone-mapping / exposición para output de generativos

> Los modelos generativos escupen LDR sRGB 8-bit ya "tonemapeado" — plano, con highlights quemados y sombras tapadas.
> Recuperar rango dinámico y aplicar una curva de tono correcta es lo que da el "pop" fotográfico que el output crudo no tiene.

## El problema con el output crudo
Difusión genera en sRGB de 8 bits: highlights clippeados a 255 (sin detalle en lo blanco), sombras aplastadas, gama comprimida. No hay datos lineales ni rango extendido. Para look pro necesitas: (a) expandir/recuperar rango, (b) aplicar tone-mapping deliberado, (c) controlar exposición — en vez de aceptar la curva implícita del modelo.

## Conceptos que hay que separar
- **HDR real**: ≥10-12 bits, datos lineales de luminancia escena-referida. El gen NO lo da nativo.
- **Tone-mapping**: mapear ese rango (real o simulado) a display LDR con una curva. Donde vive el "look".
- **Exposición**: multiplicar la imagen lineal por un factor ANTES de tonemapear (sube/baja brillo sin clippear como lo haría un brightness LDR).
- **Exposure fusion**: combinar varias exposiciones (bracket) en una sola bien expuesta — sin pasar por HDR lineal.

## Operadores de tone-mapping (elige el look)
| Operador | Carácter | Uso |
|---|---|---|
| **Reinhard** | suave, neutro, local; tras multiplicar por exposición [verificado] | base segura, fotográfico natural |
| **ACES Filmic** | rolloff de highlights cinematográfico; estándar en motores/cine [verificado] | look "film", highlights cremosos |
| **Hable/Uncharted2** | filmic con shoulder/toe ajustables | control fino de pies/hombros de curva |
| **AgX** | moderno, manejo de color saturado sin viraje de tinte | highlights coloreados (neón, fuego) |

ACES es la curva por defecto en Unreal y la referencia de cine [verificado]. Reinhard para neutro; ACES/AgX para look.

## Recuperar/simular HDR desde un gen LDR (2026)
- **UltraFusion** (2025): fusión de exposiciones que modela el proceso como **inpainting guiado** por la sub-expuesta; tono natural incluso en rango altísimo, supera HDR-Transformer [verificado]. Útil si generas un bracket sintético.
- **Bracket diffusion / X2HDR**: generar/expandir a HDR vía denoising consistente o espacio perceptualmente uniforme [verificado].
- **Truco práctico sin red**: genera el mismo prompt/seed con 2-3 exposiciones (vía prompt de luz o post-curvas) y fusiónalas → recuperas detalle en cielo/highlights que una sola toma clippea.

## Pipeline en post de generativos
1. **Linearizar** (de-gamma sRGB → lineal) antes de cualquier ajuste de luz; operar en gamma da color cast.
2. **Exposición**: multiplica en lineal para nivelar (clave para batches con brillo dispar).
3. **Tone-map**: aplica el operador elegido (ACES/Reinhard). Aquí cae el look.
4. **Re-gamma** a sRGB / Rec.709 para entrega; o exporta 16-bit si va a grading posterior ([[52-color-grading-look-cinematografico]]).
5. **Trabaja en 16-bit float** todo el pipeline; recién al final baja a 8-bit → evitas banding.

## Gotchas
1. **Ajustar brillo en sRGB (no lineal)** introduce color shift y aplasta tono; siempre linealiza primero.
2. **Highlights ya clippeados a 255** NO se recuperan post — el dato no existe; debes generar bracket o re-promptear con menos exposición.
3. **Banding en gradientes** (cielos) por operar en 8-bit → mantén 16-bit hasta el export final.
4. **Doble tone-mapping**: el gen ya tonemapeó; si aplicas ACES encima a ciegas, sobre-comprimes → lavado. Considera de-tonemapear/linearizar antes.
5. **Tinte en highlights saturados** (Reinhard vira neón a blanco) → usa AgX/ACES para luces de color.
6. **Monitor sin perfil** te engaña; valida en sRGB calibrado o el look no traslada.

Cruza con [[52-color-grading-look-cinematografico]] y [[60-edicion-imagen-avanzada-ia]].
