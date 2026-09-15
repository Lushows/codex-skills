# 469 — Rehabilitar un efecto quemado

**La tesis de este módulo, y del bloque entero:** un efecto quemado **no está prohibido para siempre**.
Lo quemado es una *versión concreta* —una duración, una dosis, una frecuencia, un material— y esa
versión se cambia. El `56` ya lo dice al final: el `zoomin` de `xfade` con 3 fotogramas, un impacto de
audio y usado una vez es el golpe del `53`. Mismo filtro, otro resultado.

Ojo con la frontera: aquí se rehabilita un **efecto visual**. Los formatos y los ganchos quemados tienen
sus módulos y otro método: `359-formatos-quemados.md` (Parte D, cómo detectar que un formato se quemó) y
`362-ganchos-quemados.md` (el ciclo usar-medir-guardar-volver). No los repito.

---

## 1. Las cuatro palancas

Un efecto se quema por *cómo* se usa. Hay cuatro cosas que puedes cambiar sin cambiar el efecto:

| Palanca | Qué se cambia | Ejemplo |
|---|---|---|
| **Escala** | cuánto dura o cuánto interviene | 15 fotogramas → 3 |
| **Contexto** | dónde ocurre en la estructura | en cada corte → en el cambio de bloque |
| **Frecuencia** | cuántas veces aparece | 8 veces → 1 |
| **Material** | sobre qué se aplica | sobre el cuadro → sobre el rótulo |

La palanca más infravalorada es la cuarta: casi todos los efectos de la lista negra se aplican **a la
imagen entera**, y casi todos sobreviven si se aplican **solo a la capa gráfica**, donde nadie espera
física y donde el plano no paga nada.

---

## 2. El ejemplo ejecutado: el zoom con desenfoque

Es el número 1 de la lista negra del `56` y el `461` ya lo midió: `xfade=zoomin:duration=0.5` deja **10
fotogramas por debajo del 85% de la nitidez base** y toca fondo en el **3%**. Lo rehabilitamos con las
cuatro palancas, midiendo cada paso.

### Palanca 1 — Escala: de medio segundo a tres fotogramas

El mismo gesto reducido a un golpe de escala de 3 fotogramas (el comando, en `461`, §2c):

| | Fotogramas bajo el 85% | Mínimo |
|---|---|---|
| Preset, 0,5 s | 10 | **3%** |
| Golpe, 3 fotogramas | **0** | **91%** |

Con la primera palanca el efecto deja de ser un problema: el aumento se siente y la imagen no se rompe.

### Palanca 4 — Material: el desenfoque sobre el rótulo, no sobre el plano

Aquí está el rendimiento de verdad. El rótulo entra en tres pasos —tres PNG pregenerados: σ=10 con 18%
de escala de más, σ=4 con 7%, y el definitivo— un fotograma cada uno:

```bash
ffmpeg -y -loglevel error -i plano.mp4 -i txt_0.png -i txt_1.png -i txt_2.png -filter_complex "\
[0:v][1:v]overlay=0:0:enable='between(n,15,15)'[a];\
[a][2:v]overlay=0:0:enable='between(n,16,16)'[b];\
[b][3:v]overlay=0:0:enable='gte(n,17)'" \
  -r 30 -c:v libx264 -crf 14 -pix_fmt yuv420p rotulo.mp4
```

Frente a la versión que desenfoca el cuadro entero en esos mismos dos fotogramas:

| Dónde se aplica el desenfoque | Nitidez en el fotograma 15 | …respecto al fotograma anterior |
|---|---|---|
| Al cuadro completo | 1,9 | **9%** |
| Solo al rótulo | 20,9 | **97%** |

El gesto es idéntico —el texto llega borroso y grande y se asienta nítido— pero **la placa conserva el
97% de su detalle**: el espectador ve el mismo impacto y el plano no paga nada.

> **La trampa de la medición:** la nitidez mediana del clip sube de 21,5 a 25,4 en cuanto entra el
> rótulo, porque el texto añade alta frecuencia, y con la mediana como base ambas versiones parecen
> igual de malas. **Compara contra el fotograma inmediatamente anterior** (`461`, error 3).

### Palancas 2 y 3 — Contexto y frecuencia

Pregenerar tres PNG en vez de desenfocar por fotograma no es solo más barato: **te obliga a decidir
dónde va**. Un efecto que cuesta tres archivos no se pone ocho veces. **Contexto:** en el cambio de
bloque, no en cada corte, donde la estructura ya cambia y el efecto acompaña algo
(`19-mapa-de-bloques.md`, `323-romper-el-patron.md`). **Frecuencia:** una vez, dos como mucho. Y el
audio, que no es palanca sino requisito: un evento visual sin evento sonoro no existe en el mundo real
(`76-diseño-sonoro.md`).

---

## 3. El mismo método, aplicado al glitch

Para ver que no depende del efecto, los números del `463` sobre el mismo ejercicio: **escala**, rachas
de 5 fotogramas → 2–3; **frecuencia**, del 53% de los fotogramas al 4%; **contexto**, de un evento cada
0,30 s con metrónomo a tres instantes con huecos no múltiplos. La medida delatora —la autocorrelación de
YDIF— pasa de **+0,77 a +0,11**, y la factura oculta, el caudal, de **×39 a ×6,9**.

---

## 4. La ficha de rehabilitación

Antes de rescatar cualquier efecto de la lista negra, rellena esto. Si alguna casilla queda vacía, el
efecto no se rehabilita: se quita.

- [ ] **Qué magnitud lo delataba** y cuánto medía (bloque `460`–`468`).
- [ ] **Qué palanca muevo** —escala, contexto, frecuencia o material— y a qué valor.
- [ ] **La medida después**, por debajo del umbral del módulo correspondiente.
- [ ] **De dónde sale**: la marca, la historia o el material. No se mide, se justifica (`56`).
- [ ] **El evento de audio** en el mismo fotograma, y **cuántas veces aparece** en la pieza.
- [ ] **La comparación renderizada** lado a lado para el cliente
      (`08-presentar-y-defender-un-corte.md`, `369-comparar-dos-videos-sin-enganarse.md`).

---

## 5. Cuándo NO se rehabilita

Tres casos en los que la respuesta es quitarlo y punto:

1. **Cuando afirma algo falso sobre la escena.** El destello sin fuente de luz (`465`) no tiene palanca:
   no hay escala ni frecuencia que arregle un sol inventado.
2. **Cuando el sustituto hace lo mismo y es más barato.** El resplandor de `267` §5.1 da el 70% del
   efecto de un rayo de luz en un minuto: rehabilitar el rayo con `geq` es gastar diez para empatar.
3. **Cuando el efecto es la identidad de otro.** Si se lee como cita, no lo rehabilitas: lo tomas
   prestado. Y eso ya es dirección creativa (`directorcreativo_lushows/97-tendencias-de-diseno-2026.md`).

---

## Errores frecuentes

1. **Sustituir un efecto quemado por otro quemado.** Cambiar `zoomin` por `pixelize` con la misma
   duración no arregla nada (`56`).
2. **Mover una sola palanca.** Acortarlo y seguir poniéndolo en cada corte deja la mitad del problema.
3. **Rehabilitar sin volver a medir.** La ficha existe para eso; el número de antes y el de después.
4. **Usar la mediana del clip como base al medir.** El rótulo sube la base y falsea la comparación.
5. **Confundir "quemado para el público" con "quemado para mí".** Un formato no está quemado porque tú
   lo hayas hecho cinco veces: tu audiencia no ha visto tus cinco videos (`359`, contra-señal).
6. **Rehabilitar por nostalgia y dejar el audio como estaba.** Si el motivo para rescatarlo es que te
   gustaba, no es un motivo; y el evento sonoro nunca es opcional.

---

## Relacionado

- `56-efectos-que-se-ven-baratos.md` — la lista negra y el test de las cuatro preguntas.
- `460-el-catalogo-medido.md` — el índice del bloque y las seis magnitudes.
- `461-el-zoom-con-desenfoque.md` · `463-el-glitch-decorativo.md` — los dos casos medidos de arriba.
- `359-formatos-quemados.md` · `362-ganchos-quemados.md` — lo mismo, pero para formatos y ganchos.
- `57-glitch-y-textura.md` · `53-whip-flash-y-golpe.md` — los sustitutos ejecutados.
- `472-la-prueba-ab-de-un-efecto.md` — **el arnés de la comparación emparejada, con criterio escrito
  antes.** La ficha de aquí decide *qué* mover; el `472` decide si el resultado se queda con su plaza.
- `429-cuando-quitar-un-efecto.md` — los seis disparadores y la prueba del día después: el camino
  contrario a este módulo, y el que hay que tomar cuando la rehabilitación no sale.
- `269-el-presupuesto-del-esfuerzo.md` · `470-cuantos-efectos-por-minuto.md` — el presupuesto.
