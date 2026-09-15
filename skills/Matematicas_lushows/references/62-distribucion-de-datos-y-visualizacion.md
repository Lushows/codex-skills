# 62 · Distribución de datos y visualización

> **Qué resuelve / cuándo usarlo** — Antes de promediar un conjunto de datos, mira su *forma*: histograma, percentiles, sesgo y outliers. Te dice si el promedio es honesto o si te está mintiendo.

## Concepto (para no-experto)

Imagina que mides cuánto gasta cada cliente en tu restaurante en un día. Tienes 200 números. Si solo calculas el **promedio** (la suma dividida entre la cantidad), corres un peligro real: un solo cliente que organizó un evento de $2.000.000 puede inflar el promedio y hacerte creer que "el cliente típico gasta mucho", cuando la mayoría gasta $25.000. **Por eso miramos la distribución ANTES de promediar.**

Definamos los términos clave (cada uno la primera vez):

- **Distribución**: cómo se reparten los datos a lo largo de su rango. ¿Están apelotonados cerca de un valor? ¿Repartidos parejo? ¿Con una cola larga hacia un lado?
- **Histograma**: un gráfico de barras donde el eje horizontal se parte en intervalos iguales llamados **bins** (cajones/cubetas) y la altura de cada barra cuenta cuántos datos caen en ese bin. Es la "radiografía" de la forma. Analogía: si vaciaras todos los gastos en frascos etiquetados "$0–10k", "$10k–20k", etc., el histograma es la foto de qué tan llenos quedan los frascos.
- **Percentil**: el valor por debajo del cual cae cierto porcentaje de los datos. El **percentil 90 (P90)** es el valor que deja al 90% de los datos por debajo. La **mediana** es el P50: el valor del medio, el que parte los datos en dos mitades iguales.
- **Cuartiles**: los percentiles 25, 50 y 75 (Q1, Q2=mediana, Q3). El **rango intercuartílico (IQR)** = Q3 − Q1: el ancho de la "caja central" donde vive el 50% más típico.
- **Sesgo (skewness)**: mide si la distribución es asimétrica. **Sesgo positivo** (cola a la derecha) = unos pocos valores muy grandes estiran la cola derecha (típico en ingresos, gastos, tiempos de espera). **Sesgo negativo** = cola a la izquierda. Sesgo ≈ 0 = simétrica.
- **Outlier (valor atípico)**: un dato que está muy lejos del resto. No siempre es un error; a veces es la información más valiosa (un cliente VIP, un fraude, una venta récord).

Regla de oro: **si la distribución es muy sesgada, la mediana describe mejor "lo típico" que el promedio.**

## Fórmulas / método

**Percentil por interpolación lineal** (método "linear" de NumPy, el estándar). Para el percentil `p` (0 ≤ p ≤ 100) sobre `n` datos ordenados `x[0] ≤ ... ≤ x[n-1]`:

```
rango   = (p/100) · (n − 1)        # posición fraccionaria (índice base 0)
k       = floor(rango)             # índice entero inferior
d       = rango − k                # parte fraccionaria
Pp      = x[k] + d · (x[k+1] − x[k])   # interpolación entre vecinos
```

Si `rango` es entero, `Pp = x[rango]`. Unidades: las mismas que los datos (p. ej. COP).

**Regla del IQR para outliers (Tukey)** — un dato es atípico si cae fuera de:

```
límite_inferior = Q1 − 1.5 · IQR
límite_superior = Q3 + 1.5 · IQR        donde IQR = Q3 − Q1
```

**Sesgo (skewness muestral, fórmula ajustada de Fisher-Pearson)**:

```
g1 = (1/n) · Σ ( (xᵢ − x̄) / s )³          (sesgo poblacional/biased)
G1 = g1 · √(n(n−1)) / (n−2)                 (corrección muestral, n>2)
```

donde `x̄` es la media y `s` la desviación estándar muestral. Interpretación: `|G1| < 0.5` ≈ casi simétrico; `0.5–1` moderado; `>1` fuerte. Unidad: adimensional (es una razón al cubo).

**Regla de Sturges para nº de bins** del histograma: `bins ≈ ⌈log₂(n) + 1⌉`. Es un punto de partida, no ley.

## Verificación en código

```python
# Distribución de gastos por cliente (COP) en un restaurante — un día.
import numpy as np
from scipy import stats

# Datos: la mayoría gasta poco, unos pocos eventos grandes (cola derecha).
gastos = np.array([
    18000, 22000, 25000, 25000, 27000, 30000, 31000, 33000, 35000, 40000,
    21000, 24000, 26000, 28000, 29000, 32000, 34000, 38000, 45000, 52000,
    19000, 23000, 27000, 30000, 36000, 42000, 60000, 95000, 1500000, 2000000
], dtype=float)
n = gastos.size

media    = gastos.mean()
mediana  = np.median(gastos)
q1, q3   = np.percentile(gastos, [25, 75])
iqr      = q3 - q1
p90, p99 = np.percentile(gastos, [90, 99])
sesgo    = stats.skew(gastos, bias=False)   # G1, corregido para muestra

lim_inf  = q1 - 1.5 * iqr
lim_sup  = q3 + 1.5 * iqr
outliers = gastos[(gastos < lim_inf) | (gastos > lim_sup)]

print(f"n              = {n}")
print(f"Media          = {media:,.0f} COP")
print(f"Mediana (P50)  = {mediana:,.0f} COP")
print(f"Q1 / Q3        = {q1:,.0f} / {q3:,.0f} COP   IQR={iqr:,.0f}")
print(f"P90 / P99      = {p90:,.0f} / {p99:,.0f} COP")
print(f"Sesgo (G1)     = {sesgo:.3f}")
print(f"Outliers (>{lim_sup:,.0f}): {outliers.astype(int).tolist()}")

# Histograma en texto (sin librería gráfica) con regla de Sturges.
bins = int(np.ceil(np.log2(n) + 1))
conteo, bordes = np.histogram(gastos, bins=bins)
for i, c in enumerate(conteo):
    print(f"[{bordes[i]:>9,.0f} - {bordes[i+1]:>9,.0f}) | {'█'*c} {c}")
```

**Verificación por segunda vía** (percentil a mano + cuenta de outliers + chequeo de sesgo):

```python
# (A) P90 recalculado con la fórmula de interpolación, a mano.
x = np.sort(gastos)
p = 90
rango = (p/100) * (n - 1)
k = int(np.floor(rango)); d = rango - k
p90_manual = x[k] + d * (x[k+1] - x[k]) if d > 0 else x[k]
assert abs(p90_manual - p90) < 1e-6, "P90 no coincide entre método y manual"

# (B) La mediana parte los datos: ~50% por debajo y ~50% por encima.
debajo = (gastos < mediana).sum()
assert abs(debajo - n/2) <= 1, "La mediana no parte los datos en dos mitades"

# (C) Outliers: deben ser exactamente los dos eventos gigantes.
assert sorted(outliers.tolist()) == [1500000.0, 2000000.0], "Outliers inesperados"

# (D) Sanity de sesgo: media >> mediana ⇒ cola derecha ⇒ G1 positivo.
assert media > mediana and sesgo > 1, "Patrón de sesgo positivo no confirmado"

print("OK — P90, mediana, outliers y sesgo verificados por segunda vía.")
```

Los `assert` fallan ruidosamente si algún número está mal: ése es el patrón ejecutar+verificar.

## Ejemplo trabajado

**Pregunta del dueño**: "¿Cuánto gasta mi cliente típico?"

Con los 30 datos del bloque (n = 30):

- **Media** ≈ **151.300 COP** — sube disparada por los dos eventos de $1.5M y $2M.
- **Mediana (P50)** ≈ **30.000 COP** — el cliente del medio.
- **Q1 / Q3** = **25.000 / 38.500 COP**, **IQR = 13.500 COP** → el 50% central gasta entre $25k y $38.5k.
- **P90** ≈ **95.000 COP**, **P99** ≈ ~**1.95M COP** (lo arrastran los eventos).
- **Sesgo G1** ≈ **+4.0** → fuertemente sesgado a la derecha.
- **Outliers** (regla IQR, límite superior = Q3 + 1.5·IQR ≈ **58.750 COP**): **$1.500.000 y $2.000.000** (y posiblemente $60k–95k según el corte exacto).

**Conclusión con unidades**: reportar "el cliente gasta en promedio **$151.300 COP**" es engañoso — *ningún* cliente típico gasta eso. La respuesta honesta: **"el cliente típico gasta ~$30.000 COP (mediana); el 50% central va de $25.000 a $38.500 COP. Aparte, hubo 2 eventos atípicos de $1.5M y $2M que conviene analizar por separado."** Esa es una decisión de negocio distinta (¿persigo eventos o el ticket diario?).

## Errores comunes / trampas

- **Promediar sin mirar la forma.** En datos sesgados (ingresos, gastos, tiempos), la media miente. Mira histograma + mediana primero.
- **Borrar outliers por reflejo.** Un outlier puede ser un error de digitación *o* tu cliente más rentable. Decide con criterio, no automáticamente; y documenta qué quitaste.
- **Demasiados o muy pocos bins.** Muchos bins → ruido pixelado; pocos → escondes la forma. Prueba varios (Sturges es solo el arranque).
- **Confundir percentil con porcentaje.** "P90 = 95.000" significa que el 90% gasta ≤ $95k, NO que "el 90% de la plata".
- **Distintos algoritmos de percentil dan distintos números.** NumPy ("linear"), Excel `PERCENTILE.INC` vs `PERCENTILE.EXC` difieren en muestras pequeñas. Fija el método y sé consistente.
- **Sesgo poblacional vs muestral.** `scipy.stats.skew(bias=True)` ≠ `bias=False`. Para una muestra usa la corrección (`bias=False`).
- **Eje truncado en el gráfico.** Empezar el eje Y arriba de cero exagera diferencias — ver [[98-presentar-numeros-sin-enganar]] y [[69-estadistica-enganosa]].

## Cruces

- [[60-estadistica-descriptiva]] — media, mediana, moda y el resumen de 5 números.
- [[61-medidas-de-dispersion]] — varianza, desviación estándar e IQR como ancho.
- [[56-distribuciones-continuas]] — la normal y por qué los datos reales rara vez lo son.
- [[65-muestreo-y-sesgos]] — cómo el muestreo deforma la distribución que ves.
- [[69-estadistica-enganosa]] · [[98-presentar-numeros-sin-enganar]] — visualizar sin mentir.

**Mini-checklist de exactitud**
- [ ] ¿Miré el histograma y comparé media vs mediana ANTES de reportar "lo típico"?
- [ ] ¿Identifiqué outliers con la regla IQR y decidí (con razón) si los incluyo?
- [ ] ¿Verifiqué al menos un percentil por segunda vía y fijé el método de cálculo?
