# 55 · Distribuciones discretas

> **Qué resuelve / cuándo usarlo** — Cuando cuentas EVENTOS que pasan o no pasan (un sí/no, un número entero de ocurrencias): ¿cuál es la probabilidad de que de 100 visitas compren exactamente 7? ¿de que mañana lleguen 0 pedidos? Las tres reinas son Bernoulli, Binomial y Poisson.

## Concepto (para no-experto)

Una **distribución de probabilidad** es la "tabla de reglas" que dice qué tan probable es cada resultado posible de un experimento al azar. **Discreta** significa que los resultados son CONTABLES con números enteros (0, 1, 2, 3...), no hay decimales en medio: puedes vender 3 productos, nunca 3.7.

Las tres que más vas a usar en un negocio:

- **Bernoulli** — el ladrillo más simple: UN solo intento con dos resultados, "éxito" o "fracaso". Lanzar una moneda una vez. Que UN visitante compre o no compre. Su único parámetro (número que la define) es `p` = probabilidad de éxito. Analogía: una sola raspadita de lotería.

- **Binomial** — repites el MISMO experimento Bernoulli `n` veces, independientes, y cuentas cuántos éxitos hubo en total. De 200 visitantes (cada uno compra con probabilidad `p`), ¿cuántos comprarán? Analogía: comprar 200 raspaditas iguales y contar cuántas premian. Parámetros: `n` (intentos) y `p` (prob. de éxito por intento).

- **Poisson** — cuenta cuántas veces ocurre algo en un intervalo fijo de tiempo o espacio, cuando los eventos son raros y al azar y solo conoces el PROMEDIO. ¿Cuántos pedidos por WhatsApp llegan en una hora si en promedio llegan 4? Analogía: gotas de lluvia cayendo en una baldosa en un minuto. Parámetro único: `λ` (lambda) = promedio de ocurrencias por intervalo.

Regla mental para elegir: **¿uno o muchos?** Uno → Bernoulli. **¿Cuántos éxitos de N intentos con tope conocido?** → Binomial. **¿Cuántos eventos por intervalo sin tope claro, solo el promedio?** → Poisson.

## Fórmulas / método

Notación: `P(X = k)` se lee "probabilidad de que la variable X valga exactamente k". `!` es factorial (`5! = 5·4·3·2·1`). `C(n,k)` es "combinaciones de n en k" = `n! / (k!·(n−k)!)` (ver [[53-combinatoria]]).

**Bernoulli** (k solo puede ser 0 o 1):
```
P(X = 1) = p          P(X = 0) = 1 − p
Media (μ) = p         Varianza (σ²) = p·(1 − p)
```

**Binomial** (k = 0, 1, ..., n):
```
P(X = k) = C(n,k) · p^k · (1 − p)^(n − k)
Media (μ) = n·p       Varianza (σ²) = n·p·(1 − p)
```
Cada símbolo: `n` = número de intentos (entero ≥ 0), `p` = prob. de éxito por intento (0 ≤ p ≤ 1), `k` = número de éxitos cuya probabilidad queremos. Sin unidades (es probabilidad, número puro entre 0 y 1); la media `n·p` está en "número de éxitos".

**Poisson** (k = 0, 1, 2, ... sin tope):
```
P(X = k) = (λ^k · e^(−λ)) / k!
Media (μ) = λ          Varianza (σ²) = λ
```
`λ` (lambda) = promedio de eventos por intervalo (debe ser > 0), `e` = 2.71828... (número de Euler), `k` = número de eventos. Unidad de λ: "eventos por intervalo" (p. ej. pedidos/hora).

Dato clave: en Poisson media y varianza son IGUALES (ambas = λ). En Binomial la varianza siempre es MENOR que la media (porque multiplica por `(1−p) < 1`).

Conexión: la Binomial con `n` grande y `p` chico se aproxima a una Poisson con `λ = n·p`.

## Verificación en código

```python
# scipy es la librería estándar y validada para esto. No calculamos de memoria.
from scipy.stats import bernoulli, binom, poisson
from math import comb, exp, factorial
from decimal import Decimal, getcontext

# ---------- BINOMIAL ----------
# Caso: 200 visitantes, cada uno compra con p = 3% (0.03). P(exactamente 7 compras).
n, p, k = 200, 0.03, 7
prob_scipy = binom.pmf(k, n, p)   # pmf = "probability mass function" = P(X=k)
print("Binomial P(X=7) scipy:", prob_scipy)

# VERIFICACIÓN VÍA 1: fórmula a mano con math.comb (combinaciones exactas en enteros)
prob_manual = comb(n, k) * (p**k) * ((1 - p)**(n - k))
print("Binomial P(X=7) manual:", prob_manual)
assert abs(prob_scipy - prob_manual) < 1e-12, "Binomial no coincide"

# VERIFICACIÓN VÍA 2: la media debe ser n*p y todas las P deben sumar 1
media_teorica = n * p                       # 200 * 0.03 = 6
media_scipy = binom.mean(n, p)
suma_total = sum(binom.pmf(i, n, p) for i in range(n + 1))
assert abs(media_scipy - media_teorica) < 1e-9
assert abs(suma_total - 1.0) < 1e-9, "Las probabilidades no suman 1"
print("Media binomial:", media_teorica, "| suma de todas las P:", round(suma_total, 12))

# ---------- POISSON ----------
# Caso: en promedio llegan 4 pedidos/hora. P(exactamente 0 pedidos en una hora).
lam, k2 = 4, 0
pois_scipy = poisson.pmf(k2, lam)
pois_manual = (lam**k2) * exp(-lam) / factorial(k2)   # = e^(-4)
print("Poisson P(X=0) scipy:", pois_scipy, "| manual:", pois_manual)
assert abs(pois_scipy - pois_manual) < 1e-12, "Poisson no coincide"

# VERIFICACIÓN VÍA 2 (Poisson): media == varianza == lambda
assert abs(poisson.mean(lam) - poisson.var(lam)) < 1e-9
assert abs(poisson.mean(lam) - lam) < 1e-9
print("Poisson media == varianza == lambda:", poisson.mean(lam), poisson.var(lam))

# ---------- VERIFICACIÓN POR SIMULACIÓN (tercera vía, Monte Carlo) ----------
import numpy as np
rng = np.random.default_rng(42)              # semilla fija = reproducible
N = 2_000_000
sim = rng.binomial(n, p, size=N)             # 2M experimentos de 200 visitantes
frac_7 = np.mean(sim == 7)                    # fracción que dio exactamente 7
print("Binomial P(X=7) simulado:", frac_7, "vs teórico:", prob_scipy)
# Con 2M repeticiones el error esperado es ~1e-4; debe pegar en 2-3 decimales:
assert abs(frac_7 - prob_scipy) < 5e-4, "La simulación no respalda la teoría"
print("OK: teoria, formula a mano y simulacion coinciden.")
```

Nota sobre dinero: las probabilidades son números puros (no dinero), por eso uso float aquí; cuando conviertas una probabilidad en pesos esperados (p. ej. `compras_esperadas · precio`), pasa a `decimal` para el monto final (ver [[12-fracciones-decimales-y-precision]]).

## Ejemplo trabajado

**Negocio (GastroLatam):** El bot atiende **200 leads** en una campaña. Históricamente **3 de cada 100** terminan comprando la Calculadora a **$10.000 COP**. Preguntas del dueño: (a) ¿cuántas ventas espero? (b) ¿probabilidad de tener AL MENOS 10 ventas? (c) ¿cuántos pesos espero facturar?

Esto es **Binomial**: `n = 200` intentos independientes, `p = 0.03`.

Paso 1 — Ventas esperadas (media):
```
μ = n·p = 200 × 0.03 = 6 ventas
```

Paso 2 — P(al menos 10 ventas) = `P(X ≥ 10) = 1 − P(X ≤ 9)`:
```python
from scipy.stats import binom
from decimal import Decimal, ROUND_HALF_UP
n, p, precio = 200, 0.03, Decimal("10000")
p_al_menos_10 = 1 - binom.cdf(9, n, p)   # cdf(9) = P(X ≤ 9)
print(p_al_menos_10)                      # ≈ 0.08385  -> 8.39%

# Verificación inversa: P(X>=10) + P(X<=9) debe ser 1
assert abs((1 - binom.cdf(9, n, p)) + binom.cdf(9, n, p) - 1) < 1e-12

# Paso 3 — facturación esperada, AHORA sí con decimal (es dinero)
ventas_esp = Decimal(str(n)) * Decimal(str(p))            # 6.00 ventas
ingreso_esp = (ventas_esp * precio).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print(ingreso_esp)                                         # 60000
```

**Resultados:**
- (a) Ventas esperadas = **6 ventas** (en promedio).
- (b) P(al menos 10 ventas) ≈ **8.39 %** — poco probable superar el promedio por tanto; útil para fijar expectativas realistas.
- (c) Facturación esperada = **$60.000 COP** (6 ventas × $10.000). Redondeo aplicado UNA sola vez al final.

## Errores comunes / trampas

- **Confundir Binomial con Poisson.** Si hay un tope claro de intentos (`n` visitantes), es Binomial. Si solo conoces un promedio por intervalo sin tope ("4 pedidos/hora"), es Poisson. Elegir mal cambia la varianza y por tanto los riesgos.
- **Sumar λ de intervalos distintos sin escalar.** Si llegan 4 pedidos/hora y quieres 3 horas, usa `λ = 12`, no `λ = 4`. Poisson escala linealmente con el intervalo.
- **Olvidar la independencia.** Binomial y Poisson asumen que los eventos no se influyen. Si una promo viral hace que las compras se "contagien", el modelo subestima la varianza (sobre-dispersión); ahí mira binomial negativa, fuera de este módulo.
- **`P(X = k)` vs `P(X ≤ k)`.** `pmf` es exactamente k; `cdf` es k o menos. Para "al menos k" usa `1 − cdf(k−1)`, NO `1 − cdf(k)`.
- **Calcular factoriales gigantes a mano.** `200!` desborda y produce errores; usa `scipy.stats` o `math.comb`, que están optimizados y son exactos en enteros.
- **Usar float para el dinero resultante.** La probabilidad va en float; el peso final va en `decimal`.

## Cruces

- [[54-variables-aleatorias]] — qué es una variable aleatoria y su función de masa (la base de este módulo).
- [[53-combinatoria]] — de dónde sale el `C(n,k)` de la Binomial.
- [[57-valor-esperado-y-varianza]] — cómo se derivan μ y σ² que aquí usamos como atajos.
- [[56-distribuciones-continuas]] — el salto a Normal/Exponencial cuando n es grande (aproximación).
- [[58-simulacion-monte-carlo]] — la tercera vía de verificación por simulación que usamos arriba.

---

**Mini-checklist de exactitud**
- [ ] ¿Elegí la distribución correcta? (uno→Bernoulli; n con tope→Binomial; promedio/intervalo→Poisson)
- [ ] ¿Verifiqué por 2ª vía? (fórmula a mano + suma de P = 1, y/o simulación que pega en 2-3 decimales)
- [ ] ¿La probabilidad quedó en [0,1] y el dinero final en `decimal` redondeado una sola vez?
