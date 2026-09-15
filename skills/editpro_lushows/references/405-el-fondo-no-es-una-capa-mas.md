# 405 — El fondo no es una capa más

**Qué resuelve:** en la lista del guion visual el fondo parece el elemento cero. No lo es. Es el que
**define el lienzo**, el único que vive la escena entera, el único que se mueve y el que se lleva la mitad
del render. Tratarlo como una capa más produce tres clases de fallo que no se parecen entre sí y que
siempre acaban culpando al elemento equivocado.

---

## 1. Define el lienzo, y con él todas las posiciones

En `overlay`, `W` y `H` son el ancho y el alto del **primer flujo**, no del proyecto. Medido con el mismo
filtro y dos fondos distintos:

```
[0:v]format=rgba[bg];[1:v]format=rgba[a];[bg][a]overlay=x='W*0.5':y='H*0.1'[v];[v]format=rgb24[out]
```

| fondo | salida | el elemento arranca en |
|---|---|---|
| 800 × 450 | 800 × 450 | x = **400** |
| 1280 × 720 | 1280 × 720 | x = **640** |

Las posiciones del guion están escritas en fracciones (`"x": "W*0.04"`, `"y": "H*0.42"`) precisamente para
sobrevivir a eso. Pero la consecuencia va más allá: **si el fondo entra con el tamaño equivocado, la
escena entera cambia de tamaño** y luego la concatenación falla o, peor, `concat -c copy` produce un
fichero que unos reproductores abren y otros no. El motor lo cierra en el propio `zoompan`:

```python
filtros = [f"[0:v]zoompan=z='{z}':d=1:x='{fx}':y='{fy}':s={W}x{H}:fps={FPS},format=rgba[bg]"]
```

`s=1920x1080` es el contrato del lienzo. No es decoración: es lo único que garantiza que las cinco escenas
concatenen.

---

## 2. Es el único que se mueve

Todos los elementos derivan de una posición fija con entrada y deriva (`expr_elemento`). El fondo tiene su
propia gramática de recorrido (`expr_fondo`): `in`, `out`, `diag`, `golpe`. Y ese movimiento es lo que
separa un plano vivo de una diapositiva con calcomanías.

El precio, medido sobre 75 fotogramas a 1920×1080, descomponiendo la cadena paso a paso:

| qué hace | CPU |
|---|---|
| solo codificar un color plano | 1,39 s |
| codificar una **foto** fija escalada a 1920×1080 | 11,20 s |
| **+ `zoompan`** sobre el PNG de 2688 (el fondo real) | **20,61 s** |
| + destello (`eq` con `eval=frame` sobre todo el cuadro) | 21,14 s |

Dos lecturas. **El movimiento del fondo cuesta casi tanto como codificar la imagen** (9,4 s de los 20,6).
Y **el destello es gratis** (+0,53 s): un filtro que evalúa una expresión por fotograma sobre el cuadro ya
compuesto no se nota al lado de un reescalado.

---

## 3. Se lleva la mitad del render

Sobre el episodio real `ep01-lustig` —1.586 fotogramas, 59 elementos vivos, 3.596 fotogramas-capa, ancho
medio declarado 802 px— aplicando los costes medidos arriba:

| partida | CPU estimado | reparto |
|---|---|---|
| fondo (`zoompan` + codificar) | 435,8 s | **55 %** |
| las 59 capas | 352,8 s | 45 % |
| **total** | **13,1 min CPU** | |

El render real anotado en el repo es de **9 min 42 s de reloj** para esos 63,45 s de vídeo. Encaja: en
esta máquina ffmpeg saca un paralelismo medido de ~1,9×, así que 13,1 min de CPU caen justo en ese orden.
*(No he vuelto a lanzar el render completo: otra sesión estaba escribiendo en `salida/` mientras medía.)*

La conclusión que cambia decisiones: **antes de podar elementos para que el render corra, mira el fondo.**
La mitad del presupuesto está ahí, y ahí es donde está el ahorro grande (`408` §5).

---

## 4. Es el único que siempre está vivo

Un elemento tiene `ini`, `fin` y un `enable`. El fondo no: existe desde el primer fotograma hasta el
último, y por eso es el único que puede resolver el hueco. `canales_lushows/11` lo llama el hueco
prohibido: un tramo con cero elementos en pantalla. El fondo nunca lo tapa —está detrás de todo—, pero sí
determina si ese tramo se lee como respiración o como error.

De ahí una asimetría práctica: **un fondo puede estar cargado o vacío, pero nunca puede faltar.** Si
`buscar()` no lo encuentra, la escena no existe; si no encuentra un elemento, la escena sale con un
elemento menos y nadie se entera (`403`).

---

## 5. Las tres reglas que salen de todo esto

1. **El fondo se resuelve primero y se prerreduce una vez.** Nunca entra a tamaño de archivo (`408` §5).
2. **El lienzo se declara explícitamente** (`s=1920x1080`), no se hereda del fichero.
3. **El fondo no compite.** Si el fondo tiene más movimiento, más contraste o más detalle que el elemento
   protagonista, la gente mira el fondo (`204` §1). El fondo es el sitio donde pasa, no lo que pasa.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por hecho que `W` y `H` son los del proyecto | Son los del primer flujo: las posiciones se van a la mitad |
| Omitir `s=1920x1080` en el `zoompan` | El lienzo lo decide el fichero; la concatenación falla o sale corrupta |
| Poner el fondo como segunda entrada del `overlay` | El lienzo se recorta al tamaño de la capa |
| Podar elementos para acelerar el render | El 55 % del coste es el fondo |
| Fondo con más movimiento o contraste que el sujeto | La gente mira el fondo |
| Fondo distinto de tamaño entre escenas | `concat -c copy` produce un fichero que no todos los reproductores abren |
| Tratar la falta de fondo como la falta de un elemento | Sin fondo no hay escena; sin elemento, la escena sale muda y sin aviso |

## Relacionado

`400` el orden de render es narrativo · `404` acumular o sustituir · `408` lo que cuesta cada capa ·
`409` depurar un apilado · `102` filtros de vídeo · `104` filter_complex · `105` superponer capas ·
`204` §1 el modelo de las cuatro capas · `canales_lushows/50` sistema de fondos ·
`canales_lushows/11` el hueco prohibido · `canales_lushows/248` pre-escalado y caché
