# 07 · Falacias y errores numéricos comunes

> **Qué resuelve / cuándo usarlo** — Catálogo de las trampas que producen números falsos aunque la aritmética "parezca" correcta. Úsalo como checklist antes de entregar cualquier cifra que sostenga una decisión de dinero.

## Concepto (para no-experto)

La mayoría de los números falsos en un negocio **no** vienen de sumar mal. Vienen de calcular *bien* la operación equivocada: tomar el porcentaje sobre la base que no era, promediar cosas que ya eran promedios, contar el mismo peso dos veces, o usar `float` (la forma en que el computador guarda números con decimales en binario, que **no** representa exactamente la mayoría de los decimales) para dinero.

Analogía cotidiana: si pesas frutas en una balanza descalibrada, puedes sumar los pesos con toda la precisión del mundo y el total seguirá estando mal. La balanza descalibrada aquí es **la definición** del cálculo, no la aritmética. Este módulo es la lista de balanzas descalibradas más frecuentes.

Términos que usaremos:
- **Base** (de un porcentaje): el número del que tomas un %. "20% de qué". Cambiar la base cambia todo.
- **Punto porcentual (pp)**: la diferencia *absoluta* entre dos porcentajes. De 10% a 12% hay **2 pp**, pero un **+20%** de cambio relativo.
- **Promedio ponderado**: promedio donde cada valor pesa según su tamaño (cuántos casos representa), no todos por igual.
- **Doble conteo**: sumar un mismo elemento más de una vez sin darte cuenta.
- **Off-by-one** ("error por uno"): equivocarte en 1 al contar elementos o días, casi siempre por confundir extremos incluidos/excluidos.

## Fórmulas / método

**1. Porcentaje sobre la base correcta.** El % de un cambio de A→B es:

```
cambio_relativo = (B − A) / A          ← base = valor inicial A, NUNCA B ni el promedio
```

Subir 100→120 es +20% (base 100). Bajar 120→100 es −16,67% (base 120). **No son simétricos.**

**2. Cambio en puntos porcentuales vs cambio relativo.** Si una tasa pasa de p₁ a p₂ (ambas en %):

```
Δ en puntos porcentuales  = p₂ − p₁                 [pp]
cambio relativo           = (p₂ − p₁) / p₁          [%]
```

**3. Promedio de promedios → usa promedio ponderado.** Si el grupo i tiene media mᵢ y tamaño nᵢ:

```
media_global = Σ(mᵢ · nᵢ) / Σ(nᵢ)      ← correcto
media_global ≠ Σ(mᵢ) / k                ← FALSO salvo que todos los nᵢ sean iguales
```

**4. Dinero:** trabaja en **centavos enteros** o con `Decimal`. Nunca `float`. Redondea **una sola vez** al final.

**5. División por cero / indeterminados:** toda razón `x/y` exige verificar `y ≠ 0`. Define explícitamente qué pasa cuando `y = 0` (p. ej. "tasa de conversión = 0 visitas → N/D, no 0%").

**6. Off-by-one (conteo inclusivo):** elementos del día D₁ al D₂ inclusive = `D₂ − D₁ + 1` (no `D₂ − D₁`).

## Verificación en código

```python
from decimal import Decimal, getcontext
getcontext().prec = 40

# ── TRAMPA 1: % sobre base equivocada (asimetría sube/baja) ──
A, B = Decimal("100"), Decimal("120")
sube = (B - A) / A            # base = A = 100
baja = (A - B) / B            # base = B = 120
print("sube 100→120:", sube * 100, "%")   # +20%
print("baja 120→100:", baja * 100, "%")   # -16.666...%
assert sube != -baja, "subir y bajar el mismo monto NO son % simétricos"

# ── TRAMPA 2: puntos porcentuales vs cambio relativo ──
p1, p2 = Decimal("10"), Decimal("12")     # tasa de conversión 10% -> 12%
delta_pp  = p2 - p1                        # 2 pp
delta_rel = (p2 - p1) / p1 * 100           # +20%
print("Δpp =", delta_pp, "pp   |   relativo =", delta_rel, "%")
assert delta_pp == Decimal("2") and delta_rel == Decimal("20")  # son cosas distintas

# ── TRAMPA 3: promediar promedios vs ponderar ──
# Sede A: 100 ventas, ticket medio $30.000 ; Sede B: 10 ventas, ticket medio $90.000
medias  = [Decimal("30000"), Decimal("90000")]
tamanos = [Decimal("100"),   Decimal("10")]
ingenuo    = sum(medias) / len(medias)                       # promedio de promedios (MAL)
ponderado  = sum(m*n for m, n in zip(medias, tamanos)) / sum(tamanos)
print("promedio de promedios (MAL):", ingenuo)              # 60.000
print("ponderado (BIEN):           ", ponderado)            # 35.454,54...

# ── TRAMPA 4: float en dinero ──
print("float 0.1+0.2 =", 0.1 + 0.2)                          # 0.30000000000000004
print("Decimal 0.1+0.2 =", Decimal("0.1") + Decimal("0.2"))  # 0.3 exacto
```

```python
# ── VERIFICACIÓN POR SEGUNDA VÍA ──
# (a) El ponderado se recupera del total real de ingresos / total de ventas.
ingresos_totales = Decimal("100")*Decimal("30000") + Decimal("10")*Decimal("90000")
ventas_totales   = Decimal("110")
assert ingresos_totales / ventas_totales == ponderado          # 3.900.000 / 110
print("check ponderado:", ingresos_totales, "/", ventas_totales, "=", ponderado)

# (b) Inversa del cambio: aplicar +20% y luego -16,666...% debe volver a 100.
assert A * (1 + sube) * (1 + baja) == A
print("ida y vuelta vuelve a", A)  # confirma la asimetría: distintos %, mismo retorno

# (c) División por cero: defínela en vez de dejar que reviente.
def conversion(compras, visitas):
    if visitas == 0:
        return None  # N/D, no 0% — no había a quién convertir
    return compras / visitas
assert conversion(0, 0) is None and conversion(5, 100) == Decimal("0.05")
print("conversion(0,0) =", conversion(0, 0))
```

Salida clave: `ingenuo = 60000` vs `ponderado = 35454,545…`; `0.1+0.2 = 0.30000000000000004` en float. Las dos vías concuerdan, así que el resultado correcto queda confirmado.

## Ejemplo trabajado

**Caso GastroLatam.** Un anuncio reporta: "la conversión del bot **subió del 4% al 5%**, ¡un +1% de mejora!". ¿Es correcto el +1%?

1. La conversión es una **tasa** (compras ÷ chats). Pasó de 4% a 5%.
2. El **cambio en puntos porcentuales** es `5% − 4% = 1 pp`. Decir "1 pp" es correcto.
3. El **cambio relativo** (cuánto mejoró respecto a sí misma) es `(5 − 4) / 4 = 0,25 = +25%`.
4. El anuncio mezcla ambos: escribe "+1%" cuando son **+1 pp** ó **+25%**. Decir "+1%" sugiere una mejora minúscula cuando en realidad la conversión creció una cuarta parte.

Comprobación con dinero, base 1.000 chats/mes y ticket $10.000 COP:
- Antes: `0,04 × 1.000 = 40` ventas → `40 × $10.000 = $400.000 COP`.
- Después: `0,05 × 1.000 = 50` ventas → `50 × $10.000 = $500.000 COP`.
- Aumento real: `$100.000 COP/mes`, es decir `100.000 / 400.000 = +25%` de ingresos. Concuerda con el cambio relativo.

**Resultado:** el titular honesto es **"+1 punto porcentual (+25% relativo), +$100.000 COP/mes"**, no "+1%". Verificado por dos vías (tasas e ingresos en COP), ambas dan +25%.

## Errores comunes / trampas

- **Base equivocada:** tomar el % sobre el valor final, o sobre un total que ya incluía la parte. Pregúntate siempre "% ¿de qué exactamente?".
- **Confundir pp con %:** "subió 5%" cuando en realidad subió 5 **pp**. En tasas (conversión, churn, interés) esto distorsiona enormemente.
- **Promediar promedios** sin ponderar por tamaño de cada grupo → da el peso a la sede/cohorte pequeña.
- **Sumar porcentajes de bases distintas:** "30% descuento + 20% descuento ≠ 50%". Es `1 − 0,7·0,8 = 44%`.
- **Doble conteo:** un cliente que compró dos veces contado como dos clientes nuevos; un pedido sumado al ingreso de dos meses; un lead en dos canales.
- **float en dinero:** `0.1+0.2`, totales de carrito, IVA. Usa `Decimal` o centavos enteros.
- **División por cero silenciosa:** ROAS/CAC/conversión con denominador 0 → N/D, no 0 ni infinito.
- **Off-by-one:** "del 1 al 31" son 31 días, no 30; rangos `[a, b]` inclusivos.
- **Redondear en cada paso:** acumula error. Redondea una sola vez al final.

## Cruces

- [[14-porcentajes-sin-errores]] — la mecánica correcta de bases, pp y descuentos encadenados.
- [[12-fracciones-decimales-y-precision]] — por qué `float` falla en dinero y cómo usar `Decimal`.
- [[60-estadistica-descriptiva]] — promedio ponderado vs simple, medianas y su uso correcto.
- [[06-estimacion-y-sanity-checks]] — atrapar estos errores con una estimación de orden de magnitud.
- [[89-trampas-de-metricas-y-dashboards]] — doble conteo y bases inconsistentes en KPIs y reportes.

---

**Mini-checklist de exactitud**
- [ ] ¿El % está tomado sobre la **base correcta**, y distingo **pp** de **% relativo**?
- [ ] ¿Ponderé promedios y descarté **doble conteo**; dinero en `Decimal`/centavos; denominadores ≠ 0?
- [ ] ¿Verifiqué por una **segunda vía** (inversa, total real o estimación) y redondeé **una sola vez**?
