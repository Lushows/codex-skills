# 263 — Integrar un elemento

**Qué resuelve:** ya tienes el elemento recortado y colocado, y **se ve pegado**. Este módulo es el
paso 4 del compositing: los seis ajustes que hacen que deje de verse pegado, en orden de rendimiento,
con el comando exacto de cada uno y **cómo medir el número en vez de adivinarlo**.

> El módulo `204` te dice **qué** hay que igualar. Este te dice **cómo se mide y con qué comando**. Si
> ya leíste `204`, ve directo a la sección 2.

---

## 1. El orden por rendimiento (no por perfección)

Si solo tienes cinco minutos, haz los tres primeros y para. Dan el 80%.

| # | Ajuste | Tiempo | Cuánto aporta | Dónde |
|---|---|---|---|---|
| 1 | **Sombra de contacto** | 2 min | ★★★★★ | CapCut o ffmpeg |
| 2 | **Nivel y temperatura** | 2 min | ★★★★★ | CapCut o ffmpeg |
| 3 | **Grano encima de todo** | 1 min | ★★★★☆ | ffmpeg (CapCut lo hace mal) |
| 4 | **Desenfoque igualado** | 2 min | ★★★☆☆ | CapCut o ffmpeg |
| 5 | **Luz de borde** | 5 min | ★★★☆☆ | ffmpeg |
| 6 | **Movimiento compartido** | 10 min | ★★☆☆☆ | `264` |

La sorpresa para casi todo el mundo: **la sombra vale más que el borde**. Puedes tener un recorte
mediocre y un plano creíble si el elemento proyecta sombra. Puedes tener un recorte perfecto y un plano
imposible si el elemento flota.

---

## 2. Sombra de contacto: el truco de mayor rendimiento

> **Sombra de contacto:** la mancha oscura, difusa y corta que aparece justo donde un objeto toca una
> superficie. No es la sombra proyectada larga: es la manchita del punto de apoyo.

Es lo que le dice al cerebro **dónde está el objeto en el espacio**. Sin ella, todo flota.

**En CapCut** (para un texto, un logo o un PNG): con el elemento seleccionado, panel derecho, busca
**Sombra** en las opciones de texto o de superposición. Los cuatro controles:

- **Difuminado / Blur**: alto. Una sombra de contacto es difusa, nunca dura.
- **Distancia**: baja. 5 a 15 px. Si la subes mucho, parece una calcomanía con relieve de PowerPoint.
- **Ángulo**: apuntando **al lado contrario de donde viene la luz en el video**. Míralo en el video: si
  la cara está iluminada desde la izquierda, la sombra va a la derecha.
- **Opacidad**: 25% a 45%. Más que eso se ve sucio.

**En ffmpeg**, para un PNG con alfa. La receta: extraes el canal alfa, lo difuminas, lo bajas de nivel,
lo vuelves negro, y lo pones **debajo** del elemento, desplazado:

```bash
ffmpeg -y -i fondo.mp4 -i elemento.png -f lavfi -i "color=c=black:s=400x400" \
  -filter_complex "\
[1:v]format=rgba,split=2[el][a];\
[a]alphaextract,gblur=sigma=14,lutyuv=y='val*0.55'[sa];\
[2:v][sa]alphamerge[sombra];\
[0:v][sombra]overlay=x=320+16:y=700+22[bg];\
[bg][el]overlay=x=320:y=700[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p integrado.mp4
```

Los tres números que ajustas: `sigma=14` (qué tan difusa), `val*0.55` (qué tan oscura), y el
desplazamiento `+16 / +22` (hacia dónde y qué tan lejos). El `color=black:s=400x400` tiene que ser
**del mismo tamaño que tu PNG**.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** El tamaño del `color=` debe coincidir
> con el del elemento o `alphamerge` falla. Pruébalo con `-frames:v 1` y mira el PNG antes de renderizar
> el video completo.

**La regla de oro de la sombra:** si dudas, **más difusa y más suave** de lo que crees. Una sombra
demasiado marcada delata el efecto más que no tener sombra.

---

## 3. Nivel y temperatura: medir en vez de adivinar

El elemento casi siempre viene más brillante, más saturado y más frío que el plano. Se arregla en dos
minutos si mides.

### Cómo medir el plano

```bash
# Estadísticas del fondo: brillo mínimo, medio y máximo
ffmpeg -v error -i fondo.mp4 -vf "signalstats,metadata=print:file=stats_fondo.txt" -t 2 -f null -
```

En el archivo buscas `YMIN`, `YAVG`, `YMAX`. Y lo mismo para tu elemento:

```bash
ffmpeg -v error -i elemento.png -vf "signalstats,metadata=print:file=stats_elem.txt" -f null -
```

**Lo que estás comparando:**

- **YMIN** — el negro más oscuro. Si el fondo tiene YMIN 32 y tu elemento tiene YMIN 0, tu elemento
  tiene negros más profundos que el plano: se ve recortado. **Es el error más común y el más delator.**
- **YMAX** — el blanco más claro. Si tu elemento llega a 255 y el fondo a 210, tu elemento brilla más de
  lo que la escena permite.
- **YAVG** — el brillo general.

### Cómo corregir

**Subir los negros** del elemento para que coincidan con el plano (lo que más se nota):

```bash
# El elemento tiene negros a 0 y el plano los tiene a 32
ffmpeg -y -i elemento.png -vf "format=rgba,colorlevels=rimin=0:gimin=0:bimin=0:romin=0.125:gomin=0.125:bomin=0.125" elemento_niv.png
```

`0.125` es 32/255. Ese solo ajuste hace que el elemento "entre" en la escena de una manera que sorprende.

**Temperatura** — si el plano es cálido (luz de bombillo) y el elemento es neutro:

```bash
# Valores en Kelvin: por debajo de 6500 = más cálido, por encima = más frío
ffmpeg -y -i elemento.png -vf "colortemperature=temperature=4200:mix=0.8" elemento_calido.png
```

**Saturación y contraste** — casi siempre hay que **bajarle** al elemento:

```bash
ffmpeg -y -i elemento.png -vf "eq=saturation=0.88:contrast=0.94:brightness=-0.02" elemento_apagado.png
```

> **La intuición correcta:** el elemento nuevo casi nunca hay que mejorarlo. **Hay que empeorarlo** para
> que se parezca al plano. Menos contraste, menos saturación, menos nitidez, negros más altos. Todo lo
> que un principiante haría al revés.

**En CapCut** esto se hace en **Ajustar** sobre el clip del elemento: Brillo, Contraste, Saturación,
Temperatura, Sombras (para levantar los negros). Los mismos ajustes, sin poder medir. Truco para no
adivinar: pon el elemento y el fondo lado a lado en pantalla partida durante el ajuste; el ojo compara
mucho mejor de lo que juzga en aislado.

---

## 4. Grano: el paso que amarra todo

El material de celular tiene ruido. El elemento generado por IA o el gráfico vectorial **no tiene
ninguno**. Esa diferencia de textura es una de las señales más fuertes de "esto está pegado", y casi
nadie la ve conscientemente.

**La regla que casi todos rompen: el grano va AL FINAL, sobre la mezcla completa, no sobre la capa.**
Si lo pones sobre el elemento y luego lo escalas, el grano se escala con él y queda del tamaño
equivocado. Y si va sobre la mezcla, unifica todas las capas de una sola vez, que es justo lo que
quieres.

### Medir cuánto grano tiene tu material

```bash
ffmpeg -v error -i fondo.mp4 -vf "bitplanenoise=bitplane=1,metadata=print:file=ruido.txt" -t 2 -f null -
```

No necesitas interpretar el número con precisión: te sirve para **comparar** el antes y el después.

### Aplicarlo

```bash
ffmpeg -y -i compuesto.mp4 -vf "noise=alls=7:allf=t+u" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p final.mp4
```

- `alls` — la fuerza. **5 a 10 para material de celular limpio.** 12 a 18 si el video es de noche y ya
  tiene ruido visible. Por encima de 20 se ve sucio a propósito.
- `allf=t+u` — `t` = temporal (el grano cambia en cada fotograma, que es como se comporta el ruido real)
  y `u` = uniforme. **Sin `t` el grano queda congelado y se ve como suciedad en el lente.** Es el error
  clásico.

**Truco de tamaño de grano.** El grano de ffmpeg es de un píxel. En un video 1080×1920 se ve demasiado
fino y la compresión de Instagram se lo come. Para un grano más gordo y que sobreviva la subida: aplica
el ruido en pequeño y escala.

```bash
ffmpeg -y -i compuesto.mp4 -filter_complex "\
[0:v]scale=540:960,noise=alls=9:allf=t+u,scale=1080:1920:flags=bilinear[g];\
[0:v][g]blend=all_mode=overlay:all_opacity=0.35" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p final.mp4
```

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** Es una receta agresiva: el `blend` en
> modo `overlay` también afecta el contraste. Prueba `all_opacity` entre 0.2 y 0.4 y quédate con el
> mínimo que se note.

**En CapCut:** hay filtros de "grano" y de "film" en la biblioteca de efectos. Funcionan, pero son
opacos (no controlas la fuerza con precisión) y algunos vienen con un tinte de color de regalo. Si el
video final pasa por ffmpeg, hazlo ahí.

---

## 5. Desenfoque: el elemento está demasiado nítido

En el video real, todo lo que no está en el plano de foco está algo suave. Un PNG pegado está
perfectamente nítido en toda su superficie. Eso, en un plano con fondo desenfocado, canta.

**Diagnóstico:** mira el fondo. ¿Se ve suave? Entonces tu elemento también tiene que estarlo.

```bash
# Suavizar el elemento antes de componerlo
ffmpeg -y -i elemento.png -vf "format=rgba,gblur=sigma=1.2" elemento_suave.png
```

`sigma` entre **0,8 y 2,5** para un elemento que está en el mismo plano que el sujeto. Más de 3 si
está claramente al fondo.

**El caso al revés, más frecuente de lo que parece:** el elemento viene borroso (una imagen chica que
escalaste) y el plano está nítido. Ahí toca el otro lado:

```bash
ffmpeg -y -i elemento.png -vf "format=rgba,unsharp=5:5:0.7:5:5:0.0" elemento_nitido.png
```

Pero sé honesto: **una imagen chica escalada no se arregla con nitidez**. Se ve nítida y falsa. Consigue
la imagen en tamaño grande.

**Desenfoque de movimiento.** Si el elemento se mueve rápido en el video y el resto de la escena tiene
borrón de movimiento, el elemento sin borrón se ve como un sticker. Truco barato con `tmix`, que promedia
fotogramas consecutivos:

```bash
ffmpeg -y -i elemento_animado.mov -vf "tmix=frames=3:weights='1 1 1'" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le elemento_mb.mov
```

Solo úsalo si el elemento se mueve rápido. En algo lento, `tmix` produce un rastro fantasma feo.

---

## 6. Luz de borde: el remate de lujo

> **Luz de borde (rim light):** el filo luminoso en el contorno de un objeto cuando hay luz detrás de
> él. Es la señal que más rápido hace que un recorte parezca filmado en ese sitio.

Si el fondo tiene una fuente de luz clara —una ventana, una lámpara, el cielo—, tu elemento debería
tener un filo de esa luz por ese lado. Casi nadie lo hace, y es de las cosas que más suman.

La receta en ffmpeg: duplicas el elemento, lo desplazas unos píxeles hacia la luz, lo pintas del color
de la luz, lo difuminas, y lo pones **debajo** del elemento. Solo asoma el borde.

```bash
ffmpeg -y -i fondo.mp4 -i elemento.png -f lavfi -i "color=c=0xFFE9C4:s=400x400" \
  -filter_complex "\
[1:v]format=rgba,split=2[el][a];\
[a]alphaextract,gblur=sigma=3[borde];\
[2:v][borde]alphamerge[luz];\
[0:v][luz]overlay=x=320-7:y=700-6[bg];\
[bg][el]overlay=x=320:y=700[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p con_luz.mp4
```

El desplazamiento `-7 / -6` es **hacia donde está la luz** en el fondo. El color `0xFFE9C4` es un
blanco cálido: cámbialo por el color real de la luz de tu escena.

**En CapCut** el equivalente barato: duplica la capa recortada, a la de abajo le subes el brillo al
máximo y la saturación a cero, la desplazas 6–8 px hacia la luz, y le bajas la opacidad al 40–60%. No es
lo mismo, pero sugiere lo mismo.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** Un rim light desplazado hacia el lado
> equivocado se ve mucho peor que no tenerlo. Mira dónde está la fuente de luz en el fondo antes de
> decidir el signo del desplazamiento.

---

## 7. Unificar: el paso final que casi nadie da

Después de todo lo anterior tienes un compuesto. **Ahora lo tratas como si fuera una sola toma.**

```bash
# Un solo pase sobre la mezcla ya terminada: grano + una pizca de grado + viñeta suave
ffmpeg -y -i compuesto.mp4 -vf "\
eq=contrast=1.03:saturation=1.02,\
vignette=PI/5,\
noise=alls=7:allf=t+u" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p final.mp4
```

La **viñeta** merece un párrafo aparte: oscurecer levemente las esquinas es el truco más viejo y más
efectivo para unificar capas. El ojo interpreta el oscurecimiento como una propiedad del lente, y si es
del lente, todo lo que está adentro fue filmado por ese lente. `PI/5` es sutil; `PI/4` ya se nota.

**En CapCut:** el equivalente es aplicar un filtro o un ajuste **a un clip compuesto** (agrupar y
ajustar), o exportar y volver a entrar. Es incómodo. Si tu flujo termina en ffmpeg, este pase va ahí.

---

## 8. La prueba final

```bash
# Antes y después, lado a lado, para ver si de verdad mejoró
ffmpeg -y -i sin_integrar.mp4 -i final.mp4 -filter_complex \
  "[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p comparacion.mp4
```

Míralo a tamaño de celular. Si con el comparativo al lado no distingues cuál es cuál, hiciste trabajo
invisible en el mal sentido: revísalo o quítalo.

Y la prueba del espejo de `260`: voltea el plano. Los errores de luz y borde saltan.

---

## Errores comunes

1. **Empezar por el borde y no por la sombra.** La sombra de contacto vale más que un recorte perfecto.
2. **Sombra demasiado marcada o demasiado lejos.** Difusa, corta, entre 25% y 45% de opacidad. Si dudas,
   más suave.
3. **Sombra apuntando al lado contrario de la luz.** Mira el video antes de decidir el ángulo.
4. **Adivinar los niveles en vez de medirlos.** `signalstats` te da YMIN/YMAX en 5 segundos.
5. **Dejar los negros del elemento en 0** cuando el plano los tiene en 32. Es el delator número uno y es
   el ajuste más fácil de todos.
6. **Mejorar el elemento en vez de empeorarlo.** Menos contraste, menos saturación, menos nitidez.
7. **Poner el grano sobre la capa y no sobre la mezcla.** Se escala con la capa y queda del tamaño
   equivocado; y no unifica nada.
8. **Grano sin la bandera `t` (temporal).** Queda congelado y parece mugre en el lente.
9. **Grano demasiado fuerte.** Instagram lo recomprime y se convierte en un bloque de basura. 5 a 10 es
   el rango sano.
10. **Elemento perfectamente nítido sobre fondo desenfocado.** Un `gblur=sigma=1.2` arregla el plano.
11. **Escalar una imagen chica y taparlo con nitidez.** Se ve nítida y falsa. Consigue la imagen grande.
12. **Usar `tmix` en un elemento que se mueve lento.** Produce rastro fantasma.
13. **Saltarse el paso de unificar.** Un pase de grano + viñeta sobre la mezcla amarra el plano y toma
    un minuto.
14. **No comparar el antes y el después.** Si no ves la diferencia, o no funcionó o no hacía falta.

---

## Checklist

Antes de dar por integrado un elemento:

- [ ] Tiene **sombra de contacto**: difusa, corta, en la dirección correcta, 25–45% de opacidad.
- [ ] **Medí** YMIN/YMAX del fondo y del elemento con `signalstats` en vez de adivinar.
- [ ] Los **negros del elemento** están al mismo nivel que los del plano.
- [ ] Igualé **temperatura** de color con la escena.
- [ ] Le **bajé** contraste, saturación y nitidez al elemento hasta que se pareció al plano.
- [ ] El **desenfoque** del elemento coincide con el de su plano de profundidad.
- [ ] Si hay una fuente de luz clara en el fondo, el elemento tiene **luz de borde** por ese lado.
- [ ] Apliqué **grano al final, sobre la mezcla completa**, con la bandera `t`, fuerza 5–10.
- [ ] Le puse una **viñeta suave** al compuesto para unificar.
- [ ] Comparé **antes y después** lado a lado, a tamaño de celular.
- [ ] Hice la **prueba del espejo** (`260`) y no salta ningún error de luz.
- [ ] Nada de esto me tomó más de 15 minutos en un reel (`269`).
