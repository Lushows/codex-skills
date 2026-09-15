# 08 · Herramientas de cálculo

> **Qué resuelve / cuándo usarlo** — Te dice qué herramienta usar para cada tipo de cálculo (dinero, fracciones exactas, álgebra simbólica, datos) y cómo ejecutarla de verdad. Es el "taller" de la skill: aquí están las llaves correctas para cada tornillo, para que NUNCA calcules de memoria.

## Concepto (para no-experto)

Calcular "de cabeza" o en una calculadora simple es como medir una pared a ojo: funciona para algo aproximado, pero si de ese número cuelga dinero real, necesitas un instrumento de precisión. En esta skill ese instrumento es **código ejecutable**: le escribimos al computador exactamente la operación y él la resuelve sin equivocarse ni cansarse.

El detalle clave es que **no todas las herramientas sirven para todo**. Igual que no usas un martillo para apretar un tornillo, no usas el tipo de número equivocado para el trabajo equivocado. Los principales "instrumentos" son:

- **Python con `decimal`** — para **dinero**. (Decimal = números con punto decimal manejados de forma exacta, como lo haría un contador, no como lo hace una calculadora barata).
- **Python con `fractions`** — para **fracciones exactas** (un tercio es exactamente 1/3, no 0.3333…).
- **Python con `sympy`** — para **álgebra y cálculo simbólico** (resolver ecuaciones con letras, derivar, integrar; "simbólico" = trabaja con símbolos como *x*, no solo con números).
- **Python con `numpy` / `statistics`** — para **muchos datos a la vez** (promedios, listas grandes, matrices).
- **Node.js** — alternativa cuando el proyecto ya es JavaScript (el bot de WhatsApp corre en Node).

**La trampa más cara de todas:** los computadores, por defecto, guardan los decimales en un formato llamado **`float`** (coma flotante = aproximación binaria de un decimal). Con `float`, `0.1 + 0.2` NO da `0.3`, da `0.30000000000000004`. Eso es invisible en un cálculo, pero en mil facturas se convierte en pesos que no cuadran. Por eso: **dinero SIEMPRE con `decimal` o con centavos enteros, NUNCA con `float`.**

## Fórmulas / método

No hay "fórmula" matemática, sino una **tabla de decisión** (qué herramienta para qué trabajo) y el **patrón de ejecución**.

**Tabla de decisión:**

| Necesito… | Herramienta | Por qué |
|---|---|---|
| Sumar/restar/multiplicar **dinero** | `decimal.Decimal` | Exactitud contable, control de redondeo |
| Resultado **fraccionario exacto** (proporciones, recetas) | `fractions.Fraction` | 1/3 se queda como 1/3 |
| **Resolver ecuaciones**, derivar, integrar, simplificar con letras | `sympy` | Álgebra simbólica exacta |
| **Promedio, mediana, desviación** de una lista | `statistics` (pocos datos) | Estándar, sin instalar nada |
| **Vectores, matrices, miles de datos** | `numpy` | Rápido y vectorizado |
| **Probabilidad/estadística avanzada** (distribuciones, tests) | `scipy.stats` | Funciones estadísticas completas |
| El proyecto **ya es JavaScript** (el bot) | Node.js (`bignumber.js` para dinero) | Mismo lenguaje del entorno |

**Patrón de ejecución obligatorio (regla de la skill):**

```
1. Identificar el tipo de número (¿dinero? ¿exacto? ¿simbólico? ¿datos?)
2. Elegir la herramienta de la tabla
3. Escribir el cálculo en código y EJECUTARLO (no estimar de cabeza)
4. VERIFICAR por una segunda vía (inversa, otro método, assert o estimación)
5. Redondear UNA sola vez, al final
6. Reportar el número CON UNIDADES
```

Donde **unidad** = qué representa el número (COP, kg, %, unidades vendidas). Un número sin unidad es un número incompleto.

## Verificación en código

Ejemplo integral: las cuatro herramientas en acción, cada una verificada por una segunda vía.

```python
# ---------- 1) DINERO con decimal (NUNCA float) ----------
from decimal import Decimal, ROUND_HALF_UP

# Demostración del peligro de float:
assert 0.1 + 0.2 != 0.3            # float falla
assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")  # decimal es exacto

# Precio del Excel gastronomico: 3 unidades + IVA 19%
precio = Decimal("10000")          # COP por unidad
cantidad = 3
iva_tasa = Decimal("0.19")

subtotal = precio * cantidad                 # 30000
iva = subtotal * iva_tasa                     # 5700
total = (subtotal + iva).quantize(           # redondear UNA vez, al final
    Decimal("1"), rounding=ROUND_HALF_UP)
print("Total:", total, "COP")                 # 35700 COP

# Verificacion por via inversa: total / cantidad debe dar precio con IVA por unidad
por_unidad = (total / cantidad).quantize(Decimal("0.01"))
esperado_unidad = (precio * (1 + iva_tasa)).quantize(Decimal("0.01"))
assert por_unidad == esperado_unidad, (por_unidad, esperado_unidad)

# ---------- 2) FRACCIONES exactas ----------
from fractions import Fraction
# Una receta para 1/3 de tanda + 1/6 de tanda
porcion = Fraction(1, 3) + Fraction(1, 6)
print("Porcion total:", porcion)              # 1/2 exacto, no 0.4999...
assert porcion == Fraction(1, 2)

# ---------- 3) ALGEBRA simbolica con sympy ----------
import sympy as sp
x = sp.symbols('x')
# Resolver: 250*x - 1_200_000 = 0  (punto de equilibrio: cuantas unidades)
sol = sp.solve(sp.Eq(250*x - 1_200_000, 0), x)
print("Unidades equilibrio:", sol)            # [4800]
# Verificacion: reemplazar la solucion en la ecuacion original -> debe dar 0
assert 250*sol[0] - 1_200_000 == 0

# ---------- 4) DATOS con statistics / numpy ----------
import statistics as st
ventas = [120, 95, 140, 110, 135]             # unidades por dia
prom = st.mean(ventas)
print("Promedio diario:", prom, "unidades")   # 120
# Verificacion por definicion (suma/cuenta), no confiar ciegamente en la libreria
assert prom == sum(ventas) / len(ventas)
```

Segunda vía con `numpy` para confirmar el promedio (otro motor, mismo resultado = confianza):

```python
import numpy as np
ventas = np.array([120, 95, 140, 110, 135])
assert np.isclose(ventas.mean(), 120.0)       # coincide con statistics
# Estimacion de orden de magnitud: ~5 dias * ~120 ~ 600 total; 120 prom es razonable
assert 90 <= ventas.mean() <= 150
```

Misma operación de dinero en **Node.js** (entorno del bot), con `bignumber.js` para no usar el `Number` flotante:

```javascript
// npm i bignumber.js
const BigNumber = require('bignumber.js');
const precio = new BigNumber('10000');
const total = precio.times(3).times(new BigNumber('1.19'));
console.log(total.toFixed(0)); // "35700"  (exacto, sin error de float)
// Verificacion inversa:
console.log(total.dividedBy(3).dividedBy('1.19').toFixed(0)); // "10000"
```

## Ejemplo trabajado

**Problema (negocio real, GastroLatam):** un cliente compra **3 calculadoras Excel** a **$10.000 COP** c/u. Se le aplica un descuento del **15%** y luego IVA del **19%**. ¿Cuánto paga en total?

Paso a paso, ejecutado con `decimal`:

```python
from decimal import Decimal, ROUND_HALF_UP

precio   = Decimal("10000")
cantidad = 3
desc     = Decimal("0.15")
iva      = Decimal("0.19")

subtotal      = precio * cantidad                  # 30000 COP
con_descuento = subtotal * (1 - desc)              # 30000 * 0.85 = 25500 COP
total         = (con_descuento * (1 + iva)).quantize(
                   Decimal("1"), rounding=ROUND_HALF_UP)  # redondeo unico
print(total)   # 30345
```

**Resultado: $30.345 COP** (treinta mil trescientos cuarenta y cinco pesos).

Verificación por **segunda vía** (camino distinto: factor combinado en un solo paso):

```python
factor = (1 - desc) * (1 + iva)                    # 0.85 * 1.19 = 1.0115
total_2 = (subtotal * factor).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
assert total_2 == total                            # 30345 == 30345  OK
```

Y **sanity check** de orden de magnitud: 30.000 con ~1% neto de ajuste (descuento −15% y IVA +19% casi se cancelan) debe quedar cerca de 30.000 → 30.345 es razonable. **Verificado, con unidades (COP).**

## Errores comunes / trampas

- **Usar `float` para dinero.** El error #1. `0.1 + 0.2 != 0.3`. Siempre `decimal` o centavos enteros. Ver [[12-fracciones-decimales-y-precision.md]].
- **Construir `Decimal` desde un float:** `Decimal(0.1)` hereda el error del float (da 0.1000000000000000055…). Hazlo **siempre desde string**: `Decimal("0.1")`.
- **Redondear en pasos intermedios.** Acumula error. Redondea UNA sola vez al final. Ver [[05-cifras-significativas-y-redondeo.md]].
- **Confundir exacto con aproximado:** `1/3` en Python da `0.333…` (float). Para exactitud usa `Fraction(1,3)` o `sympy`.
- **Comparar floats con `==`:** casi nunca es seguro. Usa `math.isclose` / `numpy.isclose` con tolerancia.
- **Confiar en la librería sin verificar.** Una librería puede usarse mal (argumentos invertidos, eje equivocado en numpy). Siempre confirma con un `assert` o un segundo método.
- **Olvidar las unidades** en el resultado. Un "30345" pelado no le sirve a nadie; "$30.345 COP" sí.
- **No ejecutar el código.** Escribirlo "mentalmente" sin correrlo viola la regla central de la skill: todo cálculo no trivial se EJECUTA. Ver [[03-protocolo-de-verificacion-por-codigo.md]].

## Cruces

- [[03-protocolo-de-verificacion-por-codigo.md]] — el protocolo formal de ejecutar + verificar que estas herramientas implementan.
- [[12-fracciones-decimales-y-precision.md]] — por qué `decimal`/`fractions` y no `float`, en profundidad.
- [[05-cifras-significativas-y-redondeo.md]] — cómo y cuándo redondear (una sola vez, al final).
- [[06-estimacion-y-sanity-checks.md]] — la verificación por orden de magnitud que acompaña al código.
- [[04-notacion-unidades-y-dimensiones.md]] — por qué todo resultado lleva unidades.

---

**Mini-checklist de exactitud:**
- [ ] ¿Elegí la herramienta correcta para el tipo de número (dinero→`decimal`, exacto→`fractions`, letras→`sympy`, datos→`numpy`/`statistics`)?
- [ ] ¿Ejecuté el código de verdad y lo verifiqué por una segunda vía (inversa/otro método/`assert`/estimación)?
- [ ] ¿Redondeé una sola vez al final y reporté el resultado CON UNIDADES?
