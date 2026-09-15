# 12 · Fracciones, decimales y precisión

> **Qué resuelve / cuándo usarlo** — Cuando un número tiene que ser EXACTO (sobre todo dinero) y el cálculo "normal" con decimales de computadora te puede mentir. Aquí aprendes por qué `0.1 + 0.2` no da `0.3`, cuándo usar fracciones exactas, y cómo manejar pesos sin perder ni un centavo.

## Concepto (para no-experto)

Un **número racional** es cualquier número que se puede escribir como una **fracción**: una división de dos enteros, `a/b` (con `b ≠ 0`). Ejemplo: `3/4`, `1/3`, `7/1`. Al número de arriba (`a`) se le llama **numerador** y al de abajo (`b`) **denominador**.

Una **fracción es exacta**: `1/3` representa *exactamente* "un tercio", sin pérdida.

Un **decimal** es esa misma cantidad escrita con punto: `3/4 = 0.75`. El problema es que **no toda fracción cabe en un decimal finito**. `1/3 = 0.3333…` nunca termina. Si lo cortas en `0.333`, ya perdiste un poquito.

Ahora la trampa fina: las computadoras guardan los decimales en **punto flotante** (en inglés *float*) — un formato binario (base 2) que solo puede representar exactamente las fracciones cuyo denominador es una potencia de 2 (1/2, 1/4, 1/8…). El número `0.1` en base 2 es **periódico infinito** (igual que 1/3 en base 10), así que el computador guarda una **aproximación** redondeada. Por eso:

```
0.1 + 0.2  →  0.30000000000000004   (¡no es 0.3!)
```

**Analogía:** imagina una regla marcada solo en mitades, cuartos y octavos. Te piden medir exactamente "un tercio de metro". No tienes esa marca, así que pones el lápiz lo más cerca posible. Cada vez que mides un tercio cometes un error minúsculo. Si mides 10.000 tercios, esos errores se acumulan. El `float` es esa regla: precisa para mitades, mentirosa para tercios y para casi todos los decimales "humanos" como 0.1.

**Conclusión de oro:** para **dinero** nunca uses `float`. Usa **decimales exactos** (`Decimal` en Python) o cuenta en **centavos enteros** (trabaja con números enteros y divide al final).

## Fórmulas / método

**Fracción → decimal:** divides numerador entre denominador.
`d = a / b`

El decimal **termina** (es finito) si y solo si, tras simplificar la fracción, el denominador `b` solo tiene factores primos **2 y/o 5** (los factores de la base 10). Si tiene cualquier otro primo (3, 7, 11…), el decimal es **periódico** (se repite para siempre).

- `b = 8 = 2³` → finito: `1/8 = 0.125`
- `b = 3` → periódico: `1/3 = 0.333…`
- `b = 6 = 2·3` → periódico (por el 3): `1/6 = 0.1666…`

**Decimal exacto (finito) → fracción:** si tienes `n` cifras decimales,
`fracción = (número sin punto) / 10ⁿ`, luego simplifica.
Ejemplo: `0.75 = 75/100 = 3/4`.

**Centavos enteros (dinero):** trabaja en la unidad mínima indivisible.
`centavos = round(pesos × 100)` → operas con enteros → al mostrar: `pesos = centavos / 100`.
Para pesos colombianos (COP) que normalmente no usan centavos, la "unidad mínima" suele ser **1 peso entero**.

**Símbolos:** `a` numerador, `b` denominador, `d` valor decimal, `n` cantidad de cifras decimales. Unidades: las que tenga la cantidad (COP, kg, m, %, …).

## Verificación en código

```python
# ============================================================
# 1) Demostración: por qué float falla
# ============================================================
print(0.1 + 0.2)              # 0.30000000000000004
print(0.1 + 0.2 == 0.3)      # False  <-- la trampa clásica
print(f"{0.1:.17f}")         # 0.10000000000000001  (lo que float guarda de verdad)

# ============================================================
# 2) Fracciones EXACTAS con el módulo fractions (cero pérdida)
# ============================================================
from fractions import Fraction

a = Fraction(1, 10)          # exactamente 1/10
b = Fraction(2, 10)          # exactamente 2/10
suma = a + b
print(suma)                  # 3/10   <-- EXACTO
assert suma == Fraction(3, 10), "La suma de fracciones debe ser exacta"

# Una fracción que NO cabe en decimal finito
print(Fraction(1, 3))        # 1/3 (se queda como fracción, sin redondear)

# ============================================================
# 3) DINERO con Decimal (la forma correcta)
# ============================================================
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 28       # 28 cifras de precisión: más que suficiente para finanzas

# OJO: se construye desde STRING, no desde float.
# Decimal(0.1) heredaría el error del float; Decimal("0.1") es exacto.
precio   = Decimal("10000")          # COP, precio de la calculadora gastronómica
iva_pct  = Decimal("0.19")           # 19% IVA Colombia
iva      = (precio * iva_pct)        # = 1900 exacto
total    = precio + iva
print(total)                          # 11900

# Redondeo bancario controlado (a 0 decimales para COP):
total_cop = total.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print(total_cop)                      # 11900

# ============================================================
# VERIFICACIÓN POR SEGUNDA VÍA
# ============================================================
# Vía A (centavos enteros): mismo cálculo con enteros puros.
precio_ent = 10000
iva_ent    = round(precio_ent * 19 / 100)   # 1900
total_ent  = precio_ent + iva_ent           # 11900
assert int(total_cop) == total_ent, "Decimal y enteros deben coincidir"

# Vía B (operación inversa): si quito el IVA, vuelvo al precio base.
base_recuperada = total_cop / Decimal("1.19")
base_recuperada = base_recuperada.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
assert base_recuperada == precio, f"Inversa falló: {base_recuperada} != {precio}"

# Vía C (float vs exacto en lote: demuestra la acumulación de error)
suma_float = sum(0.1 for _ in range(1000))          # 0.1 sumado 1000 veces
suma_exacta = float(Fraction(1, 10) * 1000)         # 100.0 exacto
print(suma_float, suma_exacta)                       # 99.9999999999986  vs  100.0
assert suma_float != 100.0          # float ya se desvió
assert suma_exacta == 100.0         # la vía exacta no

print("OK: todas las verificaciones pasaron")
```

Salida esperada (resumen): `0.30000000000000004`, `False`, `3/10`, `11900`, y `OK: todas las verificaciones pasaron`.

## Ejemplo trabajado

**Situación (LatAm):** GastroLatam vende la calculadora a **$10.000 COP**. Una promo da **15% de descuento** y luego se suma **19% de IVA** sobre el precio ya descontado. ¿Cuál es el total exacto que paga el cliente?

Paso 1 — Descuento (15%):
`descuento = 10000 × 0.15 = 1500 COP`
`precio_con_desc = 10000 − 1500 = 8500 COP`

Paso 2 — IVA (19%) sobre 8500:
`iva = 8500 × 0.19 = 1615 COP`
`total = 8500 + 1615 = 10115 COP`

Verificación en código exacto:

```python
from decimal import Decimal, ROUND_HALF_UP

precio = Decimal("10000")
desc   = (precio * Decimal("0.15"))                 # 1500
base   = precio - desc                              # 8500
iva    = (base * Decimal("0.19"))                   # 1615
total  = (base + iva).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print(total)   # 10115

# Segunda vía: total = base × 1.19  (un solo paso)
total2 = (base * Decimal("1.19")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
assert total == total2 == Decimal("10115")
```

**Resultado: el cliente paga $10.115 COP** (precio base 8.500 + IVA 1.615), verificado por dos métodos. Redondeo aplicado **una sola vez al final**.

## Errores comunes / trampas

- **Usar `float` para dinero.** `0.1 + 0.2 ≠ 0.3` y el error se acumula factura tras factura. Usa `Decimal` o centavos enteros.
- **`Decimal(0.1)` en vez de `Decimal("0.1")`.** Construir un `Decimal` desde un `float` *importa* el error del float. Siempre pásale un **string**.
- **Comparar decimales con `==` después de operar en float.** `if precio == 0.3:` casi nunca es lo que crees. En float, compara con tolerancia (`abs(x-y) < 1e-9`) o, mejor, usa `Decimal`/`Fraction` y compara exacto.
- **Redondear en cada paso.** Cada redondeo intermedio mete sesgo. Redondea **una sola vez al final** (ver [[05-cifras-significativas-y-redondeo]]).
- **Truncar `1/3` a `0.33` y multiplicar por 3** esperando `1.00` → da `0.99`. Si necesitas exactitud en divisiones que no terminan, quédate en `Fraction`.
- **Sumar muchos números de magnitudes muy distintas en float** (p. ej. 1e16 + 1): el pequeño "desaparece". Para sumas grandes, ordena o usa `math.fsum` / `Decimal`.

## Cruces

- [[10-numeros-y-sistemas-numericos]] — qué son racionales, base 2 vs base 10.
- [[05-cifras-significativas-y-redondeo]] — cómo y cuándo redondear (una vez, al final).
- [[14-porcentajes-sin-errores]] — descuentos e IVA exactos como en el ejemplo.
- [[03-protocolo-de-verificacion-por-codigo]] — el patrón ejecutar + verificar por segunda vía.
- [[08-herramientas-de-calculo]] — `decimal`, `fractions`, cuándo usar cada una.

---

**Mini-checklist de exactitud**
- [ ] ¿El dinero está en `Decimal("…")` o en centavos/pesos enteros (nunca `float`)?
- [ ] ¿Redondeé una sola vez, al final, con regla explícita (`ROUND_HALF_UP`)?
- [ ] ¿Confirmé el resultado por una segunda vía (inversa, enteros u otro método)?
