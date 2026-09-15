# 51 — Transiciones y montaje de video (el oficio del corte para clips IA)

El editing convierte clips IA crudos en una película. La unidad atómica es el **corte**, y tu trabajo es hacerlo
invisible salvo cuando deba sentirse.

## Tipos de corte
**Hard cut** — A→B instantáneo, el default (90% de cualquier edit). **J-cut** — el audio de B empieza ANTES de su
imagen (oyes la siguiente escena antes de verla; clave para diálogo/VO). **L-cut** — el audio de A persiste sobre
la imagen de B. **J/L cuts = el mayor tell "pro vs amateur"** porque rompen el lockstep audio-video. **Match cut**
— continuidad gráfica/de movimiento (un círculo se vuelve un sol; la era IA los ama porque puedes promptear dos
clips con composición coincidente). **Jump cut** — mismo encuadre, tiempo removido (energético, esconde bien la
deriva temporal de IA). **Cross-cut/parallel** — intercalar dos lugares para implicar simultaneidad. **Smash cut** — salto abrupto de calma a caos.

## Transiciones (úsalas con moderación — un corte suele ser mejor)
**Dissolve/crossfade** = paso de tiempo/ensueño. **Fade in/out** (negro/blanco) = capítulos. **Whip-pan** — matchea
la dirección del motion blur entre cortes (clips IA que terminan en pan rápido empalman bellísimo). **Morph** (Runway/
AE Morph Cut/Resolve SpeedWarp) — genera first/last frames que compartan sujeto e interpola. **Luma/light-leak** y
**glitch** esconden saltos entre clips IA mal-matcheados. **Zoom transition** — entra a un punto brillante, sale del siguiente clip.

## El ritmo (Rule of Six, Walter Murch — orden de prioridad)
Emoción (51%), historia (23%), ritmo (10%), eye-trace (7%), plano 2D/stage-line (5%), continuidad espacial 3D (4%)
— **la emoción le gana a la lógica espacial siempre.** **Corta en acción** (a mitad de movimiento) para esconder el
corte. **Corta al beat** en piezas con música (markers en transients). Clips cortos = tensión/energía; planos
largos = calma/gravitas. **Varía** — el largo monótono adormece.

## Teoría del montaje
**Kuleshov:** el significado se fabrica ENTRE planos (cara neutral + sopa = hambre). **Eisenstein:** colisiona dos
planos para parir una tercera idea. Tu superpoder con IA: clips individualmente mediocres ganan significado por yuxtaposición.

## ffmpeg
```bash
# concat simple (mismo codec/res/fps) — list.txt: file 'a.mp4'\nfile 'b.mp4'
ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4
# crossfade (offset = dónde empieza la transición en el timeline de A)
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "xfade=transition=fade:duration=1:offset=4" -c:v libx264 -pix_fmt yuv420p out.mp4
```
Transiciones xfade: `fade, fadeblack, fadewhite, wipeleft/right, slideleft, circlecrop, radial, dissolve,
pixelize`. Audio: `acrossfade=d=1`. Easing GLSL extra: scriptituk/xfade-easing.

## Seamless loops
Crossfade la cola sobre la cabeza (el punto de loop invisible): trim, luego `xfade` los últimos N frames sobre los
primeros N — o genera el clip i2v con first=last frame idénticos. Verifica reproduciendo 3× buscando un "pop".

## Gotchas
1. `xfade` exige ambos inputs **misma resolución, fps y pixel format** — escala/convierte fps primero o da error/stutter.
2. `offset` es tiempo absoluto en A, no "desde el final" — mal cálculo recorta el fade.
3. `-c copy` concat falla en silencio con codecs distintos → re-encode.
4. Cruzar la línea de 180° entre dos clips IA desorienta; voltea uno si hace falta.
5. **Sobre-transicionar grita amateur** — si notas la transición, está mal.
6. Loops que no matchean la *velocidad* de movimiento en la costura hitchean aunque los frames coincidan.

**Fuentes:** ffmpeg.org/ffmpeg-filters · ottverse.com (xfade) · github.com/scriptituk/xfade-easing.
