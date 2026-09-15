# 23 · Ecuaciones cuadráticas

> **Qué resuelve / cuándo usarlo** — Cualquier relación donde una variable aparece al cuadrado: áreas, trayectorias, y sobre todo problemas de negocio en forma de "parábola" (utilidad máxima, precio óptimo de venta). Te dice los valores de `x` que cumplen la ecuación y dónde está el máximo o mínimo.

## Concepto (para no-experto)

Una **ecuación cuadrática** es una igualdad donde la mayor potencia de la incógnita es el cuadrado (la variable elevada a 2). Su forma estándar es:

```
a·x² + b·x + c = 0
```

donde `a`, `b`, `c` son números conocidos (**coeficientes**) y `a ≠ 0` (si `a` fuera 0 no habría término cuadrático y sería lineal — ver [[21-ecuaciones-lineales]]).

- **Término cuadrático**: `a·x²` (el que manda).
- **Término lineal**: `b·x`.
- **Término independiente** (o constante): `c`.

Si la dibujas en el plano (ver [[34-coordenadas-y-plano-cartesiano]]), una cuadrática es una **parábola**: una curva en forma de "U" (si `a > 0`, abre hacia arriba y tiene un punto mínimo) o de "∩" (si `a < 0`, abre hacia abajo y tiene un punto máximo).

**Analogía cotidiana:** imagina que subes el precio de un producto. Si lo subes poco, vendes mucho pero ganas poco por unidad; si lo subes demasiado, casi nadie compra. La utilidad sube, llega a una **cima** y vuelve a bajar: esa cima es el vértice de una parábola. La ecuación cuadrática te dice exactamente dónde está esa cima y a qué precio "te quedas sin utilidad" (donde la curva cruza el cero, las **raíces**).

Las **raíces** (o **soluciones** o **ceros**) son los valores de `x` donde la parábola toca el eje horizontal, es decir, donde la expresión vale 0.

## Fórmulas / método

**1) Fórmula general (cuadrática)** — siempre funciona:

```
        -b ± √(b² − 4·a·c)
x =  ───────────────────────
              2·a
```

El símbolo `±` significa "más y menos": da **dos** soluciones (una con `+`, otra con `−`).

**2) Discriminante** — la cantidad bajo la raíz; decide cuántas raíces reales hay:

```
Δ (delta) = b² − 4·a·c
```

- `Δ > 0` → **dos** raíces reales distintas (la parábola cruza el eje en 2 puntos).
- `Δ = 0` → **una** raíz real doble (la parábola toca el eje en 1 punto, el vértice).
- `Δ < 0` → **ninguna** raíz real (la parábola no toca el eje; las soluciones son complejas).

**3) Factorización** — si encuentras dos números `r` y `s` tales que la ecuación se escribe `a·(x − r)·(x − s) = 0`, entonces las raíces son `r` y `s` directamente (un producto es 0 solo si uno de sus factores es 0). Rápida cuando los números son "bonitos".

**4) Completar el cuadrado** — reescribe `a·x² + b·x + c` como `a·(x − h)² + k`, donde:

```
h = −b / (2·a)        (coordenada x del vértice)
k = c − b²/(4·a)      (coordenada y del vértice = valor mínimo/máximo)
```

El **vértice** está en `(h, k)`. Esto es lo que usas para **optimizar**: si `a < 0`, `k` es el valor **máximo** (p. ej. utilidad máxima) y se alcanza en `x = h` (p. ej. el precio óptimo).

> Las cuatro vías deben dar el **mismo** resultado. Ese es nuestro chequeo de error cero.

Unidades: `x` lleva la unidad de la incógnita (COP, unidades vendidas, metros…). En `a·x²+b·x+c`, cada término debe tener la misma unidad de salida para que la suma tenga sentido (ver [[04-notacion-unidades-y-dimensiones]]).

## Verificación en código

Usamos `sympy` para resolver de forma **exacta** (sin decimales sucios) y verificamos sustituyendo las raíces de vuelta en la ecuación.

```python
# pip install sympy
from sympy import symbols, Eq, solve, sqrt, Rational, simplify, expand

x = symbols('x')

# Ejemplo: 2x^2 - 7x + 3 = 0
a, b, c = 2, -7, 3

# --- VÍA 1: fórmula general (exacta) ---
disc = b**2 - 4*a*c                  # discriminante
print("Discriminante Δ =", disc)     # > 0  -> dos raíces reales
r1 = (-b + sqrt(disc)) / (2*a)
r2 = (-b - sqrt(disc)) / (2*a)
print("Raíces por fórmula:", r1, r2)  # 3 y 1/2

# --- VÍA 2: solver simbólico (segundo método independiente) ---
sols = solve(Eq(a*x**2 + b*x + c, 0), x)
print("Raíces por solve():", sols)

# --- VERIFICACIÓN: sustituir cada raíz -> debe dar 0 EXACTO ---
for r in sols:
    valor = simplify(a*r**2 + b*r + c)
    assert valor == 0, f"FALLA: la raíz {r} no anula la ecuación (dio {valor})"
print("OK: ambas raíces sustituidas dan 0 exacto")

# --- VERIFICACIÓN 2: relaciones de Vieta (3ª vía) ---
# suma de raíces debe ser -b/a ; producto debe ser c/a
suma = simplify(sols[0] + sols[1])
prod = simplify(sols[0] * sols[1])
assert suma == Rational(-b, a), "FALLA suma de raíces"
assert prod == Rational(c, a), "FALLA producto de raíces"
print("OK Vieta: suma =", suma, "(=-b/a), producto =", prod, "(=c/a)")
```

Salida esperada:

```
Discriminante Δ = 25
Raíces por fórmula: 3 1/2
Raíces por solve(): [1/2, 3]
OK: ambas raíces sustituidas dan 0 exacto
OK Vieta: suma = 7/2 (=-b/a), producto = 3/2 (=c/a)
```

Tres vías coinciden (fórmula, solver, Vieta) y la sustitución da 0 exacto: cero error.

## Ejemplo trabajado

**Problema (negocio, COP).** Vendo la Calculadora de Costos a un precio `p` (en miles de COP). Por estudio de mercado, las unidades vendidas al mes son aproximadamente `q = 600 − 30·p`. La **utilidad** (ignorando costo fijo, producto digital de costo marginal ≈ 0) es ingreso = precio × cantidad:

```
U(p) = p · (600 − 30·p) = 600·p − 30·p²
```

es decir `U(p) = −30·p² + 600·p`. ¿A qué **precio** la utilidad es **máxima** y cuál es esa utilidad?

**Paso 1 — identificar coeficientes** (en la forma `a·p² + b·p + c`): `a = −30`, `b = 600`, `c = 0`. Como `a < 0`, la parábola abre hacia abajo → tiene un **máximo**. Bien.

**Paso 2 — vértice (precio óptimo):**

```
h = −b / (2·a) = −600 / (2·(−30)) = −600 / −60 = 10
```

Precio óptimo `p* = 10` (es decir, **$10.000 COP** porque `p` está en miles).

**Paso 3 — utilidad en el vértice:**

```
k = c − b²/(4·a) = 0 − 600²/(4·(−30)) = −360000 / −120 = 3000
```

Utilidad máxima `= 3000` (en miles de COP) = **$3.000.000 COP/mes**.

**Verificación en código:**

```python
from sympy import symbols, diff, solve, Rational
p = symbols('p')
U = -30*p**2 + 600*p

p_opt = solve(diff(U, p), p)[0]    # derivada = 0 -> óptimo (ver módulo 43)
print("Precio óptimo:", p_opt)     # 10
print("Utilidad máx:", U.subs(p, p_opt))  # 3000

# Segunda vía: fórmula del vértice h=-b/2a, k=U(h)
a, b = -30, 600
h = Rational(-b, 2*a)
assert h == p_opt
print("OK vértice coincide con derivada:", h)
```

**Resultado:** precio óptimo **$10.000 COP** (coincide con el precio real del producto, ¡buena señal!), con utilidad teórica máxima de **$3.000.000 COP/mes**. Las raíces de `U(p)=0` son `p=0` y `p=20`: por debajo de 0 o por encima de $20.000 no hay utilidad — coherente con la curva.

## Errores comunes / trampas

- **Olvidar el `±`:** la fórmula general da **dos** raíces. Reportar solo una pierde la mitad de las soluciones.
- **Signo de `b` mal copiado:** en `2x² − 7x + 3`, `b = −7` (¡con el menos!). Es el error #1; por eso siempre se sustituye de vuelta para verificar.
- **No verificar el discriminante:** si `Δ < 0` no hay solución real. En un problema físico/de negocio, raíces complejas suelen significar "ese escenario no ocurre" (p. ej. no existe precio que dé esa utilidad).
- **`a = 0` colado:** si el coeficiente cuadrático es 0, NO es cuadrática; la fórmula divide por `2a = 0` y explota. Trátala como lineal.
- **Aceptar raíces sin sentido:** una raíz negativa para "número de unidades" o "precio" se descarta por contexto, no por matemática. Filtra con la unidad.
- **Float para dinero:** resolver con `float` puede dar `2.9999999`. Usa `sympy`/`fractions` o `decimal` y redondea UNA vez al final (ver [[05-cifras-significativas-y-redondeo]]).
- **Confundir vértice con raíz:** el máximo/mínimo está en el **vértice** (`x = −b/2a`), no en las raíces. Las raíces son donde vale 0.

## Cruces

- [[21-ecuaciones-lineales]] — el caso `a = 0`; resolver el lineal que aparece al factorizar.
- [[20-expresiones-algebraicas]] — factorizar, expandir y manipular antes de resolver.
- [[43-optimizacion-con-derivadas]] — el método general (derivada = 0) para hallar máximos/mínimos; aquí lo hicimos con vértice.
- [[15-potencias-y-raices]] — la raíz cuadrada del discriminante.
- [[30-geometria-plana-areas-y-perimetros]] — aplicaciones de área que dan ecuaciones cuadráticas.

---

**Mini-checklist de exactitud**
1. ¿Verifiqué el **signo** de cada coeficiente `a, b, c` antes de sustituir?
2. ¿Sustituí **ambas** raíces de vuelta y dieron 0 exacto (o vía Vieta: suma `=-b/a`, producto `=c/a`)?
3. ¿Descarté raíces sin sentido físico/de negocio por su **unidad** y redondeé solo al final?
