# 30 · Geometría plana: áreas y perímetros

> **Qué resuelve / cuándo usarlo** — Calcular cuánto espacio cubre una figura (área) y cuánto mide su contorno (perímetro) para presupuestar pisos, pintura, tela, vidrio, vinilos, empaques, terrenos o cualquier superficie. Es la base para cotizar material por metro cuadrado o metro lineal.

## Concepto (para no-experto)

Imagina que tienes que pintar una pared o forrar una caja. Necesitas dos números distintos:

- **Área**: cuánta *superficie* hay que cubrir. Se mide en **unidades al cuadrado** (m², cm², cm²). Piensa en cuántas baldosas de 1×1 caben dentro de la figura. Eso es el área.
- **Perímetro**: cuánto mide el *borde* o contorno si lo recorrieras con una cinta. Se mide en **unidades lineales** (m, cm). Piensa en cuánta cinta necesitas para rodear la figura por fuera.

Definamos los términos que usaremos:

- **Figura plana**: un dibujo "plano" (2 dimensiones, sin grosor) como un rectángulo o un círculo.
- **Base (b)** y **altura (h)**: en un rectángulo o triángulo, son los dos lados perpendiculares (forman un ángulo de 90°, una esquina "recta"). La altura SIEMPRE se mide perpendicular a la base, no de forma inclinada.
- **Radio (r)**: la distancia del centro de un círculo a su borde. El **diámetro (d)** es el doble: `d = 2·r`.
- **π (pi)**: número fijo ≈ 3.14159… que relaciona el contorno de un círculo con su diámetro. Es **irracional** (sus decimales no terminan), por eso NUNCA lo truncamos a mano: dejamos que el código use su valor completo y redondeamos solo al final.

Analogía cotidiana: el área es el *queso* de una pizza (lo que comes); el perímetro es la *orilla* (la corteza que rodea).

## Fórmulas / método

Cada símbolo se define la primera vez. Las unidades del resultado dependen de las unidades de entrada (todas deben ser **las mismas** antes de calcular).

**Rectángulo** (lados `b` = base, `h` = altura):
- Área: `A = b · h`  → unidad²
- Perímetro: `P = 2·(b + h)`  → unidad

**Cuadrado** (lado `L`): caso del rectángulo con `b = h = L`:
- Área: `A = L²`   ·   Perímetro: `P = 4·L`

**Triángulo** (`b` = base, `h` = altura perpendicular a esa base):
- Área: `A = (b · h) / 2`  → unidad²
- Perímetro: `P = lado₁ + lado₂ + lado₃` (suma de los tres lados)
- Si solo conoces los tres lados `a, b, c` (sin la altura), usa **Herón**:
  - `s = (a + b + c) / 2`  (semiperímetro)
  - `A = √( s·(s−a)·(s−b)·(s−c) )`

**Círculo** (`r` = radio):
- Área: `A = π · r²`  → unidad²
- Perímetro (se llama **circunferencia**): `P = 2 · π · r = π · d`  → unidad

**Trapecio** (dos lados paralelos `B` y `b`, altura `h` entre ellos):
- Área: `A = ((B + b) / 2) · h`  → unidad²

**Polígono regular** (n lados iguales de longitud `L`, apotema `ap` = distancia del centro al punto medio de un lado):
- Perímetro: `P = n · L`
- Área: `A = (P · ap) / 2`

**Polígono cualquiera dado por coordenadas** de sus vértices `(x₁,y₁), …, (xₙ,yₙ)` — fórmula del **zapato (shoelace)**:
- `A = |Σ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ)| / 2`  (el último vértice se conecta con el primero)

> Regla de oro de unidades: si mezclas cm con m el resultado es basura. Convierte TODO a la misma unidad antes (ver [[37-conversion-de-unidades]]).

## Verificación en código

```python
# Geometría plana exacta. Usamos sympy para mantener pi y raíces EXACTOS
# (sin redondear a mitad de camino). Solo redondeamos al final.
from sympy import pi, Rational, sqrt, simplify, nsimplify, N

# ---------- RECTÁNGULO ----------
b, h = Rational(420, 100), Rational(310, 100)  # 4.20 m x 3.10 m (sala) en exacto
area_rect = b * h
perim_rect = 2 * (b + h)
print("Rectángulo  A =", area_rect, "m^2 =", float(area_rect))
print("Rectángulo  P =", perim_rect, "m  =", float(perim_rect))

# ---------- CÍRCULO ----------
r = Rational(35, 100)  # 0.35 m de radio (una mesa redonda)
area_circ = pi * r**2          # exacto: (49/400)*pi
perim_circ = 2 * pi * r        # exacto: (7/10)*pi
print("Círculo  A (exacto) =", simplify(area_circ), "->", float(area_circ), "m^2")
print("Círculo  P (exacto) =", simplify(perim_circ), "->", float(perim_circ), "m")

# ---------- TRIÁNGULO por base/altura y por Herón (deben coincidir) ----------
# Triángulo rectángulo de catetos 3 y 4 -> hipotenusa 5
a_, b_, c_ = 3, 4, 5
area_bh = Rational(a_ * b_, 2)              # base*altura/2 (catetos perpendiculares)
s = Rational(a_ + b_ + c_, 2)              # semiperímetro
area_heron = sqrt(s * (s - a_) * (s - b_) * (s - c_))
print("Triángulo  A (base*h/2) =", area_bh)
print("Triángulo  A (Herón)    =", simplify(area_heron))
assert simplify(area_bh - area_heron) == 0, "Las dos vías del triángulo NO coinciden"

# ---------- POLÍGONO por coordenadas (shoelace) ----------
# Mismo rectángulo de arriba como polígono: (0,0)(4.2,0)(4.2,3.1)(0,3.1)
pts = [(Rational(0), Rational(0)),
       (b, Rational(0)),
       (b, h),
       (Rational(0), h)]
acc = 0
n = len(pts)
for i in range(n):
    x1, y1 = pts[i]
    x2, y2 = pts[(i + 1) % n]   # el siguiente; el último conecta con el primero
    acc += x1 * y2 - x2 * y1
area_shoelace = abs(acc) / 2
print("Shoelace  A =", area_shoelace, "m^2")

# ===== VERIFICACIÓN POR SEGUNDA VÍA =====
# 1) El área por shoelace del rectángulo debe igualar b*h:
assert area_shoelace == area_rect, "Shoelace no coincide con b*h"

# 2) Sanity check de orden de magnitud del círculo:
#    A = pi*r^2 ~ 3.14*0.35^2 = 3.14*0.1225 ~ 0.385 m^2
aprox = 3.14159 * 0.35**2
assert abs(float(area_circ) - aprox) < 1e-3, "Círculo fuera de rango esperado"

# 3) Circunferencia vs diámetro: P debe ser ~3.14 veces el diámetro (2r):
ratio = float(perim_circ) / float(2 * r)
assert abs(ratio - float(pi)) < 1e-9, "P/d no da pi"
print("OK: todas las verificaciones cruzadas pasaron.")
```

Salida esperada (resumen): rectángulo `A = 13.02 m²`, `P = 14.60 m`; círculo `A ≈ 0.3848 m²`, `P ≈ 2.199 m`; triángulo `A = 6` por ambas vías; shoelace `= 13.02 m²`.

## Ejemplo trabajado

**Problema (negocio LatAm).** Una cafetería va a instalar piso vinílico en su salón rectangular de **4.20 m × 3.10 m** y poner un zócalo (moldura de borde) alrededor del salón, excepto en la puerta de **0.90 m**. El vinilo cuesta **$45.000 COP/m²** y se compra **+8 % de desperdicio** por cortes. El zócalo cuesta **$12.000 COP/m**. ¿Cuánto material y cuánto dinero?

Paso 1 — Área del piso (lo que cubre el vinilo):
`A = b·h = 4.20 m × 3.10 m = 13.02 m²`

Paso 2 — Vinilo a comprar con 8 % de desperdicio:
`13.02 m² × 1.08 = 14.0616 m²`

Paso 3 — Perímetro para el zócalo, menos la puerta:
`P = 2·(4.20 + 3.10) = 14.60 m` → `14.60 − 0.90 = 13.70 m`

Paso 4 — Costo (dinero SIEMPRE con `decimal`, nunca float):

```python
from decimal import Decimal, ROUND_HALF_UP
def cop(x): return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)  # peso entero

area = Decimal("13.02")
vinilo_m2 = (area * Decimal("1.08"))                 # 14.0616 m^2
costo_vinilo = vinilo_m2 * Decimal("45000")          # COP
zocalo_m = Decimal("14.60") - Decimal("0.90")        # 13.70 m
costo_zocalo = zocalo_m * Decimal("12000")           # COP
total = costo_vinilo + costo_zocalo

print("Vinilo a comprar:", vinilo_m2, "m^2")
print("Costo vinilo: $", cop(costo_vinilo))
print("Costo zócalo: $", cop(costo_zocalo))
print("TOTAL: $", cop(total))
# Verificación 2da vía (estimación gruesa): 14 m^2 * 45k ~ 630k ; 13.7 m * 12k ~ 164k ; ~794k
```

**Resultado:** vinilo `14.0616 m²` → **$632.772 COP**; zócalo `13.70 m` → **$164.400 COP**; **TOTAL ≈ $797.172 COP**. La estimación gruesa (~$794 mil) confirma el orden de magnitud. ✅

## Errores comunes / trampas

- **Confundir área con perímetro.** Para pintura/piso/tela usas **área** (unidad²); para marcos/zócalos/cercas usas **perímetro** (unidad). Revisa qué cobra el proveedor: ¿por m² o por m lineal?
- **Mezclar unidades.** 50 cm con 2 m da error. Convierte TODO a la misma unidad antes (ver [[37-conversion-de-unidades]]).
- **Usar el lado inclinado como "altura" del triángulo o trapecio.** La altura es la distancia *perpendicular* a la base, no el lado oblicuo.
- **Truncar π a 3.14 demasiado pronto.** En áreas grandes el error se acumula. Deja π exacto y redondea al final ([[05-cifras-significativas-y-redondeo]]).
- **Olvidar el desperdicio/merma.** El material real siempre exige un % extra por cortes; el área geométrica es el mínimo teórico, no lo que compras.
- **Usar float para el dinero.** `0.1 + 0.2 != 0.3` en float; usa `decimal` ([[12-fracciones-decimales-y-precision]]).
- **Diámetro vs radio.** `A = π·r²` usa **radio**. Si te dan el diámetro, divide entre 2 primero.

## Cruces

- [[37-conversion-de-unidades]] — pasar cm↔m antes de calcular, regla de oro de unidades.
- [[31-geometria-del-espacio-volumenes]] — cuando la figura tiene grosor/profundidad (m³).
- [[32-teorema-de-pitagoras-y-triangulos]] — hallar lados o alturas faltantes de triángulos.
- [[39-costos-de-material-por-area-y-volumen]] — convertir área en presupuesto con desperdicio.
- [[04-notacion-unidades-y-dimensiones]] — por qué el área es unidad² y el perímetro unidad.

**Mini-checklist de exactitud**
- [ ] ¿Todas las medidas están en la MISMA unidad antes de operar?
- [ ] ¿El resultado lleva la unidad correcta (² para área, lineal para perímetro)?
- [ ] ¿Verifiqué por una 2ª vía (shoelace, Herón, o estimación de orden de magnitud)?
