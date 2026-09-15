# 339 — Inventario del material antes de montar

**Qué resuelve:** el paso que se salta todo el mundo. Antes de abrir el editor, una tabla con **una fila
por archivo**. Cuesta cinco minutos y es lo que evita descubrir a mitad de montaje que falta un plano, que
dos tomas van a distinta velocidad o que la mejor toma no tiene audio.

---

## 1. Por qué nadie lo hace y por qué hay que hacerlo

Porque no se siente como avanzar. Abrir CapCut y arrastrar el primer clip **se siente** como empezar a
editar; hacer una tabla se siente como papeleo.

El resultado de saltárselo es el error de `330`: se agarra el primer archivo de la carpeta porque no hay
ninguna otra información sobre la cual decidir. **El inventario es lo que convierte una carpeta en un
conjunto de opciones.**

> Sin inventario no estás eligiendo. Estás aceptando lo primero que se abrió.

---

## 2. Las columnas del inventario

Una fila por archivo. Ocho columnas técnicas que salen solas, y cuatro de criterio que pones tú.

| Columna | De dónde sale |
|---|---|
| archivo | el nombre |
| hora | del nombre o de `creation_time` |
| duración | `ffprobe` |
| resolución | `ffprobe` |
| fps declarado / fps medio | `ffprobe` |
| audio (sí/no, canales) | `ffprobe` |
| tamaño | el sistema de archivos |
| qué se ve | una línea escrita por ti |
| bloque de luz | `338` |
| puesto | G / E / D / I / R / X / P (`335`) |
| veredicto | sirve · respaldo · descarte |
| razón | media línea |

Las cuatro últimas son las que valen. Las ocho primeras son las que hacen que las cuatro últimas se
puedan escribir sin abrir nada.

---

## 3. El comando que llena las ocho primeras

```bash
#!/usr/bin/env bash
# inventario.sh — corre en la carpeta del material
echo "archivo;dur_s;ancho;alto;fps_decl;fps_medio;audio;MB" > inventario.csv
for f in *.mp4; do
  v=$(ffprobe -v error -select_streams v:0 \
      -show_entries stream=width,height,r_frame_rate,avg_frame_rate -of csv=p=0 "$f")
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  a=$(ffprobe -v error -select_streams a:0 \
      -show_entries stream=codec_name,channels -of csv=p=0 "$f")
  mb=$(( $(stat -c%s "$f") / 1048576 ))
  echo "$f;${d%.*};$v;${a:-SIN_AUDIO};$mb" >> inventario.csv
done
```

Ábrelo en cualquier hoja de cálculo, agrega las cuatro columnas de criterio y ya tienes el documento que
gobierna el montaje.

---

## 4. Las cinco preguntas que solo el inventario contesta

**a) ¿Cuánto material tengo de verdad?**
Las 16 tomas del caso real suman **18 minutos y 27 segundos** y **1,3 GB**. Para un reel de 30 segundos.
Saber que hay 37 veces más material del que cabe cambia la actitud: el trabajo no es "usar lo que hay",
es **descartar bien**.

**b) ¿Cuántos escenarios y cuántos bloques de luz?**
Cuatro escenarios y cuatro bloques horarios (`338`). Eso define la estructura antes de cortar nada.

**c) ¿Los archivos son compatibles entre sí?**
Aquí aparece el hallazgo típico. En el material real:

| Toma | `r_frame_rate` | `avg_frame_rate` |
|---|---|---|
| 122837 | **355/12 = 29,58** | 29,61 |
| 135553 | **355/12 = 29,58** | 29,61 |
| 125739 | 30/1 | 30,0000000583 |
| 155807 | 30/1 | 29,9999999 |
| 161648 | 30/1 | 30/1 |

Dos cosas que hay que saber leer:

- **Hay dos velocidades distintas en la misma carpeta** (29,58 y 30). Al mezclarlas en una línea de tiempo
  a 30 fps, esas dos tomas se reajustan y el audio se desliza.
- **Casi ningún archivo tiene `avg_frame_rate` igual a `r_frame_rate`.** Eso es **fps variable**, lo que
  graba por defecto casi cualquier celular. Es la causa clásica de "el audio se va desincronizando hacia
  el final" (`109`).

Y como todo esto se ve en la tabla, se arregla antes de montar, no después:

```bash
# Normalizar a fps constante, sin volver a comprimir el audio
ffmpeg -i toma.mp4 -vsync cfr -r 30 -c:v libx264 -crf 18 -preset fast -c:a copy toma_30.mp4
```

**d) ¿Todo tiene audio?**
Un archivo `SIN_AUDIO` en la columna es una bomba de tiempo. Mejor saberlo ahora.

**e) ¿Falta algo?**
Comparando el inventario con la lista de planos (`312`): si el plan pedía un plano de la fachada y no hay
ninguna fila que diga fachada, **falta**, y hoy se puede salir a grabarlo. Mañana, con el video a medio
montar, ya no.

---

## 5. Cerrar el inventario con decisiones

El inventario no sirve si termina en datos. Termina en tres marcas por fila:

- **Bloque** (A, B, C, D) → de `338`
- **Puesto** (G / E / D / I / R / X / P) → de `335`
- **Veredicto** (sirve · respaldo · descarte) → de `336`

Cuando las tres columnas están llenas, el orden de montaje ya está escrito: se filtra por veredicto
"sirve", se ordena por puesto y se respetan las fronteras de bloque. Eso es la estructura del video, y
salió de una hoja de cálculo, no de la intuición.

---

## 6. Lo que cuesta y lo que ahorra

| | Tiempo |
|---|---|
| Correr el script | 1–2 min |
| Escribir "qué se ve" en 16 filas | 3 min |
| Marcar bloque, puesto y veredicto | 2 min |
| **Total** | **≈ 6 min** |

Contra lo que evita: elegir la toma equivocada (`330`), descubrir el fps mezclado con el montaje hecho,
buscar cuatro veces el mismo archivo, volver a discutir qué toma era la buena, y montar sin saber que
faltaba un plano.

Una sola de esas cosas cuesta más de seis minutos.

---

## 7. El inventario es un documento vivo

Guárdalo junto al material, no en el escritorio (`317`, `135`). Sirve tres veces más de lo que parece:

- **Cuando hay que hacer la versión de 15 segundos.** Todo el trabajo de selección ya está hecho.
- **Cuando el mismo material alimenta otra pieza.** Un reel, un anuncio y una historia salen del mismo
  rodaje con veredictos distintos (`245`).
- **Cuando pasan tres meses.** Nadie recuerda qué había en `lv_0_20260804135656.mp4`. La columna "qué se
  ve" sí.
- **Cuando hay que pasarle el material a otra persona o a un modelo.** El inventario en texto plano es el
  contexto perfecto: nombres reales, duraciones reales, descripciones reales. Un modelo puede razonar
  sobre esa tabla sin ver un solo fotograma.

---

## 8. La versión mínima, para cuando no hay tiempo

Si de verdad no hay seis minutos, hay una versión de noventa segundos que ya evita el error grave:

1. Hoja de contactos de todo (`333`).
2. Un archivo `notas.txt` con **una línea por toma**: número de casilla, qué se ve, veredicto.

Eso es todo. No tiene fps ni duraciones, pero cumple lo esencial: **obliga a mirar las 16 antes de elegir
una**.

---

## Errores comunes

1. **No hacerlo.** Es el origen documentado del error de este bloque.
2. **Hacerlo mental.** "Ya sé qué hay en cada archivo" dura hasta el archivo número seis.
3. **Llenar solo las columnas técnicas.** Los datos sin veredicto no deciden nada.
4. **No mirar el fps.** Mezclar 29,58 con 30 desliza el audio y nadie sabe por qué.
5. **No detectar el fps variable.** Es lo que graba el celular por defecto y la causa clásica de la
   desincronización progresiva.
6. **Normalizar el fps después de montar.** Hay que hacerlo antes, sobre los brutos.
7. **No revisar qué archivos vienen sin audio.**
8. **No comparar el inventario con la lista de planos.** Es el único momento en que todavía se puede
   salir a grabar lo que falta.
9. **Guardar el inventario fuera de la carpeta del material.** Se pierde.
10. **Describir con adjetivos.** "Toma buena" no dice nada; "plano medio en la barra, sonriendo" sí.
11. **Renombrar los archivos y no actualizar la tabla.** Peor que no tenerla.
12. **Tirarlo al publicar.** Es lo que hace barata la segunda versión.
13. **Hacerlo después de empezar a montar.** Entonces ya no es un inventario: es un informe de daños.

---

## Checklist

- [ ] Existe un `inventario.csv` **dentro de la carpeta del material**.
- [ ] Hay **una fila por archivo**, sin excepciones.
- [ ] Están las columnas técnicas: duración, resolución, **fps declarado y medio**, audio, tamaño.
- [ ] Revisé si hay **fps mezclados** o **fps variable**, y normalicé antes de montar.
- [ ] Revisé que **todos** los archivos que voy a usar tengan audio.
- [ ] Cada fila tiene **una línea de "qué se ve"** escrita por mí.
- [ ] Cada fila tiene **bloque de luz** (`338`).
- [ ] Cada fila tiene **puesto** (`335`).
- [ ] Cada fila tiene **veredicto** y media línea de razón (`336`).
- [ ] Comparé el inventario con la **lista de planos** para ver si falta algo.
- [ ] Sé cuánto material total tengo y **cuánto va a entrar** en el formato.
- [ ] El inventario queda guardado junto al material y **se actualiza** si renombro algo.
