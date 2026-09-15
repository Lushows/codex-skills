# 24 · Polinomios

> **Qué resuelve / cuándo usarlo** — Cuando necesitas operar, dividir, factorizar o hallar las raíces de una expresión con potencias de una variable (curvas de costo, ingresos, ajustes de datos, modelos de crecimiento). El polinomio es la "fórmula multiusos" del álgebra aplicada.

## Concepto (para no-experto)

Un **polinomio** es una suma de términos donde cada término es un número (el **coeficiente**) multiplicado por una variable elevada a un exponente entero no negativo (0, 1, 2, 3, …). Ejemplo:

```
P(x) = 2x³ − 5x² + 4x − 7
```

Aquí los **coeficientes** son 2, −5, 4, −7 y la **variable** es `x`. El número más alto al que se eleva `x` se llama **grado** (en este caso 3, por `x³`). El término sin variable (−7) se llama **término independiente** o **constante**.

Analogía cotidiana: piensa en un polinomio como una **receta de costos**. Si vendes `x` calculadoras gastronómicas, tu costo total podría ser algo como "un costo fijo + un costo por unidad + un descuento por volumen que crece con el cuadrado". Cada ingrediente de esa receta es un término del polinomio. Evaluar el polinomio en un valor de `x` es simplemente "ejecutar la receta" para esa cantidad.

Conceptos clave que usaremos:
- **Raíz** (o **cero**): un valor de `x` que hace que `P(x) = 0`. Es donde la curva cruza el eje horizontal. En negocio, suele ser un punto de equilibrio (donde la ganancia es cero).
- **Factorizar**: reescribir el polinomio como un producto, p. ej. `x² − 5x + 6 = (x − 2)(x − 3)`. Las raíces "saltan a la vista": 2 y 3.
- **Dividir polinomios**: como la división larga de números, pero con `x`. Da un **cociente** y un **resto**.

## Fórmulas / método

Sea `P(x) = aₙ·xⁿ + aₙ₋₁·xⁿ⁻¹ + … + a₁·x + a₀`, con `aₙ ≠ 0`. El **grado** es `n`.

**Operaciones básicas**
- Suma/resta: se suman/restan coeficientes del mismo grado.
- Producto: cada término por cada término (propiedad distributiva); los grados se **suman**.

**División con resto** (algoritmo de la división):
```
P(x) = D(x)·Q(x) + R(x)     con   grado(R) < grado(D)
```
donde `D` es el divisor, `Q` el cociente y `R` el resto.

**Teorema del resto**: al dividir `P(x)` entre `(x − c)`, el resto es exactamente `P(c)`.
```
resto de [ P(x) ÷ (x − c) ] = P(c)
```

**Teorema del factor** (consecuencia directa): `(x − c)` es factor de `P(x)` ⟺ `P(c) = 0` ⟺ `c` es raíz.

**Teorema de las raíces racionales**: si `P` tiene coeficientes enteros, toda raíz racional `p/q` (en forma irreducible) cumple que `p` divide a `a₀` y `q` divide a `aₙ`. Sirve para listar *candidatos* a raíz.

**Teorema fundamental del álgebra**: un polinomio de grado `n` tiene exactamente `n` raíces contando multiplicidad (algunas pueden ser complejas). Símbolos sin unidad salvo que `x` represente una magnitud física/monetaria; en ese caso `x` y `P(x)` llevan sus unidades (p. ej. `x` en unidades vendidas, `P(x)` en COP).

## Verificación en código

```python
# Polinomios EXACTOS con sympy (álgebra simbólica, sin error de redondeo)
import sympy as sp

x = sp.symbols('x')
P = 2*x**3 - 5*x**2 + 4*x - 7   # polinomio de ejemplo, grado 3

# 1) Teorema del resto: dividir entre (x - 3) -> resto debe ser P(3)
c = 3
cociente, resto = sp.div(P, x - c, x)   # división exacta de polinomios
P_en_c = P.subs(x, c)                    # evaluar P(3)
print("cociente:", sp.expand(cociente)) # 2*x**2 + x + 7
print("resto    :", resto)              # 38
print("P(3)     :", P_en_c)             # 38

# --- VERIFICACIÓN POR SEGUNDA VÍA (reconstrucción) ---
# Debe cumplirse P(x) == D(x)*Q(x) + R(x). Lo comprobamos simbólicamente.
reconstruido = sp.expand((x - c)*cociente + resto)
assert sp.simplify(reconstruido - P) == 0, "La división NO reconstruye P"
# Y el teorema del resto: resto == P(c)
assert sp.simplify(resto - P_en_c) == 0, "Teorema del resto falla"
print("OK division y teorema del resto verificados")

# 2) Factorización y raíces de un polinomio con raíces enteras
Q = x**3 - 6*x**2 + 11*x - 6
print("factorizado:", sp.factor(Q))          # (x - 1)(x - 2)(x - 3)
raices = sp.roots(Q)                          # dict raiz -> multiplicidad
print("raices:", raices)                      # {1:1, 2:1, 3:1}

# --- VERIFICACIÓN: cada raíz debe anular Q (segunda vía: sustitución) ---
for r in raices:
    assert Q.subs(x, r) == 0, f"{r} no es raiz real de Q"
# Y el producto de factores debe reexpandir a Q
assert sp.expand((x-1)*(x-2)*(x-3)) == Q
print("OK factorizacion y raices verificadas")
```

Salida esperada: `cociente: 2*x**2 + x + 7`, `resto: 38`, `P(3): 38`, factorización `(x-1)*(x-2)*(x-3)`, raíces `{1:1, 2:1, 3:1}`, y ambos `OK`.

Para coeficientes con dinero, usa `sympy.Rational` (fracciones exactas) en vez de `float`; nunca metas decimales binarios en la factorización.

## Ejemplo trabajado

**Problema (negocio LatAm).** GastroLatam modela su **ganancia mensual** (en miles de COP) al vender `x` cientos de licencias de la calculadora con:

```
G(x) = −2x³ + 21x² − 60x + 0     [miles de COP]
```

(El término cúbico negativo refleja que, pasado cierto punto, costos de soporte y descuentos por volumen erosionan la ganancia.) Pregunta: ¿en qué niveles de venta la ganancia es exactamente cero (puntos de equilibrio)?

Paso 1 — Sacar factor común: `G(x) = −x·(2x² − 21x + 60)`. Una raíz obvia es `x = 0` (vender nada → ganancia 0).

Paso 2 — Resolver `2x² − 21x + 60 = 0` con la cuadrática (ver [[23-ecuaciones-cuadraticas]]):
- Discriminante `Δ = (−21)² − 4·2·60 = 441 − 480 = −39 < 0`.

Paso 3 — Como `Δ < 0`, **no hay más raíces reales**: el único cruce real es `x = 0`. La ganancia nunca vuelve a cero para `x > 0` (no hay segundo punto de equilibrio real en este modelo).

Verificación en código:

```python
import sympy as sp
x = sp.symbols('x', real=True)
G = -2*x**3 + 21*x**2 - 60*x
print(sp.factor(G))                 # -x*(2*x**2 - 21*x + 60)
print(sp.solve(G, x))               # [0]  (única raíz real)
print(sp.discriminant(2*x**2 - 21*x + 60, x))  # -39  -> confirma sin raíces reales
```

**Resultado:** el único punto de equilibrio real es `x = 0` (es decir, 0 licencias). Para cualquier venta positiva la ganancia es estrictamente positiva o negativa pero nunca vuelve a cruzar cero en los reales. **Unidad:** `x` en cientos de licencias; `G(x)` en miles de COP. (Sanity check: `G(1) = −2 + 21 − 60 = −41`, negativo → con 100 licencias aún hay pérdida; coherente con que el negocio necesita volumen.)

## Errores comunes / trampas

- **Confundir grado y número de raíces reales.** Grado `n` ⇒ `n` raíces *contando complejas y multiplicidad*; las **reales** pueden ser menos. No supongas que "grado 3 = 3 cruces en el eje".
- **Olvidar `(x − c)` vs `(x + c)`.** El teorema del resto usa `(x − c)`. Para `(x + 2)` el valor a evaluar es `c = −2`, no `+2`.
- **Perder el signo al restar polinomios.** `(2x − 3) − (x − 5) = x + 2`, no `x − 8`: distribuye el menos a **todos** los términos.
- **Factorizar con floats.** `0.1 + 0.2` no es `0.3` en binario; usa `sympy.Rational` o enteros para no inventar raíces espurias.
- **Aplicar raíces racionales sin coeficientes enteros.** El teorema de la raíz racional solo lista candidatos si los coeficientes son enteros; multiplica primero por el común denominador.
- **Dar el cociente sin el resto.** Una división de polinomios está incompleta (y mal verificable) si no reportas `R(x)`.

## Cruces
- [[23-ecuaciones-cuadraticas]] — el caso grado 2; base para factorizar cúbicas.
- [[20-expresiones-algebraicas]] — manipular, expandir y simplificar antes de factorizar.
- [[18-divisibilidad-factores-y-primos]] — la analogía de factores/resto con números enteros.
- [[29-algebra-aplicada-al-modelado]] — usar polinomios para modelar costo, ingreso y ganancia.
- [[25-funciones-concepto-dominio-rango]] — un polinomio visto como función y su gráfica.

---

**Mini-checklist de exactitud**
- [ ] Verifiqué la división con la identidad `P = D·Q + R` (reexpansión simbólica).
- [ ] Confirmé cada raíz por sustitución (`P(r) == 0`), no solo por la factorización.
- [ ] Reporté grado, raíces reales **y** unidades de `x` y `P(x)`.
