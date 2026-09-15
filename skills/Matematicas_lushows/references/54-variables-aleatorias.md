# 54 · Variables aleatorias

> **Qué resuelve / cuándo usarlo** — Convierte un fenómeno con azar (cuántos pedidos llegan, cuánto pesa un saco, si un cliente compra) en un objeto matemático con el que se puede calcular probabilidades, promedios y riesgo. Úsalo cada vez que un número futuro sea incierto y necesites razonar sobre él con rigor en vez de "a ojo".

## Concepto (para no-experto)

Una **variable aleatoria** (VA) es una regla que le asigna un **número** a cada resultado posible de un experimento con azar. No es una variable común (no tiene un valor fijo desconocido): es una función que "traduce a número" lo que pasó.

Ejemplo cotidiano: lanzas dos monedas. Los resultados crudos son `{cara-cara, cara-sello, sello-cara, sello-sello}`. Define `X = número de caras`. Entonces `X` toma valores `0, 1, 2`. Esa `X` es una variable aleatoria: tomó el azar (las monedas) y lo convirtió en números con los que sí puedes hacer cuentas.

Por convención se escriben con **mayúscula** la variable (`X`) y con **minúscula** un valor concreto que puede tomar (`x`). Así `P(X = x)` se lee "probabilidad de que la variable `X` tome el valor `x`".

Hay dos tipos, y la diferencia es **práctica**, no filosófica:

- **Discreta** — toma valores **contables y separados**, normalmente enteros: 0, 1, 2, 3… *Cuántas* cosas. Ej.: pedidos por día, número de reservas, defectos en un lote. Aquí tiene sentido la pregunta "¿cuál es la probabilidad de que sea exactamente 7?".
- **Continua** — toma **cualquier valor dentro de un rango**, con decimales infinitos posibles. *Cuánto* mide algo. Ej.: peso de un saco de café (kg), tiempo de espera (min), temperatura. Aquí "exactamente 7.000000… kg" tiene probabilidad **cero**; solo tiene sentido preguntar por intervalos: "entre 6.9 y 7.1 kg".

La herramienta que describe **cómo se reparte la probabilidad** entre los valores tiene dos nombres según el tipo:

- En discretas: **función de probabilidad** o **función de masa** (PMF, *probability mass function*). Da directamente `P(X = x)`. Imagínala como porciones de una torta: cada valor se lleva un trozo, y todos los trozos suman 1 (= 100 %).
- En continuas: **función de densidad** (PDF, *probability density function*), que se escribe `f(x)`. Ojo: `f(x)` **no** es una probabilidad, es una *densidad* (probabilidad por unidad de `x`). Para obtener una probabilidad debes mirar el **área bajo la curva** en un intervalo. Analogía: la densidad es como cuántas personas por km² hay en un mapa; la "cantidad de gente" (la probabilidad) solo aparece cuando eliges una región y sumas el área.

Así modelan el azar: una VA + su distribución es un "modelo de juguete" del fenómeno real con el que puedes preguntar *qué tan probable es esto* y *cuánto esperar en promedio*, antes de que ocurra.

## Fórmulas / método

**Variable aleatoria discreta — PMF** `p(x) = P(X = x)`:

1. No-negatividad: `p(x) ≥ 0` para todo `x`.
2. Normalización: `Σ_x p(x) = 1` (la suma sobre todos los valores posibles es 1).
3. Probabilidad de un conjunto: `P(X ∈ A) = Σ_{x ∈ A} p(x)`.

**Variable aleatoria continua — PDF** `f(x)`:

1. No-negatividad: `f(x) ≥ 0`.
2. Normalización: `∫_{-∞}^{∞} f(x) dx = 1` (el área total bajo la curva es 1).
3. Probabilidad de un intervalo: `P(a ≤ X ≤ b) = ∫_a^b f(x) dx` (área bajo la curva entre `a` y `b`).
4. Punto exacto: `P(X = c) = 0` (un intervalo de ancho cero tiene área cero).

**Función de distribución acumulada (CDF)** — válida para ambos tipos, `F(x) = P(X ≤ x)`:

- Discreta: `F(x) = Σ_{t ≤ x} p(t)`.
- Continua: `F(x) = ∫_{-∞}^{x} f(t) dt`, y `P(a < X ≤ b) = F(b) − F(a)`.

Símbolos: `X` = variable aleatoria; `x, a, b, c, t` = valores numéricos concretos; `Σ` = suma; `∫` = integral (suma continua = área); `P(·)` = probabilidad (número entre 0 y 1, adimensional). Las **unidades** viven en `x` (kg, min, pedidos); `p(x)` y `P(·)` son adimensionales; `f(x)` tiene unidades de **1/[unidad de x]** (p. ej. 1/kg), justo porque al multiplicar por `dx` (kg) el resultado queda adimensional.

## Verificación en código

```python
# Requisitos de error cero: nada de memoria. Discreta -> fractions (exacto).
# Continua -> sympy integra simbólicamente (exacto, sin error de float).
from fractions import Fraction
import sympy as sp

# ---------- 1) VA DISCRETA: X = número de caras al lanzar 2 monedas justas ----------
# Espacio: CC, CS, SC, SS -> X = 0,1,2 con conteos 1,2,1 sobre 4 resultados.
pmf = {0: Fraction(1, 4), 1: Fraction(2, 4), 2: Fraction(1, 4)}

# (Ley 1) no-negatividad
assert all(p >= 0 for p in pmf.values()), "PMF no puede ser negativa"
# (Ley 2) normalizacion: suma EXACTA = 1
total = sum(pmf.values())
assert total == 1, f"La PMF no suma 1, suma {total}"
print("PMF suma:", total)                        # 1

# P(X >= 1) por la regla del conjunto
p_ge1 = pmf[1] + pmf[2]
print("P(X>=1) =", p_ge1)                         # 3/4

# CDF: F(1) = P(X<=1)
F1 = pmf[0] + pmf[1]
print("F(1) =", F1)                               # 3/4

# ---------- 2) VA CONTINUA: tiempo de espera exponencial, media 5 min ----------
# f(x) = (1/mu) * e^(-x/mu),  x >= 0 ; mu = 5 min
x, mu = sp.symbols('x mu', positive=True)
f = (1/mu) * sp.exp(-x/mu)

# (Ley 2 continua) area total bajo la curva = 1, EXACTO
area_total = sp.integrate(f.subs(mu, 5), (x, 0, sp.oo))
print("Area total PDF:", area_total)              # 1

# P(X <= 5) = integral de 0 a 5  (probabilidad de esperar <= 5 min)
P_le5 = sp.integrate(f.subs(mu, 5), (x, 0, 5))
print("P(X<=5) exacto:", P_le5, "=", float(P_le5))  # 1 - e^-1 ~ 0.6321
```

```python
# ---------- VERIFICACION POR SEGUNDA VIA ----------
# (a) Discreta por SIMULACION (otro metodo): debe acercarse a la PMF teorica.
import random
random.seed(42)
N = 2_000_000
caras = [sum(random.randint(0, 1) for _ in range(2)) for _ in range(N)]
from collections import Counter
c = Counter(caras)
emp = {k: c[k] / N for k in (0, 1, 2)}
print("Empirico:", {k: round(v, 4) for k, v in emp.items()})
# Deben coincidir con 0.25, 0.50, 0.25 a 2 decimales
assert abs(emp[1] - 0.50) < 0.01 and abs(emp[0] - 0.25) < 0.01

# (b) Continua por la CDF cerrada (inversa del calculo): F(x)=1-e^(-x/mu).
import math
P_le5_formula = 1 - math.exp(-5/5)               # 1 - e^-1
assert abs(float(P_le5) - P_le5_formula) < 1e-12, "PDF y CDF no coinciden"
print("P(X<=5) por CDF cerrada:", round(P_le5_formula, 6))  # 0.632121

# (c) Sanity de orden de magnitud: una prob. SIEMPRE en [0,1].
for v in (float(p_ge1), float(P_le5)):
    assert 0 <= v <= 1, "Probabilidad fuera de [0,1] -> error"
print("OK: todo verificado por segunda via")
```

## Ejemplo trabajado

**Caso GastroLatam (dark kitchen, Bogotá).** Los pedidos que entran por hora en la franja de almuerzo se modelan como una VA **discreta** `X`. Por histórico, en promedio llegan `λ = 8` pedidos/hora y se usa la distribución de Poisson (típica para "conteos de eventos por unidad de tiempo"). PMF de Poisson: `p(k) = e^(−λ) · λ^k / k!`, con `k` = 0, 1, 2, … pedidos.

Pregunta de negocio: *¿probabilidad de recibir más de 12 pedidos en una hora?* (sirve para decidir si la cocina aguanta el pico). Es decir `P(X > 12) = 1 − P(X ≤ 12)`.

```python
import sympy as sp
lam = 8
# P(X <= 12) sumando la PMF exacta termino a termino (sin float)
P_le12 = sum(sp.exp(-lam) * sp.Integer(lam)**k / sp.factorial(k) for k in range(13))
P_gt12 = 1 - P_le12
print(float(P_le12), float(P_gt12))   # 0.9362  ,  0.0638
```

Verificación por segunda vía (`scipy`, otra implementación):

```python
from scipy.stats import poisson
import sympy as sp
assert abs(poisson.cdf(12, 8) - float(sum(sp.exp(-8)*sp.Integer(8)**k/sp.factorial(k) for k in range(13)))) < 1e-12
print(round(1 - poisson.cdf(12, 8), 4))   # 0.0638
```

**Resultado:** `P(X > 12 pedidos/hora) ≈ 0,0638 = 6,38 %`. Lectura: aproximadamente 6 de cada 100 horas-almuerzo superan los 12 pedidos. Si eso desborda la cocina, conviene reforzar el turno en horas pico. La unidad de `X` es **pedidos/hora**; la probabilidad es **adimensional**.

## Errores comunes / trampas

- **Tratar `f(x)` como si fuera una probabilidad.** En continuas `f(x)` es densidad (1/unidad) y puede ser **mayor que 1**; no significa "probabilidad > 100 %". La probabilidad es el **área**, no la altura.
- **Preguntar `P(X = c)` en una continua y esperar algo distinto de 0.** Siempre es 0; usa intervalos.
- **Olvidar normalizar.** Si `Σ p(x) ≠ 1` (discreta) o el área ≠ 1 (continua), el modelo está mal y todo número que salga es falso. Verifícalo SIEMPRE como primer assert.
- **Confundir discreta con continua.** "Cantidad de personas" es discreta aunque hagas un promedio decimal (4,3 personas); el modelo de conteo es discreto.
- **Usar float para probabilidades exactas** (sumas de PMF, factoriales): acumula error. Usa `fractions`/`sympy` cuando necesites exactitud, y `scipy` como verificación independiente.
- **`> 12` vs `≥ 12`.** En discretas la frontera importa: `P(X > 12) = 1 − P(X ≤ 12)`, no `1 − P(X < 12)`. Decide el operador desde la pregunta de negocio.

### Mini-checklist de exactitud
- [ ] ¿La PMF suma 1 (o el área de la PDF = 1)? Confirmado en código.
- [ ] ¿Toda probabilidad cae en `[0, 1]` y verifiqué por una segunda vía (simulación / CDF / otra librería)?
- [ ] ¿Las unidades viven en `x` y el resultado de probabilidad quedó adimensional?

## Cruces
- [[50-fundamentos-de-probabilidad]] — base conceptual de probabilidad sobre la que se define toda VA.
- [[55-distribuciones-discretas]] — modelos concretos de PMF (Bernoulli, binomial, Poisson, geométrica).
- [[56-distribuciones-continuas]] — modelos concretos de PDF (uniforme, normal, exponencial).
- [[57-valor-esperado-y-varianza]] — cómo resumir una VA en su promedio y su dispersión.
- [[58-simulacion-monte-carlo]] — verificar y estimar probabilidades muestreando la VA por código.
