# 427 — Efecto sobre material mixto

Un efecto medido sobre un clip se comporta como el clip. Sobre ocho fuentes distintas —archivo de 1914,
una foto de museo de 2019, un mugshot, un fotograma de cine mudo— se comporta de ocho maneras, y la
hipótesis con la que lo pusiste («esto une el material») puede ser exactamente lo contrario de lo que
hace.

Este módulo mide esa hipótesis. El resultado es incómodo: **un efecto global no unifica material
mixto.** Lo desplaza entero y deja la dispersión casi intacta.

---

## 1. El material de prueba

Ocho recortes reales del banco de archivo del canal documental (`canales_lushows`), elegidos por ser
tan distintos entre sí como el material que de verdad llega: un mugshot policial, una celda de
Alcatraz fotografiada en 2005, un billete de 1914, un concurso de automóviles de 1927, un museo alemán
en 2019, un edificio abandonado, una limusina de los años 20 y un vagón desguazado.

Medido crudo, escalados todos a 1280 px de ancho:

| Fuente | YAVG | SATAVG |
|---|---|---|
| mugshot | 147,4 | 30,31 |
| celda Alcatraz 2005 | 130,1 | 14,85 |
| billete 1914 | 117,1 | **0,32** |
| concurso 1927 | **167,4** | 0,36 |
| museo Dresde 2019 | **66,2** | 11,93 |
| edificio abandonado | 92,1 | 17,38 |
| limusina 1921 | 143,5 | 11,36 |
| vagón desguazado | 130,4 | **0,00** |

**Rango de luminancia: 101 puntos sobre 255.** Rango de saturación: de 0 (blanco y negro puro) a 30
(una foto virada). Ése es el problema real de un canal de archivo, y ningún filtro lo resuelve por
arte de magia.

---

## 2. Medido: el efecto global NO unifica

Tres tratamientos sobre las mismas ocho fuentes. La medida que importa no es la media: es la
**dispersión** (desviación típica y rango).

| Tratamiento | YAVG media | YAVG **sd** | YAVG rango | SATAVG media | SATAVG **sd** | SATAVG rango |
|---|---|---|---|---|---|---|
| **crudo** | 124,3 | **30,2** | 101,2 | 10,81 | **9,86** | 30,31 |
| **efecto global**<br>`eq`+`noise`+`vignette` | 116,9 | **23,1** | 75,0 | 9,37 | **6,83** | 20,74 |
| **normalize global** + desaturar a 0,35 | 102,1 | **24,1** | 74,6 | 4,01 | **1,45** | 4,24 |
| **corrección por clip** + desaturar | 90,6 | **2,9** | **9,3** | 4,32 | 2,08 | 6,30 |

🔴 **La fila 2 es la lección.** La cadena de acabado completa del canal —corrección de exposición, grano
y viñeta, aplicada igual a todo— baja la dispersión de luminancia solo un **24%** (30,2 → 23,1). Sigue
habiendo **75 puntos** entre la fuente más clara y la más oscura. El efecto global desplazó las ocho
fuentes hacia abajo; no las acercó entre sí.

**La fila 3 mata un atajo popular.** `normalize`, que estira el rango de cada imagen a negro-blanco
completos, **no arregla la luminancia** (sd 24,1, prácticamente igual que el efecto global): estirar el
contraste de cada fuente no iguala sus medias. Lo que sí arregla es el color: bajar la saturación a 0,35
lleva la dispersión de SATAVG de 9,86 a **1,45**, un **−85%**. Es el motivo real por el que casi todos
los canales de archivo trabajan casi en monocromo: **la desaturación es el unificador más barato y más
eficaz que existe**, porque elimina de golpe la dimensión donde las fuentes más difieren.

**La fila 4 es la que funciona.** Medir cada fuente y corregirla individualmente a un objetivo común
deja la desviación de luminancia en **2,9** —un **90% menos** que el crudo— y el rango en 9,3 puntos.
Ninguna cadena global se acerca.

---

## 3. El arnés: medir cada fuente y corregirla

El principio es de `62` (emparejar planos), ejecutado por código:

```bash
#!/usr/bin/env bash
# igualar.sh — mide cada fuente y la lleva a un YAVG objetivo
OBJ=110
yavg () { ffmpeg -hide_banner -loop 1 -t 0.1 -i "$1" \
  -vf "scale=1280:-2,$2,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -frames:v 1 -f null - 2>&1 | grep -o 'YAVG=[0-9.]*' | head -1 | cut -d= -f2; }

for f in archivo/*.jpg archivo/*.png; do
  Y0=$(yavg "$f" "null")
  # eq aplica  salida = 255*(entrada/255)^(1/gamma)
  #   -> el gamma que lleva Y0 a OBJ es  ln(Y0/255) / ln(OBJ/255)
  G=$(awk -v y="$Y0" -v o="$OBJ" 'BEGIN{g=log(y/255)/log(o/255);
       if(g<0.4)g=0.4; if(g>2.5)g=2.5; printf "%.3f",g}')
  echo "$f  Y0=$Y0  gamma=$G"
done
```

Los topes de 0,4 y 2,5 no son decorativos: una fuente muy oscura pide un gamma enorme que levanta el
ruido y lava los negros. Cuando el gamma calculado se sale del rango, **la fuente no se corrige: se
descarta o se usa a propósito como excepción** (`336`).

Medido sobre las ocho fuentes, con `OBJ=110`:

| Fuente | Y0 | gamma calculado | Y final |
|---|---|---|---|
| mugshot | 147,4 | 0,652 | 90,8 |
| celda Alcatraz | 130,1 | 0,800 | 91,5 |
| billete 1914 | 117,1 | 0,926 | 91,8 |
| concurso 1927 | 167,4 | **0,501** | 91,0 |
| museo Dresde | 66,2 | **1,604** | 86,7 |
| edificio abandonado | 92,1 | 1,211 | 85,6 |
| limusina 1921 | 143,5 | 0,684 | 94,8 |
| vagón desguazado | 130,4 | 0,797 | 92,7 |

### 🔴 La trampa de la fórmula cerrada

Fíjate: el objetivo era **110** y la media quedó en **90,6**. La fórmula no está mal, pero dos cosas la
desvían:

1. **La media de una transformación no es la transformación de la media.** `gamma` es una curva; aplicar
   la curva píxel a píxel y promediar después da un resultado distinto de aplicar la curva al promedio.
   El error crece cuanto más contrastada sea la imagen.
2. **Lo que va después sigue moviendo el número.** En la cadena medida, detrás del `eq` van el grano y
   una `vignette=PI/5.6`, y la viñeta oscurece. El `Y` que mides al final no es el que salió del `eq`.

La solución no es una fórmula mejor: es **medir el resultado y corregir una segunda vez**. Con una sola
iteración adicional —recalcular el gamma partiendo del Y ya medido con la cadena completa— se llega al
objetivo con menos de dos puntos de error. El trabajo importante ya lo hizo la primera pasada: la
dispersión cayó de 30,2 a 2,9; la segunda pasada solo mueve el centro.

**Y la moraleja general del bloque:** *mide el resultado, no confíes en el cálculo.* Es la misma razón
por la que `420` existe.

---

## 4. Las tres dimensiones de la mezcla

No todo lo que hace que dos fuentes «no casen» se arregla igual:

| Dimensión | Se mide con | Se iguala con | ¿Sirve un efecto global? |
|---|---|---|---|
| **Luminancia** | YAVG, YLOW/YHIGH | gamma por clip | ❌ (24% de mejora) |
| **Saturación** | SATAVG | desaturar a un techo común | ✅ (85% de mejora) |
| **Dominante de color** | UAVG, VAVG, HUEAVG | virado común encima de la desaturación | ✅ |
| **Textura / ruido** | YDIF, peso codificado | denoise por clip + grano común | parcial |
| **Nitidez** | peso codificado | no se iguala: se elige el plano | ❌ |
| **Resolución real** | `ffprobe` + peso | escalar todo al mismo techo | ✅ |

Las que responden a un efecto global son las de **color**. Las que no, son las de **nivel** y las de
**detalle**, y ésas piden medida por clip.

De ahí sale la receta de casa para archivo mixto:

```
1. POR CLIP     escalar a un techo comun + gamma medido a un YAVG objetivo
2. GLOBAL       desaturar a un techo comun (0.30-0.40)
3. GLOBAL       virado de marca sobre el monocromo
4. GLOBAL       grano + viñeta + format=yuv420p
```

El paso 1 es el único que hay que calcular por fuente. Los otros tres se aplican igual a todo, y es
precisamente porque el paso 1 ya hizo el trabajo que los otros tres funcionan.

---

## 5. Por qué los canales de archivo son casi monocromos

Ahora se puede decir con el número delante. En las ocho fuentes, la saturación va de 0,00 a 30,31: hay
fotos en blanco y negro puro y fotos viradas al sepia conviviendo en el mismo minuto. Ninguna
corrección de color las va a poner de acuerdo, porque no hay nada que corregir en una imagen que tiene
saturación cero.

**Desaturar a un techo común elimina la dimensión del problema en vez de resolverla.** Bajar todo a
SATAVG ≈ 4 deja la dispersión en 1,45, y a partir de ahí un virado común —el azul tinta del canal, el
sepia, lo que decida `directorcreativo_lushows`— se aplica sobre una base uniforme y tiñe las ocho
fuentes igual.

No es pobreza de recursos: es la única jugada que funciona sobre material que no controlas.

---

## 6. Cuándo NO se iguala

Igualar es la norma, no la ley. Tres casos donde la diferencia entre fuentes es la herramienta:

1. **El contraste narrativo.** Pasar de un archivo oscuro y granulado a una foto moderna limpia marca un
   salto de época mejor que cualquier rótulo.
2. **La fuente que es el argumento.** Un documento, una ficha policial, un titular de periódico: si el
   plano existe para que se lea, se optimiza para legibilidad, no para que case con el vecino.
3. **El plano de descanso.** Después de dos minutos de collage igualado, una imagen que rompe el patrón
   reinicia la atención (`323`).

En los tres, la diferencia **está declarada** en el guion visual. La regla operativa es que la mesa esté
igualada por defecto y la excepción sea explícita, no al revés.

---

## Errores frecuentes

- **Creer que la cadena de acabado une el material.** Medido: reduce la dispersión de luminancia un 24%.
  El material sigue sin casar.
- **Usar `normalize` como igualador.** Iguala el **contraste** de cada imagen, no su nivel medio: la sd
  de YAVG se quedó igual (24,1 contra 23,1).
- **Medir la media y no la dispersión.** La media puede estar perfecta con las fuentes desperdigadas.
- **Fiarse de la fórmula del gamma sin volver a medir.** Objetivo 110, resultado 90,6.
- **Medir el `Y` a la salida del `eq` en vez de al final de la cadena.** La viñeta que viene detrás lo
  cambia.
- **Corregir con `brightness` en vez de `gamma`.** `brightness` desplaza todo: sube los negros y lava la
  imagen. `gamma` conserva los extremos.
- **Corregir fuentes que no se pueden corregir.** Si el gamma se sale de 0,4–2,5, la fuente se descarta.
- **Igualar sobre un fotograma de un clip con movimiento.** Mide varios y promedia.
- **Aplicar el virado antes de desaturar.** El virado sobre una base desigual sale desigual.
- **Igualar por criterio y no por medida.** Con ocho fuentes todavía se puede a ojo; con cuatrocientos
  recortes en un episodio, no.

---

## Checklist

- [ ] Medí YAVG y SATAVG de cada fuente **antes** de tocar nada.
- [ ] Miro la **dispersión**, no la media.
- [ ] La corrección de luminancia es por clip, con gamma calculado sobre su medida.
- [ ] Volví a medir **al final de la cadena** y corregí una segunda vez.
- [ ] Las fuentes cuyo gamma se sale de 0,4–2,5 están descartadas o declaradas como excepción.
- [ ] La saturación se iguala con un techo común y el virado va después.
- [ ] Todas las fuentes entran a la cadena al mismo techo de resolución.
- [ ] Lo que hace la cadena global es caracterizar, no igualar: eso ya está hecho.
- [ ] Las excepciones —los planos que rompen a propósito— están en el guion visual.

---

## Relacionado

- `62` — emparejar planos: el mismo oficio a mano
- `420`, `421` — el arnés y las magnitudes por familia
- `425`, `426` — competencia entre efectos y orden de aplicación
- `428` — lo que sobrevive a la entrega
- `339`, `336` — inventario del material y descartar sin culpa
- `60`, `61`, `64` — fundamentos de color, corrección frente a gradación, forzar la paleta de marca
- `108` — `signalstats` y el resto del instrumental
- `canales_lushows` — el banco de archivo y el guion visual del canal documental
- `directorcreativo_lushows` — el virado, la paleta y qué look tiene el monocromo: esa decisión es suya
