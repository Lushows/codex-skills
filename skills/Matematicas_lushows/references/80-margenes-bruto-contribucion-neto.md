# 80 · Márgenes: bruto, contribución y neto

> **Qué resuelve / cuándo usarlo** — Te dice cuánto de cada peso vendido te queda, en tres niveles distintos (bruto, contribución, neto), sin confundirlos ni con el *markup*. Úsalo cada vez que veas "margen" y necesites estar seguro de cuál es y sobre qué base se calcula.

## Concepto (para no-experto)

Imagina tu negocio como un balde con un chorro de agua entrando (las **ventas**, también llamadas *ingresos* o *facturación*: el dinero total que cobras) y varios huecos por donde se escapa agua (los **costos** y **gastos**). El **margen** mide qué fracción del agua que entró sigue en el balde después de tapar cierto tipo de huecos. Según qué huecos tapes, hablas de un margen u otro.

Tres términos que NO son sinónimos:

- **Costo de los bienes vendidos (COGS, *Cost of Goods Sold*)** — lo que te cuesta *producir o adquirir* exactamente lo que vendiste (materia prima, mercancía, mano de obra directa). En el caso de la Calculadora de GastroLatam, sería el costo de crear/entregar ese Excel.
- **Costos variables** — los que suben y bajan *con cada unidad vendida* (comisión de pasarela de pago, empaque, envío por pedido). El COGS suele ser variable, pero "costos variables" puede incluir más cosas.
- **Costos fijos** — los que pagas sí o sí, vendas mucho o nada (arriendo, salarios fijos, software mensual, publicidad de base).

Con esto, los tres márgenes son:

| Margen | Qué resta de las ventas | Pregunta que responde |
|---|---|---|
| **Bruto** | el COGS | ¿Gano dinero con el producto en sí? |
| **De contribución** | *todos* los costos variables | ¿Cuánto aporta cada venta a pagar los fijos? |
| **Neto** | *todo* (variables + fijos + impuestos + financieros) | ¿Gana plata el negocio al final? |

**Margen vs *markup* (la trampa más cara):** el **margen** se mide *sobre el precio de venta*; el ***markup*** (margen de marcación o sobreprecio) se mide *sobre el costo*. Un producto que cuesta \$100 y vendes a \$150 tiene **markup del 50%** (50 sobre 100) pero **margen del 33.3%** (50 sobre 150). Confundirlos te hace creer que ganas más de lo que ganas.

## Fórmulas / método

Sea, en una moneda (p. ej. COP) y para un período o por unidad:

- `V` = Ventas (ingresos)
- `COGS` = costo de bienes vendidos
- `CV` = costos variables totales
- `CF` = costos fijos totales
- `I` = impuestos + gastos financieros + otros no operativos

**Utilidad bruta** = `V − COGS`
**Margen bruto (%)** = `(V − COGS) / V × 100`

**Utilidad de contribución** = `V − CV`
**Margen de contribución (%)** = `(V − CV) / V × 100`
**Contribución unitaria** = `precio − costo_variable_unitario` (clave para el punto de equilibrio)

**Utilidad neta** = `V − COGS − (resto de CV) − CF − I` = `V − todos los costos`
**Margen neto (%)** = `Utilidad neta / V × 100`

**Margen vs markup (conversión exacta):**
- `margen = markup / (1 + markup)`
- `markup = margen / (1 − margen)`
- Precio desde costo y margen objetivo: `precio = costo / (1 − margen)`
- Precio desde costo y markup: `precio = costo × (1 + markup)`

Todos los `%` son adimensionales (fracción × 100). El denominador del **margen** SIEMPRE es `V` (ventas); el del **markup** SIEMPRE es el costo. Ese es el único punto donde se cometen el 90% de los errores.

## Verificación en código

```python
# Márgenes con dinero EXACTO usando decimal (nunca float para plata)
from decimal import Decimal, ROUND_HALF_UP

def pct(num, den):
    """Devuelve porcentaje exacto num/den*100 como Decimal."""
    if den == 0:
        raise ZeroDivisionError("Ventas = 0: el margen no está definido")
    return (Decimal(num) / Decimal(den) * Decimal(100))

# --- Caso GastroLatam: Calculadora de Costos (Excel), pago único ---
precio        = Decimal("10000")   # COP por venta
cogs_unit     = Decimal("0")       # producto digital: costo de bienes ~0
comision_pago = Decimal("1490")    # pasarela ~ 2.99% + 1.190 fijo (variable)
# costos variables totales por unidad = COGS + comisión
cv_unit       = cogs_unit + comision_pago

# Fijos del mes y unidades vendidas en el mes
cf_mes        = Decimal("600000")  # software + hosting + parte de ads fija
unidades      = Decimal("400")
impuestos     = Decimal("0")       # simplificado para el ejemplo

ventas = precio * unidades
util_bruta       = ventas - (cogs_unit * unidades)
util_contrib     = ventas - (cv_unit  * unidades)
util_neta        = ventas - (cv_unit * unidades) - cf_mes - impuestos

mb = pct(util_bruta, ventas)
mc = pct(util_contrib, ventas)
mn = pct(util_neta, ventas)

q = Decimal("0.01")  # redondear UNA sola vez, al final, a 2 decimales
print("Ventas:            COP", ventas)
print("Margen bruto:      ", mb.quantize(q, ROUND_HALF_UP), "%")
print("Margen contribuc.: ", mc.quantize(q, ROUND_HALF_UP), "%")
print("Margen neto:       ", mn.quantize(q, ROUND_HALF_UP), "%")

# --- VERIFICACIÓN POR SEGUNDA VÍA ---
# (1) Inversa: reconstruir el precio desde costo + margen de contribución.
#     contribución unitaria = precio - cv_unit; margen_c = contrib/precio
margen_c_frac = (precio - cv_unit) / precio
precio_reconstruido = cv_unit / (1 - margen_c_frac)
assert precio_reconstruido == precio, "Falla la inversa precio<->margen"

# (2) Identidad margen<->markup sobre la contribución unitaria
markup = (precio - cv_unit) / cv_unit            # sobre costo
margen = (precio - cv_unit) / precio             # sobre venta
assert margen == markup / (1 + markup), "margen != markup/(1+markup)"

# (3) Sanity / orden de magnitud: neto <= contribución <= bruto siempre
assert mn <= mc <= mb, "Jerarquía de márgenes rota: revisar costos"
print("Verificaciones OK")
```

Salida esperada (resumen): Ventas COP 4 000 000; **margen bruto 100.00%** (digital, COGS≈0), **contribución 85.10%**, **neto 70.10%**.

## Ejemplo trabajado

Restaurante que vende una **bandeja paisa** a **\$28.000 COP**.

- Costo de ingredientes (COGS) de esa bandeja: **\$11.200**
- Costo variable extra por plato (gas, empaque domicilio): **\$2.800**
- Costos fijos del mes (arriendo, cocina, salarios fijos): **\$9.000.000**
- Platos vendidos en el mes: **900**

Paso 1 — Por unidad:
- Utilidad bruta unitaria = 28.000 − 11.200 = **\$16.800**
- Margen bruto = 16.800 / 28.000 = 0.60 → **60.00%**
- Contribución unitaria = 28.000 − (11.200 + 2.800) = 28.000 − 14.000 = **\$14.000**
- Margen de contribución = 14.000 / 28.000 = 0.50 → **50.00%**

Paso 2 — Mes (900 platos):
- Ventas = 28.000 × 900 = **\$25.200.000 COP**
- Contribución total = 14.000 × 900 = **\$12.600.000 COP**
- Utilidad neta = 12.600.000 − 9.000.000 = **\$3.600.000 COP**
- Margen neto = 3.600.000 / 25.200.000 = **14.29%**

Verificación (orden de magnitud y jerarquía): 60% ≥ 50% ≥ 14.29% ✓. Inversa del *markup*: el plato tiene *markup* sobre COGS de 16.800/11.200 = **150%**, y margen = 150% / (1+150%) = 60% ✓ — coincide con el margen bruto. **Resultado: margen neto 14.29% (COP 3.600.000 de utilidad en el mes).**

## Errores comunes / trampas

- **Confundir margen con markup.** "Le pongo 40% de margen" multiplicando el costo por 1.40 → eso es *markup* 40%, margen real 28.6%. Usa `precio = costo / (1 − margen)`.
- **Dividir sobre el costo creyendo que es margen.** El margen SIEMPRE va sobre ventas.
- **Meter costos fijos en el margen de contribución.** La contribución solo resta *variables*; si metes el arriendo, ya no sirve para el punto de equilibrio.
- **Mezclar períodos:** ventas del mes con fijos del año (o al revés). Unidades de tiempo deben coincidir.
- **Usar `float` para dinero.** `0.1 + 0.2 != 0.3` en float; usa `decimal` o centavos enteros.
- **Redondear a mitad de camino.** Redondea una sola vez, al final.
- **Reportar margen bruto como si fuera la ganancia real.** Un margen bruto del 80% puede convivir con utilidad neta negativa si los fijos son altos.

## Cruces

- [[81-costeo-y-costo-unitario]] — de dónde sale el COGS y el costo variable unitario que alimenta estas fórmulas.
- [[82-pricing-markup-margin-y-elasticidad]] — fijar el precio a partir del margen objetivo; markup vs margin a fondo.
- [[76-punto-de-equilibrio]] — usa la contribución unitaria para saber cuántas unidades pagan los fijos.
- [[14-porcentajes-sin-errores]] — la mecánica de "sobre qué base" que evita el error margen/markup.
- [[78-flujo-de-caja-y-presupuesto]] — la utilidad neta vs el efectivo real disponible.

**Mini-checklist de exactitud**
1. ¿El denominador del margen es **ventas** (no costo)? ¿Y el del markup es **costo**?
2. ¿La contribución resta **solo variables** y el neto resta **todo**, con períodos que coinciden?
3. ¿Se cumple **neto ≤ contribución ≤ bruto** y el dinero se calculó con `decimal`, redondeando una sola vez?
