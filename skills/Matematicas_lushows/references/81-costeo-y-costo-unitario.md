# 81 · Costeo y costo unitario

> **Qué resuelve / cuándo usarlo** — Saber cuánto cuesta REALMENTE producir una unidad (un plato, un producto, un Excel vendido) separando lo fijo de lo variable. Es la base honesta sobre la que se decide precio, margen y punto de equilibrio.

## Concepto (para no-experto)

**Costear** significa medir, en dinero, todo lo que se consume para producir y entregar lo que vendes. Si no costeas bien, fijas precios a ciegas y puedes estar vendiendo con pérdida sin darte cuenta.

Hay dos familias de costos, y confundirlas es el error #1:

- **Costo fijo (CF)**: lo que pagas SÍ o SÍ aunque no vendas ni una unidad. El arriendo del local, el sueldo del administrador, la licencia del software, internet. *Analogía:* es como la cuota de Netflix — pagas lo mismo veas 1 película o 100.
- **Costo variable (CV)**: lo que sube cada vez que produces UNA unidad más. En un restaurante: los ingredientes del plato, el empaque para domicilio, la comisión de la pasarela de pago. *Analogía:* es como la gasolina — cuanto más manejas (produces), más pagas.

Términos que definimos al usarlos:

- **Costo unitario total (CU)**: lo que cuesta, en promedio, cada unidad, incluyendo su parte de los fijos. Es CV por unidad **más** la "tajada" de los costos fijos que le toca a esa unidad.
- **Costo variable unitario (CVU)**: solo la parte variable de UNA unidad (los ingredientes de UN plato).
- **Food cost** (costo de receta / costo de alimentos): cuánto cuestan los ingredientes de una receta. Casi siempre se expresa también como **% del precio de venta** ("food cost %"). En gastronomía sano suele estar entre 25 % y 35 %.

La trampa central: el **costo unitario total depende de cuántas unidades produzcas**, porque los fijos se reparten entre más o menos unidades. Más volumen → cada unidad carga menos fijo → CU baja. Esto se llama *economía de escala* y mucha gente lo ignora.

## Fórmulas / método

Costo variable total para Q unidades:

```
CV_total = CVU · Q
```

Costo total:

```
CT = CF + CV_total = CF + CVU · Q
```

Costo unitario total (lo que cuesta en promedio cada unidad):

```
CU = CT / Q = CF/Q + CVU
```

Donde:
- `CF` = costos fijos del período (COP / mes)
- `CVU` = costo variable unitario (COP / unidad)
- `Q` = cantidad de unidades producidas/vendidas en el período (unidades)
- `CU` = costo unitario total (COP / unidad)

Food cost de una receta (suma de ingredientes a su costo por porción usada):

```
FoodCost_receta = Σ ( cantidad_usada_i · costo_por_unidad_i )
```

Food cost porcentual:

```
FoodCost% = FoodCost_receta / PrecioVenta · 100
```

**Costo por porción usable** (clave y muy olvidado): si compras a granel y hay merma (desperdicio: cáscaras, hueso, recortes), el costo real por gramo usable es mayor:

```
costo_por_g_usable = costo_compra / (peso_comprado · rendimiento)
```
donde `rendimiento` (yield) es la fracción aprovechable (0 < rendimiento ≤ 1). Si rindes 80 %, `rendimiento = 0.80`.

## Verificación en código

```python
from decimal import Decimal, ROUND_HALF_UP

# --- DINERO SIEMPRE EN Decimal, NUNCA float ---
def cop(x):
    """Redondea a peso entero (COP no usa centavos) UNA sola vez al final."""
    return Decimal(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

# Caso: dark kitchen que vende un solo plato (bowl de pollo)
CF  = Decimal("4500000")   # costos fijos del mes (arriendo+sueldos+servicios) [COP/mes]
Q   = Decimal("1500")      # platos vendidos en el mes [unidades]

# Costo variable unitario = suma de ingredientes + empaque + comisión por plato
ingredientes = Decimal("4200")   # COP/plato
empaque      = Decimal("600")    # COP/plato
comision     = Decimal("450")    # pasarela/domicilio por plato [COP/plato]
CVU = ingredientes + empaque + comision   # [COP/unidad]

CT = CF + CVU * Q                 # costo total [COP]
CU = CT / Q                       # costo unitario total [COP/unidad]
fijo_por_unidad = CF / Q          # tajada de fijo por plato [COP/unidad]

print("CVU           =", cop(CVU), "COP/plato")
print("Fijo/unidad   =", cop(fijo_por_unidad), "COP/plato")
print("Costo total   =", cop(CT), "COP")
print("Costo unitario=", cop(CU), "COP/plato")

# --- VERIFICACIÓN POR SEGUNDA VÍA #1: descomposición ---
# CU debe ser exactamente CVU + CF/Q
assert CU == CVU + CF / Q, "CU no coincide con su descomposición"

# --- VERIFICACIÓN POR SEGUNDA VÍA #2: operación inversa ---
# Si multiplico el CU por Q debo recuperar el costo total
assert (CU * Q) == CT, "CU·Q no reconstruye CT"

# --- SANITY CHECK de orden de magnitud ---
# Fijo/unidad ≈ 4.5M / 1500 = 3000; CVU = 5250; CU ≈ 8250
assert Decimal("8000") < CU < Decimal("8500"), "CU fuera del rango esperado"
print("Verificaciones OK")
```

Food cost con merma, verificado:

```python
from decimal import Decimal, ROUND_HALF_UP
def cop(x): return Decimal(x).quantize(Decimal("1"), ROUND_HALF_UP)

# Pechuga: compro 1000 g a 14.000 COP, rinde 80% (merma 20%)
costo_compra = Decimal("14000")     # COP
peso         = Decimal("1000")      # g comprados
rendimiento  = Decimal("0.80")      # fracción usable
costo_g_usable = costo_compra / (peso * rendimiento)   # COP/g usable

# La receta usa 150 g usables de pechuga
usado = Decimal("150")              # g usables
costo_pechuga_receta = costo_g_usable * usado          # COP

print("Costo/g usable     =", costo_g_usable, "COP/g")
print("Pechuga por receta =", cop(costo_pechuga_receta), "COP")

# VERIFICACIÓN: sin contar merma daría 14000/1000*150 = 2100; con merma debe ser 2100/0.8 = 2625
sin_merma = costo_compra/peso*usado
assert cop(costo_pechuga_receta) == cop(sin_merma/rendimiento), "merma mal aplicada"
print("OK:", cop(sin_merma), "->", cop(costo_pechuga_receta), "por la merma del 20%")
```

## Ejemplo trabajado

**Negocio:** dark kitchen en Bogotá, un plato (bowl de pollo).

Datos del mes:
- Costos fijos `CF` = 4 500 000 COP/mes (arriendo + 1 sueldo + servicios).
- Variables por plato: ingredientes 4 200 + empaque 600 + comisión 450 = `CVU` = 5 250 COP/plato.
- Ventas `Q` = 1 500 platos/mes.

Paso 1 — Fijo por unidad: 4 500 000 / 1 500 = **3 000 COP/plato**.
Paso 2 — Costo unitario total: `CU` = CVU + fijo/unidad = 5 250 + 3 000 = **8 250 COP/plato**.
Paso 3 — Verificación inversa: 8 250 × 1 500 = 12 375 000 = CF (4 500 000) + CV (5 250 × 1 500 = 7 875 000) ✓.

**Lectura de negocio:** si vendes el bowl a 18 000 COP, tu costo unitario es 8 250 → te quedan 9 750 de margen bruto por plato. Pero ojo: ese 3 000 de fijo por plato **solo es válido si de verdad vendes 1 500**. Si caes a 750 platos, el fijo por unidad se DUPLICA a 6 000 y el CU sube a 11 250 COP/plato.

Food cost % a 18 000 de precio, usando solo ingredientes (4 200): 4 200 / 18 000 = **23,3 %** — sano (rango típico 25–35 %).

## Errores comunes / trampas

- **Meter costos fijos dentro del CVU.** El arriendo no cambia por plato; va en CF, no en el costo variable. Mezclarlos infla el "costo por plato" de forma fantasma.
- **Olvidar la merma/yield.** Costear con el peso comprado y no con el usable subestima el food cost (a veces 15–25 %). Siempre dividir por el rendimiento.
- **Tratar el CU como una constante.** El costo unitario total cambia con el volumen porque los fijos se reparten. Nunca cites un CU sin decir a qué Q corresponde.
- **Usar `float` para dinero.** `0.1 + 0.2` en float no da `0.3`. Usa `Decimal` o centavos enteros; redondea una sola vez al final.
- **Olvidar costos variables "invisibles":** comisión de pasarela, empaque, domicilio, gas, mano de obra a destajo. Si escalan con cada unidad, son variables.
- **Confundir food cost (solo insumos) con costo unitario total** (insumos + fijos + todo lo demás). Son números distintos para decisiones distintas.

## Cruces

- [[80-margenes-bruto-contribucion-neto.md]] — del costo unitario sale el margen.
- [[82-pricing-markup-margin-y-elasticidad.md]] — fijar precio a partir del costo.
- [[76-punto-de-equilibrio.md]] — usa CF y CVU para hallar el Q mínimo.
- [[39-costos-de-material-por-area-y-volumen.md]] — costear insumos por área/volumen.
- [[03-protocolo-de-verificacion-por-codigo.md]] — patrón ejecutar+verificar aplicado aquí.

---

**Mini-checklist de exactitud**
- [ ] ¿Separé bien CF (no cambia con Q) de CV (escala con Q)?
- [ ] ¿Apliqué el rendimiento/merma al food cost y cité el Q al que corresponde el CU?
- [ ] ¿Dinero en `Decimal`, una sola vez redondeado, y verificado por la vía inversa (CU·Q = CT)?
