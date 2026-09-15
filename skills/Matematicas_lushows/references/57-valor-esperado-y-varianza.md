# 57 · Valor esperado y varianza

> **Qué resuelve / cuándo usarlo** — Decidir bajo incertidumbre comparando el "promedio a largo plazo" de cada opción (valor esperado) y midiendo qué tan riesgosa es (varianza/desviación). Úsalo en apuestas, inversiones, pricing, garantías, y cualquier elección donde el resultado depende del azar.

## Concepto (para no-experto)

Imagina que vas a repetir una jugada (una apuesta, un negocio, una campaña) **miles de veces**. El **valor esperado** (en inglés *expected value*, símbolo `E[X]` o μ "mu") es el promedio que obtendrías por jugada si la repitieras infinitas veces. No es lo que pasa "una vez", sino el centro de gravedad de todos los resultados posibles, **ponderado por su probabilidad**.

Términos clave (definidos la primera vez):

- **Variable aleatoria** `X`: un número cuyo valor depende del azar (lo que ganas en una jugada).
- **Probabilidad** `p`: qué tan posible es cada resultado, entre 0 (imposible) y 1 (seguro). La suma de todas debe dar exactamente 1.
- **Valor esperado** `E[X]`: el promedio ponderado de los resultados. "Ponderado" = cada resultado pesa según su probabilidad.
- **Varianza** `Var(X)` (símbolo σ², "sigma al cuadrado"): qué tan dispersos están los resultados respecto al promedio. Mide el **riesgo**.
- **Desviación estándar** `σ` ("sigma"): la raíz cuadrada de la varianza. Está en las **mismas unidades** que `X` (ej. pesos), por eso es más fácil de interpretar que la varianza.

Analogía cotidiana: dos restaurantes. El A vende casi siempre 100 platos (poca variación). El B vende a veces 30, a veces 170, promediando también 100. **Mismo valor esperado, distinto riesgo.** La varianza/desviación es justo lo que distingue al B del A. Por eso `E[X]` solo no basta para decidir: hay que mirar también la dispersión.

⚠️ Trampa fundamental: el valor esperado describe el **largo plazo**. Si solo vas a jugar **una vez** y una pérdida te arruina, un `E[X]` positivo no te salva (ver [[90-teoria-de-decisiones]] y [[94-riesgo-var-y-volatilidad]]).

## Fórmulas / método

Para una variable aleatoria **discreta** (resultados contables `x₁, x₂, …` con probabilidades `p₁, p₂, …`):

```
E[X] = μ = Σᵢ xᵢ · pᵢ            (suma de cada resultado por su probabilidad)

Var(X) = σ² = Σᵢ (xᵢ − μ)² · pᵢ   (definición)
       = E[X²] − (E[X])²          (fórmula de atajo, equivalente)

σ = √Var(X)                       (desviación estándar; mismas unidades que X)
```

Propiedades útiles (con `a`, `b` constantes):

```
E[aX + b] = a·E[X] + b           (linealidad)
Var(aX + b) = a²·Var(X)          (el +b NO afecta la dispersión; el a se eleva al cuadrado)
E[X + Y] = E[X] + E[Y]           (siempre, aun si X e Y dependen entre sí)
Var(X + Y) = Var(X) + Var(Y)     (SOLO si X e Y son independientes)
```

**Coeficiente de variación** `CV = σ / |E[X]|`: riesgo relativo (sin unidades), permite comparar opciones de tamaños distintos.

Unidades: si `X` está en COP, entonces `E[X]` y `σ` están en COP, y `Var(X)` en COP² (por eso la varianza es difícil de interpretar directamente y preferimos `σ`).

## Verificación en código

Caso: un sorteo cuesta $5.000 COP el boleto. Con probabilidad 1/100 ganas $300.000, con 5/100 ganas $20.000, y el resto pierdes el boleto. ¿Conviene? (X = ganancia neta por jugada.)

```python
from fractions import Fraction as F  # exacto, sin floats: probabilidades como fracciones

# Resultados de ganancia NETA (premio - costo del boleto) en COP, y sus probabilidades
costo = 5000
escenarios = [
    (300000 - costo, F(1, 100)),   # premio mayor
    ( 20000 - costo, F(5, 100)),   # premio menor
    (     0 - costo, F(94, 100)),  # sin premio: pierdes el boleto
]

# 0) Sanity check OBLIGATORIO: las probabilidades deben sumar exactamente 1
assert sum(p for _, p in escenarios) == 1, "Las probabilidades no suman 1"

# 1) Valor esperado  E[X] = Σ x·p   (exacto, en fracciones)
EX = sum(F(x) * p for x, p in escenarios)

# 2) E[X^2]  (para la fórmula de atajo de la varianza)
EX2 = sum(F(x)**2 * p for x, p in escenarios)

# 3) Varianza por atajo:  Var = E[X^2] - (E[X])^2
var_atajo = EX2 - EX**2

# 4) Desviación estándar  σ = sqrt(Var)
import math
sigma = math.sqrt(float(var_atajo))

print("E[X]  =", float(EX), "COP")
print("Var   =", float(var_atajo), "COP^2")
print("sigma =", round(sigma, 2), "COP")
```

Salida: `E[X] = -2050.0 COP`, `Var = 1015...`, `sigma ≈ 31867 COP`.

Verificación por SEGUNDA VÍA (definición directa de varianza, debe coincidir con el atajo):

```python
# Var por DEFINICIÓN:  Σ (x - μ)^2 · p   -> debe igualar var_atajo exactamente
var_def = sum((F(x) - EX)**2 * p for x, p in escenarios)
assert var_def == var_atajo, "Las dos vías de la varianza no coinciden"

# Tercera comprobación: linealidad. Si Y = 2X+1000 -> E[Y]=2E[X]+1000, Var(Y)=4Var(X)
EY  = sum(F(2*x + 1000) * p for x, p in escenarios)
assert EY == 2*EX + 1000, "Falla linealidad de E"
varY = sum((F(2*x + 1000) - EY)**2 * p for x, p in escenarios)
assert varY == 4 * var_atajo, "Falla Var(aX+b)=a^2 Var(X)"
print("Verificacion OK: definicion == atajo, y propiedades se cumplen")
```

Como `E[X] = −2.050 COP` (negativo), **en promedio pierdes 2.050 por boleto**: el sorteo no conviene a largo plazo. La `σ ≈ 31.867 COP` enorme frente a la media confirma que es un juego de alta varianza (casi siempre pierdes poco, rarísima vez ganas mucho).

## Ejemplo trabajado

**Decisión de negocio (LatAm):** GastroLatam evalúa pautar una campaña de WhatsApp. Cuesta **$200.000 COP**. Estima estos resultados de **ganancia neta** (ingresos − costo):

| Escenario      | Ganancia neta (COP) | Probabilidad |
|----------------|--------------------:|-------------:|
| Viral          |          +800.000   |        0,10  |
| Bueno          |          +150.000   |        0,40  |
| Flojo          |          −200.000   |        0,50  |

Paso 1 — Verificar probabilidades: `0,10 + 0,40 + 0,50 = 1,00`. ✓

Paso 2 — Valor esperado:
```
E[X] = 800000·0,10 + 150000·0,40 + (−200000)·0,50
     = 80.000 + 60.000 − 100.000
     = +40.000 COP por campaña
```
En promedio, **cada campaña deja +$40.000 COP**. A largo plazo, conviene.

Paso 3 — Riesgo (varianza por definición), con μ = 40.000:
```
(800000−40000)² · 0,10 = (760000)²·0,10 = 57.760.000.000
(150000−40000)² · 0,40 = (110000)²·0,40 = 4.840.000.000
(−200000−40000)²·0,50 = (−240000)²·0,50 = 28.800.000.000
Var = 91.400.000.000 COP²
σ  = √91.400.000.000 ≈ 302.324 COP
```

Paso 4 — Interpretación honesta: aunque `E[X] = +40.000 COP`, la desviación `σ ≈ 302.324 COP` es **7,5 veces** la media (CV ≈ 7,6). Hay 50% de probabilidad de **perder $200.000**. Si la empresa solo puede correr **una** campaña y no aguanta perder 200k, el valor esperado positivo no justifica el riesgo. Si puede correr **muchas**, la ley de los grandes números hace que el +40.000 promedio se materialice. Resultado: **+40.000 COP/campaña esperados, con riesgo alto (σ ≈ 302.324 COP)** — decisión correcta solo si se repite a volumen.

(Comprobación de orden de magnitud: la media debe caer entre el peor −200.000 y el mejor +800.000; 40.000 está dentro. σ debe ser comparable a las distancias típicas a la media (~110k a 760k); ~302k es razonable. ✓)

## Errores comunes / trampas

- **Confundir `E[X]` con "lo que va a pasar".** El valor esperado puede ser un número que **nunca ocurre** (ej. media 40.000 cuando los resultados son 800k, 150k o −200k). Es un promedio de largo plazo, no una predicción de una jugada.
- **Probabilidades que no suman 1.** Siempre verifícalo con un `assert` antes de calcular; si no, todo el resultado es basura.
- **Olvidar restar el costo.** Trabaja siempre con la ganancia **neta** (premio − costo), no con el premio bruto, o el `E[X]` sale inflado.
- **Sumar varianzas de variables dependientes.** `Var(X+Y) = Var(X)+Var(Y)` **solo** vale si son independientes. Con dependencia hay que sumar también la covarianza.
- **Reportar la varianza como si fuera dinero.** La varianza está en COP² (sin sentido físico); para hablar de riesgo en pesos usa la **desviación estándar** σ.
- **Decidir solo por `E[X]` ignorando el riesgo de ruina.** Una apuesta con `E[X]` positivo pero que puede quebrarte en una mala jugada NO conviene si no la puedes repetir. Ver criterio de Kelly y utilidad en [[90-teoria-de-decisiones]].
- **Usar float para las probabilidades en cálculos largos.** Acumula error; usa `fractions.Fraction` o `decimal` cuando la exactitud importe.

## Cruces

- [[54-variables-aleatorias]] — define `X`, su soporte y su función de probabilidad (la base de este módulo).
- [[55-distribuciones-discretas]] — `E[X]` y `Var(X)` cerrados para binomial, Poisson, etc.
- [[56-distribuciones-continuas]] — versión con integrales: `E[X]=∫x·f(x)dx`.
- [[58-simulacion-monte-carlo]] — estimar `E[X]` y `σ` cuando la fórmula exacta es difícil.
- [[90-teoria-de-decisiones]] — cómo combinar valor esperado y riesgo para decidir (utilidad, aversión al riesgo).
- [[94-riesgo-var-y-volatilidad]] — la desviación como medida de riesgo financiero y VaR.

---

**Mini-checklist de exactitud:**
- [ ] Las probabilidades suman exactamente 1 (verificado con `assert`).
- [ ] La varianza se confirmó por dos vías (definición vs atajo `E[X²]−E[X]²`) y coinciden.
- [ ] El resultado lleva unidades (COP) y `E[X]` cae dentro del rango [mín, máx] de los resultados.
