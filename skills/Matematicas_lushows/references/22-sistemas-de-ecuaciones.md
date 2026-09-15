# 22 · Sistemas de ecuaciones

> **Qué resuelve / cuándo usarlo** — Cuando tienes **varias incógnitas a la vez** (ej. precio de dos productos, mezcla de dos insumos, dos cuentas que deben cuadrar) y dispones de **varias condiciones** que las relacionan. Resuelve todas las incógnitas de forma simultánea y exacta.

## Concepto (para no-experto)

Una **ecuación** es una igualdad con una o más cantidades desconocidas (las **incógnitas**, normalmente `x`, `y`, `z`). Un **sistema de ecuaciones** es un grupo de dos o más ecuaciones que deben cumplirse **todas al mismo tiempo**. La **solución** es el conjunto de valores que hace verdaderas a TODAS las ecuaciones simultáneamente.

Regla de oro intuitiva: para encontrar `n` incógnitas necesitas, en general, `n` ecuaciones **independientes** (que aporten información distinta). Con 1 sola ecuación y 2 incógnitas hay infinitas combinaciones posibles; necesitas una segunda condición para fijarlas.

**Analogía cotidiana.** En una cafetería vendiste hoy 50 productos entre cafés y jugos, y recaudaste $250.000. "50 productos" es una condición; "$250.000" es otra. Cada una sola no te dice cuántos cafés ni cuántos jugos vendiste — pero las **dos juntas** sí. Eso es un sistema: dos pistas que, combinadas, revelan los dos números.

**Geometría.** Cada ecuación lineal con 2 incógnitas es una recta en un plano. La solución del sistema es el **punto donde las rectas se cruzan**. De ahí salen los tres casos posibles:
- **Una solución única** — las rectas se cruzan en un punto (se *cortan*).
- **Ninguna solución** (sistema **incompatible**) — las rectas son **paralelas**, nunca se tocan. Las condiciones se contradicen.
- **Infinitas soluciones** (sistema **compatible indeterminado**) — las rectas son la **misma recta**; una ecuación es solo la otra disfrazada (redundante).

## Fórmulas / método

Sistema lineal de 2×2 (dos ecuaciones, dos incógnitas):

```
a₁·x + b₁·y = c₁
a₂·x + b₂·y = c₂
```

Donde `a, b` son **coeficientes** (números que multiplican a la incógnita) y `c` son los **términos independientes** (constantes). Las unidades viven en `c` y en las incógnitas, no en los coeficientes adimensionales.

**Tres métodos para resolverlo a mano:**

1. **Sustitución.** Despeja una incógnita en una ecuación y métela (sustitúyela) en la otra. Te queda una sola ecuación con una sola incógnita.
2. **Eliminación (reducción).** Multiplica una o ambas ecuaciones por un número para que, al sumarlas o restarlas, **se cancele una incógnita**.
3. **Matricial / regla de Cramer.** Para `A·**x** = **b**`, donde `A = [[a₁,b₁],[a₂,b₂]]`:
   ```
   D  = a₁·b₂ − a₂·b₁        (determinante de A)
   x  = (c₁·b₂ − c₂·b₁) / D
   y  = (a₁·c₂ − a₂·c₁) / D
   ```
   El **determinante** `D` es un número que mide si el sistema tiene solución única.

**Cómo decidir el caso (test exacto):**
- Si `D ≠ 0` → **solución única**.
- Si `D = 0` y el sistema es consistente → **infinitas soluciones**.
- Si `D = 0` y es inconsistente → **sin solución**.

> Para sistemas grandes (3×3 o más), no uses Cramer a mano: usa eliminación de Gauss o álgebra lineal en código (ver [[47-sistemas-lineales-con-matrices]]).

## Verificación en código

```python
# Resolución EXACTA con fracciones (sin floats) + clasificación del caso.
from fractions import Fraction as F
import sympy as sp

# Sistema de ejemplo (cafetería): cafés (x) y jugos (y)
#   x + y      = 50          (unidades vendidas)
#   4000x + 6000y = 250000   (recaudo en COP)
a1,b1,c1 = F(1),    F(1),    F(50)
a2,b2,c2 = F(4000), F(6000), F(250000)

D  = a1*b2 - a2*b1            # determinante: número exacto
assert D != 0, "D=0: revisar caso (sin solución o infinitas)"

# Regla de Cramer con aritmetica exacta de fracciones
x = (c1*b2 - c2*b1) / D
y = (a1*c2 - a2*c1) / D
print("x (cafés) =", x, "| y (jugos) =", y)   # -> 25, 25

# ---- VERIFICACIÓN POR SEGUNDA VÍA #1: sustituir en AMBAS ecuaciones ----
assert a1*x + b1*y == c1, "Falla ecuación 1"
assert a2*x + b2*y == c2, "Falla ecuación 2"

# ---- VERIFICACIÓN POR SEGUNDA VÍA #2: resolver con sympy (otro método) ----
X, Y = sp.symbols('X Y')
sol = sp.solve([sp.Eq(X+Y,50), sp.Eq(4000*X+6000*Y,250000)], [X,Y], dict=True)
assert sol == [{X: 25, Y: 25}], sol
print("OK: dos vías coinciden ->", sol)
```

**Clasificar los tres casos en código (robusto, sin asumir solución única):**

```python
import sympy as sp
X, Y = sp.symbols('X Y')

def clasificar(eqs):
    sol = sp.linsolve(eqs, [X, Y])           # devuelve conjunto solución exacto
    if len(sol) == 0:
        return "SIN solución (incompatible: rectas paralelas)"
    pt = list(sol)[0]
    if any(s.free_symbols for s in pt):      # quedan símbolos -> parámetro libre
        return f"INFINITAS soluciones (familia): {pt}"
    return f"Solución ÚNICA: x={pt[0]}, y={pt[1]}"

print(clasificar([sp.Eq(X+Y,50), sp.Eq(4000*X+6000*Y,250000)]))  # única
print(clasificar([sp.Eq(X+Y,10), sp.Eq(X+Y,12)]))                # sin solución
print(clasificar([sp.Eq(X+Y,10), sp.Eq(2*X+2*Y,20)]))           # infinitas
```

## Ejemplo trabajado

**Problema (mezcla de insumos, dark kitchen).** Quieres preparar **20 kg** de una base de salsa mezclando un concentrado A ($18.000/kg) y un concentrado B ($10.000/kg). Tu presupuesto para esos 20 kg es **$260.000**. ¿Cuántos kg de cada uno?

Incógnitas (con unidades): `x` = kg de A, `y` = kg de B.

Condiciones:
```
(1)  x + y = 20            [kg]
(2)  18000·x + 10000·y = 260000   [COP]
```

**Método: eliminación.** Multiplico (1) por 10.000 y resto de (2):
```
(2)            18000x + 10000y = 260000
10000·(1)  -> (10000x + 10000y = 200000)
restando:       8000x          =  60000   ->  x = 60000/8000 = 7.5 kg de A
de (1):         y = 20 − 7.5            =  12.5 kg de B
```

**Verificación por sustitución (segunda vía):**
- (1): `7.5 + 12.5 = 20` kg ✓
- (2): `18000·7.5 + 10000·12.5 = 135000 + 125000 = 260000` COP ✓

**Sanity check de orden de magnitud:** el costo promedio pedido es `260000/20 = 13.000 $/kg`, que cae entre $10.000 y $18.000 → la mezcla debe existir y estar más cerca del barato (B), por eso B (12.5 kg) pesa más que A (7.5 kg). Coherente.

**Resultado:** **7,5 kg de A** y **12,5 kg de B**.

## Errores comunes / trampas

- **Contar mal las ecuaciones.** Con menos ecuaciones independientes que incógnitas, NO hay solución única (hay infinitas). No "inventes" un valor para forzar una respuesta.
- **Ecuaciones redundantes disfrazadas.** Si la segunda ecuación es múltiplo de la primera (ej. `2x+2y=20` vs `x+y=10`), aportan la misma información → infinitas soluciones, no única. Detectarlo con `D=0`.
- **Sistema inconsistente sin darse cuenta.** `x+y=10` y `x+y=12` se contradicen → no hay solución. Si al resolver llegas a `0 = 2`, ese es el síntoma.
- **Usar floats con dinero.** `0.1 + 0.2 != 0.3` en punto flotante. Usa `Fraction`/`Decimal` o centavos enteros (ver [[12-fracciones-decimales-y-precision]]).
- **Olvidar las unidades.** Un coeficiente confunde $/kg con kg si no rotulas. Revisa dimensiones (ver [[04-notacion-unidades-y-dimensiones]]).
- **Redondear a mitad de camino.** Resuelve en exacto y redondea UNA sola vez al final (ver [[05-cifras-significativas-y-redondeo]]).
- **Cramer en sistemas grandes.** Es exacto pero ineficiente y propenso a errores manuales en 3×3+; prefiere eliminación de Gauss / código.

**Mini-checklist de exactitud**
- [ ] Verifiqué la solución sustituyéndola en **TODAS** las ecuaciones (no solo una).
- [ ] Confirmé el caso con el determinante `D` (única / infinitas / ninguna) o con `linsolve`.
- [ ] El resultado tiene **unidades** y pasa el sanity check de orden de magnitud.

## Cruces
- [[21-ecuaciones-lineales]] — resolver una sola ecuación con una incógnita (base de este módulo).
- [[20-expresiones-algebraicas]] — manipular y despejar términos antes de resolver.
- [[47-sistemas-lineales-con-matrices]] — sistemas grandes con notación matricial y Gauss.
- [[48-determinantes-e-inversas]] — qué es el determinante y cómo decide la unicidad.
- [[29-algebra-aplicada-al-modelado]] — traducir un problema de negocio a ecuaciones.
