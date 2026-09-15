# 72 · Valor presente y futuro

> **Qué resuelve / cuándo usarlo** — Te dice cuánto vale HOY un dinero que recibirás (o pagarás) en el futuro, y cuánto valdrá en el futuro un dinero que tienes hoy. Es la base para comparar peras con manzanas cuando el dinero llega en momentos distintos.

## Concepto (para no-experto)

Imagina que un cliente te ofrece dos opciones: te paga **$1.000.000 hoy**, o te paga **$1.000.000 dentro de un año**. ¿Son lo mismo? **No.** El millón de hoy vale más, porque puedes ponerlo a trabajar (un CDT, reinvertir en tu negocio) y al cabo de un año tendrás *más* de un millón. Y al revés: un millón que recibirás en un año, traído a hoy, vale *menos* de un millón. A esto se le llama el **valor del dinero en el tiempo**.

Definamos los términos clave la primera vez:

- **Valor futuro (VF)** — cuánto valdrá una cantidad de dinero en una fecha futura, después de ganar intereses. Es lo que pasa cuando **capitalizas** (dejas que el dinero crezca).
- **Valor presente (VP)** — cuánto vale HOY una cantidad de dinero futura. Se obtiene al **descontar** (quitarle el "crecimiento" que tendría, para traerlo al presente).
- **Tasa de descuento / tasa de interés (i)** — el porcentaje por período que usamos para mover el dinero en el tiempo. Es el "precio" del tiempo. Ejemplo: 2 % mensual.
- **Número de períodos (n)** — cuántos saltos de tiempo hay. Si la tasa es mensual, n se cuenta en meses.

**Analogía cotidiana:** capitalizar es como inflar un globo (de hoy hacia adelante, crece). Descontar es desinflarlo de regreso al tamaño de hoy. La tasa `i` dice qué tan rápido infla o desinfla.

**Regla de oro de la consistencia:** la tasa y los períodos deben estar en la **misma unidad de tiempo**. Si la tasa es mensual, n va en meses. Mezclar una tasa anual con n en meses es el error #1 de este tema.

## Fórmulas / método

Con **interés compuesto** (los intereses generan más intereses — ver [[71-interes-simple-y-compuesto]]):

```
Capitalizar (VP → VF):   VF = VP × (1 + i)^n
Descontar  (VF → VP):    VP = VF / (1 + i)^n  =  VF × (1 + i)^(-n)
```

Donde:
- `VF` = valor futuro (en unidad monetaria, p. ej. COP)
- `VP` = valor presente (misma unidad monetaria)
- `i` = tasa por período, en **decimal** (2 % → `0.02`)
- `n` = número de períodos (adimensional, pero "amarrado" a la unidad de `i`)

El factor `(1 + i)^n` se llama **factor de capitalización**; su inverso `(1 + i)^(-n)` es el **factor de descuento**.

Despejes útiles (para verificar por inversa):
```
i = (VF / VP)^(1/n) − 1          ← tasa implícita
n = ln(VF / VP) / ln(1 + i)      ← cuántos períodos (ver [[16-logaritmos]])
```

> Si necesitas pasar de una tasa anual a una mensual (o viceversa) correctamente, ve a [[75-tasas-nominal-efectiva-y-real]]. No dividas la tasa anual entre 12 a la ligera: eso solo vale para tasas nominales, no efectivas.

## Verificación en código

Dinero SIEMPRE con `decimal`, NUNCA `float`, para no arrastrar errores de redondeo binario.

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 40  # precisión interna alta; redondeamos UNA vez al final

def valor_futuro(vp: Decimal, i: Decimal, n: int) -> Decimal:
    """VF = VP * (1+i)^n   — capitalizar (hoy -> futuro)."""
    return vp * (Decimal(1) + i) ** n

def valor_presente(vf: Decimal, i: Decimal, n: int) -> Decimal:
    """VP = VF / (1+i)^n   — descontar (futuro -> hoy)."""
    return vf / (Decimal(1) + i) ** n

def cop(x: Decimal) -> Decimal:
    """Redondea a peso entero (COP no usa centavos). Redondeo UNA sola vez, al final."""
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

# --- Caso: ¿cuánto valdrán hoy $1.000.000 que recibiré en 12 meses, a 2% mensual? ---
VF = Decimal("1000000")
i  = Decimal("0.02")
n  = 12

vp = valor_presente(VF, i, n)
print("VP (sin redondear):", vp)
print("VP redondeado     :", cop(vp), "COP")
```

Verificación por **segunda vía** (operación inversa: si descontar es correcto, capitalizar el VP debe devolver el VF):

```python
# Vía 1 ya hecha: descontamos VF -> vp
# Vía 2 (inversa): capitalizamos vp -> debe reconstruir VF
vf_reconstruido = valor_futuro(vp, i, n)

# Comparamos con tolerancia mínima (ambos sin redondear -> deben coincidir casi exacto)
diferencia = abs(vf_reconstruido - VF)
assert diferencia < Decimal("0.0000001"), f"Inversa falla, dif={diferencia}"
print("Inversa OK: capitalizar(VP) =", cop(vf_reconstruido), "= VF original ✔")

# Sanity check de orden de magnitud (ver modulo 06):
# 2% mensual ~ poco menos del 27% efectivo anual -> VP debe ser ~ 1.000.000 / 1.27 ~ 787.000
# nuestro VP redondeado debe caer cerca de esa cifra
estimacion = Decimal("1000000") / Decimal("1.27")
print("Estimacion rapida ~", cop(estimacion), "COP (debe ser cercana al VP)")
```

Salida esperada:
```
VP (sin redondear): 788.493196...   (más decimales)
VP redondeado     : 788493 COP
Inversa OK: capitalizar(VP) = 1000000 = VF original ✔
Estimacion rapida ~ 787402 COP (debe ser cercana al VP)
```

El VP (788.493) cae muy cerca de la estimación (787.402) → pasa el sanity check. Y la inversa reconstruye el VF exacto → doble verificación superada.

## Ejemplo trabajado

**Situación (GastroLatam):** Un proveedor te ofrece un descuento si pagas por adelantado. Tienes que decidir si te conviene tener **$5.000.000 COP hoy** o **$5.500.000 COP dentro de 8 meses**. Tu dinero, puesto en tu negocio, te rinde aproximadamente **2,5 % mensual** (esa es tu tasa de descuento).

**Paso 1 — Definir variables (con unidades):**
- VF = $5.500.000 COP (lo que recibirías en el futuro)
- i = 2,5 % mensual = `0.025`
- n = 8 meses
- Tasa y períodos coinciden en "meses" ✔

**Paso 2 — Traer los $5.500.000 a hoy (descontar):**
```
VP = 5.500.000 / (1 + 0.025)^8
   = 5.500.000 / (1.025)^8
   = 5.500.000 / 1.218402...
   = 4.514.281,9... COP
```

**Paso 3 — Redondear UNA vez al final:** VP ≈ **$4.514.282 COP**.

**Paso 4 — Decidir:** Los $5.500.000 futuros valen hoy solo **$4.514.282 COP**, que es **menos** que los $5.000.000 que te ofrecen hoy. → **Conviene tomar los $5.000.000 hoy.**

**Verificación por inversa:** capitalizamos el VP 8 meses: `4.514.282 × (1.025)^8 ≈ 5.500.000` ✔ (reconstruye el VF). Y por orden de magnitud: 2,5 % × 8 ≈ 20 % "simple", el compuesto da algo más (~21,8 %), así que el VP debe ser ~5.500.000/1,218 ≈ 4,51 millones → coincide.

## Errores comunes / trampas

- **Mezclar unidades de tiempo.** Tasa anual con n en meses (o viceversa). Si i es anual, n va en años. Convierte primero ([[75-tasas-nominal-efectiva-y-real]]).
- **Usar la tasa en porcentaje en vez de decimal.** `(1 + 2)^n` en lugar de `(1 + 0.02)^n`. Siempre pasa el % a decimal dividiendo entre 100.
- **Confundir capitalizar con descontar** (poner la potencia con signo equivocado). Truco mental: el VP siempre es **menor** que el VF cuando i > 0; si te sale al revés, invertiste la fórmula.
- **Usar `float` para dinero.** `0.1 + 0.2 != 0.3` en float. Usa `Decimal` o centavos enteros ([[12-fracciones-decimales-y-precision]]).
- **Redondear en cada paso intermedio.** Acumula error. Redondea solo el resultado final ([[05-cifras-significativas-y-redondeo]]).
- **Ignorar la inflación.** Esta fórmula da valor *nominal*. Si quieres poder adquisitivo real, usa la tasa real ([[79-moneda-inflacion-y-devaluacion]]).
- **Asumir una tasa de descuento arbitraria.** La tasa cambia toda la decisión; sé honesto sobre de dónde sale (tu costo de oportunidad real).

## Cruces

- [[70-valor-del-dinero-en-el-tiempo]] — el principio conceptual del que sale todo esto.
- [[71-interes-simple-y-compuesto]] — de dónde viene el factor `(1+i)^n`.
- [[75-tasas-nominal-efectiva-y-real]] — convertir tasas entre períodos sin equivocarse.
- [[73-anualidades-y-amortizacion]] — VP/VF de *series* de pagos, no de un solo monto.
- [[74-vpn-y-tir]] — descontar varios flujos en el tiempo para evaluar un proyecto.

---

**Mini-checklist de exactitud:**
- [ ] ¿La tasa `i` (decimal) y `n` están en la **misma unidad de tiempo**?
- [ ] ¿El VP me dio **menor** que el VF (con i > 0)? Si no, revisé la fórmula.
- [ ] ¿Verifiqué por la inversa (capitalizar el VP reconstruye el VF) y por orden de magnitud?
