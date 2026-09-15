# 46 · Matrices y operaciones

> **Qué resuelve / cuándo usarlo** — Cuando tienes datos organizados en tablas (filas × columnas) o varias ecuaciones a la vez, y necesitas sumarlos, combinarlos, escalarlos o transformarlos de forma exacta. Es la base para sistemas lineales, regresión, gráficos, optimización y machine learning.

## Concepto (para no-experto)

Una **matriz** es simplemente una **tabla rectangular de números** ordenados en **filas** (líneas horizontales) y **columnas** (líneas verticales). Nada más. Si alguna vez viste una hoja de Excel con números, ya viste una matriz.

Ejemplo cotidiano: tus ventas de 2 productos en 3 días.

```
            Día1  Día2  Día3
Empanadas [  12    15    9  ]
Jugos     [   8    10   14  ]
```

Eso es una matriz de **2 filas y 3 columnas**, que escribimos como una matriz **2×3** (se lee "dos por tres"; siempre va **filas primero, columnas después**).

Términos que usaremos (los defino una sola vez):

- **Elemento (o entrada)**: cada número dentro de la tabla. Lo ubicamos con dos índices: `a[i][j]` = el número en la **fila i**, **columna j**. En el ejemplo, jugos del día 1 = 8, que es `a[2][1]` (fila 2, columna 1).
- **Dimensión / orden**: el tamaño "filas × columnas". La del ejemplo es 2×3.
- **Vector**: una matriz con una sola fila (vector fila) o una sola columna (vector columna). Es el caso más simple de matriz. (Ver [[35-vectores]].)
- **Matriz cuadrada**: tiene igual número de filas que de columnas (2×2, 3×3...).
- **Escalar**: un número solo (no una tabla), como 3 o 0.5. "Escalar una matriz" = multiplicar cada elemento por ese número.
- **Transpuesta**: voltear la tabla cambiando filas por columnas (como girar la hoja 90° y reflejarla).

**Analogía del producto de matrices**: imagina que tienes (1) una tabla de cuántas unidades vendiste de cada producto y (2) una tabla con el precio de cada producto. Multiplicar matrices es la máquina que combina ambas tablas para darte, de golpe, el ingreso total — fila por columna, sumando los productos cruzados. Es "filas con columnas".

## Fórmulas / método

Sea `A` una matriz `m×n` (m filas, n columnas) y `a_ij` su elemento en fila *i*, columna *j*.

**1) Suma / resta** (solo si tienen **la misma dimensión**):
```
(A + B)_ij = a_ij + b_ij     (elemento a elemento)
```

**2) Multiplicación por escalar** `k` (un número):
```
(k·A)_ij = k · a_ij          (multiplica cada elemento)
```

**3) Transpuesta** `Aᵀ` (la "T" arriba significa transpuesta) — la fila *i* se vuelve columna *i*:
```
(Aᵀ)_ij = a_ji              (intercambia índices; si A es m×n, Aᵀ es n×m)
```

**4) Producto matricial** `A · B`:
- **Regla de compatibilidad (CRÍTICA)**: solo se puede si las **columnas de A = filas de B**. Si `A` es `m×n` y `B` es `n×p`, el resultado `C` es `m×p`. La dimensión interior (n) debe coincidir y "desaparece".
- Cada elemento del resultado:
```
c_ij = Σ_{k=1..n}  a_ik · b_kj
```
Es decir: tomo la **fila i de A** y la **columna j de B**, multiplico par a par y sumo. (`Σ` = sumatoria, sumar todo lo que sigue.)

> ⚠️ El producto de matrices **NO es conmutativo**: en general `A·B ≠ B·A`. El orden importa. Esta es la trampa #1.

**Unidades**: en `c_ij = Σ a_ik · b_kj`, las unidades se multiplican. Si A está en *unidades vendidas* y B en *COP/unidad*, entonces C está en *COP*. (Ver [[04-notacion-unidades-y-dimensiones]].)

## Verificación en código

Filosofía error cero: **nunca multiplicamos matrices a mano de memoria**. Ejecutamos en código y verificamos por segunda vía.

```python
import numpy as np
from fractions import Fraction

# --- DATOS ---
# Unidades vendidas: 2 productos (filas) x 3 dias (columnas)  -> matriz 2x3
A = np.array([[12, 15,  9],
              [ 8, 10, 14]])

# Precio unitario por producto (COP): vector columna 2x1
precio = np.array([[ 3500],    # empanada
                   [ 2500]])   # jugo

print("A es", A.shape, "| precio es", precio.shape)  # (2,3) y (2,1)

# 1) SUMA elemento a elemento (con otra matriz de igual dimension)
B = np.array([[1, 0, 2],
              [3, 1, 0]])
suma = A + B
print("A+B =\n", suma)

# 2) ESCALAR: subir todos los precios 10%
precio_subido = precio * Fraction(11, 10)   # 1.10 EXACTO con fraccion, sin float
print("precio +10% (COP) =\n", precio_subido.astype(object))

# 3) TRANSPUESTA: queremos dias en filas, productos en columnas
At = A.T
print("A^T es", At.shape, "\n", At)          # (3,2)

# 4) PRODUCTO: ingreso por dia = (precio^T) . A  -> (1x2)(2x3) = 1x3
#    columnas de precio^T (2) == filas de A (2)  -> compatible
ingreso_dia = precio.T @ A    # @ es el operador de producto matricial
print("Ingreso por dia (COP) =", ingreso_dia.ravel())
```

**Verificación por segunda vía** (calculamos lo mismo "a mano" con bucles y enteros exactos, y comparamos con `assert`):

```python
# Segunda via: producto manual con enteros (cero floats) para confirmar numpy
precios = [3500, 2500]                 # COP por producto
unidades = [[12, 15, 9],
            [ 8, 10, 14]]
dias = 3
ingreso_manual = []
for j in range(dias):                  # para cada dia (columna)
    total = 0
    for i in range(2):                 # sumar sobre productos (filas)
        total += precios[i] * unidades[i][j]   # COP/u * u = COP
    ingreso_manual.append(total)

print("Ingreso manual (COP) =", ingreso_manual)
assert ingreso_manual == [42000+20000, 52500+25000, 31500+35000]
assert list(ingreso_dia.ravel()) == ingreso_manual   # numpy == manual -> OK

# Verificacion extra: (A^T)^T debe devolver A (propiedad de la transpuesta)
assert np.array_equal(A.T.T, A)
# Verificacion extra: no conmutatividad ilustrada
P = np.array([[1,2],[3,4]]); Q = np.array([[0,1],[1,0]])
assert not np.array_equal(P @ Q, Q @ P)   # A·B != B·A en general
print("Todas las verificaciones pasaron.")
```

Salida esperada: `Ingreso por dia (COP) = [62000 77500 66500]` y `Todas las verificaciones pasaron.`

## Ejemplo trabajado

**Situación (GastroLatam, Colombia):** un food truck vende 3 productos en 2 sucursales. Quieres el **ingreso total por sucursal** en un solo cálculo.

Unidades vendidas (matriz `U`, 2 sucursales × 3 productos):

```
              Empanada  Jugo  Arepa
Sucursal A  [   40       25    30  ]
Sucursal B  [   18       12    50  ]
```

Precios (vector columna `p`, 3 productos × 1), en COP: empanada 3.500, jugo 2.500, arepa 4.000.

**Compatibilidad:** `U` es 2×3 y `p` es 3×1. Columnas de U (3) = filas de p (3) → producto válido, resultado **2×1** (ingreso por sucursal). La dimensión interior 3 desaparece.

**Cálculo `U · p`:**
- Sucursal A: 40·3500 + 25·2500 + 30·4000 = 140.000 + 62.500 + 120.000 = **322.500 COP**
- Sucursal B: 18·3500 + 12·2500 + 50·4000 = 63.000 + 30.000 + 200.000 = **293.000 COP**

```python
import numpy as np
U = np.array([[40,25,30],[18,12,50]])
p = np.array([[3500],[2500],[4000]])
ingreso = U @ p                      # 2x3 . 3x1 -> 2x1
print(ingreso.ravel())               # [322500 293000]
# Segunda via: suma directa (sanity check de orden de magnitud)
assert ingreso[0,0] == 40*3500 + 25*2500 + 30*4000 == 322500
assert ingreso[1,0] == 18*3500 + 12*2500 + 50*4000 == 293000
```

**Resultado:** Sucursal A = **322.500 COP**, Sucursal B = **293.000 COP**. Total del día = **615.500 COP**.

Sanity check de orden de magnitud (ver [[06-estimacion-y-sanity-checks]]): ~95 unidades por sucursal a un precio promedio de ~3.300 COP → del orden de 300.000 COP cada una. Coincide. ✓

## Errores comunes / trampas

- **Sumar matrices de distinta dimensión.** Solo se suman/restan si son del **mismo tamaño**. numpy a veces "ayuda" con *broadcasting* (estira automáticamente) y puede dar un resultado que NO es la suma que querías. Verifica `.shape` antes.
- **Multiplicar sin compatibilidad.** Si columnas de A ≠ filas de B, el producto no existe. Pega el chequeo `A.shape[1] == B.shape[0]`.
- **Confundir orden:** `A·B ≠ B·A`. Si pones precio×unidades en el orden equivocado, las dimensiones no cuadran o el número sale absurdo.
- **`*` vs `@` en numpy.** `A * B` multiplica **elemento a elemento** (Hadamard); `A @ B` es el **producto matricial**. Es el error silencioso más caro: ambos pueden "funcionar" y dar números falsos.
- **Filas/columnas al revés.** "m×n" es **filas × columnas**, siempre en ese orden. Etiqueta tus ejes.
- **Dinero con float.** Para precios usa enteros en centavos/pesos o `Fraction`/`Decimal`; los float introducen errores de redondeo (ver [[12-fracciones-decimales-y-precision]]).
- **Olvidar las unidades.** Verifica que el resultado tenga sentido dimensional: unidades × (COP/unidad) = COP.

### Mini-checklist de exactitud
- [ ] Verifiqué `.shape` de cada matriz y la **compatibilidad** del producto (columnas A = filas B).
- [ ] Usé `@` para producto matricial (no `*`) y confirmé por una **segunda vía** (bucle/assert).
- [ ] El resultado tiene la **dimensión** y las **unidades** correctas, y pasa el sanity check de magnitud.

## Cruces
- [[35-vectores]] — el vector es el caso más simple de matriz; fila o columna.
- [[47-sistemas-lineales-con-matrices]] — resolver varias ecuaciones a la vez con la forma `A·x = b`.
- [[48-determinantes-e-inversas]] — invertir matrices y medir si un sistema tiene solución única.
- [[64-regresion-lineal]] — la regresión se calcula con álgebra matricial (`Xᵀ·X`).
- [[03-protocolo-de-verificacion-por-codigo]] — el patrón ejecutar + verificar que usamos aquí.
