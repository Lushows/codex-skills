# 50 — Storyboard y planificación de shots para video IA

Los profesionales planean ANTES de generar porque cada re-roll cuesta créditos y tiempo. La diferencia entre un
video IA caótico y uno dirigido está toda en la pre-producción. Flujo: **brief → guion/voz → storyboard → shot list → generación → ensamble.**

## 1. Creative brief
Una frase de objetivo (qué siente/hace el espectador), audiencia, plataforma, duración, tono, referencias visuales. Sin brief, cada plano apunta distinto.

## 2. Guion / voiceover PRIMERO
En anuncios/explainers, **escribe la voz antes que la imagen.** La narración define el ritmo, el nº de planos y la
duración de cada uno. Con Veo 3 (audio nativo) o TTS (ElevenLabs), genera la voz primero y edita imágenes contra ella. (~150 wpm → 30s ≈ 75 palabras.)

## 3. Storyboard (thumbnails por plano)
Dibuja —o **genera con IA**— un frame clave por plano (MJ/Nano Banana/FLUX, mismo character sheet para
consistencia). Esos boards son DOBLE valiosos: comunican la idea Y *son* los start frames para i2v. Tools: **LTX
Studio** y **Katalist** generan storyboards completos con personajes consistentes.

## 4. Shot list
Una fila por plano: `# | shot type | camera move | duración | descripción/acción | audio`.

| # | Plano | Cámara | Dur | Contenido |
|---|---|---|---|---|
| 1 | Establishing wide | Static | 3s | Cabaña al amanecer, niebla |
| 2 | Medium | Slow dolly-in | 4s | Mujer abre la ventana |
| 3 | Close-up | Static | 2s | Manos sostienen taza humeante |

**Una idea por plano.** Si un plano necesita dos acciones, son dos planos.

## 5. Continuidad (reglas que la IA ignora si no las impones)
- **Eyeline match** (hacia dónde mira) · **regla de los 180°** (cámara de un lado de la línea de acción para no
  invertir la geografía) · **screen direction** (si va a la derecha, sigue a la derecha) · **match on action**
  (corta en mitad de un gesto). Las consigues fijando el lado de la luz y la dirección de movimiento en cada prompt.

## 6. Ritmo por plataforma
**TikTok/Reels:** cortes rápidos (1-2s), hook en el 1er segundo, 9:16, acción inmediata. **YouTube:** planos más
largos (4-8s), respiración, 16:9. **Anuncio/branded:** arco de 15-30s, beat de producto claro, CTA final. Diseña la duración de cada clip según esto (recuerda: 5-10s nativos máx).

## 7. B-roll
Lista aparte de planos de apoyo (detalles, texturas, atmósfera) para cubrir cortes y dar respiro. Baratos de generar, salvan el montaje.

## 8. Board → prompts
Cada viñeta = (a) prompt de imagen para el start frame (sujeto+comp+luz+óptica+estilo), (b) prompt de video con el
movimiento de cámara de la shot list. El board resolvió el "qué"; el prompt de video solo añade el "cómo se mueve".

## Gotchas
- **Generar sin plan:** re-rolls infinitos quemando créditos. El board barato evita el video caro.
- **Saltarse continuidad:** luz/dirección cambia entre planos y el montaje se siente roto → fija lado de luz y screen direction en cada prompt.
- **Planos demasiado ambiciosos:** dos acciones en un clip = morphing → divídelo.
- **Ignorar la duración nativa:** planear un plano de 15s que el modelo no genera → bloques de 5-10s.
- **Voz e imagen desfasadas:** editar imagen primero y meter voz después descuadra el ritmo → voz primero.
- **Sin b-roll:** te quedas sin material para cortar y el montaje se siente rígido.

**Fuentes:** runwayml.com/research · ltx.studio · katalist.ai · studiobinder.com (guías de storyboard).
