# 68 · Efectos que se ven baratos

**Qué resuelve:** la lista negra. Ninguno de estos efectos está prohibido por gusto:
todos comparten el mismo defecto y todos tienen sustituto. Si un plano necesita uno de
ellos, lo que necesita en realidad está en la columna de la derecha.

---

## Por qué se ven baratos

**Un efecto se ve barato cuando llama la atención sobre sí mismo.** El espectador deja
de mirar al detenido y mira el destello. Tres señales de que un efecto está en esa
categoría:

1. **Viene de fábrica.** Si es un preajuste que trae cualquier editor, lo han visto mil
   veces esta semana y su cerebro ya lo clasificó como "vídeo de relleno".
2. **No aporta información.** Un tachado dice *esto se anuló*. Un destello dorado no dice
   nada: es decoración, y la decoración en un documental se lee como que no hay material.
3. **Podría ir en cualquier plano.** Los efectos buenos sólo funcionan en el suyo. Si el
   efecto encaja igual en el minuto 1 y en el minuto 8, es papel pintado.

Hay una razón añadida, y no es estética: **la política de contenido no auténtico**. Un
episodio hecho de preajustes se parece a los otros diez mil episodios hechos de
preajustes. El collage cosido a mano es lo que hace que este canal no se confunda.

---

## La lista negra y su sustituto

| ❌ Efecto | Por qué falla | ✅ En su lugar |
|---|---|---|
| **Lens flare / destello anamórfico** | No hay lente: es un collage de papel. Delata el preajuste | Halo detrás del recorte, alfa ≤ 0,30 (`67`) |
| **Partículas doradas flotando** | Decoración pura, sin información | Lluvia de billetes en bucle, que sí dice algo (`61`) |
| **Zoom-blur de transición** | La transición de fábrica número uno del mundo | Corte duro; o el tachado rojo de marca (`77`) |
| **Rayos de sol / god rays** | Luz añadida sobre un fondo construido: no encaja con nada | Foco sustractivo: oscurecer alrededor (`67`) |
| **Bloom sobre todo el cuadro** | Empaña el collage y mata los negros del canal | Contraste local: subir el elemento, bajar el fondo (`21`) |
| **Glitch RGB genérico** | Dice "digital" en un canal cuyo material es papel | Textura VHS de verdad, con pérdida real de detalle (`66`) |
| **Lluvia de código / terminal verde** | Estética de otro nicho; envejeció mal | Rejilla técnica y tablero de datos (`54`) |
| **Contador con dígitos rodando en 3D** | Efecto de casino: quita seriedad a la cifra | Serie de estados con rampa ease-out (`61`) |
| **Degradado dorado con bisel en la tipografía** | Se lee como plantilla de miniatura de 2015 | Amarillo dato plano `#E8C547` sobre tinta (`42`) |
| **Sombra paralela dura sin difuminar** | El recorte flota como un adhesivo | Sombra de papel: 8-20 px de desenfoque y desplazada (`25`) |
| **Iconos planos y emojis** | Vocabulario de presentación de empresa | Objetos dibujados y rotulados (`60`) |
| **Chincheta roja de mapa** | Es el icono de Google Maps, y el mapa suele serlo también | Punto que late con rótulo, sobre trazado propio (`64`) |
| **Latido o pulso en todos los elementos** | Cuando todo late, nada destaca | Late sólo el que la voz nombra en ese segundo (`39`) |
| **Ken Burns siempre en la misma dirección** | El ojo lo detecta a los tres planos y se aburre | Cambiar de dirección entre planos (`38`) |
| **Flecha animada persiguiendo una ruta** | El extremo del trazo ya indica avance | `stroke-dasharray` sin punta (`64`) |
| **Barras de cine (letterbox) puestas de adorno** | Recorta 1080 a 800 sin ganar nada | Composición con márgenes reales (`28`) |
| **Marca de agua o logo fijo en la esquina** | Tapa cuadro 90 s para nada | Cierre de marca al final (`76`) |
| **Onda de audio decorativa** | Sólo tiene sentido si hay una grabación real que se cita | Cita en documento con máquina de escribir (`48`, `41`) |
| **Texto que rebota (elastic / bounce)** | Tono de dibujo animado en una historia de fraude | Golpe seco con ease-out corto (`31`, `47`) |
| **Fundido a negro entre cada bloque** | Mata el ritmo y suma 0,8 s muertos cada vez | Corte duro; el 90% van así (`70`) |

---

## Los tres casos límite

Hay efectos de la lista que **sí** entran, con condiciones estrictas:

| Efecto | Cuándo sí |
|---|---|
| **Flash blanco** | Sólo con algo fotografiable en pantalla, ≤ 0,22 s, máximo 3 por episodio, con su sonido (`67`) |
| **Glitch** | Sólo sobre material que de verdad es de vídeo (una cinta, una cámara de seguridad), nunca sobre papel |
| **Fundido a negro** | Sólo una vez por episodio: el salto temporal grande, y con el audio cruzando (`75`) |

La condición común es la misma en los tres: **el efecto tiene que estar justificado por
lo que se ve o por lo que se oye**, no por el montaje.

---

## Cómo se detecta uno metido por descuido

En la revisión, sobre la grilla de fotogramas (`ffmpeg -vf "fps=1/2,...,tile=6x4"`):

1. Buscar el fotograma donde **el ojo va a un sitio que no es el sujeto**. Ahí hay un
   efecto compitiendo.
2. Tapar mentalmente el efecto. Si el plano sigue contando lo mismo, el efecto sobra.
3. Preguntarse si ese plano podría ser de otro canal. Si la respuesta es sí, el efecto
   vino de fábrica.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Meter un efecto porque el plano "se ve vacío" | El hueco se rellena con ruido en vez de con información (`11`) |
| Justificar un preajuste con "es sólo un toque" | Un toque por plano son 45 toques por episodio |
| Usar glitch sobre un documento de papel | Contradice el material y rompe el idioma del canal |
| Copiar el efecto de un canal que funciona | Ese canal funciona por su material, no por su preajuste |

## Relacionado

`67` luz y destellos · `60` el criterio para que un efecto exista · `70` cuándo usar transición · `19` errores de ritmo · `25` el borde de papel
