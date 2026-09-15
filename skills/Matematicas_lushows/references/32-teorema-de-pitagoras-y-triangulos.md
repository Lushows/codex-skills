# 32 · Teorema de Pitágoras y triángulos

> **Qué resuelve / cuándo usarlo** — Cuando necesitas hallar una distancia, una altura, una diagonal o un lado faltante de algo con forma de triángulo (o que puedas convertir en triángulo): rampa, escalera, diagonal de una pantalla/mesa, altura de un local o de un letrero, distancia en línea recta entre dos puntos.

## Concepto (para no-experto)

Un **triángulo** es una figura de tres lados rectos y tres esquinas (**vértices**). La suma de sus tres ángulos interiores SIEMPRE da **180°** (grados; un ángulo recto, como la esquina de una hoja, mide 90°).

Un **triángulo rectángulo** es el que tiene un ángulo de exactamente 90° (un "rincón perfecto", como la esquina de una pared). En él:
- Los dos lados que forman ese rincón se llaman **catetos** (los lados "cortos").
- El lado de enfrente, el más largo e inclinado, se llama **hipotenusa**.

El **Teorema de Pitágoras** dice algo asombroso: en CUALQUIER triángulo rectángulo, si construyes un cuadrado sobre cada cateto y un cuadrado sobre la hipotenusa, **el área del cuadrado grande (hipotenusa) es igual a la suma de las áreas de los dos cuadrados chicos (catetos)**.

> **Analogía cotidiana.** Una escalera apoyada en la pared forma un triángulo rectángulo: el piso es un cateto, la pared el otro cateto, y la escalera es la hipotenusa. Si sabes cuánto separaste el pie de la escalera de la pared (1.5 m) y a qué altura llega (2 m), Pitágoras te dice exactamente cuánto mide la escalera, sin medirla.

**Semejanza.** Dos triángulos son **semejantes** cuando tienen la misma forma pero distinto tamaño (uno es una "foto ampliada" del otro). Tienen los mismos ángulos y sus lados son proporcionales. Esto sirve para medir lo inalcanzable: la altura de un poste a partir de su sombra, comparándola con la sombra de un palo de altura conocida.

## Fórmulas / método

**Teorema de Pitágoras** (solo triángulos rectángulos):

    a² + b²  =  c²

- `a`, `b` = catetos (las dos longitudes que forman el ángulo de 90°), en metros (u otra unidad de longitud).
- `c` = hipotenusa (lado opuesto al ángulo recto), misma unidad.
- Despejes:
  - Hipotenusa:  `c = √(a² + b²)`
  - Un cateto:   `a = √(c² − b²)`  (requiere `c > b`)

**Clasificación de un triángulo por sus lados** (con lados `a ≤ b ≤ c`):
- `a² + b² = c²`  → **rectángulo** (90°).
- `a² + b² > c²`  → **acutángulo** (todos los ángulos < 90°).
- `a² + b² < c²`  → **obtusángulo** (un ángulo > 90°).

**Desigualdad triangular** (condición para que los tres lados formen un triángulo):

    a + b > c   (el lado mayor debe ser menor que la suma de los otros dos)

**Distancia entre dos puntos** (Pitágoras en el plano), puntos `(x₁,y₁)` y `(x₂,y₂)`:

    d = √( (x₂−x₁)² + (y₂−y₁)² )

**Semejanza** (triángulos con los mismos ángulos): los lados correspondientes guardan una razón constante `k`:

    a'/a = b'/b = c'/c = k

Unidades: las longitudes deben estar TODAS en la misma unidad antes de operar (ver [[37-conversion-de-unidades]]).

## Verificación en código

```python
# Pitágoras EXACTO. Para longitudes "bonitas" usamos sympy (raíz simbólica);
# para un número decimal final, Decimal con redondeo UNA sola vez.
from sympy import sqrt, Rational, simplify
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 50  # precisión alta de trabajo

def hipotenusa_exacta(a, b):
    """c = sqrt(a^2 + b^2) en forma EXACTA (símbolos)."""
    return sqrt(Rational(a)**2 + Rational(b)**2)

# Caso escalera: catetos 1.5 m (piso) y 2 m (pared)
a = Rational("1.5")   # m
b = Rational("2")     # m
c = hipotenusa_exacta(a, b)
print("c exacta =", simplify(c))                 # 5/2  -> 2.5 m exacto
print("c decimal =", Decimal(float(c)).quantize(Decimal("0.001"),
                                                 rounding=ROUND_HALF_UP), "m")

# --- VERIFICACIÓN POR SEGUNDA VÍA: operación inversa ---
# Si c es correcto, entonces c^2 - b^2 debe devolver a^2 (recuperar el cateto).
a_recuperado = sqrt(c**2 - b**2)
assert simplify(a_recuperado - a) == 0, "FALLA: la inversa no recupera el cateto"
print("Inversa OK: cateto recuperado =", simplify(a_recuperado), "m")

# --- VERIFICACIÓN 2: terna pitagórica entera conocida (3,4,5) ---
assert hipotenusa_exacta(3, 4) == 5, "FALLA: 3-4-5"
assert hipotenusa_exacta(5, 12) == 13, "FALLA: 5-12-13"
print("Ternas 3-4-5 y 5-12-13 OK")
```

Salida esperada:

```
c exacta = 5/2
c decimal = 2.500 m
Inversa OK: cateto recuperado = 3/2 m
Ternas 3-4-5 y 5-12-13 OK
```

```python
# Clasificación de triángulo + desigualdad triangular, con enteros exactos.
def clasificar(lados):
    a, b, c = sorted(lados)            # a <= b <= c
    if a + b <= c:
        return "NO es triángulo (viola la desigualdad triangular)"
    izq, der = a*a + b*b, c*c
    if izq == der:  return "rectángulo"
    if izq >  der:  return "acutángulo"
    return "obtusángulo"

assert clasificar((3, 4, 5))   == "rectángulo"
assert clasificar((2, 3, 4))   == "obtusángulo"   # 4+9=13 < 16
assert clasificar((6, 6, 6))   == "acutángulo"    # equilátero
assert clasificar((1, 2, 3))   == "NO es triángulo (viola la desigualdad triangular)"
print("Clasificación OK")
```

## Ejemplo trabajado

**Caso (LatAm, negocio).** GastroLatam quiere instalar un **letrero rectangular** en la fachada del local. El espacio disponible mide **1.20 m de ancho × 0.90 m de alto**. El proveedor cobra el cartel por su **diagonal en pulgadas** (como las TV). ¿Qué diagonal pedir?

Paso 1 — Identificar el triángulo. El ancho y el alto son los **catetos**; la **diagonal** del rectángulo es la **hipotenusa**.

Paso 2 — Aplicar Pitágoras (todo en metros):

    d = √(1.20² + 0.90²) = √(1.44 + 0.81) = √2.25 = 1.50 m

Paso 3 — Verificación inversa: `1.50² − 0.90² = 2.25 − 0.81 = 1.44 = 1.20²`. ✓ Recupera el ancho.

Paso 4 — Convertir a pulgadas (1 pulgada = 2.54 cm = 0.0254 m):

    1.50 m ÷ 0.0254 m/pulgada = 59.055... ≈ 59.06 pulgadas

Paso 5 — Sanity check de orden de magnitud: la diagonal debe ser mayor que el lado más largo (1.20 m) y menor que la suma de lados (2.10 m). 1.50 m cae justo en medio. ✓

**Resultado: la diagonal es 1.50 m ≈ 59.06 pulgadas.** Pides un letrero de ~60", confirmado por la operación inversa y por el sanity check.

```python
from decimal import Decimal, ROUND_HALF_UP
from sympy import sqrt, Rational
ancho, alto = Rational("1.20"), Rational("0.90")   # m
d = sqrt(ancho**2 + alto**2)                        # = 3/2 m exacto
pulg = Decimal(float(d)) / Decimal("0.0254")
print(d, "m  =", pulg.quantize(Decimal("0.01"), ROUND_HALF_UP), "pulgadas")
# 3/2 m  = 59.06 pulgadas
assert ancho < d < ancho + alto                     # sanity check
```

## Errores comunes / trampas

- **Usar Pitágoras en un triángulo que NO es rectángulo.** Solo vale si hay un ángulo de 90°. Para otros triángulos usa la ley de cosenos ([[33-trigonometria]]).
- **Confundir cateto con hipotenusa al despejar.** La hipotenusa es SIEMPRE el lado más largo. Si despejas un cateto y te da un número imaginario (`c² − b² < 0`), pusiste mal cuál era la hipotenusa.
- **Sumar antes de elevar al cuadrado.** `(a+b)² ≠ a²+b²`. Hay que elevar cada cateto al cuadrado *primero*, luego sumar, luego sacar raíz. Respeta el orden ([[11-operaciones-y-orden-pemdas]]).
- **Mezclar unidades.** Catetos en metros y centímetros sin convertir → resultado falso. Unifica unidades antes ([[37-conversion-de-unidades]]).
- **Redondear a mitad de camino.** Redondear `a²` o pasos intermedios arrastra error. Redondea UNA sola vez al final ([[05-cifras-significativas-y-redondeo]]).
- **Olvidar la desigualdad triangular.** Tres longitudes cualesquiera no siempre forman triángulo: el lado mayor debe ser menor que la suma de los otros dos.
- **Semejanza mal emparejada.** En triángulos semejantes hay que dividir lados *correspondientes* (los que están entre los mismos ángulos), no cualesquiera dos lados.

## Cruces

- [[30-geometria-plana-areas-y-perimetros]] — áreas y perímetros de triángulos y otras figuras.
- [[33-trigonometria]] — ángulos, seno/coseno y la ley de cosenos para triángulos NO rectángulos.
- [[34-coordenadas-y-plano-cartesiano]] — la fórmula de distancia es Pitágoras en el plano.
- [[15-potencias-y-raices]] — cuadrados y raíces, base del teorema.
- [[37-conversion-de-unidades]] — unificar unidades antes de operar y convertir el resultado.

---

**Mini-checklist de exactitud**
- [ ] ¿El triángulo es realmente rectángulo (tiene 90°) y la hipotenusa es el lado mayor?
- [ ] ¿Verifiqué por la vía inversa (`c² − b²` recupera el otro cateto) o con una terna conocida?
- [ ] ¿Todas las longitudes en la misma unidad y redondeo aplicado UNA sola vez al final?
