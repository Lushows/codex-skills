# 04 · Notación, unidades y dimensiones

> **Qué resuelve / cuándo usarlo** — Te da un blindaje casi infalible contra errores: si las **unidades** no cuadran al final de un cálculo, el cálculo está mal, punto. Úsalo siempre que mezcles cantidades del mundo real (pesos, kilos, horas, porcentajes, clientes) antes de creerte cualquier resultado.

## Concepto (para no-experto)

Un número solo casi nunca dice la verdad completa. "Compré 3" no significa nada hasta que digas "3 **qué**": ¿3 kilos?, ¿3 pesos?, ¿3 pizzas? Esa etiqueta —kilos, pesos, pizzas— es la **unidad**, y es **parte inseparable del número**. Tratar `15.000` como "quince mil" a secas es el origen de fortunas perdidas; `15.000 COP/kg` (quince mil pesos colombianos por kilo) es información que puedes usar sin equivocarte.

Definamos los términos clave la primera vez:

- **Unidad**: la cosa que estás contando o midiendo (peso colombiano `COP`, kilogramo `kg`, hora `h`, unidad de producto `und`, cliente, porción).
- **Magnitud** (o **dimensión**): la *categoría física* de la unidad. Ejemplos de dimensiones: longitud (L), masa (M), tiempo (T), dinero (que tratamos como una dimensión propia, $). El metro y el centímetro son **unidades distintas** de la **misma dimensión** (longitud). Los pesos y los kilos son dimensiones **distintas**: no se pueden sumar jamás.
- **Análisis dimensional**: la técnica de arrastrar las unidades por todo el cálculo —como si fueran factores de una multiplicación— y exigir que el resultado tenga la unidad correcta. Es tu detector de mentiras.

**Analogía cotidiana.** Las unidades funcionan como las fracciones que se cancelan. Si multiplicas `(3 manzanas/caja) × (4 cajas)`, la palabra "cajas" se tacha arriba y abajo y queda `12 manzanas`. Igual que en `(3/caja) × (4 caja) = 12`. Si al final te quedara "manzanas·caja" o "manzanas/caja²", sabrías que algo está roto **sin revisar la aritmética**. Eso es el superpoder: detectas el error por la *forma*, no por la cuenta.

**Regla de oro #1**: solo puedes **sumar o restar** cantidades de la **misma unidad**. `5 kg + 3 kg = 8 kg` ✅. `5 kg + 3 COP` = error sin sentido ❌.

**Regla de oro #2**: al **multiplicar o dividir**, las unidades se multiplican y dividen *junto con* los números, y se cancelan cuando aparecen arriba y abajo.

## Fórmulas / método

Una **cantidad física** se escribe siempre como:

```
cantidad = valor_numérico × unidad
```

Ejemplo: `precio = 15000 × (COP/kg)`. El "15000" sin la `COP/kg` está incompleto.

**Cancelación de unidades (el motor del método).** Para convertir o combinar, multiplicas por **factores de conversión**, que son fracciones que valen exactamente 1 porque numerador y denominador son la misma cantidad expresada distinto. Ejemplo: `1 kg = 1000 g`, así que `(1000 g / 1 kg) = 1`. Multiplicar por 1 no cambia el valor, pero sí reescribe la unidad:

```
masa = 2.5 kg × (1000 g / 1 kg) = 2500 g
                  └─ kg se cancela ─┘
```

**Receta general (método de los factores en cadena):**

1. Escribe la cantidad de partida **con su unidad**.
2. Decide la unidad **objetivo** del resultado.
3. Encadena factores de conversión `(=1)` orientados para que cada unidad indeseada quede una vez arriba y una vez abajo y se tache.
4. Multiplica los números; lo único que debe sobrevivir es la unidad objetivo.
5. Si sobrevive otra unidad → el cálculo está mal. Corrige la orientación de los factores.

**Notación consistente (convenciones que usamos siempre):**

- Moneda con código ISO: `COP`, `USD`, `MXN`, `EUR` (no "$" a secas, que es ambiguo entre países).
- Separadores claros: en Colombia el **punto** es de miles y la **coma** de decimales (`15.000,50 COP`). En código y en formato internacional usamos punto decimal (`15000.50`). Declara cuál estás usando para no confundir 1.500 (mil quinientos) con 1.500 (uno coma cinco).
- Tasas y "por": `COP/und`, `kg/mes`, `clientes/día`. La barra `/` se lee "por".
- Porcentaje: es **adimensional** (`% = 1/100`), pero siempre di "% **de qué**" (ver [[14-porcentajes-sin-errores]]).

## Verificación en código

Usamos la librería `pint` cuando esté disponible (lleva las unidades por ti y *explota* si no cuadran), y `decimal` para el dinero (ver [[12-fracciones-decimales-y-precision]]). El bloque incluye un **fallback** sin `pint` para que sea ejecutable en cualquier entorno.

```python
# Objetivo: costo de materia prima de una receta y verificación dimensional.
# Datos: una salsa usa 250 g de queso; el queso cuesta 28.000 COP/kg.
# Pregunta: ¿cuánto cuesta el queso por porción de salsa? -> resultado en COP.

from decimal import Decimal, ROUND_HALF_UP

# --- Dinero SIEMPRE con Decimal, nunca float ---
precio_por_kg = Decimal("28000")   # COP / kg
cantidad_g    = Decimal("250")     # g

# Factor de conversión: 1 kg = 1000 g  =>  (1 kg / 1000 g) = 1
# Encadenamos para que 'g' y 'kg' se cancelen y sobreviva COP:
#   g * (kg/g) * (COP/kg) = COP
cantidad_kg = cantidad_g / Decimal("1000")          # g -> kg (g se cancela)
costo = cantidad_kg * precio_por_kg                  # kg -> COP (kg se cancela)
costo = costo.quantize(Decimal("1"), rounding=ROUND_HALF_UP)  # redondeo final, 1 sola vez
print("Costo del queso por porción:", costo, "COP")   # -> 7000 COP
```

```python
# === VERIFICACIÓN POR SEGUNDA VÍA ===
# Vía A (arriba): por regla de tres / factores -> 7000 COP
# Vía B: análisis dimensional automático con pint (falla solo si las unidades NO cuadran)
try:
    import pint
    u = pint.UnitRegistry()
    # Definimos COP como una "moneda" (unidad nueva, dimensión propia [moneda])
    u.define("COP = [moneda]")
    precio = 28000 * u.COP / u.kg
    cant   = 250 * u.g
    costo_pint = (cant * precio).to(u.COP)   # pint cancela g/kg solo; si no cuadrara, lanzaría error
    # Comparamos magnitudes (orden de magnitud + valor)
    assert abs(costo_pint.magnitude - 7000) < 1e-9, "Discrepancia entre vías"
    assert str(costo_pint.units) == "COP", f"Unidad final inesperada: {costo_pint.units}"
    print("pint confirma:", costo_pint)      # -> 7000.0 COP
except ImportError:
    # Vía B alternativa (sin pint): estimación de orden de magnitud (sanity check)
    # 250 g es 1/4 de kg; 1/4 de 28.000 ≈ 7.000. Orden de magnitud correcto. ✅
    aprox = 28000 * 0.25
    assert abs(aprox - 7000) < 1, "Estimación no concuerda"
    print("Estimación de orden de magnitud confirma ~", aprox, "COP")
```

Si por error hubiéramos hecho `cantidad_g * precio_por_kg` (sin convertir), `pint` habría dado `g·COP/kg` —una unidad absurda— y habría delatado el bug. Esa es la idea: que el código grite cuando las unidades no cierran.

## Ejemplo trabajado

**Problema (LatAm, dark kitchen).** Un domiciliario recorre **12 km** por pedido. La moto rinde **40 km/L** (kilómetros por litro) y la gasolina cuesta **15.900 COP/L**. ¿Cuál es el costo de combustible **por pedido**? El resultado debe quedar en **COP/pedido**.

Encadenamos factores para que se cancele todo menos `COP/pedido`:

```
costo = 12 (km/pedido) × ( 1 L / 40 km ) × ( 15.900 COP / 1 L )
```

Cancelación paso a paso:
- `km` aparece arriba (en `km/pedido`) y abajo (en `1 L / 40 km`) → se tacha.
- `L` aparece arriba (en `1 L / 40 km`) y abajo (en `15.900 COP / L`) → se tacha.
- Sobrevive: `COP / pedido`. ✅ La unidad ya es la correcta **antes** de hacer la cuenta.

Números:
```
12 / 40 = 0,30 L/pedido
0,30 L/pedido × 15.900 COP/L = 4.770 COP/pedido
```

```python
from decimal import Decimal, ROUND_HALF_UP
dist   = Decimal("12")      # km/pedido
rend   = Decimal("40")      # km/L
precio = Decimal("15900")   # COP/L
litros = dist / rend                    # km/pedido ÷ km/L = L/pedido (km se cancela)
costo  = (litros * precio).quantize(Decimal("1"), rounding=ROUND_HALF_UP)  # L se cancela -> COP
print(costo, "COP/pedido")              # -> 4770 COP/pedido

# Verificación inversa: si gasto 4770 COP/pedido y la gasolina vale 15900 COP/L,
# entonces consumí 4770/15900 = 0,30 L; a 40 km/L eso son 0,30*40 = 12 km. ✅ vuelve al dato original.
assert (costo / precio) * rend == dist
```

**Resultado: 4.770 COP por pedido**, verificado por la operación inversa (que reconstruye los 12 km originales).

## Errores comunes / trampas

- **Sumar peras con manzanas.** Sumar `COP + USD`, `kg + g` o `horas + minutos` sin convertir. Si las unidades no son idénticas, **no se suman**.
- **Olvidar convertir y mezclar prefijos.** `250 g × 28.000 COP/kg` directo da basura. Siempre lleva todo a una sola unidad antes de multiplicar tasas.
- **Confiar en el número desnudo.** Reportar "el costo es 4770" sin la unidad: el que lo lea puede creer que son dólares, o por mes, o por kilo.
- **Separador de miles vs. decimal.** `1.500` puede ser "mil quinientos" (COL) o "uno coma cinco" (USA). Declara la convención. En código, usa punto decimal y nada de separador de miles.
- **Porcentaje sin referente.** "Subió 30%" — ¿30% de qué base? El % es adimensional pero necesita su "de qué" (ver [[14-porcentajes-sin-errores]]).
- **Tasas invertidas.** Confundir `km/L` con `L/km`. El análisis dimensional lo atrapa: si el resultado sale en una unidad rara, invertiste un factor.
- **Dinero en float.** `0.1 + 0.2 != 0.3` en float. Para plata, `Decimal` o centavos enteros, siempre (ver [[12-fracciones-decimales-y-precision]]).

## Cruces

- [[03-protocolo-de-verificacion-por-codigo]] — el patrón "ejecutar + verificar por segunda vía" que aquí aplicamos a unidades.
- [[37-conversion-de-unidades]] — la mecánica completa de factores de conversión y tablas.
- [[06-estimacion-y-sanity-checks]] — la estimación de orden de magnitud como segunda vía rápida.
- [[14-porcentajes-sin-errores]] — el caso especial de la unidad adimensional "%".
- [[17-notacion-cientifica-y-magnitudes]] — notación y prefijos para números muy grandes o pequeños.

**Mini-checklist de exactitud**
- [ ] Cada número del resultado lleva su unidad explícita (incluida la moneda con código ISO).
- [ ] Arrastré las unidades por el cálculo y solo sobrevive la unidad objetivo (si no, hay bug).
- [ ] Verifiqué por segunda vía (inversa, pint o estimación de orden de magnitud) y coincide.
