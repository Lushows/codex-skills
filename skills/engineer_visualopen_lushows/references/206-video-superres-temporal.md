# 206 · Super-resolución de vídeo temporalmente coherente (SeedVR2 / FlashVSR)

> Subir un vídeo de 540p a 4K sin que parpadee: cada frame debe mirar a sus vecinos, no upscalear solo.
> Un upscaler de imagen aplicado por-frame da nitidez pero **flicker**; el truco es la atención temporal.

## Por qué no sirve un upscaler de imagen
Real-ESRGAN/4x por frame trata cada uno aislado → detalles inventados que **cambian entre frames** =
hervor visible. Un VSR temporal procesa **ventanas de frames** con atención cruzada → el detalle es
consistente en el tiempo y el movimiento se ve suave.

## Los dos modelos open de 2026

| | **SeedVR2** (ByteDance) | **FlashVSR** |
|---|---|---|
| Arquitectura | difusión latente 1-paso (adversarial post-training) | difusión 1-paso **streaming**, atención dispersa local |
| Calidad | mayor fidelidad/detalle | comparable, ligeros artefactos de rejilla en zoom |
| Velocidad | más lento | **~3× más rápido**, pensado para tiempo real |
| Destino | hasta 4K, batch, máxima calidad | streaming/real-time, eficiente |
| Licencia | open, permisiva | open, permisiva |

Ambos one-step (no decenas de pasos de difusión) → viables en producción. SeedVR2 tiene integración
**ComfyUI** madura (540p→4K). Regla: **SeedVR2 para calidad final**, **FlashVSR para velocidad/streaming**.

## Cómo encaja
Es la **última etapa** de casi todo pipeline de vídeo: generas barato a baja resolución (avatar, restyle,
audio-reactive), validas, y sólo entonces pagas el upscale. Nunca generes a 4K nativo si puedes generar
a 540p y super-resolver — es órdenes de magnitud más barato.

## Lo que muerde
- **VRAM por ventana**: la atención temporal carga varios frames a la vez en VRAM. Clips largos → procesa
  en **chunks con solape** (p. ej. solape de 2-4 frames) y mezcla los bordes, o verás costura entre chunks.
- **Costura entre chunks**: sin solape, el límite de cada ventana salta. Solapa y promedia la transición.
- **One-step ≠ gratis**: sigue siendo difusión; presupuesta GPU Ampere+/Ada. FlashVSR baja el coste, SeedVR2 lo sube.
- **Artefactos de rejilla** (FlashVSR en primeros planos): si el sujeto es cara grande, prefiere SeedVR2.
- **No arregla movimiento roto**: VSR sube resolución, no corrige manos rotas ni flicker de contenido de
  la etapa anterior. Limpia el render **antes** ([[204-video-restyle-relight]]), no esperes que el VSR salve un mal vídeo.
- **Factor de escala**: 540p→4K es ~4×; saltos mayores inventan detalle. Encadena 2× dos veces si hace falta.

## Chunking con solape (la receta que evita costura)
```
clip largo → ventanas de N frames con solape de S (p. ej. N=16, S=4)
          → super-resolver cada ventana → mezclar (blend) los S frames de solape entre ventanas
          → concatenar
```
Sin solape, el borde de cada ventana salta (la atención temporal no ve más allá de su ventana). Con solape
y blend lineal en la transición, la costura desaparece. Ajusta N al límite de VRAM, S a 2-4 frames.

## Sizing y serving
- **VRAM** es el cuello: la atención temporal carga la ventana entera. Más frames por ventana = mejor
  coherencia pero más VRAM → balancea N contra tu GPU. SeedVR2 pide más que FlashVSR.
- One-step (no decenas de pasos) → latencia razonable, pero sigue siendo difusión: Ampere+/Ada mínimo.
- Pesos del modelo → **Network Volume** para no re-bajar en cada frío ([[113-network-volume-modelos-grandes]]).
- **Última etapa, gasto justificado**: aquí sí pagas resolución porque todo lo anterior fue barato a 540p.
  Cruza con [[30-finops-gpu]].

## Elegir en 30 segundos
Entrega final / cara grande / máxima fidelidad → **SeedVR2**. Streaming / lote enorme / latencia → **FlashVSR**.
Salto > 4× → encadena 2× dos veces, no un 8× de golpe (inventa detalle).

## Pipeline
```
generación barata (540p) → [validar contenido] → chunk+solape → SeedVR2 (calidad) | FlashVSR (velocidad)
                        → blend → 4K → entregar
```

Cruza con [[138-upscaling-restauracion-realtime-escala]].
