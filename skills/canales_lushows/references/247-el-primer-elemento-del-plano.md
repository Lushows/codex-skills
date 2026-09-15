# 247 · El primer elemento del plano

**Qué resuelve:** un plano con **un solo elemento vivo** no puede cubrir las dos mitades
del cuadro, salvo que sea ancho y esté justo en el centro. La otra mitad queda desierta,
y eso no se arregla moviéndolo: solo cambia de lado el hueco. Se arregla poniendo algo
**enfrente**.

---

## Por qué es una segunda pasada

`contrapeso()` va después de `generar()`: hasta que no está todo colocado no se sabe
dónde queda el hueco. Y mide con el **mismo criterio que el auditor** — si midiera
distinto, arreglaría algo que nadie comprueba. Lo que cuesta no tenerla, sobre
`ep01-lustig` (63,45 s):

| | con 2ª pasada | sin ella | descarta entera | 1 vuelta | umbral único 0,9 s |
|---|---|---|---|---|---|
| elementos | **61** | 47 | 53 | 59 | 59 |
| simultaneidad | **2,02** | 1,72 | 1,85 | 1,99 | 2,00 |
| cobertura media | **38,0 %** | 31,7 % | 34,2 % | 37,4 % | 37,6 % |
| cuadro casi vacío | **2,40 s** | 8,45 s | 5,35 s | 2,40 s | 4,05 s |
| huecos | **0** | 6 | 2 | 0 | 1 |
| descompensado | **0,00 s** | **14,80 s** | 12,60 s | 2,20 s | 0,00 s |

Las tres últimas columnas son las tres decisiones que vienen abajo. La segunda es la
pasada entera: **14,80 s con todo el peso en un rincón, el 23 % del episodio**. No es un
retoque, es una cuarta parte del montaje.

## Tres cosas que no son evidentes

### (a) El lado pelado se decide sobre todo el tramo, no en su punto medio

```python
si = sd = 0.0
t = max(ini, a - holgura)
while t < min(fin, b + holgura):
    i, d, _k, _h = reparto(t)
    si, sd = si + i, sd + d
    t = round(t + paso, 2)
lado = "izquierda" if si <= sd else "derecha"
```

Si se mira solo en `(a+b)/2` y justo ahí no hay nada vivo, los dos lados empatan a cero
y el desempate `si <= sd` manda el contrapeso a la izquierda — **que es justo donde
estaba el elemento al que venía a hacer contrapeso**. Promediar todo el tramo (y 0,30 s
más por cada borde, la `holgura`) hace que el lado lo decida lo que de verdad hay.

Medido pieza a pieza, **4 de los 14 contrapesos cambian de lado** con el punto medio
(`bajo_la_torre`, `jardines_torre` y `guardia_boveda` se van a la izquierda;
`banco_paris_1929`, a la derecha). Y no se ve en las métricas: con el punto medio el
episodio sigue dando 61 elementos, 0 huecos y 0 s descompensado. **Es un fallo que solo
se ve en el vídeo**, y por eso hay que razonarlo en el código.

### (b) Si un vecino estorba, se le recorta la vida a la pieza — no se descarta

```python
estorbos = []
for x0, x1, o, txt in vivas:
    tope = 0.05 if (txt or es_texto(recurso)) else 0.30
    if max(pisa(c, o), pisa(o, c)) >= tope:
        estorbos.append((x0 - 0.15, x1 + 0.15))
hueco = _mayor_libre(t0, t1, estorbos)
if hueco is None or hueco[1] - hueco[0] < 0.7:
    continue
```

`_mayor_libre()` devuelve el tramo más largo de `[t0, t1]` que no pisa ningún intervalo
ocupado. Descartar la pieza entera dejaba fuera contrapesos por culpa de vecinos que
solapaban tres décimas: **ocho elementos menos y 12,60 s descompensados** (columna 3 de
la tabla) — descartar por un roce deja casi el mismo episodio que no tener segunda
pasada.

Y después hay que comprobar que el trozo que queda **cubre el tramo malo de verdad**, no
que le roza un borde: `min(hueco[1], b) - max(hueco[0], a) < min(0.7, (b - a) * 0.6)`.

### (c) Hay que volver a mirar después de colocar

Un contrapeso puesto a la derecha se convierte él mismo en el único elemento del plano y
**abre un hueco nuevo a la izquierda**. El defecto no desaparece: cambia de lado.

```python
fuera = []
for _vuelta in range(4):
    nuevos = [e for e in (colocar(a, b) for a, b in tramos_malos()) if e]
    if not nuevos:
        break
    fuera.extend(nuevos)
return fuera
```

Con una sola vuelta quedan dos tramos que la segunda caza: `6.20 - 7.20` («murió un
hombre») y `56.60 - 57.80` («y aquí vamos a hacer»), 2,20 s en total.
En este episodio bastan dos, pero el bucle va a cuatro y sale por `break`: el coste de
una vuelta de más es una pasada de medida; el de una de menos, un segundo de cuadro
partido.

## Un cuadro vacío no admite el mismo umbral que uno escorado

```python
VACIO = 0.35                                          # el tramo contiene un instante SIN NADA
...
if t - arranque >= (VACIO if hubo_vacio else minimo):  # 'minimo' = 0,9 s: solo escorado
```

Los huecos reales de este episodio duran 0,40 · 0,45 · 0,50 · 0,70 · 0,90 · 1,25 s. Con
el mínimo único de 0,9 s, **tres de los seis quedan por debajo del listón y no se
rellenan nunca**: última columna de la tabla, dos elementos menos y un hueco que
sobrevive. Medio segundo sin nada en pantalla se ve; un tramo meramente escorado, no
tanto. De ahí que sigan siendo dos umbrales y no uno.

## El pool es del bloque, y aun así respeta la memoria

`contrapeso()` recibe sus candidatas por bloque (`CONTRAPESO[nombre]`, cinco por bloque
en `ep01-lustig`) y elige con la misma regla que todo el episodio —gana la que lleva más
tiempo sin salir—, pero si hasta la más olvidada salió hace menos de 25 s, `colocar()`
devuelve `None` y **no se pone nada**. Repetir para tapar un hueco es peor que el
hueco (`253`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Mover el elemento solitario en vez de acompañarlo | El hueco cambia de lado y sigue ahí |
| Decidir el lado en el punto medio del tramo | 4 de 14 contrapesos al lado equivocado, invisible en las métricas |
| Descartar la pieza si un vecino solapa | 8 contrapesos menos y 12,6 s descompensados |
| Colocar y no volver a medir | El contrapeso abre un hueco nuevo enfrente |
| Un solo umbral de duración | Los huecos de 0,4-0,5 s no se rellenan jamás |
| Medir distinto que el auditor | Se arregla algo que nadie comprueba |
| Repetir una pieza para tapar un hueco | Peor que el hueco |

## Relacionado

`11` el hueco prohibido · `12` capas simultáneas · `144` presencia no es superficie ·
`145` la media esconde el suelo · `246` equilibrio del cuadro · `253` la ventana
antirrepetición
