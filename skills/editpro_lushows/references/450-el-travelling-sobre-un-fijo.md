# 450 — El travelling sobre un fijo

Un montaje hecho de fotos, recortes y capturas no tiene cámara. Tiene una **imagen grande y una
ventana que se pasea por ella**. Ese paseo es el travelling sobre un fijo, y es el recurso que
sostiene el 90% de un documental de archivo, de un carrusel convertido en vídeo o de cualquier pieza
donde el material no se mueve solo.

`226` es movimiento de cámara **con cámara**: peso, inercia, operador. Esto es lo contrario: no hay
física que respetar, hay una cuenta que hacer. `83` explica *por qué* una imagen fija mata un vídeo;
este módulo es el **modelo geométrico** del recurso y el reparto de sus tres gestos.

---

## 1. El modelo: ventana, lienzo y margen

`zoompan` recorta una ventana de `iw/zoom` × `ih/zoom` de la imagen de entrada y la escala al tamaño
de salida (`s=`). De ahí salen las tres cantidades que gobiernan todo:

| Cantidad | Fórmula | Qué significa |
|---|---|---|
| Ventana | `iw/z` × `ih/z` | lo que se ve en cada fotograma |
| Recorrido disponible | `iw·(1 − 1/z)` | cuánto se puede desplazar sin salirse del lienzo |
| Ampliación efectiva | `salida / (iw/z)` | píxeles de salida por píxel de fuente |

Con una fuente de 2688 px y `z = 1,12`, el recorrido disponible es `2688 · (1 − 1/1,12) = 288` píxeles
de fuente. Traducido a pantalla (2688/1,12 = 2400 de ventana → 1920 de salida, factor 0,80) son
**230 píxeles de recorrido**, ni uno más. Pedir 400 deja ver el borde del lienzo: eso es `456`.

**La consecuencia que nadie calcula:** el zoom no solo acerca, también **compra recorrido**. Sin zoom
(`z = 1`) el recorrido disponible es exactamente cero. Un travelling lateral limpio necesita o bien
una fuente más ancha que el lienzo, o bien un zoom mínimo del que colgarse.

---

## 2. Los tres gestos y lo que dicen

| Gesto | Expresión de `z` | Lo que el espectador entiende |
|---|---|---|
| **Empuje** (acercarse) | `1+r/nf*on` | «entra aquí», «mira esto», compromiso |
| **Apertura** (alejarse) | `1+r − r/nf*on` | «hay más», contexto, consecuencia, soledad |
| **Deriva** (desplazarse) | `z` fijo, `x`/`y` móviles | tránsito, inquietud, plano de apoyo |

`on` es el índice del fotograma de salida, `nf` el total de fotogramas del plano y `r` el recorrido en
tanto por uno. Escribir el zoom en función de `on` —y no de `zoom`, el valor del fotograma
anterior— es lo que hace que el gesto **acabe exactamente donde dijiste** aunque cambie la duración.

```bash
# Empuje del 12% sobre un plano de 6,73 s a 25 fps  (nf = 168)
ffmpeg -hide_banner -y -loop 1 -framerate 25 -t 6.730 -i foto_2688.png \
  -filter_complex "[0:v]zoompan=z='1+0.00071429*on':d=1:\
x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,format=yuv420p[out]" \
  -map "[out]" -frames:v 168 -c:v libx264 -crf 18 -preset veryfast plano.mp4
```
`0.00071429` es `0,12 / 168`. Esa división es todo el módulo: **el coeficiente sale de la duración, no
del gusto**.

### La deriva diagonal, que es la que mejor funciona

Un empuje centrado es simétrico y el ojo lo lee como «zoom». Un desplazamiento diagonal, no: lo lee
como cámara. El motor del canal documental lo resuelve moviendo el centro respecto a la mitad del
plano, de modo que el recorrido queda repartido a ambos lados:

```bash
zoompan=z='1+0.00059524*on':d=1:\
x='iw/2-(iw/zoom/2)+(on-84)*2.1':y='ih/2-(ih/zoom/2)-(on-84)*0.85':s=1920x1080:fps=25
```
`(on-84)` vale −84 al principio y +84 al final: el plano entra ya desplazado a un lado y sale por el
otro. Los factores 2,1 y 0,85 son píxeles de fuente por fotograma; cuánto es eso en pantalla y qué
velocidades son legibles, en `451`.

---

## 3. El recorrido: entre el 8% y el 16%

La regla viva de un canal de archivo con 60+ planos medidos:

| Recorrido | Cómo se lee |
|---|---|
| < 5% | no se percibe. El plano sigue pareciendo congelado |
| **8% – 16%** | **respiración. Se siente vivo y nadie mira el movimiento** |
| 18% – 25% | intencionado. Un remate, una revelación, un golpe |
| > 35% | marea, y delata la resolución de la fuente |

Fuera de esa banda solo se sale **a propósito y con motivo**: el golpe de entrada de un bloque
(`z` que cae del 1,22 al 1,00 en un 16% de la duración), o un travelling largo declarado como tal.

---

## 4. Cómo se elige el gesto

Tres preguntas, en este orden:

1. **¿Qué hay dentro del cuadro que merezca acercarse?** Si la respuesta es «nada concreto», no es un
   empuje: es una deriva.
2. **¿El plano abre o cierra un bloque?** Los que abren piden apertura (dan contexto); los que cierran
   piden empuje (concentran).
3. **¿Qué hizo el plano anterior?** Dos empujes seguidos se detectan; tres, cansan. El reparto sano en
   una secuencia larga es alternar familias, y eso es `38` en `canales_lushows`.

**El gesto nunca se elige por el archivo, se elige por la frase que suena encima.** Un retrato puede
pedir apertura si la voz está diciendo que ese hombre estaba solo.

---

## 5. La comprobación antes de renderizar

Antes de gastar minutos de CPU, saca el primer y el último fotograma y míralos juntos:

```bash
ffmpeg -hide_banner -y -loop 1 -i foto_2688.png -vf \
"zoompan=z='1+0.00071429*on':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,\
select='eq(n\,0)+eq(n\,167)',tile=2x1" -frames:v 1 -fps_mode vfr extremos.png
```
Si en esos dos fotogramas no ves diferencia, el recorrido es demasiado corto. Si en el último se ve
una franja vacía, te pasaste de deriva (`456`). Los dos fallos se cazan aquí, en dos segundos, y no
después de renderizar el episodio entero.

---

## Errores frecuentes

1. **Pedir deriva con `z = 1`.** El recorrido disponible es cero: la imagen no se mueve y ffmpeg no
   avisa de nada.
2. **Escribir `z` en función de `zoom`** (el valor del fotograma anterior) y esperar que el gesto
   termine en un valor concreto. Acumula error; usa `on`.
3. **Calcular el coeficiente «a ojo»** en vez de dividir el recorrido entre el número de fotogramas.
   Al cambiar la duración del plano el gesto se descuadra en silencio.
4. **Empuje centrado en todos los planos.** Es el acento de vídeo hecho con plantilla.
5. **Recorrido por debajo del 5%.** Cuesta lo mismo renderizarlo y no sirve para nada.
6. **Confundir esto con estabilizar o con mover la cámara de verdad.** Son `59` y `226`, otro oficio.
7. **Elegir el gesto mirando la foto y no escuchando la frase.**

---

## Relacionado

- `451` — cuánto recorrido por segundo es legible: el mismo 12% en 4 s y en 12 s no es lo mismo
- `455` — las trampas de `zoompan`: `d`, `crop` que no se anima, `eq` sin `eval=frame`
- `456` — el margen que hay que reservar para no enseñar el borde del lienzo
- `458` — lo que cuesta en minutos de render cada decisión de este módulo
- `83` — por qué una imagen fija se lee como avería, y las formas de animarla de verdad
- `226` — movimiento de cámara **real**, en rodaje: otro problema, otras reglas
- `canales_lushows/30` y `/38` — el repertorio cerrado de gestos y su reparto a lo largo de un episodio
