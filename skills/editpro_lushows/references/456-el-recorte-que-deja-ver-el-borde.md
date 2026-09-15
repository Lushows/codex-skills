# 456 — El recorte que deja ver el borde

Dos fallos distintos que se confunden porque salen a la vez: el **fondo** se mueve tanto que aparece
una franja vacía en el canto del cuadro, y el **recorte superpuesto** se sale del lienzo y pierde la
cara del protagonista. Los dos son cuestión de margen, y los dos se miden antes de renderizar.

---

## 1. El margen del fondo: cuánto recorrido te da el zoom

`zoompan` recorta una ventana de `iw/z` × `ih/z`. El desplazamiento posible sin salirse es:

> **Recorrido disponible = `iw · (1 − 1/z)` píxeles de fuente**, y lo mismo en vertical con `ih`.

| Fuente | z | Ventana | Recorrido disponible (fuente) | En pantalla (salida 1920) |
|---:|---:|---:|---:|---:|
| 2688 | 1,05 | 2560 | 128 px | 96 px |
| 2688 | 1,12 | 2400 | 288 px | 230 px |
| 2688 | 1,25 | 2150 | 538 px | 480 px |
| 3840 | 1,12 | 3429 | 411 px | 230 px |

Dos lecturas que cambian el trabajo:

- **Con `z = 1` el recorrido disponible es cero.** Una deriva sin zoom no se mueve; simplemente
  ffmpeg satura la coordenada y el plano se queda clavado, sin un solo aviso.
- **Subir la resolución de la fuente no compra recorrido en pantalla.** 2688 y 3840 con el mismo zoom
  dan los mismos 230 px: el recorrido en pantalla depende solo del zoom.

### Un caso medido: la deriva que no ocurría

La deriva diagonal de un motor de montaje real pide `x = iw/2 − iw/z/2 + (on − nf/2)·2,1` sobre 168
fotogramas, con el zoom creciendo del 1,00 al 1,10. Es decir: pide arrancar 176 px a la izquierda del
centro cuando el zoom todavía es 1 y el recorrido disponible es **cero**.

| `on` | zoom | x pedida | x máxima | x real |
|---:|---:|---:|---:|---:|
| 0 | 1,000 | −176,4 | 0,0 | 0,0 ← saturada |
| 42 | 1,025 | −55,4 | 65,6 | 0,0 ← saturada |
| 84 | 1,050 | 64,0 | 128,0 | 64,0 |
| 126 | 1,075 | 182,0 | 187,5 | 182,0 |
| 167 | 1,099 | 295,8 | 243,0 | 243,0 ← saturada |

**En 100 de los 168 fotogramas (el 60%) la coordenada estaba saturada.** Y se ve en el render: la
diferencia media entre fotogramas consecutivos se queda en 0,45 durante el primer tercio —solo el
zoom—, sube a 1,09 en el centro y vuelve a caer. La deriva solo ocurre de verdad en el tercio de en
medio. ffmpeg no dijo nada: `zoompan` recorta la coordenada al rango válido y sigue.

**La comprobación que lo caza:** para cada fotograma, `0 ≤ x ≤ iw·(1 − 1/z)`. Cuatro líneas de Python
antes de renderizar, y ninguna sorpresa después.


### La verificación en dos fotogramas

```bash
ffmpeg -hide_banner -y -loop 1 -i fondo_2688.png -vf \
"zoompan=z='1+0.00071429*on':d=1:x='iw/2-(iw/zoom/2)+(on-84)*2.1':y='ih/2-(ih/zoom/2)':\
s=1920x1080:fps=25,select='eq(n\,0)+eq(n\,167)',tile=2x1" \
-frames:v 1 -fps_mode vfr extremos.png
```
Sale un PNG de 3840×1080 con el primer y el último fotograma pegados. Si hay franja, hay franja. Dos
segundos de cómputo frente a los minutos que cuesta el plano entero (`458`).

---

## 2. El margen del recorte: la sangría

Un recorte que asoma un poco por el canto se lee como **página que se sale**, que es el lenguaje del
collage. Uno que se sale mucho es un elemento cortado, y el ojo distingue las dos cosas al instante.
La constante que gobierna eso es la sangría: cuánto se le permite salirse por cada borde, en tanto por
uno del lienzo.

Medido sobre un episodio real de 61 elementos colocados, contando cuántos acaban con **más del 12% de
su superficie fuera del lienzo** de 1920×1080:

| Sangría | Elementos fuera (>12%) | El peor |
|---:|---:|---:|
| 0,000 | 0 | — |
| **0,022** | **0** | — |
| 0,040 | 8 | 16% fuera |
| 0,070 | 12 | **25% fuera** |
| 0,120 | 22 | **33% fuera** |

El salto está entre 0,022 y 0,040: **por debajo de un 2,5% del lienzo no hay ningún elemento
maltratado; a partir del 4% empiezan a aparecer, y al 7% son doce.** Con 0,070 el peor caso perdía un
cuarto de su superficie, y ese cuarto es exactamente la cara del retrato, porque la sangría se aplica
por el lado donde el elemento no cabía.

**Por qué 0,022 y no cero:** con sangría cero todo queda encajado dentro, pero los elementos se apilan
contra los bordes y el cuadro pierde el aire de collage. Ese 2,2% (42 px en horizontal, 24 en
vertical) es justo lo que hace falta para que un recorte muerda el canto sin perder nada legible.

### El umbral del 12%

No cualquier salida es un fallo. El auditor avisa a partir del 12% de la superficie del elemento fuera
del lienzo, porque por debajo de ahí lo que se pierde es fondo o margen del recorte, no contenido.
La cuenta es el área de la intersección con el lienzo dividida por el área propia:

```python
dentro_x = max(0, min(c[2], 1920) - max(c[0], 0))
dentro_y = max(0, min(c[3], 1080) - max(c[1], 0))
fuera = 1 - (dentro_x * dentro_y) / ((c[2]-c[0]) * (c[3]-c[1]))
```

---

## 3. Encajar en vez de descartar

Cuando un elemento no cabe en la posición declarada hay dos salidas, y solo una conserva la densidad
del cuadro: **correrlo hacia dentro hasta que quepa** en lugar de tirarlo.

```python
x = min(max(x, -mx), W - ancho + mx)     # mx = W * SANGRE
y = min(max(y, -my), H - alto  + my)
```

Sin ese encaje, una posición pensada para un rótulo de 520 px recibe un retrato de 1280 y la cara sale
cortada por el borde derecho. Con él, el retrato se corre hacia dentro y el plano sigue lleno. La
única condición es comprobar **antes** que el elemento cabe del todo en el lienzo (ancho ≤ lienzo más
dos sangrías): si no cabe, no hay posición que lo salve y hay que reducirlo.

---

## 4. Ver el borde antes de que lo vea nadie

```bash
# marca los 42 px de sangría horizontal y los 24 verticales sobre un fotograma real
ffmpeg -y -ss 3 -i plano.mp4 -frames:v 1 -vf \
"drawbox=x=0:y=0:w=42:h=ih:color=red@0.35:t=fill,\
 drawbox=x=iw-42:y=0:w=42:h=ih:color=red@0.35:t=fill,\
 drawbox=x=0:y=0:w=iw:h=24:color=red@0.35:t=fill,\
 drawbox=x=0:y=ih-24:w=iw:h=24:color=red@0.35:t=fill" margenes.png
```
Lo que asome dentro de las bandas rojas está en zona de sangría: aceptable. Lo que esté cortado por el
canto sin llegar a la banda es que se pasó. Y si aparece una franja de color liso donde debería haber
imagen, eso es el fondo que se quedó corto de margen: vuelve al apartado 1.

---

## Errores frecuentes

1. **Pedir deriva con `z = 1`.** Recorrido disponible cero. El plano no se mueve y nadie avisa.
2. **Subir la resolución de la fuente para «tener más margen».** El margen en pantalla lo da el zoom,
   no los megapíxeles.
3. **Sangría por encima del 4%.** Medido: 8 elementos maltratados; al 7%, doce, con uno perdiendo el
   25% de su superficie.
4. **Sangría cero.** Todo cabe y el cuadro se ve apretado contra los bordes.
5. **Descartar el elemento que no cabe** en vez de correrlo hacia dentro. Se pierde densidad y se
   pierde el evento.
6. **Aplicar la sangría sin comprobar que el elemento cabe en el lienzo.** Ninguna posición salva a un
   recorte más ancho que el cuadro.
7. **Medir la salida de cuadro en píxeles absolutos.** El umbral que importa es el **porcentaje de la
   superficie del elemento**: 100 px fuera no significan nada sin saber su tamaño.
8. **Descubrir la franja al final, con el episodio renderizado.** La prueba de los dos extremos cuesta
   dos segundos.

---

## Relacionado

- `450` — de dónde sale la fórmula del recorrido disponible
- `451` — cuánta deriva se puede permitir el plano por velocidad, antes de que por margen
- `455` — por qué `x` e `y` saturan en silencio y `crop` ni siquiera te deja animar el tamaño
- `457` — el mismo problema en vertical, donde el margen horizontal sobra y el vertical no existe
- `45` y `102` — zonas seguras de plataforma y `drawbox` como instrumento de diagnóstico
- `canales_lushows/245` y `/242` — la sangría como constante del motor y la colocación por rectángulo
