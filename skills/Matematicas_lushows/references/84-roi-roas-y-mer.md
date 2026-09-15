# 84 · ROI, ROAS y MER

> **Qué resuelve / cuándo usarlo** — Cómo medir si la plata que metiste a un negocio o a una campaña de pauta volvió con ganancia. Úsalo cuando alguien diga "tuve 4x de ROAS" o "el ROI fue del 200%" y necesites saber si eso de verdad significa que estás ganando dinero.

## Concepto (para no-experto)

Estas tres siglas miden lo mismo en esencia —**¿la inversión rindió?**— pero desde ángulos distintos. Confundirlas hace que un negocio crea que gana cuando en realidad pierde.

- **ROI** = *Return On Investment* (Retorno de la Inversión). Mide la **ganancia neta** respecto a lo que invertiste. Responde: "por cada peso que metí, ¿cuánto peso de **utilidad** me quedó?". Es la métrica más honesta porque ya descuenta costos.

- **ROAS** = *Return On Ad Spend* (Retorno de la Inversión Publicitaria). Mide los **ingresos** (ventas, no ganancia) que generó **una campaña específica** por cada peso de pauta. Responde: "por cada peso de publicidad, ¿cuántos pesos de **venta** entraron?". Es **ingreso bruto**, no ganancia: un ROAS alto puede igual estar perdiendo plata si el producto es caro de producir.

- **MER** = *Marketing Efficiency Ratio* (Razón de Eficiencia de Marketing), también llamado **blended ROAS** (ROAS mezclado). Es el ROAS pero a nivel de **todo el negocio**: ingresos totales ÷ gasto total de marketing (todas las plataformas juntas). Responde: "contando toda mi venta y toda mi publicidad, ¿qué tan eficiente soy?".

**Analogía cotidiana.** Imagina una venta de empanadas en un evento.
- El **ROAS** es como mirar solo el volante que pagaste: "pagué $10.000 en volantes y por esos volantes vendí $40.000" → ROAS 4. Suena genial.
- Pero el **ROI** mira la realidad completa: de esos $40.000, las empanadas te costaron $24.000 en harina y carne, y el volante $10.000. Ganancia real = $40.000 − $24.000 − $10.000 = $6.000. Sobre el volante de $10.000, eso es un ROI del 60%, no del 300%.
- El **MER** es cuando además pagaste perifoneo y un post en Instagram: sumas TODA la venta del día y la divides entre TODO lo que gastaste en promoción, sin importar de qué canal vino cada cliente.

**Término clave — atribución:** decidir a qué campaña "pertenece" una venta. El ROAS necesita atribución (saber qué venta vino de qué anuncio); el MER **no** la necesita, por eso muchos negocios confían más en el MER.

## Fórmulas / método

**ROI** (en proporción y en porcentaje):

```
ROI            = (Ganancia neta) / (Inversión)
ROI%           = ROI × 100

donde  Ganancia neta = Ingresos − Costos totales − Inversión
```

- *Ingresos* [unidad monetaria, p. ej. COP]: dinero que entró.
- *Costos totales* [COP]: costo de producir/entregar lo vendido (COGS), operación, etc.
- *Inversión* [COP]: el capital cuyo retorno mides (pauta, máquina, proyecto).
- *ROI* es **adimensional** (peso/peso); se expresa en % o como múltiplo.

**ROAS** (múltiplo y porcentaje):

```
ROAS  = (Ingresos atribuidos a la campaña) / (Gasto en pauta de esa campaña)
ROAS% = ROAS × 100
```

- *ROAS* es **adimensional** (COP de venta / COP de pauta). "ROAS 4" = "4x" = "400%".

**MER / blended ROAS:**

```
MER = (Ingresos totales del negocio) / (Gasto total de marketing)
```

**Del ROAS al beneficio real — el puente que casi nadie cruza.** El ROAS que apenas cubre costos se llama **ROAS de equilibrio** (break-even ROAS):

```
ROAS_equilibrio = 1 / Margen_de_contribución

donde  Margen_de_contribución = (Precio − Costo variable unitario) / Precio   [fracción 0–1]
```

Y la ganancia real que deja una campaña:

```
Ganancia_campaña = Ingresos × Margen_de_contribución − Gasto_pauta
```

Regla de oro: **un ROAS solo es bueno si supera el ROAS de equilibrio.** Si tu margen es 50% (0,5), necesitas ROAS ≥ 2 solo para no perder.

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28  # alta precisión; el dinero NUNCA con float

D = Decimal

def dinero(x):
    """Redondea a centavos UNA sola vez, al final."""
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

# --- Datos de una campaña real (en COP) ---
gasto_pauta   = D("500000")    # invertido en anuncios
ingresos_camp = D("2000000")   # ventas atribuidas a la campaña
precio        = D("50000")     # precio de venta unitario
costo_var_u   = D("20000")     # costo variable por unidad (COGS + envío)

# ROAS (múltiplo, adimensional)
roas = ingresos_camp / gasto_pauta
print("ROAS =", roas, "=>", roas * 100, "%")   # 4 => 400 %

# Margen de contribución (fracción)
margen = (precio - costo_var_u) / precio        # (50000-20000)/50000 = 0.6
print("Margen de contribución =", margen)        # 0.6  (60 %)

# ROAS de equilibrio
roas_eq = D(1) / margen
print("ROAS de equilibrio =", roas_eq)           # 1.666...

# Ganancia real de la campaña (en dinero, redondeo final)
ganancia = ingresos_camp * margen - gasto_pauta
print("Ganancia campaña =", dinero(ganancia), "COP")  # 700000.00

# ROI de la campaña (ganancia neta / inversión)
roi = ganancia / gasto_pauta
print("ROI =", roi, "=>", dinero(roi * 100), "%")     # 1.4 => 140 %
```

**Verificación por segunda vía** (reconstrucción inversa + asserts independientes):

```python
# Vía 2A: ¿el ROAS supera el de equilibrio? Si sí, la ganancia debe ser > 0.
assert (roas > roas_eq) == (ganancia > 0)

# Vía 2B: reconstruir ingresos desde ROAS y gasto (operación inversa)
assert roas * gasto_pauta == ingresos_camp        # 4 * 500000 = 2000000

# Vía 2C: calcular ganancia por unidades vendidas, otro método
unidades = ingresos_camp / precio                 # 2000000/50000 = 40 unidades
util_x_unidad = precio - costo_var_u              # 30000 por unidad
ganancia_v2 = util_x_unidad * unidades - gasto_pauta
assert ganancia_v2 == ganancia                    # 30000*40 - 500000 = 700000

# Vía 2D: relación exacta ROI = ROAS*margen - 1
assert roi == roas * margen - D(1)                # 4*0.6 - 1 = 1.4

# Sanity de orden de magnitud: 40 unidades * 30k margen ≈ 1.2M, menos 0.5M ≈ 0.7M ✓
print("Verificaciones OK")
```

La identidad **ROI = ROAS × margen − 1** es el puente exacto entre las dos métricas. Si la memorizas, nunca volverás a confundir "4x de ROAS" con "ganancia 4x".

## Ejemplo trabajado

**Caso GastroLatam (LatAm).** Campaña en Meta para vender la Calculadora de Costos Gastronómicos.

- Gasto en pauta: **$500.000 COP**
- Ventas atribuidas: **$2.000.000 COP** (40 unidades a $50.000)
- Costo variable por unidad: **$20.000 COP** (pasarela de pago + soporte + entrega digital)

Paso 1 — **ROAS**: 2.000.000 ÷ 500.000 = **4,0** (es decir, 400%). "Por cada peso de pauta entraron 4 pesos de venta."

Paso 2 — **Margen de contribución**: (50.000 − 20.000) ÷ 50.000 = 30.000/50.000 = **0,60** (60%).

Paso 3 — **ROAS de equilibrio**: 1 ÷ 0,60 = **1,667**. Necesitabas mínimo 1,667x para no perder. Tu 4,0 lo supera holgadamente. ✅

Paso 4 — **Ganancia real de la campaña**: 2.000.000 × 0,60 − 500.000 = 1.200.000 − 500.000 = **$700.000 COP**.

Paso 5 — **ROI**: 700.000 ÷ 500.000 = **1,40 = 140%**. Comprobado con la identidad: ROAS×margen − 1 = 4×0,6 − 1 = 1,4. ✅

**Lectura para Lushows:** el ROAS de 4 suena a "cuadrupliqué", pero la ganancia real fue 140% sobre lo invertido (que sigue siendo excelente). Si el costo variable hubiera sido $35.000 (margen 30%, ROAS de equilibrio 3,33), ese mismo ROAS de 4 dejaría ROI = 4×0,3 − 1 = **0,2 = 20%**: el mismo "4x" pasa de gran negocio a apenas decente.

## Errores comunes / trampas

- **Creer que ROAS = ganancia.** ROAS es ingreso bruto. Un ROAS de 5 con margen de 15% deja ROI = 5×0,15 − 1 = −0,25 → **pierdes 25%**. El ROAS alto puede ocultar pérdidas.
- **No restar el costo del producto.** El ROI debe descontar COGS y costos variables; si solo restas la pauta, inflas el resultado.
- **Doble conteo entre canales.** Sumar el ROAS atribuido de Meta + Google + TikTok suele dar más ventas que las reales (cada plataforma se cuelga la misma venta). Por eso existe el **MER**: usa la venta total verdadera.
- **Confundir múltiplo y porcentaje.** ROAS 4 = 400%, no 4%. ROI 1,4 = 140%, no 14%.
- **ROI sin horizonte de tiempo.** Un ROI de 50% en un mes ≠ 50% en tres años; al comparar inversiones, anualiza o fija el mismo período (ver valor del dinero en el tiempo).
- **Redondear a media calle.** Mantén precisión durante el cálculo y redondea a centavos **una sola vez** al final; con `float` aparecen centavos fantasma.
- **Olvidar costos fijos en decisiones de escala.** ROI/ROAS miran lo variable; para saber si el negocio entero gana, cruza con el punto de equilibrio.

## Cruces

- [[80-margenes-bruto-contribucion-neto]] — el margen de contribución es la pieza que convierte ROAS en ROI.
- [[83-cac-ltv-y-payback]] — ROAS mide la venta inmediata; CAC/LTV miden el valor del cliente a largo plazo.
- [[82-pricing-markup-margin-y-elasticidad]] — el precio fija el margen y por tanto el ROAS de equilibrio.
- [[76-punto-de-equilibrio]] — complementa el ROAS de equilibrio a nivel de todo el negocio.
- [[14-porcentajes-sin-errores]] — para no confundir múltiplo (4x) con porcentaje (400%).

---

**Mini-checklist de exactitud**
1. ¿Resté el costo del producto (no solo la pauta) antes de llamarlo "ganancia"? → si no, es ROAS, no ROI.
2. ¿El ROAS supera el ROAS de equilibrio (1/margen)? → confirma con `ganancia > 0`.
3. ¿Verifiqué con la identidad `ROI = ROAS × margen − 1` y un segundo método (por unidades)?
