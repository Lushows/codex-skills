# 25 · Funciones: concepto, dominio y rango

> **Qué resuelve / cuándo usarlo** — Cuando necesitas modelar una relación "una entrada → una salida" (precio según cantidad, ingreso según unidades vendidas, costo según área) y saber QUÉ valores de entrada son válidos (dominio) y QUÉ resultados puede producir (rango), evaluarla, encadenarla con otra (composición) o "deshacerla" (inversa).

## Concepto (para no-experto)

Una **función** es una regla que toma un número de entrada y le asigna **exactamente un** número de salida. La condición "exactamente uno" es lo que la hace función: para una misma entrada nunca puede haber dos resultados distintos.

Analogía: una máquina expendedora. Pones el código **A3** (entrada) y sale **una** gaseosa específica (salida). Si al pulsar A3 a veces saliera gaseosa y a veces papas, no sería una función: sería impredecible. En negocio igual: "si vendo 100 unidades, mi ingreso es X" — un solo X por cada cantidad.

Términos clave (definidos la primera vez que aparecen):

- **Variable independiente (entrada)**: el número que tú eliges/controlas. Suele llamarse `x`.
- **Variable dependiente (salida)**: el resultado que la función produce. Suele llamarse `y` o `f(x)` (se lee "f de x").
- **Dominio** (en inglés *domain*): el conjunto de TODAS las entradas válidas. Es decir, qué valores de `x` puedo meter sin "romper" la regla.
- **Rango** o **recorrido / imagen** (en inglés *range / image*): el conjunto de TODAS las salidas que la función realmente puede producir cuando recorres todo el dominio.
- **Evaluar**: meter un número concreto en la función y calcular su salida. Evaluar `f` en `x = 5` es calcular `f(5)`.
- **Composición**: encadenar dos funciones; la salida de una es la entrada de la otra. Se escribe `(g ∘ f)(x) = g(f(x))` — "primero aplico f, luego g".
- **Función inversa**: la regla que **deshace** lo que hizo la función. Si `f` convierte 5 en 12, su inversa `f⁻¹` convierte 12 de vuelta en 5.

¿Por qué importa el dominio en negocio? Porque limita la realidad. Si `x` es "número de empleados", el dominio no incluye `x = 3.7` ni `x = -2`: solo enteros ≥ 0. Calcular con valores fuera del dominio produce números falsos.

## Fórmulas / método

Notación de función:

```
f : D → C
y = f(x)
```

- `D` = **dominio** (conjunto de entradas válidas).
- `C` = **codominio** (conjunto donde "viven" las salidas posibles; el **rango** es el subconjunto de `C` que de verdad se alcanza).
- `f(x)` = salida correspondiente a la entrada `x`. Unidades: las que correspondan al contexto (p. ej. `x` en unidades, `f(x)` en COP).

**Cómo hallar el dominio** (qué `x` rompen la regla):
- División: el denominador no puede ser `0` → excluir esos `x`.
- Raíz par (√): lo de adentro debe ser `≥ 0`.
- Logaritmo: su argumento debe ser `> 0` (estrictamente).
- Contexto del negocio: cantidades físicas suelen exigir `x ≥ 0` y, a veces, enteros.

**Composición** (orden importa, casi nunca conmuta):
```
(g ∘ f)(x) = g( f(x) )      # primero f, luego g
```
Regla del dominio de la composición: `x` debe estar en el dominio de `f`, **y** `f(x)` debe estar en el dominio de `g`.

**Inversa** (existe solo si `f` es **inyectiva** = cada salida proviene de una sola entrada; "uno a uno"):
```
y = f(x)   ⇔   x = f⁻¹(y)
f⁻¹( f(x) ) = x   y   f( f⁻¹(y) ) = y      # se deshacen mutuamente
```
Para hallar la inversa algebraicamente: escribe `y = f(x)`, despeja `x` en términos de `y`, e intercambia los nombres.

## Verificación en código

Modelo de negocio: ingreso por venta de la Calculadora de Costos a $10.000 COP la unidad, con un costo fijo de plataforma de $50.000 COP. La utilidad como función de las unidades `x`: `f(x) = 10000·x − 50000`. Comprobamos evaluación, dominio, rango, composición e inversa de forma EXACTA con dinero entero (sin float).

```python
from sympy import symbols, Eq, solve, Rational, S, simplify, oo
from sympy.calculus.util import function_range, continuous_domain

x = symbols('x', real=True)

# --- Función de utilidad (dinero en COP, enteros: usamos racionales exactos) ---
f = 10000*x - 50000          # utilidad según unidades vendidas

# 1) EVALUACIÓN: utilidad si vende 8 unidades
util_8 = f.subs(x, 8)
print("f(8) =", util_8, "COP")                # 30000

# 2) DOMINIO matemático de f (polinomio de 1er grado: todos los reales)
dom = continuous_domain(f, x, S.Reals)
print("Dominio matematico:", dom)             # Reals

# 3) RANGO matemático sobre los reales
rng = function_range(f, x, S.Reals)
print("Rango matematico:", rng)               # Reals

# 4) PUNTO DE EQUILIBRIO: unidades para utilidad = 0 (cruce con módulo 76)
breakeven = solve(Eq(f, 0), x)[0]
print("Punto de equilibrio:", breakeven, "unidades")   # 5

# 5) INVERSA: dado un objetivo de utilidad y, ¿cuántas unidades x?
y = symbols('y', real=True)
inv = solve(Eq(f, y), x)[0]                   # x en funcion de y
print("Inversa f^-1(y) =", inv)               # y/10000 + 5

# 6) COMPOSICIÓN: aplicar 19% de IVA sobre la utilidad -> g(u) = u*119/100
g = symbols('u')
g_expr = symbols('u')*Rational(119, 100)
comp = (10000*x - 50000)*Rational(119, 100)   # g(f(x))
print("g(f(4)) =", comp.subs(x, 4), "COP")    # utilidad con IVA en x=4
```

Verificación por **segunda vía** (operación inversa + identidad de la inversa, con `assert`):

```python
# (a) La inversa debe deshacer a f: f^-1(f(8)) == 8
assert inv.subs(y, f.subs(x, 8)) == 8, "La inversa NO deshace a f"

# (b) Chequeo del punto de equilibrio por sustitucion directa
assert f.subs(x, 5) == 0, "Breakeven mal calculado"

# (c) Sanity check de orden de magnitud para f(8):
#     8 unidades * 10.000 = 80.000 ; menos 50.000 = 30.000. Coincide con util_8.
assert util_8 == 8*10000 - 50000 == 30000

print("Verificaciones OK: inversa, equilibrio y magnitud cuadran.")
```

Salida esperada (resumen): `f(8) = 30000`, dominio y rango `Reals`, equilibrio `5`, inversa `y/10000 + 5`, y todos los `assert` pasan.

## Ejemplo trabajado

**Situación (GastroLatam):** modelar el costo por hora de un dark kitchen.
Costo: arriendo fijo de $40.000 COP por turno más $3.000 COP por cada hora `h` operada.

1. **Función:** `C(h) = 3000·h + 40000`  (salida en COP, entrada `h` en horas).
2. **Dominio (con contexto):** un turno operativo va de 0 a 12 horas → `h ∈ [0, 12]`, horas reales no negativas. Matemáticamente la recta acepta cualquier real, pero el negocio restringe el dominio.
3. **Evaluar en `h = 6`:** `C(6) = 3000·6 + 40000 = 18000 + 40000 = 58000 COP`.
4. **Rango (sobre el dominio real [0,12]):** como la función crece, el mínimo está en `h = 0` (`C(0) = 40000`) y el máximo en `h = 12` (`C(12) = 76000`). Rango = `[40000, 76000] COP`.
5. **Inversa (¿cuántas horas para un presupuesto dado?):** despejo `h`:
   `C = 3000h + 40000 → h = (C − 40000) / 3000`. Con presupuesto `C = 58000`: `h = (58000 − 40000)/3000 = 18000/3000 = 6 horas`. ✔ coincide con el paso 3 (la inversa deshace la evaluación).
6. **Verificación de magnitud:** 6 horas a 3.000 son 18.000, más el fijo de 40.000 → 58.000 COP. Cuadra.

**Resultado:** `C(6) = 58.000 COP`; dominio operativo `[0, 12] horas`; rango `[40.000, 76.000] COP`; la inversa confirma 6 horas para un presupuesto de 58.000 COP.

## Errores comunes / trampas

- **Confundir dominio con rango.** Dominio = entradas válidas; rango = salidas alcanzables. No son lo mismo.
- **Olvidar restringir el dominio por el negocio.** Una recta acepta `h = -3` o `h = 4.7`, pero "horas de turno" no. Calcular fuera del dominio da números sin sentido.
- **No verificar división por cero / raíz de negativo / log de no positivo** antes de evaluar: producen error o resultado complejo.
- **Suponer que la inversa siempre existe.** Solo las funciones inyectivas (uno a uno) tienen inversa propia. `f(x) = x²` sobre todos los reales no es invertible (12 viene de +√12 y −√12).
- **Invertir el orden de la composición.** `g(f(x))` ≠ `f(g(x))` en general. Define qué se aplica primero.
- **Pensar que una relación es función cuando no lo es** ("prueba de la línea vertical": si una vertical corta la gráfica en dos puntos, hay una entrada con dos salidas → NO es función).
- **Redondear en pasos intermedios.** Mantén exacto (racionales/decimal) y redondea una sola vez al final.

## Cruces

- [[26-funciones-lineales-y-afines]] — el caso más común en negocio (costo, ingreso, utilidad como rectas).
- [[27-funciones-exponenciales-y-logaritmicas]] — funciones con dominio/rango restringidos (log requiere argumento > 0).
- [[21-ecuaciones-lineales]] — despejar es la base de evaluar e invertir.
- [[34-coordenadas-y-plano-cartesiano]] — graficar una función y leer su dominio/rango visualmente.
- [[76-punto-de-equilibrio]] — caso de uso directo: raíz de la función de utilidad.

**Mini-checklist de exactitud**
- [ ] Verifiqué que cada `x` usado pertenece al dominio (sin división por 0, raíz negativa ni log ≤ 0 ni valores imposibles en el negocio).
- [ ] Confirmé el resultado por segunda vía (inversa que deshace la evaluación o sanity check de magnitud).
- [ ] Llevé unidades en cada salida y redondeé una sola vez al final.
