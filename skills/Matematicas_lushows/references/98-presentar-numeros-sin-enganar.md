# 98 · Presentar números sin engañar

> **Qué resuelve / cuándo usarlo** — Cómo comunicar un número correcto sin que el formato, el gráfico o el redondeo cuenten una mentira. Úsalo cada vez que un cálculo exacto vaya a un dashboard, una presentación, un reporte a un cliente o una decisión de dinero.

## Concepto (para no-experto)

Tener el número **exacto** es solo la mitad del trabajo. La otra mitad es **comunicarlo sin engañar** — ni a otros ni a ti mismo. Un número 100% correcto puede mentir si lo presentas mal.

Términos clave (definidos la primera vez):

- **Base de comparación (baseline)**: el número contra el cual se mide el cambio. "Subimos 50%" no significa nada si no dices "respecto a qué". 50% de 1 venta es 0.5 ventas; 50% de 1.000 es 500.
- **Punto porcentual (pp)** vs **porcentaje (%)**: si una tasa pasa de 4% a 6%, subió **2 puntos porcentuales** (6−4), pero **50% en términos relativos** (2/4). Confundirlos es la mentira numérica más común de LatAm en marketing y finanzas.
- **Eje truncado**: un gráfico cuyo eje vertical NO empieza en cero. Hace que una diferencia pequeña parezca enorme. Es la trampa visual #1.
- **Cherry-picking de fechas**: elegir el punto de inicio/fin que más favorece tu narrativa (ej. medir crecimiento desde el peor mes).
- **Incertidumbre**: cuánto podría variar el número si repitiéramos la medición. Un número sin su margen es una opinión disfrazada de hecho.

Analogía cotidiana: es como una balanza de cocina. La balanza puede estar perfectamente calibrada (número exacto), pero si la pones encima de una mesa inclinada (eje truncado) o pesas solo el ingrediente que te conviene (cherry-picking), el resultado "real" engaña. Presentar bien = poner la balanza en piso plano y mostrar todo lo que pesaste.

**Regla de oro:** *un número honesto siempre lleva consigo su base, su unidad y su incertidumbre.*

## Fórmulas / método

**1. Cambio absoluto vs relativo** (de un valor `v0` a `v1`):

```
Cambio absoluto   = v1 − v0                 [misma unidad que v]
Cambio relativo   = (v1 − v0) / v0          [adimensional → ×100 para %]
```

**2. Puntos porcentuales vs cambio relativo** (cuando v ya es un porcentaje, ej. tasa de conversión `p0`, `p1`):

```
Δ en puntos porcentuales (pp) = p1 − p0
Δ relativo (%)                = (p1 − p0) / p0 × 100
```

**3. Regla del eje honesto** (gráfico de barras): el eje vertical **debe** incluir el cero. La "exageración visual" se cuantifica:

```
factor_engaño = (rango_real_de_datos) / (rango_mostrado_en_eje)
```
Si `factor_engaño > 1`, el gráfico amplifica diferencias. Para barras, el eje debe empezar en 0 (factor = 1 respecto al origen).

**4. Redondeo comunicado** — siempre indicar la dirección y la regla:

```
valor_mostrado = round_half_even(valor_exacto, n)   # banker's rounding
error_de_redondeo = |valor_exacto − valor_mostrado|
```
Ver [[05-cifras-significativas-y-redondeo.md]]. Regla dura de esta skill: **redondear UNA sola vez, al final.**

**5. Incertidumbre visible** — reportar como `estimación ± margen [unidad]` o como intervalo `[bajo, alto]`. Ver [[66-intervalos-de-confianza.md]].

## Verificación en código

Ejemplo real: un dashboard de GastroLatam afirma *"la conversión subió 50%"*. La tasa pasó de 4% a 6%. ¿Es honesto decir 50%? Calculemos ambas lecturas con exactitud (dinero/tasas con `Decimal`, nunca `float`).

```python
from decimal import Decimal, ROUND_HALF_EVEN, getcontext
getcontext().prec = 28

# Tasas de conversión observadas (proporciones exactas, NO float)
p0 = Decimal("0.04")   # 4.00%  -> base de comparación
p1 = Decimal("0.06")   # 6.00%

# Las dos lecturas legítimas del MISMO hecho
delta_pp  = (p1 - p0) * Decimal("100")              # puntos porcentuales
delta_rel = (p1 - p0) / p0 * Decimal("100")         # cambio relativo (%)

# Redondeo comunicado: UNA vez, al final, banker's rounding, 2 decimales
def fmt(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

print(f"De {p0*100}% a {p1*100}%")
print(f"  -> subió {fmt(delta_pp)} puntos porcentuales (pp)")
print(f"  -> subió {fmt(delta_rel)} % en términos relativos")
# Honesto: "subió 2 pp (de 4% a 6%), un +50% relativo"
# Engañoso: "subió 50%" sin contexto -> el lector cree 50 pp
```

Salida:
```
De 4.00% a 6.00%
  -> subió 2.00 puntos porcentuales (pp)
  -> subió 50.00 % en términos relativos
```

**Verificación por segunda vía** (reconstrucción inversa + assert de consistencia):

```python
# Vía inversa: si parto de p0 y aplico cada lectura, debo recuperar p1
# 1) Aplicando los puntos porcentuales:
p1_desde_pp  = p0 + delta_pp / Decimal("100")
# 2) Aplicando el cambio relativo:
p1_desde_rel = p0 * (Decimal("1") + delta_rel / Decimal("100"))

assert p1_desde_pp  == p1, "La lectura en pp no reconstruye p1"
assert p1_desde_rel == p1, "La lectura relativa no reconstruye p1"

# Sanity check de orden de magnitud: 50% relativo NO puede ser 50 pp
assert delta_rel != delta_pp, "pp y % relativo NO deben coincidir aqui"
assert delta_pp < delta_rel, "con base<100% el cambio relativo es mayor"
print("OK: ambas lecturas reconstruyen 6.00% y son distintas (2pp vs 50%)")
```

Las dos vías reconstruyen exactamente `p1 = 6%`, confirmando que **ambos números (2 pp y 50%) son correctos**; el engaño nace solo de cuál muestras y cómo lo etiquetas.

## Ejemplo trabajado

**Caso:** GastroLatam vende la Calculadora de Costos a $10.000 COP. En enero vendió 80 unidades; en febrero, 120. Marketing quiere poner en el reporte: *"¡Las ventas se dispararon!"* con un gráfico de barras cuyo eje va de 75 a 125.

Paso 1 — Cambio real, con unidades:
- Absoluto: 120 − 80 = **40 unidades**.
- Relativo: 40 / 80 = 0,50 = **+50%**.
- Ingreso: 40 × $10.000 = **$400.000 COP** adicionales (verificable: 120×10.000 − 80×10.000 = 1.200.000 − 800.000 = 400.000 ✓).

Paso 2 — Auditar el gráfico. Eje propuesto: 75 a 125 (rango mostrado = 50 unidades). Datos reales van de 80 a 120 (rango = 40). Con barras truncadas en 75, la barra de febrero (120−75 = 45 de alto) parece **9 veces** la de enero (80−75 = 5 de alto), cuando en realidad es solo **1,5 veces**. Eso es mentira visual.

Paso 3 — Versión honesta:
- Texto: *"Ventas: 80 → 120 unidades (+40 uds, +50%). Ingreso adicional: $400.000 COP."*
- Gráfico de barras con **eje desde 0**: la barra de feb (120) es exactamente 1,5× la de ene (80). Real y verificable.
- Si hay incertidumbre (ej. 5 ventas de febrero aún sin confirmar pago): reportar **120 confirmadas, +5 pendientes**, no inflar a 125.

Resultado: el mismo número exacto (+50%, +$400.000 COP) comunicado sin distorsión. La cifra impresiona sola; no necesita el truco del eje.

## Errores comunes / trampas

- **Confundir pp con %**: "el IVA subió 3%" cuando pasó de 16% a 19% (eso son 3 **pp**, o +18,75% relativo). Siempre etiquetar la unidad del cambio.
- **Eje truncado en barras**: nunca empieces un gráfico de barras fuera de cero. (En líneas de series temporales a veces se justifica, pero hay que avisarlo.)
- **Redondear varias veces**: redondear cada paso intermedio acumula error. Redondea solo al mostrar. Ver [[05-cifras-significativas-y-redondeo.md]].
- **Falsa precisión**: reportar "$12.347,8923 COP" cuando los datos solo soportan miles. Las cifras significativas deben reflejar la calidad del dato.
- **Promedio que esconde la dispersión**: "ticket promedio $25.000" puede ocultar que el 80% paga $10.000 y unos pocos $200.000. Acompaña con mediana y rango. Ver [[60-estadistica-descriptiva.md]] y [[61-medidas-de-dispersion.md]].
- **Cherry-picking de fechas / base**: medir crecimiento desde el peor mes. Fija la base por una razón objetiva, no por conveniencia.
- **Número sin incertidumbre**: dar un forecast como cifra única sin rango. Ver [[86-forecasting-y-proyeccion.md]].
- **Porcentaje sin base**: "+300% de clics" puede ser de 1 a 4 clics. Muestra siempre los absolutos junto al porcentaje.
- **Ratio invertido**: presentar el inverso que conviene (margen sobre costo vs sobre precio). Define la fórmula. Ver [[82-pricing-markup-margin-y-elasticidad.md]].

## Cruces

- [[05-cifras-significativas-y-redondeo.md]] — cuánta precisión mostrar y cómo redondear una sola vez.
- [[14-porcentajes-sin-errores.md]] — base de los porcentajes, pp vs relativo.
- [[69-estadistica-enganosa.md]] — catálogo de gráficos y estadísticas tramposas.
- [[62-distribucion-de-datos-y-visualizacion.md]] — cómo graficar sin distorsionar.
- [[89-trampas-de-metricas-y-dashboards.md]] — métricas vanidosas y cómo no mentir en un dashboard.

---

**Mini-checklist de exactitud (antes de publicar un número):**
1. ¿El número lleva su **unidad**, su **base de comparación** y (si aplica) su **margen de incertidumbre**?
2. ¿El **gráfico de barras** empieza en cero y no exagera diferencias?
3. ¿Redondeé **una sola vez**, al final, y comuniqué la regla (ej. "redondeado a miles de COP")?
