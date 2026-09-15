# 36 · Transformaciones y escalas

> **Qué resuelve / cuándo usarlo** — Cuando necesitas mover, girar o redimensionar una figura/objeto y entender cómo cambia su tamaño: la trampa clásica es "lo hago el doble de grande" y olvidar que el área crece ×4 y el volumen ×8. Clave para diseño, packaging, planos, presupuestos de material y ampliar una receta o empaque.

## Concepto (para no-experto)

Una **transformación** es una operación que toma una figura y produce otra figura cambiando su posición, orientación o tamaño. Las cuatro básicas:

- **Traslación** (trasladar): mover la figura sin girarla ni cambiarla de tamaño. Como deslizar una hoja sobre la mesa: cada punto se mueve la misma distancia en la misma dirección.
- **Rotación** (rotar): girar la figura alrededor de un punto fijo llamado **centro de rotación**, un cierto **ángulo**. Como las manecillas de un reloj girando alrededor del centro.
- **Reflexión** (reflejar): voltear la figura como en un espejo respecto a una línea (el **eje de reflexión**).
- **Escalado** (escalar): agrandar o achicar la figura multiplicando por un **factor de escala** `k`. Como usar el zoom de una foto.

Las tres primeras (traslación, rotación, reflexión) son **isometrías**: conservan distancias y tamaños (la figura no cambia de tamaño, solo de lugar u orientación). El escalado NO es isometría: cambia el tamaño.

**El punto más importante de todo el módulo.** Cuando escalas con factor `k`:
- las **longitudes** (lados, perímetros, distancias) se multiplican por **k**,
- las **áreas** (superficies) se multiplican por **k²**,
- los **volúmenes** se multiplican por **k³**.

Analogía cotidiana: si pides una pizza familiar que tiene el **doble de diámetro** (k = 2) que la personal, no recibes el doble de pizza: recibes **4 veces** más pizza (k² = 4), porque lo que comes es área. Por eso la familiar "rinde" mucho más por peso. Y si una caja de empaque la haces el doble de grande en sus tres lados (k = 2), cabe **8 veces** más producto adentro (k³ = 8) y pesa ~8 veces más si es maciza.

**Semejanza**: dos figuras son **semejantes** si una es una versión escalada de la otra (misma forma, distinto tamaño). El factor de escala `k` es la **razón de semejanza** (razón = división entre dos cantidades comparables; ver [[13-razones-y-proporciones]]).

## Fórmulas / método

Sea `k` el factor de escala (número puro, sin unidades). Con `k > 1` agranda, `0 < k < 1` achica, `k = 1` no cambia.

| Magnitud | Cómo escala | Fórmula |
|---|---|---|
| Longitud | `× k` | `L' = k · L` |
| Área | `× k²` | `A' = k² · A` |
| Volumen | `× k³` | `V' = k³ · V` |

**Despejes útiles** (ir de un cambio conocido al factor `k`):

```
Si conoces la razón de áreas:     k = sqrt(A'/A)
Si conoces la razón de volúmenes:  k = cbrt(V'/V)   (cbrt = raíz cúbica)
Si conoces la razón de longitudes: k =  L'/L
```

**Transformaciones en el plano** (un punto `P = (x, y)`):

- Traslación por el vector `(tx, ty)` (ver [[35-vectores]]):
  `(x', y') = (x + tx, y + ty)`
- Escalado con factor `k` respecto al origen:
  `(x', y') = (k·x, k·y)`
- Rotación un ángulo `θ` (theta) en sentido antihorario respecto al origen:
  `x' = x·cos θ − y·sin θ`
  `y' = x·sin θ + y·cos θ`
  (ver [[33-trigonometria]] para seno y coseno).

Unidades: `k` es adimensional. `L` en cm/m, `A` en cm²/m², `V` en cm³/m³ o L. Los ángulos van en **radianes** dentro de las funciones de código (`π rad = 180°`).

## Verificación en código

```python
# Patrón ejecutar+verificar para transformaciones y escalas.
from decimal import Decimal, getcontext
import numpy as np

getcontext().prec = 30  # alta precisión para evitar arrastre de error

# --- 1) EFECTO DEL FACTOR DE ESCALA en longitud / area / volumen ---
k = Decimal("2")                 # factor de escala (doble de grande, lineal)
L0 = Decimal("30")               # lado original, cm
A0 = L0 * L0                     # area original (cuadrado), cm^2
V0 = L0 * L0 * L0                # volumen original (cubo), cm^3

L1 = k * L0
A1 = (k**2) * A0
V1 = (k**3) * V0

print("L:", L0, "->", L1, " (x", L1/L0, ")")
print("A:", A0, "->", A1, " (x", A1/A0, ")")
print("V:", V0, "->", V1, " (x", V1/V0, ")")

# VERIFICACION VIA 2: recalcular area/volumen desde la longitud escalada,
# SIN usar k^2 ni k^3. Deben coincidir exactamente.
assert A1 == L1 * L1,        "el area escalada no cuadra con el lado escalado"
assert V1 == L1 * L1 * L1,   "el volumen escalado no cuadra con el lado escalado"
# y las razones deben ser k, k^2, k^3 exactos:
assert L1/L0 == k
assert A1/A0 == k**2
assert V1/V0 == k**3
print("OK escalas verificadas por segunda via")

# --- 2) ROTACION: una rotacion conserva la longitud (isometria) ---
def rot(p, deg):
    th = np.deg2rad(deg)
    M = np.array([[np.cos(th), -np.sin(th)],
                  [np.sin(th),  np.cos(th)]])
    return M @ np.array(p, dtype=float)

p  = (3.0, 4.0)                  # punto; su distancia al origen es 5 (3-4-5)
pr = rot(p, 37.0)               # rotar 37 grados
d0 = np.hypot(*p)
d1 = np.hypot(*pr)
print("distancia antes:", round(d0,6), "despues:", round(d1,6))
# VERIFICACION: la rotacion NO cambia la distancia al origen
assert abs(d0 - d1) < 1e-9, "una rotacion no deberia cambiar la longitud"

# Verificacion extra: rotar +37 y luego -37 devuelve el punto original
back = rot(pr, -37.0)
assert np.allclose(back, p), "rotar y desrotar debe devolver el punto"
print("OK rotacion es isometria y es invertible")
```

Salida esperada (resumida): `L: 30 -> 60 (x2)`, `A: 900 -> 3600 (x4)`, `V: 27000 -> 216000 (x8)`, y ambos bloques `OK`.

## Ejemplo trabajado

**Situación (packaging real, LatAm).** Una marca empaca su producto en una caja cúbica de **10 cm** de lado. Para una edición familiar quieren una caja **semejante** (misma forma) con **el doble de volumen**, no el doble de lado. Pregunta: ¿cuánto debe medir el lado de la caja nueva, y cuánto más cartón (área) consume?

Paso 1 — Identificar qué nos dan. Nos dan la razón de **volúmenes**: `V'/V = 2`.

Paso 2 — Hallar el factor de escala lineal `k`. Como el volumen escala con `k³`:
`k = cbrt(V'/V) = cbrt(2) ≈ 1.259921`.

Paso 3 — Lado nuevo: `L' = k · L = 1.259921 × 10 cm ≈ 12.599 cm` → **redondeo final** a 12.6 cm.

Paso 4 — Cartón (superficie). El área escala con `k²`:
`A'/A = k² = (cbrt(2))² = 2^(2/3) ≈ 1.5874`. El cartón sube **~58.7 %**, no se duplica.

```python
from decimal import Decimal
L = Decimal(10)                 # cm
k = Decimal(2) ** (Decimal(1)/Decimal(3))     # raiz cubica de 2
Lp = k * L
print("Lado nuevo:", round(Lp, 3), "cm")               # 12.599 cm
print("Volumen x:", round(k**3, 6))                    # 2.000000
print("Area (carton) x:", round(k**2, 6))              # 1.587401

# VERIFICACION 2da via: calcular volumenes reales con los lados, sin usar k
V0 = Decimal(10)**3
V1 = Lp**3
assert abs(V1/V0 - 2) < Decimal("1e-9"), "el volumen nuevo no es el doble"
print("OK: caja nueva tiene exactamente el doble de volumen")
```

**Respuesta:** lado nuevo ≈ **12.6 cm**; el volumen se duplica (objetivo cumplido) y el consumo de cartón sube **≈ 58.7 %** (área × 1.587). Doblar el contenido NO duplica el material: ahorro de empaque que conviene tener en el costeo (ver [[39-costos-de-material-por-area-y-volumen]]).

## Errores comunes / trampas

- **Escalar área o volumen por k en vez de k² / k³.** El error #1. "Lo hago el doble" (k=2) NO duplica el área (×4) ni el volumen (×8).
- **Olvidar que el centro importa.** Escalar/rotar respecto al origen mueve la figura; respecto a su propio centro la deja en su lugar. Define siempre el centro.
- **Mezclar grados y radianes.** Las funciones `sin`/`cos` de Python/numpy esperan **radianes**. Convierte con `np.deg2rad` o `math.radians`, o tu rotación saldrá disparatada.
- **Creer que rotar/trasladar cambia el tamaño.** No: son isometrías. Si tras una rotación el área cambia, hay un bug.
- **Confundir "doble de diámetro" con "doble de área".** Pizza, ruedas, tanques: el área/volumen vive en k², k³.
- **Redondear `k` antes de tiempo.** Si redondeas `cbrt(2)≈1.26` y luego elevas al cubo, te da 2.0004, no 2. Redondea **una sola vez al final** (ver [[05-cifras-significativas-y-redondeo]]).
- **Aplicar transformaciones en el orden equivocado.** Rotar-luego-trasladar ≠ trasladar-luego-rotar. El orden cambia el resultado.

## Cruces

- [[13-razones-y-proporciones]] — la razón de semejanza `k` es una razón pura.
- [[30-geometria-plana-areas-y-perimetros]] — qué área estás escalando con k².
- [[31-geometria-del-espacio-volumenes]] — qué volumen estás escalando con k³.
- [[35-vectores]] — traslaciones y rotaciones se expresan con vectores/matrices.
- [[39-costos-de-material-por-area-y-volumen]] — convertir el efecto k², k³ en dinero de material.

---

**Mini-checklist de exactitud**
1. ¿Identifiqué bien si la magnitud es longitud (k), área (k²) o volumen (k³)?
2. ¿Definí el centro de la escala/rotación y usé radianes en el código?
3. ¿Redondeé una sola vez al final y verifiqué el resultado por una segunda vía (recalcular desde la longitud, o rotar y desrotar)?
