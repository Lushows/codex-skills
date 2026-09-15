# 46 — Dirección de arte para imágenes con IA (que se vean intencionales y caras)

La diferencia entre "AI slop" y una imagen de campaña no está en el modelo, está en cuántas DECISIONES de
dirección tomaste. Un prompt genérico deja que el modelo promedie millones de imágenes mediocres; tú impones
intención. **El error #1: describir el SUJETO y olvidar describir la FOTO** (cámara, luz, encuadre, película).
Piensa como director: sujeto + composición + luz + óptica + color + atmósfera + referencia de estilo.

## Composición
Vocabulario que MJ v7 / FLUX.2 / Nano Banana Pro / Seedream 4 / Reve / Recraft V3 obedecen: `rule of thirds`,
`negative space`, `centered composition`, `leading lines`, `frame within a frame`, `low/high/dutch angle`,
`over-the-shoulder`, `eye-level`. **El negative space es el truco de lujo #1:** aire alrededor del sujeto =
editorial, no "render de stock". `generous negative space, subject in lower-left third`.

## Iluminación (aquí se gana/pierde el realismo)
`golden hour`, `blue hour`, `rim/back/kicker light`, `side light`, `softbox/soft diffused`, `hard light with
sharp shadows`, `chiaroscuro`, `Rembrandt lighting` (triángulo bajo el ojo), `loop`, `butterfly/paramount`,
`practical lights` (lámparas/neón dentro de la escena), `volumetric/god rays`, `motivated lighting`. **Una luz
nombrada vence a "iluminación bonita" siempre.**

## Color
Disciplina de paleta = lujo. `limited palette`, `monochromatic teal`, `complementary orange and teal`,
`analogous`, `muted earth tones`, `desaturated`, + grading: `color graded`, `filmic`, `crushed blacks`, `warm
highlights cool shadows`. **Looks de película:** `Kodak Portra 400` (piel cálida, suave), `CineStill 800T`
(halación roja, nocturno), `Kodak Ektar` (saturado nítido), `Fuji Pro 400H` (verdes suaves), `Ilford HP5` (B&N grano clásico).

## Óptica y cámara
`35mm` (reportaje), `50mm` (natural), `85mm` (retrato, compresión, bokeh), `macro`, `tilt-shift`, `24mm wide`,
`anamorphic` (bokeh oval, flares horizontales), `shallow DoF`, `f/1.4`, `creamy bokeh`, `deep focus`. `shot on Hasselblad/Phase One` empuja a medio formato.

## Atmósfera & referencias de estilo
`film grain`, `atmospheric haze`, `morning fog`, `dust particles in light`, `light leaks`, `subtle vignette`. El
grano sutil es el antídoto #1 contra el look "plástico digital". **Referencias:** `in the style of Annie
Leibovitz / Peter Lindbergh / Gregory Crewdson / Saul Leiter`, `Wes Anderson symmetry`, `film noir`, `1970s
editorial`. Una referencia concreta colapsa la ambigüedad mejor que 10 adjetivos.

## Ejemplo
> *Editorial portrait of a woman in a linen suit, seated, eye-level 85mm, shallow DoF f/1.8, Rembrandt lighting
> from a window, warm practical lamp behind as kicker, muted earth-tone palette, shot on Kodak Portra 400, subtle
> film grain, generous negative space on the right, in the style of Peter Lindbergh.*

## Gotchas
- **Piel de plástico:** añade `natural skin texture, visible pores, fine skin detail` + film stock; baja stylize (`--s 100`, no 600+).
- **Sobre-saturación/HDR:** `muted, desaturated, filmic, soft contrast` o sale "calendario de banco".
- **Simetría artificial:** la IA ama centrar → `off-center, candid, asymmetric composition`.
- **Manos/texto rotos:** para TEXTO usa **Ideogram 3.0** o **Nano Banana Pro** (mejores en tipografía 2026); para manos, inpaint localizado > re-roll completo.
- **Luz incoherente:** sombras que no coinciden con la fuente → especifica UNA dirección de luz dominante.
- **Bokeh falso (recortes duros):** `optical depth of field` + focal length real.
- **Marca:** define un *style token* fijo (paleta hex + film stock + focal length + tipo de luz) y reúsalo verbatim; en MJ guarda un `--sref` propio.

**Fuentes:** docs.midjourney.com · bfl.ai (FLUX.2) · deepmind.google/models/gemini-image · ideogram.ai · recraft.ai.
