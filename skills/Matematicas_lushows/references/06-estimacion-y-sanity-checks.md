# 06 · Estimación y sanity checks

> **Qué resuelve / cuándo usarlo** — Antes de entregar cualquier número, comprueba que sea *plausible*: estima el orden de magnitud "a mano" y compáralo con el cálculo exacto. Es nuestra segunda vía de verificación más rápida y la que atrapa los errores más caros (un cero de más, una unidad mal, una fórmula equivocada).

## Concepto (para no-experto)

Un **sanity check** ("chequeo de cordura") es preguntarse: *"¿tiene sentido este número?"* antes de confiar en él. No busca la respuesta exacta; busca detectar lo absurdo. Si calculas el costo mensual de un café y te sale **$48.000.000 COP**, no necesitas revisar la fórmula: ya sabes que está mal porque un café no cuesta lo que un carro.

La herramienta central es la **estimación de orden de magnitud**: en lugar de un número exacto, calculas "más o menos cuántos ceros tiene". El **orden de magnitud** de un número es la potencia de 10 más cercana. Por ejemplo, 850 es del orden de 10³ (mil), y 47.000 es del orden de 10⁴–10⁵ (decenas de miles). Si el cálculo exacto y la estimación tienen *distinto número de ceros*, hay un error grave en alguna parte.

La **estimación de Fermi** (por el físico Enrico Fermi, famoso por estimar cosas imposibles de medir directamente, como "¿cuántos afinadores de piano hay en Chicago?") consiste en **descomponer** un problema grande en factores que sí puedes estimar, redondear cada uno a una cifra cómoda, multiplicarlos, y aceptar que el resultado tiene un margen de error pero el **orden de magnitud** es confiable.

**Analogía cotidiana:** cuando vas al supermercado y llenas el carrito, sumas mentalmente "como $5.000 cada cosa, llevo unas 20 → unos $100.000". No es exacto, pero si en caja te dicen "$850.000" sabes inmediatamente que algo está mal (te cobraron de más o leíste mal). Esa suma mental es un sanity check.

## Fórmulas / método

**Orden de magnitud** de un número positivo `x`:

```
om(x) = floor(log10(x))
```

donde `log10` es el logaritmo base 10 (cuántas veces hay que multiplicar 10 por sí mismo para llegar a x) y `floor` es "redondear hacia abajo". Ejemplos: om(850)=2, om(7.500)=3, om(47.000)=4.

**Test de plausibilidad** entre un valor exacto `E` y una estimación `S`:

```
plausible  ⇔  | log10(E) − log10(S) | ≤ 1
```

Es decir, **están dentro de un factor de 10** (un orden de magnitud) uno del otro. Equivale a que la razón `E/S` esté entre 0,1 y 10.

**Estimación de Fermi** — descomposición multiplicativa:

```
Resultado ≈ f₁ × f₂ × f₃ × … × fₙ
```

donde cada `fᵢ` es un factor estimado y redondeado. Las unidades de los factores deben **cancelarse correctamente** hasta dejar la unidad final (ver `04`). Truco de Fermi: redondea cada factor a 1 cifra significativa; los errores por exceso y por defecto tienden a compensarse.

**Cotas (acotar el resultado):** estima un **límite inferior** (todo redondeado "para abajo") y un **límite superior** (todo "para arriba"). El valor verdadero debe caer dentro: `cota_inf ≤ verdadero ≤ cota_sup`.

## Verificación en código

Patrón de la skill: **calcular exacto** (con `decimal` para dinero) y **verificar con una estimación independiente** (un `assert` que falla si el resultado no es plausible).

```python
from decimal import Decimal, ROUND_HALF_UP
import math

# --- CÁLCULO EXACTO: costo mensual de insumos de un café de barrio ---
# Vende 120 cafés/día, 26 días/mes. Cada café usa 18 g de café tostado.
# El kilo de café cuesta 38.000 COP.  (dinero -> Decimal, NUNCA float)
cafes_dia      = 120
dias_mes       = 26
gramos_por_taza = Decimal("18")      # g
precio_kilo     = Decimal("38000")   # COP / 1000 g

tazas_mes   = cafes_dia * dias_mes                       # 3120 tazas
gramos_mes  = gramos_por_taza * tazas_mes                # g
kilos_mes   = gramos_mes / Decimal("1000")              # g -> kg
costo_exacto = (kilos_mes * precio_kilo).quantize(       # COP
    Decimal("1"), rounding=ROUND_HALF_UP)               # redondeo UNA vez al final
print("Tazas/mes:", tazas_mes)
print("Costo exacto:", costo_exacto, "COP/mes")

# --- 2ª VÍA: ESTIMACIÓN DE FERMI (orden de magnitud, redondeo grueso) ---
# ~100 cafés/día x ~25 días = ~2.500 tazas. ~20 g c/u = 50.000 g = 50 kg.
# ~40.000 COP/kg -> ~2.000.000 COP/mes
estimacion = 2500 * 20 / 1000 * 40000   # COP, float a propósito (solo estima)
print("Estimación Fermi:", int(estimacion), "COP/mes")

# --- SANITY CHECK: exacto y estimación dentro de 1 orden de magnitud ---
diff_ordenes = abs(math.log10(float(costo_exacto)) - math.log10(estimacion))
assert diff_ordenes <= 1, f"INVEROSÍMIL: difieren {diff_ordenes:.2f} órdenes"
print(f"OK plausible (difieren {diff_ordenes:.3f} órdenes de magnitud)")
```

Salida esperada:

```
Tazas/mes: 3120
Costo exacto: 2134080 COP/mes
Estimación Fermi: 2000000 COP/mes
OK plausible (difieren 0.028 órdenes de magnitud)
```

Segunda vía adicional por **cotas** (el verdadero debe quedar encajonado):

```python
# Cota inferior: 100 tazas/día, 25 días, 15 g, 35.000/kg
cota_inf = 100*25 * 15/1000 * 35000      # 1.312.500
# Cota superior: 130 tazas/día, 27 días, 20 g, 40.000/kg
cota_sup = 130*27 * 20/1000 * 40000      # 2.808.000
assert cota_inf <= float(costo_exacto) <= cota_sup, "fuera de cotas"
print(f"Encajonado: {int(cota_inf):,} <= {costo_exacto} <= {int(cota_sup):,}  OK")
```

## Ejemplo trabajado

**Pregunta de Fermi (LatAm):** *¿Cuánto factura al mes una dark kitchen de almuerzos en Bogotá que vende por apps de domicilio?*

No tenemos el dato; lo **construimos** descomponiendo en factores estimables:

| Factor | Estimación (1 cifra sig.) | Unidad |
|---|---|---|
| Pedidos por día | 80 | pedidos/día |
| Días operados al mes | 26 | días/mes |
| Ticket promedio | 28.000 | COP/pedido |

Cálculo:

```
Facturación ≈ 80 pedidos/día × 26 días/mes × 28.000 COP/pedido
            = 80 × 26 × 28.000  COP/mes
            = 58.240.000 COP/mes  ≈ 58 millones COP/mes
```

Las unidades se cancelan así: `(pedidos/día)·(días/mes)·(COP/pedido) = COP/mes`. ✔ (ver `04`)

**Verificación 1 — orden de magnitud:** ~10² pedidos/día × ~10¹ días × ~10⁴ COP ≈ 10⁷ → **decenas de millones**. Coincide: 58 millones es 10⁷·5,8. Plausible.

**Verificación 2 — cotas:** rango pesimista 60×24×24.000 ≈ **34,6 M** y optimista 100×27×32.000 ≈ **86,4 M**. El estimado (58 M) cae dentro. ✔

**Verificación 3 — vía independiente (margen):** si la dark kitchen deja ~12% neto, ganaría ≈ 7 M COP/mes; razonable para un negocio chico. Si nos hubiera salido "facturación 580 M/mes → utilidad 70 M/mes", el sanity check de "utilidad de pyme" lo rechazaría.

**Respuesta:** ≈ **58 millones COP/mes** (orden de magnitud confiable: decenas de millones COP/mes; el número exacto depende de datos reales que habría que medir).

## Errores comunes / trampas

- **Confundir estimación con resultado final.** Fermi da el *orden de magnitud*, no el número de la factura. Para el dinero que se cobra/paga, calcula exacto con `decimal` (`12`, `14`).
- **Error de un cero (×10 o ÷10).** Es el error más caro y el que el sanity check detecta mejor. Siempre compara cantidad de ceros antes de entregar.
- **Unidades que no cancelan.** Multiplicar "gramos" por "COP/kilo" sin convertir g→kg da un número 1.000 veces mal. La estimación dimensional lo atrapa (`04`, `37`).
- **Anclarse al primer número que sale.** Si el cálculo "se ve serio", uno tiende a creerlo. El sanity check es justo el antídoto: dudar a propósito.
- **Estimar y calcular con el mismo método.** Si ambos comparten el mismo error de fórmula, "coinciden" pero los dos están mal. La 2ª vía debe ser *independiente* (otra ruta, no la misma cuenta repetida).
- **Sumar muchos factores redondeados sin notar el sesgo.** Redondear siempre "para arriba" infla el total; en Fermi se redondea a la cifra más cercana para que los errores se compensen.

## Cruces

- [[03-protocolo-de-verificacion-por-codigo]] — la estimación es una de las "segundas vías" obligatorias.
- [[02-mentalidad-de-exactitud-error-cero]] — por qué dudar de todo número antes de entregarlo.
- [[17-notacion-cientifica-y-magnitudes]] — manejar potencias de 10 y órdenes de magnitud.
- [[04-notacion-unidades-y-dimensiones]] — el análisis dimensional como sanity check.
- [[89-trampas-de-metricas-y-dashboards]] — números de negocio que "se ven bien" pero son absurdos.

---

**Mini-checklist de exactitud**
- [ ] ¿El orden de magnitud (cantidad de ceros) del resultado coincide con una estimación rápida e independiente?
- [ ] ¿Las unidades del resultado salen correctas al cancelar las de los factores?
- [ ] ¿El valor exacto cae entre la cota inferior y la superior que estimé?
