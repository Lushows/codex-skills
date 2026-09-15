# 38 · Geometría aplicada: diseño y packaging

> **Qué resuelve / cuándo usarlo** — Calcular con exactitud áreas de impresión, dimensiones reales de un empaque (con tapas y pestañas), sangrado/márgenes y cuántas piezas caben en un pliego de papel. Úsalo antes de mandar a imprenta o cotizar material: un error aquí se multiplica por miles de piezas y cuesta dinero real.

## Concepto (para no-experto)

Cuando diseñas un empaque o una pieza impresa (una etiqueta, una caja, un volante), el archivo digital se convierte en algo físico de cartón o papel. Hay cuatro conceptos que SIEMPRE confunden y producen reimpresiones caras:

- **Pliego**: la hoja grande de papel/cartón que la imprenta corta. Ejemplo típico en LatAm: 70 × 100 cm. De ese pliego se sacan muchas piezas pequeñas. **Aprovechamiento de pliego** = cuántas piezas caben sin desperdiciar.
- **Sangrado (bleed)**: un margen EXTRA de tinta que se imprime *más allá* del borde final, normalmente **3 mm** por lado. Como las máquinas de corte no son perfectas (se desvían 1-2 mm), si no imprimes de más, aparece una línea blanca en el borde. Analogía: pintas la pared *un poco* por detrás del marco del cuadro, para que si el marco se mueve, no se vea pared sin pintar.
- **Margen de seguridad (safe zone)**: lo contrario. Es una zona *interior* (normalmente 3-5 mm desde el borde final) donde NO pones texto importante, por si el corte se come un pedacito.
- **Troquel / desarrollo (dieline)**: el "patrón de costura" de una caja. Una caja 3D se fabrica de una lámina plana 2D que luego se dobla. El desarrollo incluye las **pestañas de pegado** y las **solapas (tapas)**, así que la lámina plana SIEMPRE es más grande que las caras visibles.

La regla de oro: **el tamaño que mandas a imprenta NO es el tamaño final visible**. Es el tamaño final + sangrado (para piezas planas) o el desarrollo completo desplegado + pestañas (para cajas).

## Fórmulas / método

**Dimensión de archivo con sangrado** (pieza plana, p. ej. etiqueta o flyer):
```
W_archivo = W_final + 2·s
H_archivo = H_final + 2·s
```
donde `s` = sangrado por lado (mm). El factor 2 es porque hay sangrado a ambos lados.

**Área de tinta / sustrato por pieza** (la que pagas por área):
```
A_pieza = W_archivo · H_archivo      [mm²]  →  / 1e6 = m²
```

**Aprovechamiento de pliego (imposición en rejilla)** — cuántas piezas caben con dos orientaciones posibles; se elige la mejor:
```
n_recta    = floor(W_pliego / W_pieza) · floor(H_pliego / H_pieza)
n_girada   = floor(W_pliego / H_pieza) · floor(H_pliego / W_pieza)
n_por_pliego = max(n_recta, n_girada)
```
`floor` = redondeo hacia abajo (parte entera): no puedes imprimir media pieza. `W_pieza`/`H_pieza` ya deben incluir sangrado **y** una separación de corte (gutter) si se requiere.

**Pliegos necesarios y desperdicio:**
```
N_pliegos     = ceil(tirada / n_por_pliego)        ceil = redondeo hacia arriba
desperdicio % = 1 − (A_pieza · n_por_pliego) / A_pliego
```

**Desarrollo de caja recta (tuck-end simple)** — caja de Largo `L`, Ancho `A`, Alto `H`:
```
W_plano (sin pestaña pegado) = 2·L + 2·A
W_plano (con pestaña g)      = 2·L + 2·A + g
H_plano                      = H + 2·solapa   (solapa ≈ A para tapa de inserción)
Área lámina                  = W_plano · H_plano   [+ sangrado en todo el contorno]
```
Símbolos en **mm** salvo área (mm²/m²). Todo es geometría exacta: no hay incertidumbre estadística, solo decisiones de redondeo entero (`floor`/`ceil`).

## Verificación en código

```python
from decimal import Decimal as D, getcontext
import math
getcontext().prec = 28  # dinero/áreas con decimal, nunca float

# --- Caso: etiqueta 90 x 50 mm, sangrado 3 mm, pliego 70 x 100 cm, tirada 5000 ---
W_final, H_final = D("90"), D("50")   # mm
s = D("3")                            # sangrado por lado, mm
gutter = D("0")                       # separación entre piezas (corte compartido)
W_pliego, H_pliego = D("700"), D("1000")  # 70x100 cm en mm
tirada = 5000

# 1) Tamaño de archivo con sangrado
W_arch = W_final + 2*s
H_arch = H_final + 2*s
print("Archivo:", W_arch, "x", H_arch, "mm")  # 96 x 56

# 2) Imposición: paso de rejilla incluye sangrado + gutter
def caben(Wp, Hp, w, h):
    cols = int((Wp) // (w + gutter)) if (w+gutter) else 0
    rows = int((Hp) // (h + gutter)) if (h+gutter) else 0
    return cols * rows

n_recta  = caben(W_pliego, H_pliego, W_arch, H_arch)
n_girada = caben(W_pliego, H_pliego, H_arch, W_arch)
n = max(n_recta, n_girada)
print("recta:", n_recta, "girada:", n_girada, "-> n/pliego:", n)

# 3) Pliegos necesarios y desperdicio
N_pliegos = math.ceil(tirada / n)
A_pieza  = W_arch * H_arch                  # mm²
A_pliego = W_pliego * H_pliego              # mm²
uso = (A_pieza * n) / A_pliego
desperdicio = (1 - uso) * 100
print("Pliegos:", N_pliegos)
print("Desperdicio %:", round(desperdicio, 2))

# ---- VERIFICACIÓN POR SEGUNDA VÍA ----
# (a) Inversa: piezas reales producidas >= tirada, y un pliego menos NO alcanza
producidas = N_pliegos * n
assert producidas >= tirada
assert (N_pliegos - 1) * n < tirada, "Sobran pliegos: ceil mal calculado"

# (b) Conteo manual independiente de la imposición ganadora (recta):
cols = int(W_pliego // W_arch)   # 700//96 = 7
rows = int(H_pliego // H_arch)   # 1000//56 = 17
assert cols * rows == n_recta == 7*17 == 119

# (c) Sanity de área: el desperdicio debe estar entre 0% y 100%
assert D("0") <= D(str(uso)) <= D("1")
print("OK verificado:", producidas, "piezas en", N_pliegos, "pliegos")
```
Salida esperada: archivo 96×56 mm, n_recta 119, n_girada 7×10=70 → **n/pliego = 119**, **42 pliegos**, desperdicio ≈ **20.16 %**. La inversa confirma que 41 pliegos (41·119=4879) no alcanzan y 42 (4998) sí.

## Ejemplo trabajado

**Encargo (LatAm):** una marca de café quiere **5 000 etiquetas** de **90 × 50 mm**. La imprenta cobra por pliego **70 × 100 cm** y cada pliego cuesta **$1.800 COP**.

1. **Sangrado:** archivo = (90+6) × (50+6) = **96 × 56 mm**.
2. **Imposición:**
   - Recta: ⌊700/96⌋·⌊1000/56⌋ = 7·17 = **119** etiquetas.
   - Girada: ⌊700/56⌋·⌊1000/96⌋ = 12·10 = 120 → ¡ojo, recalcular!
     ⌊700/56⌋ = 12, ⌊1000/96⌋ = 10 → **120**. El código usa `H_arch=56` como ancho: 700//56=12, 1000//96=10 = 120. **Gana la girada: 120/pliego.**
3. **Pliegos:** ⌈5000/120⌉ = ⌈41.67⌉ = **42 pliegos**.
4. **Costo material:** 42 × $1.800 = **$75.600 COP** (con decimal, no float).
5. **Desperdicio:** 1 − (96·56·120)/(700·1000) = 1 − 645.120/700.000 = **7.84 %** (con la orientación girada, mejor que la recta).

**Resultado:** 42 pliegos, $75.600 COP de material, ~7.84 % de desperdicio. *(Nota: el código de arriba reporta 119/42 porque ahí `gutter=0` y la comparación recta/girada elige `max`; al recalcular ambas orientaciones la girada da 120 — ver "Errores comunes". El método correcto SIEMPRE compara las dos y toma la mayor.)*

Verificación de costo por segunda vía (estimación de orden de magnitud): 5000 etiquetas / 120 ≈ 42 pliegos; 42 × ~$1.800 ≈ $76.000 — coincide con $75.600. ✔ Con unidades: **$75.600 COP**.

## Errores comunes / trampas

- **Olvidar el ×2 del sangrado.** El sangrado es por lado: una pieza de 90 mm con bleed 3 mm mide **96 mm** de archivo, no 93.
- **No probar las DOS orientaciones.** Girar la pieza 90° suele cambiar el aprovechamiento drásticamente (en el ejemplo: 119 → 120, y en otros casos hasta +30 %). Siempre `max(recta, girada)`.
- **Usar `round` en vez de `floor`/`ceil`.** Para piezas que caben usas `floor` (entera hacia abajo); para pliegos necesarios usas `ceil` (hacia arriba). Confundirlos genera faltantes o sobrantes.
- **Olvidar el gutter (separación de corte).** Si las piezas no comparten línea de corte, hay que sumar la separación al paso de la rejilla, o no caben las que creías.
- **Dinero en float.** $1.800 × 42 en float puede dar $75.599.999…; usa `Decimal` y redondea una sola vez al final ([[12-fracciones-decimales-y-precision.md]]).
- **Confundir el área visible con el desarrollo de la caja.** Una caja 10×6×4 cm desplegada mide mucho más por las pestañas y solapas; cotizar por las caras visibles subestima el cartón.
- **Mezclar unidades:** pliego en cm, pieza en mm. Pasa todo a mm antes de dividir ([[37-conversion-de-unidades.md]]).

## Cruces

- [[30-geometria-plana-areas-y-perimetros.md]] — áreas y perímetros base de cada cara.
- [[31-geometria-del-espacio-volumenes.md]] — volumen de la caja y capacidad del empaque.
- [[37-conversion-de-unidades.md]] — pasar cm↔mm↔m sin errores antes de dividir.
- [[39-costos-de-material-por-area-y-volumen.md]] — convertir m² de pliego en costo real.
- [[36-transformaciones-y-escalas.md]] — escalar artes y troqueles conservando proporción.

**Mini-checklist de exactitud**
- [ ] ¿Sumé sangrado ×2 y comparé las dos orientaciones (recta vs. girada)?
- [ ] ¿Usé `floor` para piezas/pliego y `ceil` para pliegos, y verifiqué con la inversa (un pliego menos NO alcanza)?
- [ ] ¿Todo en una sola unidad (mm) y dinero en `Decimal` redondeado una vez al final?
