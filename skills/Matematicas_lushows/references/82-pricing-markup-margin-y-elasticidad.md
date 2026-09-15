# 82 · Pricing: markup, margin y elasticidad

> **Qué resuelve / cuándo usarlo** — Para fijar el precio de venta sin perder plata: traduce el costo y el margen que quieres ganar en un precio exacto, y estima cuánto caerían las ventas si subes el precio (elasticidad). Úsalo cada vez que pongas o ajustes un precio.

## Concepto (para no-experto)

Imagina que compras una camiseta a **$10.000** (eso es el **costo**, lo que te cuesta a ti el producto) y la vendes a **$15.000** (ese es el **precio de venta**, lo que paga el cliente). Ganaste **$5.000** de diferencia: a eso lo llamamos **utilidad bruta** o **markup en pesos**.

Ahora, ¿qué porcentaje es esa ganancia? Aquí está la confusión más cara del comercio y la que más plata hace perder:

- **Markup** (margen sobre el **costo**): la ganancia comparada con lo que TE costó. $5.000 / $10.000 = **50%** de markup.
- **Margin** (margen sobre el **precio**): la ganancia comparada con lo que el CLIENTE pagó. $5.000 / $15.000 = **33,3%** de margin.

Es la **misma plata** ($5.000), pero el porcentaje cambia según contra qué la compares. Un comerciante que dice "trabajo al 50%" puede estar hablando de markup (gana 50% sobre el costo) o de margin (gana 50% sobre el precio), y son precios MUY distintos. Confundirlos hace que pongas un precio más bajo del que crees y te quedes sin ganancia.

**Analogía:** markup es "subí el precio la mitad de lo que me costó"; margin es "de cada peso que entra a la caja, esta fracción es ganancia". El primero mira hacia abajo (el costo), el segundo mira hacia adentro (la venta).

La segunda mitad del módulo es la **elasticidad precio-demanda**: un número que responde "si subo el precio 10%, ¿cuánto bajan las ventas?". Si suben mucho las quejas y se van los clientes, la demanda es **elástica** (sensible al precio). Si nadie se inmuta, es **inelástica**. Esto decide si subir el precio te da MÁS o MENOS ingreso total.

## Fórmulas / método

Símbolos (todos con unidades de dinero en la misma moneda, p. ej. COP):

- `C` = costo unitario (lo que te cuesta una unidad)
- `P` = precio de venta unitario
- `U = P − C` = utilidad bruta unitaria (en $)

**Markup (sobre costo):**

```
markup% = (P − C) / C
P = C · (1 + markup%)
```

**Margin (margen bruto, sobre precio):**

```
margin% = (P − C) / P
P = C / (1 − margin%)      ← precio objetivo desde el margen deseado
```

**Conversión entre ambos (la regla de oro para no equivocarse):**

```
margin% = markup% / (1 + markup%)
markup% = margin% / (1 − margin%)
```

**Elasticidad precio-demanda (E):** mide el % de cambio de la cantidad vendida `Q` ante un % de cambio del precio `P`.

```
E_punto = (dQ/dP) · (P/Q)                      ← elasticidad puntual (cálculo)
E_arco  = ((Q2−Q1)/((Q1+Q2)/2)) / ((P2−P1)/((P1+P2)/2))   ← elasticidad arco (dos puntos)
```

E suele ser **negativa** (subes precio → bajan ventas). Se interpreta por su valor absoluto |E|:

- |E| > 1 → **elástica**: subir precio reduce el **ingreso total** (`P·Q`).
- |E| < 1 → **inelástica**: subir precio aumenta el ingreso total.
- |E| = 1 → **unitaria**: el ingreso no cambia.

Unidades: markup%, margin% y E son **adimensionales** (razones puras); `C`, `P`, `U` van en moneda.

## Verificación en código

```python
# Pricing exacto: markup, margin y precio objetivo. Dinero con Decimal (NUNCA float).
from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 28

def money(x):  # redondea UNA vez al final, a peso entero (COP no usa centavos)
    return Decimal(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

C = Decimal("10000")   # costo unitario (COP)
P = Decimal("15000")   # precio de venta (COP)

U        = P - C                 # utilidad bruta unitaria
markup   = (P - C) / C           # margen sobre costo
margin   = (P - C) / P           # margen sobre precio

print("Utilidad $:", money(U))             # 5000
print("Markup  %:", markup * 100)          # 50
print("Margin  %:", margin * 100)          # 33.333...

# Precio objetivo desde un MARGIN deseado del 40%
margin_deseado = Decimal("0.40")
P_objetivo = C / (1 - margin_deseado)      # = 10000 / 0.60
print("Precio p/ 40% margin:", money(P_objetivo))   # 16667

# --- VERIFICACIÓN POR SEGUNDA VÍA ---
# 1) Conversión cruzada markup<->margin debe ser consistente
assert markup / (1 + markup) == margin            # markup -> margin
assert margin / (1 - margin) == markup            # margin -> markup
# 2) El precio objetivo, reinsertado, debe devolver EXACTAMENTE 40% de margin
margin_check = (P_objetivo - C) / P_objetivo
assert abs(margin_check - margin_deseado) < Decimal("1e-12")
# 3) Trampa clásica: tratar margin como si fuera markup da un precio MENOR
P_si_confundo = C * (1 + margin_deseado)          # 10000*1.40 = 14000 (¡mal!)
assert money(P_si_confundo) < money(P_objetivo)   # confundir cuesta plata
print("OK: conversiones y precio objetivo verificados")
```

```python
# Elasticidad arco + efecto en ingreso total. Cantidades pueden ir en float; el dinero, Decimal.
from decimal import Decimal
P1, Q1 = Decimal("15000"), Decimal("100")   # precio y unidades/mes antes
P2, Q2 = Decimal("18000"), Decimal("80")    # después de subir precio

dQ_pct = (Q2 - Q1) / ((Q1 + Q2) / 2)        # cambio % de cantidad (método punto medio)
dP_pct = (P2 - P1) / ((P1 + P2) / 2)        # cambio % de precio
E = dQ_pct / dP_pct
print("Elasticidad arco E:", E)             # ~ -1.22  -> ELASTICA

ingreso1 = P1 * Q1                            # 1.500.000
ingreso2 = P2 * Q2                            # 1.440.000
print("Ingreso antes:", ingreso1, "| después:", ingreso2)

# VERIFICACIÓN: si |E|>1 el ingreso debe CAER al subir precio
assert abs(E) > 1 and ingreso2 < ingreso1
print("OK: elástica => subir precio bajó el ingreso, coherente")
```

## Ejemplo trabajado

**Caso (cafetería en Bogotá):** un sánduche te cuesta producir `C = $4.200 COP`. Quieres un **margin del 35%** (de cada peso vendido, 35 centavos son ganancia bruta). ¿A qué precio lo vendes?

Paso 1 — precio objetivo desde el margin:
`P = C / (1 − margin) = 4.200 / (1 − 0,35) = 4.200 / 0,65 = $6.461,54`
Redondeas al final a precio comercial: **$6.500 COP**.

Paso 2 — verifica el margin real a $6.500:
`margin = (6.500 − 4.200) / 6.500 = 2.300 / 6.500 = 35,38%` ✓ (≥ 35%, bien).

Paso 3 — ¿cuál es el markup equivalente? `markup = 2.300 / 4.200 = 54,76%`. Es decir, subiste el precio ~55% sobre el costo para lograr ~35% de margin. **Mismo precio, dos números distintos.**

Paso 4 — la trampa: si hubieras hecho `4.200 × 1,35 = $5.670` creyendo que "35%" se aplica al costo, tu margin real habría sido solo `(5.670−4.200)/5.670 = 25,9%`, casi 10 puntos menos de ganancia. En 1.000 sánduches/mes eso son **$830.000 COP** de utilidad bruta perdida.

**Resultado:** vender a **$6.500 COP/unidad** da **35,4% de margin** (54,8% de markup), con utilidad bruta de **$2.300 COP/unidad**.

## Errores comunes / trampas

- **Confundir markup con margin** (el error #1, ya mostrado): tratar el margin deseado como markup deja el precio bajo y la ganancia más chica de lo que crees. Usa `P = C/(1−margin)` para margin, `P = C·(1+markup)` para markup.
- **Creer que markup% y margin% son iguales.** Nunca lo son (salvo en 0%). 50% markup = 33,3% margin; 100% markup = 50% margin.
- **Restar el descuento del margin directamente.** Un 20% de descuento NO baja el margin en 20 puntos; recalcula el margin con el precio ya descontado.
- **Olvidar costos variables más allá del producto** (comisión de pasarela, empaque, flete) al calcular `C`: infla el margin aparente. Ver [[81-costeo-y-costo-unitario]].
- **Calcular elasticidad con la fórmula simple `%ΔQ/%ΔP`** en cambios grandes: da resultados distintos según el punto base. Usa la **elasticidad arco** (punto medio), que es simétrica.
- **Asumir elasticidad constante** y subir precios sin techo: la demanda casi siempre se vuelve más elástica a precios altos.
- **Redondear a mitad de cuenta** (p. ej. redondear el margin antes de calcular el precio): redondea UNA sola vez, al final. Ver [[05-cifras-significativas-y-redondeo]].

## Cruces

- [[80-margenes-bruto-contribucion-neto]] — de dónde sale el margin bruto y cómo encaja con contribución y neto.
- [[81-costeo-y-costo-unitario]] — calcular bien `C` (el costo unitario) antes de fijar precio.
- [[76-punto-de-equilibrio]] — cuántas unidades necesitas vender a ese precio para no perder.
- [[14-porcentajes-sin-errores]] — la base de markup/margin: porcentajes sobre distinta base.
- [[43-optimizacion-con-derivadas]] — hallar el precio que maximiza ingreso/utilidad usando elasticidad.

---

**Mini-checklist de exactitud**
- [ ] ¿Calculé el precio con `C/(1−margin)` para margin (no `C·(1+margin)`)?
- [ ] ¿Verifiqué el margin real reinsertando el precio final y redondeé una sola vez?
- [ ] ¿Usé elasticidad arco (punto medio) y confirmé el signo y el efecto en el ingreso total?
