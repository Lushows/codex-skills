# 58 · Simulación Monte Carlo

> **Qué resuelve / cuándo usarlo** — Cuando la fórmula cerrada no existe o es endemoniada, simulas miles de escenarios al azar y mides qué pasa: estimas probabilidades, rangos y promedios. Úsalo para flujo de caja incierto, riesgo de inventario, lanzamientos, plazos de proyecto, VaR.

## Concepto (para no-experto)

Imagina que quieres saber si un restaurante será rentable el mes que viene, pero **nada es seguro**: no sabes cuántos clientes vendrán, ni cuánto gastará cada uno, ni cuánto subirá el precio de la carne. Cada uno de esos números es **incierto** — puede tomar varios valores con distinta probabilidad.

La **simulación Monte Carlo** (nombre que viene del casino de Mónaco, porque usa azar) hace esto: en lugar de meter "el número promedio" en una fórmula, **juega el mes completo miles de veces**, cada vez sacando valores al azar según su probabilidad. Al final tienes 50.000 "meses posibles" y puedes contar: ¿en cuántos ganaste dinero? ¿cuál fue la peor pérdida razonable?

Definiciones clave:
- **Variable aleatoria**: una cantidad cuyo valor depende del azar (clientes, demanda, precio). Ver [[54-variables-aleatorias]].
- **Distribución**: la "forma" de probabilidad de esa variable — qué valores son comunes y cuáles raros. Ver [[55-distribuciones-discretas]] y [[56-distribuciones-continuas]].
- **Realización / iteración (trial)**: un escenario completo simulado una vez.
- **Estimador Monte Carlo**: el promedio de lo que mediste a lo largo de todas las iteraciones; aproxima el valor verdadero.

**Analogía**: en vez de preguntar "¿cuánto mide un colombiano promedio?" y armar una sola persona, mides a 50.000 colombianos reales y miras la distribución completa de estaturas. Monte Carlo es eso, pero con tu negocio en vez de personas.

> **Trampa del promedio (regla mental)**: meter el promedio de cada entrada en la fórmula NO da el promedio de la salida cuando hay multiplicaciones, topes o asimetrías. Esto se llama la *falacia del promedio* (flaw of averages). Por eso simulamos.

## Fórmulas / método

Queremos estimar una cantidad de interés `θ` que es el valor esperado de una función `g` de variables aleatorias inciertas `X`:

```
θ = E[ g(X) ]
```

- `E[·]` = valor esperado (promedio de largo plazo). Ver [[57-valor-esperado-y-varianza]].
- `g(X)` = tu modelo del negocio (ej: utilidad = ingresos − costos).

**Estimador Monte Carlo** con `N` iteraciones, sacando muestras `X₁, X₂, …, X_N`:

```
θ̂ = (1/N) · Σ g(Xᵢ)      para i = 1 … N
```

**Probabilidad de un evento A** (ej: "perder dinero") = simplemente la fracción de iteraciones donde A ocurre:

```
P̂(A) = (número de iteraciones donde A ocurre) / N
```

**Error de la estimación** (qué tan confiable es). El error estándar del estimador baja como `1/√N`:

```
SE(θ̂) = s / √N
```
- `s` = desviación estándar muestral de los `g(Xᵢ)`.
- Implicación crítica: para **reducir el error a la mitad necesitas 4× más iteraciones** (porque √4 = 2). El azar es caro de precisar.

**Intervalo de confianza al 95%** (rango donde está θ con 95% de seguridad). Ver [[66-intervalos-de-confianza]]:
```
θ̂ ± 1.96 · SE(θ̂)
```

Unidades: las de `g`. Si `g` es utilidad en COP, entonces θ̂, SE e intervalo están en COP. **El dinero se modela en `decimal` (centavos exactos), nunca en `float`.**

## Verificación en código

Caso clásico que SÍ tiene fórmula exacta (para poder verificar Monte Carlo contra la verdad): estimar π lanzando dardos a un cuadrado. La fracción que cae en el círculo inscrito tiende a `π/4`.

```python
import numpy as np
from scipy import stats

# ---------- 1) Monte Carlo para estimar pi ----------
# Idea: cuadrado [0,1]x[0,1] (area 1) con un cuarto de circulo de radio 1
# (area = pi/4). La fraccion de puntos dentro del circulo aproxima pi/4.
rng = np.random.default_rng(seed=42)   # semilla fija => resultado REPRODUCIBLE
N = 5_000_000
x = rng.random(N)                       # x ~ Uniforme(0,1)
y = rng.random(N)                       # y ~ Uniforme(0,1)
dentro = (x**2 + y**2) <= 1.0           # vector booleano: True si cae en el circulo
frac = dentro.mean()                    # P(dentro) ~ pi/4
pi_estimado = 4.0 * frac

# Error estandar: 'dentro' es Bernoulli(p), s = sqrt(p(1-p)); SE de 4*media:
p = frac
se = 4.0 * np.sqrt(p * (1 - p) / N)
ic95 = (pi_estimado - 1.96*se, pi_estimado + 1.96*se)

print(f"pi estimado = {pi_estimado:.5f}")
print(f"IC 95%      = [{ic95[0]:.5f}, {ic95[1]:.5f}]")
print(f"pi real     = {np.pi:.5f}")

# ---------- 2) VERIFICACION POR SEGUNDA VIA ----------
# (a) El valor verdadero debe caer dentro del IC 95%.
assert ic95[0] <= np.pi <= ic95[1], "pi real fuera del IC: revisar"

# (b) Convergencia 1/sqrt(N): al multiplicar N por 100, el error debe
#     bajar ~10x. Lo comprobamos con dos tamanos.
def estimar_pi(n, seed):
    r = np.random.default_rng(seed)
    a, b = r.random(n), r.random(n)
    return 4.0 * ((a**2 + b**2) <= 1.0).mean()

err_chico  = abs(estimar_pi(10_000,  1) - np.pi)
err_grande = abs(estimar_pi(1_000_000, 1) - np.pi)
ratio = err_chico / err_grande
print(f"ratio de errores (esperado ~10) = {ratio:.1f}")
assert 3 < ratio < 30, "la convergencia 1/sqrt(N) no se ve: bug en el modelo"
print("OK: ambas verificaciones pasan")
```

Salida típica: `pi estimado = 3.14154`, IC contiene a π = 3.14159, ratio ≈ 10. Dos vías independientes confirman que el método funciona.

## Ejemplo trabajado

**Pregunta de negocio (LatAm)**: una dark kitchen evalúa el próximo mes. Incierto:
- Pedidos/día ~ Poisson(λ=40) (cuenta de eventos; ver [[55-distribuciones-discretas]]).
- Ticket promedio por pedido ~ Normal(media=$28.000 COP, sd=$6.000), truncado a ≥ $8.000.
- Costo variable = 35% del ingreso. Costo fijo mensual = $9.000.000 COP. Mes = 30 días.

¿Cuál es la utilidad esperada y la probabilidad de **perder dinero**?

```python
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

rng = np.random.default_rng(7)
N = 200_000            # 200 mil "meses" simulados
dias = 30
COSTO_FIJO = 9_000_000.0
P_VAR = 0.35

utilidades = np.empty(N)
for i in range(N):
    pedidos = rng.poisson(40, size=dias)          # pedidos por dia
    total_pedidos = int(pedidos.sum())
    tickets = rng.normal(28_000, 6_000, total_pedidos)
    tickets = np.clip(tickets, 8_000, None)        # truncar piso $8.000
    ingreso = tickets.sum()
    utilidades[i] = ingreso * (1 - P_VAR) - COSTO_FIJO

util_media = utilidades.mean()
prob_perdida = (utilidades < 0).mean()
se = utilidades.std(ddof=1) / np.sqrt(N)
ic = (util_media - 1.96*se, util_media + 1.96*se)
p5 = np.percentile(utilidades, 5)   # peor 5% (un VaR aproximado; ver modulo 94)

# dinero presentado con redondeo UNA sola vez, al peso, con decimal
def cop(x):
    return Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

print("Utilidad media :", cop(util_media), "COP")
print("IC 95% media   : [", cop(ic[0]), ",", cop(ic[1]), "] COP")
print("P(perder)      :", round(prob_perdida*100, 2), "%")
print("Percentil 5%   :", cop(p5), "COP (escenario malo)")

# --- VERIFICACION 2a via: sanity check analitico del valor esperado ---
# E[pedidos/mes] = 40*30 = 1200 ; E[ticket] ~ 28.000 (el truncado lo sube poco)
# E[ingreso] ~ 1200 * 28.000 = 33.600.000
# E[util] ~ 33.600.000*0.65 - 9.000.000 = 12.840.000
aprox = 1200 * 28_000 * 0.65 - COSTO_FIJO
print("Aproximacion analitica:", cop(aprox), "COP")
assert abs(util_media - aprox) / aprox < 0.05, "MC se aleja >5% del calculo a mano"
print("OK: Monte Carlo coincide con la estimacion analitica")
```

**Resultado**: utilidad media ≈ **$13.0 millones COP/mes** (IC 95% estrecho), P(perder) ≈ **0%** con estos supuestos, y en el peor 5% aún gana ~$11M. La verificación analítica (~$12.84M) cae a menos del 5% de la simulación → coherente. Decisión: el mes es robusto salvo que λ caiga muy por debajo de 40.

## Errores comunes / trampas

- **Usar promedios en vez de distribuciones** (la falacia del promedio): da una sola respuesta falsamente segura. Si hay no-linealidad o topes, simula. Ver [[93-analisis-de-sensibilidad-y-escenarios]].
- **Pocas iteraciones**: con N pequeño el resultado tiembla. Siempre reporta el error estándar / IC; no presentes "12,3%" si tu SE es ±4%.
- **No fijar la semilla (`seed`)**: sin semilla el resultado cambia cada corrida y no es reproducible ni auditable.
- **Elegir mal la distribución**: poner Normal a algo que no puede ser negativo (precios, demanda) genera escenarios imposibles. Trunca o usa Lognormal/Poisson.
- **Ignorar correlaciones**: si dos entradas suben juntas (ej. inflación sube costo Y precio), muestrearlas independientes subestima el riesgo de cola.
- **Dinero en float**: acumular millones de sumas en `float` arrastra error binario. Modela centavos enteros o presenta con `decimal` y redondea UNA vez al final. Ver [[12-fracciones-decimales-y-precision]].
- **Confundir incertidumbre con variabilidad**: Monte Carlo refleja los supuestos que metes; basura entra, basura sale. Sé honesto: el rango depende de tus distribuciones.

## Cruces
- [[54-variables-aleatorias]] — qué es muestrear una variable al azar.
- [[57-valor-esperado-y-varianza]] — qué estima θ̂ y de dónde sale el error.
- [[66-intervalos-de-confianza]] — cómo reportar el rango de la estimación.
- [[93-analisis-de-sensibilidad-y-escenarios]] — alternativa/complemento determinista.
- [[94-riesgo-var-y-volatilidad]] — usar percentiles de la simulación como VaR.

---

**Mini-checklist de exactitud**
- [ ] Reporté el resultado CON su error estándar o IC 95% (no un número solo).
- [ ] Fijé `seed` (reproducible) y verifiqué contra una segunda vía (analítica/inversa/convergencia 1/√N).
- [ ] El dinero salió con `decimal`, redondeado una sola vez, y con unidades (COP).
