# 48 · Determinantes e inversas

> **Qué resuelve / cuándo usarlo** — Para saber si un sistema de ecuaciones tiene solución única (y cuál), si una matriz se puede "deshacer", y para medir cuánto estira o aplasta el espacio una transformación. Es el chequeo de "¿esto es resoluble?" antes de gastar tiempo resolviéndolo.

## Concepto (para no-experto)

Una **matriz** es una tabla rectangular de números organizada en filas y columnas (la primera vez: filas = horizontales, columnas = verticales). Una matriz **cuadrada** tiene el mismo número de filas que de columnas (2×2, 3×3, etc.).

El **determinante** es un único número que resume una matriz cuadrada. Su significado geométrico es el más intuitivo: el determinante mide **el factor por el que la matriz cambia el área (en 2D) o el volumen (en 3D)**.

- Analogía: imagina una cuadrícula de baldosas. Si aplicas una transformación con determinante = 2, cada baldosa de área 1 pasa a tener área 2 (todo se duplica). Si el determinante = 0.5, todo se encoge a la mitad. Si el determinante = **0**, las baldosas se aplastan en una línea (área cero): la transformación **colapsó una dimensión** y perdió información — ya no se puede deshacer.

La **matriz inversa** de A (se escribe A⁻¹) es la matriz que "deshace" lo que A hace. Como dividir entre un número: 5 × (1/5) = 1; aquí A × A⁻¹ = I, donde **I es la matriz identidad** (unos en la diagonal, ceros en el resto — el "1" de las matrices, no cambia nada al multiplicar).

La conexión clave:
- Si **det(A) ≠ 0** → la matriz NO aplastó dimensiones → **tiene inversa** → el sistema A·x = b tiene **solución única**. Se dice que A es **invertible** o **no singular**.
- Si **det(A) = 0** → la matriz aplastó una dimensión → **NO tiene inversa** → el sistema tiene **infinitas soluciones o ninguna**. Se dice que A es **singular**.

Ejemplo cotidiano: tres ofertas de combos de comida con tres precios totales. Si las ofertas son "independientes" (cada una aporta información nueva), puedes despejar el precio individual de cada plato → det ≠ 0. Si una oferta es solo "el doble de otra", no aporta nada nuevo → det = 0 → no puedes despejar precios únicos.

## Fórmulas / método

**Determinante 2×2.** Para A = [[a, b], [c, d]]:

```
det(A) = a·d − b·c
```

**Determinante 3×3** (regla de Sarrus o expansión por cofactores). Para A = [[a,b,c],[d,e,f],[g,h,i]]:

```
det(A) = a(e·i − f·h) − b(d·i − f·g) + c(d·h − e·g)
```

**Inversa 2×2** (solo si det ≠ 0):

```
A⁻¹ = (1 / det(A)) · [[ d, −b],
                       [−c,  a]]
```

(se intercambia a↔d, se cambia el signo de b y c, y se divide todo entre el determinante).

**Inversa general** (n×n): A⁻¹ = adj(A) / det(A), donde adj(A) es la **matriz adjunta** (transpuesta de la matriz de cofactores). En la práctica NO se calcula así a mano para n>3 — se usa eliminación de Gauss-Jordan o software.

**Regla de Cramer** (resolver A·x = b cuando det ≠ 0): cada incógnita xⱼ = det(Aⱼ) / det(A), donde Aⱼ es A con su columna j reemplazada por el vector b.

**Símbolos:** A = matriz cuadrada n×n; det(A) o |A| = determinante (un escalar, sin unidades propias salvo que las entradas las tengan); I = identidad; A⁻¹ = inversa; x = vector de incógnitas; b = vector de términos independientes.

**Regla de oro de exactitud:** si las entradas son enteros o fracciones exactas, calcula con **fracciones** (no float), porque det(A) puede dar exactamente 0 y el float puede mostrar `1e-16` y engañarte.

## Verificación en código

```python
# Determinante, inversa y resolubilidad EXACTOS con sympy (aritmética simbólica/racional).
from sympy import Matrix, Rational, eye

# Matriz de ejemplo (3x3 con enteros)
A = Matrix([
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0],
])

det = A.det()                 # determinante EXACTO (entero, no float)
print("det(A) =", det)        # -> -1

if det != 0:
    Ainv = A.inv()            # inversa EXACTA (fracciones)
    print("A^-1 =\n", Ainv)
    es_invertible = True
else:
    es_invertible = False
    print("Singular: no tiene inversa, sistema no tiene solucion unica")

# ---- VERIFICACION POR SEGUNDA VIA ----
# Via 1: la definicion de inversa exige A * A^-1 = I  (identidad)
I3 = eye(3)
assert A * Ainv == I3,  "FALLO: A * A^-1 no da la identidad"
assert Ainv * A == I3,  "FALLO: A^-1 * A no da la identidad"

# Via 2: propiedad det(A^-1) = 1/det(A)
assert Ainv.det() == Rational(1, det), "FALLO: det(inversa) != 1/det(A)"

# Via 3: chequeo independiente del determinante por expansion de Sarrus a mano
a,b,c = 2,1,1
d,e,f = 1,3,2
g,h,i = 1,0,0
det_sarrus = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
assert det_sarrus == det, "FALLO: Sarrus discrepa del det de sympy"

print("OK: inversa y determinante verificados por 3 vias")
```

```python
# Caso SINGULAR: detectar que NO es resoluble (det = 0 exacto)
from sympy import Matrix
S = Matrix([
    [1, 2],
    [2, 4],   # fila 2 = 2 x fila 1  -> dependiente -> det = 0
])
print("det(S) =", S.det())          # -> 0 EXACTO (no 1e-16)
print("invertible?", S.det() != 0)  # -> False
# S.inv() lanzaria NonInvertibleMatrixError: correcto, no hay inversa.
```

## Ejemplo trabajado

**Problema (LatAm).** En un restaurante, tres clientes piden combinaciones de arepa (precio a) y jugo (precio j), en pesos colombianos (COP):

- Cliente 1: 2 arepas + 1 jugo = 16 000 COP
- Cliente 2: 1 arepa + 3 jugos = 23 000 COP

¿Cuánto cuesta cada arepa y cada jugo?

**Planteo matricial.** A·x = b con

```
A = [[2, 1],     x = [a]     b = [16000]
     [1, 3]]         [j]         [23000]   (todo en COP)
```

**Paso 1 — ¿es resoluble?** det(A) = 2·3 − 1·1 = 6 − 1 = **5**. Como 5 ≠ 0 → solución única. ✔

**Paso 2 — inversa:**
```
A⁻¹ = (1/5)·[[ 3, −1],
             [−1,  2]]
```

**Paso 3 — x = A⁻¹·b:**
```
a = (1/5)·( 3·16000 − 1·23000) = (1/5)·(48000 − 23000) = 25000/5 = 5 000 COP
j = (1/5)·(−1·16000 + 2·23000) = (1/5)·(−16000 + 46000) = 30000/5 = 6 000 COP
```

**Resultado:** arepa = **5 000 COP**, jugo = **6 000 COP**.

**Verificación (sustituir en las ecuaciones originales):**
- Cliente 1: 2·5000 + 1·6000 = 10000 + 6000 = 16 000 COP ✔
- Cliente 2: 1·5000 + 3·6000 = 5000 + 18000 = 23 000 COP ✔

```python
from sympy import Matrix, Rational
A = Matrix([[2,1],[1,3]]); b = Matrix([16000, 23000])
assert A.det() == 5
x = A.inv() * b
assert x == Matrix([5000, 6000])          # via inversa
assert (A*x) == b                          # via sustitucion (segunda via)
# Tercera via: regla de Cramer
a_cramer = Matrix([[16000,1],[23000,3]]).det() / A.det()
assert a_cramer == 5000
print("arepa=5000 COP, jugo=6000 COP, verificado")
```

## Errores comunes / trampas

- **Calcular det a ojo y equivocar un signo.** En 3×3 el patrón de signos es +, −, +. Un signo mal cambia todo. Solución: ejecútalo en código.
- **Float que finge det = 0.** Con `numpy.linalg.det` una matriz singular puede dar `-1.1e-16` (basura numérica). NUNCA compares `det == 0` con floats; usa sympy/fracciones para la decisión de resolubilidad, o un umbral con `numpy.linalg.matrix_rank`.
- **Invertir una matriz singular.** Si det = 0 NO existe inversa: cualquier "inversa" que arroje un programa es un error o ruido. Comprueba det ≠ 0 ANTES.
- **Orden de multiplicación.** Las matrices NO conmutan: x = A⁻¹·b, no b·A⁻¹. A izquierda siempre.
- **Usar la inversa para "solo resolver un sistema".** Calcular A⁻¹ es más caro y menos preciso que resolver directo (Gauss / `numpy.linalg.solve`). La inversa es para teoría o cuando reusas A⁻¹ muchas veces.
- **Matriz no cuadrada.** Determinante e inversa solo existen para matrices cuadradas. Para rectangulares se usan otras herramientas (pseudoinversa).

**Mini-checklist de exactitud**
- [ ] ¿Confirmé det ≠ 0 con aritmética exacta (no float) antes de afirmar "tiene solución única"?
- [ ] ¿Verifiqué la inversa con A·A⁻¹ = I y la solución sustituyéndola en el sistema original?

## Cruces
- [[46-matrices-y-operaciones]] — qué es una matriz y cómo se multiplican (base de todo esto).
- [[47-sistemas-lineales-con-matrices]] — plantear A·x = b y resolverlo con Gauss/solve.
- [[22-sistemas-de-ecuaciones]] — la versión sin matrices del mismo problema.
- [[49-eigenvalores-y-descomposiciones]] — cuando det = 0 hay un eigenvalor 0; descomposiciones más estables que la inversa.
- [[03-protocolo-de-verificacion-por-codigo]] — por qué todo cálculo no trivial se ejecuta y se doble-verifica.
