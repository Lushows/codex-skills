# 43 · Optimización con derivadas

> **Qué resuelve / cuándo usarlo** — Encontrar el valor de una variable (precio, cantidad, tamaño de lote) que **maximiza** una ganancia o **minimiza** un costo. Es la matemática detrás de "¿a qué precio gano más?" o "¿qué tamaño de empaque me sale más barato?".

## Concepto (para no-experto)

Imagina que vas en bici por una montaña. Donde el camino deja de subir y empieza a bajar, estás en la **cima** (un máximo). Donde deja de bajar y empieza a subir, estás en el **fondo del valle** (un mínimo). En esos puntos exactos, por un instante, el camino está **plano**: ni sube ni baja.

La **derivada** (ver [[41-derivadas-concepto]]) es justo eso: la **pendiente** o inclinación del camino en cada punto. La derivada te dice cuánto sube o baja la función por cada paso que avanzas.

- Si la derivada es **positiva** → la función sube (vas cuesta arriba).
- Si la derivada es **negativa** → la función baja (vas cuesta abajo).
- Si la derivada es **cero** → el camino está plano. ¡Ahí puede haber una cima o un valle!

Optimizar es encontrar esos puntos planos y luego decidir cuáles son cimas (máximos) y cuáles valles (mínimos). En negocios, la "altura del camino" suele ser la **utilidad** (lo que ganas) o el **costo** (lo que gastas), y la variable que mueves (el "avanzar en la bici") suele ser el **precio** o la **cantidad producida**.

**Términos clave:**
- **Función objetivo**: la cantidad que quieres optimizar, escrita como fórmula. Ej.: utilidad `U(q)`.
- **Variable de decisión**: lo que controlas. Ej.: la cantidad `q` o el precio `p`.
- **Punto crítico**: un valor donde la derivada vale cero (o no existe). Candidato a máximo/mínimo.
- **Máximo / mínimo global**: el mejor (o peor) valor en TODO el rango permitido, no solo en una colina local.

## Fórmulas / método

Sea `f(x)` la función objetivo y `x` la variable de decisión, en un dominio permitido `[a, b]`.

**Condición de primer orden (CPO) — encontrar candidatos:**
```
f'(x) = 0        →  resuelve para x  (puntos críticos)
```
`f'(x)` es la **primera derivada**: la pendiente. Igualarla a cero busca los puntos planos.

**Condición de segundo orden (CSO) — clasificar el punto:**
```
f''(x) < 0   →  MÁXIMO local   (la curva es "ceño fruncido" ∩, cóncava hacia abajo)
f''(x) > 0   →  MÍNIMO local   (la curva es "sonrisa" ∪, cóncava hacia arriba)
f''(x) = 0   →  no concluye; usar otro criterio (signo de f' alrededor, o test de orden superior)
```
`f''(x)` es la **segunda derivada**: la derivada de la pendiente. Mide cómo cambia la curvatura.

**Regla del óptimo global (¡no la olvides!):** el máximo/mínimo global está entre:
1. los puntos críticos interiores que cumplen la CSO, **y**
2. los **extremos del dominio** `x = a` y `x = b` (las "fronteras").

Se evalúa `f` en TODOS esos candidatos y se compara el valor.

**Caso negocio típico — maximizar utilidad por cantidad:**
```
U(q) = I(q) − C(q)            utilidad = ingreso − costo
U'(q) = I'(q) − C'(q) = 0     →   I'(q) = C'(q)
```
Esto es el principio económico **"ingreso marginal = costo marginal"** (`I' = C'`): produce hasta que la última unidad vendida deje de aportar ganancia.

Unidades: si `q` está en unidades y `U` en COP, entonces `U'(q)` está en **COP por unidad** (cuánto cambia la utilidad por cada unidad extra).

## Verificación en código

Ejemplo de negocio: una calculadora gastronómica se vende y la **demanda** (cantidad que el mercado compra) baja al subir el precio. Modelo lineal de demanda y un costo. Buscamos el **precio que maximiza la utilidad**.

```python
import sympy as sp
from decimal import Decimal, ROUND_HALF_UP

# --- Modelo ---
# p = precio (COP). Demanda lineal: q(p) = 5000 - 0.20*p  (unidades/mes)
# Costo: 8000 COP por unidad (variable) + 2_000_000 COP fijos.
p = sp.symbols('p', positive=True)
q = 5000 - sp.Rational(20, 100) * p        # cantidad demandada (usa fracción exacta, NO float)
ingreso = p * q
costo   = 8000 * q + 2_000_000
U = sp.expand(ingreso - costo)             # función objetivo: utilidad U(p)

# --- Condición de 1er orden: U'(p) = 0 ---
Up  = sp.diff(U, p)
crit = sp.solve(sp.Eq(Up, 0), p)
print("U(p)   =", U)
print("U'(p)  =", Up)
print("crítico p* =", crit)                # [16500]

p_star = crit[0]

# --- Condición de 2do orden: U''(p) ---
Upp = sp.diff(U, p, 2)
print("U''(p) =", Upp, "->", "MÁXIMO" if Upp < 0 else "mínimo/otro")

# --- Evaluar utilidad en el óptimo ---
U_opt = U.subs(p, p_star)
q_opt = q.subs(p, p_star)
print("precio óptimo p* =", p_star, "COP")
print("cantidad q*      =", q_opt, "unidades/mes")
print("utilidad máx     =", U_opt, "COP")
```

Salida: `p* = 16500`, `U'' = -0.4 < 0` (máximo), `q* = 1700`, `U_opt = 12,450,000` COP/mes.

**Verificación por segunda vía** (tres comprobaciones independientes):

```python
# Vía 1 — principio económico I'(q)=C'(q) resuelto en función de q (otro método):
qd = sp.symbols('qd', positive=True)
# Invertimos la demanda: p = (5000 - q)/0.2 = 25000 - 5*q
p_de_q = (5000 - qd) / sp.Rational(20,100)
I = p_de_q * qd
C = 8000*qd + 2_000_000
U_q = sp.expand(I - C)
q_check = sp.solve(sp.diff(U_q, qd), qd)[0]
assert q_check == 1700, q_check                       # coincide con q* anterior
assert p_de_q.subs(qd, q_check) == 16500              # coincide con p*

# Vía 2 — chequeo numérico: la utilidad a izquierda y derecha debe ser MENOR.
f = sp.lambdify(p, U, 'math')
assert f(16500) > f(16400) and f(16500) > f(16600)    # es una cima, no un valle

# Vía 3 — vértice de la parábola (U es cuadrática en p): p* = -b/(2a).
a, b, c = (U.coeff(p,2), U.coeff(p,1), U.coeff(p,0))
assert -b/(2*a) == 16500
print("OK — triple verificación pasa")
```

Las tres vías (sympy, principio marginal, vértice de parábola) coinciden en `p* = 16.500 COP`.

## Ejemplo trabajado

**Problema (packaging, LatAm):** quieres una lata cilíndrica que contenga **1 litro (1000 cm³)** usando la **mínima cantidad de hojalata** (menos material = menos costo, ver [[39-costos-de-material-por-area-y-volumen]]). ¿Qué radio `r` la hace más barata?

Variable de decisión: radio `r` (cm). Restricción: volumen fijo `V = π r² h = 1000`.

1. **Despejar la altura:** `h = 1000 / (π r²)`.
2. **Función objetivo (área total = material):**
   `A(r) = 2π r²  +  2π r h  =  2π r²  +  2000/r`   (cm²).
   El primer término son las dos tapas; el segundo, el costado.
3. **CPO:** `A'(r) = 4π r − 2000/r² = 0  →  r³ = 500/π  →  r = (500/π)^(1/3)`.
4. **CSO:** `A''(r) = 4π + 4000/r³ > 0` siempre → es un **MÍNIMO**. Correcto.

```python
import sympy as sp
r = sp.symbols('r', positive=True)
A = 2*sp.pi*r**2 + 2000/r          # área total (cm^2)
r_opt = sp.solve(sp.diff(A, r), r)[0]
print("r* =", sp.nsimplify(r_opt), "≈", float(r_opt), "cm")
print("A'' =", sp.diff(A, r, 2).subs(r, r_opt), "(positiva -> mínimo)")
print("A mín =", float(A.subs(r, r_opt)), "cm^2")
# Verificación: el óptimo cumple h = 2r (resultado clásico de la lata)
h = 1000/(sp.pi*r_opt**2)
assert sp.simplify(h - 2*r_opt) == 0     # altura = diámetro, característico del mínimo
```

**Resultado:** `r* ≈ 5,419 cm`, altura `h ≈ 10,839 cm` (justo `h = 2r`), área mínima `A ≈ 553,58 cm²`. La verificación `h = 2·r` es la "huella digital" del óptimo de una lata: confirma que no nos equivocamos. Con un costo de hojalata de, por ejemplo, **0,12 COP/cm²**, cada lata óptima usa `553,58 × 0,12 = 66,43 COP` de material (redondear UNA vez al final, ver [[05-cifras-significativas-y-redondeo]]).

## Errores comunes / trampas

- **Olvidar la condición de 2do orden.** Un punto con `f'=0` puede ser máximo, mínimo o ni lo uno ni lo otro (punto de inflexión). Siempre clasifica con `f''` o con el signo de `f'`.
- **Ignorar las fronteras del dominio.** El verdadero máximo puede estar en el borde (`q=0`, capacidad máxima de planta, precio mínimo legal), no en un punto crítico interior. Evalúa SIEMPRE los extremos `a` y `b`.
- **Confundir local con global.** Una función puede tener varias colinas; la más alta es la global. Compara los valores de `f`, no solo cuenta los puntos críticos.
- **Usar `float` en dinero.** `0.20*p` con floats arrastra error binario. Usa `sympy.Rational` o `decimal` para cifras monetarias exactas (ver [[12-fracciones-decimales-y-precision]]).
- **Redondear el precio antes de derivar.** Redondea solo el resultado final, no las variables intermedias.
- **Modelo de demanda inventado.** La derivada es exacta, pero si la fórmula de demanda es falsa, el óptimo es falso ("basura entra, basura sale"). Valida el modelo con datos reales ([[64-regresion-lineal]], [[06-estimacion-y-sanity-checks]]).
- **Unidades mezcladas.** Si `q` es en miles y `p` en COP, `U'` queda en unidades raras. Mantén unidades consistentes ([[04-notacion-unidades-y-dimensiones]]).

## Cruces

- [[41-derivadas-concepto]] — qué es la derivada (la pendiente que aquí igualamos a cero).
- [[42-reglas-de-derivacion]] — cómo calcular `f'` y `f''` paso a paso.
- [[23-ecuaciones-cuadraticas]] — resolver la CPO cuando la utilidad es una parábola (vértice).
- [[91-programacion-lineal]] — optimizar cuando hay restricciones lineales (sin derivadas).
- [[82-pricing-markup-margin-y-elasticidad]] — el precio óptimo conecta con elasticidad de demanda.
- [[80-margenes-bruto-contribucion-neto]] — la utilidad que aquí maximizamos.

---

**Mini-checklist de exactitud**
- [ ] Clasifiqué cada punto crítico con `f''` (o signo de `f'`) — sé si es máximo o mínimo.
- [ ] Comparé los puntos críticos **contra las fronteras del dominio** para el óptimo global.
- [ ] Verifiqué el resultado por una segunda vía (otro método, vértice, o chequeo numérico izquierda/derecha) y todo coincide.
