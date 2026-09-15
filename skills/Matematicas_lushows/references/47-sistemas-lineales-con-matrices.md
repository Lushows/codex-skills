# 47 · Sistemas lineales con matrices

> **Qué resuelve / cuándo usarlo** — Resolver de golpe varias ecuaciones lineales que comparten las mismas incógnitas (ej: "tengo 2 mezclas de café y quiero cierta proporción de cafeína y cierto costo"). Lo escribes como `Ax = b` y lo resuelves con álgebra de matrices, exacto y verificado.

## Concepto (para no-experto)

Imagina que tienes varias preguntas que se responden juntas. Por ejemplo, en un restaurante vendes dos combos y sabes dos cosas: el total de combos vendidos y la plata total que entró. Cada cosa que sabes es una **ecuación**: una afirmación con un signo `=` que relaciona números desconocidos. Cada cantidad desconocida (¿cuántos combos A?, ¿cuántos B?) es una **incógnita**.

Cuando tienes **varias ecuaciones lineales** (lineales = las incógnitas solo se suman y se multiplican por números fijos, nunca se elevan al cuadrado ni se multiplican entre sí) que comparten las mismas incógnitas, eso es un **sistema lineal**. Resolverlo es encontrar los valores de las incógnitas que hacen ciertas TODAS las ecuaciones a la vez.

La forma matricial `Ax = b` es solo una manera ordenada de empaquetar el sistema:

- **A** = la **matriz de coeficientes**: una tabla de números (los multiplicadores que acompañan a cada incógnita). "Matriz" = arreglo rectangular de números en filas y columnas.
- **x** = el **vector de incógnitas**: la columna con las cosas que buscamos. "Vector" aquí = lista de números en columna.
- **b** = el **vector de términos independientes** (los resultados de cada ecuación, el lado derecho del `=`).

Analogía: `A` es una receta que dice cómo combinar los ingredientes `x` para obtener un plato `b`. Resolver `Ax = b` es preguntar al revés: "dado el plato final `b` y la receta `A`, ¿cuánto de cada ingrediente `x` usé?".

**¿Cuándo hay solución única?** Una sola respuesta posible existe cuando tienes **tantas ecuaciones independientes como incógnitas** y ninguna ecuación es repetición o contradicción de otra. El número que detecta esto es el **determinante** de `A` (un número que resume la matriz): si es distinto de cero, hay solución única. Si es cero, o no hay solución, o hay infinitas.

## Fórmulas / método

Sistema con `n` incógnitas y `n` ecuaciones:

```
a11·x1 + a12·x2 + ... + a1n·xn = b1
a21·x1 + a22·x2 + ... + a2n·xn = b2
   ...
an1·x1 + an2·x2 + ... + ann·xn = bn
```

En forma matricial:

```
A · x = b
```

- `A` es `n × n` (n filas, n columnas). `a_ij` = coeficiente de la incógnita `j` en la ecuación `i`.
- `x` es `n × 1` (las incógnitas).
- `b` es `n × 1` (los resultados).

**Solución (concepto):** `x = A⁻¹ · b`, donde `A⁻¹` es la matriz **inversa** (la que "deshace" a `A`, análoga a dividir).

> ⚠️ En la práctica NO se invierte la matriz para resolver. Calcular `A⁻¹` y luego multiplicar es más lento y acumula más error de redondeo. El método correcto es la **eliminación gaussiana** (ir restando filas para despejar), que es lo que hace `numpy.linalg.solve` internamente. Inviertes solo si necesitas `A⁻¹` para otra cosa.

**Criterio de solución única:**

- `det(A) ≠ 0`  →  **una** solución (`A` es invertible / "no singular").
- `det(A) = 0`  →  **cero o infinitas** soluciones (`A` es singular). Hay que analizar el rango para distinguir.

**Unidades:** cada incógnita lleva su unidad (combos, kg, litros, COP). El producto `a_ij · x_j` debe tener la unidad de `b_i`. Si no cuadran las unidades, el sistema está mal planteado.

## Verificación en código

```python
import numpy as np

# Sistema 2x2 (negocio gastronómico):
#   Combo A + Combo B = 50          (total de combos vendidos)
#   12000*A + 18000*B = 750000      (recaudo total en COP)
#
# Incógnitas: A = nº de combos A, B = nº de combos B
A_mat = np.array([
    [1.0,      1.0   ],   # coef. de A y B en la ecuación de unidades
    [12000.0,  18000.0],  # coef. de A y B en la ecuación de plata
])
b_vec = np.array([50.0, 750000.0])

# Paso 0: ¿hay solución única? -> determinante distinto de cero
det = np.linalg.det(A_mat)
print("det(A) =", det)              # si != 0 -> solución única
assert abs(det) > 1e-9, "Matriz singular: no hay solución única"

# Paso 1: resolver con el método correcto (eliminación gaussiana interna)
x = np.linalg.solve(A_mat, b_vec)
print("Combo A =", x[0], " Combo B =", x[1])
```

Verificación por **segunda vía** (sustituir la solución y comprobar que reproduce `b`, más un método independiente):

```python
# Vía 1: residuo A·x - b debe ser ~0 (reconstruir el lado derecho)
b_reconstruido = A_mat @ x          # @ = multiplicación matriz-vector
residuo = b_reconstruido - b_vec
print("residuo:", residuo)
assert np.allclose(b_reconstruido, b_vec, atol=1e-6), "La solución NO satisface el sistema"

# Vía 2: método independiente (regla de Cramer, hecho a mano)
#   x_i = det(A con la columna i reemplazada por b) / det(A)
A1 = A_mat.copy(); A1[:, 0] = b_vec      # columna 0 -> b
A2 = A_mat.copy(); A2[:, 1] = b_vec      # columna 1 -> b
x_cramer = np.array([np.linalg.det(A1)/det, np.linalg.det(A2)/det])
print("Cramer:", x_cramer)
assert np.allclose(x, x_cramer, atol=1e-6), "solve y Cramer no coinciden"

print("OK: solución verificada por residuo y por Cramer")
```

Salida esperada: `Combo A = 25.0  Combo B = 25.0`, residuo ≈ `[0, 0]`, y Cramer coincide.

> **Nota de dinero:** aquí los coeficientes de precio son enteros exactos y la respuesta da entero, así que float es seguro. Si el resultado debe ser dinero con centavos y necesitas exactitud contable, resuelve con racionales usando `sympy` (ver más abajo) en vez de float.

Versión **exacta con fracciones** (sin error de redondeo, ideal cuando los datos son racionales):

```python
import sympy as sp
A = sp.Matrix([[1, 1], [12000, 18000]])
b = sp.Matrix([50, 750000])
x_exacto = A.solve(b)           # resuelve en aritmética racional exacta
print(x_exacto.T)               # Matrix([[25, 25]]) -> exacto, sin 24.9999
```

## Ejemplo trabajado

**Problema (GastroLatam, dark kitchen):** Compras dos insumos para tus salsas. La mezcla de hoy debe tener **3 kg** en total y costar exactamente **$42.000 COP**. El insumo X cuesta **$10.000/kg** y el insumo Y cuesta **$16.000/kg**. ¿Cuántos kg de cada uno?

**Paso 1 — Plantear.** Incógnitas: `x` = kg de X, `y` = kg de Y.

```
x + y = 3                  (kg totales)         [unidad: kg]
10000·x + 16000·y = 42000  (costo total)        [unidad: COP]
```

**Paso 2 — Forma matricial.**

```
A = [[1,      1   ],     b = [3,
     [10000,  16000]]         42000]
```

**Paso 3 — ¿Solución única?** `det(A) = 1·16000 − 1·10000 = 6000 ≠ 0` → sí, hay una única respuesta.

**Paso 4 — Resolver (Cramer, a mano para que se vea):**

- `det(A) = 6000`
- `x = det([[3,1],[42000,16000]]) / 6000 = (3·16000 − 1·42000)/6000 = (48000 − 42000)/6000 = 6000/6000 = 1`
- `y = det([[1,3],[10000,42000]]) / 6000 = (1·42000 − 3·10000)/6000 = (42000 − 30000)/6000 = 12000/6000 = 2`

**Resultado:** `x = 1 kg` de insumo X y `y = 2 kg` de insumo Y.

**Verificación con unidades:**
- Total: `1 kg + 2 kg = 3 kg` ✓
- Costo: `1 kg · 10.000 COP/kg + 2 kg · 16.000 COP/kg = 10.000 + 32.000 = 42.000 COP` ✓

Confirmado con código:

```python
import numpy as np
A = np.array([[1.,1.],[10000.,16000.]]); b = np.array([3.,42000.])
x = np.linalg.solve(A, b)
assert np.allclose(A @ x, b)
print(x)   # [1. 2.]  -> kg de X, kg de Y
```

## Errores comunes / trampas

- **Invertir la matriz para resolver.** `np.linalg.inv(A) @ b` funciona pero es más lento y menos preciso que `np.linalg.solve(A, b)`. Usa `solve` siempre que solo quieras `x`.
- **No revisar el determinante.** Si `det(A) = 0` la matriz es **singular**: `solve` lanzará `LinAlgError` o dará basura. Significa que tus ecuaciones se repiten (información redundante) o se contradicen (sistema imposible). Revisa el planteamiento, no fuerces un número.
- **Casi-singular (mal condicionado).** Si `det(A)` es diminuto comparado con los datos, pequeñas variaciones en `b` cambian mucho `x`: la respuesta es poco confiable. Mide con `np.linalg.cond(A)`; un número de condición enorme (p. ej. > 1e8) es bandera roja.
- **Confundir filas y columnas.** En `A·x`, cada **fila** de `A` es una ecuación. Si transpones por error, resuelves otro sistema. Verifica reconstruyendo `b = A @ x`.
- **Comparar floats con `==`.** Por redondeo, `x` puede dar `24.9999999`. Compara con `np.allclose`, o resuelve exacto con `sympy`/`fractions` si los datos son racionales.
- **Olvidar las unidades.** Cada incógnita y cada `b_i` tiene unidad. Si un término no cuadra dimensionalmente, el sistema está mal armado (no lo "arregles" cambiando números).

## Cruces

- [[22-sistemas-de-ecuaciones]] — el mismo problema sin matrices (sustitución/igualación); empieza aquí si es 2×2.
- [[46-matrices-y-operaciones]] — qué es una matriz y cómo se multiplican (base de `Ax`).
- [[48-determinantes-e-inversas]] — el determinante (criterio de unicidad) y la inversa `A⁻¹` en detalle.
- [[35-vectores]] — `x` y `b` son vectores columna.
- [[91-programacion-lineal]] — cuando además hay desigualdades y un objetivo a optimizar (no solo `=`).

---

**Mini-checklist de exactitud**
- [ ] Calculé `det(A)` (o `cond(A)`) y confirmé que hay solución única antes de confiar en `x`.
- [ ] Verifiqué por segunda vía: `A @ x` reproduce `b` (`np.allclose`) y/o coincide con Cramer/`sympy`.
- [ ] Cada incógnita y resultado lleva su unidad y las dimensiones cuadran.
