# 93 · Análisis de sensibilidad y escenarios

> **Qué resuelve / cuándo usarlo** — Cuando tienes un modelo (un VPN, un punto de equilibrio, un presupuesto) que depende de supuestos inciertos y necesitas saber **qué tan frágil es el resultado** y **cuáles variables mueven la aguja**. Responde a "¿qué pasa si...?" con números, no con corazonadas.

## Concepto (para no-experto)

Imagina que tu negocio es una receta y el resultado (la utilidad) es el sabor del plato. Algunos ingredientes, si te equivocas un poco en la cantidad, casi no cambian el sabor; otros, si te pasas un gramo, arruinan todo. El **análisis de sensibilidad** es probar la receta cambiando **un ingrediente a la vez** para descubrir cuáles son peligrosos (los que más mueven el sabor).

Definiciones clave la primera vez que aparecen:

- **Variable de entrada (input / supuesto)**: un número que asumes y que podría salir distinto en la realidad (precio de venta, unidades vendidas, costo del insumo, tasa de descuento).
- **Variable de salida (output / resultado)**: lo que te importa decidir (utilidad mensual, VPN, margen, punto de equilibrio).
- **Análisis de sensibilidad**: medir **cuánto cambia la salida** cuando mueves **una entrada** dejando las demás fijas (*ceteris paribus* = "todo lo demás igual").
- **Escenario**: una combinación **coherente** de varias entradas a la vez. Los tres clásicos son:
  - **Base** (lo más probable),
  - **Optimista** (todo sale bien, pero realista),
  - **Pesimista** (todo sale mal, pero realista, no apocalíptico).
- **Análisis de palanca (leverage / what-if)**: identificar qué entrada es la "palanca" más poderosa — la que, con un cambio pequeño, produce el mayor cambio en la salida.
- **Tabla de sensibilidad (data table)**: una rejilla que muestra la salida para muchas combinaciones de una o dos entradas.

Analogía cotidiana: ajustar el volumen, los graves y los agudos del equipo de sonido. Sensibilidad de un parámetro = mueves SOLO un control y oyes el cambio. Escenario = una "perilla maestra" que mueve varios controles juntos hacia "fiesta" o "estudio".

## Fórmulas / método

**1. Sensibilidad absoluta** (cuánto cambia la salida por unidad de entrada):

```
S_abs = (Y(x + Δx) − Y(x)) / Δx       [unidad de Y por unidad de x]
```

**2. Elasticidad (sensibilidad relativa, adimensional)** — la más comparable entre variables con unidades distintas:

```
E = (%ΔY) / (%Δx) = ( (Y₁ − Y₀)/Y₀ ) / ( (x₁ − x₀)/x₀ )
```

Donde:
- `Y` = variable de salida; `Y₀` valor base, `Y₁` valor con la entrada perturbada.
- `x` = variable de entrada; `x₀` valor base, `x₁` valor perturbado.
- `Δx` = `x₁ − x₀`. `%Δx = Δx/x₀`.
- `E` se lee: "si `x` sube 1 %, `Y` cambia `E` %". Su **valor absoluto |E|** ordena las palancas: mayor |E| = palanca más poderosa.

**3. Escenario**: cada escenario `s` fija un vector de entradas `(x₁, x₂, …, xₙ)` y se evalúa `Y_s = f(x₁, …, xₙ)`. No hay fórmula única: depende de tu modelo `f`.

**Unidades**: `S_abs` lleva unidades (p. ej. COP de utilidad por COP de precio). `E` es **adimensional** (un número puro). El dinero se calcula con `Decimal` (centavos exactos), nunca con `float`.

## Verificación en código

Modelo de ejemplo: utilidad mensual de un negocio = `(precio − costo_variable) × unidades − costos_fijos`.

```python
from decimal import Decimal, getcontext
getcontext().prec = 28

def utilidad(precio, costo_var, unidades, fijos):
    """Todos en Decimal. Retorna utilidad mensual en COP (Decimal)."""
    margen_unit = precio - costo_var          # COP/unidad
    return margen_unit * unidades - fijos      # COP/mes

# --- Caso base (supuestos) ---
base = dict(
    precio    = Decimal("10000"),   # COP por unidad
    costo_var = Decimal("4000"),    # COP por unidad
    unidades  = Decimal("800"),     # unidades/mes
    fijos     = Decimal("2000000"), # COP/mes
)
Y0 = utilidad(**base)
print("Utilidad base:", Y0, "COP/mes")   # 2,800,000

# --- Sensibilidad: perturbar cada entrada +10% (una a la vez) ---
def elasticidad(var, pct=Decimal("0.10")):
    perturbado = dict(base)
    x0 = base[var]
    x1 = x0 * (Decimal("1") + pct)
    perturbado[var] = x1
    Y1 = utilidad(**perturbado)
    pctY = (Y1 - Y0) / Y0
    E = pctY / pct
    return Y1, pctY, E

print("\nElasticidad de Y ante +10% en cada variable:")
ranking = []
for v in ("precio", "costo_var", "unidades", "fijos"):
    Y1, pctY, E = elasticidad(v)
    ranking.append((abs(E), v, E, Y1))
    print(f"  {v:10s}: Y={Y1:>12} | %ΔY={pctY*100:6.2f}% | E={E:+.3f}")

ranking.sort(reverse=True)
print("\nPalanca más poderosa (|E| mayor):", ranking[0][1])

# --- Escenarios coherentes ---
escenarios = {
    "pesimista": dict(precio=Decimal("9000"),  costo_var=Decimal("4500"),
                      unidades=Decimal("600"),  fijos=Decimal("2200000")),
    "base":      base,
    "optimista": dict(precio=Decimal("11000"), costo_var=Decimal("3800"),
                      unidades=Decimal("1000"), fijos=Decimal("1900000")),
}
print("\nEscenarios:")
for nombre, sup in escenarios.items():
    print(f"  {nombre:10s}: {utilidad(**sup)} COP/mes")
```

**Verificación por segunda vía** (recálculo manual independiente + assert):

```python
# Vía 2: la utilidad debe ser exactamente margen*Q - F, recomputado a mano.
# precio +10% => 11000; margen=11000-4000=7000; 7000*800=5,600,000; -2,000,000 = 3,600,000
Y_precio = utilidad(precio=Decimal("11000"), costo_var=Decimal("4000"),
                    unidades=Decimal("800"), fijos=Decimal("2000000"))
assert Y_precio == Decimal("3600000"), Y_precio
# %ΔY = (3,600,000-2,800,000)/2,800,000 = 800,000/2,800,000 = 0.285714...
# E = 0.285714.../0.10 = 2.857... -> coincide con la salida de elasticidad("precio")
E_precio = ((Y_precio - Decimal("2800000")) / Decimal("2800000")) / Decimal("0.10")
assert abs(E_precio - Decimal("2.857142857142857142857142857")) < Decimal("1e-20")
print("OK: verificación cruzada del precio exacta.")
```

## Ejemplo trabajado

Negocio de arepas (Bogotá). Base: precio **$10.000 COP/unidad**, costo variable **$4.000 COP/unidad**, **800 unidades/mes**, fijos **$2.000.000 COP/mes**.

Paso 1 — Utilidad base:
`(10.000 − 4.000) × 800 − 2.000.000 = 6.000 × 800 − 2.000.000 = 4.800.000 − 2.000.000 = **2.800.000 COP/mes**`.

Paso 2 — Sensibilidad +10 % (una variable a la vez), resultados del código:

| Variable | Y con +10 % | %ΔY | Elasticidad E |
|---|---|---|---|
| precio | 3.600.000 | +28,57 % | **+2,857** |
| unidades | 3.280.000 | +17,14 % | +1,714 |
| costo_var | 2.480.000 | −11,43 % | −1,143 |
| fijos | 2.600.000 | −7,14 % | −0,714 |

Paso 3 — Lectura: la **palanca más poderosa es el precio** (|E| = 2,857): subirlo 10 % sube la utilidad casi 29 %. Conclusión accionable: antes de pelear por bajar costos fijos (palanca débil, |E| = 0,714), conviene testear si el mercado aguanta un precio mayor.

Paso 4 — Escenarios (combinaciones coherentes):

| Escenario | Utilidad (COP/mes) |
|---|---|
| Pesimista (P=9.000, CV=4.500, Q=600, F=2.200.000) | **500.000** |
| Base | 2.800.000 |
| Optimista (P=11.000, CV=3.800, Q=1.000, F=1.900.000) | **5.300.000** |

Decisión: incluso en el pesimista el negocio queda **positivo** (+500.000 COP/mes). Es un modelo robusto, no frágil. Todas las cifras con unidad COP/mes verificadas por segunda vía.

## Errores comunes / trampas

- **Mover dos variables y atribuir el efecto a una sola.** La sensibilidad pura exige *ceteris paribus*: una entrada cambia, las demás se quedan fijas.
- **Comparar sensibilidades absolutas con unidades distintas** (COP/unidad vs unidades/mes). No son comparables; usa **elasticidad** (adimensional) para rankear palancas.
- **Escenarios incoherentes / "doble conteo"**: en optimista subir precio Y bajar costo Y subir volumen a la vez puede ser contradictorio (subir precio suele bajar volumen). Que cada escenario cuente una historia creíble.
- **Pesimismo de fantasía** (ventas en cero) u **optimismo de fantasía** (todo a tope): inútiles para decidir. Usa rangos realistas (p. ej. percentil 10 y 90 de lo plausible).
- **Float para dinero**: `0.1 + 0.2 != 0.3`. Usa `Decimal` o centavos enteros.
- **Sensibilidad alrededor de saltos**: cerca del punto de equilibrio o de un umbral, un cambio pequeño puede cruzar de pérdida a ganancia; reporta también ese umbral, no solo la pendiente.
- **Tablas de sensibilidad gigantes sin sanity check**: valida al menos una celda a mano.

## Cruces

- [[74-vpn-y-tir.md]] — la salida más típica sobre la que se hace sensibilidad y escenarios.
- [[76-punto-de-equilibrio.md]] — umbral donde la utilidad cruza cero; clave para escenarios pesimistas.
- [[58-simulacion-monte-carlo.md]] — el paso siguiente: en vez de 3 escenarios, miles de combinaciones aleatorias.
- [[90-teoria-de-decisiones.md]] — cómo elegir entre escenarios bajo incertidumbre.
- [[86-forecasting-y-proyeccion.md]] — de dónde salen los supuestos base/optimista/pesimista.

**Mini-checklist de exactitud**
1. ¿Cada sensibilidad movió **una sola** variable (ceteris paribus) y el resto quedó en base?
2. ¿El dinero se calculó con `Decimal` y verifiqué al menos una celda por segunda vía?
3. ¿Los tres escenarios son **coherentes** y realistas (no fantasía), con unidades en cada cifra?
