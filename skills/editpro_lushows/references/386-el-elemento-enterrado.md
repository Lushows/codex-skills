# 386 — El elemento enterrado

**Qué resuelve:** el peor caso de la pisada no es el mordisco, es el elemento que **no se ve en absoluto**.
Se paga un recurso, se paga un evento, se paga el render, y en pantalla no hay nada. Y es el defecto que
peor se detecta: no rompe nada, no da error, no baja ninguna métrica. Mejora la sensación de densidad.

---

## 1. El caso, tal como está escrito en el código

Está en el docstring de `pisa()`, en `diccionario.py:365`:

> *Las BANDAS reservan posiciones, pero 'centro' y 'lado' se cruzan en el lienzo: reservar la banda no
> impedía que un elemento cayera encima de otro. **En el episodio 01 un retrato quedó 100% enterrado 1,8 s
> bajo un organigrama y solo se descubrió mirando la grilla, ya renderizada.** Ahora se comprueba el
> rectángulo de verdad, no la etiqueta de la banda.*

Y hay un segundo del mismo tipo anotado en `auditar.py`: la ficha del juicio enterrada bajo la foto del
tribunal, descubierta también en la grilla y también después de renderizar.

Las dos veces el mecanismo fue idéntico: **el sistema comprobaba una etiqueta (la banda) en vez del
rectángulo.** Dos elementos con banda distinta pueden ocupar el mismo sitio; «centro» y «lado» se cruzan en
un lienzo de 1920×1080. La etiqueta decía que estaban separados. Los píxeles decían lo contrario.

Lo que costó cada una: un recurso curado, recortado y preescalado (10–30 min); un evento del presupuesto
del bloque, que además **mejora** la sensación de densidad; el render de la escena (50–309 s); la grilla
para encontrarlo (40,3 s, y solo si ya renderizaste); y el render entero otra vez para arreglarlo.

---

## 2. Por qué la auditoría no lo caza

`auditar.py` tiene su propio chequeo de oclusión, en la línea 563:

```python
tapados = []
for i, (a1, b1, e1, r1, _, c1) in enumerate(vidas):        # vidas ORDENADAS POR TIEMPO
    ...
    for a2, b2, e2, r2, _, c2 in vidas[i + 1:]:
        if c2 is None or a2 >= b1 or e1 != e2:
            continue
        ...
        if propia > 0 and sx * sy / propia > 0.55:
            tapados.append(...)
```

El comentario de arriba lo dice: *«Un elemento que entra DESPUÉS se pinta encima»*. **Y eso no es verdad.**
`motor.py` encadena los overlays en el orden de la lista de elementos, no en el orden de entrada (`380`
§2). Medido hoy sobre las dos versiones del episodio 01:

| Episodio | Parejas simultáneas | Orden de capa ≠ orden de entrada |
|---|---|---|
| `ep01-lustig` | 96 | **30 (31%)** |
| `episodio01` | 93 | **27 (29%)** |

En una de cada tres parejas el chequeo mide **en la dirección contraria**: calcula cuánto tapa el de abajo
al de arriba. Ese número no significa nada y casi nunca pasa del 55%, así que el chequeo calla.

Y calla de verdad: corriendo hoy `python auditar.py ep01-lustig` y `python auditar.py episodio01`, **la
sección «elementos TAPADOS» no aparece en ninguno de los dos**. Cero hallazgos.

Rehaciendo la misma comprobación con la capa real —índice en la lista— `episodio01` da **nueve**:
`fajo` bajo `camiones` (77%, 0,14 s y 71%, 0,84 s), los cuatro `usd_*` bajo `dinero_real` (52%, 49%, 48% y
47%), y tres piezas de texto: `t_maquina` bajo `dinero_real` (17%), `t_ningun` bajo `boveda` (16%, 2,45 s)
y `t_maquina` bajo `prensa_vieja` (15%).

---

## 3. Y ahora la parte honesta: tres de esos nueve no existen

Pasando esas mismas parejas por la medida de tinta (`381`):

| El de abajo | Rectángulo | Tinta real |
|---|---|---|
| `usd_11` bajo `dinero_real` | 47,9% | **4,3%** |
| `t_maquina` bajo `dinero_real` | 16,9% | **1,8%** |
| `t_ningun` bajo `boveda` | 15,6% | **0,0%** |

Los cuatro `usd_*` son cifras sueltas sobre transparente con un 11% de tinta: el recorte cae en el aire del
PNG. Los dos `fajo` bajo `camiones` sí son reales (78,9% y 66,9% de tinta tapada).

> **La lección completa, que es lo que hace útil este módulo:** el chequeo de enterramiento falla **dos
> veces seguidas**. Primero por ordenar la pareja por reloj en vez de por capa —y se le escapa todo—, y
> luego, si se corrige solo eso, por medir el rectángulo en vez del contenido —y grita por cosas que no
> pasan. Hay que arreglar las dos o el comprobador acaba desconectado.

---

## 4. La definición de «enterrado» que sí se sostiene

Un elemento está enterrado cuando se cumplen las tres:

1. **más del 55% de su tinta** queda bajo elementos de capa superior,
2. **durante más de 0,6 s** de ventana visible (`385`),
3. **y lo que queda visible no incluye su zona protegida** (`382`).

Y la compuerta: **ningún elemento enterrado se renderiza.** No es un aviso, es un `raise`. Un elemento
enterrado no tiene arreglo en post: o se mueve, o se acorta, o se quita. Las tres cosas cuestan segundos en
la tabla de eventos y minutos en el render.

```python
if v_tinta > 0.55 and dur_visible > 0.6:
    raise SystemExit(
        f"ENTERRADO: '{bajo}' queda al {v_tinta:.0%} bajo '{arriba}' durante "
        f"{dur_visible:.2f} s en {escena}. Se paga el elemento y no se ve.")
```

---

## 5. Cómo se descubrió y cómo no hay que volver a descubrirlo

La grilla de fotogramas del episodio ya renderizado. Funciona, y hay que seguir haciéndola, pero es la
**última** red, no la primera:

```bash
# 64 fotogramas a 2 por segundo, del episodio ya montado
ffmpeg -y -v error -i _mudo.mp4 -vf "fps=2,scale=320:-1,tile=8x8" \
  -frames:v 1 -q:v 3 _grid.jpg
```

Medido sobre `ep01-lustig/salida/_mudo.mp4` (63,44 s): **40,3 s**. Contra los 0,31 s que cuesta el censo de
las 96 parejas. Y la grilla solo sirve si ya has renderizado, es decir, si ya has pagado los diez o quince
minutos de ffmpeg.

El orden correcto de las tres redes:

| Orden | Red | Coste | Qué caza |
|---|---|---|---|
| 1 | compuerta de colocación (`383`) | ~0 s | impide que la pisada nazca |
| 2 | censo de pisadas (`384`) | 0,31 s | lo que se coló entre los elementos escritos a mano |
| 3 | grilla de fotogramas | 40,3 s + el render | lo que el modelo geométrico no sabe ver |

La tercera nunca desaparece: la grilla ve lo que ningún rectángulo modela —un recorte oscuro sobre un fondo
oscuro, una silueta que se confunde con otra— y para eso está `canales_lushows/160`–`169`, que es la
verificación por ojo del episodio. Aquí solo se dice **cuándo** se llega a ella: ya sin pisadas medibles.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Suponer que el que entra después va encima | El chequeo mira al revés en el 30% de las parejas y no reporta nada |
| Comprobar la **banda** en vez del rectángulo | «Centro» y «lado» se cruzan: el retrato enterrado 1,8 s |
| Corregir la capa y seguir midiendo el rectángulo | Tres alarmas de nueve son aire del PNG (`381`) |
| Usar el mismo umbral para enterrado y para pisada | 0,55 sirve para enterrar; para texto el listón es 0,05 (`383`) |
| Reportar el enterramiento en vez de abortar | Se renderizan diez minutos de un elemento que no se ve |
| Dejar la grilla como única red | Se descubre el fallo cuando ya se pagó todo el render |
| Quitar la grilla porque el censo sale limpio | El censo no ve contraste ni siluetas (`canales_lushows/163`) |

## Relacionado

`380` qué es pisar en números · `381` el área que importa · `383` umbrales por tipo de contenido ·
`384` medir el solape antes de renderizar · `385` la pisada que dura · `388` informar una pisada ·
`98` verificación del corte · `canales_lushows/160` la grilla de fotogramas ·
`canales_lushows/150` catálogo del fallo silencioso
