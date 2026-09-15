# 49 · Eigenvalores y descomposiciones

> **Qué resuelve / cuándo usarlo** — Encontrar las "direcciones propias" de una matriz (las que solo se estiran, no se giran) y descomponer datos en sus componentes principales. Es la base matemática de PCA, reducción de dimensión, sistemas de recomendación, PageRank y casi todo machine learning.

## Concepto (para no-experto)

Imagina que una **matriz** (una tabla de números que actúa como una "máquina" que transforma vectores) toma una flecha y la mueve: la rota, la estira o la encoge. Para la mayoría de las flechas, la dirección cambia. Pero algunas flechas especiales, al pasar por la máquina, **siguen apuntando exactamente a la misma dirección** — solo se hacen más largas o más cortas. Esas flechas son los **eigenvectores** (vectores propios), y el factor por el que se estiran o encogen es el **eigenvalor** (valor propio).

Analogía cotidiana: una hoja de masa que estiras con un rodillo. Casi todos los granos de harina se mueven en diagonal, pero los que están justo sobre el eje en que empujas solo se alejan en línea recta. Ese eje es el eigenvector; cuánto se estira la masa en ese eje es el eigenvalor.

- **Eigenvalor (λ, lambda):** número escalar. Cuánto se estira (λ>1), encoge (0<λ<1), o invierte (λ<0) el eigenvector.
- **Eigenvector (v):** dirección que la matriz no rota, solo escala.
- **PCA (Análisis de Componentes Principales):** técnica que busca, en una nube de datos, las direcciones donde los datos más se "dispersan". Esas direcciones son los eigenvectores de la **matriz de covarianza** (tabla que mide cómo varían juntas las variables). Sirve para resumir muchas columnas en pocas sin perder la información importante.

Por qué importa con dinero/datos: si tienes 30 métricas de tus clientes, PCA puede decirte que en realidad 2 o 3 "ejes" explican el 90% de las diferencias entre ellos. Decides sobre esos pocos ejes en vez de ahogarte en 30 columnas.

## Fórmulas / método

La definición central, la **ecuación de eigenvalores**:

```
A · v = λ · v        con v ≠ 0
```

- `A` = matriz cuadrada n×n (la transformación).
- `v` = eigenvector (vector columna n×1, no nulo). Adimensional o en las unidades del espacio.
- `λ` = eigenvalor (escalar). Sin unidades si A es adimensional.

Para hallar los λ se resuelve el **polinomio característico**:

```
det(A − λ·I) = 0
```

- `det` = determinante (ver [[48-determinantes-e-inversas]]).
- `I` = matriz identidad (1 en la diagonal, 0 fuera).

**Descomposición espectral (diagonalización):** si A tiene n eigenvectores independientes:

```
A = V · D · V⁻¹
```

- `V` = matriz cuyas columnas son los eigenvectores.
- `D` = matriz diagonal con los eigenvalores.
- `V⁻¹` = inversa de V.

**SVD (Descomposición en Valores Singulares):** funciona para CUALQUIER matriz (no solo cuadrada):

```
A = U · Σ · Vᵀ
```

- `Σ` (sigma) = diagonal con los **valores singulares** σᵢ ≥ 0.
- `U`, `V` = matrices ortogonales (columnas perpendiculares de longitud 1).

**PCA en términos de eigenvalores:** sobre la matriz de covarianza `C`, cada eigenvalor λᵢ = varianza capturada por su componente. La **proporción de varianza explicada** del componente i es:

```
varianza_explicada_i = λᵢ / (λ₁ + λ₂ + ... + λₙ)
```

## Verificación en código

```python
# Eigenvalores y eigenvectores con verificación exacta (sympy) y numérica (numpy).
import numpy as np
import sympy as sp

# --- VÍA 1: EXACTA con sympy (sin errores de float) ---
A_sym = sp.Matrix([[2, 0],
                   [1, 3]])
eig = A_sym.eigenvals()          # {eigenvalor: multiplicidad}
print("Eigenvalores exactos:", eig)   # {2: 1, 3: 1}

# Polinomio característico exacto
lam = sp.symbols('lambda')
poli = (A_sym - lam*sp.eye(2)).det()
print("det(A - λI) =", sp.expand(poli))   # λ**2 - 5*λ + 6

# --- VÍA 2: NUMÉRICA con numpy ---
A = np.array([[2.0, 0.0],
              [1.0, 3.0]])
vals, vecs = np.linalg.eig(A)
print("Eigenvalores numpy:", np.sort(vals))   # [2. 3.]

# --- DOBLE VERIFICACIÓN: A·v debe ser igual a λ·v para cada par ---
for i in range(len(vals)):
    v = vecs[:, i]
    izq = A @ v            # A · v
    der = vals[i] * v      # λ · v
    assert np.allclose(izq, der, atol=1e-9), f"Falla eigen {i}"
print("OK: A·v == λ·v para todos los eigenvectores")

# Verificación cruzada: traza = suma de λ ; determinante = producto de λ
assert np.isclose(np.trace(A), sum(vals))          # 2+3 = 5
assert np.isclose(np.linalg.det(A), np.prod(vals)) # 2*3 = 6
print("OK: traza =", np.trace(A), "= Σλ ;  det =", round(np.linalg.det(A)), "= Πλ")
```

La **traza** (suma de la diagonal) siempre iguala la suma de eigenvalores, y el **determinante** siempre iguala su producto. Son dos chequeos baratos e independientes — si fallan, hay un error.

## Ejemplo trabajado

**Caso GastroLatam:** 5 restaurantes, dos métricas estandarizadas (centradas y escaladas): *ticket promedio* y *food cost %*. Quiero saber si una sola dimensión resume a los clientes (para segmentarlos con un solo número).

```python
import numpy as np

# Datos estandarizados (media 0, desv 1) — 5 restaurantes × 2 métricas
X = np.array([
    [ 1.2,  -1.1],   # ticket alto, food cost bajo
    [ 0.8,  -0.9],
    [-0.3,   0.2],
    [-0.9,   0.8],
    [-0.8,   1.0],
])

# 1) Matriz de covarianza (2×2) — rowvar=False: columnas = variables
C = np.cov(X, rowvar=False)

# 2) Eigen-descomposición (eigh: matriz simétrica → resultado real y estable)
vals, vecs = np.linalg.eigh(C)

# 3) Ordenar de mayor a menor varianza
orden = np.argsort(vals)[::-1]
vals, vecs = vals[orden], vecs[:, orden]

total = vals.sum()
for i, lv in enumerate(vals):
    print(f"PC{i+1}: λ={lv:.4f}  varianza explicada={lv/total*100:.2f}%")

# Verificación: las dos proporciones suman 100%
assert np.isclose((vals/total).sum(), 1.0)
```

**Resultado (redondeado al final):** PC1 ≈ **98.7 %** de la varianza, PC2 ≈ **1.3 %**.

Interpretación con unidades: un solo eje (PC1) — combinación de "ticket alto + food cost bajo" — explica casi toda la diferencia entre los 5 restaurantes. Puedo asignar a cada local **un único score (adimensional)** y segmentar sin perder casi nada. Verificado: 98.7 % + 1.3 % = 100 %.

## Errores comunes / trampas

- **No estandarizar antes de PCA.** Si una columna está en pesos (miles) y otra en % (0–100), la de números grandes domina los eigenvalores artificialmente. Centra y escala primero (media 0, desv 1).
- **Usar `np.linalg.eig` en matriz simétrica.** Para covarianzas usa `eigh`: es más estable y garantiza eigenvalores reales (con `eig` pueden salir partes imaginarias diminutas por ruido de float).
- **Confundir eigenvalor con valor singular.** Solo coinciden si A es simétrica positiva. En general usa SVD para matrices no cuadradas.
- **Esperar eigenvectores únicos.** Un eigenvector multiplicado por cualquier escalar sigue siendo eigenvector; numpy los devuelve normalizados (longitud 1) y el signo puede variar entre librerías. No te asustes si el signo se invierte.
- **Olvidar ordenar por eigenvalor.** numpy no garantiza orden; siempre ordena de mayor a menor antes de leer "el componente principal".
- **Float en lugar de verificación exacta para casos críticos.** Si necesitas certeza simbólica, usa sympy y confirma `A·v = λ·v`.

## Cruces

- [[46-matrices-y-operaciones]] — multiplicación y estructura de matrices (base de A·v).
- [[48-determinantes-e-inversas]] — det(A−λI)=0 y la V⁻¹ de la diagonalización.
- [[35-vectores]] — qué es un vector y su norma (eigenvectores son vectores).
- [[95-matematica-para-machine-learning]] — PCA aplicado a features de ML.
- [[63-correlacion-vs-causalidad]] — covarianza/correlación que alimenta PCA.

---

**Mini-checklist de exactitud**
- [ ] ¿Verifiqué `A·v ≈ λ·v` para cada par (assert con tolerancia)?
- [ ] ¿Traza = Σλ y determinante = Πλ coinciden?
- [ ] ¿Estandaricé los datos y ordené los componentes antes de leer la varianza explicada?
