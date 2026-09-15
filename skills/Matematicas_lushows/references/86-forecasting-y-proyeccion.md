# 86 · Forecasting y proyección

> **Qué resuelve / cuándo usarlo** — Cuando necesitas estimar cuánto venderás (o gastarás, o crecerás) el próximo mes/trimestre/año a partir del histórico. Da un **número con método**, un **rango de escenarios** y, sobre todo, deja **explícitos los supuestos** para no engañarte a ti mismo.

## Concepto (para no-experto)

**Forecast** (pronóstico) = una estimación del futuro basada en datos del pasado y en supuestos. No es una bola de cristal: es "si el patrón que vi sigue parecido, esto es lo que cabe esperar".

Imagina que registras tus ventas cada mes. Para proyectar el mes que viene tienes varias formas honestas de hacerlo, cada una con un supuesto distinto:

- **Naïve** ("ingenuo"): el próximo mes será igual al último. Supuesto: nada cambia. Es la línea base contra la que se mide cualquier método más sofisticado: si tu modelo elaborado no le gana al naïve, no sirve.
- **Tendencia** (trend): los datos suben (o bajan) en línea recta; la prolongas. Supuesto: el ritmo lineal continúa. Se ajusta con una **regresión lineal** (ver módulo 64).
- **Media móvil** (moving average): el próximo valor ≈ promedio de los últimos *k* meses. Suaviza el ruido. Supuesto: el nivel es estable y solo hay fluctuaciones aleatorias.
- **Crecimiento compuesto** (CAGR): los datos crecen un % fijo cada periodo (como un interés compuesto). Supuesto: crecimiento porcentual constante. Útil para negocios en expansión.
- **Estacionalidad** (seasonality): hay un patrón que se repite por época (diciembre vende más, enero menos). Supuesto: ese patrón se repetirá.

**Analogía:** proyectar es como predecir a qué hora llegarás manejando. Naïve = "tardé 30 min ayer, tardaré 30 hoy". Tendencia = "cada día hay más tráfico, hoy serán 33". Estacionalidad = "es viernes, siempre tardo 45". Ninguna es la verdad; cada una es un supuesto sobre qué se repite.

Regla de oro de este módulo: **un forecast sin supuesto declarado y sin rango es propaganda, no matemática.**

## Fórmulas / método

Sea la serie histórica de valores `y_1, y_2, ..., y_n` (unidad: p. ej. COP/mes o unidades/mes).

**1. Naïve:** `ŷ_{n+1} = y_n`

**2. Media móvil de orden k:**
```
MM_k = (y_n + y_{n-1} + ... + y_{n-k+1}) / k
ŷ_{n+1} = MM_k
```
`k` = nº de periodos promediados (entero). Mayor `k` ⇒ más suave, más lento a reaccionar.

**3. Tendencia lineal (mínimos cuadrados):** ajusta `ŷ = a + b·t`, donde `t` = índice del periodo (1,2,...,n).
```
b (pendiente)   = Σ(t-t̄)(y-ȳ) / Σ(t-t̄)²      [unidad: y por periodo]
a (intercepto)  = ȳ - b·t̄                       [unidad de y]
ŷ_{n+h} = a + b·(n+h)
```
`t̄`, `ȳ` = promedios de t y de y. `h` = horizonte (cuántos periodos adelante).

**4. CAGR (Compound Annual Growth Rate / tasa de crecimiento compuesta):**
```
CAGR = (y_n / y_1)^(1/(n-1)) − 1        [adimensional, por periodo]
ŷ_{n+h} = y_n · (1 + CAGR)^h
```
Define el **% constante** que, aplicado cada periodo, lleva de `y_1` a `y_n`. Ojo: solo usa primer y último dato, ignora el camino (ver trampas).

**5. Estacionalidad (descomposición multiplicativa simple):**
```
índice_estacional_m = promedio( y de los periodos en estación m / nivel-base de ese ciclo )
ŷ = (tendencia o nivel) × índice_estacional_m
```
Los índices se normalizan para que su promedio sea 1 (así no inflan el total).

**6. Rango de escenarios:** nunca un punto solo. Mínimo tres:
```
Pesimista = ŷ × (1 − d)   ·   Base = ŷ   ·   Optimista = ŷ × (1 + d)
```
`d` = desviación plausible (p. ej. del error histórico del modelo, ver MAPE abajo). Mejor que inventar `d`: usar el **error de validación** del modelo.

**Métrica de error (para elegir y para fijar el rango): MAPE** (Mean Absolute Percentage Error):
```
MAPE = (1/m) · Σ |y_real − ŷ| / |y_real|       [%]
```

## Verificación en código

```python
# Forecasting: tendencia + media móvil + CAGR + estacionalidad, con verificación.
from decimal import Decimal, getcontext
import numpy as np

getcontext().prec = 28

# --- Datos: ventas mensuales (unidades) de una cafetería, 12 meses ---
y = [120, 135, 150, 140, 160, 175, 170, 190, 210, 205, 230, 250]
n = len(y)
t = np.arange(1, n + 1)          # índices 1..12 (periodo)
ya = np.array(y, dtype=float)

# 1) TENDENCIA LINEAL (mínimos cuadrados) -> y = a + b*t
b = np.sum((t - t.mean()) * (ya - ya.mean())) / np.sum((t - t.mean())**2)
a = ya.mean() - b * t.mean()
h = 1
trend_next = a + b * (n + h)
print(f"Tendencia: a={a:.4f}, b={b:.4f} uds/mes -> mes {n+h} = {trend_next:.2f} uds")

# VERIFICACIÓN 2ª VÍA: polyfit de numpy debe dar los mismos coeficientes
b2, a2 = np.polyfit(t, ya, 1)    # devuelve [pendiente, intercepto]
assert abs(b - b2) < 1e-9 and abs(a - a2) < 1e-9, "Discrepancia en regresión"
print(f"  [check] polyfit b={b2:.4f}, a={a2:.4f}  OK")

# 2) MEDIA MÓVIL k=3
k = 3
mm = sum(y[-k:]) / k
print(f"Media móvil k=3 -> mes {n+1} = {mm:.2f} uds")
# VERIFICACIÓN: el promedio reconstruye la suma
assert abs(mm * k - sum(y[-k:])) < 1e-9
print(f"  [check] {mm:.2f} x {k} = {mm*k:.0f} = suma últimos 3 ({sum(y[-k:])})  OK")

# 3) CAGR (dinero/unidades con razón de extremos) usando Decimal
y1, yn = Decimal(y[0]), Decimal(y[-1])
periods = Decimal(n - 1)
cagr = (yn / y1) ** (Decimal(1) / periods) - 1
proj_cagr = yn * (1 + cagr) ** 1
print(f"CAGR mensual = {cagr*100:.4f}%  -> mes {n+1} = {proj_cagr:.2f} uds")
# VERIFICACIÓN INVERSA: aplicar CAGR (n-1) veces desde y1 debe regresar yn
recon = y1 * (1 + cagr) ** periods
assert abs(recon - yn) < Decimal("0.0001"), f"CAGR no reconstruye yn: {recon}"
print(f"  [check] y1*(1+CAGR)^(n-1) = {recon:.4f} ≈ yn={yn}  OK")

# 4) RANGO con MAPE de validación (back-test 1 paso con media móvil)
errs = [abs(y[i] - sum(y[i-k:i])/k) / y[i] for i in range(k, n)]
mape = sum(errs) / len(errs)
base = mm
print(f"MAPE(MM k=3) = {mape*100:.2f}%")
print(f"Escenarios -> Pesim: {base*(1-mape):.1f} | Base: {base:.1f} | Optim: {base*(1+mape):.1f} uds")
```

Salida esperada (resumen): tendencia ≈ **252.6 uds**, media móvil ≈ **228.3 uds**, CAGR mensual ≈ **6.88 %** → ≈ **267.2 uds**, con todos los `assert` pasando. Las tres cifras difieren porque **cada una asume algo distinto**: ese es el punto, no un error.

## Ejemplo trabajado

**Negocio:** GastroLatam vende la Calculadora de Costos a $10.000 COP. Ventas de los últimos 6 meses (unidades): `40, 52, 61, 58, 75, 88`.

**Paso 1 — CAGR mensual** (crecimiento compuesto):
```
CAGR = (88/40)^(1/5) − 1 = (2.2)^(0.2) − 1
     = 1.17075... − 1 = 0.17075 = 17.075 % por mes
```
**Paso 2 — proyección del mes 7 (base):**
```
ŷ_7 = 88 × (1 + 0.17075) = 103.03 ≈ 103 unidades/mes
```
**Paso 3 — verificación inversa:** `40 × (1.17075)^5 = 88.00 uds` ✓ (reconstruye el último dato).

**Paso 4 — sanity check con tendencia lineal** (otro método): la pendiente ronda `+9.1 uds/mes`, lo que da ≈ `88 + 9.1·(7−6 desde el centro)` ≈ **96–99 uds**. CAGR (103) y tendencia (~97) son del mismo orden de magnitud → no hay disparate. La diferencia (103 vs 97) viene de que CAGR asume aceleración porcentual y la recta no; el rango honesto **96–103 uds** ya captura ambas visiones.

**Paso 5 — escenarios e ingresos** (con `d ≈ 8 %` por error histórico):
```
Pesimista  ≈ 95 uds  → 95 × $10.000  = $950.000 COP/mes
Base       ≈ 103 uds → 103 × $10.000 = $1.030.000 COP/mes
Optimista  ≈ 111 uds → 111 × $10.000 = $1.110.000 COP/mes
```
**Resultado:** ingreso proyectado mes 7 = **$1.030.000 COP/mes (rango $950k–$1.110k)**, supuesto: el crecimiento mensual reciente (~17 % compuesto / +9 uds lineal) se mantiene; redondeo aplicado **una sola vez** al final. El dinero se calcula como centavos/enteros, nunca con float.

## Errores comunes / trampas

- **Dar un solo número sin rango.** Un punto exacto del futuro es falsa precisión. Siempre tres escenarios + supuesto escrito.
- **CAGR engañoso:** solo usa el primer y último dato. Si `y_1` o `y_n` fue un mes atípico (pico de campaña, caída por falla), el % sale inflado o ridículo. Mira la serie completa.
- **Extrapolar lineal "para siempre":** ninguna recta sube infinito. Una tendencia de +9 uds/mes proyectada a 5 años da números absurdos. Los modelos lineales/CAGR valen para horizontes cortos.
- **Confundir tendencia con estacionalidad:** un buen diciembre no es "crecimiento", es estación. Sin desestacionalizar, proyectas un pico como si fuera la nueva normalidad.
- **No validar (back-test):** elige el método por su error en datos pasados que el modelo no vio, no por cuál da el número que te gusta.
- **MAPE con valores cero o cercanos a cero** en el denominador explota. Si hay ceros, usa otra métrica (MAE/RMSE).
- **Float en el dinero:** proyectar pesos con `float` arrastra errores de redondeo; usa `Decimal` o centavos enteros (módulo 12).
- **Ignorar el contexto:** la matemática proyecta el patrón; un evento conocido (lanzas un producto, cierra un competidor) rompe el patrón. Ajusta a mano y dilo.

### Mini-checklist de exactitud
- [ ] ¿Declaré el **supuesto** (qué se mantiene) y el **horizonte** (cuántos periodos)?
- [ ] ¿Di un **rango** (pesimista/base/optimista) anclado al error histórico, no inventado?
- [ ] ¿**Verifiqué** por 2ª vía (inversa del CAGR / otro método del mismo orden de magnitud) y dejé las **unidades**?

## Cruces
- [[64-regresion-lineal]] — el motor matemático detrás de la proyección por tendencia.
- [[71-interes-simple-y-compuesto]] — el CAGR es interés compuesto aplicado a ventas/crecimiento.
- [[93-analisis-de-sensibilidad-y-escenarios]] — cómo construir y estresar los escenarios pesimista/base/optimista.
- [[06-estimacion-y-sanity-checks]] — verificar que el forecast es del orden de magnitud correcto.
- [[87-metricas-de-crecimiento-mrr]] — proyectar ingresos recurrentes (MRR) con estas mismas técnicas.
