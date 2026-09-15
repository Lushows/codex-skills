# 467 — El keyframe lineal: el índice de frenado

**Qué resuelve:** el `84-keyframes-y-curvas.md` explica qué es una curva y trae las fórmulas listas
para copiar. **→ ese es el módulo de referencia.** Este demuestra con números por qué la interpolación
lineal se lee como barata, y da **una sola cifra** —el índice de frenado— con la que auditas cualquier
animación en dos minutos. De todo el bloque 460–469 es el que más rinde: cambiar lineal por frenado sube
la percepción de calidad más que cualquier efecto que puedas comprar, y cuesta editar una expresión.

---

## 1. El material: una entrada lineal de verdad, en producción

No hay que inventar el ejemplo. El motor de montaje del canal PAPER EMPIRES
(`Desktop\CANALES-LUSHOWS\piloto\motor.py`, función `expr_elemento`) mete así los elementos en cuadro:

```python
if ent == "izq":      # entra deslizando desde fuera por la izquierda
    x = (f"if(lt(t,{t0+de:.2f}),"
         f"({x})-(1-(t-{t0:.2f})/{de:.2f})*520,{x})")
```

El comentario del propio archivo es correcto —"las entradas no son adorno: un elemento que aparece de
golpe se lee como error de render"— y la duración (0,36 s) está dentro de la tabla de `84`. Pero
`(1-(t-t0)/de)` es **una recta**: el elemento recorre los mismos píxeles en cada fotograma y se detiene
en seco. Es el caso de estudio perfecto: código real, en producción, escrito con criterio, y con el
único fallo que este módulo caza.

---

## 2. Las cuatro versiones, renderizadas

Mismo elemento, mismo recorrido (520 px), misma duración (0,36 s = 18 fotogramas a 50 fps):

```bash
# a) LINEAL — la expresion de motor.py, tal cual
overlay=y=880:x='if(lt(t,0.36),390-(1-t/0.36)*520,390)'
# b) EASE OUT CUBICO — frena al llegar
overlay=y=880:x='st(0,clip(t/0.36,0,1)); 390-(1-(1-pow(1-ld(0),3)))*520'
# c) EASE OUT BACK atenuado — se pasa un poco y vuelve (d = igual con 2.70158 / 1.70158)
overlay=y=880:x='st(0,clip(t/0.36,0,1)); st(1, 1+1.6*pow(ld(0)-1,3)+0.9*pow(ld(0)-1,2)); 390-(1-ld(1))*520'
```

Y la medición: se localiza el borde del elemento fotograma a fotograma y se deriva la velocidad.
```python
def borde_izq(f):                       # f = fotograma en gris
    banda = f[940:960, :].mean(axis=0)  # franja horizontal que cruza el elemento
    idx = np.where(banda > 100)[0]
    return float(idx[0]) if len(idx) else float('nan')
x = np.array([borde_izq(f) for f in fotogramas]); v = np.diff(x)
```

---

## 3. Los números

| Curva | v máxima | v en los 3 últimos fotogramas | **% del recorrido en el último 25% del tiempo** | Sobreimpulso |
|---|---|---|---|---|
| **Lineal** (`motor.py`) | 30 px/f | **30 / 28 / 30** | **29,7%** | 0% |
| Ease out cúbico | 64 px/f | **2 / 0 / 2** | **1,5%** | 0% |
| Ease out back atenuado | 82 px/f | −4 / −4 / −4 | −4,9% | **3,8%** |
| Ease out back estándar | 102 px/f | −10 / −6 / −2 | −7,2% | **9,6%** |

La serie de velocidades del caso lineal, entera —`0 · 14 · 28 · 30 · 28 · 30 · 28 · 28 · 30 · 28 · 30 ·
28 · 30 · 28 · 30 · 28 · 30 · 0`—: catorce fotogramas seguidos a la misma velocidad y una parada de 30 a 0 **en un fotograma**. La
aceleración en ese instante es de 30 px/f² —infinita, en la práctica—: el elemento choca contra una
pared invisible. Ninguna cosa con masa se mueve así, y el cerebro lo registra aunque el espectador no
sepa nombrarlo (`85-los-12-principios-aplicados.md`).

La del ease out cúbico —`0 · 24 · 64 · 56 · 50 · 40 · 36 · 30 · 24 · 20 · 14 · 12 · 8 · 6 · 2 · 2 · 0`—
arranca más rápido (pico de 64 frente a 30) **y llega mucho antes al sitio**, pero los últimos cinco
fotogramas se mueven 6 píxeles en total. Eso es lo que el ojo llama "llegó y se posó".

---

## 4. El índice de frenado

> **Índice de frenado = qué fracción del recorrido total ocurre en el último 25% del tiempo.** Lineal
> **29,7%** (un movimiento uniforme reparte el 25% por definición; la cuantización lo deja en 29,7);
> ease out cúbico **1,5%**; con sobreimpulso, **negativo**, porque en ese cuarto el elemento vuelve.
>
> **Umbral: por encima del 15% en el último cuarto, el movimiento se lee como lineal.** Entre el 0% y el
> 5%, se lee como frenado.

Es una sola cifra, no depende de la resolución ni de la duración, y sirve para auditar animación ajena:
sacas la tira de fotogramas (`84`, §9), mides la posición en cuatro y divides. Si el elemento recorrió
lo mismo entre los cuatro, es lineal. El sobreimpulso va en la misma escala: el `back` estándar se pasa
un **9,6%**; el `56` (punto 10) fija lo correcto en 5–12% para marcas con energía, y el atenuado, con
**3,8%**, es el guiño para marcas serias. Los presets de rebote elástico andan por el 40%.

---

## 5. El parche a `motor.py`

Sustituir la recta por un frenado es una línea, y ffmpeg acepta la expresión tal cual:

```python
if ent == "izq":      # entra deslizando y FRENA al llegar (ease out cubico)
    x = (f"if(lt(t,{t0+de:.2f}),"
         f"st(0,clip((t-{t0:.2f})/{de:.2f},0,1));"
         f"({x})-(1-(1-pow(1-ld(0),3)))*520,{x})")
```

Tres advertencias: **`clip(...,0,1)` no es opcional** (sin recortar, la fórmula sigue evaluándose fuera
de la ventana y el elemento se va de cuadro); **`st(0,…)` y `ld(0)` comparten registros con el resto de
la cadena**, así que usa uno distinto por elemento; y **la salida va con ease *in* y al 60–70% de la
entrada** (`84`, §6). Lo que **no** hay que tocar de `motor.py` es la deriva lenta (`deriva`): está bien
pensada, y una deriva sí es uniforme en el mundo real porque no arranca ni frena dentro del plano.

---

## Errores frecuentes

1. **Creer que "ya tiene animación" es suficiente.** La animación existe; la curva es la que decide si
   se ve cara. El comentario de `motor.py` demuestra que se puede tener el criterio correcto y la
   interpolación equivocada.
2. **Aplicar la misma curva a la entrada y a la salida.** Entra con ease out, sale con ease in (`84`).
3. **Medir el índice sobre un elemento que además tiene deriva.** La deriva contamina el último cuarto:
   mide solo la ventana de entrada.
4. **Poner sobreimpulso en todo.** Uno o dos elementos por pieza; el `back` estándar se pasa un 9,6% y
   eso, repetido, convierte la pieza en un juguete.
5. **Fiarse de la vista previa del programa** en vez de la tira de fotogramas (`84`, §9), o **olvidar
   `eval=frame`** al animar escala, que se evalúa una vez y no pasa nada.
6. **Medir un elemento oscuro sobre fondo oscuro.** El detector busca la primera columna clara: la serie
   sale a `nan` y parece que la curva falló.
7. **Suponer que los keyframes de CapCut ya interpolan con curva.** Depende de la opción elegida
   (`213-capcut-keyframes.md`, `212-capcut-animaciones.md`).

---

## Relacionado

- `84-keyframes-y-curvas.md` — **las fórmulas, las duraciones, la anticipación y los arcos.**
- `85-los-12-principios-aplicados.md` — por qué el cerebro pide aceleración.
- `202-animacion-de-entrada-y-salida.md` · `203-keyframes-a-mano.md` · `375-entradas-y-salidas-del-texto.md`
- `451-velocidad-del-movimiento-medida.md` (§5) — **la misma corrección aplicada al movimiento del
  fondo con `zoompan`**, en px/s. Allí el sujeto es la cámara; aquí, el elemento.
- `213-capcut-keyframes.md` — el mismo problema en el programa; `56` (punto 10), el rebote exagerado.
- `canales_lushows` — la skill del proyecto del que sale `motor.py`.
