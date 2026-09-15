# 176 · Editar expresión y mirada de un retrato

> A veces no quieres otra cara ni más nitidez: quieres **la misma persona, sonriendo**, o **mirando a cámara** en vez de al lado.
> Editar expresión/gaze de un retrato fijo es retargeting facial: mover ojos y boca conservando identidad, pose y fondo.

## Qué es (y qué no)
- **Sí**: cambiar apertura de ojos, dirección de mirada, apertura/forma de boca, sonrisa, micro-pose de cabeza — sobre **una foto estática**.
- **No**: animar (eso es lip-sync/talking-head, otro bloque) ni cambiar identidad (eso es swap/IP-Adapter). Aquí la persona **no cambia**, solo su gesto.

## Herramienta de referencia: LivePortrait
Aunque LivePortrait se vende como animador foto→video, su módulo de **stitching & retargeting** sirve para **edición de un solo frame**:
- **Control regional**: driving por *expresión, pose, labios, ojos* o *todo*. Puedes tocar solo ojos sin alterar la boca.
- **Eye retargeting**: módulo dedicado de redirección de ojos; un *multiplier* gradúa cuánto se mueven. Controla **gaze** (a dónde mira) y apertura de párpados.
- **Lip retargeting**: abre/cierra/forma la boca; opción "keep lip silent" para forzar boca neutra.
- **Stitching**: re-pega el recorte editado sobre la imagen original → fondo y cuerpo intactos, solo cambia la cara.

Dos MLP (ojos y labios) permiten dosificar cada región de forma independiente → ediciones sutiles sin el efecto "muñeco".

## Parámetros que mueven la aguja

| Control | Efecto | Cuidado |
|---|---|---|
| eyes retargeting multiplier | apertura/dramatismo de ojos | alto → mirada saltona, "asustado" |
| gaze / pupila | a dónde mira | desalinear con la pose = bizco/inquietante |
| lip retargeting | forma de boca/sonrisa | sobre-abrir = dientes artefactuados |
| stitching on/off | re-pega en original | off → costura visible en el cuello |

## Cómo encaja en el pipeline
- Va **después** de fijar identidad (swap/IP-Adapter) y **antes** de la restauración final:
  editas gesto → restauras nitidez (`[[148-face-restoration-output-avatar]]`,
  `[[175-face-enhance-beautify]]` con fidelity alto para no perder lo ajustado).
- Para retratos generados con difusor donde "salió serio" y querías sonrisa, esto evita
  re-generar (y re-tirar el dado de la identidad).
- Transferencia de expresión más amplia (de un video driver completo) →
  `[[120-liveportrait-expression-transfer]]`.

## Driving: foto vs valores explícitos
Dos formas de manejar a LivePortrait para un frame:
- **Driving image**: pasas una cara de referencia con la expresión deseada → copia su gesto.
  Cómodo pero arrastra rasgos de la referencia si no usas solo la región.
- **Driving por valores** (retargeting params): mueves ojos/boca con sliders, sin segunda
  foto. Más control fino y reproducible; ideal para ajustes sutiles y batch.

Para edición de marca consistente, prefiere valores explícitos: son auditables y repetibles.

## Límites (cuándo no usarlo)
- Cambios **grandes** de pose de cabeza → empieza a deformar; mejor regenerar con ID-preservation.
- Ojos cerrados → abiertos con poca info → mirada artificial. El módulo inventa la pupila.
- Caras pequeñas o de baja resolución → el retargeting amplifica el ruido; restaura primero.

## Serving
- VRAM modesta; LivePortrait corre en GPUs pequeñas. El costo es marginal frente a la generación. Cachea pesos en el volumen (`[[113-network-volume-modelos-grandes]]`).
- Para un solo frame, una pasada; no necesitas la maquinaria de video segmentado.

## Riesgo legal — sutil pero real
Cambiar la **expresión** de una persona real puede falsear su intención: hacer que alguien "sonría" aprobando algo, o "mire a cámara" en un contexto que no consintió, es manipulación de imagen con potencial difamatorio/engañoso. Mismo régimen de likeness, consentimiento y etiquetado de contenido sintético que el resto del bloque. Ver `[[39-legal-ia-generativa]]` y `[[165-moderacion-safety-output-generado]]`.

Cruza con [[120-liveportrait-expression-transfer]], [[148-face-restoration-output-avatar]] y [[175-face-enhance-beautify]].
