# 53 — Motion graphics & tipografía cinética sobre video IA

Texto y gráficos son cómo marcas, clarificas y das energía al footage IA — y, convenientemente, cómo cubres frames débiles.

## Principios de tipografía cinética
**Timing** es todo: el texto debe animar más rápido de lo que se lee (reveal snappy ~8-14 frames, hold más largo,
exit rápido). **Jerarquía** — una palabra/línea dominante; varía peso, tamaño y color para guiar el ojo. **Peso
como movimiento** — palabras más pesadas cargan más inercia; escalona la entrada de palabras para que la línea
"construya". **Trata el texto como objeto en movimiento, no caption estático pegado encima.**

## Toolkit
**After Effects** — estándar de la industria para motion bespoke (shape layers, graph editor para easing, plugins
Animation Composer/Motion Bro para presets). **Apple Motion** — rápido, template-driven. **Remotion** — escribe
video en React/TS y renderiza con browser headless; ideal para video **programático, data-driven, brand-templated**
a escala (perfecto al generar muchos clips de marca). **Lottie** — animaciones vectoriales (diseñadas en AE vía
Bodymovin) que corren como JSON liviano en web/app/CSS — logos animados y motion de UI, NO video full-frame.
**CapCut/Canva** — captions/templates rápidos. **ffmpeg drawtext** para texto quemado sin editor:
```bash
ffmpeg -i in.mp4 -vf "drawtext=fontfile=Inter-Bold.ttf:text='BIO-SETA':fontcolor=white:fontsize=64:\
x=(w-text_w)/2:y=h-160:box=1:boxcolor=black@0.4:boxborderw=20" out.mp4
```

## Elementos comunes
**Lower-thirds** (nombre/título), **title cards** (intro full-frame), **captions/subtitles**, **callouts/
annotations** (flechas, círculos, labels), **logo stings** (bumper de marca 2-4s).

## Captions — la tendencia dominante 2026
~80% del video social se ve EN MUTE → captions quemados son obligatorios para alcance. Auto-caption vía CapCut/
Opus Clip/Premiere Speech-to-Text/Whisper → SRT → quema:
```bash
ffmpeg -i in.mp4 -vf "subtitles=cap.srt:force_style='Fontname=Inter,Fontsize=22,Bold=1,Outline=2,Shadow=1,MarginV=120'" out.mp4
```
Mantén captions en la **action-safe zone** (~90% interior) y sobre la banda de UI de plataforma (el ~15% inferior de 9:16 lo tapan botones/handle).

## Easing
Movimiento lineal = robótico. **ease-out** para reveals (rápido in, settle suave), **ease-in-out** para moves. En
CSS `cubic-bezier(0.16,1,0.3,1)`; un toque de overshoot/spring da vida. **Animación de números** — count-up
odometers, barras/% animados (AE expressions, Remotion `interpolate()`, react-spring).

## Sistema de títulos consistente
Define una vez: fuentes de marca, color tokens, layout estándar de lower-third, logo sting, estilo de caption →
templatealo (AE Essential Graphics `.mogrt`, o librería de componentes Remotion). Reusa, no rediseñes por clip.

## Gotchas
1. Texto ilegible — siempre scrim/stroke/drop-shadow detrás del tipo sobre footage IA ocupado.
2. Demasiado busy — anima una cosa a la vez; movimientos que compiten se cancelan.
3. Fuentes/colores off-brand destruyen cohesión — lockea un sistema.
4. **Safe areas** — texto fuera de la action-safe se recorta en distintos aspect ratios o se oculta tras UI.
5. `drawtext` necesita la RUTA completa de la fuente y caracteres especiales (`:`, `'`, `%`) escapados o falla.
6. El filtro `subtitles` quema a la resolución FUENTE — escala el video primero, luego quema, o los tamaños de fuente quedan mal.
7. Lottie no renderiza video IA fotográfico — es solo vector; no lo uses para full-frame.

**Fuentes:** remotion.dev/docs · lottiefiles.com/what-is-lottie · ffmpeg.org/ffmpeg-filters (drawtext/subtitles).
