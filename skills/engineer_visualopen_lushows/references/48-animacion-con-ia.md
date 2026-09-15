# 48 — Animación con IA: dar movimiento a imágenes fijas y personajes

**Regla de oro: movimiento sutil = premium; movimiento exagerado = barato.** Un fijo de calidad con
micro-movimiento (pelo que ondea, vapor que sube, parpadeo, parallax leve) se lee como caro y controlado. El
error del principiante es pedir demasiado movimiento y obtener uncanny warping.

## Base: image-to-video
Toda animación premium hoy parte de un still bien dirigido + i2v (Kling, Runway Gen-4, Luma, Hailuo). Describe
*qué* se mueve y *cuánto*, no la escena entera.

## Motion control (separa pro de amateur)
- **Motion brush (Runway) / Motion Control (Kling):** pintas qué región se mueve y en qué dirección. Animas solo el agua, dejas el resto quieto = cinemagraph.
- **Trajectory/drag:** defines la trayectoria de un objeto (Kling, Pika).
- **Cámara vs sujeto:** sepáralos. Fija el sujeto y mueve solo la cámara (orbit) = look de producto premium; o al revés.

## Animación de personaje
- **Talking avatars / lip-sync:** **HeyGen**/**Synthesia** (comercial plug-and-play); **HunyuanAvatar** y
  **LongCat-Video-Avatar 1.5** (open, lip-sync + gestos desde audio, auto-hospedable en RunPod); **OmniHuman**
  (ByteDance, foto+audio→cuerpo entero hablando). Drive = un audio; boca/cara/gestos se generan.
- **Cuerpo entero / danza / gesto:** OmniHuman, LongCat-Avatar (gestos corporales), pose-driven.
- **Pose/driving-video:** **Act-One (Runway)** y **DreamActor** transfieren la actuación de un video de referencia (tu cara/cuerpo actuando) al personaje generado. La forma más expresiva de animar performance.

## Loops y atmósfera
- **Cinemagraphs / seamless loops:** un solo elemento en movimiento (humo/agua/neón) sobre escena estática. `seamless loop` o ensambla con first=last frame.
- **Parallax / 2.5D desde un still:** separa capas (fg/mid/bg) con velocidades distintas → profundidad desde una sola foto. Runway/Luma vía `slow dolly`.
- **Partículas/atmósfera:** `floating dust, drifting fog, falling snow, embers` — micro-movimiento que da vida sin romper.

## Ejemplo (cinemagraph de producto)
> *Static locked-off shot, product jar on marble, only the steam rising and slowly curling, everything else
> perfectly still, soft window light, seamless loop.*

**Stop-motion:** `stop-motion claymation style, on-twos, slight jitter` para estética Laika/Aardman.

## Gotchas
- **Drift:** rasgos del personaje se deslizan con el tiempo → clips cortos, baja intensidad, frame inicial muy nítido.
- **Uncanny / ojos muertos:** lip-sync que no llega a los ojos → usa modelos con gesto+mirada (LongCat-Avatar, OmniHuman), no solo boca.
- **Manos y dientes:** lo primero que se rompe al hablar/gesticular → encuadres que oculten manos o planos más cerrados.
- **Costuras de loop:** el salto frame final→inicial se nota → first=last frame o crossfade corto en post.
- **Sobre-animación:** si todo se mueve, todo se ve falso → aísla UN elemento con motion brush.
- **Desync de audio:** en lip-sync, audio limpio sin música encima de la voz mejora la sincronía.

**Fuentes:** runwayml.com (Motion Brush, Act-One) · klingai.com · heygen.com · github.com/Tencent-Hunyuan/HunyuanVideo-Avatar · omnihuman-lab.github.io.
