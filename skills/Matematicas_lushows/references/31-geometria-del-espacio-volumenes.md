# 31 · Geometría del espacio: volúmenes

> **Qué resuelve / cuándo usarlo** — Calcular cuánto *cabe* dentro de un sólido (volumen) y cuánta *superficie* tiene (área), para diseñar empaques, dimensionar tanques/recipientes, estimar capacidad y costear material.

## Concepto (para no-experto)

Un **sólido** es un cuerpo con tres dimensiones: largo, ancho y alto (a diferencia de una figura plana que solo tiene dos). Pensemos en una caja de cartón, una lata, una pelota o un cono de helado.

De cada sólido nos interesan dos números distintos:

- **Volumen (V):** *cuánto espacio ocupa por dentro*, es decir cuánto le cabe. Se mide en unidades cúbicas: centímetros cúbicos (cm³), metros cúbicos (m³), litros (L). Analogía: el volumen es cuánta agua puedes echar dentro del recipiente.
- **Área de superficie (A):** *cuánta "piel" tiene por fuera*, la suma del área de todas sus caras o de su cáscara. Se mide en unidades cuadradas: cm², m². Analogía: el área es cuánto papel necesitas para forrarlo por completo.

Son cosas diferentes y se miden en unidades diferentes. Para un negocio: el **volumen** te dice cuánto producto entra en el empaque; el **área** te dice cuánto cartón/lámina/etiqueta compras (y eso es plata — ver [[39-costos-de-material-por-area-y-volumen]]).

Un término más: **radio (r)** es la distancia del centro de un círculo a su borde; el **diámetro (d)** es el ancho completo que pasa por el centro, así que `d = 2·r`. La constante **π (pi) ≈ 3.14159…** aparece siempre que hay círculos.

## Fórmulas / método

Sea `b` = base, `h` = altura, `r` = radio, `L` `W` `H` = largo, ancho, alto. `π` = pi.

**Caja (prisma rectangular / ortoedro):**
- Volumen: `V = L · W · H`
- Área de superficie: `A = 2·(L·W + L·H + W·H)`

**Cilindro** (lata, tanque circular), radio `r`, altura `h`:
- Volumen: `V = π · r² · h`
- Área total: `A = 2·π·r²  +  2·π·r·h`  (dos tapas + el costado/manto)

**Esfera** (pelota, domo), radio `r`:
- Volumen: `V = (4/3) · π · r³`
- Área de superficie: `A = 4 · π · r²`

**Cono** (cono de helado, tolva), radio `r`, altura `h`:
- Volumen: `V = (1/3) · π · r² · h`
- Generatriz (lado inclinado): `g = √(r² + h²)`
- Área total: `A = π·r²  +  π·r·g`  (base + manto lateral)

**Unidades — regla de oro:** todas las longitudes deben estar en la *misma* unidad antes de operar. El resultado del volumen sale en esa unidad al cubo. Conversiones clave de capacidad:

- `1 L = 1000 cm³`   ·   `1 m³ = 1000 L = 1 000 000 cm³`

(Ver [[37-conversion-de-unidades]] para el método de factores.)

## Verificación en código

No calculamos π de memoria ni redondeamos a mano. Usamos Python con `math` para fórmulas exactas y `decimal` cuando el resultado se convierte en dinero o capacidad facturable.

```python
import math
from decimal import Decimal, ROUND_HALF_UP

# ---------- Volúmenes y áreas (geometría) ----------
def caja(L, W, H):
    V = L * W * H
    A = 2 * (L*W + L*H + W*H)
    return V, A

def cilindro(r, h):
    V = math.pi * r**2 * h
    A = 2*math.pi*r**2 + 2*math.pi*r*h
    return V, A

def esfera(r):
    V = (4/3) * math.pi * r**3
    A = 4 * math.pi * r**2
    return V, A

def cono(r, h):
    g = math.sqrt(r**2 + h**2)        # generatriz por Pitágoras
    V = (1/3) * math.pi * r**2 * h
    A = math.pi*r**2 + math.pi*r*g
    return V, A, g

# Caso: lata cilíndrica r=4 cm, h=12 cm  -> ¿cuántos mL entran?
r_cm, h_cm = 4, 12
V_cm3, A_cm2 = cilindro(r_cm, h_cm)
litros = Decimal(str(V_cm3)) / Decimal(1000)   # 1 L = 1000 cm3
print(f"Volumen = {V_cm3:.4f} cm3 = {litros.quantize(Decimal('0.001'))} L")
print(f"Area total = {A_cm2:.4f} cm2")

# ---------- VERIFICACIÓN POR SEGUNDA VÍA ----------
# (1) Integración: el volumen del cilindro es la integral del área de los
#     discos a lo largo de la altura: ∫ pi r^2 dz, z de 0 a h = pi r^2 h.
import scipy.integrate as si
V_integral, _ = si.quad(lambda z: math.pi * r_cm**2, 0, h_cm)
assert abs(V_integral - V_cm3) < 1e-9, "El volumen por integral no coincide"

# (2) Estimación de orden de magnitud (sanity check):
#     pi ~ 3.14, r^2 = 16, h = 12  ->  ~3.14*16*12 ~ 603 cm3 ~ 0.6 L. Razonable.
aprox = 3.14 * 16 * 12
assert abs(aprox - V_cm3) / V_cm3 < 0.01, "Fuera del rango estimado"

# (3) Esfera vs cilindro circunscrito (relación de Arquímedes):
#     V_esfera = (2/3) del cilindro que la encierra (r mismo, h=2r).
Ve, _ = esfera(5)
Vcil_circ, _ = cilindro(5, 2*5)
assert abs(Ve - (2/3)*Vcil_circ) < 1e-9, "Falla relación de Arquímedes"
print("Verificaciones OK")
```

Salida esperada:
```
Volumen = 603.1858 cm3 = 0.603 L
Area total = 402.1239 cm2
Verificaciones OK
```

Las tres comprobaciones son *vías independientes*: integral (cálculo), estimación a mano (orden de magnitud) y una identidad geométrica clásica (Arquímedes). Si las tres concuerdan, confiamos.

## Ejemplo trabajado

**Caso (LatAm):** Una marca de salsa picante va a vender en **frasco cilíndrico** de radio `r = 3.5 cm` y altura `h = 10 cm`. Quiere saber: (a) cuántos **mililitros** envasa, y (b) cuántos **cm² de etiqueta** necesita para forrar solo el costado (sin tapas), que es lo que se imprime.

**Paso 1 — Volumen (capacidad):**
`V = π·r²·h = π · (3.5)² · 10 = π · 12.25 · 10 = 122.5·π cm³`
`V = 384.845 cm³` (calculado en código).
Como `1 cm³ = 1 mL`, el frasco envasa **≈ 384.8 mL** (un frasco "de 380 mL" comercial encaja perfecto, con holgura).

**Paso 2 — Etiqueta (solo el manto lateral):**
El costado de un cilindro, desenrollado, es un rectángulo de alto `h` y ancho igual al perímetro de la base `2·π·r`:
`A_lado = 2·π·r·h = 2·π·3.5·10 = 70·π = 219.911 cm²`
**≈ 219.9 cm²** de etiqueta por frasco.

Verificación de orden de magnitud: el frasco mide ~7 cm de diámetro (≈22 cm de contorno) por 10 cm de alto → ~22·10 = 220 cm². Coincide. ✓

Decisión de negocio: con un pliego de etiquetas de `1 m² = 10 000 cm²`, salen `10 000 / 219.9 ≈ 45` etiquetas por pliego (descontando margen de corte; ver [[39-costos-de-material-por-area-y-volumen]]).

## Errores comunes / trampas

- **Confundir radio con diámetro.** Las fórmulas usan `r`. Si te dan el diámetro, primero `r = d/2`. Olvidarlo cuadruplica el área (`r²`) u octuplica el volumen de la esfera (`r³`).
- **Mezclar unidades.** Largo en metros y alto en cm en la misma fórmula da basura. Unifica *antes* de operar.
- **Confundir cm³ con cm².** Volumen y área son dimensiones distintas; revisa que las unidades del resultado tengan el exponente correcto (³ para capacidad, ² para material).
- **Mala conversión a litros.** `1 L = 1000 cm³`, no 100 ni 10. Y `1 m³ = 1000 L`, no 100.
- **Usar π = 3 o 3.14 cuando importa el dinero.** Para presupuestos grandes usa el `math.pi` completo y redondea una sola vez al final (ver [[05-cifras-significativas-y-redondeo]]).
- **En el cono, usar la altura `h` como si fuera la generatriz `g`** en el área lateral. El manto usa `g = √(r²+h²)`, no `h`.
- **Suponer que doblar el lado dobla el volumen.** El volumen escala con el *cubo* de la escala lineal (ver [[36-transformaciones-y-escalas]]): al doblar dimensiones, el volumen se multiplica por 8.

**Mini-checklist de exactitud**
- [ ] ¿Convertí diámetro→radio y unifiqué unidades antes de calcular?
- [ ] ¿El resultado tiene la unidad correcta (³ para volumen/capacidad, ² para superficie)?
- [ ] ¿Verifiqué por una segunda vía (estimación, integral o identidad) y redondeé una sola vez al final?

## Cruces

- [[30-geometria-plana-areas-y-perimetros]] — las caras y bases de los sólidos son figuras planas; el área de superficie se arma sumándolas.
- [[32-teorema-de-pitagoras-y-triangulos]] — la generatriz del cono `g = √(r²+h²)` sale de Pitágoras.
- [[37-conversion-de-unidades]] — pasar cm³ ↔ L ↔ m³ sin errores.
- [[38-geometria-aplicada-diseno-y-packaging]] — aplicar estos volúmenes/áreas al diseño real de empaques.
- [[39-costos-de-material-por-area-y-volumen]] — convertir el área en costo de cartón/lámina/etiqueta y el volumen en costo de llenado.
- [[36-transformaciones-y-escalas]] — cómo escalan volumen (cubo) y área (cuadrado) al cambiar el tamaño.
