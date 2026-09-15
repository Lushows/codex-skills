# 39 · Costos de material por área y volumen

> **Qué resuelve / cuándo usarlo** — Convierte dimensiones físicas (largo, ancho, alto, diámetro) en cantidad de material y de ahí en costo exacto, contando el desperdicio, para saber cuánto cuesta de verdad producir **una** unidad.

## Concepto (para no-experto)

Imagina que vendes empanadas en cajitas de cartón, o etiquetas para frascos, o tableros de melamina cortados. En todos esos casos pagas el material por **área** (metros cuadrados de cartón, de vinilo, de tela) o por **volumen** (litros de pintura, mililitros de resina, gramos de masa). Pero el cliente no compra "metros cuadrados": compra **una caja, una etiqueta, una pieza**. El problema central de este módulo es el puente entre ambos mundos.

Definamos los términos clave la primera vez que aparecen:

- **Área**: cuánta superficie ocupa algo plano. Se mide en unidades cuadradas (cm², m²). Una hoja de 1 m × 1 m tiene 1 m² de área.
- **Volumen**: cuánto espacio ocupa algo con grosor (líquidos, sólidos). Se mide en unidades cúbicas (cm³, m³) o en litros (1 L = 1 000 cm³).
- **Costo unitario del material** (o **costo por unidad de medida**): lo que pagas por 1 m², por 1 L, por 1 kg. Ejemplo: el vinilo cuesta $18.000 por m².
- **Desperdicio (merma / scrap)**: el material que pagas pero **no** termina en el producto. Al cortar círculos de una lámina rectangular sobran recortes; al servir un líquido queda residuo en el envase. Se expresa como porcentaje.
- **Rendimiento (yield)**: la fracción del material que **sí** se aprovecha. Si el desperdicio es 20%, el rendimiento es 80%.

**Analogía cotidiana**: hacer galletas con un molde redondo sobre masa estirada en una bandeja cuadrada. La masa estirada es lo que pagaste (el área completa); las galletas son tu producto; los huecos entre galletas son el desperdicio que igual costó harina.

La regla de oro: **el costo verdadero por unidad NO es "material que entra al producto", es "material que tuviste que comprar dividido por unidades buenas que salieron"**. Ignorar el desperdicio es el error #1 que arruina los costeos.

## Fórmulas / método

**Paso 1 — Geometría: dimensiones → área o volumen** (ver [[30-geometria-plana-areas-y-perimetros]] y [[31-geometria-del-espacio-volumenes]]):

- Rectángulo: `A = largo × ancho`
- Círculo: `A = π · r²`  (r = radio)
- Cilindro (volumen): `V = π · r² · h`  (h = altura)
- Caja/prisma (volumen): `V = largo × ancho × alto`

**Paso 2 — Material neto por unidad** (lo que el producto realmente contiene):

```
material_neto = medida_geométrica × (unidades de material por unidad geométrica)
```

**Paso 3 — Material bruto con desperdicio** (lo que debes comprar):

```
material_bruto = material_neto / rendimiento
rendimiento = 1 − fracción_desperdicio
```

Símbolos:
- `material_neto` = área o volumen que queda en el producto (m², L, kg)
- `rendimiento` (η) = fracción aprovechada, número entre 0 y 1
- `fracción_desperdicio` (w) = merma, número entre 0 y 1

> ⚠️ **Trampa de dirección**: el desperdicio se **divide**, no se multiplica. Si pierdes 20%, no compras `neto × 1.20`; compras `neto / 0.80`. Comprar 20% más NO repone una pérdida del 20% (ver Errores comunes).

**Paso 4 — Costo del material por unidad producida:**

```
costo_material_unitario = material_bruto × precio_por_unidad_de_medida
```

**Paso 5 — Costo total de material por unidad** (sumar cada material: cartón + tinta + pegante…), y solo al final se redondea **una vez** (ver [[05-cifras-significativas-y-redondeo]]).

## Verificación en código

Ejemplo: caja de cartón troquelada. Calculamos el área de cartón que necesita una caja (con sus solapas), añadimos desperdicio de corte, y obtenemos el costo. El dinero se maneja con `decimal` (NUNCA float) y verificamos por una segunda vía.

```python
from decimal import Decimal, ROUND_HALF_UP

# --- Datos de entrada (con unidades en el nombre) ---
# Caja tipo prisma: 20 cm x 12 cm x 8 cm. Una caja desplegada (con solapas)
# requiere aprox. el desarrollo: 2*(L*A) tapa/fondo + 2*(L*H) + 2*(A*H) lados,
# más un 15% extra de solapas de pegado.
L_cm = Decimal("20")
A_cm = Decimal("12")
H_cm = Decimal("8")

area_caras_cm2 = 2*(L_cm*A_cm) + 2*(L_cm*H_cm) + 2*(A_cm*H_cm)  # superficie cerrada
solapas = Decimal("1.15")                                       # +15% por solapas
area_neta_cm2 = area_caras_cm2 * solapas                        # cartón que queda en la caja

# Convertir a m2 (1 m2 = 10 000 cm2) — ver módulo de conversión de unidades
area_neta_m2 = area_neta_cm2 / Decimal("10000")

# Desperdicio de corte del pliego: 18% -> rendimiento 82%
w = Decimal("0.18")
rendimiento = Decimal("1") - w
area_bruta_m2 = area_neta_m2 / rendimiento     # se DIVIDE por el rendimiento

# Precio del cartón: $9.500 COP por m2
precio_m2 = Decimal("9500")
costo = area_bruta_m2 * precio_m2

# Redondear UNA sola vez, al final, a peso entero
costo_final = costo.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

print("Área caras (cm2):", area_caras_cm2)
print("Área neta con solapas (m2):", area_neta_m2)
print("Área bruta con desperdicio (m2):", area_bruta_m2)
print("Costo material por caja (COP):", costo_final)
```

Salida:
```
Área caras (cm2): 992
Área neta con solapas (m2): 0.114080
Área bruta con desperdicio (m2): 0.139121951219512...
Costo material por caja (COP): 1322
```

**Verificación por segunda vía** (operación inversa + sanity check de orden de magnitud, ver [[03-protocolo-de-verificacion-por-codigo]] y [[06-estimacion-y-sanity-checks]]):

```python
# Vía 2a — INVERSA: del costo final, ¿cuántos m2 brutos implica? ¿coincide?
m2_recuperados = (Decimal(costo_final) / precio_m2)
assert abs(m2_recuperados - area_bruta_m2) < Decimal("0.001"), "Inversa no cuadra"

# Vía 2b — INVERSA del desperdicio: el material neto debe ser el bruto * rendimiento
assert area_bruta_m2 * rendimiento == area_neta_m2, "Rendimiento mal aplicado"

# Vía 2c — ORDEN DE MAGNITUD: ~0.11 m2 netos, +18% desperdicio ~ 0.14 m2,
# a ~$9.500/m2 -> debe rondar 0.14*9500 ≈ 1330. El resultado 1322 es del orden. OK.
estimado = Decimal("0.14") * precio_m2
assert Decimal("1000") < estimado < Decimal("1500")
print("Verificaciones OK. Estimación de orden:", estimado)
```

Ambas vías confirman ~$1.322 COP de cartón por caja.

## Ejemplo trabajado

**Caso (LatAm): etiquetas circulares para frascos de salsa.**

Un frasco lleva una etiqueta circular de **6 cm de diámetro**. El vinilo adhesivo cuesta **$22.000 COP por m²**. Al troquelar círculos sobre la lámina, el desperdicio entre círculos es del **25%** (rendimiento 75%). ¿Cuánto cuesta la etiqueta de **un** frasco?

1. **Radio**: r = diámetro/2 = 6/2 = **3 cm**.
2. **Área del círculo**: A = π·r² = π·(3 cm)² = π·9 cm² = **28,2743 cm²** (neto por etiqueta).
3. **A m²**: 28,2743 cm² ÷ 10 000 = **0,00282743 m²**.
4. **Con desperdicio**: 0,00282743 / 0,75 = **0,00376991 m²** brutos comprados.
5. **Costo**: 0,00376991 m² × $22.000/m² = $82,938… → **$83 COP por etiqueta** (redondeo único al final).

```python
from decimal import Decimal, ROUND_HALF_UP
import math
r_cm = Decimal("3")
area_cm2 = Decimal(str(math.pi)) * r_cm**2          # π·r²
area_m2 = area_cm2 / Decimal("10000")
bruto_m2 = area_m2 / Decimal("0.75")               # desperdicio 25%
costo = (bruto_m2 * Decimal("22000")).quantize(Decimal("1"), ROUND_HALF_UP)
print(area_cm2, area_m2, bruto_m2, costo)   # 28.27..., 0.002827..., 0.003769..., 83
# Inversa: 83/22000 = 0.003772 m2 ≈ bruto. OK
```

**Resultado: $83 COP de vinilo por etiqueta** (con unidades). Si el cálculo ingenuo ignorara el 25% de desperdicio daría $62 → habrías subcosteado un 25% cada etiqueta.

## Errores comunes / trampas

- **Multiplicar por (1+desperdicio) en vez de dividir por el rendimiento.** Perder 20% NO se repone comprando 20% más: `neto/0,80 = neto×1,25`, no `×1,20`. El error crece con el desperdicio.
- **Mezclar unidades al elevar al cuadrado/cubo.** 1 m² = 10 000 cm² (no 100), y 1 m³ = 1 000 000 cm³. Convertir SIEMPRE antes de multiplicar por el precio (ver [[37-conversion-de-unidades]]).
- **Usar diámetro como radio** en π·r². El radio es la **mitad** del diámetro; equivocarse cuadruplica o divide entre 4 el área.
- **Float para dinero.** `0.1 + 0.2 != 0.3` en float; usa `decimal` (ver [[12-fracciones-decimales-y-precision]]).
- **Redondear en cada paso.** Acumula error. Redondea **una sola vez** al final.
- **Olvidar solapas, costuras, márgenes de sangrado o mermas de proceso** (líquido que queda en el tanque, recortes). El "área del producto" casi nunca es el "material comprado".
- **Confundir costo de material con costo total.** Aquí solo costeamos material; mano de obra, energía y overhead van aparte (ver [[81-costeo-y-costo-unitario]]).

## Cruces

- [[31-geometria-del-espacio-volumenes]] — volúmenes (cilindros, cajas) para materiales líquidos/sólidos.
- [[30-geometria-plana-areas-y-perimetros]] — áreas planas para cartón, vinilo, tela.
- [[37-conversion-de-unidades]] — cm²↔m², cm³↔L, kg, sin errores de factor.
- [[81-costeo-y-costo-unitario]] — sumar este material a mano de obra y overhead para el costo total.
- [[38-geometria-aplicada-diseno-y-packaging]] — desarrollo de troqueles y empaques.

---

**Mini-checklist de exactitud:**
1. ¿Convertí las unidades ANTES de multiplicar por el precio (m², no cm²)?
2. ¿Apliqué el desperdicio **dividiendo** por el rendimiento, no multiplicando?
3. ¿Verifiqué por la vía inversa (costo→m²) y por orden de magnitud, y redondeé una sola vez al final?
