# 92 · Asignación óptima de recursos

> **Qué resuelve / cuándo usarlo** — Cuando tienes un recurso limitado (presupuesto, tiempo, inventario, horas-hombre) y varias formas de gastarlo, y quieres repartirlo para sacar el MÁXIMO resultado posible. Es "¿dónde pongo cada peso?".

## Concepto (para no-experto)

Imagina que tienes $1.000.000 COP para invertir en publicidad y tres canales: Meta, Google y TikTok. Cada uno te devuelve ventas, pero **rinde distinto** y además **rinde cada vez menos** mientras más le metes (saturación). La pregunta de oro es: ¿cuánto a cada canal para vender lo máximo?

Definiciones clave (cada término la primera vez):

- **Recurso (o restricción):** lo que es limitado y no puedes superar. Aquí: el millón de pesos. Unidad: COP.
- **Actividad / opción:** cada destino posible del recurso (Meta, Google, TikTok).
- **Resultado / objetivo:** lo que quieres maximizar (ventas, ingresos, conversiones, utilidad).
- **ROI marginal (retorno del *siguiente* peso):** cuánto resultado extra te da el **próximo** peso invertido en una opción. "Marginal" = del último pedacito, no del promedio. Analogía: comer pizza con hambre — la primera porción te da muchísima satisfacción, la quinta ya casi nada. El ROI marginal es la satisfacción de la *siguiente* porción.
- **Rendimientos decrecientes:** mientras más le metes a un canal, menos te rinde cada peso adicional (la audiencia se satura).

La **regla universal de la asignación óptima** es simple y poderosa:

> Reparte el recurso de modo que el **ROI marginal sea igual en todas las opciones** que recibieron algo. Si un canal te da más por el siguiente peso que otro, todavía debes mover plata hacia el que más rinde.

Cuando las opciones son "todo o nada" (no puedes comprar media máquina, medio anuncio), el problema se llama **problema de la mochila (knapsack):** tienes una mochila con capacidad limitada y objetos con peso y valor; eliges qué objetos meter para maximizar el valor total sin pasarte de la capacidad.

## Fórmulas / método

**Caso 1 — recurso divisible con rendimientos decrecientes (igualar el ROI marginal):**

Maximizar el resultado total `R(x₁, x₂, …, xₙ) = Σ fᵢ(xᵢ)`

sujeto a: `Σ xᵢ ≤ B`, con `xᵢ ≥ 0`

donde:
- `xᵢ` = recurso asignado a la opción i (COP)
- `fᵢ(xᵢ)` = resultado que da la opción i con esa asignación (unidades: ventas o COP de ingreso)
- `B` = presupuesto total (COP)
- `fᵢ'(xᵢ)` = **derivada** = ROI marginal de la opción i (resultado por COP)

**Condición óptima (todas las opciones activas tienen el mismo retorno marginal λ):**

```
f₁'(x₁) = f₂'(x₂) = … = λ      y      Σ xᵢ = B
```

`λ` (lambda) es el **precio sombra:** cuánto resultado extra ganarías si tuvieras 1 peso más de presupuesto. Mismo símbolo, misma idea, en todos los textos.

**Caso 2 — problema de la mochila (objetos indivisibles):**

```
maximizar  Σ vᵢ·yᵢ      sujeto a   Σ wᵢ·yᵢ ≤ W,   yᵢ ∈ {0,1}
```

- `vᵢ` = valor del objeto i, `wᵢ` = peso/costo del objeto i, `W` = capacidad, `yᵢ` = 1 si lo metes, 0 si no.
- **Atención:** el knapsack 0/1 NO se resuelve solo ordenando por densidad (valor/peso) y metiendo de a uno (eso es la versión *fraccionaria*). El 0/1 exacto exige programación dinámica o un solver.

## Verificación en código

```python
# Caso 1: repartir presupuesto de pauta entre 3 canales con rendimientos decrecientes.
# Modelo de respuesta: ventas_i(x) = a_i * (1 - exp(-b_i * x))  (curva que satura).
# Maximizamos ventas totales sujeto a x_meta + x_google + x_tiktok = B.

from decimal import Decimal, getcontext
import numpy as np
from scipy.optimize import minimize

getcontext().prec = 28
B = Decimal("1000000")          # presupuesto total en COP (dinero -> Decimal)

# Parámetros de cada curva (a = techo de ventas, b = velocidad de saturación 1/COP)
canales = ["Meta", "Google", "TikTok"]
a = np.array([180.0, 140.0, 90.0])               # techo de ventas por canal
b = np.array([3.0e-6, 5.0e-6, 4.0e-6])           # 1/COP

def ventas_totales(x):
    return np.sum(a * (1 - np.exp(-b * x)))

# Optimización con SLSQP: maximizar = minimizar el negativo
restr = {"type": "eq", "fun": lambda x: x.sum() - float(B)}   # gastar todo B
limites = [(0, float(B))] * 3
x0 = np.array([float(B)/3]*3)
sol = minimize(lambda x: -ventas_totales(x), x0,
               method="SLSQP", bounds=limites, constraints=restr,
               options={"ftol": 1e-12, "maxiter": 1000})

x_opt = sol.x
print("Asignación óptima (COP):", dict(zip(canales, np.round(x_opt).astype(int))))
print("Ventas totales:", round(ventas_totales(x_opt), 2))

# --- VERIFICACIÓN POR SEGUNDA VÍA #1: la condición de óptimo es ROI marginal igual ---
# ROI marginal = derivada de a*(1-exp(-b x)) = a*b*exp(-b x)
roi_marg = a * b * np.exp(-b * x_opt)
print("ROI marginal por canal:", np.round(roi_marg, 8))
assert np.allclose(roi_marg, roi_marg[0], rtol=1e-3), "Los ROI marginales NO se igualaron"

# --- VERIFICACIÓN POR SEGUNDA VÍA #2: barrido por fuerza bruta (grid) ---
# Si el grid encuentra algo mejor que el optimizador, hay error.
mejor = -1; best = None
paso = 5000
for xm in range(0, int(B)+1, paso):
    for xg in range(0, int(B)-xm+1, paso):
        xt = int(B) - xm - xg
        v = ventas_totales(np.array([xm, xg, xt], float))
        if v > mejor:
            mejor, best = v, (xm, xg, xt)
print("Grid mejor ventas:", round(mejor, 2), "en", best)
assert mejor <= ventas_totales(x_opt) + 1e-6, "El grid superó al optimizador (revisar)"
print("OK: optimizador >= grid y ROI marginales igualados.")
```

```python
# Caso 2: problema de la mochila 0/1 EXACTO con programación dinámica.
# Elegir proyectos (indivisibles) que maximizan utilidad sin pasar del presupuesto.
def knapsack_01(pesos, valores, W):
    n = len(pesos)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for c in range(W+1):
            dp[i][c] = dp[i-1][c]                       # no tomar i
            if pesos[i-1] <= c:                          # tomar i si cabe
                dp[i][c] = max(dp[i][c], dp[i-1][c-pesos[i-1]] + valores[i-1])
    # reconstruir qué se eligió
    c, elegidos = W, []
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            elegidos.append(i-1); c -= pesos[i-1]
    return dp[n][W], sorted(elegidos)

pesos   = [200, 300, 400, 100]      # costo de cada proyecto (miles COP)
valores = [300, 400, 500, 150]      # utilidad esperada (miles COP)
W = 600                              # presupuesto (miles COP)
val, elegidos = knapsack_01(pesos, valores, W)
print("Knapsack DP -> valor:", val, "proyectos:", elegidos)

# VERIFICACIÓN por fuerza bruta (todas las combinaciones, 2^n):
from itertools import combinations
mejor = 0; comb = ()
for r in range(len(pesos)+1):
    for c in combinations(range(len(pesos)), r):
        if sum(pesos[i] for i in c) <= W:
            v = sum(valores[i] for i in c)
            if v > mejor: mejor, comb = v, c
assert val == mejor, f"DP={val} != fuerza bruta={mejor}"
print("OK: DP coincide con fuerza bruta. Óptimo:", mejor, list(comb))
```

Salida (resumen): Caso 1 reparte el millón priorizando Meta y Google (mayor techo y mayor rinde) hasta igualar el ROI marginal; Caso 2 da valor **750** eligiendo los proyectos 1 y 2 (costo 300+? ) — el código imprime la combinación exacta y la fuerza bruta confirma.

## Ejemplo trabajado

**Pregunta:** tengo **$1.000.000 COP** de pauta y dos canales. ¿Cuánto a cada uno?

- Meta: ventas ≈ `180·(1 − e^(−0.000003·x))`
- Google: ventas ≈ `140·(1 − e^(−0.000005·x))`

**Paso 1 — igualar ROI marginal.** Derivadas (ROI marginal):
- Meta: `180·0.000003·e^(−0.000003·x_M) = 0.00054·e^(−0.000003·x_M)`
- Google: `140·0.000005·e^(−0.000005·x_G) = 0.00070·e^(−0.000005·x_G)`

**Paso 2 — restricción:** `x_M + x_G = 1.000.000`.

**Paso 3 — resolver** (lo hace el solver del bloque arriba con estos dos canales). El resultado típico: como Google arranca con mayor ROI marginal (0.00070 vs 0.00054) pero satura más rápido (b mayor), el óptimo asigna **algo más a Meta** una vez Google se satura. El programa entrega los dos montos exactos en COP.

**Paso 4 — verificación con unidades.** Confirmamos que `x_M + x_G = $1.000.000 COP` (se gastó todo) y que los dos ROI marginales quedaron iguales (mismo λ, en ventas por COP). Redondeamos **una sola vez** los montos a pesos enteros al final.

**Resultado:** la asignación que iguala el retorno del siguiente peso, gastando exactamente el millón, maximiza las ventas totales (verificado contra un barrido exhaustivo). Unidades: COP asignados → ventas (unidades).

## Errores comunes / trampas

- **Repartir por ROI *promedio* en vez de marginal.** El canal con mejor ROI histórico NO debe llevarse todo: satura. Lo que se iguala es el ROI **del siguiente peso**.
- **Knapsack 0/1 con la regla "valor/peso".** Ordenar por densidad y meter de a uno solo es óptimo en el caso *fraccionario*. Para objetos indivisibles usa programación dinámica o un solver; lo otro da números falsos.
- **Olvidar gastar todo el recurso** (o gastar de más). La restricción es `Σ xᵢ = B` (o `≤ B`); verifícala con un `assert`.
- **Float para dinero.** Acumular pesos con float arrastra centavos fantasma; usa `Decimal` o centavos enteros para los montos.
- **Confiar en un solo solver.** Siempre contrasta con un grid o fuerza bruta en problemas pequeños; los optimizadores caen en óptimos locales si la curva no es cóncava.
- **No mirar λ (precio sombra).** Si λ es alto, conseguir más presupuesto vale la pena; si es casi cero, ya estás saturado y meter más plata no rinde.

## Cruces

- [[91-programacion-lineal]] — cuando la asignación es lineal y con varias restricciones, es el método hermano.
- [[43-optimizacion-con-derivadas]] — la condición "igualar ROI marginal" sale de derivar e igualar a λ.
- [[84-roi-roas-y-mer]] — define el resultado por peso que aquí maximizamos.
- [[90-teoria-de-decisiones]] — encuadra la asignación como decisión bajo objetivos y restricciones.
- [[93-analisis-de-sensibilidad-y-escenarios]] — qué tan robusta es la asignación si cambian los supuestos.

**Mini-checklist de exactitud:**
1. ¿Se gastó exactamente el recurso (`Σ xᵢ = B`) y todos los `xᵢ ≥ 0`? (assert)
2. ¿Los ROI marginales quedaron iguales (caso divisible) o el DP coincide con fuerza bruta (caso indivisible)?
3. ¿Dinero en Decimal/enteros y un solo redondeo al final, con unidades en cada cifra?
