# 20 · Expresiones algebraicas

> **Qué resuelve / cuándo usarlo** — Manipular, simplificar, factorizar y expandir expresiones con letras sin equivocarte. Úsalo cuando una fórmula de negocio tenga variables (precio, cantidad, costo) y necesites reescribirla, comprobarla o reducirla antes de meter números.

## Concepto (para no-experto)

Una **expresión algebraica** es una "frase matemática" que mezcla **números** y **variables** (letras que representan un valor que aún no fijamos, como `x`, `p` o `q`) unidos por operaciones (+, −, ×, ÷, potencias). Ejemplo: `3x + 5`.

Definiciones que usaremos (cada una la primera vez):

- **Término**: cada pedazo separado por + o −. En `3x + 5`, los términos son `3x` y `5`.
- **Coeficiente**: el número que multiplica a la variable. En `3x`, el coeficiente es `3`.
- **Términos semejantes**: términos con la **misma parte literal** (mismas letras con los mismos exponentes). `3x` y `7x` son semejantes; `3x` y `3x²` NO lo son. Solo los semejantes se pueden **sumar/restar** entre sí.
- **Expandir** (o "desarrollar"): quitar paréntesis multiplicando todo. `2(x+3) → 2x+6`.
- **Factorizar**: lo inverso de expandir; escribir la expresión como un **producto**. `2x+6 → 2(x+3)`.
- **Simplificar**: dejar la expresión en su forma más corta equivalente, juntando términos semejantes.

Analogía cotidiana: imagina cajas de productos. `3x` = "3 cajas tipo x". Solo puedes sumar cajas del **mismo tipo**: 3 cajas de manzanas + 7 cajas de manzanas = 10 cajas de manzanas (`3x+7x=10x`). No puedes sumar manzanas con peras (`3x + 5y` se queda así). Expandir es abrir las cajas; factorizar es volver a empacarlas.

**Idea clave de exactitud**: dos expresiones son **equivalentes** si dan el mismo número *para todo valor* de las variables. No basta con probar un número; por eso verificamos en código con `sympy`.

## Fórmulas / método

Reglas exactas (cada símbolo: `a`, `b`, `c`, `x` son números o variables reales):

- **Distributiva**: `a·(b + c) = a·b + a·c`
- **Suma de semejantes**: `a·x + b·x = (a + b)·x`
- **Producto de binomios (FOIL)**: `(a + b)(c + d) = a·c + a·d + b·c + b·d`
- **Cuadrado de binomio**: `(a + b)² = a² + 2ab + b²` ; `(a − b)² = a² − 2ab + b²`
- **Diferencia de cuadrados**: `a² − b² = (a + b)(a − b)`
- **Factor común**: `a·b + a·c = a·(b + c)`
- **Reglas de exponentes** (misma base): `xᵐ·xⁿ = xᵐ⁺ⁿ` ; `xᵐ/xⁿ = xᵐ⁻ⁿ` ; `(xᵐ)ⁿ = xᵐⁿ`

Método de simplificación (orden seguro):
1. Expandir todos los paréntesis (distributiva).
2. Aplicar reglas de exponentes.
3. Agrupar y sumar **solo** términos semejantes.
4. (Si conviene) factorizar el resultado.

**Regla de exactitud**: simplificación es transformación *exacta*, no aproximación. No se redondea nada hasta que sustituyes números reales (ver [[05-cifras-significativas-y-redondeo]]).

## Verificación en código

`sympy` es la librería de Python para **álgebra simbólica**: opera con letras, no con floats. `expand` expande, `factor` factoriza, `simplify` simplifica. La verificación de oro es `simplify(A - B) == 0`: si la **resta** de dos expresiones es cero, son idénticas para todo valor.

```python
import sympy as sp

# 1) Declarar las variables simbólicas (letras, no números)
x, y = sp.symbols('x y')

# Expresión cruda: margen tras descuento, sin simplificar
expr = 2*(x + 3) + 3*x - (x - 4)

# 2) Simplificar (juntar términos semejantes)
simplificada = sp.simplify(expr)
print("Original    :", expr)
print("Simplificada:", simplificada)   # 4*x + 10

# 3) Expandir y factorizar un binomio al cuadrado
cuadrado = sp.expand((x + 5)**2)
print("Expandido   :", cuadrado)        # x**2 + 10*x + 25
print("Factorizado :", sp.factor(cuadrado))  # (x + 5)**2

# 4) Diferencia de cuadrados
print("Factor dif² :", sp.factor(x**2 - 9))  # (x - 3)*(x + 3)
```

Verificación por SEGUNDA VÍA — dos métodos independientes:

```python
import sympy as sp
x, y = sp.symbols('x y')

A = 2*(x + 3) + 3*x - (x - 4)   # forma cruda
B = 4*x + 10                    # forma simplificada propuesta

# VÍA 1 (simbólica, exacta): la resta debe ser idénticamente 0
assert sp.simplify(A - B) == 0, "NO son equivalentes"

# VÍA 2 (numérica, independiente): evaluar en varios valores al azar.
# Si A y B fueran distintas, casi seguro diferirían en algún punto.
import random
for _ in range(1000):
    v = random.randint(-500, 500)
    assert A.subs(x, v) == B.subs(x, v), f"Difieren en x={v}"

print("OK: equivalentes por vía simbólica y por 1000 evaluaciones")
```

Por qué dos vías: la simbólica **prueba** la igualdad para todo `x`; la numérica es un *sanity check* independiente que atraparía un error de tipeo en el assert (ver [[03-protocolo-de-verificacion-por-codigo]] y [[06-estimacion-y-sanity-checks]]).

## Ejemplo trabajado

**Contexto LatAm.** Un restaurante vende `q` almuerzos. El precio es `p` (COP). Da un descuento de `2.000 COP` por almuerzo a partir del menú, y tiene un costo variable de `8.000 COP` por almuerzo. Quieren la **utilidad** `U(p, q)` simplificada.

Planteo (con unidades — todo en COP·almuerzos, resultado en COP):

```
Ingreso  = (p − 2000) · q          # precio neto × cantidad
Costo    = 8000 · q
U        = (p − 2000)·q − 8000·q
```

Simplificar paso a paso:
```
U = (p − 2000)·q − 8000·q
U = p·q − 2000·q − 8000·q          # distributiva
U = p·q − 10000·q                   # juntar términos semejantes en q
U = q·(p − 10000)                   # factor común q
```

Comprobación en código (incluye dinero exacto con `decimal` al sustituir):

```python
import sympy as sp
from decimal import Decimal, getcontext
getcontext().prec = 28

p, q = sp.symbols('p q')
U = (p - 2000)*q - 8000*q
U_factor = sp.factor(U)
print(U_factor)   # q*(p - 10000)

# Verificación simbólica
assert sp.simplify(U - q*(p - 10000)) == 0

# Caso real: 120 almuerzos a 15.000 COP -> dinero con decimal
precio  = Decimal("15000")
cant    = Decimal("120")
utilidad = cant * (precio - Decimal("10000"))   # = 120*(15000-10000)
print("Utilidad:", utilidad, "COP")             # 600000 COP

# Segunda vía: sustituir en la fórmula original sin factorizar
util2 = (precio - Decimal("2000"))*cant - Decimal("8000")*cant
assert utilidad == util2
print("OK verificado:", util2, "COP")
```

**Resultado**: `U = q·(p − 10000)`. Para 120 almuerzos a 15.000 COP → **600.000 COP** de utilidad. La forma factorizada deja ver al instante el punto de equilibrio: `U = 0` cuando `p = 10.000 COP` (ver [[76-punto-de-equilibrio]]).

## Errores comunes / trampas

- **Sumar términos no semejantes**: `3x + 5x² ≠ 8x³`. Distinto exponente → no se suman. Quedan separados.
- **Olvidar el signo al quitar paréntesis con resta**: `−(x − 4) = −x + 4`, NO `−x − 4`. El menos cambia **todos** los signos de adentro.
- **Confundir `(a+b)²` con `a²+b²`**: falta el `2ab`. `(a+b)² = a² + 2ab + b²`.
- **Distribuir mal una potencia**: `(2x)³ = 8x³`, no `2x³`. El exponente afecta también al coeficiente.
- **Cancelar términos en vez de factores**: en `(x+3)/3` NO se cancela el 3; solo se cancelan **factores** comunes a todo el numerador y denominador.
- **"Probé un número y dio igual" como prueba**: un solo valor puede coincidir por casualidad (ej. en `x=0` muchas cosas falsas dan lo mismo). Usa `simplify(A-B)==0`.

Mini-checklist de exactitud:
- [ ] ¿Confirmé equivalencia con `sympy.simplify(A - B) == 0` (no solo un valor)?
- [ ] ¿Respeté el signo al quitar paréntesis precedidos de `−`?
- [ ] ¿Al sustituir dinero usé `decimal`/centavos enteros, no float, y redondeé una sola vez al final?

## Cruces
- [[11-operaciones-y-orden-pemdas]] — el orden correcto de operaciones al expandir.
- [[15-potencias-y-raices]] — reglas de exponentes usadas al simplificar.
- [[24-polinomios]] — expresiones con varios términos y grados; factorización avanzada.
- [[21-ecuaciones-lineales]] — simplificar es el paso previo a despejar y resolver.
- [[29-algebra-aplicada-al-modelado]] — convertir un problema de negocio en una expresión.
