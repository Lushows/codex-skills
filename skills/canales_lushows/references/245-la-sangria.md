# 245 · La sangría

**Qué resuelve:** cuánto se le deja salir del lienzo a un recorte. Un poco de sangría se
lee como página que se sale, que es el lenguaje del collage; demasiada es un elemento
cortado, y el ojo del espectador distingue las dos cosas al instante.

---

## Una constante con nombre

```python
SANGRE = 0.022     # cuanto puede salirse un recorte por cada borde. Con 0,07
                   # un elemento de 940 px se iba un 31% fuera del lienzo.
```

2,2 % del lienzo son **42 px por el lado horizontal y 24 px por el vertical**. Parece
poquísimo y es justo lo que hace falta: la sangría no es un efecto, es la holgura que
permite que el encaje mueva el elemento sin que se note el empujón.

Se aplica en `rect()`, y solo cuando se pide encajar:

```python
if encajar:
    mx, my = W_LIENZO * SANGRE, H_LIENZO * SANGRE
    x = min(max(x, -mx), W_LIENZO + mx - ancho)
    y = min(max(y, -my), H_LIENZO + my - alto)
```

Correr hacia dentro en vez de descartar es lo que conserva la densidad: un elemento que
solo necesitaba moverse 30 px no tiene por qué perderse.

## Lo que pasa al aflojarla

Mismo episodio, misma tabla, cambiando solo la constante. El porcentaje es la
superficie del elemento que queda fuera del lienzo de 1920×1080:

| `SANGRE` | Margen | Máximo fuera del cuadro | Elementos con más del 12 % fuera |
|---|---|---|---|
| **0,022** | 42 × 24 px | **9 %** (`torre_utrillo`) | **0** |
| 0,045 | 86 × 49 px | 18 % (`calle_paris`) | 9 |
| 0,070 | 134 × 76 px | 25 % (`celda_catre`) | 12 |
| 0,120 | 230 × 130 px | 33 % (`torre_aerea`) | 22 |

La curva es brutal: **doblar la sangría dispara de 0 a 9 los elementos que el auditor
marca**, y a partir de ahí sube casi lineal. Con 0,12 son 22 de 61 elementos, más de un
tercio del episodio con un pedazo fuera del cuadro.

Y el salto de 0 a 9 en el primer escalón no es casualidad. La mayoría de los elementos
del episodio quedan justo al borde de la tolerancia: el encaje los pega contra el límite
que se le dé. **La constante no describe lo que pasa, lo decide.**

## Dos sangrías distintas y no se mezclan

`SANGRE` gobierna el **encaje**. `cabe()` gobierna el **descarte**, y usa otra:

```python
def cabe(c, sangre=0.10):
    mx, my = W_LIENZO * sangre, H_LIENZO * sangre
    return (c[2] - c[0] <= W_LIENZO + 2 * mx
            and c[3] - c[1] <= H_LIENZO + 2 * my)
```

Ojo a lo que compara: **el tamaño del rectángulo, no su posición**. `cabe()` no pregunta
«¿está dentro?», pregunta «¿podría estarlo?». Un elemento de 2400 px de ancho no cabe se
ponga donde se ponga, y por eso se descarta antes de gastar en él la elección de
posición. Es el cinturón que impidió que el repliegue de banda metiera un retrato de
1280 px en una posición pensada para un rótulo de 520 (`243`).

## El límite lo pone el auditor, no el gusto

El 12 % de la tabla de arriba no es un número inventado: es el umbral de alarma de
`auditar.py`.

```python
fuera_pc = 1 - (dentro_x * dentro_y / propia) if propia else 0
if fuera_pc > 0.12:
    fugados.append((a, e, r, fuera_pc * 100))
```

Con la constante en 0,022 esa sección no se imprime: ni un elemento la dispara. Con
0,070 aparecen ocho en los tres primeros bloques:

```
  --- elementos que se salen del cuadro ---
     4.45  muerte    'galeria_celdas' con el  19% fuera del lienzo
     6.87  muerte    'celda_catre' con el  25% fuera del lienzo
     9.11  muerte    'sin_padre' con el  16% fuera del lienzo
    11.26  muerte    'presos_grabado' con el  16% fuera del lienzo
    17.18  oficio    'r_casilla' con el  14% fuera del lienzo
    18.35  oficio    'imprenta_sellos' con el  16% fuera del lienzo
    29.73  nombre    'aviso_falsos' con el  13% fuera del lienzo
    33.01  nombre    'balanza_02' con el  23% fuera del lienzo
```

La medida se hace con `encajar=False` **a propósito**: hay que medir dónde está el
elemento, no dónde estaría si se le dejara. Medir con el encaje puesto da siempre
resultados preciosos y no mide nada (`142`).

## Cuándo sangrar a propósito

La sangría automática es holgura; la sangría **narrativa** se escribe a mano y es otra
cosa. Un documento que entra por el borde izquierdo ocupando media pantalla y se sale por
arriba dice «esto es un papel de verdad, más grande que el cuadro». Eso se declara con
`x` negativa explícita en la capa CLAVE y se acepta que el auditor lo marque: la alarma
no es una prohibición, es una lista de cosas que hay que haber mirado.

Lo que no vale es llegar ahí por acumulación: nueve elementos al 18 % fuera no son nueve
decisiones, son una constante mal puesta.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Subir `SANGRE` para «que quepa todo» | De 0 a 9 elementos cortados en el primer escalón |
| Confundir `SANGRE` con la de `cabe()` | Se descarta por posición lo que había que descartar por tamaño |
| Medir el fuera de cuadro con `encajar=True` | Sale siempre 0 % y la medida no mide nada |
| Tratar la alarma del 12 % como prohibición | Se pierden las sangrías narrativas escritas a mano |
| Descartar en vez de encajar | Se pierde un elemento que solo necesitaba moverse 30 px |
| Sangrar por el borde inferior | Se cruza la zona de la barra de YouTube (`49`) |

## Relacionado

`25` el borde de papel · `49` zona segura y tamaños · `142` la medida que miente ·
`242` colocación por rectángulo · `243` bandas y anclaje central · `244` el techo de
altura
