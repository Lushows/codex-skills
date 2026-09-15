# 91 · Programación lineal

> **Qué resuelve / cuándo usarlo** — Cuando quieres maximizar (ganancia) o minimizar (costo) algo que depende de varias decisiones, sujeto a límites de recursos (horas, dinero, materia prima). Te da la combinación exacta que más conviene.

## Concepto (para no-experto)

**Programación lineal (PL)** es una técnica para encontrar la *mejor* decisión cuando todo se comporta de forma proporcional (lineal) y hay límites.

Imagina una panadería que hace **pan** y **tortas**. Cada producto deja una ganancia y consume recursos (harina, horas de horno). Tienes harina y horas limitadas. ¿Cuántos panes y cuántas tortas hacer para ganar lo máximo posible? Eso es PL.

Términos clave (los defino la primera vez que aparecen):

- **Variables de decisión**: las cantidades que tú eliges. Ej.: `x` = panes, `y` = tortas. Son los "botones" que puedes mover.
- **Función objetivo**: la fórmula del número que quieres hacer lo más grande (max) o lo más pequeño (min) posible. Ej.: ganancia total = `3x + 5y`. Se llama "lineal" porque cada variable aparece multiplicada por un número fijo y se suman; no hay `x²`, ni `x·y`, ni raíces.
- **Restricciones**: las reglas que limitan tus decisiones, escritas como desigualdades. Ej.: "la harina alcanza para `2x + 4y ≤ 100`".
- **Región factible**: el conjunto de TODAS las combinaciones `(x, y)` que cumplen todas las restricciones a la vez. Visualmente, en 2 variables, es un polígono. La solución óptima SIEMPRE está en una **esquina (vértice)** de ese polígono — esa es la propiedad mágica de la PL.

Analogía: la región factible es un terreno con cercas (las restricciones). Buscas el punto más alto (max ganancia). En PL ese punto siempre cae en una esquina del terreno, nunca en el medio de un lado plano. Por eso basta revisar las esquinas.

## Fórmulas / método

Forma estándar (la que usa `scipy.optimize.linprog`, que **siempre minimiza**):

```
minimizar    c · x        (función objetivo: c es vector de coeficientes)
sujeto a     A_ub · x ≤ b_ub   (restricciones de desigualdad ≤)
             A_eq · x  = b_eq   (restricciones de igualdad =)
             lb ≤ x ≤ ub        (cotas de cada variable, por defecto x ≥ 0)
```

Símbolos (con unidades de ejemplo en una panadería):

- `x` = vector de variables de decisión (panes, tortas) [unidades].
- `c` = coeficientes de la función objetivo (ganancia por unidad) [$/unidad].
- `A_ub`, `b_ub` = matriz y vector de las restricciones tipo "≤" (consumo ≤ disponible).
- `A_eq`, `b_eq` = restricciones tipo "=" (rara vez se usan; ej.: "produce exactamente 10").
- `lb`, `ub` = cota inferior / superior de cada variable.

**Truco clave (no negociable):** linprog SOLO minimiza. Para **maximizar** `c·x`, minimizas `-c·x` y luego le cambias el signo al resultado. Olvidar esto es el error #1.

Conversión de "≥" a "≤": una restricción `a·x ≥ b` se reescribe multiplicando por −1 → `−a·x ≤ −b`.

## Verificación en código

Problema: panadería. `x` = panes, `y` = tortas.
- Ganancia: $3/pan, $5/torta → maximizar `3x + 5y`.
- Harina: cada pan usa 2 kg, cada torta 4 kg; hay 100 kg → `2x + 4y ≤ 100`.
- Horno: cada pan usa 1 h, cada torta 1 h; hay 40 h → `x + y ≤ 40`.
- `x, y ≥ 0`.

```python
# Vía 1: resolver con scipy.optimize.linprog (Simplex/HiGHS, aritmética robusta)
from scipy.optimize import linprog

# linprog MINIMIZA c·x. Queremos MAXIMIZAR 3x+5y -> minimizamos -(3x+5y).
c = [-3, -5]                  # signos invertidos para maximizar

A_ub = [[2, 4],              # harina: 2x + 4y <= 100
        [1, 1]]              # horno:  1x + 1y <= 40
b_ub = [100, 40]

bounds = [(0, None), (0, None)]   # x>=0, y>=0

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

x_opt, y_opt = res.x
ganancia = -res.fun           # volvemos a invertir el signo
print(f"panes = {x_opt:.6f}, tortas = {y_opt:.6f}")
print(f"ganancia maxima = ${ganancia:.6f}")
# panes = 30.000000, tortas = 10.000000
# ganancia maxima = $140.000000
```

```python
# Vía 2 (verificación independiente): teorema de los vertices.
# La solucion optima de un PL esta en un VERTICE de la region factible.
# Enumeramos todos los vertices (intersecciones de pares de rectas) y
# evaluamos la ganancia en cada uno. Si coincide con linprog, doble check OK.
from fractions import Fraction as F   # aritmetica EXACTA, sin floats

# Rectas frontera (como igualdades a·x + b·y = k):
#  R1 harina: 2x + 4y = 100
#  R2 horno:  1x + 1y = 40
#  R3 eje x:  y = 0      ->  0x + 1y = 0
#  R4 eje y:  x = 0      ->  1x + 0y = 0
rectas = [
    (F(2), F(4), F(100)),  # R1
    (F(1), F(1), F(40)),   # R2
    (F(0), F(1), F(0)),    # R3 (y=0)
    (F(1), F(0), F(0)),    # R4 (x=0)
]

def interseccion(r1, r2):
    a1, b1, k1 = r1
    a2, b2, k2 = r2
    det = a1*b2 - a2*b1          # determinante 2x2
    if det == 0:
        return None             # rectas paralelas: sin interseccion unica
    x = (k1*b2 - k2*b1) / det
    y = (a1*k2 - a2*k1) / det
    return (x, y)

def factible(p):
    x, y = p
    return (x >= 0 and y >= 0 and 2*x + 4*y <= 100 and x + y <= 40)

import itertools
vertices = []
for r1, r2 in itertools.combinations(rectas, 2):
    p = interseccion(r1, r2)
    if p is not None and factible(p):
        vertices.append(p)

mejor = max(vertices, key=lambda p: 3*p[0] + 5*p[1])
g = 3*mejor[0] + 5*mejor[1]
print("vertices factibles:", [(str(x), str(y)) for x, y in sorted(set(vertices))])
print(f"mejor vertice: x={mejor[0]}, y={mejor[1]}, ganancia=${g}")

# Comparamos las dos vias con tolerancia (linprog usa float, vertice es exacto)
assert abs(float(mejor[0]) - x_opt) < 1e-6
assert abs(float(mejor[1]) - y_opt) < 1e-6
assert abs(float(g) - ganancia) < 1e-6
print("OK: linprog y enumeracion de vertices coinciden")
```

La doble vía confirma: linprog (método numérico Simplex/HiGHS) **y** la enumeración exacta de vértices con fracciones dan el mismo óptimo. Dos caminos, mismo número.

## Ejemplo trabajado

**Caso LatAm — taller de confecciones (Medellín).** Produce **camisetas** (`x`) y **buzos** (`y`).

| Recurso | Camiseta | Buzo | Disponible |
|---|---|---|---|
| Tela (m²) | 1.5 | 3.0 | 600 m² |
| Mano de obra (h) | 0.5 | 1.0 | 250 h |
| Ganancia ($) | $8.000 | $14.000 | — |

Objetivo: maximizar `8000·x + 14000·y` [COP].

Restricciones:
- Tela: `1.5x + 3y ≤ 600`
- Mano de obra: `0.5x + y ≤ 250`
- `x, y ≥ 0`

Paso a paso (vértices de la región factible):
- Intersección tela ∩ mano de obra: resolviendo `1.5x+3y=600` y `0.5x+y=250` → las dos rectas son **paralelas** (la segunda ×3 = `1.5x+3y=750` ≠ 600), no se cruzan dentro. El óptimo cae en otro vértice.
- Sobre el eje (`x=0`): tela permite `y ≤ 200`, mano de obra `y ≤ 250` → manda tela: `y=200` → ganancia = `14000·200 = $2.800.000`.
- Sobre el eje (`y=0`): tela `x ≤ 400`, mano de obra `x ≤ 500` → manda tela: `x=400` → ganancia = `8000·400 = $3.200.000`.

Resultado óptimo: **400 camisetas, 0 buzos → ganancia máxima = $3.200.000 COP**, usando 600 m² de tela (tope) y 200 h de mano de obra (sobran 50 h). Verifícalo con el mismo `linprog` cambiando `c`, `A_ub`, `b_ub`. *(Lección de negocio: con estos números la camiseta rinde más por m² de tela —el recurso que se agota— así que conviene 100% camisetas; cambia el precio de la tela o la ganancia del buzo y la respuesta puede invertirse.)*

## Errores comunes / trampas

- **Maximizar sin invertir el signo.** linprog minimiza siempre; para max usa `-c` y luego `-res.fun`. Olvidarlo da el peor punto, no el mejor.
- **Restricción "≥" metida como "≤".** Conviértela: `a·x ≥ b` → `-a·x ≤ -b`. Mezclar el sentido cambia la región factible por completo.
- **No revisar `res.success` / `res.status`.** Si es infactible (status 2) o no acotado (status 3), `res.x` no sirve. Siempre `assert res.success`.
- **Confundir el coeficiente con el lado derecho.** `c` son ganancias/costos por unidad; `b_ub` son los recursos disponibles. Cruzarlos da basura plausible.
- **Esperar enteros.** PL da reales (ej.: 12.5 camisetas). Si necesitas enteros forzosos es *programación entera* (otra herramienta: `scipy.optimize.milp` o un solver MIP), no `linprog`.
- **Unidades inconsistentes.** Si la tela está en m² en un lado y cm² en otro, todo se rompe silenciosamente. Fija una unidad por recurso (ver [[04-notacion-unidades-y-dimensiones]]).

## Cruces

- [[22-sistemas-de-ecuaciones]] — los vértices de la región factible son soluciones de sistemas lineales.
- [[28-desigualdades]] — las restricciones son desigualdades lineales; aquí se combinan.
- [[43-optimizacion-con-derivadas]] — optimización cuando la función es curva (no lineal); PL es el caso lineal con límites.
- [[92-asignacion-optima-de-recursos]] — aplicación directa de PL a repartir recursos escasos.
- [[93-analisis-de-sensibilidad-y-escenarios]] — qué tan robusto es el óptimo si cambian precios o recursos.

---

**Mini-checklist de exactitud**
- [ ] Para maximizar usé `-c` y reporté `-res.fun`; verifiqué `res.success == True`.
- [ ] Confirmé el óptimo por segunda vía (enumeración de vértices con `fractions` o cambiando de solver) y coinciden.
- [ ] Cada coeficiente, recurso y resultado lleva su unidad y la respuesta tiene sentido de orden de magnitud.
