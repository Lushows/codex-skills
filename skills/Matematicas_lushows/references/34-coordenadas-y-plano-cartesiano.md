# 34 · Coordenadas y plano cartesiano

> **Qué resuelve / cuándo usarlo** — Ubicar puntos en un plano y medir relaciones entre ellos: distancia (¿qué tan lejos?), punto medio (¿dónde queda el centro?), pendiente (¿qué tan inclinada va una tendencia?) y la ecuación de la recta (la fórmula de una línea). Es la base de gráficos, mapas, layouts de diseño y de cualquier tendencia lineal en datos.

## Concepto (para no-experto)

Imagina un mapa de una ciudad con calles numeradas. Para decir dónde está un local no basta una sola dirección: necesitas dos números — cuántas cuadras al **este** y cuántas al **norte**. El **plano cartesiano** hace exactamente eso con dos rectas perpendiculares:

- **Eje X** (horizontal, "abscisa"): cuánto te mueves a izquierda/derecha.
- **Eje Y** (vertical, "ordenada"): cuánto te mueves abajo/arriba.
- **Origen**: el punto donde se cruzan, las coordenadas (0, 0).

Un **punto** es un par ordenado `(x, y)`. "Ordenado" significa que el orden importa: `(3, 5)` no es lo mismo que `(5, 3)`, igual que "3 cuadras al este y 5 al norte" no es lo mismo que al revés.

Sobre eso construimos cuatro herramientas:

- **Distancia entre dos puntos**: la longitud de la línea recta que los une (en línea de pájaro, no por las calles).
- **Punto medio**: el punto que queda justo a mitad de camino entre dos puntos (el "promedio" de sus coordenadas).
- **Pendiente** (en inglés *slope*): qué tan inclinada está una recta. Es "cuánto sube por cada paso que avanza a la derecha". Una rampa empinada tiene pendiente grande; un piso plano tiene pendiente 0.
- **Ecuación de la recta**: la fórmula que describe TODOS los puntos de esa línea. Sirve para predecir: si las ventas suben de forma lineal, la recta te dice cuánto venderás el mes que viene.

## Fórmulas / método

Dados dos puntos `A = (x₁, y₁)` y `B = (x₂, y₂)`:

**Distancia** (Pitágoras aplicado a las diferencias de coordenadas):
```
d(A,B) = √[ (x₂ − x₁)² + (y₂ − y₁)² ]
```
La diferencia en X (`Δx = x₂ − x₁`) es un cateto, la diferencia en Y (`Δy`) es el otro, y la distancia es la hipotenusa. Unidad: la misma de los ejes (m, km, px, $...).

**Punto medio** (promedio de cada coordenada):
```
M = ( (x₁ + x₂)/2 , (y₁ + y₂)/2 )
```

**Pendiente** (subida sobre avance):
```
m = (y₂ − y₁) / (x₂ − x₁) = Δy / Δx        (requiere x₁ ≠ x₂)
```
Si `x₁ = x₂` la recta es **vertical** y la pendiente NO existe (división por cero).

**Ecuación de la recta**:
- Punto-pendiente:  `y − y₁ = m·(x − x₁)`
- Pendiente-ordenada (la más usada): `y = m·x + b`, donde `b` es la **ordenada al origen** (el valor de y cuando x = 0, o sea dónde la recta cruza el eje Y).
- Forma general:  `A·x + B·y + C = 0`.

Símbolos: `m` = pendiente, `b` = intercepto en Y, `Δ` (delta) = "diferencia/cambio de".

## Verificación en código

Usamos `fractions.Fraction` para que la pendiente sea EXACTA (sin error de float) y `decimal`/`sympy` para la distancia.

```python
from fractions import Fraction
from decimal import Decimal, getcontext
import sympy as sp

getcontext().prec = 30

# --- Datos: dos puntos ---
A = (Fraction(2), Fraction(3))
B = (Fraction(8), Fraction(11))
(x1, y1), (x2, y2) = A, B

# --- 1) Distancia (exacta con sympy: deja la raíz simbólica) ---
dx = x2 - x1                      # = 6
dy = y2 - y1                      # = 8
dist_exacta = sp.sqrt(dx**2 + dy**2)         # = sqrt(100) = 10
print("Distancia exacta:", dist_exacta)      # 10

# --- 2) Punto medio (promedio coordenada a coordenada) ---
M = ((x1 + x2) / 2, (y1 + y2) / 2)
print("Punto medio:", M)                     # (5, 7)

# --- 3) Pendiente (Fraction => exacta, sin float) ---
assert x2 != x1, "Recta vertical: pendiente indefinida"
m = Fraction(dy, dx)                          # 8/6 = 4/3
print("Pendiente m:", m)                      # 4/3

# --- 4) Ecuación y = m x + b  ->  b = y1 - m*x1 ---
b = y1 - m * x1                               # 3 - (4/3)*2 = 1/3
print(f"Recta: y = {m} x + {b}")             # y = 4/3 x + 1/3
```

Verificación por segunda vía (otro método + sympy + asserts):

```python
# (a) Distancia por decimal independiente y comprobando con el cuadrado
d_dec = (Decimal(dx)**2 + Decimal(dy)**2).sqrt()
assert d_dec == Decimal(10)                      # raíz cuadrada coincide
assert dx**2 + dy**2 == 100                       # inverso: elevar al cuadrado

# (b) La recta DEBE pasar por A y por B (sustituir y verificar identidad)
for (px, py) in (A, B):
    assert m * px + b == py, f"La recta no pasa por ({px},{py})"

# (c) El punto medio equidista de A y B (mismas distancias a cada extremo)
mx, my = M
dAM = sp.sqrt((mx - x1)**2 + (my - y1)**2)
dBM = sp.sqrt((mx - x2)**2 + (my - y2)**2)
assert sp.simplify(dAM - dBM) == 0               # distancias iguales => es el medio

# (d) Pendiente con sympy de forma totalmente independiente
xs = sp.symbols('xs')
recta = sp.Eq(sp.Symbol('y'), sp.Rational(4,3)*xs + sp.Rational(1,3))
sol = sp.solve(recta.subs(xs, 8), sp.Symbol('y'))[0]
assert sol == 11                                  # en x=8 la recta da y=11 (=B)
print("Todas las verificaciones OK")
```

## Ejemplo trabajado (negocio LatAm)

Una cafetería en Bogotá midió clientes en dos meses y quiere proyectar el siguiente, asumiendo crecimiento lineal.

- Mes 1: 120 clientes → punto `A = (1, 120)`
- Mes 3: 180 clientes → punto `B = (3, 180)`

**Paso 1 — Pendiente** (cuántos clientes gana por mes):
```
m = Δy/Δx = (180 − 120) / (3 − 1) = 60 / 2 = 30 clientes/mes
```
Unidad clave: la pendiente NO es adimensional, es **30 clientes por mes**.

**Paso 2 — Ecuación de la recta** (`y = m·x + b`), usando A:
```
b = y₁ − m·x₁ = 120 − 30·1 = 90 clientes
→  y = 30·x + 90
```
Lectura de negocio: `b = 90` es el "punto de partida" teórico en el mes 0; cada mes suma 30.

**Paso 3 — Proyección del mes 4**:
```
y(4) = 30·4 + 90 = 210 clientes
```

**Paso 4 — Punto medio** (promedio entre los dos meses medidos):
```
M = ( (1+3)/2 , (120+180)/2 ) = (2, 150)  →  150 clientes en el mes 2
```

**Verificación**: la recta debe pasar por A y B. En x=1: `30·1+90 = 120` ✓. En x=3: `30·3+90 = 180` ✓. La proyección de **210 clientes** para el mes 4 es coherente (sigue subiendo de a 30). Resultado: **+30 clientes/mes**, proyección mes 4 = **210 clientes**.

> Honestidad sobre la incertidumbre: una recta con solo 2 puntos es una suposición fuerte (crecimiento perfectamente lineal). Para decisiones de dinero, valida con más datos y mira [[64-regresion-lineal]] antes de comprometerte.

## Errores comunes / trampas

- **Invertir x e y** al escribir el punto: `(y, x)` en vez de `(x, y)`. Mantén siempre X primero (horizontal).
- **Restar las coordenadas en orden distinto** arriba y abajo de la pendiente: usa el MISMO orden para Δy y Δx (`y₂−y₁` con `x₂−x₁`). Invertir solo uno cambia el signo y arruina la inclinación.
- **Olvidar el caso vertical** (`x₁ = x₂`): la pendiente es indefinida, no cero. Cero es horizontal. Confundirlos es un error clásico.
- **Distancia sin elevar al cuadrado** o sin la raíz: la fórmula no es `Δx + Δy`; es la raíz de la suma de los cuadrados (es Pitágoras, ver [[32-teorema-de-pitagoras-y-triangulos]]).
- **Calcular pendiente con float** y arrastrar errores (`8/6 = 1.3333...`): usa `Fraction` para mantenerla exacta.
- **Confundir pendiente con ángulo**: la pendiente es la razón Δy/Δx, no los grados. Para grados usa `arctan(m)` ([[33-trigonometria]]).
- **Redondear a mitad de camino**: calcula todo exacto y redondea UNA vez al final ([[05-cifras-significativas-y-redondeo]]).

### Mini-checklist de exactitud
- [ ] Verifiqué que la recta `y = mx + b` pasa por AMBOS puntos dados (sustitución).
- [ ] La distancia la confirmé por segunda vía (cuadrado inverso o decimal independiente) y lleva unidades.
- [ ] Revisé el caso `x₁ = x₂` (vertical) antes de dividir, para no dividir por cero.

## Cruces
- [[32-teorema-de-pitagoras-y-triangulos]] — la distancia es Pitágoras aplicado a Δx y Δy.
- [[26-funciones-lineales-y-afines]] — `y = mx + b` es una función lineal/afín.
- [[35-vectores]] — un punto y las diferencias Δx, Δy son vectores en el plano.
- [[64-regresion-lineal]] — cuando hay muchos puntos, se ajusta la "mejor recta".
- [[33-trigonometria]] — convertir pendiente en ángulo de inclinación.
