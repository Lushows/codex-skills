# 87 · Métricas de crecimiento (MRR)

> **Qué resuelve / cuándo usarlo** — Mide cuánto dinero recurrente entra cada mes en un negocio de suscripción (software, membresías, planes) y a qué velocidad crece. Úsalo para reportar ingresos a inversionistas, fijar metas y diagnosticar salud (¿crezco sano o quemo plata?).

## Concepto (para no-experto)

Imagina que tienes un negocio donde los clientes te pagan **todos los meses** (Netflix, un gimnasio, un software por suscripción). No te interesa solo "cuánto vendí este mes una vez", sino **cuánto dinero recurrente tienes asegurado cada mes** mientras los clientes no se vayan. Eso es el **MRR**.

- **MRR (Monthly Recurring Revenue, ingreso recurrente mensual):** la suma de lo que te pagan **por mes** todos tus clientes activos. Si tienes 100 clientes pagando $50.000 COP/mes cada uno → MRR = $5.000.000 COP/mes. **Importante:** es dinero *normalizado a un mes*. Si alguien paga $600.000 al año, eso aporta $50.000 al MRR (600.000 ÷ 12), no $600.000.
- **ARR (Annual Recurring Revenue, ingreso recurrente anual):** el MRR proyectado a un año → `ARR = MRR × 12`. Es la "etiqueta de tamaño" del negocio.
- **Tasa de crecimiento:** qué tanto creció el MRR de un mes al siguiente, en porcentaje.
- **CMGR (Compound Monthly Growth Rate, tasa de crecimiento compuesto mensual):** el crecimiento *promedio por mes* a lo largo de varios meses, ya considerando el efecto bola de nieve (mes a mes crece sobre lo ya crecido).
- **NRR (Net Revenue Retention, retención neta de ingresos):** de los clientes que ya tenías hace un año, ¿cuánto dinero te siguen dando hoy, contando que algunos subieron de plan, otros bajaron y otros se fueron? Si es mayor a 100%, ¡tus clientes viejos te dan MÁS plata que antes sin necesidad de clientes nuevos!
- **Regla del 40:** un atajo para saber si un SaaS está sano: `crecimiento (%) + margen de ganancia (%) ≥ 40`. Permite cambiar velocidad por rentabilidad.

**Analogía cotidiana:** el MRR es como el sueldo mensual *garantizado* de tu negocio. El ARR es ese sueldo "anualizado" para presumirlo. El NRR mide si tus clientes antiguos, como una huerta, dan más fruta cada temporada (NRR > 100%) o se van secando (NRR < 100%).

## Fórmulas / método

Símbolos y unidades:

- `MRR` = ingreso recurrente mensual **[COP/mes]** (o cualquier moneda).
- `ARR = MRR × 12` **[COP/año]**.
- Componentes del cambio de MRR de un mes:
  - `New` = MRR de clientes nuevos.
  - `Expansion` = aumento de MRR de clientes existentes (subieron de plan, add-ons).
  - `Contraction` = reducción de MRR de existentes (bajaron de plan).
  - `Churned` = MRR perdido por clientes que cancelaron.
  - **Net New MRR** `= New + Expansion − Contraction − Churned` **[COP/mes]**.

Tasa de crecimiento mes a mes (MoM):

```
growth = (MRR_t − MRR_{t-1}) / MRR_{t-1}        [adimensional → ×100 para %]
```

Crecimiento compuesto mensual (CMGR), entre un valor inicial `MRR_0` y uno final `MRR_n` separados por `n` meses:

```
CMGR = (MRR_n / MRR_0)^(1/n) − 1                [por mes]
```

Net Revenue Retention (ventana típica: 12 meses), partiendo del MRR de una cohorte hace 12 meses (`MRR_base`):

```
NRR = (MRR_base + Expansion − Contraction − Churned) / MRR_base   [×100 → %]
```

(Ojo: NRR **no** incluye clientes nuevos; solo mide qué pasó con los que ya tenías. Si incluyes nuevos es GRR/“Gross” → distinto.)

Regla del 40:

```
Rule40 = growth_anual(%) + margen(%)            (margen = EBITDA % o FCF %)
sano si  Rule40 ≥ 40
```

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28  # alta precisión interna; redondeamos UNA vez al final

# ---- Datos de ejemplo (COP/mes) ----
mrr_prev   = Decimal("12000000")   # MRR del mes pasado
new        = Decimal("1500000")    # nuevos
expansion  = Decimal("400000")     # upgrades de existentes
contraction= Decimal("150000")     # downgrades de existentes
churned    = Decimal("600000")     # cancelaciones

# ---- Net New MRR y MRR actual ----
net_new = new + expansion - contraction - churned
mrr_now = mrr_prev + net_new
print("Net New MRR:", net_new, "COP/mes")
print("MRR actual :", mrr_now, "COP/mes")

# ---- ARR ----
arr = mrr_now * 12
print("ARR        :", arr, "COP/año")

# ---- Tasa de crecimiento MoM ----
growth = (mrr_now - mrr_prev) / mrr_prev
print("Growth MoM :", (growth * 100).quantize(Decimal("0.01"), ROUND_HALF_UP), "%")

# ---- CMGR sobre varios meses ----
# Serie real de MRR a lo largo de 6 meses (n = 5 saltos)
serie = [Decimal(x) for x in
         ["10000000","10800000","11700000","12500000","13400000","14500000"]]
n = len(serie) - 1
ratio = serie[-1] / serie[0]
cmgr = ratio ** (Decimal(1) / Decimal(n)) - 1   # Decimal soporta ** con Decimal
print("CMGR/mes   :", (cmgr * 100).quantize(Decimal("0.01"), ROUND_HALF_UP), "%")

# ---- NRR a 12 meses (cohorte) ----
mrr_base = Decimal("8000000")
exp_y    = Decimal("1200000")
con_y    = Decimal("300000")
chu_y    = Decimal("900000")
nrr = (mrr_base + exp_y - con_y - chu_y) / mrr_base
print("NRR 12m    :", (nrr * 100).quantize(Decimal("0.01"), ROUND_HALF_UP), "%")
```

**Verificación por segunda vía (operación inversa + reconstrucción de la serie):**

```python
# (1) Inversa del MoM: a partir de growth, reconstruir mrr_now y comparar.
mrr_now_check = mrr_prev * (1 + growth)
assert mrr_now_check == mrr_now, "MoM inverso no cuadra"

# (2) CMGR: si aplico el crecimiento compuesto n veces sobre el inicio,
#     debo recuperar el valor final (dentro de tolerancia de redondeo).
reconstruido = serie[0] * (1 + cmgr) ** n
dif = abs(reconstruido - serie[-1])
assert dif < Decimal("0.01"), f"CMGR no reconstruye el final, dif={dif}"

# (3) Sanity de orden de magnitud del CMGR:
#     la serie va de 10M a 14.5M en 5 meses ≈ +45% total → ~7.7%/mes.
#     Debe caer en un rango razonable 6%–9%.
assert Decimal("0.06") < cmgr < Decimal("0.09"), "CMGR fuera de rango esperado"

# (4) ARR consistente con MRR.
assert arr == mrr_now * 12
print("OK: todas las verificaciones pasaron")
```

**Por qué `decimal` y no `float`:** con dinero, `float` arrastra errores binarios (0.1 + 0.2 ≠ 0.3). Para sumar/restar millones de pesos y comparar con `assert`, `Decimal` da igualdad exacta. El exponente fraccionario del CMGR sí es irracional, por eso ahí redondeamos al final y comparamos con tolerancia, no con `==`.

## Ejemplo trabajado

**Caso (LatAm):** un SaaS colombiano de facturación para pymes.

- MRR mes pasado: **$12.000.000 COP/mes**.
- Este mes: nuevos $1.500.000, expansión $400.000, contracción $150.000, churn $600.000.

Paso 1 — **Net New MRR**:
`1.500.000 + 400.000 − 150.000 − 600.000 = $1.150.000 COP/mes`.

Paso 2 — **MRR actual**:
`12.000.000 + 1.150.000 = $13.150.000 COP/mes`.

Paso 3 — **ARR**:
`13.150.000 × 12 = $157.800.000 COP/año`.

Paso 4 — **Crecimiento MoM**:
`1.150.000 / 12.000.000 = 0,095833… → 9,58 %` mensual.

Paso 5 — **CMGR** (serie de 6 meses, 10M → 14,5M, n=5):
`(14.500.000 / 10.000.000)^(1/5) − 1 = 1,45^0,2 − 1 = 0,07714… → 7,71 %/mes`.
Verificado: `10.000.000 × 1,07714^5 = 14.500.000` ✓.

Paso 6 — **NRR a 12 meses** (cohorte base $8.000.000):
`(8.000.000 + 1.200.000 − 300.000 − 900.000) / 8.000.000 = 8.000.000 / 8.000.000 = 100,00 %`.
Interpretación: los clientes viejos hoy te dan exactamente lo mismo que hace un año (la expansión compensó churn + contracción). Está en el filo: arriba de 100% sería excelente.

Paso 7 — **Regla del 40** (si el crecimiento *anual* fuera ~+60% y el margen FCF −15%):
`60 + (−15) = 45 ≥ 40 → sano` (crece tan rápido que se le perdona quemar caja).

**Resultados con unidades:** Net New = **$1.150.000 COP/mes**, MRR = **$13.150.000 COP/mes**, ARR = **$157.800.000 COP/año**, MoM = **9,58 %**, CMGR = **7,71 %/mes**, NRR = **100,00 %**.

## Errores comunes / trampas

- **Confundir ingreso recurrente con ingreso total.** Una venta única (setup, consultoría, hardware) **NO** va al MRR. Solo lo que se repite cada mes.
- **No normalizar planes anuales.** Un cliente que paga $600.000/año aporta **$50.000** al MRR, no $600.000. Quien mete el pago completo infla el MRR 12×.
- **Promediar tasas en vez de componer.** El crecimiento promedio NO es el promedio aritmético de los % mensuales; es el **CMGR** (media geométrica). El promedio simple casi siempre exagera.
- **Mezclar NRR con GRR.** NRR incluye expansión (puede superar 100%); GRR (Gross Retention) nunca pasa de 100% porque ignora upgrades. No los confundas al reportar.
- **Meter clientes nuevos en el NRR.** El NRR mide SOLO la cohorte vieja. Si sumas nuevos, ya no estás midiendo retención.
- **Doble conteo de moneda.** Si mezclas clientes en COP y USD, convierte todo a una sola moneda a una tasa fija antes de sumar; ver [[79-moneda-inflacion-y-devaluacion]].
- **Regla del 40 con la métrica de margen equivocada.** Define si usas EBITDA% o FCF% y mantenlo constante; cambiarlo entre periodos hace el número incomparable.

## Cruces

- [[85-cohortes-retencion-y-churn]] — el churn y la retención que alimentan el NRR.
- [[83-cac-ltv-y-payback]] — cuánto cuesta y cuánto vale cada cliente recurrente.
- [[86-forecasting-y-proyeccion]] — proyectar el MRR futuro con el CMGR.
- [[71-interes-simple-y-compuesto]] — la matemática de la composición detrás del CMGR.
- [[89-trampas-de-metricas-y-dashboards]] — cómo NO inflar ni engañar con estas métricas.

---

**Mini-checklist de exactitud**
- [ ] Todo monto del MRR está **normalizado a un mes** y en **una sola moneda**; las ventas únicas quedan fuera.
- [ ] El crecimiento multi-mes se calculó con **CMGR (media geométrica)** y se reconstruyó la serie (`MRR_0·(1+CMGR)^n = MRR_n`).
- [ ] NRR usa SOLO la cohorte base (sin clientes nuevos) y se aclaró si el número es NRR o GRR.
