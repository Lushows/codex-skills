# 05 · Cifras significativas y redondeo

> **Qué resuelve / cuándo usarlo** — Decidir cuántos decimales tienen sentido reportar (precisión honesta) y redondear bien: una sola vez, al final, con el modo correcto, para que el redondeo no genere números falsos ni descuadres de centavos.

## Concepto (para no-experto)

**Cifras significativas** (o "cifras sig.") son los dígitos de un número que realmente cargan información, no los que son puro relleno. Si tu báscula mide hasta el gramo y marca `1850 g`, no puedes reportar `1850.7 g`: ese `.7` es inventado. La precisión de un resultado nunca puede ser mayor que la del dato más pobre que entró.

Analogía cotidiana: si mides una mesa con una cinta marcada en centímetros, puedes decir "1.83 m", pero NO "1.834217 m". Esos decimales extra mienten sobre cuánto sabes realmente. Reportar decimales que no mediste es como presumir un sueldo que no ganas.

**Redondear** es reemplazar un número por otro más corto, "cercano". El problema serio no es redondear: es redondear **antes de tiempo**. Cada redondeo intermedio mete un pequeño error; si encadenas operaciones sobre números ya redondeados, esos errores se acumulan y el resultado final puede salir mal por varios centavos o más. Por eso la regla de oro: **calcula con toda la precisión disponible y redondea UNA sola vez, al final.**

Términos clave:
- **Precisión**: cuántos dígitos confiables tiene un número.
- **Exactitud**: qué tan cerca está del valor verdadero (distinta de precisión).
- **Half-up** ("redondeo escolar"): el `.5` siempre sube. Ej: `2.5 → 3`.
- **Half-even** (redondeo bancario / "round half to even"): el `.5` va al par más cercano. Ej: `2.5 → 2`, `3.5 → 4`. Reduce el sesgo cuando redondeas muchos números.
- **Truncar**: cortar dígitos sin redondear. `2.99 → 2` (¡casi siempre un error!).

## Fórmulas / método

**Reglas de cifras significativas (operaciones):**

- Multiplicación / división: el resultado lleva tantas cifras significativas como el factor con **menos** cifras sig.
  - Ej: `3.0` (2 sig.) × `1.4567` (5 sig.) → 2 sig. → `4.4`
- Suma / resta: el resultado lleva tantos **decimales** como el sumando con menos decimales.
  - Ej: `12.1` (1 decimal) + `0.0345` → 1 decimal → `12.1`

**Redondeo a *n* decimales** (definición formal con half-even):

Sea `x` el valor exacto y `f = 10^n`. Buscamos el entero `m` que minimiza `|x·f − m|`; si hay empate exacto (la parte fraccionaria es exactamente `0.5`), se elige el `m` **par**. El resultado es `m / f`.

- `n` = número de decimales (adimensional)
- `f` = factor de escala = `10^n`
- El resultado conserva las unidades de `x` (COP, kg, %, etc.)

**Regla operativa (la más importante):**

```
resultado_final = redondear( f(d1, d2, ..., dk), n )    ← UNA sola vez
```

NUNCA:

```
resultado = f( redondear(d1), redondear(d2), ... )       ← error acumulado
```

Para **dinero** trabajamos en `Decimal` (aritmética decimal exacta) o en **centavos enteros**, jamás en `float` (los `float` no representan `0.1` exactamente).

## Verificación en código

```python
# ---------------------------------------------------------------
# Por qué NO usar float para dinero, y cómo redondear bien.
# ---------------------------------------------------------------
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, getcontext

# 1) El float MIENTE en decimales:
print(0.1 + 0.2)            # -> 0.30000000000000004  (¡no es 0.3!)
assert 0.1 + 0.2 != 0.3     # confirma el problema

# 2) Decimal es exacto si los construyes desde STRING (no desde float):
a = Decimal("0.1") + Decimal("0.2")
assert a == Decimal("0.3")  # ahora sí

# 3) Redondeo bancario (half-even) vs escolar (half-up):
def red(x, n, modo):
    cuant = Decimal(1).scaleb(-n)          # 10^-n  (ej: n=2 -> 0.01)
    return Decimal(str(x)).quantize(cuant, rounding=modo)

# Casos de empate exacto en .5:
casos = ["0.5", "1.5", "2.5", "3.5", "2.675"]
for c in casos:
    he = red(c, 0 if "." not in c[2:] else 2, ROUND_HALF_EVEN)
print(red("2.5", 0, ROUND_HALF_EVEN))  # -> 2  (par más cercano)
print(red("3.5", 0, ROUND_HALF_EVEN))  # -> 4  (par más cercano)
print(red("2.5", 0, ROUND_HALF_UP))    # -> 3  (siempre sube)
```

```python
# ---------------------------------------------------------------
# DEMOSTRACIÓN: redondear antes (mal) vs al final (bien)
# Caso: 1000 ítems de COP 1234.567 cada uno -> total.
# ---------------------------------------------------------------
from decimal import Decimal, ROUND_HALF_EVEN

precio = Decimal("1234.567")   # precio exacto por ítem (COP)
unidades = 1000
centavo = Decimal("0.01")

# MAL: redondeo cada precio y luego sumo
mal = sum((precio.quantize(centavo, ROUND_HALF_EVEN) for _ in range(unidades)),
          Decimal("0"))

# BIEN: calculo exacto y redondeo UNA vez al final
bien = (precio * unidades).quantize(centavo, ROUND_HALF_EVEN)

print("MAL :", mal)    # 1234570.00
print("BIEN:", bien)   # 1234567.00
print("Diferencia por redondeo prematuro:", mal - bien)  # 3.00 COP

# --- VERIFICACIÓN POR SEGUNDA VÍA (operación inversa) ---
# El total correcto dividido entre unidades debe devolver el precio exacto.
assert bien / unidades == precio          # 1234567 / 1000 == 1234.567  ✔
# Y por orden de magnitud: ~1000 * ~1234 ≈ 1.234 millones  ✔
assert Decimal("1.2e6") < bien < Decimal("1.3e6")
print("Verificación OK: el redondeo prematuro infló el total en 3 COP")
```

Salida clave: redondear cada línea infla el total en **3.00 COP**. Sobre miles de líneas esto descuadra una contabilidad.

## Ejemplo trabajado

**Situación (GastroLatam):** Un restaurante compra 3.5 kg de carne a COP 28 990 el kilo y le aplican 7% de descuento. ¿Cuánto paga?

Paso 1 — Subtotal exacto:
`3.5 kg × 28 990 COP/kg = 101 465 COP` (exacto, sin redondear todavía).

Paso 2 — Descuento exacto:
`101 465 × 0.07 = 7 102.55 COP`.

Paso 3 — Total exacto:
`101 465 − 7 102.55 = 94 362.45 COP`.

Paso 4 — Redondeo final UNA vez, al peso entero (en Colombia no circula el centavo de peso), half-even:
`94 362.45 → 94 362 COP`.

```python
from decimal import Decimal, ROUND_HALF_EVEN
kg     = Decimal("3.5")
precio = Decimal("28990")           # COP/kg
sub    = kg * precio                # 101465 exacto
desc   = sub * Decimal("0.07")      # 7102.55 exacto
total  = (sub - desc).quantize(Decimal("1"), ROUND_HALF_EVEN)  # 1 = pesos enteros
print(total)                        # 94362  COP
# Verificación inversa: total ≈ subtotal * (1 - 0.07)
chk = (sub * Decimal("0.93")).quantize(Decimal("1"), ROUND_HALF_EVEN)
assert total == chk                 # 94362 == 94362  ✔
```

**Resultado: COP 94 362** (un solo redondeo al final; verificado por la vía equivalente `subtotal × 0.93`).

## Errores comunes / trampas

- **Redondear en cada paso.** Acumula error; el total final descuadra. Redondea una sola vez, al final.
- **Usar `float` para dinero.** `0.1 + 0.2 ≠ 0.3`. Usa `Decimal("...")` (desde string) o centavos enteros.
- **`round()` de Python es half-even**, pero opera sobre `float`, así que `round(2.675, 2)` da `2.67` (no `2.68`) por error de representación binaria. Para dinero usa `Decimal.quantize`, no `round`.
- **Confundir truncar con redondear.** Truncar `2.99 → 2` pierde casi un peso entero por línea.
- **Inventar precisión.** Reportar `tasa = 12.473829%` cuando los datos solo justifican `12.5%`. Los decimales de más mienten.
- **Mezclar half-up y half-even** en el mismo flujo: produce diferencias de centavos imposibles de cuadrar. Elige UN modo y documéntalo.
- **El "problema del centavo perdido"** al repartir un total entre líneas (ej. prorratear COP 100 entre 3): suma de redondeos individuales ≠ total. Solución: redondear y asignar el residuo a la última línea (algoritmo "largest remainder").

## Cruces

- [[12-fracciones-decimales-y-precision.md]] — por qué los float fallan y cómo manejar decimales exactos.
- [[14-porcentajes-sin-errores.md]] — descuentos e impuestos donde el redondeo prematuro descuadra.
- [[04-notacion-unidades-y-dimensiones.md]] — la precisión va atada a las unidades del instrumento.
- [[03-protocolo-de-verificacion-por-codigo.md]] — patrón ejecutar + verificar por segunda vía.
- [[06-estimacion-y-sanity-checks.md]] — chequeo de orden de magnitud para detectar redondeos rotos.

---

**Mini-checklist de exactitud:**
1. ¿Calculé todo en `Decimal`/centavos (no float) y redondeé UNA sola vez al final?
2. ¿El número de decimales reportado está justificado por los datos (no inventé precisión)?
3. ¿Verifiqué por segunda vía (inversa u orden de magnitud) que el redondeo no descuadró el total?
