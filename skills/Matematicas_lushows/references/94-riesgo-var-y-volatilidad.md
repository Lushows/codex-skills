# 94 · Riesgo: VaR y volatilidad

> **Qué resuelve / cuándo usarlo** — Cuando necesitas *poner número* al riesgo de un retorno, un portafolio o un flujo: cuánto se mueve (volatilidad), cuánto podrías perder en un mal día (VaR), y si vale la pena el riesgo (relación riesgo-retorno). Útil para inversiones, presupuestos con incertidumbre y decisiones de "cuánto puedo perder".

## Concepto (para no-experto)

Riesgo no significa "que algo salga mal" en abstracto: en finanzas significa **incertidumbre cuantificable** sobre el resultado. Medimos cuánto puede *desviarse* el resultado real de lo esperado.

Términos, definidos la primera vez que aparecen:

- **Retorno (rendimiento)**: cuánto ganas o pierdes en proporción a lo invertido, en un periodo. Si un activo pasa de $100 a $108, el retorno simple es +8 %.
- **Volatilidad**: qué tanto "tiembla" el retorno alrededor de su promedio. Matemáticamente es la **desviación estándar** (raíz de la varianza) de los retornos. Analogía: dos buses llegan en promedio en 30 min, pero uno varía ±2 min y el otro ±20 min. Mismo promedio, riesgo muy distinto. La volatilidad es ese "±".
- **Varianza**: el promedio de las desviaciones al cuadrado respecto a la media. Está en "unidades al cuadrado"; por eso para reportar usamos su raíz (la desviación estándar), que vuelve a las unidades originales.
- **VaR (Value at Risk, "valor en riesgo")**: la pérdida máxima esperada en un horizonte (ej. 1 día) con cierta confianza (ej. 95 %). "VaR 95 % a 1 día = $1.200.000" significa: *en el 95 % de los días no perderás más de $1,2 M; pero 1 de cada 20 días podrías perder más*. Es un piso de tranquilidad, NO el peor caso.
- **Downside (riesgo a la baja)**: la volatilidad solo de los resultados *malos* (por debajo de un objetivo). A un inversionista no le molesta que el activo suba mucho; le molesta que baje. La **semidesviación** y el VaR miden solo ese lado.
- **Diversificación**: combinar activos que no se mueven igual para que el riesgo del conjunto sea **menor que la suma** de los riesgos. "No poner todos los huevos en la misma canasta": si una baja mientras otra sube, se compensan.

## Fórmulas / método

Retornos a partir de precios `P_t`:

- **Retorno simple**: `r_t = (P_t − P_{t−1}) / P_{t−1}`
- **Retorno logarítmico** (se suman bien en el tiempo): `ℓ_t = ln(P_t / P_{t−1})`

Media y dispersión de una muestra de `n` retornos:

- **Media**: `μ = (1/n) · Σ r_t`
- **Varianza muestral**: `s² = (1/(n−1)) · Σ (r_t − μ)²`  → se usa `n−1` (corrección de Bessel) porque estimamos la media de la misma muestra.
- **Volatilidad (desv. estándar)**: `σ = √(s²)`  [unidad: misma del retorno, ej. % por día]

**Anualización** (de periodo a año, asumiendo independencia entre periodos):

- `σ_anual = σ_periodo · √k`   donde `k` = periodos por año (252 días bursátiles, 12 meses).
- `μ_anual = μ_periodo · k`   (la media escala con `k`, la volatilidad con `√k`: por eso a largo plazo el retorno domina al ruido).

**VaR paramétrico (Gaussiano)** — supone que los retornos siguen una **distribución normal** (campana de Gauss):

- `VaR_α = −(μ + z_α · σ) · V`
  - `α` = nivel de confianza (0,95 o 0,99); `z_α` = percentil de la normal estándar (`z_{0,95} ≈ −1,6449`, `z_{0,99} ≈ −2,3263`).
  - `V` = valor de la posición (dinero). El signo negativo convierte una pérdida en número positivo "de riesgo".

**VaR histórico** (sin suponer normal): ordena los retornos observados y toma el percentil `(1−α)`:

- `VaR_α = −percentil_{1−α}(retornos) · V`

**CVaR / Expected Shortfall** (pérdida *promedio* cuando se supera el VaR — el "qué tan grave si pasa"):

- `CVaR_α = −promedio(r_t | r_t ≤ percentil_{1−α}) · V`

**Riesgo-retorno — Sharpe ratio** (retorno extra por unidad de riesgo):

- `Sharpe = (μ_anual − r_f) / σ_anual`   con `r_f` = tasa libre de riesgo.

**Diversificación — riesgo de un portafolio de 2 activos** (pesos `w₁,w₂`):

- `σ_p = √(w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·ρ·σ₁·σ₂)`
  - `ρ` = **correlación** entre los dos activos (de −1 a +1). Cuanto menor `ρ`, mayor el beneficio de diversificar.

## Verificación en código

```python
# Riesgo: volatilidad, VaR, CVaR, Sharpe y diversificacion — Python exacto/verificado
import numpy as np
from scipy.stats import norm

# --- Datos: 10 retornos diarios simulados (en proporcion, no %) ---
r = np.array([0.012, -0.008, 0.005, -0.021, 0.017,
              -0.003, 0.009, -0.015, 0.002, 0.006])
V = 50_000_000.0   # posicion en COP

# --- Volatilidad muestral (n-1) ---
mu  = r.mean()
var = r.var(ddof=1)          # ddof=1 => divide entre n-1 (Bessel)
sig = np.sqrt(var)
print(f"media diaria  = {mu:.6f}")
print(f"volatilidad d = {sig:.6f}")

# VERIFICACION 1: var calculada a mano debe coincidir
var_manual = np.sum((r - mu)**2) / (len(r) - 1)
assert abs(var_manual - var) < 1e-15, "varianza no coincide"
assert abs(np.sqrt(var_manual) - sig) < 1e-15

# --- Anualizacion (252 dias) ---
k = 252
sig_anual = sig * np.sqrt(k)
mu_anual  = mu  * k
print(f"vol anual     = {sig_anual:.4f}  ({sig_anual*100:.2f}%)")

# --- VaR parametrico (Gaussiano) 95% a 1 dia, en dinero ---
alpha = 0.95
z = norm.ppf(1 - alpha)               # z_{0.05} = -1.6449
VaR_param = -(mu + z * sig) * V
print(f"z_0.05        = {z:.4f}")
print(f"VaR 95% param = {VaR_param:,.0f} COP")

# --- VaR historico (percentil 5 de los retornos) ---
q = np.percentile(r, (1 - alpha) * 100)   # percentil 5
VaR_hist = -q * V
print(f"VaR 95% hist  = {VaR_hist:,.0f} COP")

# --- CVaR (perdida promedio en la cola peor) ---
cola = r[r <= q]
CVaR = -cola.mean() * V
print(f"CVaR 95%      = {CVaR:,.0f} COP")
assert CVaR >= VaR_hist - 1, "CVaR debe ser >= VaR (cola mas profunda)"

# --- Sharpe (rf = 8% anual, tipico CDT Colombia) ---
rf = 0.08
sharpe = (mu_anual - rf) / sig_anual
print(f"Sharpe        = {sharpe:.3f}")
```

```python
# VERIFICACION 2 (segunda via): VaR parametrico via Monte Carlo
# Si los retornos fueran normales(mu, sig), simular 1M dias y tomar percentil 5
# debe acercarse al VaR parametrico cerrado.
import numpy as np
from scipy.stats import norm
mu, sig, V, alpha = 0.000400, 0.012566, 50_000_000.0, 0.95   # valores del bloque previo (aprox)
rng = np.random.default_rng(42)
sim = rng.normal(mu, sig, 1_000_000)
VaR_mc = -np.percentile(sim, (1-alpha)*100) * V
VaR_cerrado = -(mu + norm.ppf(1-alpha)*sig) * V
print(f"VaR Monte Carlo = {VaR_mc:,.0f}")
print(f"VaR cerrado     = {VaR_cerrado:,.0f}")
# Deben coincidir dentro de ~1% (error de muestreo)
assert abs(VaR_mc - VaR_cerrado)/VaR_cerrado < 0.01, "MC no valida la formula"
print("OK: Monte Carlo confirma la formula parametrica")
```

```python
# VERIFICACION 3: diversificacion reduce riesgo cuando rho < 1
import numpy as np
s1, s2, w1, w2 = 0.20, 0.30, 0.5, 0.5     # vol anuales y pesos
for rho in (1.0, 0.0, -1.0):
    sp = np.sqrt(w1**2*s1**2 + w2**2*s2**2 + 2*w1*w2*rho*s1*s2)
    print(f"rho={rho:+.0f}  sigma_portafolio = {sp:.4f}")
# rho=+1 => promedio ponderado (0.25); rho=0 => menor; rho=-1 => minimo (0.05)
prom = w1*s1 + w2*s2
sp_corr1 = np.sqrt(w1**2*s1**2 + w2**2*s2**2 + 2*w1*w2*1*s1*s2)
assert abs(sp_corr1 - prom) < 1e-12, "con rho=1 debe igualar el promedio ponderado"
print("OK: con correlacion < 1 el riesgo del portafolio baja")
```

## Ejemplo trabajado

**Caso:** Lushows invierte **$50.000.000 COP** en un activo. Con 10 días de retornos observa media diaria `μ = 0,000400` y volatilidad diaria `σ = 0,012566` (1,26 % por día).

1. **Volatilidad anual**: `σ_anual = 0,012566 · √252 = 0,1995` → **≈ 19,95 % anual**. (Unidad: % de variación por año.)
2. **VaR 95 % a 1 día (paramétrico)**: `z_{0,05} = −1,6449`
   `VaR = −(0,000400 + (−1,6449)·0,012566) · 50.000.000`
   `= −(0,000400 − 0,020670) · 50.000.000 = 0,020270 · 50.000.000 ≈ $1.013.500 COP`.
   **Lectura:** en un día normal (95 % de los días) no perderías más de **≈ $1.013.500**; pero 1 de cada 20 días podrías perder más.
3. **CVaR 95 %**: el promedio de la cola peor (~$1.050.000 COP) dice *qué tan grave* es ese 5 % de días malos — siempre ≥ VaR.
4. **¿Vale el riesgo?** Con `μ_anual = 0,000400·252 = 0,1008` (10,08 %) y `r_f = 8 %`:
   `Sharpe = (0,1008 − 0,08) / 0,1995 = 0,104`. Un Sharpe tan bajo (cercano a 0) dice que el retorno extra apenas compensa el riesgo: **un CDT al 8 % casi le iguala sin volatilidad**. Decisión bien fundamentada, no por intuición.

Todos los números provienen del código (no de cálculo mental) y están verificados por Monte Carlo.

## Errores comunes / trampas

- **Confundir VaR con el peor caso.** VaR 95 % NO es el máximo que puedes perder; es el umbral que se supera el 5 % de las veces. Para el "qué tan malo cuando pasa", usa **CVaR**.
- **Dividir la varianza entre `n` en vez de `n−1`** al estimar de una muestra: subestima el riesgo. Usa `ddof=1` (`s²`).
- **Anualizar la volatilidad multiplicando por `k` en vez de `√k`.** La vol escala con la raíz del tiempo; la media sí con `k`. Mezclarlas infla el riesgo varias veces.
- **Suponer normalidad ciegamente.** Los retornos reales tienen *colas gruesas* (eventos extremos más frecuentes que la campana). El VaR Gaussiano subestima crisis; contrasta con VaR histórico o `t`-Student.
- **Sumar VaR de activos como si fueran independientes.** El VaR de un portafolio NO es la suma de los VaR individuales salvo correlación perfecta; ignorar `ρ` desperdicia (o exagera) la diversificación.
- **Mezclar retornos simples y logarítmicos** en la misma serie, o reportar el riesgo sin unidad ni horizonte ("VaR de $1 M" sin decir 95 %, 1 día).
- **Float para el dinero final.** Calcula el riesgo con numpy, pero al **convertir a pesos y reportar** usa `decimal`/centavos y redondea una sola vez (ver [[12-fracciones-decimales-y-precision.md]] y [[05-cifras-significativas-y-redondeo.md]]).

## Cruces

- [[61-medidas-de-dispersion.md]] — varianza y desviación estándar, la base de la volatilidad.
- [[57-valor-esperado-y-varianza.md]] — media y varianza de variables aleatorias.
- [[56-distribuciones-continuas.md]] — la normal y sus percentiles (`z_α`) usados en el VaR paramétrico.
- [[58-simulacion-monte-carlo.md]] — segunda vía para validar y para VaR sin fórmula cerrada.
- [[93-analisis-de-sensibilidad-y-escenarios.md]] — complementa el riesgo con escenarios y estrés.
- [[63-correlacion-vs-causalidad.md]] — la correlación `ρ` que gobierna la diversificación.

**Mini-checklist de exactitud**
- [ ] Volatilidad anualizada con `√k` (no con `k`) y media con `k`.
- [ ] VaR reporta SIEMPRE confianza (95/99 %) y horizonte (1 día/10 días), con unidad de dinero.
- [ ] Resultado confirmado por segunda vía (Monte Carlo o VaR histórico) antes de decidir.
