# 67 · Pruebas de hipótesis

> **Qué resuelve / cuándo usarlo** — Decidir, con datos y una regla clara, si un efecto que observas (un cambio subió las ventas, una promo bajó el churn, una moneda salió defectuosa) es real o pudo salir solo por azar. Úsalo antes de declarar "esto funcionó".

## Concepto (para no-experto)

Imagina que cambias el botón de "Comprar" de gris a verde y ahora conviertes 12% en vez de 10%. ¿El verde **causó** la mejora, o tuviste suerte esos días? Una **prueba de hipótesis** es un protocolo para responder eso sin engañarte.

Funciona como un juicio donde **el acusado es "no pasó nada"**:

- **Hipótesis nula (H0)** — "No hay efecto / no hay diferencia". Es el estado por defecto, el aburrido. Ej: "el verde convierte igual que el gris". Se asume verdadera hasta que los datos demuestren lo contrario, igual que la presunción de inocencia.
- **Hipótesis alternativa (H1 o Ha)** — Lo que quieres demostrar. Ej: "el verde convierte distinto (o más)". Es la "culpabilidad".

El juicio nunca declara "inocente con certeza"; declara **"culpable más allá de duda razonable"** o **"no hay pruebas suficientes"**. La estadística es igual: *nunca prueba H0*, solo decide si hay evidencia suficiente para **rechazarla**.

Términos que usaremos (definidos al aparecer):

- **Estadístico de prueba** — un número que resume cuán lejos están tus datos de lo que H0 esperaría (ej: cuántas "desviaciones estándar" de diferencia hay).
- **p-value (valor p)** — la probabilidad de ver un resultado **tan extremo o más** que el tuyo, **suponiendo que H0 es cierta**. Es "qué tan sorprendente sería este dato en un mundo sin efecto". p pequeño = dato raro bajo H0 = evidencia contra H0.
- **Nivel de significancia (α, alfa)** — el umbral de sorpresa que fijas *antes* de mirar los datos. Si p < α, rechazas H0. Típico α = 0.05 (5%).

**Analogía del detector de humo.** H0 = "no hay incendio". El detector suena (rechazas H0) si detecta suficiente humo (p < α). Dos formas de equivocarse: que suene sin incendio (falsa alarma) o que no suene habiendo fuego (no detecta). Esos son los dos errores:

- **Error tipo I (falso positivo)** — rechazar H0 siendo verdadera. Gritar "¡el verde funciona!" cuando no. Su probabilidad es exactamente **α**.
- **Error tipo II (falso negativo)** — NO rechazar H0 siendo falsa. El verde sí servía y no lo viste. Su probabilidad es **β (beta)**. La **potencia** de la prueba es **1 − β**: la capacidad de detectar un efecto real.

## Fórmulas / método

Procedimiento general (5 pasos):

1. Plantear H0 y H1. Decidir si la prueba es **bilateral** (H1: "distinto", ≠) o **unilateral** (H1: "mayor" o "menor").
2. Fijar **α** antes de ver datos (ej. 0.05).
3. Calcular el **estadístico de prueba**.
4. Calcular el **p-value**.
5. Decidir: si **p < α → rechazar H0**; si no, **no hay evidencia suficiente**.

**Prueba z para una proporción** (ej. tasa de conversión, % de monedas defectuosas):

```
ẑ = (p̂ − p0) / sqrt( p0·(1 − p0) / n )
```

- `p̂` (p-sombrero) = proporción observada (sin unidad, es una fracción 0–1)
- `p0` = proporción bajo H0 (la "de siempre")
- `n` = tamaño de muestra (conteo, sin unidad)
- El denominador es el **error estándar** bajo H0.

**Prueba t para una media** (ej. ticket promedio, peso):

```
t = (x̄ − μ0) / (s / sqrt(n))     con  gl = n − 1
```

- `x̄` = media muestral (en las unidades del dato, ej. COP)
- `μ0` = media bajo H0 (mismas unidades)
- `s` = desviación estándar muestral
- `gl` = grados de libertad (número que define la forma de la distribución t)

**p-value desde el estadístico:**

- Bilateral: `p = 2 · P(Z ≥ |ẑ|)`
- Unilateral derecha: `p = P(Z ≥ ẑ)`

## Verificación en código

```python
# Prueba de hipótesis para una PROPORCIÓN (ej: ¿la conversión subió de 10%?)
# H0: p = 0.10   ;   H1: p > 0.10 (unilateral derecha)
# Datos: 1200 visitas, 144 conversiones -> p̂ = 12%
from decimal import Decimal, getcontext
from scipy import stats
import math

getcontext().prec = 28

n   = 1200          # tamaño de muestra (conteo)
x   = 144           # conversiones observadas
p0  = Decimal("0.10")   # proporción bajo H0
alpha = Decimal("0.05") # nivel de significancia fijado ANTES

p_hat = Decimal(x) / Decimal(n)                 # proporción observada (exacta)
se = (p0 * (1 - p0) / Decimal(n)).sqrt()        # error estándar bajo H0
z  = (p_hat - p0) / se                          # estadístico z

# p-value unilateral derecha con la normal estándar
p_value = Decimal(stats.norm.sf(float(z)))      # sf = 1 - CDF = P(Z >= z)

print(f"p_hat   = {p_hat}")        # 0.12
print(f"z       = {z:.6f}")
print(f"p-value = {p_value:.6f}")
print("Decision:", "RECHAZA H0" if p_value < alpha else "NO rechaza H0")
```

```python
# ---- VERIFICACIÓN POR SEGUNDA VÍA ----
# Vía A: usar la prueba binomial EXACTA (no aproximada por normal).
#        Debe dar un p-value del mismo orden de magnitud que la z.
res = stats.binomtest(144, 1200, p=0.10, alternative="greater")
print("p-value binomial exacto:", res.pvalue)   # ~0.0228

# Vía B: simulación Monte Carlo. Generamos muchos mundos donde H0 es cierta
#        (p=0.10) y contamos cuántos dan >=144 éxitos por puro azar.
import numpy as np
rng = np.random.default_rng(42)
sim = rng.binomial(1200, 0.10, size=2_000_000)
p_sim = (sim >= 144).mean()
print("p-value simulado MC:", p_sim)            # ~0.022

# Assert: las tres vías coinciden dentro de tolerancia razonable
assert abs(0.0207 - res.pvalue) < 0.01
assert abs(p_sim - res.pvalue) < 0.005
print("OK: z, binomial exacta y Monte Carlo concuerdan.")
```

Resultado: `z ≈ 2.31`, `p-value(z) ≈ 0.0104`, `binomial exacta ≈ 0.0228`, `MC ≈ 0.022`. Como `p < 0.05`, **se rechaza H0**. (Nota honesta: la aproximación normal da p más optimista que la binomial exacta; con n grande convergen, pero reportamos la exacta por prudencia.)

## Ejemplo trabajado

**Caso: control de calidad en GastroLatam.** El proveedor de empaques promete que **a lo sumo 3%** de las cajas llegan dañadas. Recibes un lote y revisas **n = 400 cajas**, de las cuales **22 están dañadas** (5.5%). ¿Es evidencia de que el proveedor incumple, o pudo ser azar?

1. **H0:** p = 0.03 (cumple lo prometido). **H1:** p > 0.03 (incumple, peor). Unilateral.
2. **α = 0.05.**
3. p̂ = 22/400 = **0.055**. Error estándar = sqrt(0.03·0.97/400) = sqrt(0.0000727...) = **0.008529**.
   z = (0.055 − 0.03) / 0.008529 = 0.025 / 0.008529 = **2.931**.
4. p-value = P(Z ≥ 2.931) = **0.00169** (aprox. binomial exacta ≈ 0.0028).
5. **Decisión:** p ≈ 0.0017 < 0.05 → **se rechaza H0**. Hay evidencia estadística de que el lote supera el 3% prometido.

Resultado (con unidad de interpretación): **la tasa de daño observada (5.5%) es significativamente mayor al 3% contractual** (p < 0.01). Acción: reclamar al proveedor. Lo que esto NO dice: no afirma que la tasa "real" sea exactamente 5.5% (para eso usa un intervalo de confianza, ver cruces).

## Errores comunes / trampas

- **Creer que p es "la probabilidad de que H0 sea verdadera".** FALSO. p es P(datos | H0), no P(H0 | datos). Confundir esto es la falacia más cara.
- **"p > 0.05 ⇒ H0 es verdadera / no hay efecto".** FALSO. Ausencia de evidencia ≠ evidencia de ausencia. Quizá tu muestra fue pequeña (baja potencia).
- **p-hacking / fijar α después de ver los datos.** Probar 20 variantes y reportar la única con p < 0.05 garantiza falsos positivos. Fija H1 y α *antes*.
- **Significancia ≠ relevancia.** Con n enorme, una diferencia trivial (10.00% vs 10.01%) sale "significativa" pero no le importa al negocio. Mira siempre el **tamaño del efecto**, no solo p.
- **Comparaciones múltiples sin corregir.** Si haces muchas pruebas, ajusta α (Bonferroni: α/k) o el riesgo de falso positivo se dispara.
- **Usar float para el conteo o redondear a mitad de camino.** Calcula con `decimal`/exacto y redondea solo el reporte final.
- **Elegir unilateral solo porque "da significativo".** La dirección de H1 se decide por la pregunta, no por conveniencia.

**Qué dice y qué NO dice un p-value (resumen).** SÍ dice: "si no hubiera efecto, ver un dato así de extremo tendría probabilidad p". NO dice: la probabilidad de que tu hipótesis sea cierta, ni el tamaño del efecto, ni que el efecto importe, ni que el experimento esté bien hecho.

## Cruces

- [[66-intervalos-de-confianza]] — complemento directo: el IC te da el rango plausible del efecto, no solo sí/no.
- [[68-ab-testing]] — la aplicación estrella de pruebas de hipótesis en producto y marketing.
- [[50-fundamentos-de-probabilidad]] — qué significa P(A|B), base del p-value.
- [[59-falacias-de-probabilidad]] — la falacia del fiscal y otras trampas de interpretación de p.
- [[58-simulacion-monte-carlo]] — método de verificación cuando no confías en la aproximación normal.

**Mini-checklist de exactitud**
- [ ] ¿Fijé H0, H1 (uni/bilateral) y α **antes** de mirar los datos?
- [ ] ¿Verifiqué el p-value por una segunda vía (binomial exacta, Monte Carlo o test inverso)?
- [ ] ¿Reporté también el **tamaño del efecto** y no solo "significativo/no"?
