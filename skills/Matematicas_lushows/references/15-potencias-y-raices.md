# 15 · Potencias y raíces

> **Qué resuelve / cuándo usarlo** — Multiplicar un número por sí mismo muchas veces (potencias) y la operación inversa (raíces). Es la base del crecimiento compuesto (dinero, ventas, virales), de áreas/volúmenes y de la notación científica.

## Concepto (para no-experto)

Una **potencia** es una multiplicación repetida del mismo número. En `aⁿ`:
- `a` es la **base** (el número que se repite).
- `n` es el **exponente** (cuántas veces se multiplica la base por sí misma).

Ejemplo: `2³ = 2 × 2 × 2 = 8`. Se lee "dos elevado a tres" o "dos al cubo". Tres copias del 2 multiplicadas.

Analogía cotidiana: si un rumor lo cuentan 2 personas, y cada una se lo cuenta a 2 nuevas cada día, el número de personas que se enteran cada día es `2¹, 2², 2³, ...` = 2, 4, 8, 16... Eso es **crecimiento exponencial**: el exponente está en el lugar donde sube la cuenta.

Una **raíz** es la pregunta inversa: "¿qué número, elevado a `n`, da este resultado?". La **raíz cuadrada** de 9 es 3, porque `3² = 9`. Se escribe `√9 = 3`. La **raíz cúbica** de 8 es 2, porque `2³ = 8`, y se escribe `∛8 = 2`.

Casos especiales que confunden al principio:
- **Exponente 0**: cualquier número (distinto de 0) elevado a 0 es **1**. `7⁰ = 1`. (Razón: dividir una potencia por sí misma, `7³/7³ = 7⁰ = 1`.)
- **Exponente negativo**: significa "uno dividido entre". `2⁻³ = 1 / 2³ = 1/8 = 0.125`. El signo menos NO hace negativo el resultado; lo hace **fracción**.
- **Exponente fraccionario**: es una raíz. `9^(1/2) = √9 = 3`. El denominador del exponente es el índice de la raíz: `8^(1/3) = ∛8 = 2`.

## Fórmulas / método

Símbolos: `a, b` = bases (números reales); `m, n` = exponentes; `√` = raíz.

**Reglas de potencias** (mismas bases):
- Producto: `aᵐ · aⁿ = a^(m+n)`  (se **suman** los exponentes)
- Cociente: `aᵐ / aⁿ = a^(m−n)`  (se **restan**)
- Potencia de potencia: `(aᵐ)ⁿ = a^(m·n)`  (se **multiplican**)

**Reglas con bases distintas** (mismo exponente):
- Producto: `(a·b)ⁿ = aⁿ · bⁿ`
- Cociente: `(a/b)ⁿ = aⁿ / bⁿ`

**Casos clave:**
- `a⁰ = 1`  (con `a ≠ 0`)
- `a⁻ⁿ = 1 / aⁿ`
- `a^(1/n) = ⁿ√a`  (raíz n-ésima)
- `a^(m/n) = ⁿ√(aᵐ) = (ⁿ√a)ᵐ`

**Raíz como inversa:**  si `b = ⁿ√a`  entonces  `bⁿ = a`. Verificar siempre elevando de vuelta.

**Aplicaciones típicas (con unidades):**
- Crecimiento compuesto: `Valor_final = Valor_inicial · (1 + r)ⁿ`, donde `r` = tasa por período (sin unidad, ej. 0.05 = 5%), `n` = número de períodos (meses, años).
- Tasa de crecimiento implícita entre dos valores: `r = (V_final / V_inicial)^(1/n) − 1`.
- Área de un cuadrado: `A = lado²` (m²). Volumen de un cubo: `V = lado³` (m³).

## Verificación en código

```python
from decimal import Decimal, getcontext
from fractions import Fraction
import sympy as sp

getcontext().prec = 30  # alta precisión para dinero/decimales

# --- 1) Reglas de potencias con fracciones EXACTAS (sin error de float) ---
a = Fraction(2)
assert a**3 * a**4 == a**7            # producto: 2^3 * 2^4 = 2^7
assert a**7 / a**4 == a**3            # cociente
assert (a**3)**2 == a**6              # potencia de potencia
assert a**0 == 1                      # exponente 0
assert a**-3 == Fraction(1, 8)        # exponente negativo = fracción
print("Reglas de potencias: OK")

# --- 2) Raíz como inversa exacta con sympy (no float) ---
raiz = sp.root(8, 3)                  # raíz cúbica de 8
assert sp.simplify(raiz) == 2
assert sp.Integer(2)**3 == 8          # verificación inversa: elevar de vuelta
print("Raiz cubica de 8 =", raiz, "-> 2**3 =", 2**3)

# --- 3) Exponente fraccionario = raíz ---
assert sp.nsimplify(9**sp.Rational(1, 2)) == 3   # 9^(1/2) = sqrt(9) = 3
print("9^(1/2) =", 9**sp.Rational(1, 2))

# --- 4) Crecimiento compuesto con Decimal (dinero, sin float) ---
inicial = Decimal("1000000")   # 1.000.000 COP
r = Decimal("0.05")            # 5% mensual
n = 12                         # 12 meses
final = inicial * (1 + r) ** n
print("Final 12 meses:", final.quantize(Decimal("0.01")))
```

**Verificación por segunda vía** (operación inversa + estimación de orden de magnitud):

```python
from decimal import Decimal

inicial = Decimal("1000000")
r = Decimal("0.05")
n = 12
final = inicial * (1 + r) ** n

# Vía A (inversa): si crecí n períodos al 5%, dividir de vuelta debe dar el inicial
recuperado = final / (1 + r) ** n
assert recuperado.quantize(Decimal("0.01")) == inicial.quantize(Decimal("0.01"))

# Vía B (estimación de orden de magnitud): 1.05^12 ≈ 1.8 (regla del 72: a 5% dobla en ~14 meses,
# así que a 12 meses aún no dobla -> factor entre 1.5 y 2). 1.000.000 * ~1.8 ≈ 1.8M.
factor = (final / inicial)
assert Decimal("1.5") < factor < Decimal("2.0"), "Fuera de rango esperado"
print("Factor de crecimiento:", factor.quantize(Decimal("0.0001")))  # ~1.7959
print("Doble verificacion: OK")
```

## Ejemplo trabajado

**Problema (LatAm).** Un restaurante vende **$1.000.000 COP/mes**. El dueño proyecta crecer **5% cada mes** durante **1 año**. ¿Cuánto venderá en el mes 12 y cuál fue el factor total?

Paso 1 — Modelo: `V₁₂ = V₀ · (1 + r)ⁿ` con `V₀ = 1.000.000 COP`, `r = 0.05`, `n = 12`.

Paso 2 — Factor de crecimiento: `(1.05)¹² = 1.795856...` (calculado con Decimal arriba, sin float).

Paso 3 — Valor final:
`1.000.000 COP × 1.795856 = 1.795.856,33 COP` (redondeado **una sola vez** al final, a centavos).

Paso 4 — Verificación inversa: `1.795.856,33 / (1.05)¹² = 1.000.000,00 COP`. ✔ Vuelve al inicial.

Paso 5 — Sanity check (regla del 72): a 5% mensual, el dinero se dobla en ≈ 72/5 ≈ 14,4 meses. A los 12 meses **aún no debe doblar**, y efectivamente el factor 1,80 < 2. ✔ Coherente.

**Resultado:** en el mes 12 venderá ≈ **$1.795.856 COP**, un factor de **1,80×** sobre el mes inicial. (Ojo: NO es "5% × 12 = 60% más"; el interés compuesto da 79,6% más.)

## Errores comunes / trampas

- **Confundir `aⁿ` con `a · n`.** `2⁵` NO es `10`; es `32`. La potencia es multiplicación repetida, no una multiplicación.
- **Creer que exponente negativo da resultado negativo.** `2⁻³ = 1/8 = 0.125` (positivo). El menos invierte, no cambia el signo del valor.
- **`(−a)ⁿ` vs `−aⁿ`.** `(−3)² = 9` (el paréntesis eleva el signo), pero `−3² = −9` (solo se eleva el 3). Sin paréntesis, el exponente "muerde" antes que el signo.
- **Sumar exponentes con bases distintas.** `2³ · 5² ≠ 10⁵`. La regla de sumar exponentes solo aplica si la **base es la misma**.
- **Raíz cuadrada de negativo en reales.** `√(−4)` no existe en números reales (sí en complejos). Si aparece, revisa el planteamiento.
- **Sumar tasas en vez de componer.** "5% mensual durante 12 meses" no es 60%; es `(1.05)¹² − 1 = 79.6%`. Confundir esto sobreestima o subestima dinero real.
- **Usar float para dinero.** `0.1 + 0.2 != 0.3` en float. Usa `decimal`/`fractions` o centavos enteros.
- **Redondear a mitad de camino.** Redondea **una sola vez** al final; redondear el factor antes de multiplicar arrastra error.

## Cruces

- [[16-logaritmos]] — el logaritmo es la operación inversa de la potencia (despeja el exponente).
- [[27-funciones-exponenciales-y-logaritmicas]] — cuando el exponente es variable: `f(x) = a^x`.
- [[71-interes-simple-y-compuesto]] — el interés compuesto es potencias aplicadas al dinero.
- [[17-notacion-cientifica-y-magnitudes]] — potencias de 10 para escribir números enormes o diminutos.
- [[30-geometria-plana-areas-y-perimetros]] — áreas (cuadrados) y volúmenes usan exponentes 2 y 3.

---

**Mini-checklist de exactitud**
- [ ] ¿Calculé en código con `decimal`/`fractions`/`sympy` (no de memoria, no float para dinero)?
- [ ] ¿Verifiqué la raíz/potencia por la **operación inversa** y por un **sanity check** de orden de magnitud?
- [ ] ¿Redondeé **una sola vez** al final y dejé las **unidades** (COP, m², meses) en el resultado?
