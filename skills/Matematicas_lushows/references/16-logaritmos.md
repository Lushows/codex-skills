# 16 · Logaritmos

> **Qué resuelve / cuándo usarlo** — El logaritmo responde "¿a qué exponente elevo una base para obtener este número?". Es la herramienta exacta para medir crecimiento (CAGR), comparar tasas de retorno (log returns), comprimir escalas enormes (decibeles, sismos, dinero) y resolver despejes donde la incógnita está en el exponente.

## Concepto (para no-experto)

Un **logaritmo** es la operación inversa de una **potencia** (multiplicar una base por sí misma varias veces; ver [[15-potencias-y-raices]]).

Si una potencia dice "2 elevado a 3 da 8" → `2³ = 8`, el logaritmo dice lo contrario: "¿a qué exponente elevo 2 para obtener 8?" → `log₂(8) = 3`.

En palabras simples: **el logaritmo es el exponente escondido.**

- La **base** (`b`) es el número que se multiplica por sí mismo. Debe ser positiva y distinta de 1.
- El **argumento** (`x`) es el número del que sacamos el log. Debe ser **estrictamente positivo** (no existe log de cero ni de negativos en los reales).
- El **resultado** es el exponente.

**Analogía cotidiana.** Piensa en "cuántas veces tengo que doblar una hoja para llegar a cierto grosor". Cada doblez multiplica por 2 (eso es la potencia `2ⁿ`). Si te pregunto "¿cuántos dobleces necesito para multiplicar el grosor por 1.000?", estás pidiendo `log₂(1000) ≈ 9,97`, o sea unos 10 dobleces. El logaritmo cuenta los pasos de multiplicación.

**¿Por qué importa en negocios?**
- **Escalas**: el dinero, las visitas o los seguidores crecen de forma multiplicativa. Una gráfica en escala logarítmica convierte el crecimiento exponencial (una curva que se dispara) en una línea recta fácil de leer.
- **CAGR** (tasa de crecimiento anual compuesta): para sacar el crecimiento promedio por año entre dos cifras se usa logaritmo (o su gemela, la raíz; ver [[15-potencias-y-raices]]).
- **Log returns** (retornos logarítmicos): en finanzas se suman entre periodos, a diferencia de los retornos simples — facilita análisis de riesgo (ver [[94-riesgo-var-y-volatilidad]]).

## Fórmulas / método

**Definición.** Para base `b > 0`, `b ≠ 1` y argumento `x > 0`:

```
log_b(x) = y   ⟺   b^y = x
```

- `b` = base · `x` = argumento (adimensional) · `y` = exponente resultante (adimensional).

**Tres bases que importan:**
- **Base 10** — `log₁₀(x)` o "log". Cada +1 = ×10 (órdenes de magnitud; ver [[17-notacion-cientifica-y-magnitudes]]).
- **Base e** — `ln(x)`, logaritmo **natural**. `e ≈ 2,718281828…`. Es la base del crecimiento continuo; aparece en interés compuesto continuo y log returns.
- **Base 2** — `log₂(x)`. Cada +1 = ×2 (duplicaciones; útil en informática y crecimiento viral).

**Propiedades (válidas para argumentos positivos):**

| Nombre | Fórmula | Idea |
|---|---|---|
| Producto | `log_b(x·y) = log_b(x) + log_b(y)` | multiplicar → sumar logs |
| Cociente | `log_b(x/y) = log_b(x) − log_b(y)` | dividir → restar logs |
| Potencia | `log_b(x^p) = p · log_b(x)` | baja el exponente como factor |
| Cambio de base | `log_b(x) = ln(x) / ln(b)` | calcula cualquier base con ln o log10 |
| Inversa | `b^(log_b(x)) = x` y `log_b(b^y) = y` | log y potencia se cancelan |
| Valores fijos | `log_b(1) = 0` ; `log_b(b) = 1` | el log de 1 siempre es 0 |

**CAGR (tasa compuesta anual)** entre valor inicial `V₀` y final `V₁` en `n` años:

```
CAGR = (V₁ / V₀)^(1/n) − 1      (equivale a   exp( ln(V₁/V₀) / n ) − 1 )
```

**Log return** de un periodo:  `r_log = ln(P₁ / P₀)`. Se **suman** entre periodos.

## Verificación en código

```python
# Logaritmos exactos y verificados. Para dinero usamos Decimal.
from decimal import Decimal, getcontext
import math, sympy as sp

getcontext().prec = 30  # alta precisión en decimales

# --- 1) Logaritmo base 2 de 8 (debe dar exactamente 3) ---
val = sp.log(8, 2)            # sympy: log exacto y simbólico
print("log2(8) =", sp.nsimplify(val), "=", float(val))   # -> 3
assert sp.simplify(val - 3) == 0, "log2(8) debe ser 3"

# --- 2) Cambio de base verificado: log2(1000) ---
log2_1000 = math.log(1000, 2)
via_ln     = math.log(1000) / math.log(2)   # ln(1000)/ln(2)
print("log2(1000) =", log2_1000)
assert math.isclose(log2_1000, via_ln, rel_tol=1e-15), "cambio de base falla"

# --- 3) Propiedad del producto: log(a*b) == log(a)+log(b) ---
a, b = 7, 13
izq = math.log(a * b)
der = math.log(a) + math.log(b)
assert math.isclose(izq, der, rel_tol=1e-15), "propiedad producto falla"

# --- 4) CAGR con Decimal (dinero) y doble verificación ---
V0 = Decimal("10000000")   # COP ventas año 0
V1 = Decimal("17280000")   # COP ventas año 3
n  = 3
# CAGR usando logaritmo natural para exactitud: exp(ln(V1/V0)/n) - 1
ratio = V1 / V0
cagr = Decimal(math.exp(math.log(float(ratio)) / n)) - Decimal(1)
print("CAGR =", round(cagr * 100, 4), "%")

# VERIFICACIÓN POR SEGUNDA VÍA: reconstruir V1 a partir del CAGR
reconstruido = V0 * (Decimal(1) + cagr) ** n
print("V1 reconstruido =", round(reconstruido, 2))
assert abs(reconstruido - V1) < Decimal("1"), "el CAGR no reconstruye V1"
print("OK: todas las verificaciones pasaron")
```

Salida esperada: `log2(8) = 3`, `log2(1000) ≈ 9,9658`, CAGR `≈ 20,0000 %`, `V1 reconstruido ≈ 17.280.000,00`.

## Ejemplo trabajado

**Situación (LatAm).** Las ventas de una cafetería pasaron de **$10.000.000 COP** (año 0) a **$17.280.000 COP** (año 3). ¿Cuál fue el crecimiento promedio por año (CAGR)?

**Paso 1 — razón de crecimiento total:**
`17.280.000 / 10.000.000 = 1,728` (creció 72,8 % en total en 3 años).

**Paso 2 — repartir ese crecimiento de forma compuesta entre 3 años** con logaritmo:
`ln(1,728) = 0,547068…`
`0,547068 / 3 = 0,182356…`  ← crecimiento continuo anual promedio
`e^(0,182356) = 1,20` → restamos 1 → **0,20 = 20 %**.

**Paso 3 — verificación inversa (la prueba de error cero):**
`10.000.000 × (1,20)³ = 10.000.000 × 1,728 = 17.280.000 COP` ✅ coincide exacto.

**Resultado:** CAGR = **20 % anual** (con unidades: 20 % de crecimiento compuesto por año, COP). No es lo mismo que dividir 72,8 % / 3 = 24,3 % — ese sería el error clásico de promediar linealmente un crecimiento que en realidad es multiplicativo.

## Errores comunes / trampas

- **Log de cero o negativos.** `log(0)` no existe (tiende a −∞) y `log(−5)` no es real. Si tu argumento puede ser ≤ 0, valida antes de calcular.
- **Promediar crecimiento linealmente.** Dividir el crecimiento total entre los años da un número inflado. El crecimiento compuesto se reparte con logaritmo/raíz, no con división.
- **Confundir `log` con `ln`.** En muchas calculadoras y en Excel `LOG()` es base 10, pero en NumPy `np.log()` es base e (natural) y `np.log10()` es base 10. Verifica siempre qué base usa tu herramienta.
- **`log(a+b) ≠ log(a)+log(b)`.** La propiedad de la suma de logs aplica a **productos** (`a·b`), nunca a sumas. Es el error algebraico más frecuente.
- **Float en dinero.** No acumules log returns sobre montos en float esperando centavos exactos; usa Decimal para el dinero y reserva el float solo para el exponente (ver [[12-fracciones-decimales-y-precision]]).
- **Redondear a mitad de camino.** Mantén toda la precisión y redondea **una sola vez al final** (ver [[05-cifras-significativas-y-redondeo]]).

## Cruces

- [[15-potencias-y-raices]] — el log es la operación inversa de la potencia; CAGR también se puede ver como raíz.
- [[27-funciones-exponenciales-y-logaritmicas]] — la función log/exp como modelo de crecimiento y curvas.
- [[17-notacion-cientifica-y-magnitudes]] — escalas logarítmicas y órdenes de magnitud (cada +1 en log10 = ×10).
- [[71-interes-simple-y-compuesto]] — crecimiento compuesto y tiempo de duplicación con `ln(2)/r`.
- [[86-forecasting-y-proyeccion]] — usar CAGR y modelos log para proyectar ventas.

---

**Mini-checklist de exactitud**
- [ ] ¿El argumento del log es estrictamente positivo? (nunca 0 ni negativo)
- [ ] ¿Confirmé qué base usa mi herramienta (`ln` vs `log10` vs `log2`)?
- [ ] ¿Verifiqué el resultado por la vía inversa (reconstruir el valor con la potencia)?
