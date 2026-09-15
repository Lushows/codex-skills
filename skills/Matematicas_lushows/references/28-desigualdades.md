# 28 · Desigualdades

> **Qué resuelve / cuándo usarlo** — Cuando una cantidad no tiene que ser igual a algo, sino estar por encima, por debajo o dentro de un rango: "¿cuántas unidades debo vender para NO perder plata?", "¿qué precios me dan margen ≥ 30%?", "¿qué presupuesto cabe en mi caja?". Las desigualdades describen *zonas viables*, no un único valor.

## Concepto (para no-experto)

Una **ecuación** dice "esto es igual a esto" (`x = 5`). Una **desigualdad** dice "esto es mayor/menor que esto", y por eso su respuesta no es un número, sino un **rango** de números (un *conjunto de soluciones*).

Los cuatro símbolos:

| Símbolo | Se lee | Incluye el extremo |
|---|---|---|
| `<` | menor que | NO |
| `>` | mayor que | NO |
| `≤` | menor o igual que | SÍ |
| `≥` | mayor o igual que | SÍ |

**Analogía cotidiana.** Pensa en la temperatura de un horno. No te sirve "exactamente 180°C": te sirve "entre 170 y 190". Eso es una desigualdad doble: `170 ≤ T ≤ 190`. Cualquier valor dentro de ese rango funciona; fuera, se quema o queda crudo. Igual en un negocio: "vender al menos 84 unidades para no perder" es `q ≥ 84`.

**Intervalo** = la forma corta de escribir un rango.
- `(a, b)` paréntesis = extremo **abierto**, NO incluido (`<` o `>`).
- `[a, b]` corchete = extremo **cerrado**, SÍ incluido (`≤` o `≥`).
- `∞` (infinito) siempre va con paréntesis: `[84, ∞)` significa "84 o más, sin tope".

**Recta numérica (gráfico).** Una desigualdad se dibuja sombreando la zona buena sobre una línea: círculo **vacío** ○ si el extremo NO se incluye, círculo **relleno** ● si se incluye.

```
x ≥ 84:   ────────●═══════════>
                  84
x < 84:   ════════○────────────>
                  84
```

## Fórmulas / método

**Reglas para despejar (igual que una ecuación, con UNA trampa):**

1. Sumar o restar el mismo número a ambos lados → el sentido NO cambia.
   Si `a < b` entonces `a + c < b + c`.
2. Multiplicar o dividir por un número **positivo** → el sentido NO cambia.
   Si `a < b` y `c > 0`, entonces `a·c < b·c`.
3. **⚠️ TRAMPA CLAVE:** multiplicar o dividir por un número **negativo** → **se invierte** el sentido.
   Si `a < b` y `c < 0`, entonces `a·c > b·c`.
   Ejemplo: `2 < 3` es verdad; multiplico por `-1`: `-2 > -3` (también verdad — el `<` se volvió `>`).

**Desigualdad lineal:** `m·x + b  ⪋  0` → se despeja `x` aislándola.

**Desigualdad doble (rango):** `a ≤ expresión ≤ b` → se opera en los tres bloques a la vez.

**Sistema de restricciones (varias a la vez):** la solución es la **intersección** (lo que cumple TODAS). En la recta, la zona común; en el plano, el polígono donde se solapan.

Notación de unidades: las desigualdades de negocio llevan unidades igual que cualquier cálculo (`q ≥ 84 unidades`, `P ≥ $14.286 COP`).

## Verificación en código

Resolvemos de forma **exacta** con `sympy` (álgebra simbólica, sin errores de redondeo de `float`). Caso: punto de equilibrio.

Datos: precio de venta `P = 10.000 COP/unidad`, costo variable `cv = 4.000 COP/unidad`, costos fijos `CF = 504.000 COP/mes`. Pregunta: ¿qué cantidad `q` deja utilidad ≥ 0?

```python
from sympy import symbols, solve_univariate_inequality, Rational, S

q = symbols('q', real=True)

# Dinero como Rational (fracción exacta), NUNCA float
P  = Rational(10000)   # precio venta  [COP/unidad]
cv = Rational(4000)    # costo variable[COP/unidad]
CF = Rational(504000)  # costos fijos  [COP/mes]

# Utilidad = ingresos - costos variables - costos fijos
utilidad = P*q - cv*q - CF          # = 6000*q - 504000

# Restricción de viabilidad: utilidad >= 0
sol = solve_univariate_inequality(utilidad >= 0, q, relational=True)
print("Solucion exacta:", sol)       # q >= 84

# Frontera (punto de equilibrio): resolver la igualdad
break_even = solve(utilidad, q) if False else CF / (P - cv)
print("Punto de equilibrio:", break_even, "unidades")  # 84
```

```python
# ===== VERIFICACION POR SEGUNDA VIA: evaluar en 3 puntos =====
def utilidad_en(qv):
    return 6000*qv - 504000

assert utilidad_en(83) <  0, "83 deberia dar perdida"   # -6000  -> rojo
assert utilidad_en(84) == 0, "84 es el equilibrio exacto"#     0  -> empate
assert utilidad_en(85) >  0, "85 deberia dar ganancia"   #  6000  -> verde
print("OK: la frontera q>=84 es correcta por evaluacion directa")

# Tercera via: estimacion de orden de magnitud (sanity check)
# margen por unidad = 6.000; fijos = 504.000 ; 504.000/6.000 = 84  ✔
```

Las dos vías coinciden: **`q ≥ 84 unidades`**. El extremo se incluye (en 84 la utilidad es exactamente 0, que cumple `≥ 0`).

## Ejemplo trabajado

**Problema (dark kitchen, GastroLatam).** Vendes almuerzos a $18.000 COP. El costo de insumos por almuerzo es $11.000 COP y tienes $1.260.000 COP de costos fijos al mes (arriendo + plataforma). Quieres una utilidad **de al menos** $700.000 COP al mes. ¿Cuántos almuerzos `q` debes vender?

**Planteo.** Utilidad mensual = `(18.000 − 11.000)·q − 1.260.000`. Margen de contribución por almuerzo = `7.000 COP`.

Restricción: utilidad `≥ 700.000`.

```
7000·q − 1.260.000 ≥ 700.000
7000·q ≥ 700.000 + 1.260.000        (sumo 1.260.000 a ambos lados)
7000·q ≥ 1.960.000
q ≥ 1.960.000 / 7000                 (divido por 7000, positivo → no se invierte)
q ≥ 280
```

**Respuesta: `q ≥ 280 almuerzos/mes`** (intervalo `[280, ∞)`).

Como no se pueden vender fracciones de almuerzo, en la práctica `q` es entero, así que el mínimo real es **280 almuerzos al mes** (≈ 9,3 al día con 30 días).

Verificación rápida (segunda vía, inversa): en `q = 280` → `7000·280 − 1.260.000 = 1.960.000 − 1.260.000 = 700.000` ✔ exactamente el piso pedido. En `q = 279` → `693.000 < 700.000`, no alcanza. Frontera confirmada.

## Errores comunes / trampas

- **No invertir el signo al multiplicar/dividir por negativo.** Es EL error mortal. `−2x < 6` → divido por `−2` → `x > −3` (el `<` se vuelve `>`). Si te queda `x < −3`, está mal.
- **Confundir abierto y cerrado.** `q ≥ 84` incluye el 84 (círculo relleno, corchete `[84,`). `q > 84` no lo incluye. En negocio importa: "al menos" = `≥`, "más de" = `>`.
- **Olvidar que la respuesta es un rango, no un punto.** Resolver solo la igualdad (la frontera) y reportar ese número como "la respuesta" pierde toda la zona viable.
- **Restricciones de la vida real ignoradas.** `q ≥ 84` matemáticamente admite 84,5; pero unidades vendidas son enteras y `≥ 0` siempre. Ajusta al dominio real (entero, no negativo).
- **Redondear en medio del despeje.** Mantén fracciones exactas (`Rational`) y redondea una sola vez al final.
- **Intersección mal hecha en sistemas.** Con varias restricciones, la solución es lo que cumple TODAS a la vez (la más restrictiva manda), no la unión.

## Cruces

- [[21-ecuaciones-lineales]] — la desigualdad lineal se despeja igual que la ecuación (cuidando el signo).
- [[76-punto-de-equilibrio]] — el "≥ 0 de utilidad" es exactamente una desigualdad de viabilidad.
- [[25-funciones-concepto-dominio-rango]] — el dominio/rango se define con desigualdades.
- [[91-programacion-lineal]] — optimizar sujeto a un sistema de desigualdades (restricciones).
- [[92-asignacion-optima-de-recursos]] — repartir recursos limitados = restricciones `≤` simultáneas.

---

**Mini-checklist de exactitud**
1. ¿Invertí el signo cada vez que multipliqué/dividí por un negativo?
2. ¿El extremo es abierto (`<`,`>`) o cerrado (`≤`,`≥`) y lo dibujé/escribí bien (○ vs ●, `(` vs `[`)?
3. ¿Probé un valor DENTRO y otro FUERA del rango para confirmar la frontera?
