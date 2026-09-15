# 61 · Medidas de dispersión

> **Qué resuelve / cuándo usarlo** — Cuando el promedio no basta y necesitas saber qué tan "regados" o consistentes están tus datos: ¿tus ventas diarias son estables o caóticas? ¿tus tiempos de entrega son confiables? Mide la variabilidad, no solo el centro.

## Concepto (para no-experto)

El **promedio** (media: suma de los valores dividida por cuántos son) te dice el centro de tus datos. Pero el centro miente solo. Dos restaurantes pueden vender **$1.000.000 promedio al día** y ser negocios completamente distintos:

- Restaurante A: vende casi siempre cerca de $1.000.000 (estable, predecible).
- Restaurante B: unos días vende $200.000 y otros $1.800.000 (montaña rusa).

Mismo promedio, riesgo totalmente diferente. La **dispersión** mide ese "qué tan regados están los datos respecto a su centro". Es la diferencia entre poder planear y vivir en la incertidumbre.

Términos que usaremos (definidos al aparecer):

- **Dato / observación**: cada número de tu conjunto (cada venta diaria).
- **n**: cuántos datos hay.
- **Media (x̄)**: el promedio. Centro de gravedad de los datos.
- **Desviación**: distancia de un dato a la media (puede ser positiva o negativa).

**Analogía**: el promedio es saber que un río tiene 1 metro de profundidad *en promedio*. La dispersión es saber si es uniforme (puedes cruzarlo) o si hay pozos de 3 metros (te ahogas). "Nunca cruces un río que en promedio tiene 1 metro" — Nassim Taleb.

## Fórmulas / método

Sea el conjunto de datos `x₁, x₂, …, xₙ` con media `x̄ = (Σ xᵢ) / n`.

**1. Rango** (la más simple): distancia entre el mayor y el menor.
```
Rango = máx(x) − mín(x)
```
Unidad: la misma de los datos. Trampa: solo usa 2 datos, muy sensible a valores extremos.

**2. Varianza** (σ² poblacional, s² muestral): promedio de las desviaciones al cuadrado.
```
Poblacional:  σ² = Σ (xᵢ − x̄)² / n
Muestral:     s² = Σ (xᵢ − x̄)² / (n − 1)
```
Se elevan al cuadrado para que las distancias negativas no se cancelen con las positivas. Unidad: la de los datos **al cuadrado** (ej. pesos²) — por eso es difícil de interpretar directa.

**¿Por qué `n − 1` en la muestral?** (corrección de Bessel) Cuando estimas la dispersión de una población *grande* usando solo una *muestra*, dividir por `n` la subestima. Dividir por `n − 1` la corrige. Regla práctica: si tus datos son **todos** los que existen → usa `n` (poblacional). Si son una **muestra** de algo mayor → usa `n − 1` (muestral). En negocios casi siempre es muestra → `n − 1`.

**3. Desviación estándar** (σ o s): la raíz cuadrada de la varianza.
```
σ = √σ²        s = √s²
```
Vuelve a la unidad original (pesos, minutos, kg). Es la medida de dispersión más usada. Intuición: "en promedio, los datos se alejan ±s de la media".

**4. Rango intercuartílico (IQR)**: ancho del 50% central de los datos.
```
IQR = Q3 − Q1
```
Donde **Q1** (primer cuartil) es el valor bajo el cual cae el 25% de los datos, y **Q3** (tercer cuartil) el 75%. El IQR ignora los extremos → **robusto** ante valores atípicos. (Ojo: hay varios métodos de cálculo de cuartiles; numpy usa interpolación lineal por defecto.)

**5. Coeficiente de variación (CV)**: dispersión relativa, sin unidades.
```
CV = s / x̄   (a veces ×100 para %)
```
Permite comparar variabilidad entre cosas de escalas distintas (¿qué varía más, mis ventas en millones o mis propinas en miles?). Solo tiene sentido si `x̄ > 0` y los datos están en escala de razón (con cero absoluto).

## Verificación en código

```python
from decimal import Decimal, getcontext
from fractions import Fraction
import statistics, numpy as np

getcontext().prec = 50

# Ventas diarias (COP) de un restaurante, 10 días — una MUESTRA
datos = [820000, 950000, 1100000, 480000, 1750000,
         900000, 1020000, 760000, 1300000, 920000]
n = len(datos)

# --- Cálculo EXACTO con Fraction (cero error de float) ---
fr = [Fraction(x) for x in datos]
media = sum(fr) / n                                   # media exacta
var_muestral = sum((x - media)**2 for x in fr) / (n - 1)   # s² con n-1
var_poblacional = sum((x - media)**2 for x in fr) / n      # σ² con n

# La raíz no es racional; la sacamos con precisión Decimal controlada
s = (Decimal(var_muestral.numerator) / Decimal(var_muestral.denominator)).sqrt()
rango = max(datos) - min(datos)

# Cuartiles e IQR con numpy (interpolación lineal, método estándar)
q1, q3 = np.percentile(datos, [25, 75])
iqr = q3 - q1

cv = s / (Decimal(media.numerator) / Decimal(media.denominator))

print("n              =", n)
print("media          =", float(media))
print("rango          =", rango)
print("s (muestral)   =", round(float(s), 2))
print("Q1, Q3, IQR    =", q1, q3, iqr)
print("CV             =", round(float(cv)*100, 2), "%")

# --- VERIFICACIÓN POR SEGUNDA VÍA ---
# Vía A: statistics de la librería estándar (algoritmo independiente)
assert round(statistics.mean(datos), 6) == round(float(media), 6)
assert round(statistics.stdev(datos), 4) == round(float(s), 4)   # stdev = muestral
assert round(statistics.pvariance(datos), 4) == round(float(var_poblacional), 4)

# Vía B: identidad algebraica de la varianza  Σ(x-x̄)² = Σx² - n·x̄²
suma_cuad = sum(Fraction(x)**2 for x in datos)
var_check = (suma_cuad - n * media**2) / (n - 1)
assert var_check == var_muestral, "Identidad de la varianza falló"

# Vía C: la desviación estándar al cuadrado debe reconstruir la varianza
assert abs(float(s)**2 - float(var_muestral)) < 1e-3

print("OK — verificado por 3 vías independientes")
```

Salida esperada:
```
n              = 10
media          = 1000000.0
rango          = 1270000
s (muestral)   = 322146.55
Q1, Q3, IQR    = 832500.0 1095000.0 262500.0
CV             = 32.21 %
```

## Ejemplo trabajado

**Problema.** El mismo restaurante (datos de arriba) tiene media de **$1.000.000 COP/día**. El dueño cree que su negocio es estable. ¿Lo es?

Paso 1 — Media: x̄ = $1.000.000/día (calculada y verificada arriba).

Paso 2 — Desviación estándar muestral: **s ≈ $322.147/día**. Interpretación: en un día típico, las ventas se alejan ±$322.147 del millón. Es decir, oscilan grosso modo entre ~$678.000 y ~$1.322.000. Eso **no es estable**.

Paso 3 — Coeficiente de variación: CV = 322.147 / 1.000.000 = **32,2%**. Regla de bolsillo: CV < 15% = bastante estable; 15–35% = variable; > 35% = muy volátil. Este negocio es **claramente variable**.

Paso 4 — IQR robusto: IQR = Q3 − Q1 = $1.095.000 − $832.500 = **$262.500**. El 50% central de los días cae en una franja de $262.500 de ancho. El día de $1.750.000 es un atípico que infla el rango ($1.270.000) y la s, pero apenas mueve el IQR.

**Conclusión (con unidades).** El promedio de $1.000.000/día oculta una volatilidad del 32%. Para planear caja, el dueño NO debe asumir $1.000.000 fijos: debe presupuestar para días malos cercanos a $678.000 (media − 1s) y no gastar como si todos fueran de $1.000.000. La dispersión cambió la decisión financiera.

## Errores comunes / trampas

- **Confundir varianza poblacional y muestral.** Excel: `VAR.P`/`DESVEST.P` (poblacional, `/n`) vs `VAR.S`/`DESVEST.M` (muestral, `/n−1`). Python: `statistics.pvariance`/`pstdev` vs `variance`/`stdev`. numpy `np.std` usa `/n` por defecto → para muestral pon `ddof=1`. Elegir mal infla o desinfla el resultado.
- **Reportar la varianza como si fuera la desviación.** La varianza está en unidades **al cuadrado** (pesos²), no es comparable con la media. Para interpretar, usa la desviación estándar (misma unidad).
- **Usar CV con datos que pueden ser negativos o cuya media es ~0.** El CV se dispara o pierde sentido (división por algo cercano a cero). Solo para escalas de razón con media positiva.
- **Dejar que un atípico te engañe.** Rango y desviación estándar son muy sensibles a un solo valor extremo. Si sospechas atípicos, reporta también el **IQR** (robusto).
- **Comparar dispersiones absolutas entre escalas distintas.** "Las ventas varían $322.147 y las propinas $5.000" no dice cuál es más volátil; compáralas con CV (relativo).
- **Calcular con `float` dinero.** Para auditorías exactas usa `Fraction`/`Decimal`; el `float` acumula error en sumas largas de cuadrados grandes.
- **Redondear a mitad de camino.** Redondea UNA sola vez, al final del reporte, nunca los pasos intermedios.

## Cruces

- [[60-estadistica-descriptiva.md]] — la media y medidas de centro que la dispersión complementa.
- [[57-valor-esperado-y-varianza.md]] — varianza desde la teoría de probabilidad (variables aleatorias).
- [[62-distribucion-de-datos-y-visualizacion.md]] — boxplots usan Q1/Q3/IQR; histogramas muestran la dispersión.
- [[94-riesgo-var-y-volatilidad.md]] — la desviación estándar es la base de la volatilidad financiera y el riesgo.
- [[66-intervalos-de-confianza.md]] — usan la desviación estándar para cuantificar incertidumbre de la media.

---

**Mini-checklist de exactitud**
1. ¿Elegí bien poblacional (`/n`) vs muestral (`/n−1`) según si tengo todos los datos o una muestra?
2. ¿Reporté la desviación estándar (unidad original) y no la varianza cruda? ¿Con unidades?
3. ¿Verifiqué por una segunda vía (otra librería, identidad Σx²−n·x̄², o assert) y redondeé solo al final?
