# 147 — Formato vertical a fondo: componer para 9:16 de verdad

> Verificado a **agosto de 2026**. Las medidas de píxeles son estables; las zonas de interfaz cambian
> (ver `45`). Lo de composición no caduca: es lenguaje visual, no especificación técnica.

## El malentendido que arruina la mitad de los videos

La gente cree que vertical es "horizontal recortado". No lo es. **Es otro idioma.**

Un plano horizontal cuenta con lo que hay **al lado** del sujeto: el contexto, el fondo, la relación entre
dos personas. Un plano vertical no tiene lados. Tiene **arriba y abajo**. Todo lo que quieras contar
tiene que caber en una columna.

Consecuencia inmediata: **el plano general no existe en vertical.** Un plano abierto del bar en 9:16 es
una tira estrecha donde no se entiende nada. Si quieres mostrar el lugar, muéstralo en pedazos:
la barra, la cara del que sirve, el vaso, la mesa llena.

---

## Los números

| Formato | Píxeles | Proporción | Dónde |
|---|---|---|---|
| **9:16** | 1080 x 1920 | 0,5625 | Reels, TikTok, Shorts, Stories |
| **4:5** | 1080 x 1350 | 0,8 | Feed de Instagram y Facebook |
| **1:1** | 1080 x 1080 | 1,0 | Grid del perfil, feed antiguo |
| **16:9** | 1920 x 1080 | 1,78 | YouTube largo, televisión |

De 16:9 a 9:16 hay un salto brutal. Los números:

```
Un fotograma 4K horizontal:  3840 x 2160  =  8.294.400 px
Recorte a 9:16 manteniendo alto:  1215 x 2160  =  2.624.400 px

Sobrevive el 31,6 %.  Se pierde el 68,4 % de la imagen.
```

**Cuando recortas un 16:9 a vertical, tiras dos tercios de lo que grabaste.** No es una conversión, es una
amputación. Y decidida después, sin poder ver lo que había.

---

## Dónde va el sujeto en vertical

### La regla del tercio superior

En 9:16, **el ojo entra por arriba**. La zona de abajo está comida por la interfaz (caption, botones,
CTA de anuncios). Entonces:

```
        0
        ├──────────────────┤  ← 250 px: zona muerta (interfaz)
        │                  │
   250  ├──────────────────┤
        │                  │
        │   ★ AQUÍ VA      │  ← 250 a 900: la zona de oro
        │     LA CARA      │     Los ojos del sujeto entre
        │     (ojos ~600)  │     y = 500 y y = 750
   900  ├──────────────────┤
        │                  │
        │   TEXTO / MANOS  │  ← 900 a 1480: acción secundaria
        │                  │
  1480  ├──────────────────┤
        │                  │
        │  ZONA MUERTA     │  ← 1480 a 1920: no pongas nada aquí
  1920  └──────────────────┘
```

**Los ojos del sujeto van alrededor de y = 550–700**, es decir, más o menos al 30–35 % desde arriba. Es el
equivalente vertical de la regla de tercios, y es lo que hace que un plano se sienta "bien" sin que sepas
por qué.

Si pones la cara centrada verticalmente (y = 960), el video se siente vacío arriba y la cara queda tapada
por el caption cuando la persona baja la vista.

### El sujeto en horizontal: centrado, sí

En el eje horizontal, **centra**. En 9:16 no hay espacio para composiciones descentradas elegantes; el
ancho es de 1080 px y los iconos de TikTok se comen 165 de la derecha. Un sujeto descentrado a la derecha
queda debajo de los botones.

Excepción: si vas a poner texto grande a un lado, descentra el sujeto al lado contrario. Pero entonces
verifica que en TikTok no quede bajo los iconos.

### El fondo importa el doble

En vertical hay tan poco ancho que **el fondo está pegado al sujeto**. Un fondo desordenado en horizontal
se disimula; en vertical te grita.

Para el bar: fondo con profundidad (una fila de botellas desenfocadas, luces al fondo) funciona muchísimo
mejor que una pared plana. Y **evita las líneas horizontales fuertes** detrás del sujeto (el borde de la
barra, un estante): en 9:16 cortan el encuadre en dos y el ojo se atora.

---

## Qué se pierde exactamente al recortar de 16:9

| Lo que pierdes | Ejemplo en tu bar | Qué hacer |
|---|---|---|
| **El contexto lateral** | Se ve la cerveza pero no que está en el bar | Meter un plano de contexto aparte |
| **La relación entre dos personas** | Dos amigos brindando no caben | Grabar el brindis en primerísimo plano |
| **El movimiento lateral** | Alguien caminando sale del cuadro en medio segundo | Grabar el movimiento hacia cámara, no de lado |
| **Los rótulos y letreros** | El letrero de "Bendita Pola" no cabe | Grabarlo aparte, vertical |
| **La profundidad de campo lateral** | La barra larga se ve como un palito | Cambiar el ángulo: grabar a lo largo de la barra |

**Regla general: cuanto más abierto el plano, peor sobrevive el recorte.** Un primer plano de una cara
recorta bien. Un plano general de un salón no recorta, se destruye.

---

## Cómo recortar cuando no tienes más remedio

A veces solo tienes material 16:9. Estas son las opciones, de mejor a peor.

### 1. Recorte con movimiento (lo mejor)

En vez de recortar fijo, **haces un paneo dentro del fotograma**: la ventana vertical se mueve dentro del
16:9 siguiendo la acción. Se siente como un movimiento de cámara real.

```bash
# Ventana vertical que se desplaza de izquierda a derecha en un clip de 5 s
ffmpeg -i horizontal.mov -vf \
"crop=w=ih*9/16:h=ih:x='(iw-ih*9/16)*(t/5)':y=0,scale=1080:1920" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy -y vertical_pan.mp4
```

`x='(iw-ih*9/16)*(t/5)'` mueve la ventana desde el borde izquierdo al derecho a lo largo de 5 segundos.
Cambia el `5` por la duración de tu clip.

### 2. Recorte fijo, decidido a mano

No aceptes el centro por defecto. Mira el plano y decide.

```bash
# Recorte fijo desplazado: la ventana empieza en x=900 del 16:9 original
ffmpeg -i horizontal.mov -vf "crop=1215:2160:900:0,scale=1080:1920" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy -y vertical_fijo.mp4
```

Para encontrar el `x` correcto, saca un fotograma con la retícula:

```bash
ffmpeg -ss 2 -i horizontal.mov -vf "drawbox=x=900:y=0:w=1215:h=2160:color=lime:t=8" \
  -frames:v 1 -y prueba_recorte.png
```

Abre el PNG y mueve el `x=900` hasta que el sujeto quede donde lo quieres.

### 3. Sujeto arriba, texto o gráfico abajo

Metes el 16:9 arriba (ocupa 1080x608) y llenas el resto con fondo de marca, texto grande, o un segundo
plano. **Funciona bien** y se ve intencional, no como un recorte de emergencia.

```bash
ffmpeg -i horizontal.mov -f lavfi -i color=c=black:s=1080x1920:d=15 \
  -filter_complex "[0:v]scale=1080:608[v];[1:v][v]overlay=0:420" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy -y vertical_bloque.mp4
```

El `overlay=0:420` deja el video empezando en y=420: arriba queda espacio para un título y abajo para
texto grande. **Es mejor que el fondo desenfocado**, que se ve a plantilla de app gratuita.

### 4. Fondo desenfocado (lo último)

El video ampliado y borroso detrás del video normal. Se ve barato y ya se lee como "esto es reciclado".
Úsalo solo si no hay otra.

```bash
ffmpeg -i horizontal.mov -filter_complex \
"[0:v]scale=1080:1920,boxblur=30:5[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a copy -y vertical_blur.mp4
```

### Lo que nunca: barras negras

Un 16:9 con barras negras arriba y abajo en un feed vertical es la señal más clara de "no me importó".
Es la peor opción de todas.

---

## Cómo grabar pensando en vertical

Si vas a grabar de nuevo (y casi siempre puedes), estas son las decisiones que te ahorran todo lo anterior.

### 1. Graba en vertical, punto

El celular ya lo hace. Si tu cámara no, ponla vertical con un soporte. No hay premio por grabar horizontal.

### 2. Acércate

**La regla más útil: acércate el doble de lo que crees.** En vertical, el plano medio se lee como plano
general. Lo que en 16:9 sería un primer plano, en 9:16 es el plano normal.

Para el bar:
- El vaso llenándose **ocupando media pantalla**, no en una mesa a 2 metros.
- La cara de quien come **desde el pecho**, no de cuerpo entero.
- El plato **desde arriba, cerca**, no en el contexto de la mesa.

### 3. Mueve la cámara hacia adelante y atrás, no de lado

El movimiento lateral en vertical hace que el sujeto entre y salga en medio segundo. El movimiento hacia
adelante (acercarse) llena la columna y se siente potente.

### 4. Usa la profundidad vertical

Es la ventaja del formato: puedes tener **tres planos apilados**. Botella en primer plano abajo, cara al
medio, luces al fondo arriba. Eso en 16:9 no se puede.

### 5. Graba con margen si vas a poner texto

Si sabes que va a haber texto grande en el tercio inferior, **no pongas nada importante ahí al grabar**.
Deja mesa vacía, o suelo, o fondo.

### 6. Graba también la versión 4:5

Truco práctico: si compones el sujeto dentro del rectángulo central de **1080 x 1350**, el mismo material
sirve para 9:16 (con aire arriba y abajo) y para 4:5 (recortando) sin rehacer nada.

```
   1080x1920 (9:16)
   ┌──────────────┐
   │   aire       │  285 px
   ├──────────────┤
   │              │
   │  1080x1350   │  ← compón AQUÍ
   │    (4:5)     │
   │              │
   ├──────────────┤
   │   aire       │  285 px
   └──────────────┘
```

Combina esto con la zona segura de `45` y tienes una sola composición que sirve para las tres redes y para
la pauta.

---

## Verificar que tu composición vertical funciona

### La prueba del pulgar

Mira tu video en el celular con el brazo estirado. Si a esa distancia no distingues qué es lo importante,
tu sujeto está demasiado lejos.

### La prueba del primer fotograma

```bash
ffmpeg -i vertical.mp4 -frames:v 1 -y primer_frame.png
```

Ábrelo. **¿Se entiende qué es sin leer nada?** Si no, tu gancho visual no existe.

### La prueba de las tres interfaces

Superpón las zonas muertas y mira si tu sujeto sobrevive:

```bash
ffmpeg -i vertical.mp4 -vf \
"drawbox=x=0:y=0:w=1080:h=250:color=red@0.4:t=fill,\
drawbox=x=0:y=1480:w=1080:h=440:color=red@0.4:t=fill,\
drawbox=x=900:y=0:w=180:h=1920:color=red@0.4:t=fill" \
  -c:v libx264 -crf 23 -preset fast -pix_fmt yuv420p -c:a copy -y prueba_zonas.mp4
```

---

## Errores comunes

- **Creer que vertical es horizontal recortado.** Es otro idioma.
- **Usar planos generales.** En 9:16 un plano abierto no cuenta nada.
- **Poner la cara al centro vertical.** Va al tercio superior, ojos alrededor de y=600.
- **Descentrar el sujeto a la derecha.** Ahí van los iconos de TikTok.
- **Fondo con una línea horizontal fuerte detrás del sujeto.** Corta el encuadre en dos.
- **Recortar en el centro por defecto.** Mira cada plano y decide dónde recortar.
- **Barras negras.** La peor opción posible.
- **Fondo desenfocado como solución estándar.** Se lee como plantilla de app gratis.
- **Grabar movimiento lateral.** El sujeto sale del cuadro en medio segundo.
- **Grabar lejos.** En vertical hay que acercarse el doble.
- **Grabar sin dejar la zona inferior libre** cuando ya sabes que ahí va el texto.
- **No aprovechar la profundidad.** El vertical es el único formato donde puedes apilar tres planos.
- **Componer sin pensar en el 4:5.** Compón dentro de 1080x1350 y te sirve para todo.

---

## Checklist

### Al grabar
- [ ] Grabé **en vertical**, no horizontal para recortar después.
- [ ] Estoy **el doble de cerca** de lo que me pareció suficiente.
- [ ] El sujeto está **centrado horizontalmente** y en el **tercio superior** verticalmente.
- [ ] Los **ojos** quedan alrededor del 30–35 % desde arriba.
- [ ] El movimiento de cámara es **hacia adelante/atrás**, no lateral.
- [ ] El fondo tiene **profundidad** y no tiene líneas horizontales fuertes detrás del sujeto.
- [ ] Dejé **libre el tercio inferior** para el texto.
- [ ] Compuse el sujeto dentro del rectángulo **1080x1350**, para que sirva también en 4:5.

### Al montar
- [ ] Si recorté de 16:9, **decidí el recorte a mano**, plano por plano.
- [ ] Si tuve que rellenar, usé **bloque de color con texto**, no fondo desenfocado.
- [ ] **Cero barras negras.**
- [ ] Verifiqué con `prueba_zonas.mp4` que nada importante cae bajo la interfaz.
- [ ] Saqué el **primer fotograma como PNG** y se entiende solo.
- [ ] Hice la **prueba del pulgar**: se distingue lo importante con el brazo estirado.
- [ ] El export es **1080x1920 exacto**, sin escalados raros.
