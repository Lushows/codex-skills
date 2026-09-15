# 33 · Trigonometría

> **Qué resuelve / cuándo usarlo** — Calcular lados y ángulos de triángulos, alturas y distancias que no se pueden medir directamente (un poste, un techo), pendientes de rampas y descripción de fenómenos que oscilan (ondas, estacionalidad de ventas).

## Concepto (para no-experto)

La **trigonometría** estudia la relación entre los **ángulos** y los **lados** de un triángulo. La idea base se ve en un **triángulo rectángulo** (un triángulo que tiene un ángulo de 90°, llamado **ángulo recto**, como la esquina de una hoja de papel).

En ese triángulo, fijándonos en un ángulo agudo (menor a 90°) que llamamos **θ** (la letra griega *theta*, así nombramos al ángulo), los tres lados tienen nombre:

- **Hipotenusa**: el lado más largo, el que está frente al ángulo recto. La "rampa".
- **Cateto opuesto**: el lado de enfrente del ángulo θ. La "altura".
- **Cateto adyacente**: el lado que toca al ángulo θ (sin ser la hipotenusa). El "piso".

La magia: si el ángulo θ no cambia, las **proporciones** (divisiones) entre esos lados tampoco cambian, sin importar si el triángulo es grande o chico. Esas tres proporciones tienen nombre:

- **Seno** (`sin`): opuesto ÷ hipotenusa.
- **Coseno** (`cos`): adyacente ÷ hipotenusa.
- **Tangente** (`tan`): opuesto ÷ adyacente.

**Analogía cotidiana:** una rampa de acceso. El ángulo de inclinación es θ. La tangente de θ te dice cuántos metros sube por cada metro que avanza horizontalmente. Si conoces el ángulo y lo que avanza, sacas la altura sin subir una escalera.

**Ángulos: grados vs radianes.** Medimos ángulos en dos unidades:
- **Grados (°)**: una vuelta completa = 360°.
- **Radianes (rad)**: una vuelta completa = 2π rad ≈ 6,2832 rad. Es la unidad "natural" de las matemáticas; casi todas las librerías (Python, Excel con `RADIANES`) trabajan en radianes por dentro.

Regla de conversión: **π rad = 180°**.

## Fórmulas / método

Para un triángulo rectángulo con ángulo agudo θ:

```
sin(θ) = opuesto / hipotenusa
cos(θ) = adyacente / hipotenusa
tan(θ) = opuesto / adyacente = sin(θ) / cos(θ)
```

Para **recuperar el ángulo** desde una proporción usamos las funciones **inversas** (arco): `arcsin`, `arccos`, `arctan` (en código: `asin`, `acos`, `atan`).

```
θ = arctan(opuesto / adyacente)
```

**Conversión de unidades de ángulo** (símbolo π ≈ 3,14159265):

```
radianes = grados × (π / 180)
grados   = radianes × (180 / π)
```

**Identidad fundamental** (sirve de verificación, vale para cualquier θ):

```
sin²(θ) + cos²(θ) = 1
```

**Triángulos NO rectángulos** (cualquier triángulo), con lados a, b, c opuestos a los ángulos A, B, C:

- **Ley de senos:**  `a / sin(A) = b / sin(B) = c / sin(C)`
- **Ley de cosenos:** `c² = a² + b² − 2·a·b·cos(C)`  (generaliza Pitágoras)

Unidades: los lados llevan unidad de longitud (m, cm); los ángulos llevan ° o rad. Las proporciones (sin, cos, tan) son **adimensionales** (sin unidad).

## Verificación en código

Patrón de error cero: calcular con código exacto y confirmar por una segunda vía (identidad, función inversa y `assert`).

```python
import math

# --- Caso: altura de un poste ---
# Medimos el ángulo de elevación a la punta = 35 grados,
# parados a 12 metros de la base (cateto adyacente).
angulo_grados = 35.0
distancia_m   = 12.0  # cateto adyacente

# Las funciones de math trabajan en RADIANES: convertir primero.
theta = math.radians(angulo_grados)   # = grados * pi/180

# altura = adyacente * tan(theta)  (porque tan = opuesto/adyacente)
altura = distancia_m * math.tan(theta)
print(f"theta (rad)   = {theta:.6f} rad")
print(f"altura        = {altura:.4f} m")   # -> 8.4023 m

# ---------- VERIFICACIÓN POR SEGUNDA VÍA ----------
# (1) Inversa: si parto de los dos catetos, ¿recupero los 35 grados?
angulo_recuperado = math.degrees(math.atan(altura / distancia_m))
assert abs(angulo_recuperado - angulo_grados) < 1e-9, "La inversa no cuadra"

# (2) Identidad pitagórica sin^2 + cos^2 = 1 (debe dar 1 exacto salvo redondeo)
ident = math.sin(theta)**2 + math.cos(theta)**2
assert abs(ident - 1.0) < 1e-12, "Falla identidad fundamental"

# (3) Sanity check de orden de magnitud:
# 35 grados es menos de 45 grados, asi que la altura debe ser MENOR que la distancia (12 m).
assert altura < distancia_m, "Para theta<45, opuesto<adyacente"

print("Verificaciones OK")
```

Para ángulos "notables" donde queremos valor **exacto** (sin redondeo de float), usamos `sympy`:

```python
import sympy as sp

theta = sp.rad(60)              # 60 grados a radianes, simbólico
print(sp.sin(theta))           # sqrt(3)/2   (exacto, no 0.866...)
print(sp.cos(theta))           # 1/2
# Verificación: identidad debe ser EXACTAMENTE 1
assert sp.simplify(sp.sin(theta)**2 + sp.cos(theta)**2) == 1
```

## Ejemplo trabajado

**Problema (rampa de acceso, LatAm).** Una cafetería en Bogotá debe construir una rampa para silla de ruedas. La norma técnica (NTC 4143) exige pendiente máxima del **8 %** para desniveles de hasta 1 m. El desnivel a salvar es **0,45 m** (altura del andén). ¿Cuántos metros de largo horizontal necesita la rampa y qué ángulo tendrá?

Pendiente 8 % significa: por cada 100 cm de avance horizontal, sube 8 cm. O sea `tan(θ) = 8/100 = 0,08`.

1. **Ángulo:** θ = arctan(0,08).
2. **Largo horizontal** (cateto adyacente): si la altura (opuesto) es 0,45 m y `tan(θ)=opuesto/adyacente`, entonces `adyacente = opuesto / tan(θ) = 0,45 / 0,08`.

```python
import math
from decimal import Decimal, getcontext
getcontext().prec = 28

altura     = Decimal("0.45")   # m, desnivel
pendiente  = Decimal("0.08")   # tan(theta) = 8 %

# Largo horizontal con decimal (exacto, sin float)
largo_horizontal = altura / pendiente
print(f"Largo horizontal = {largo_horizontal} m")   # 5.625 m

# Angulo (aqui si usamos float: el angulo es informativo, no dinero)
theta_deg = math.degrees(math.atan(float(pendiente)))
print(f"Angulo de la rampa = {theta_deg:.4f} grados")  # ~4.5739 grados

# Largo REAL de la rampa (hipotenusa) por Pitagoras
hip = (altura**2 + largo_horizontal**2).sqrt()
print(f"Largo de rampa (hipotenusa) = {hip} m")        # ~5.6430 m

# --- Verificacion segunda via ---
# tan del angulo recuperado debe volver a 0.08
assert abs(math.tan(math.radians(theta_deg)) - 0.08) < 1e-9
# sin(theta) = altura / hipotenusa
assert abs(math.sin(math.radians(theta_deg)) - float(altura/hip)) < 1e-9
print("OK")
```

**Resultado:** la rampa necesita **5,625 m de largo horizontal**, con un ángulo de **≈ 4,57°** y una longitud real (hipotenusa) de **≈ 5,643 m**. Como 4,57° < 45°, la rampa es suave: coherente con que debe ser cómoda. Todas las longitudes en metros.

## Errores comunes / trampas

- **Grados vs radianes**: el error #1. `math.sin(30)` en Python NO es seno de 30°, es seno de 30 *radianes*. Siempre convierte con `math.radians(...)` primero. En Excel igual: usa `RADIANES()`.
- **Confundir opuesto y adyacente**: identifica primero cuál ángulo es θ; el opuesto es el lado de enfrente, el adyacente el que lo toca.
- **Usar Pitágoras en triángulos sin ángulo recto**: solo vale con ángulo de 90°. Si no, usa ley de cosenos.
- **`tan(90°)` no existe** (división por cos(90°)=0): da infinito. Cuidado con ángulos cercanos a 90°.
- **Redondear a mitad de camino**: arrastra el valor completo y redondea solo al final (ver `[[05-cifras-significativas-y-redondeo]]`).
- **Confundir pendiente % con grados**: 100 % de pendiente NO es 90°, es 45° (sube tanto como avanza). Pendiente = tan(ángulo), no el ángulo mismo.

## Cruces

- [[32-teorema-de-pitagoras-y-triangulos]] — base geométrica del triángulo rectángulo.
- [[30-geometria-plana-areas-y-perimetros]] — áreas (incluye área = ½·a·b·sin(C)).
- [[37-conversion-de-unidades]] — grados ↔ radianes como conversión de unidad.
- [[35-vectores]] — seno/coseno para descomponer fuerzas y direcciones.
- [[04-notacion-unidades-y-dimensiones]] — por qué sin/cos son adimensionales.

---

**Mini-checklist de exactitud**
- [ ] ¿Convertí grados → radianes antes de llamar sin/cos/tan en código?
- [ ] ¿Verifiqué con la inversa (arctan/arcsin) o con sin²+cos²=1?
- [ ] ¿Todas las longitudes llevan unidad y redondeé solo al final?
