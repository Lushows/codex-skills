# 246 · Equilibrio del cuadro

**Qué resuelve:** entre las posiciones válidas, cuál se elige. Es la decisión que
reparte el peso del collage, y estuvo mal planteada desde el principio por un motivo
que cuesta ver: **el equilibrio se medía como si el plano fuera estático, y el cuadro se
juzga instante a instante.**

---

## El fallo

La regla original decía: si el elemento nuevo coincide con alguien, gana la posición más
lejana al centro de gravedad de lo que ya está en pantalla (equilibra); si no coincide
con nadie, gana la más cercana al centro del lienzo (no se queda arrinconado).

«Coincidir» era un sí/no: bastaba con solapar **un instante** con la vida del nuevo.

Ahí está el agujero. Un recorte de 2,6 s mandado al extremo derecho para compensar a un
vecino de la izquierda que solo vive 0,3 s de esos 2,6 **se queda solo en ese extremo
durante los otros 2,3**, con la mitad izquierda del cuadro desierta. El sistema lo dio
por equilibrado porque en algún momento hubo alguien enfrente. En el diagnóstico del día
en que se cazó, siete de los ocho tramos descompensados del episodio eran exactamente
eso: **14,6 s, el 23 % del minuto**.

## El arreglo: el vecino pesa por el tiempo que comparte

```python
vida = max(1e-6, t1 - t0)
cx = cy = masa = comp = 0.0
for a, b, o, _t in vivos:
    if o is None:
        continue
    solape = min(t1, b) - max(t0, a)
    if solape <= 0:
        continue
    f = solape / vida
    m = (o[2] - o[0]) * (o[3] - o[1]) * f
    cx += (o[0] + o[2]) / 2 * m
    cy += (o[1] + o[3]) / 2 * m
    masa += m
    comp = max(comp, f)       # 0 = vive solo · 1 = acompanado toda su vida
if masa:
    cx, cy = cx / masa, cy / masa
else:
    cx, cy = W_LIENZO / 2, H_LIENZO / 2
```

Dos cosas cambian a la vez y las dos importan:

1. **La masa del vecino se pondera por `f`**, la fracción de vida compartida. Un vecino
   que acompaña tres décimas pesa tres décimas; uno que acompaña siempre pesa entero. El
   centro de gravedad deja de ser el de un fotograma imaginario y pasa a ser el promedio
   real de lo que se ve mientras el elemento está vivo.
2. **`comp` deja de ser booleano.** Es el mayor `f` de todos los vecinos: cuánto de
   acompañado está este elemento en el mejor de los casos.

## La nota

```python
px_, py_ = (c[0] + c[2]) / 2, (c[1] + c[3]) / 2
# las dos fuerzas, en la misma unidad (diagonales del lienzo):
#   d  = lejos del centro de gravedad  -> equilibra el plano lleno
#   dc = cerca del centro del cuadro   -> salva el plano de uno solo
d = ((px_ - cx) ** 2 + (py_ - cy) ** 2) ** 0.5 / DIAGONAL
dc = ((px_ - W_LIENZO / 2) ** 2 +
      (py_ - H_LIENZO / 2) ** 2) ** 0.5 / DIAGONAL
nota = (comp * d + (1 - comp) * (0.5 - dc)) * (1 - choque)
```

`comp` **interpola entre las dos fuerzas** en vez de elegir una. Con `comp = 1` la nota
es pura centrifugación; con `comp = 0` es pura atracción al centro; con `comp = 0,4` el
elemento se aleja un poco del vecino pero sin irse al borde, que es exactamente lo que
pedía el caso de los 2,3 s en solitario.

Tres detalles que hacen que la fórmula funcione y que se pierden si se reescribe a ojo:

- **Las dos distancias se normalizan por la diagonal del lienzo** (2202,9 px). Sin eso
  se estarían sumando píxeles con píxeles de escalas distintas y el término dominante
  sería siempre el mismo.
- **`0.5 - dc`** invierte el signo para que las dos fuerzas se maximicen igual, y el 0,5
  las pone en rangos comparables: `dc` nunca pasa de 0,5 porque media diagonal es la
  distancia máxima del centro a una esquina.
- **`(1 - choque)`** multiplica, no resta. Una posición que pisa un 30 % a una foto no
  se descarta, se penaliza proporcionalmente; así una posición algo sucia pero bien
  colocada puede ganarle a una limpia y arrinconada.

## Lo que cuesta la regla binaria

Mismo episodio, misma tabla, sustituyendo `comp = max(comp, f)` por `comp = 1.0` — es
decir, volviendo a «si hay alguien, aléjate»:

| | fracción (hoy) | binaria (regla vieja) |
|---|---|---|
| elementos | 61 | 63 |
| cobertura media | 38,0 % | 39,7 % |
| cuadro casi vacío | **2,40 s** | 2,95 s |
| **cuadro descompensado** | **0,00 s** | **1,00 s** |
| centro de gravedad de la capa AUTO | **962 px** | 1045 px |
| contrapesos colocados | 14 (6 izq / 8 der) | 14 (9 izq / 5 der) |

El número que lo dice todo es el penúltimo. El lienzo mide 1920, su eje está en 960: con
la regla de fracción la capa automática se apoya en **962 px**, dos píxeles del centro.
Con la binaria se va a **1045**, 85 px escorada a la derecha, porque todo elemento con
un vecino cualquiera huye hacia fuera y casi todos huyen hacia el mismo lado.

Y el resto de la tabla muestra el precio de arreglarlo tarde: la segunda pasada tiene que
gastar **dos elementos más** y nueve de sus catorce contrapesos en la izquierda para
recoger el desastre, y aun así queda un segundo descompensado. La regla binaria no
produce un episodio malo — produce uno **más caro y peor repartido**.

## Por qué no basta con esto

El equilibrio elige entre posiciones **de un elemento que ya existe**. Un plano con un
solo elemento vivo no tiene equilibrio posible: se puede centrar, y ya. Ese caso se
resuelve poniendo algo enfrente, no moviendo lo que hay, y es la segunda pasada (`247`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tratar «acompañado» como sí/no | El elemento se queda solo en el extremo al morir el vecino |
| Medir el centro de gravedad sin ponderar por tiempo | Se equilibra contra un fotograma que nunca existe |
| Sumar distancias sin normalizar por la diagonal | Un término domina siempre y la otra fuerza no hace nada |
| Descartar toda posición con solape | Se pierden posiciones bien colocadas por ensuciar un 10 % |
| Coger la primera posición libre de la banda | Todo el peso a un lado, media pantalla desierta |
| Creer que el equilibrio arregla el plano de uno | Solo cambia de lado el hueco (`247`) |

## Relacionado

`20` retícula del collage · `21` peso visual y jerarquía · `28` respiración del cuadro ·
`243` bandas y anclaje central · `247` el primer elemento del plano · `148` el cuadro de
mando
