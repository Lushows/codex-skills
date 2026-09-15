# 438 — El destello que marea

> Hay un punto en el que un recurso de montaje deja de ser un recurso y se convierte en un riesgo
> médico. Ese punto está escrito, tiene números, y no depende de si a ti te parece mucho o poco.

Dos criterios reales, con fuente, y un arnés para comprobarlos sobre tu propio render.

---

## 1. El criterio de la web: WCAG 2.3.1

El **criterio de conformidad 2.3.1 "Three Flashes or Below Threshold"** del W3C dice que el contenido no
debe contener nada que destelle más de tres veces en un segundo, salvo que esté por debajo de los
umbrales de *destello general* y *destello rojo*. Sus definiciones, que son las que se pueden medir:

| Concepto | Definición del W3C |
|---|---|
| **Destello general** | un par de cambios opuestos de luminancia relativa **del 10 % o más** del máximo, donde la luminancia relativa de la imagen más oscura está **por debajo de 0,80** |
| **Destello rojo** | cualquier par de transiciones opuestas que involucre un **rojo saturado** |
| **Área** | se aplica si la zona que destella ocupa más del **25 % de un campo visual de 10°** — que para pantalla se estima con **un rectángulo de 341 × 256 px sobre un contenido de 1024 × 768** |
| **Límite** | no más de **tres destellos generales y/o tres destellos rojos en cualquier periodo de un segundo** |

Traducido a un vídeo vertical de 1920 × 1080: el rectángulo equivalente al campo de 10° es
**640 × 360 px** (un tercio de ancho y un tercio de alto). Un fogonazo a pantalla completa siempre
cumple el criterio de área, así que en tu caso **sólo cuentan la magnitud y la frecuencia**.

## 2. El criterio de la televisión: UIT-R BT.1702

La **Recomendación UIT-R BT.1702**, *Guidance for the reduction of photosensitive epileptic seizures
caused by television*, es la versión de radiodifusión. Su definición de destello potencialmente dañino
es un par de cambios opuestos de luminancia de **20 cd/m² o más**. La guía de Ofcom que la aplica añade
las dos condiciones que la completan: que la imagen oscura esté **por debajo de 160 cd/m²** y que la
zona ocupe más del **25 % de la pantalla**, con el límite de **tres destellos por segundo**.

> ⚠️ **Honestidad sobre estas cifras.** Las definiciones de WCAG las he verificado textualmente contra
> la página del W3C. Las de BT.1702 y Ofcom las he verificado a través de citas de esos documentos, no
> extrayendo el PDF entero (el de Ofcom devuelve 403 y el del UIT viene como imagen). Los tres números
> —20 cd/m², 160 cd/m², 25 %— aparecen consistentemente en ambas fuentes, pero si vas a certificar una
> pieza para emisión, **abre tú los PDF originales**, no te fíes de este resumen.
>
> Y lo que nadie te puede certificar desde aquí: BT.1702 habla en **cd/m²**, o sea en luz emitida por
> la pantalla del espectador, que depende de su tele y de su brillo. Por eso el criterio operativo para
> quien monta vídeo es el de WCAG, que está en luminancia **relativa** y se mide sobre el archivo.

---

## 3. Cómo se mide sobre tu archivo

La luminancia relativa del W3C no es el `Y` de `signalstats`: hay que quitar el rango limitado y
linealizar la curva sRGB.

```python
def rel_lum(Y):                       # Y de signalstats, rango limitado 16-235
    c = max(0.0, min(1.0, (Y - 16.0) / 219.0))
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
```

Con eso, el procedimiento completo: sacar `YAVG` por fotograma (`432`), convertir, buscar los máximos y
mínimos locales, y contar los pares consecutivos cuyo salto llega al 10 % con el extremo oscuro por
debajo de 0,80. Luego, ventana deslizante de 1 s y contar cuántos caben.

Ejecutado sobre `e02_nombre.mp4` del piloto documental (288 fotogramas, 11,48 s, con un destello real
dentro):

```
fotogramas: 288  ·  duracion: 11.48 s
transiciones >= 10% de luminancia relativa: 0
maximo en una ventana de 1 s: 0  (limite 3)
VEREDICTO: pasa
```

---

## 4. El dato que cambia todo: la base importa más que la fuerza

El mismo destello, con los mismos parámetros (`fuerza` 0,18, `ancho` 0,075), aplicado sobre imágenes de
distinta luminancia de partida:

| Base Y | Pico Y | Δ Y | L relativa base | L relativa pico | **Δ L** | ¿Destello general? |
|---|---|---|---|---|---|---|
| 35,1 | 57,8 | +22,7 | 0,008 | 0,030 | **2,2 %** | no |
| 51,1 | 77,7 | +26,7 | 0,022 | 0,065 | **4,3 %** | no |
| 67,1 | 97,7 | +30,6 | 0,044 | 0,115 | **7,0 %** | no |
| 84,1 | 119,0 | +34,9 | 0,079 | 0,188 | **10,9 %** | **sí** |
| 104,1 | 144,0 | +40,0 | 0,134 | 0,301 | **16,6 %** | **sí** |
| 125,1 | 170,3 | +45,2 | 0,212 | 0,454 | **24,2 %** | **sí** |

**Un destello idéntico pasa de 2,2 % a 24,2 % según lo clara que sea la imagen debajo.** Once veces. El
umbral del 10 % se cruza alrededor de una base de Y ≈ 80.

Consecuencias prácticas:

1. **Un destello afinado sobre material oscuro se vuelve agresivo al ponerlo sobre material claro.** No
   se reutiliza el número entre piezas: se mide otra vez.
2. **Sobre base clara, `fuerza` 0,18 ya produce un destello general** en el sentido de la norma. Sigue
   siendo legal — porque hay uno cada 12 s, no tres por segundo — pero ya no tienes margen para
   encadenarlos.
3. La misma tabla avisa de lo otro: a partir de base 125 el `YMAX` llega a 255 y **estás quemando**
   (`222`, `436`).

---

## 5. Dónde está el riesgo de verdad (no en tus destellos)

Medido en las dos piezas del piloto: **un destello cada 12,6–13,3 s, o sea 0,08 Hz**, 38 veces por
debajo del límite de 3/s. Los destellos deliberados casi nunca son el problema.

Lo que sí lo es, y nadie mide:

- **Montajes de corte rapidísimo alternando planos oscuros y claros.** Ocho cortes por segundo entre un
  plano nocturno y uno a pleno sol son ocho destellos generales por segundo. Ese es el caso real.
- **Efectos de estroboscopio y "glitch" de parpadeo** (`57`), que por definición trabajan en la banda
  peligrosa.
- **Rojo saturado que entra y sale.** Es un criterio aparte y más estricto. Un logotipo rojo que
  parpadea puede incumplir aunque la luminancia apenas se mueva.
- **El bucle.** Una pieza de 6 s con un destello al principio y otro al final, en bucle automático,
  produce dos destellos cada seis segundos indefinidamente. La norma habla de un segundo, pero BT.1702
  advierte además de que una secuencia de más de 5 s de parpadeo puede suponer riesgo aunque cumpla.

---

## 6. Por debajo del umbral tampoco es gratis

Cumplir la norma es el suelo, no el objetivo. Un parpadeo de 6 %, repetido cada dos segundos durante
treinta, no provoca una crisis pero **cansa**, y el cansancio se ve en la retención (`140`). La prueba
barata: mira la pieza entera dos veces seguidas. Si a la segunda te molesta algo que no sabes nombrar,
casi siempre es luz repetida.

---

## Errores frecuentes

- **Decidir "a ojo" si un destello marea.** Hay dos normas con números y un script de treinta líneas.
- **Usar `YAVG` como si fuera luminancia relativa.** Hay que quitar el rango limitado y linealizar sRGB,
  o el resultado sale muy por debajo de la realidad.
- **Reutilizar la fuerza entre piezas.** El mismo número da 2,2 % o 24,2 % según la base.
- **Medir sólo los destellos declarados.** El riesgo suele estar en los cortes, no en los efectos.
- **Olvidar el rojo saturado.** Tiene su propio umbral y es más estricto.
- **Olvidar el bucle.** En redes la pieza se repite sola; el recuento no termina cuando termina el vídeo.
- **Citar "el estándar" sin haberlo abierto.** Si la pieza va a emisión, los PDF originales, no resúmenes.
- **Confundir cumplir con estar bien.** El umbral protege de una crisis, no del cansancio.

---

## Relacionado

- `430`, `439` — densidad y presupuesto: la primera defensa contra esto es no poner tantos.
- `431`, `432` — la curva y el arnés de medición del que sale la serie de luminancia.
- `436` — pulsos de exposición, donde el mismo problema aparece en cámara lenta.
- `222` — exposición y rango dinámico: la otra mitad de la tabla del §4 (el quemado).
- `57`, `93` — glitch y parpadeo, y qué sobrevive a la recompresión.
- `95` — metadatos y accesibilidad: dónde encaja esto en la entrega.

**Fuentes:** [W3C · Understanding SC 2.3.1 Three Flashes or Below
Threshold](https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html) ·
[Rec. UIT-R BT.1702-2](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1702-2-201910-S!!PDF-E.pdf) ·
[Ofcom · guidance note on flashing images (legacy
ITC)](https://www.ofcom.org.uk/__data/assets/pdf_file/0021/16248/gn_flash.pdf)
