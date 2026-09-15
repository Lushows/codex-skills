# 199 · Video por keyframes / first-last-frame (FLF2V)

> Le das el primer frame y el último; el modelo inventa el camino entre ambos. Control de
> composición exacto en los extremos, libertad en el medio. La forma más barata de dirigir una toma.

## Qué es FLF2V
First-Last-Frame-to-Video (Wan 2.1/2.2 FLF2V): provees `first_image` y `last_image` + prompt
opcional, y el modelo interpola una trayectoria de movimiento coherente entre los dos. No es morphing
ciego: entiende el contenido y construye una transición física plausible (un objeto que se desplaza,
una cara que cambia de expresión, un producto que rota).

## Por qué importa para producción
- **Composición garantizada en los extremos**: el cliente aprueba dos frames fijos; tú controlas
  exactamente dónde empieza y termina la toma. Sin lotería de t2v.
- **Encadenable**: el último frame de un clip = primer frame del siguiente → secuencias largas
  consistentes (base de [[200-video-extension-looping]]).
- **Más barato que dirigir con controles densos**: solo dos imágenes vs pose/depth por frame.

## Pipeline (ComfyUI, Wan 2.2 FLF2V)
1. Preparar/generar `first` y `last` (mismo estilo, resolución y aspecto — críticos).
2. Nodo FLF2V Wan: first + last + prompt + nº frames + longitud.
3. (Opcional) **Frame interpolation** (RIFE/FILM) al final para subir FPS y suavizar.

## Dónde brilla y dónde falla
| Funciona bien | Falla / degrada |
|---|---|
| Transformación continua simple (caminar de A→B, push-in, rotar producto) | Acción multi-paso (caminar → girar → sentarse) entre keyframes lejanos |
| Cambio de expresión, day→night, abrir/cerrar | Cambios de identidad o topología grandes (alucina el intermedio) |
| Loops (first == last) | Movimientos con oclusión fuerte sin pistas |

- Regla: **un solo "gesto" por par de keyframes**. Si necesitas tres acciones, usa tres pares
  encadenados, no un par con tres cosas.

## Detalles que muerden
- **Coherencia first↔last**: si difieren mucho en iluminación/encuadre/estilo, el intermedio se
  vuelve inestable o hace un "salto". Genera ambos del mismo seed/pipeline cuando puedas.
- **Distancia semántica**: keyframes muy distintos = interpolación pobre. Acércalos o mete un
  keyframe intermedio (multi-keyframe encadenado).
- **Resolución/aspect idénticos** en first y last, si no el modelo deforma para cuadrar.
- **Nº de frames vs velocidad**: más frames = movimiento más lento/suave; menos = brusco. Calibra
  según la distancia del gesto.
- **Memoria**: hay variantes "low memory" (Civitai v1.4) si la GPU no aguanta el 14B a 720p.

## FLF2V vs alternativas
- **FLF2V**: control en extremos, medio libre. Para tomas dirigidas con composición fija.
- **VACE** ([[198-vace-control-video-deep]]): control denso por frame (pose/depth). Más control, más
  trabajo y coste.
- **SVD/AnimateDiff img2video** ([[151-animatediff-svd-image-to-video]]): solo primer frame, final
  libre. Menos control, bueno para movimiento ambiental.

Cruza con [[122-wan-video-self-hosting-2026]] y [[151-animatediff-svd-image-to-video]].
