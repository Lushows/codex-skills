# 71 · Interés simple y compuesto

> **Qué resuelve / cuándo usarlo** — Calcular cuánto crece (o cuesta) el dinero al prestarlo, invertirlo o pedirlo prestado, distinguiendo el interés que NO se reinvierte (simple) del que SÍ (compuesto). Úsalo para créditos, ahorros, tarjetas, inversiones y para medir el crecimiento promedio anual (CAGR) de cualquier cosa.

## Concepto (para no-experto)

**Interés** es el precio del dinero en el tiempo: lo que te pagan por prestar (o ahorrar) o lo que pagas por que te presten. Se mide como una **tasa** (un porcentaje por período, por ejemplo 2 % mensual).

Hay dos formas de calcularlo:

- **Interés simple:** los intereses se calculan SIEMPRE sobre el capital original (el monto inicial, llamado **principal**). Los intereses no "generan más intereses". Es como un grifo que llena un balde a ritmo constante.

- **Interés compuesto:** al final de cada período, los intereses ganados se SUMAN al capital, y el siguiente período rinde sobre ese total más grande. Los intereses "trabajan" y generan más intereses. Es como una bola de nieve que rueda cuesta abajo: cada vuelta es más grande porque la anterior la hizo crecer.

**Analogía cotidiana.** Imagina que prestas $1.000.000 al 2 % mensual.
- Simple: te pagan $20.000 todos los meses, fijo. Punto.
- Compuesto: el primer mes ganas $20.000, pero el segundo mes el 2 % se calcula sobre $1.020.000, así que ganas $20.400. Y así sube. Esa diferencia, pequeña al inicio, se vuelve enorme con el tiempo. Eso es la **fuerza del interés compuesto**.

**Capitalización** (o composición) es el acto de sumar los intereses al capital. La **frecuencia de capitalización** es cada cuánto ocurre: mensual, trimestral, diaria. A más frecuente, más rápido crece (con la misma tasa anual nominal).

**CAGR** (Compound Annual Growth Rate = tasa de crecimiento anual compuesta) es la pregunta inversa: si algo pasó de un valor inicial a uno final en N años, ¿qué tasa anual constante produciría ese mismo resultado? Sirve para comparar inversiones o el crecimiento de ventas/usuarios "como si" hubiera crecido parejo cada año.

## Fórmulas / método

Símbolos (todos con sus unidades):

- `P` = principal o capital inicial (en dinero, p. ej. COP)
- `i` = tasa de interés por período (en fracción decimal; 2 % = 0,02) [adimensional]
- `n` = número de períodos (adimensional; deben coincidir con la unidad de `i`)
- `A` = monto final / valor futuro (en dinero, misma moneda que `P`)
- `I` = interés total ganado o pagado = `A − P` (en dinero)

**Interés simple:**

```
A = P · (1 + i · n)
I = P · i · n
```

**Interés compuesto** (capitaliza una vez por período):

```
A = P · (1 + i)^n
I = P · [ (1 + i)^n − 1 ]
```

**Compuesto con frecuencia de capitalización `m` por año**, tasa nominal anual `j`, durante `t` años:

```
A = P · (1 + j/m)^(m · t)
```

donde `m` = veces que capitaliza al año (mensual = 12, trimestral = 4, diaria = 365) y `n = m · t` es el total de períodos.

**Caso límite — capitalización continua** (m → ∞):

```
A = P · e^(j · t)        (e ≈ 2,718281828…)
```

**CAGR** (de un valor `V0` a `Vn` en `n` años):

```
CAGR = (Vn / V0)^(1/n) − 1
```

> Regla de oro de unidades: `i` y `n` deben estar en la MISMA unidad temporal. Si la tasa es mensual, `n` va en meses. Nunca mezcles "tasa mensual" con "n en años".

## Verificación en código

```python
# Interés simple vs compuesto, dinero EXACTO con decimal (nunca float para plata).
from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 40  # alta precisión interna; redondeamos UNA vez al final

def redondear_pesos(x: Decimal) -> Decimal:
    # COP no usa centavos en la práctica -> redondeo a peso entero.
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

P = Decimal("1000000")   # principal: $1.000.000 COP
i = Decimal("0.02")      # 2% mensual (fracción decimal)
n = 12                   # 12 meses

# --- Interés simple ---
A_simple = P * (1 + i * n)
I_simple = P * i * n

# --- Interés compuesto (capitaliza cada mes) ---
A_comp = P * (1 + i) ** n
I_comp = A_comp - P

print("SIMPLE   -> A =", redondear_pesos(A_simple), "| I =", redondear_pesos(I_simple))
print("COMPUESTO-> A =", redondear_pesos(A_comp),   "| I =", redondear_pesos(I_comp))
print("Diferencia (compuesto - simple):", redondear_pesos(A_comp - A_simple))
```

Salida:
```
SIMPLE   -> A = 1240000 | I = 240000
COMPUESTO-> A = 1268242 | I = 268242
Diferencia (compuesto - simple): 28242
```

**Verificación por segunda vía** (operación inversa + acumulación mes a mes, dos métodos independientes):

```python
# Vía 1: inversa del compuesto -> recuperar el principal desde A.
P_recuperado = A_comp / (1 + i) ** n
assert redondear_pesos(P_recuperado) == redondear_pesos(P), "La inversa no devuelve el principal"

# Vía 2: simular mes a mes sumando interes al saldo (definicion de compuesto).
saldo = P
for _ in range(n):
    saldo = saldo + saldo * i          # suma el interes del mes al capital
assert redondear_pesos(saldo) == redondear_pesos(A_comp), "El bucle no coincide con la formula"

# Sanity check de orden de magnitud: 2% mensual ~ algo mayor a 24% anual simple,
# y el compuesto debe quedar por ENCIMA del simple pero del mismo orden.
assert A_comp > A_simple > P
print("Verificacion OK: inversa, simulacion y sanity-check coinciden.")
```

```python
# CAGR verificado con su inversa.
V0 = Decimal("50000000")    # ventas año 0: $50.000.000
Vn = Decimal("86400000")    # ventas año 3: $86.400.000
n_anios = 3
cagr = (Vn / V0) ** (Decimal(1) / Decimal(n_anios)) - 1
print("CAGR =", (cagr * 100).quantize(Decimal("0.01")), "% anual")

# Inversa: aplicar el CAGR n veces debe reconstruir Vn.
reconstruido = V0 * (1 + cagr) ** n_anios
assert redondear_pesos(reconstruido) == redondear_pesos(Vn), "CAGR no reconstruye Vn"
print("CAGR reconstruye Vn:", redondear_pesos(reconstruido))
```

Salida:
```
CAGR = 20.00 % anual
CAGR reconstruye Vn: 86400000
```

## Ejemplo trabajado

**Situación (LatAm).** Lushows invierte **$1.000.000 COP** a una tasa **nominal anual del 24 %**. Quiere saber cuánto tendrá en **1 año** según la frecuencia de capitalización, y compararlo con interés simple.

Datos: `P = $1.000.000`, `j = 0,24` anual, `t = 1` año.

1. **Interés simple, 24 % anual:**
   `A = 1.000.000 · (1 + 0,24 · 1) = $1.240.000 COP`. Interés ganado: **$240.000 COP**.

2. **Compuesto mensual** (`m = 12`, tasa por mes = 0,24/12 = 0,02):
   `A = 1.000.000 · (1 + 0,02)^12 = $1.268.242 COP`. Interés: **$268.242 COP**.

3. **Compuesto diario** (`m = 365`):
   `A = 1.000.000 · (1 + 0,24/365)^365 ≈ $1.271.124 COP`. Interés: **$271.124 COP**.

4. **Capitalización continua:**
   `A = 1.000.000 · e^0,24 ≈ $1.271.249 COP`. Interés: **$271.249 COP**.

**Lectura.** Con la MISMA tasa nominal (24 %), capitalizar más seguido rinde más: $240.000 (simple) → $268.242 (mensual) → $271.124 (diario) → $271.249 (continuo, el techo). La diferencia entre simple y compuesto mensual ya es **$28.242 COP** en solo un año, y crece exponencialmente con los años. Esto explica por qué una tasa "del 2 % mensual" en una tarjeta de crédito es mucho más cara que un "24 % anual" mal entendido como simple.

Resultado verificado en el bloque de código de arriba (caso compuesto mensual) y por inversa/simulación.

## Errores comunes / trampas

- **Mezclar unidades de `i` y `n`.** Usar tasa mensual con `n` en años (o viceversa) da números absurdos. Conviértelas a la misma base SIEMPRE.
- **Confundir simple con compuesto** en créditos: casi todo crédito real (tarjetas, libranzas, microcrédito) es compuesto. Asumir simple subestima lo que vas a pagar.
- **Usar `float` para dinero.** `0.1 + 0.2 != 0.3` en float. Usa `decimal.Decimal` o trabaja en centavos enteros.
- **Confundir tasa nominal con efectiva.** 24 % nominal capitalizable mensual NO es 24 % efectivo anual; el efectivo es `(1+0,02)^12 − 1 = 26,82 %`. Ver [[75-tasas-nominal-efectiva-y-real]].
- **Redondear en cada período.** Redondea UNA sola vez al final; redondear intermedio acumula error. Ver [[05-cifras-significativas-y-redondeo]].
- **Olvidar restar la inflación.** Una ganancia del 24 % con inflación del 10 % no es un 24 % real. Ver [[79-moneda-inflacion-y-devaluacion]].
- **CAGR con períodos mal contados.** De "año 0" a "año 3" son 3 períodos, no 4 (no cuentes los puntos, cuenta los saltos entre ellos).

## Cruces

- [[70-valor-del-dinero-en-el-tiempo]] — el principio que sustenta todo el interés.
- [[72-valor-presente-y-futuro]] — descontar y proyectar montos con estas mismas fórmulas.
- [[73-anualidades-y-amortizacion]] — interés compuesto aplicado a pagos periódicos y cuotas.
- [[75-tasas-nominal-efectiva-y-real]] — convertir entre nominal, efectiva y real correctamente.
- [[27-funciones-exponenciales-y-logaritmicas]] — la matemática del crecimiento compuesto y los logaritmos para despejar `n`.

---

**Mini-checklist de exactitud:**
- [ ] `i` y `n` están en la MISMA unidad temporal antes de calcular.
- [ ] Dinero con `decimal`/centavos, redondeo UNA vez al final.
- [ ] Resultado verificado por segunda vía (inversa o simulación mes a mes).
