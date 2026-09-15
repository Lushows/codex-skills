# 333 — La hoja de contactos como herramienta de decisión

**Qué resuelve:** ver **todo** el material a la vez, en una sola imagen, antes de abrir ningún editor. El
módulo `17` explica cómo se construye. Este explica cómo se **usa para decidir**, que es otra cosa.

---

## 1. Para qué sirve de verdad

Una hoja de contactos no es un catálogo bonito. Es el instrumento que hace **imposible** el error de
`330`: elegir la primera toma sin haber mirado las otras quince.

La ventaja no es que muestre las tomas. Es que las muestra **juntas**. Nadie compara bien de a una: para
notar que la toma 7 tiene mejor luz que la 12 hay que verlas al lado. En la carpeta del computador, con
sus miniaturas diminutas y sus nombres `lv_0_20260804135656`, esa comparación no ocurre nunca.

> Regla: **ninguna decisión de material se toma sin haber visto la hoja completa.** Cuesta dos minutos y
> es la única barrera contra elegir por orden alfabético.

---

## 2. La hoja de todo el rodaje: un fotograma por toma

Es la más útil y casi nadie la hace, porque `tile` en ffmpeg funciona sobre **una** entrada. El truco es
en dos pasos: primero un PNG por toma, luego el mosaico.

```bash
# Paso 1 — un fotograma representativo por toma (30% de la duración)
mkdir -p frames
i=0
for f in *.mp4; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  t=$(awk -v x="$d" 'BEGIN{printf "%.2f", x*0.3}')
  ffmpeg -v error -ss "$t" -i "$f" -frames:v 1 "$(printf 'frames/f%02d.png' $i)"
  echo "$i = $f" >> frames/indice.txt
  i=$((i+1))
done

# Paso 2 — el mosaico
cd frames
ffmpeg -i "f%02d.png" -vf "scale=200:-1,tile=4x4:padding=4:margin=4" -frames:v 1 -y ../hoja.png
```

El `indice.txt` es obligatorio: sin él, la casilla 7 no te dice qué archivo abrir.

**Elegir la cuadrícula.** 16 tomas → `tile=4x4`. 12 tomas → `4x3`. 20 → `5x4`. Con vertical 9:16 y
200 px de ancho por casilla, una hoja de 4×4 queda en 830 × 1450 px: se ve completa en la pantalla del
computador y se lee bien en el celular.

> ⚠️ **`-pattern_type glob` no existe en las compilaciones de ffmpeg para Windows.** Por eso los archivos
> se copian numerados (`f00.png`, `f01.png`…) y se leen con `-i "f%02d.png"`. Verificado.

---

## 3. Numerar las casillas

Sin número, la hoja sirve para mirar pero no para hablar. "La tercera de la segunda fila" es una manera
horrible de tomar decisiones.

```powershell
# PowerShell. La ruta de la fuente lleva DOS barras invertidas antes de los dos puntos.
ffmpeg -i "f%02d.png" -vf 'scale=200:-1,drawtext=fontfile=C\\:/Windows/Fonts/arialbd.ttf:text=%{n}:x=8:y=8:fontsize=28:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=4x4:padding=4:margin=4' -frames:v 1 -y ../hoja.png
```

Tres trampas que este comando ya esquiva, todas verificadas:

1. **`Fontconfig error: Cannot load default config file`** → hay que pasar `fontfile=` a mano.
2. **La letra de unidad** `C:` rompe el filtro → se escribe `C\\:/Windows/...`.
3. **Git Bash reescribe las rutas** y las convierte en `C;C:\Program Files\Git\Windows\...`. Este comando
   se corre en **PowerShell**, no en Git Bash.

`%{n}` numera desde 0, igual que `f00.png`. Que coincida con el `indice.txt` es justamente el punto.

---

## 4. Cómo se lee una hoja: cuatro barridos, veinte segundos

No la mires "en general". Míralas cuatro veces, buscando una sola cosa cada vez.

**Barrido 1 — Luz.** ¿Cuáles casillas tienen la cara iluminada de frente? Descarta contraluces y siluetas
de una. En el caso real esto mata la casilla 0 (escaleras) en dos segundos.

**Barrido 2 — Tamaño del sujeto.** ¿En cuáles la persona ocupa menos de un quinto del ancho? Esas no
sirven para recortar ni para hablar: sirven de establecimiento (`335`).

**Barrido 3 — Fondo.** ¿Qué hay pegado al contorno? Y una pregunta que solo se puede contestar viendo
todo junto: **¿cuántos escenarios distintos hay?** En la hoja de Bendita Pola se ven cuatro (escaleras,
pasillo, terraza de día, barra con neón), y eso decide la estructura del reel entero.

**Barrido 4 — Repetidas.** ¿Cuáles casillas son casi idénticas? Las tomas 11 a 15 son el mismo encuadre
de la barra: son variantes de una sola cosa, no cinco opciones. Tratarlas como cinco opciones distintas es
perder media hora.

---

## 5. Lo que la hoja real dijo en veinte segundos

De la hoja de las 16 tomas del 4 de agosto, sin abrir un solo video:

- Hay **dos tomas sin nadie en cuadro** (casillas 2 y 15). Son placas limpias, y valen oro para matte por
  diferencia (`261`). Nadie las había visto: parecían tomas fallidas.
- Hay **dos tomas con luz de día** (casillas 5 y 6, la terraza) en medio de catorce tomas moradas. Son las
  únicas con piel real, y quedaron confirmadas después por medición (`331`).
- Hay **un primer plano de la mano abriendo la botella** (casilla 3): el único inserto del rodaje, y el
  material con el fondo más limpio de todos.
- Hay **cinco tomas del mismo plano de barra** que solo se diferencian en la expresión.
- Hay **una sola toma de cuerpo entero**.

Ninguna de esas cinco cosas es evidente mirando la carpeta. Todas son evidentes mirando la hoja.

---

## 6. La otra hoja: por dentro de una sola toma

La anterior compara tomas. Esta encuentra **el momento** dentro de una toma que ya elegiste.

```bash
# Un fotograma cada 2 segundos de una sola toma
ffmpeg -i toma.mp4 -vf "fps=1/2,scale=240:-1,tile=5x4:padding=4" -frames:v 1 -y detalle.png
```

Sirve para lo que ninguna transcripción muestra: dónde mira, cuándo gesticula, en qué segundo se le va el
pelo a la cara, cuándo pasa alguien por detrás. Para elegir el tramo exacto que vas a recortar (`330`),
esta hoja es más útil que ver el video entero.

El paso se calcula así: `paso = duración / (columnas × filas)`. Una toma de 76 s en una hoja de 5×4 pide
un fotograma cada 3,8 s → `fps=1/3.8`.

---

## 7. Anotar sobre la hoja

La hoja sin anotar se olvida. Ábrela en cualquier cosa que deje pintar encima (Paint, Fotos de Windows,
el celular) y marca:

- ✅ verde en las finalistas
- ✖ rojo en las descartadas, **con la razón en una palabra**: "contraluz", "lejos", "movida"
- ⭐ en la que va de gancho (`335`)
- 🧱 en las placas limpias

Guárdala como `hoja-anotada.png` junto al material. En dos semanas, cuando haya que hacer la versión de
30 segundos, esa imagen ahorra la tarde entera de volver a mirar todo.

---

## 8. Pasársela a un modelo

Un modelo de lenguaje **no ve tu video**. Ve las imágenes que le pases. La hoja de contactos es la forma
más barata de darle contexto visual de todo un rodaje en un solo archivo.

Cómo pedirlo bien:

> "Esta es una hoja de contactos de 16 tomas, numeradas del 0 al 15, leyendo de izquierda a derecha y de
> arriba abajo. Voy a recortar a la persona y ponerla sobre una ilustración. Dime **qué casillas descartas
> y por qué**, en una línea cada una. No me des la mejor: dame las descartadas."

Pedir descartes funciona mucho mejor que pedir la mejor. Descartar es una tarea de evidencia visible;
elegir la mejor es una opinión, y ahí el modelo improvisa.

Y una advertencia honesta: la casilla es **un fotograma de la toma**, no la toma. El modelo no puede
juzgar el micro-movimiento, ni el audio, ni si el pelo se mueve. Eso es tuyo (`332`).

---

## 9. Cuándo la hoja no sirve

- **Cuando lo que decide es el audio.** Para elegir la mejor lectura de una frase, la herramienta es la
  transcripción con marcas de tiempo (`12`, `124`), no la imagen.
- **Cuando hay una sola toma.** Ahí la hoja útil es la del punto 6, la temporal.
- **Cuando las tomas son casi idénticas.** Las casillas 10 a 14 del caso real se ven iguales en miniatura
  y se diferencian en la expresión, que a 200 px no se lee. Hay que abrirlas.
- **Cuando hay más de 30 tomas.** La hoja se vuelve ilegible. Divide por escenario: una hoja por sitio.

---

## Errores comunes

1. **No hacerla.** Es el error de `330` y cuesta la toma equivocada.
2. **Hacerla y no numerarla.** Sin números no se puede hablar de ella ni anotarla.
3. **No guardar el índice casilla → archivo.** La hoja queda bonita e inservible.
4. **Sacar el fotograma en el segundo 0.** Casi siempre es la mano tapando el lente.
5. **Usar `-pattern_type glob` en Windows.** No existe en esas compilaciones.
6. **Pelear con `drawtext` sin `fontfile`.** Falla siempre por fontconfig.
7. **Correr el comando con rutas de Windows en Git Bash.** MSYS las reescribe y las rompe.
8. **Casillas demasiado pequeñas.** Por debajo de 150 px de ancho no se distingue una expresión.
9. **Mirar la hoja "en general"** en vez de hacer los cuatro barridos con un objetivo cada uno.
10. **Confundir cinco variantes del mismo plano con cinco opciones.** Son una opción con cinco lecturas.
11. **Tirar la hoja al terminar.** Es el documento que ahorra la segunda versión del video.
12. **Creer que la miniatura dice si está enfocado.** No lo dice. Eso se mide (`331`) y se mira grande.
13. **Pedirle al modelo "la mejor toma".** Pídele descartes con razón.

---

## Checklist

- [ ] Saqué **un fotograma por toma**, al mismo porcentaje de duración.
- [ ] Armé la hoja con una cuadrícula que **cabe en una pantalla**.
- [ ] Las casillas están **numeradas** y hay un **índice** casilla → archivo.
- [ ] Hice los **cuatro barridos**: luz, tamaño del sujeto, fondo, repetidas.
- [ ] Conté **cuántos escenarios distintos** hay en el material.
- [ ] Busqué **placas limpias** (tomas sin nadie en cuadro).
- [ ] Marqué finalistas, descartes con razón, gancho y placas.
- [ ] Para la toma elegida hice además la hoja **temporal** y elegí el tramo.
- [ ] Guardé `hoja-anotada.png` junto al material (`317`).
- [ ] Si le pedí ayuda a un modelo, le pedí **descartes**, no la mejor.
- [ ] No decidí nada de audio mirando imágenes.
- [ ] Abrí a tamaño real las 2 o 3 finalistas antes de comprometerme.
