# 52 — Color grading & el look cinematográfico para clips IA

## Correction vs grading
**Color correction** = arreglar la realidad: neutralizar WB, exposición, matchear clips a un baseline correcto
(rec.709). **Color grading** = el look creativo encima: mood, paleta, firma emocional. **Corrige primero, gradea
después** — gradear sobre footage roto compone errores. Con clips IA importa DOBLE: cada clip llega con su propio WB/contraste random.

## Primary vs secondary
**Primary** = todo el frame (lift/gamma/gain, exposición, WB). **Secondary** = regiones aisladas vía **HSL
qualifier** (solo la piel, solo el cielo), masks, power windows. En **DaVinci Resolve** (free tier es full pro):
usa el **node graph** — N1 balance/exposición, N2 contraste/curves, N3 LUT creativa, N4 secondaries (piel/cielo), N5 grano/halación, nodo paralelo para vignette. Non-destructivo y re-ordenable.

## Scopes — confía en ellos, no en tus ojos (tu monitor miente)
**Waveform** = distribución de luma; deja los negros fuera de 0 y blancos fuera de 100 salvo intención. **Parade**
(RGB waveforms) = WB; alinea las bases de R/G/B para negros neutros. **Vectorscope** = hue/sat; la **skin-tone line** (~11 en punto, la I-line) es sagrada — la piel debe sentarse ahí sin importar el look.

## LUTs
**Técnicas** convierten color spaces (Log→Rec709). **Creativas** imponen un look. Aplica técnica primero, gradea,
luego LUT creativa — y baja la creativa a 50-70% de opacidad (las LUTs crudas son heavy-handed). Film-emulation
(Kodak 2383, Fuji 3513) en built-ins de Resolve, Dehancer, FilmConvert. Construye looks con **lift-gamma-gain**, **curves** (la S-curve suave es el workhorse de contraste), y HSL para targeted.

## Color theory
**Teal-orange** — piel cálida, sombras frías; default del blockbuster moderno (sobreusado — restraint).
Complementarias para tensión, análogas para armonía, monocromo para mood. **Ancla en la piel primero**, diseña el resto alrededor.

## El look "caro" (3 cosas DESPUÉS de gradear)
**Film grain** (sutil, animado — mata el sheen plástico digital y, clave, enmascara el banding/artefactos de IA),
**halation** (sangrado rojo/naranja cálido alrededor de luces, imita film stock), **bloom** (glow suave en luces).
Estas 3 son por qué los clips IA se ven baratos sin ellas. En Resolve: nodo de grano + nodo glow/bloom + OFX de halación.

## Matchear clips (la tarea core de IA, porque los clips varían)
Elige un **hero clip** de referencia, abre scopes lado a lado, matchea blacks/whites en el waveform, luego mids,
luego usa el vectorscope para matchear piel, luego aplica la *misma* LUT creativa a todos. "Shot Match" de Resolve te lleva al 70%; termina a ojo en scopes.

## ffmpeg grading (rápido/batch)
`ffmpeg -i in.mp4 -vf lut3d=look.cube -c:a copy out.mp4` · `eq=contrast=1.1:brightness=0.02:saturation=1.15` ·
`curves=preset=increase_contrast`. Usa Resolve para grading real; ffmpeg para normalización batch de muchos clips IA. **SDR Rec.709 por default** para web/social (HDR lo maltratan plataformas/viewers).

## Gotchas
1. Aplastar negros a 0 puro destruye detalle de sombra y bandea — deja unos IRE.
2. Skin tone fuera de la I-line del vectorscope = enfermizo/quemado — guárdalo sobre todo.
3. Over-grading: si grita "filtro", baja 30%.
4. **Banding** en cielos/gradientes — añade grano/dither sutil; gradea en alta profundidad de bits.
5. `lut3d` espera el color space de input correcto — meter Rec709 a una LUT Log se ve mal.
6. Gradear clip por clip en vez de desde una referencia garantiza una secuencia mal-matcheada y amateur.

**Fuentes:** blackmagicdesign.com/products/davinciresolve · ffmpeg.org/ffmpeg-filters (lut3d).
