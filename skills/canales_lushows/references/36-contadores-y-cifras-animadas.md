# 36 · Contadores y cifras animadas

**Qué resuelve:** una cifra en pantalla es un dato; una cifra que **sube** es una escena.
En un canal de historias de dinero el contador es el único momento en que el material
estático hace algo inesperado, y cuesta lo mismo que un rótulo: son PNG del mismo Chrome.

---

## Cuántos estados hacen falta

No hay animación de texto en ffmpeg que sirva. Se generan **N estados** del número como
PNG y se sustituyen con `overlay` + `enable`. El ojo lo lee como un contador.

| Magnitud | Valor |
|---|---|
| Suelo por estado | **2 fotogramas = 0,08 s** (por debajo, parpadeo) |
| Estado cómodo | **0,10 - 0,12 s** |
| Rodaje total de la cifra | **0,9 - 1,4 s** |

```
N = duración / 0,11      →   1,2 s / 0,11 ≈ 11 estados
```

Menos de 8 estados se lee como tres cortes, no como contador. Más de 16 es render
tirado: por encima de 12 cambios por segundo el ojo ya no distingue los dígitos.

## Qué valor lleva cada estado

Los estados se reparten **iguales en el tiempo**, pero el **valor** sigue una easeOut: el
contador desacelera y los últimos quedan quietos el tiempo suficiente para leerse. Es la
diferencia entre un contador y un número que parpadea.

```python
def estados(v0, v1, n):
    out = []
    for i in range(n):
        u = i / (n - 1)
        out.append(round(v0 + (v1 - v0) * (1 - (1 - u) ** 3)))
    return out

# estados(0, 84_000_000, 11) → 0 · 23.058.000 · 41.664.000 · 55.788.000 · 66.150.000
#   73.500.000 · 78.456.000 · 81.564.000 · 83.328.000 · 83.916.000 · 84.000.000
```

Los tres últimos casi no cambian: el número ya está legible cuando la voz lo dice.

## El montaje

```bash
# 11 estados desde el segundo 2,00, 0,11 s cada uno
ffmpeg -loop 1 -t 6 -i fondo.png \
       -loop 1 -i cifra_00.png -loop 1 -i cifra_01.png ... \
  -filter_complex "
[0:v]scale=4320:-2,zoompan=...:s=1920x1080:fps=25[bg];
[1:v]format=rgba[s0];[2:v]format=rgba[s1];
[11:v]format=rgba,
      scale=w='iw*(1.00+0.06*(1-clip((t-3.10)/0.14,0,1)))':h=-1:eval=frame[s10];
[bg][s0]overlay=x='(W-w)/2':y='500-h/2':enable='gte(t,2.00)*lt(t,2.11)'[v0];
[v0][s1]overlay=x='(W-w)/2':y='500-h/2':enable='gte(t,2.11)*lt(t,2.22)'[v1];
...
[v9][s10]overlay=x='(W-w)/2':y='500-h/2':enable='gte(t,3.10)'[v]
" -map "[v]" -r 25 -y plano.mp4
```

Detalles que no son opcionales:

- **`gte(t,a)*lt(t,b)`, nunca `between(t,a,b)`:** `between` es inclusivo por los dos lados
  y en el fotograma de la frontera se dibujan dos estados a la vez
- **El último estado se queda** (`enable` sin cierre) y recibe un golpe de escala de 1,06
  a 1,00 en 0,14 s, con sonido. Es el remate de la cifra
- **El golpe se aplica al elemento, antes del `overlay`;** después escalaría el cuadro
- **`x='(W-w)/2'`, `y='500-h/2'`** anclan por el centro, así el golpe no desplaza la
  cifra. Solo funciona si todos los PNG miden lo mismo

### Los PNG tienen que medir igual

Error nº 1 del contador: si cada PNG se genera al ancho de su número, la cifra **salta**.

- Lienzo de **ancho fijo**, calculado sobre el valor más largo; números alineados a la
  derecha dentro de ese lienzo
- Tipografía con **cifras tabulares** (`font-variant-numeric: tabular-nums` en el HTML):
  sin eso el 1 es más estrecho que el 8 y el número tiembla aunque el lienzo sea fijo
- Separador de miles desde el primer estado, nunca a mitad de camino

## Barras que crecen

Una barra es un PNG revelado de izquierda a derecha. **No se hace con `crop`:** `crop`
evalúa `w` y `h` una sola vez al inicializar el filtro y una anchura con `t` dentro
aborta el render con *«Error when evaluating the expression»*. El revelado se hace
recortando el **canal alfa** con `geq`, que sí evalúa por fotograma:

```bash
[1:v]format=rgba,
     geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':
         a='if(lt(X, W*(1-pow(1-clip((T-2.30)/0.90,0,1),3))), alpha(X,Y), 0)'[barra];
[bg][barra]overlay=x=280:y=620:enable='gte(t,2.30)'
```

- En `geq` el reloj es **`T` mayúscula**, no `t`; `X`/`Y` son el píxel y `W`/`H` el
  tamaño del elemento. `alpha(X,Y)` devuelve el alfa original, así que el antialias del
  borde se conserva
- El lienzo no cambia de tamaño: la barra no "camina" y no hace falta `pad`
- `geq` evalúa píxel a píxel: el PNG debe medir lo que mide la barra, no 1920x1080
- **0,7 a 1,1 s** de crecimiento, con easeOut: llega y se asienta
- Dos barras que se comparan crecen **a la vez**: la comparación es el dato
- La barra sin su cifra no dice nada; la cifra entra cuando la barra termina

## Mapas y trazados que se dibujan

Una ruta de dinero se dibuja por **segmentos**: cada tramo es un PNG propio y entran
encadenados. Un solo `crop` no sirve: avanza en un eje y una ruta real gira.

```python
{"r": "ruta_01", "t0": 3.10, "escribir": 0.28},   # Medellín → Panamá
{"r": "ruta_02", "t0": 3.34, "escribir": 0.26},   # Panamá → Miami
{"r": "ruta_03", "t0": 3.56, "escribir": 0.30},   # Miami → Zúrich
```

Cada segmento se solapa un fotograma (**0,04 s**) con el anterior para que la línea no
parpadee en la unión. El punto y el rótulo de cada nodo entran 0,10 s **después** de que
llegue la línea. Ritmo: **0,25-0,35 s por tramo**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| PNG de ancho variable | La cifra salta de posición en cada estado |
| Tipografía sin cifras tabulares | El número tiembla aunque el lienzo sea fijo |
| `between(t,a,b)` en los `enable` | Dos estados dibujados en el fotograma de la frontera |
| Valores repartidos lineales | Se lee como parpadeo, no como contador |
| Menos de 0,08 s por estado | Parpadeo ilegible |
| `crop` con `w` dependiente de `t` | El render aborta: `crop` solo evalúa `w`/`h` al iniciar |
| `t` minúscula dentro de `geq` | No existe esa variable ahí; el reloj es `T` |
| Contador sin sonido en el remate | El golpe final se queda a medias |
| La cifra sigue subiendo cuando la voz ya la dijo | El dato llega después de su palabra (`39`) |

## Relacionado

`27` composición de datos · `31` curvas de aceleración · `35` animar una foto fija ·
`41` máquina de escribir · `44` la cifra en pantalla · `89` biblioteca de sonido
