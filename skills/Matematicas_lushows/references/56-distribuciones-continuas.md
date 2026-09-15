# 56 · Distribuciones continuas

> **Qué resuelve / cuándo usarlo** — Modelar variables que pueden tomar **cualquier valor dentro de un rango** (tiempos, pesos, estaturas, ingresos, errores de medición). Las usas para calcular probabilidades de rangos, percentiles, z-scores y para sustentar intervalos de confianza, A/B testing y simulación.

## Concepto (para no-experto)

Una **variable aleatoria continua** es una cantidad que no se cuenta de uno en uno, sino que se **mide**: el tiempo que tarda un cliente en pagar, el peso de un producto, la estatura de una persona. Entre dos valores cualesquiera siempre cabe otro (entre 1.70 m y 1.71 m hay infinitos valores).

Por eso, a diferencia de las **discretas** (ver [[55-distribuciones-discretas]]), aquí la probabilidad de un valor *exacto* es **cero** — preguntar "¿cuál es la probabilidad de que alguien mida exactamente 1.70000… m?" no tiene sentido. Lo que sí tiene sentido es preguntar por un **rango**: "¿probabilidad de que mida entre 1.70 y 1.80 m?".

Dos funciones clave (term. la 1ª vez):
- **Función de densidad (PDF, *probability density function*):** la curva. **No** es una probabilidad directa; es "qué tan denso" está el valor ahí. La probabilidad es el **área bajo la curva** en un rango (una integral, ver [[44-integrales]]). El área total bajo toda la curva = 1.
- **Función de distribución acumulada (CDF, *cumulative distribution function*):** `F(x) = P(X ≤ x)`. Te da directamente la probabilidad acumulada hasta `x`. Es la herramienta que más usarás.

> Regla mental: con continuas, **probabilidad = área = CDF**. `P(a ≤ X ≤ b) = F(b) − F(a)`.

## Fórmulas / método

**Relación PDF ↔ CDF:**
- `F(x) = P(X ≤ x) = ∫_{-∞}^{x} f(t) dt`
- `P(a ≤ X ≤ b) = F(b) − F(a)`
- `P(X > a) = 1 − F(a)`

**Las tres continuas que más vas a usar:**

| Distribución | Para qué | Parámetros | Media | Varianza |
|---|---|---|---|---|
| **Uniforme** `U(a,b)` | Todo valor en `[a,b]` igual de probable | `a`, `b` | `(a+b)/2` | `(b−a)²/12` |
| **Normal** `N(μ,σ²)` | Suma de muchos efectos pequeños (estaturas, errores, promedios muestrales) | media `μ`, desviación `σ` | `μ` | `σ²` |
| **Exponencial** `Exp(λ)` | Tiempo entre eventos aleatorios (esperas, fallas) | tasa `λ` | `1/λ` | `1/λ²` |

**Normal — lo esencial:**
- **z-score** (estandarizar): `z = (x − μ) / σ`. Convierte cualquier normal en la **normal estándar** `N(0,1)`.
- **Regla 68–95–99.7** (empírica): aprox. **68%** de los datos cae en `μ ± 1σ`, **95%** en `μ ± 2σ`, **99.7%** en `μ ± 3σ`.

## Verificación en código

Nunca calcules áreas bajo la normal de memoria ni con "tablas z" aproximadas: usa `scipy.stats`, que da el valor exacto. Y **verifica por segunda vía** (aquí: la CDF analítica de la exponencial y una simulación de la regla 68-95-99.7).

```python
from scipy import stats
import numpy as np

# --- NORMAL: P(170 <= X <= 180) con mu=175, sigma=7 (estaturas en cm) ---
mu, sigma = 175, 7
N = stats.norm(loc=mu, scale=sigma)
p = N.cdf(180) - N.cdf(170)          # área entre 170 y 180 = F(180) - F(170)
print(f"P(170<=X<=180) = {p:.6f}")    # 0.523813

# Verificación 2ª vía: z-scores + integración numérica de la PDF
z1, z2 = (170-mu)/sigma, (180-mu)/sigma
from scipy.integrate import quad
area, _ = quad(N.pdf, 170, 180)       # integra la densidad directamente
print(f"por z-score: {stats.norm().cdf(z2) - stats.norm().cdf(z1):.6f}")
print(f"por integral de la PDF: {area:.6f}")
assert abs(p - area) < 1e-9           # las dos vías coinciden -> resultado exacto

# --- Regla 68-95-99.7 (verificada) ---
for k in (1, 2, 3):
    print(f"mu±{k}sigma -> {N.cdf(mu+k*sigma) - N.cdf(mu-k*sigma):.4f}")
# 0.6827, 0.9545, 0.9973

# --- EXPONENCIAL: tiempo entre clientes, lambda=2/hora. P(esperar < 30 min) ---
lam = 2                                # eventos por hora
E = stats.expon(scale=1/lam)          # scipy usa "scale" = 1/lambda
p_30min = E.cdf(0.5)                  # 0.5 h
print(f"P(T<0.5h) = {p_30min:.6f}")   # 0.632121
# Verificación 2ª vía: CDF analítica F(x)=1-e^(-lambda*x)
print(f"analítica:  {1 - np.exp(-lam*0.5):.6f}")
assert abs(p_30min - (1 - np.exp(-lam*0.5))) < 1e-12
```

## Ejemplo trabajado

**Problema (negocio):** Empacas café en bolsas. La máquina llena con media `μ = 250 g` y desviación `σ = 4 g`, distribución normal. La ley exige **mínimo 245 g**. ¿Qué % de bolsas sale *por debajo* del mínimo (defectuosas)?

1. Modelo: `X ~ N(250, 4²)`, en gramos.
2. Buscamos `P(X < 245) = F(245)`.
3. z-score: `z = (245 − 250) / 4 = −1.25`.
4. Cálculo exacto en código:

```python
from scipy import stats
defect = stats.norm(250, 4).cdf(245)
print(f"{defect:.6f}  ->  {defect*100:.2f}%")   # 0.105650 -> 10.57%
# Verificación: con z = -1.25
print(f"{stats.norm().cdf(-1.25):.6f}")          # 0.105650  ✓ coincide
```

**Resultado: ≈ 10.57 % de las bolsas** salen bajo el mínimo legal. Decisión: subir la media de llenado (p. ej. a 253 g) o reducir la variabilidad `σ` de la máquina. Si subes `μ` a 252 g, recalcula: la tasa cae a `P(X<245)` con la nueva media ≈ **4.0 %**. *(Unidades: gramos; resultado verificado por dos vías.)*

## Errores comunes / trampas

- **Tratar la PDF como probabilidad.** `f(x)` puede ser > 1; no es una probabilidad. La probabilidad es siempre **área (CDF)**, nunca la altura de la curva.
- **`P(X = valor exacto) ≠ 0`.** En continuas, la probabilidad de un punto exacto es 0; siempre trabaja con rangos.
- **Confundir `σ` con `σ²`.** `scipy.stats.norm(loc, scale)` recibe la **desviación** `σ` (scale), no la varianza. Pasar la varianza es un error silencioso clásico.
- **Exponencial: `scale = 1/λ`, no `λ`.** `scipy` parametriza por la media `1/λ`. Confundirlo invierte el resultado.
- **Asumir normalidad sin verificar.** No todo es normal (ingresos y tiempos suelen tener cola larga). Mira la forma de los datos antes (ver [[62-distribucion-de-datos-y-visualizacion]]).
- **Tablas z redondeadas a mano.** Producen error en el 3er–4º decimal. Usa código.

**Checklist de exactitud:**
- [ ] ¿Pasé la **desviación** (`σ`), no la varianza, y `scale=1/λ` en la exponencial?
- [ ] ¿Calculé con CDF (área) y verifiqué por 2ª vía (integral, z-score o fórmula analítica)?
- [ ] ¿El resultado lleva unidades y tiene sentido (0 ≤ p ≤ 1)?

## Cruces
- [[55-distribuciones-discretas]] — el caso contable (de uno en uno)
- [[54-variables-aleatorias]] — el concepto base de variable aleatoria
- [[57-valor-esperado-y-varianza]] — media y varianza de estas distribuciones
- [[66-intervalos-de-confianza]] — la normal sustenta los intervalos
- [[58-simulacion-monte-carlo]] — cuando no hay fórmula cerrada, simula
- [[44-integrales]] — por qué la probabilidad continua es un área
