# 45 · Aplicaciones de la integral

> **Qué resuelve / cuándo usarlo** — Cuando algo se acumula con el tiempo (ingresos, costos, demanda, llenado de un tanque) o cuando necesitas el promedio de una cantidad que cambia continuamente. La integral suma todos esos pedacitos para darte el total acumulado o el valor medio.

## Concepto (para no-experto)

Una **integral definida** es, en palabras simples, la suma de un montón de rebanadas finísimas. Si tienes una función `f(t)` que dice "cuánto vale algo en cada instante `t`" (por ejemplo, cuántos pesos por día entran a tu negocio), la integral entre dos tiempos `a` y `b` te da el **total acumulado** en ese período.

La analogía clásica: imagina el velocímetro de un carro (eso es la *tasa* o *ritmo*, en km/h). La distancia que recorriste (lo *acumulado*, en km) es la integral de la velocidad en el tiempo. La integral convierte un **ritmo** en un **total**.

Tres usos prácticos que cubre este módulo:

1. **Área acumulada bajo una curva** — el "total" geométrico entre la curva `f(t)` y el eje horizontal. Si `f(t)` es un ritmo, esa área *es* el total acumulado. Definimos **área con signo**: lo que está por encima del eje suma, lo que está por debajo resta.

2. **Acumulación de ingresos/costos en el tiempo** — si tus ingresos diarios cambian (un lanzamiento que crece, una temporada que cae), no puedes multiplicar "ingreso por día × días"; tienes que integrar la curva real.

3. **Valor promedio de una función** — el "nivel parejo" que, mantenido constante durante todo el período, daría el mismo total acumulado. Es el promedio de algo que varía a cada instante, no el promedio de unos pocos puntos sueltos.

**Términos definidos la primera vez:**
- **Integral definida** `∫ₐᵇ f(t) dt`: suma continua de `f(t)` desde `t=a` hasta `t=b`. El símbolo `∫` es una "S" estirada de *Suma*; `dt` indica que sumamos en pasitos infinitesimales de la variable `t`.
- **Integrando**: la función `f(t)` que está dentro de la integral.
- **Límites de integración**: `a` (inferior) y `b` (superior), el intervalo donde acumulas.
- **Antiderivada / primitiva** `F(t)`: una función cuya derivada es `f(t)`. Es la herramienta para resolver la integral a mano.

## Fórmulas / método

**1. Teorema Fundamental del Cálculo (cómo se evalúa una integral exacta):**
```
∫ₐᵇ f(t) dt = F(b) − F(a)      donde F'(t) = f(t)
```
`F` es la antiderivada de `f`. Evalúas en el límite superior, restas el límite inferior.

**2. Área acumulada (con signo):**
```
Área_con_signo = ∫ₐᵇ f(t) dt
Área_geométrica (total real) = ∫ₐᵇ |f(t)| dt
```
Usa el valor absoluto `|f(t)|` cuando quieres área física total y la curva cruza el eje.

**3. Ingreso/costo acumulado:**
Si `r(t)` es la **tasa de ingreso** (unidad: $/tiempo), el ingreso total entre `a` y `b` es:
```
Ingreso = ∫ₐᵇ r(t) dt        [$/día · día = $]
```
Las **unidades del integrando se multiplican por las unidades de `dt`**. Esto es un chequeo dimensional crítico: `($/día) × (día) = $`.

**4. Valor promedio de una función en [a, b]:**
```
f̄ = (1 / (b − a)) · ∫ₐᵇ f(t) dt
```
Es el total acumulado dividido por la longitud del intervalo. Unidad: la misma que `f`.

## Verificación en código

Patrón error cero: **una vía simbólica exacta (SymPy) + una segunda vía numérica independiente (SciPy) que debe coincidir**, y el dinero con `Decimal`.

```python
import sympy as sp
from scipy import integrate as sci
from decimal import Decimal, ROUND_HALF_UP

# --- Caso: tasa de ingreso diaria de un lanzamiento ---
# r(t) = 400000 + 60000*t  (pesos COP por dia), t en dias, de t=0 a t=30
t = sp.symbols('t', real=True, nonnegative=True)
r = 400000 + 60000*t                      # $/dia

# VIA 1: integral simbolica EXACTA (Teorema Fundamental del Calculo)
ingreso_exacto = sp.integrate(r, (t, 0, 30))   # resultado en pesos
print("Ingreso exacto (simbolico):", ingreso_exacto)   # 39000000

# Valor promedio de la tasa en [0,30]
prom = ingreso_exacto / (30 - 0)
print("Tasa promedio ($/dia):", prom)                  # 1300000

# --- VERIFICACION POR SEGUNDA VIA: cuadratura numerica independiente ---
f = sp.lambdify(t, r, 'numpy')
ingreso_num, err = sci.quad(f, 0, 30)
print("Ingreso numerico (SciPy):", ingreso_num, "err:", err)
assert abs(float(ingreso_exacto) - ingreso_num) < 1e-3, "Las dos vias NO coinciden!"

# --- VERIFICACION 3: media de tasa lineal = promedio de extremos ---
# Para una recta, el valor medio es (r(a)+r(b))/2  (regla del trapecio exacta)
r0 = r.subs(t, 0); r30 = r.subs(t, 30)
assert prom == (r0 + r30)/2, "El promedio de una recta debe ser la media de extremos"
print("OK: promedio recta = media de extremos =", (r0 + r30)/2)

# --- Redondeo a peso UNA sola vez, al final, con Decimal ---
ingreso_cop = Decimal(int(ingreso_exacto)).quantize(Decimal('1'), ROUND_HALF_UP)
print("Ingreso total redondeado:", f"$ {ingreso_cop:,} COP")  # $ 39,000,000 COP
```

Salida esperada: `Ingreso exacto: 39000000`, `Tasa promedio: 1300000`, la cuadratura numérica coincide (`assert` pasa) y el promedio de la recta = media de extremos `(400000+2200000)/2 = 1300000`. Tres vías de acuerdo.

## Ejemplo trabajado

**Problema (LatAm).** GastroLatam lanza la Calculadora de Costos. Las ventas diarias crecen los primeros 30 días según `r(t) = 400.000 + 60.000·t` (pesos COP por día), donde `t` va de 0 a 30 días. ¿Cuánto se factura en total el primer mes y cuál es la facturación promedio diaria?

**Paso 1 — Plantear la integral del total acumulado.**
```
Ingreso = ∫₀³⁰ (400000 + 60000·t) dt          [$/día · día = $]
```

**Paso 2 — Antiderivada (Teorema Fundamental).**
```
F(t) = 400000·t + 60000·(t²/2) = 400000·t + 30000·t²
```

**Paso 3 — Evaluar F(30) − F(0).**
```
F(30) = 400000·30 + 30000·30² = 12.000.000 + 30000·900 = 12.000.000 + 27.000.000 = 39.000.000
F(0)  = 0
Ingreso = 39.000.000 − 0 = 39.000.000 COP
```

**Paso 4 — Valor promedio diario.**
```
r̄ = Ingreso / (30 − 0) = 39.000.000 / 30 = 1.300.000 COP/día
```

**Paso 5 — Verificación independiente (sanity check de orden de magnitud).** La tasa va de `r(0)=400.000` a `r(30)=2.200.000`. Como es una recta, el promedio debe ser justo el punto medio: `(400.000 + 2.200.000)/2 = 1.300.000 COP/día`. ✅ Coincide con el Paso 4. Y `1.300.000 × 30 = 39.000.000` ✅ recupera el total (operación inversa).

**Resultado:** **$ 39.000.000 COP** facturados el primer mes; **$ 1.300.000 COP/día** en promedio. Con unidades verificadas y triple chequeo.

## Errores comunes / trampas

- **Multiplicar tasa × tiempo cuando la tasa cambia.** Si `r(t)` no es constante, `r·t` está mal; hay que integrar. Solo si es plana coinciden.
- **Confundir tasa con total.** `r(t)` está en $/día (ritmo); la integral está en $ (acumulado). Si las unidades del resultado no son las que esperas, revisa el integrando.
- **Olvidar el límite inferior** `F(a)`. La integral definida es `F(b) − F(a)`, no solo `F(b)`. Solo si `F(0)=0` parece que no importa, pero hay que escribirlo.
- **Área vs. área con signo.** Si la curva cruza el eje (p. ej. flujo de caja con meses negativos), `∫f` da el neto; para el área física total necesitas `∫|f|`. Decide cuál quieres.
- **Promedio de puntos ≠ valor promedio de la función.** Promediar 3 muestras no es lo mismo que `(1/(b−a))∫f dt`; el segundo pondera *toda* la curva.
- **Redondear antes de integrar / en pasos intermedios.** Redondea una sola vez al final; el dinero con `Decimal`, nunca `float`.
- **Confiar en la cuadratura numérica para funciones con saltos.** `quad` puede fallar con discontinuidades; divide el intervalo en los puntos de quiebre.

## Cruces

- [[44-integrales]] — qué es una integral y cómo se calcula la antiderivada (base de este módulo).
- [[41-derivadas-concepto]] — la operación inversa: la derivada convierte total en ritmo, la integral ritmo en total.
- [[78-flujo-de-caja-y-presupuesto]] — acumular ingresos y egresos en el tiempo (versión discreta de lo mismo).
- [[86-forecasting-y-proyeccion]] — proyectar la curva `r(t)` que luego se integra.
- [[19-secuencias-y-series]] — la versión discreta (sumatoria) de la acumulación continua.

---

**Mini-checklist de exactitud:**
1. ¿Las unidades del resultado son las del integrando × las de `dt`? (p. ej. $/día × día = $).
2. ¿Confirmé el total por una segunda vía (cuadratura numérica, operación inversa o media de extremos si es recta)?
3. ¿Redondeé el dinero una sola vez al final con `Decimal`, no en pasos intermedios?
