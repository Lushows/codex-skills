# 44 · Integrales

> **Qué resuelve / cuándo usarlo** — Cuando necesitas **acumular** algo que cambia con el tiempo o el espacio (área bajo una curva, ingresos totales a partir de una tasa de ventas, costo total a partir de un costo marginal, volumen, distancia recorrida). La integral suma infinitas piezas diminutas en un resultado exacto.

## Concepto (para no-experto)

Imagina que vendes empanadas y tu velocidad de venta cambia durante el día: a las 8am vendes pocas por hora, al mediodía muchas, en la tarde otra vez pocas. Si quisieras saber **cuántas empanadas vendiste en todo el día**, no basta multiplicar "ventas por hora × horas" porque la velocidad no es constante. Necesitas **acumular** la venta hora por hora, minuto a minuto. Eso es una **integral**: la herramienta que suma una cantidad que cambia.

Definamos los términos:

- **Función** `f(x)`: una regla que a cada valor de entrada `x` le asigna un valor de salida (ej. la velocidad de venta a la hora `x`).
- **Integral definida**: el número que resulta de acumular `f(x)` desde un punto `a` hasta un punto `b`. Geométricamente es el **área bajo la curva** de `f` entre `a` y `b`. Se escribe `∫ₐᵇ f(x) dx`.
- **dx**: significa "un pedacito infinitamente pequeño de `x`". La integral suma `f(x)·dx` (alto × ancho de un rectángulo finísimo) infinitas veces.
- **Integral indefinida** o **antiderivada** `F(x)`: la operación **inversa** de la derivada. Si derivar es "sacar la pendiente / la tasa de cambio", integrar es "deshacer eso y recuperar la función acumulada". Se escribe `∫ f(x) dx = F(x) + C`.
- **C (constante de integración)**: al deshacer una derivada perdemos información de cuánto valía la función al inicio, así que aparece una constante desconocida `+ C`. En la integral **definida** esa `C` se cancela y desaparece.

**Analogía del cuentakilómetros**: la derivada del odómetro (kilómetros acumulados) es el velocímetro (km/h). Al revés, la integral del velocímetro entre las 2pm y las 5pm es la distancia que recorriste en esas 3 horas. Velocidad → (integrar) → distancia; distancia → (derivar) → velocidad. Son operaciones opuestas.

El puente entre ambas ideas es el **Teorema Fundamental del Cálculo**: para calcular el área `∫ₐᵇ f(x) dx`, primero encuentras la antiderivada `F` y luego evalúas `F(b) − F(a)`. Esto convierte "sumar infinitos rectángulos" en una simple resta.

## Fórmulas / método

**Integral definida (área neta bajo la curva):**

```
∫ₐᵇ f(x) dx = F(b) − F(a)        donde F'(x) = f(x)
```

- `a`, `b`: límites inferior y superior de integración (unidades del eje `x`).
- El resultado tiene unidades de **[f(x)] × [x]** (alto × ancho). Si `f` es "empanadas/hora" y `x` es "horas", el área es "empanadas".

**Reglas básicas de antiderivadas** (cada una se verifica derivándola):

| `f(x)` | `∫ f(x) dx` |
|---|---|
| `k` (constante) | `k·x + C` |
| `xⁿ` (n ≠ −1) | `xⁿ⁺¹/(n+1) + C` |
| `1/x` | `ln|x| + C` |
| `eˣ` | `eˣ + C` |
| `cos x` | `sin x + C` |
| `sin x` | `−cos x + C` |

**Propiedades útiles:**

```
∫ₐᵇ [f + g] dx = ∫ₐᵇ f dx + ∫ₐᵇ g dx        (linealidad)
∫ₐᵇ k·f dx     = k·∫ₐᵇ f dx
∫ₐᵇ f dx       = −∫ᵦᵃ f dx                    (invertir límites cambia el signo)
∫ₐᵃ f dx       = 0
```

> ⚠️ El **área neta** puede ser negativa o cancelarse: lo que está bajo el eje `x` cuenta como negativo. Si quieres el **área geométrica total** (siempre positiva), integra `|f(x)|`.

## Verificación en código

Usamos **sympy** para el resultado **simbólico exacto** (sin decimales aproximados) y luego verificamos por una **segunda vía independiente**: integración numérica con `scipy.quad`.

```python
import sympy as sp

# --- VÍA 1: integral simbólica EXACTA con sympy ---
x = sp.symbols('x')
f = x**2                      # función a integrar: f(x) = x^2

F = sp.integrate(f, x)        # antiderivada indefinida
print("Antiderivada F(x) =", F)              # x**3/3

# Integral definida exacta de 0 a 3 (como FRACCIÓN exacta, no float)
area_exacta = sp.integrate(f, (x, 0, 3))
print("Area exacta [0,3] =", area_exacta)    # 9  (=27/3)

# VERIFICACION A: derivar la antiderivada debe devolver f (operacion inversa)
assert sp.simplify(sp.diff(F, x) - f) == 0, "F' != f: antiderivada mal"

# VERIFICACION B: Teorema Fundamental a mano  F(3) - F(0)
chequeo_tfc = F.subs(x, 3) - F.subs(x, 0)
assert sp.simplify(chequeo_tfc - area_exacta) == 0, "TFC no cuadra"
print("TFC F(3)-F(0) =", chequeo_tfc)        # 9
```

```python
# --- VIA 2 (independiente): integracion NUMERICA con scipy ---
from scipy import integrate as sci

valor_num, err = sci.quad(lambda t: t**2, 0, 3)
print("Numerica scipy   =", valor_num, "± aprox", err)   # ~9.0

# El resultado numerico debe coincidir con el exacto dentro de tolerancia
assert abs(valor_num - float(area_exacta)) < 1e-9, "exacto vs numerico no coinciden"
print("OK: simbolico y numerico coinciden ->", float(area_exacta))
```

Tres vías concuerdan: antiderivada `x³/3`, Teorema Fundamental `F(3)−F(0)=9`, y numérico `≈9`. Resultado: **9** (unidades = [f]·[x]).

## Ejemplo trabajado (negocio LatAm)

**Problema.** Un food-truck en Bogotá vende a una tasa que varía con la hora. Modelamos la velocidad de venta como `v(t) = 30·t − 3·t²` **empanadas por hora**, donde `t` son las horas transcurridas desde la apertura (válido de `t=0` a `t=8`). ¿Cuántas empanadas se venden entre la hora 2 y la hora 6?

**Planteo.** Total vendido = acumulación de la tasa = `∫₂⁶ (30t − 3t²) dt`.

**Paso 1 — Antiderivada** (regla `xⁿ → xⁿ⁺¹/(n+1)`):
`∫ (30t − 3t²) dt = 30·t²/2 − 3·t³/3 = 15t² − t³`. Llamémosla `F(t)`.

**Paso 2 — Teorema Fundamental** `F(6) − F(2)`:
- `F(6) = 15·36 − 216 = 540 − 216 = 324`
- `F(2) = 15·4 − 8 = 60 − 8 = 52`
- Total `= 324 − 52 = 272`

```python
import sympy as sp
t = sp.symbols('t')
v = 30*t - 3*t**2
total = sp.integrate(v, (t, 2, 6))
print("Empanadas vendidas hora 2 a 6:", total)        # 272

# Verificacion 2da via: numerica
from scipy import integrate as sci
num,_ = sci.quad(lambda u: 30*u - 3*u**2, 2, 6)
assert abs(float(total) - num) < 1e-9
# Sanity check de orden de magnitud: tasa promedio ~ v(4)=30*4-3*16=72/h por 4h ≈ 288, cercano a 272 ✓
print("OK", float(total))
```

**Respuesta:** se venden **272 empanadas** entre la hora 2 y la hora 6.
Verificación de magnitud: la tasa pico ronda `v(5)=75`/h y el promedio ~68/h durante 4 h → del orden de 270, coherente con 272. ✓

> Nota de dinero: si cada empanada deja $1.500 COP de margen, el margen acumulado es `272 × $1.500 = $408.000 COP`. Ese paso monetario hazlo siempre con `decimal`/centavos enteros (ver [[12-fracciones-decimales-y-precision]]), nunca con `float`.

## Errores comunes / trampas

- **Olvidar el `+ C`** en la integral indefinida: sin él la antiderivada está incompleta (afecta problemas con condición inicial).
- **Confundir área neta con área total**: tramos bajo el eje restan. Si quieres área geométrica total, integra `|f|` o parte la integral en los cruces por cero.
- **Invertir los límites sin cambiar el signo**: `∫ₐᵇ = −∫ᵦᵃ`. Poner `a > b` por descuido invierte el signo del resultado.
- **Aplicar `xⁿ⁺¹/(n+1)` cuando `n = −1`**: para `1/x` la antiderivada NO es `x⁰/0` (división por cero), es `ln|x|`. Caso especial aparte.
- **Confiar en integración "de memoria"**: las antiderivadas no triviales se equivocan fácil. Ejecuta sympy y verifica derivando el resultado.
- **Aproximar demasiado pronto / usar float para dinero**: deja sympy en fracciones exactas y redondea UNA sola vez al final (ver [[05-cifras-significativas-y-redondeo]]).
- **Integrar fuera del dominio válido del modelo**: el modelo `30t−3t²` se vuelve negativo tras `t=10`; integrar más allá da "ventas negativas" sin sentido.

## Cruces

- [[45-aplicaciones-de-la-integral]] — usos concretos (área entre curvas, valor acumulado, valor promedio, excedente).
- [[41-derivadas-concepto]] — la integral es la operación inversa; entender derivada primero.
- [[42-reglas-de-derivacion]] — cada antiderivada se verifica derivándola con estas reglas.
- [[40-limites-y-continuidad]] — la integral se define como límite de sumas (sumas de Riemann).
- [[03-protocolo-de-verificacion-por-codigo]] — patrón ejecutar + verificar por segunda vía.

---

**Mini-checklist de exactitud**
- [ ] ¿Verifiqué la antiderivada **derivándola** (`F' == f`) y comparé con una **vía numérica** (`scipy.quad`)?
- [ ] ¿Respeté el orden de los límites (`a→b`) y consideré si quería área **neta** o **total**?
- [ ] ¿Dejé el resultado exacto (fracción) y solo redondeé al final, con **unidades** correctas (`[f]·[x]`)?
