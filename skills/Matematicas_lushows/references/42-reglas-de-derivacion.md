# 42 · Reglas de derivación

> **Qué resuelve / cuándo usarlo** — Te da las reglas mecánicas (potencia, producto, cociente, cadena) para derivar CUALQUIER función común sin pensar desde cero, y el patrón para verificar cada derivada con `sympy` (cero error).

## Concepto (para no-experto)

**Derivada** = la *tasa de cambio instantánea* de una función. Si una función `f(x)` te dice "el costo total cuando produces x unidades", su derivada `f'(x)` te dice "cuánto sube el costo si produces *una unidad más*" en ese punto exacto. Es la pendiente de la curva en cada punto. (El concepto a fondo está en [[41-derivadas-concepto]]; aquí nos enfocamos en *cómo calcularlas*.)

Calcular una derivada con el límite (la definición) es lento y propenso a errores. Por suerte existen **reglas** que convierten la derivación en algo casi mecánico, como aplicar una receta. La analogía: derivar con la definición es como multiplicar sumando muchas veces; usar las reglas es como usar las tablas de multiplicar — el mismo resultado, mucho más rápido y seguro.

Términos que usaremos:
- **Constante**: un número fijo (ej. `5`, `7.2`), no cambia con `x`.
- **Exponente / potencia**: el número al que se eleva algo (`x³` tiene exponente 3).
- **Función compuesta**: una función "dentro" de otra, como `sen(3x²)` — primero calculas `3x²` y *ese resultado* entra al seno. La **regla de la cadena** sirve justo para estas.

## Fórmulas / método

Notación: `f'` o `d/dx[f]` es "la derivada de f respecto a x".

**1. Reglas básicas**
| Regla | Fórmula | En palabras |
|---|---|---|
| Constante | `d/dx[c] = 0` | un número fijo no cambia → pendiente 0 |
| Potencia | `d/dx[xⁿ] = n·x^(n−1)` | baja el exponente como factor y réstale 1 |
| Constante × función | `d/dx[c·f] = c·f'` | la constante sale a multiplicar |
| Suma/resta | `d/dx[f ± g] = f' ± g'` | se deriva término a término |

**2. Regla del producto** (dos funciones multiplicándose):
```
d/dx[f·g] = f'·g + f·g'
```
"derivada del primero por el segundo, MÁS el primero por derivada del segundo". Error típico: creer que es `f'·g'` (FALSO).

**3. Regla del cociente** (una función dividida por otra):
```
d/dx[f/g] = (f'·g − f·g') / g²        (con g ≠ 0)
```
"abajo por la derivada de arriba, MENOS arriba por la derivada de abajo, TODO sobre abajo al cuadrado". El orden importa por el signo menos.

**4. Regla de la cadena** (función compuesta `f(g(x))`):
```
d/dx[f(g(x))] = f'(g(x)) · g'(x)
```
"derivada de la de afuera (dejando la de adentro intacta) POR derivada de la de adentro".

**Derivadas de funciones comunes** (con `x` en radianes para trigonométricas):
```
d/dx[eˣ]    = eˣ
d/dx[ln x]  = 1/x            (x > 0)
d/dx[aˣ]    = aˣ · ln a       (a > 0)
d/dx[sen x] = cos x
d/dx[cos x] = −sen x
d/dx[√x]    = 1/(2√x)         (es x^(1/2), caso de la potencia)
```
Unidades: la derivada lleva unidades de `[salida de f] / [unidad de x]`. Ej. si el costo está en COP y `x` en unidades, `f'` está en **COP/unidad** (costo marginal).

## Verificación en código

Regla de oro de esta skill: NO confiamos en la derivada hecha a mano. La computamos con `sympy` (álgebra simbólica EXACTA, sin floats) y, como segunda vía, la comparamos contra la **derivada numérica** (la definición del límite con un paso pequeño).

```python
import sympy as sp

x = sp.symbols('x')

# --- Caso 1: cadena + producto, f(x) = x^2 * sen(3x) ---
f = x**2 * sp.sin(3*x)
df = sp.diff(f, x)
print("f'(x) =", sp.simplify(df))
# f'(x) = 2*x*sin(3*x) + 3*x**2*cos(3*x)

# A mano (producto): (x^2)'*sen(3x) + x^2*(sen(3x))'
#   = 2x*sen(3x) + x^2 * [cos(3x)*3]   <-- cadena en sen(3x)
a_mano = 2*x*sp.sin(3*x) + x**2*sp.cos(3*x)*3
assert sp.simplify(df - a_mano) == 0, "no coincide con lo hecho a mano"
print("OK: coincide con el cálculo manual")

# --- Caso 2: cociente, g(x) = (x^2 + 1)/(x - 3) ---
g = (x**2 + 1)/(x - 3)
dg = sp.simplify(sp.diff(g, x))
print("g'(x) =", dg)   # (x**2 - 6*x - 1)/(x - 3)**2
```

```python
# --- SEGUNDA VÍA: derivada numérica (definición del límite) ---
# f'(a) ≈ (f(a+h) - f(a-h)) / (2h)  con h muy pequeño (diferencia centrada).
from decimal import Decimal, getcontext
getcontext().prec = 40
import sympy as sp

x = sp.symbols('x')
f = x**2 * sp.sin(3*x)
df = sp.diff(f, x)

f_num  = sp.lambdify(x, f,  'mpmath')   # evaluación de alta precisión
df_num = sp.lambdify(x, df, 'mpmath')

import mpmath
mpmath.mp.dps = 30
a = mpmath.mpf('1.0')
h = mpmath.mpf('1e-10')
aprox = (f_num(a + h) - f_num(a - h)) / (2*h)   # numérica
exacta = df_num(a)                              # simbólica evaluada
print("numérica:", aprox)
print("exacta:  ", exacta)
assert abs(aprox - exacta) < mpmath.mpf('1e-6'), "discrepan: revisar"
print("OK: derivada simbólica y numérica coinciden")
```

## Ejemplo trabajado

**Problema de negocio (LatAm).** La calculadora de costos de GastroLatam estima el costo total mensual de operar un dark kitchen según los pedidos diarios `x`:

```
C(x) = 1_500_000 + 8_500·x + 0.5·x²   (COP)
```
El `1_500_000` es fijo (arriendo), `8_500·x` es el costo variable por pedido, y el término `0.5·x²` modela que al saturar la cocina cada pedido extra cuesta un poco más. **Pregunta:** ¿cuál es el *costo marginal* (lo que cuesta el siguiente pedido) cuando ya se hacen `x = 200` pedidos/día?

Paso a paso, aplicando potencia + suma + constante×función:
- `d/dx[1_500_000] = 0`
- `d/dx[8_500·x] = 8_500`
- `d/dx[0.5·x²] = 0.5·2·x = 1·x = x`
- ⇒ `C'(x) = 8_500 + x`
- En `x = 200`: `C'(200) = 8_500 + 200 = 8_700`

```python
from decimal import Decimal
import sympy as sp

x = sp.symbols('x')
C = Decimal('1500000') + Decimal('8500')*x + Decimal('0.5')*x**2
Cp = sp.diff(C, x)                 # 1.0*x + 8500.0
val = Cp.subs(x, 200)
print("C'(x) =", Cp, "| C'(200) =", val)   # 8700.0

# Segunda vía (dinero EXACTO con Decimal, sin floats):
# costo marginal real = C(201) - C(200)
def costo(n):
    n = Decimal(n)
    return Decimal('1500000') + Decimal('8500')*n + Decimal('0.5')*n*n
marginal_real = costo(201) - costo(200)
print("C(201)-C(200) =", marginal_real)    # 8700.5
```

**Resultado:** el costo marginal teórico es **8 700 COP/pedido** (la derivada es la *pendiente exacta* en x=200). El costo real del pedido 201 es **8 700,5 COP** — la pequeña diferencia (0,5) es normal: la derivada da la tasa instantánea, no el salto discreto de una unidad entera. Ambos confirman el orden de magnitud → cálculo sano.

## Errores comunes / trampas

- **Producto mal aplicado**: `(f·g)' ≠ f'·g'`. Siempre `f'g + fg'`.
- **Olvidar la cadena**: derivar `sen(3x)` como `cos(3x)` (FALSO) en vez de `cos(3x)·3`. Cada función "de adentro" multiplica por su propia derivada.
- **Signo del cociente**: es `(f'g − fg')/g²`, no `(fg' − f'g)`. El menos va con `f·g'`.
- **Trigonométricas en grados**: `d/dx[sen x] = cos x` solo vale con `x` en **radianes**. Si usas grados, falta el factor `π/180` (cadena). Ver [[33-trigonometria]].
- **Confundir `xⁿ` con `nˣ`**: `d/dx[x³]=3x²`, pero `d/dx[3ˣ]=3ˣ·ln 3`. La base variable vs. el exponente variable se derivan distinto.
- **Float en dinero**: evaluar costos marginales con `float` acumula error; usa `Decimal` para el dinero y `sympy` para la fórmula. Ver [[12-fracciones-decimales-y-precision]].

### Mini-checklist de exactitud
- [ ] ¿Apliqué la regla correcta (producto/cociente/cadena) y respeté el signo?
- [ ] ¿Verifiqué la derivada con `sympy` Y por segunda vía (numérica o C(n+1)−C(n))?
- [ ] ¿La derivada lleva sus unidades correctas (ej. COP/unidad)?

## Cruces
- [[41-derivadas-concepto]] — qué *es* una derivada antes de calcularla.
- [[43-optimizacion-con-derivadas]] — usar `f'(x)=0` para hallar máximos/mínimos (precio óptimo, costo mínimo).
- [[15-potencias-y-raices]] — la regla de la potencia se apoya en exponentes y raíces.
- [[33-trigonometria]] — derivadas de seno/coseno requieren radianes.
- [[03-protocolo-de-verificacion-por-codigo]] — el patrón ejecutar + verificar por segunda vía.
