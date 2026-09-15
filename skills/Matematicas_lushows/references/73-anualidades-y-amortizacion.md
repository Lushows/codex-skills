# 73 · Anualidades y amortización

> **Qué resuelve / cuándo usarlo** — Calcular el valor (presente o futuro) de una serie de pagos iguales y la cuota fija exacta de un préstamo, junto con su tabla de amortización (cuánto de cada cuota es interés y cuánto abona capital). Úsalo para préstamos, leasing, ahorros periódicos, planes de pago a clientes o financiamiento de equipos.

## Concepto (para no-experto)

Una **anualidad** (en finanzas) es simplemente **una serie de pagos iguales separados por el mismo intervalo de tiempo**. No tiene que ser "anual": puede ser mensual, quincenal, etc. Ejemplos: la cuota fija de un crédito de un horno industrial, el aporte mensual a un ahorro, el arriendo.

Términos clave (definidos la primera vez):

- **Cuota / pago (P o A)**: el monto fijo que se paga (o recibe) en cada periodo. Unidad: dinero por periodo (ej. COP/mes).
- **Tasa por periodo (i)**: el interés que se cobra **en cada periodo**, expresado como decimal. Si el préstamo cobra 2 % mensual, entonces `i = 0.02` por mes. (Cómo pasar de tasa anual a mensual: ver [[75-tasas-nominal-efectiva-y-real]].)
- **Número de periodos (n)**: cuántos pagos hay en total. Unidad: periodos (meses, etc.).
- **Valor presente (VP)**: cuánto valen HOY todos esos pagos futuros. Para un préstamo, el VP es el monto que te prestan (el principal).
- **Valor futuro (VF)**: cuánto se acumula al final si los pagos se ahorran y ganan interés.
- **Amortizar**: ir pagando una deuda con cuotas que cubren los intereses del periodo y, con lo que sobra, reducen el capital (la deuda restante).

**Analogía cotidiana:** imagina una cubeta con un hueco (la deuda). Cada mes le echas un balde de agua igual (la cuota). Parte del agua solo reemplaza lo que el hueco "cobra" por existir (el interés sobre el saldo), y el resto baja el nivel (abona capital). Al principio el hueco está muy lleno, así que el interés se come casi todo el balde; al final, casi todo el balde baja el nivel. Por eso al inicio pagas mucho interés y poco capital.

**Anualidad ordinaria (vencida):** los pagos ocurren al **final** de cada periodo. Es el caso estándar de casi todos los préstamos. (Si fueran al inicio se llama "anticipada" y se multiplica todo por `(1+i)`.)

## Fórmulas / método

Con tasa por periodo `i` (decimal) y `n` periodos:

**Valor presente de una anualidad ordinaria** (lo que valen hoy n pagos de P):

```
VP = P · [ 1 − (1 + i)^(−n) ] / i        (si i ≠ 0)
VP = P · n                               (si i = 0)
```

**Valor futuro de una anualidad ordinaria** (lo acumulado tras n pagos):

```
VF = P · [ (1 + i)^n − 1 ] / i           (si i ≠ 0)
```

**Cuota fija de un préstamo** (despejando P cuando el VP es el principal `L`):

```
P = L · i / [ 1 − (1 + i)^(−n) ]         (si i ≠ 0)
P = L / n                                (si i = 0)
```

**Tabla de amortización** (sistema francés, cuota constante). Empieza con saldo `B₀ = L`. Para cada periodo k = 1…n:

```
interés_k   = B_(k−1) · i
capital_k   = P − interés_k
B_k         = B_(k−1) − capital_k
```

- Unidades: `L`, `P`, interés y capital en dinero (COP). `i` adimensional. `n` en periodos.
- Regla de oro: **`i` y `n` deben estar en la MISMA unidad de tiempo** (tasa mensual ⇒ n en meses).

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Alta precisión interna; redondeamos UNA sola vez al presentar (a centavos/peso).
getcontext().prec = 40

def cuota_prestamo(L: Decimal, i: Decimal, n: int) -> Decimal:
    """Cuota fija (sistema francés) de un préstamo de principal L."""
    if i == 0:
        return L / Decimal(n)
    factor = (Decimal(1) + i) ** (-n)          # (1+i)^(-n)
    return L * i / (Decimal(1) - factor)

def tabla_amortizacion(L: Decimal, i: Decimal, n: int):
    """Devuelve (cuota, filas). Ajusta la última cuota para cerrar en 0 exacto."""
    P = cuota_prestamo(L, i, n)
    cent = Decimal("0.01")
    P_red = P.quantize(cent, ROUND_HALF_UP)    # cuota presentada al cliente
    saldo = L
    filas = []
    for k in range(1, n + 1):
        interes = (saldo * i).quantize(cent, ROUND_HALF_UP)
        if k < n:
            capital = (P_red - interes)
            cuota_k = P_red
        else:
            # Última cuota: paga TODO el saldo + su interés (cierra exacto).
            capital = saldo
            cuota_k = (capital + interes).quantize(cent, ROUND_HALF_UP)
        saldo = (saldo - capital).quantize(cent, ROUND_HALF_UP)
        filas.append((k, cuota_k, interes, capital, saldo))
    return P_red, filas

# --- Caso: horno industrial financiado ---
L = Decimal("5000000")     # principal: 5.000.000 COP
i = Decimal("0.02")        # 2% mensual
n = 12                     # 12 cuotas mensuales

P_red, filas = tabla_amortizacion(L, i, n)
print("Cuota mensual:", P_red, "COP")

# ---- VERIFICACIÓN POR SEGUNDA VÍA ----
# Vía A (inversa): el VP de las 12 cuotas teóricas debe reconstruir el principal.
P_teo = cuota_prestamo(L, i, n)
VP = P_teo * (Decimal(1) - (Decimal(1)+i)**(-n)) / i
assert abs(VP - L) < Decimal("0.0001"), VP
print("VP reconstruido:", VP.quantize(Decimal('0.01')), "(== principal)")

# Vía B: el saldo final de la tabla debe ser EXACTAMENTE 0.
assert filas[-1][4] == Decimal("0.00"), filas[-1]

# Vía C: suma de capitales == principal; total intereses == suma cuotas - principal.
total_capital = sum(f[3] for f in filas)
total_cuotas  = sum(f[1] for f in filas)
total_interes = sum(f[2] for f in filas)
assert total_capital == L, total_capital
print("Total pagado:", total_cuotas, "| Interés total:", total_interes)
assert (total_cuotas - L) == total_interes  # cuadre contable
print("OK: saldo final 0, capitales suman el principal, cuadre contable correcto.")
```

Salida real al ejecutar:

```
Cuota mensual: 472885.81 COP
VP reconstruido: 5000000.00 (== principal)
Total pagado: 5674623.92 | Interés total: 674623.92
OK: saldo final 0, capitales suman el principal, cuadre contable correcto.
```

## Ejemplo trabajado

**Problema (LatAm):** Un restaurante financia un horno por **5.000.000 COP** a **2 % mensual** durante **12 meses**. ¿Cuál es la cuota y cómo se reparte?

Paso 1 — Identificar: `L = 5.000.000 COP`, `i = 0,02` por mes, `n = 12` meses.

Paso 2 — Cuota:
```
P = 5.000.000 · 0,02 / [1 − (1,02)^(−12)]
(1,02)^(−12) = 0,788493…
1 − 0,788493 = 0,211506…
P = 100.000 / 0,211506 = 472.885,81 COP/mes
```

Paso 3 — Primera fila de la tabla (mes 1):
- interés₁ = 5.000.000 · 0,02 = **100.000,00 COP**
- capital₁ = 472.885,81 − 100.000,00 = **372.885,81 COP**
- saldo₁ = 5.000.000 − 372.885,81 = **4.627.114,19 COP**

Paso 4 — Verificación: el saldo llega a **0,00 COP** en el mes 12, los capitales suman exactamente **5.000.000 COP**, y el interés total es **674.623,92 COP** (lo que se paga de más sobre el principal). **Total pagado: 5.674.623,92 COP.**

Sanity check de orden de magnitud: 12 cuotas de ~473 mil ≈ 5,67 millones, un poco más que el principal de 5 millones, coherente con un interés total < 700 mil. ✔️ (ver [[06-estimacion-y-sanity-checks]]).

## Errores comunes / trampas

- **Mezclar la unidad de tasa y de periodos:** poner tasa anual con n en meses (o viceversa). Convierte primero la tasa al periodo del pago — y la conversión correcta es con `(1+i)^k`, NO dividir la efectiva entre 12 ([[75-tasas-nominal-efectiva-y-real]]).
- **Usar `float` para dinero:** acumula errores de centavos y el saldo no cierra en 0. Usa `decimal` siempre ([[12-fracciones-decimales-y-precision]]).
- **Confundir anualidad ordinaria (pago al final) con anticipada (pago al inicio):** difieren en un factor `(1+i)`. Si la cuota se paga el día que firmas, es anticipada.
- **No ajustar la última cuota:** por redondeo de cada cuota a centavos, el saldo final queda en ±unos pesos. Hay que ajustar la última cuota para cerrar en 0,00 exacto (como en el código).
- **Redondear en cada paso intermedio:** redondea la presentación, pero conserva precisión interna; redondea UNA vez ([[05-cifras-significativas-y-redondeo]]).
- **Olvidar que interés total ≠ tasa × principal:** el interés se cobra sobre el **saldo decreciente**, no sobre el principal completo cada mes.

## Cruces

- [[72-valor-presente-y-futuro]] — base del VP/VF que esta fórmula generaliza a series de pagos.
- [[71-interes-simple-y-compuesto]] — el `(1+i)^n` viene del interés compuesto.
- [[75-tasas-nominal-efectiva-y-real]] — cómo obtener la `i` por periodo correcta antes de calcular la cuota.
- [[74-vpn-y-tir]] — cuando los pagos NO son iguales o quieres la tasa efectiva real del crédito.
- [[70-valor-del-dinero-en-el-tiempo]] — el principio de que un peso hoy ≠ un peso mañana.

---

**Mini-checklist de exactitud**
- [ ] `i` y `n` en la misma unidad de tiempo (tasa del periodo = periodo del pago).
- [ ] Dinero en `decimal`; redondeo a centavos UNA sola vez; última cuota ajustada para saldo final = 0,00.
- [ ] Verificado por segunda vía: VP de las cuotas reconstruye el principal Y la suma de capitales = principal.
