# 76 · Punto de equilibrio

> **Qué resuelve / cuándo usarlo** — Calcula cuántas unidades vendes (o cuánto ingreso facturas) para no ganar ni perder. Úsalo antes de lanzar un producto, fijar un precio o decidir si un negocio "da".

## Concepto (para no-experto)

El **punto de equilibrio** (en inglés *break-even point*) es el nivel de ventas en el que tu negocio **no gana ni pierde**: las ventas alcanzan justo para pagar todos los costos. Un peso más de venta ya es ganancia; un peso menos, es pérdida.

Para entenderlo hay que separar los costos en dos clases:

- **Costos fijos (CF)**: los que pagas **vendas o no vendas**. No dependen de cuántas unidades produces. Ejemplos: arriendo del local, sueldo del personal de planta, internet, licencia de software, seguros. Si vendes 0 o 1.000 unidades, el arriendo es el mismo.
- **Costos variables (CV)**: los que **suben con cada unidad** que produces o vendes. Ejemplos: ingredientes de un plato, empaque, comisión por venta, materia prima. Se suelen expresar como **costo variable unitario (cvu)**: lo que te cuesta "fabricar" una unidad más.

La pieza central es el **margen de contribución (mc)**: lo que deja cada unidad vendida **después de pagar su propio costo variable**, para "contribuir" a cubrir los costos fijos.

> **Analogía cotidiana.** Imagina un puesto de limonada. El arriendo del puesto ($30.000 al día) es **fijo**: lo pagas vendas o no. Cada vaso te cuesta $500 en limones y azúcar (**variable**) y lo vendes a $2.000. Cada vaso "aporta" $2.000 − $500 = **$1.500** (margen de contribución) para ir pagando el arriendo. Necesitas $30.000 ÷ $1.500 = **20 vasos** solo para empatar. El vaso 21 ya es ganancia.

Definición de **precio (p)**: el valor al que vendes cada unidad. Y **utilidad**: lo que te queda al final (ganancia si es positiva, pérdida si es negativa).

## Fórmulas / método

Símbolos (todos por **unidad** salvo CF):

- `p` = precio de venta unitario \[$/unidad]
- `cvu` = costo variable unitario \[$/unidad]
- `CF` = costos fijos totales del periodo \[$]
- `Q` = cantidad de unidades vendidas \[unidades]

**Margen de contribución unitario:**

```
mc = p − cvu                          [$/unidad]
```

**Razón de margen de contribución** (qué fracción del precio queda como margen):

```
rmc = mc / p = (p − cvu) / p          [adimensional, 0 a 1]
```

**Punto de equilibrio en unidades:**

```
Q* = CF / mc = CF / (p − cvu)         [unidades]
```

**Punto de equilibrio en dinero (ingreso):**

```
Ingreso* = Q* · p = CF / rmc          [$]
```

**Unidades para una utilidad objetivo `U`:**

```
Q(U) = (CF + U) / mc                  [unidades]
```

**Utilidad para una cantidad dada Q:**

```
U(Q) = mc · Q − CF                    [$]
```

Reglas de exactitud: `mc` debe ser **positivo** (si `p ≤ cvu`, no hay punto de equilibrio: pierdes en cada venta). `Q*` casi nunca da entero → se **redondea hacia arriba** (ceil), porque no puedes vender 19,3 vasos; necesitas el 20.º para cubrir todo.

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_CEILING, ROUND_HALF_UP
import math

getcontext().prec = 28  # alta precisión; el dinero va en Decimal, NUNCA en float

def punto_equilibrio(precio, cvu, costos_fijos, utilidad_objetivo=Decimal("0")):
    """Punto de equilibrio exacto. Todos los montos en Decimal ($)."""
    p   = Decimal(precio)
    cv  = Decimal(cvu)
    CF  = Decimal(costos_fijos)
    U   = Decimal(utilidad_objetivo)

    mc = p - cv                              # margen de contribución unitario
    if mc <= 0:
        raise ValueError("mc <= 0: pierdes en cada unidad; no hay punto de equilibrio.")

    rmc = mc / p                             # razón de margen de contribución

    # Unidades exactas (fraccionarias) y unidades reales (enteras, hacia arriba)
    q_exacta = (CF + U) / mc
    q_entera = int(q_exacta.to_integral_value(rounding=ROUND_CEILING))

    # Ingreso de equilibrio: vía ceil (real) y vía CF/rmc (teórico) — redondeo final una vez
    ingreso_real = (Decimal(q_entera) * p).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    ingreso_teorico = (CF / rmc).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    return {
        "mc": mc, "rmc": rmc,
        "q_exacta": q_exacta, "q_entera": q_entera,
        "ingreso_real": ingreso_real, "ingreso_teorico": ingreso_teorico,
    }

r = punto_equilibrio(precio="10000", cvu="3500", costos_fijos="2600000")
print("mc =", r["mc"], "$/u")
print("rmc =", round(float(r["rmc"]) * 100, 2), "%")
print("Q* exacta =", r["q_exacta"], "u")
print("Q* entera =", r["q_entera"], "u")
print("Ingreso* (real) =", r["ingreso_real"], "$")
print("Ingreso* (teórico) =", r["ingreso_teorico"], "$")
```

**Verificación por segunda vía** (la utilidad en `Q*` debe ser ≥ 0 y casi cero en la unidad anterior debe ser < 0):

```python
def utilidad(Q, precio, cvu, CF):
    p, cv, CF = Decimal(precio), Decimal(cvu), Decimal(CF)
    return (p - cv) * Decimal(Q) - CF

p, cv, CF = "10000", "3500", "2600000"
q = r["q_entera"]

# 1) Inversa: en Q* la utilidad NO debe ser negativa
assert utilidad(q,   p, cv, CF) >= 0,  "Falla: en Q* aún se pierde"
# 2) En la unidad ANTERIOR todavía se debe perder (confirma que Q* es el mínimo)
assert utilidad(q-1, p, cv, CF) < 0,   "Falla: Q* no es el mínimo exacto"
# 3) Sanity check de orden de magnitud (estimación a mano)
aprox = 2_600_000 / (10_000 - 3_500)   # ~ 400
assert abs(q - aprox) < 1, "Falla el sanity check de magnitud"
print("OK — verificación cruzada pasó. Q* =", q, "unidades")
```

Salida esperada: `mc = 6500`, `rmc = 65.0 %`, `Q* exacta = 400`, `Q* entera = 400`, `Ingreso* = 4.000.000 $`, y todos los `assert` pasan.

## Ejemplo trabajado

**Caso (LatAm):** una dark kitchen vende un combo de almuerzo. Datos del mes:

- Precio del combo: **p = $10.000 COP/unidad**
- Costo variable por combo (insumos + empaque + comisión app): **cvu = $3.500 COP/unidad**
- Costos fijos mensuales (arriendo cocina + sueldo cocinero + servicios): **CF = $2.600.000 COP/mes**

**Paso 1 — margen de contribución:**
```
mc = p − cvu = 10.000 − 3.500 = 6.500 $/unidad
```
Cada combo deja $6.500 para ir pagando los costos fijos.

**Paso 2 — razón de margen:**
```
rmc = mc / p = 6.500 / 10.000 = 0,65 = 65 %
```
De cada $100 que entran, $65 sirven para cubrir lo fijo.

**Paso 3 — punto de equilibrio en unidades:**
```
Q* = CF / mc = 2.600.000 / 6.500 = 400 combos/mes
```
Como dio entero exacto, **400 combos/mes** (si hubiera dado 400,2, se redondea a **401**).

**Paso 4 — punto de equilibrio en dinero:**
```
Ingreso* = Q* · p = 400 · 10.000 = 4.000.000 $/mes
   (chequeo: CF / rmc = 2.600.000 / 0,65 = 4.000.000 $  ✓ coinciden)
```

**Interpretación con unidades:** necesita vender **400 combos/mes** (≈ **$4.000.000 COP/mes**, ≈ 13–14 combos al día) solo para no perder. El combo 401 deja $6.500 limpios. Si la meta es ganar **$1.300.000/mes**:
```
Q(U) = (CF + U) / mc = (2.600.000 + 1.300.000) / 6.500 = 600 combos/mes
```

## Errores comunes / trampas

- **Mezclar fijos con variables.** Una comisión de la app de delivery es **variable** (sube con cada venta), no fija. Clasificar mal mueve todo el resultado.
- **Usar precio sin IVA junto a costos con IVA** (o viceversa). Mantén una base consistente; ver [[14-porcentajes-sin-errores]].
- **Redondear hacia abajo `Q*`.** 400,2 combos NO es 400: con 400 todavía pierdes. Siempre **ceil** para el punto de equilibrio.
- **Margen negativo ignorado.** Si `p ≤ cvu`, vender más solo aumenta la pérdida; no existe punto de equilibrio. Hay que subir precio o bajar `cvu`.
- **Calcular dinero con float.** `0.1 + 0.2 ≠ 0.3` en float; usa `Decimal` o centavos enteros ([[12-fracciones-decimales-y-precision]]).
- **Suponer mc constante con descuentos por volumen.** Si el precio o el `cvu` cambian por escalas, el modelo lineal deja de valer; segmenta por tramos.
- **Olvidar el sueldo del dueño** dentro de CF: si no te lo pagas, el "equilibrio" es ficticio.

## Cruces

- [[80-margenes-bruto-contribucion-neto]] — el margen de contribución a fondo y sus primos (bruto, neto).
- [[81-costeo-y-costo-unitario]] — cómo calcular bien `cvu` y separar fijos de variables.
- [[82-pricing-markup-margin-y-elasticidad]] — fijar `p` para mover el punto de equilibrio.
- [[26-funciones-lineales-y-afines]] — el punto de equilibrio es la intersección de la recta de ingresos con la de costos.
- [[93-analisis-de-sensibilidad-y-escenarios]] — qué pasa con `Q*` si suben los insumos o baja el precio.

---

**Mini-checklist de exactitud**
- [ ] ¿Separé bien costos fijos vs variables, en una base consistente (con o sin IVA)?
- [ ] ¿`mc > 0` y redondeé `Q*` hacia arriba (ceil)?
- [ ] ¿Verifiqué que `U(Q*) ≥ 0` y `U(Q*−1) < 0` (segunda vía)?
