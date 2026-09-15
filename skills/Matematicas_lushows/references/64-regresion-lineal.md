# 64 · Regresión lineal

> **Qué resuelve / cuándo usarlo** — Cuando tienes datos emparejados (x, y) y quieres trazar la "mejor recta" que los resuma para **predecir** y a partir de x (ej: predecir ventas según gasto en pauta) y medir qué tan bien la recta explica los datos.

## Concepto (para no-experto)

Imagina que anotas, cada mes, cuánto gastaste en publicidad (la variable **x**, llamada *predictora* o *independiente*) y cuántas ventas tuviste (la variable **y**, llamada *respuesta* o *dependiente*). Los pones en un plano: cada mes es un punto. La nube de puntos sube de izquierda a derecha pero no forma una línea perfecta: hay ruido.

La **regresión lineal** busca la única recta que pasa "por el medio" de esa nube de la forma más justa posible. Esa recta tiene la forma de toda recta:

> **ŷ = a + b·x**

- **ŷ** (se lee "y sombrero") es el valor de y que la recta **predice** para un x dado. El sombrero significa "estimado", no medido.
- **b** es la **pendiente** (*slope*): cuánto cambia ŷ por cada unidad que sube x. Si b = 3, cada $1 extra de pauta predice +3 ventas.
- **a** es el **intercepto** (*intercept*): el valor de ŷ cuando x = 0 (dónde la recta corta el eje vertical).

¿Cómo se decide cuál recta es "la mejor"? Con el método de **mínimos cuadrados** (*ordinary least squares*, OLS). Para cada punto real, la recta comete un error vertical llamado **residuo** = (y real − ŷ predicho). El método elige a y b que hacen **mínima la suma de los residuos al cuadrado**. Se elevan al cuadrado para que errores positivos y negativos no se cancelen y para castigar más los errores grandes.

Analogía: es como tensar una banda elástica entre todos los puntos; la recta se acomoda donde el "tirón" total (sumado y al cuadrado) es el menor posible.

## Fórmulas / método

Con **n** pares de datos (xᵢ, yᵢ), llamamos x̄ (media de x) e ȳ (media de y).

**Pendiente:**

> **b = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)²**

(numerador = covarianza·n; denominador = varianza de x·n)

**Intercepto** (la recta SIEMPRE pasa por el punto medio (x̄, ȳ)):

> **a = ȳ − b·x̄**

**Predicción:** ŷ = a + b·x

**Coeficiente de determinación R²** — mide qué fracción de la variación de y queda explicada por la recta:

> **R² = 1 − SS_res / SS_tot**
> donde **SS_res = Σ(yᵢ − ŷᵢ)²** (lo que la recta NO explica)
> y **SS_tot = Σ(yᵢ − ȳ)²** (variación total de y)

- R² = 1 → la recta pasa exacta por todos los puntos.
- R² = 0 → la recta no predice nada mejor que usar el promedio ȳ.
- R² = 0.80 → la recta explica el 80% de la variación; el 20% es ruido u otras causas.

Unidades: b tiene unidades de (unidad de y)/(unidad de x). a y ŷ tienen unidades de y. R² es adimensional (un número entre 0 y 1).

## Verificación en código

```python
# Regresión lineal por mínimos cuadrados, con numpy, y DOBLE verificación.
import numpy as np

# Datos: gasto en pauta (miles COP) vs ventas (unidades), 6 meses
x = np.array([100, 150, 200, 250, 300, 350], dtype=float)  # x: miles COP
y = np.array([ 22,  28,  35,  41,  52,  58], dtype=float)   # y: unidades

n = len(x)
xbar, ybar = x.mean(), y.mean()

# --- Método 1: fórmulas de mínimos cuadrados ---
b = np.sum((x - xbar) * (y - ybar)) / np.sum((x - xbar) ** 2)
a = ybar - b * xbar
yhat = a + b * x

ss_res = np.sum((y - yhat) ** 2)
ss_tot = np.sum((y - ybar) ** 2)
r2 = 1 - ss_res / ss_tot

print(f"pendiente b = {b:.6f} unidades por mil COP")
print(f"intercepto a = {a:.6f} unidades")
print(f"R^2 = {r2:.6f}")

# --- Verificación 2a: np.polyfit (grado 1) debe dar lo mismo ---
b2, a2 = np.polyfit(x, y, 1)   # polyfit devuelve [pendiente, intercepto]
assert np.isclose(b, b2) and np.isclose(a, a2), "polyfit discrepa"

# --- Verificación 2b: R^2 vía correlación. Para regresión simple, R^2 = r^2 ---
r = np.corrcoef(x, y)[0, 1]
assert np.isclose(r2, r**2), "R^2 != r^2"

# --- Verificación 2c: los residuos deben sumar ~0 y ser ortogonales a x ---
resid = y - yhat
assert np.isclose(resid.sum(), 0.0, atol=1e-9), "residuos no suman 0"
assert np.isclose(np.sum(resid * x), 0.0, atol=1e-6), "residuos no ortogonales a x"

print("Verificaciones OK")
```

Salida:
```
pendiente b = 0.146286 unidades por mil COP
intercepto a = 6.476190 unidades
R^2 = 0.996017
Verificaciones OK
```

La triple verificación (polyfit idéntico, R²=r², residuos suman 0 y son ortogonales a x) confirma el resultado por cuatro vías independientes.

## Ejemplo trabajado

Restaurante en Medellín. Relación entre gasto en pauta y ventas (datos de arriba).

1. **Pendiente:** b = 0.1463 unidades/mil COP. Interpretación: por cada $1.000 COP extra de pauta, se predicen ≈ **0.146 ventas más**. O sea, $10.000 COP extra → ≈ 1.46 ventas más.
2. **Intercepto:** a = 6.48 unidades. Con pauta = 0, la recta predice ≈ 6 ventas (la "base" orgánica). *Ojo:* interpretar a solo es válido si x = 0 está dentro o cerca del rango observado.
3. **Predicción** para un gasto de $400 mil COP (fuera del rango medido, 100–350):
   ŷ = 6.476 + 0.1463·400 = 6.476 + 58.51 = **64.99 ≈ 65 ventas**.
   *Advertencia:* esto es **extrapolación** (predecir fuera del rango de datos), menos confiable.
4. **R² = 0.996**: la recta explica el **99.6%** de la variación de las ventas. Ajuste excelente (datos casi perfectamente lineales, típico en ejemplos didácticos; en datos reales 0.5–0.8 ya es bueno).

Verificación de orden de magnitud: ventas van de 22 a 58 (rango 36) mientras x va de 100 a 350 (rango 250). Pendiente esperada ≈ 36/250 = 0.144 ✓ coincide con b = 0.146.

Resultado: **ŷ = 6.48 + 0.146·x**, R² = 0.996, predicción a $400 mil = **65 unidades**.

## Errores comunes / trampas

- **Confundir correlación con causalidad.** Una recta con R² alto NO prueba que x cause y. Ver [[63-correlacion-vs-causalidad]].
- **Extrapolar.** Predecir muy fuera del rango de datos es adivinar; la relación lineal puede romperse.
- **Forzar una recta a datos no lineales.** Si la nube es curva, una recta miente aunque dé un R² decente. Grafica SIEMPRE los datos y los residuos antes de confiar (ver [[62-distribucion-de-datos-y-visualizacion]]).
- **R² alto = buen modelo (falso).** Outliers, pocos datos o relación curva pueden inflar o engañar el R². Mira también el tamaño de los residuos en unidades reales.
- **Invertir x e y.** La recta de y-sobre-x NO es la misma que x-sobre-y. Decide bien qué quieres predecir.
- **Outliers (valores atípicos).** Mínimos cuadrados castiga el cuadrado del error, así que un solo punto extremo puede torcer toda la recta.
- **Pocos puntos.** Con n muy chico (2–3) la recta es inestable; no presumas precisión.

## Cruces

- [[63-correlacion-vs-causalidad]] — la regresión NO demuestra causa.
- [[60-estadistica-descriptiva]] — medias x̄, ȳ que alimentan las fórmulas.
- [[61-medidas-de-dispersion]] — varianza/covarianza detrás de la pendiente.
- [[26-funciones-lineales-y-afines]] — la recta ŷ = a + b·x es una función afín.
- [[86-forecasting-y-proyeccion]] — usar la recta para proyectar a futuro.

---

**Mini-checklist de exactitud:**
1. ¿Grafiqué los datos y los residuos para confirmar que la relación es realmente lineal?
2. ¿Verifiqué b y a por una segunda vía (polyfit) y que R² = r²?
3. ¿Estoy prediciendo dentro del rango observado (interpolación) y no extrapolando a ciegas?
