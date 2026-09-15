# 37 · Conversión de unidades

> **Qué resuelve / cuándo usarlo** — Cuando un número viene en una unidad (gramos, litros, pies, USD) y necesitas el mismo valor en otra (kilos, mililitros, metros, COP) SIN equivocarte. Convertir mal es una de las causas #1 de errores caros.

## Concepto (para no-experto)

Una **unidad** es la "regla con la que medimos" algo: el metro mide longitud, el kilogramo mide masa, el litro mide volumen. Convertir una unidad a otra **no cambia la cantidad real** — solo cambia cómo la escribimos. 5.000 gramos y 5 kilogramos son *exactamente la misma masa*, igual que "una docena" y "12" son la misma cantidad.

Analogía cotidiana: cambiar de pesos a dólares no te hace más rico ni más pobre; solo expresas el mismo dinero con otra "vara de medir". Si lo haces mal, parece que tienes 1.000 veces más (o menos) de lo que realmente tienes.

Dos grandes familias de unidades:

- **SI (Sistema Internacional)** — el que usa casi todo el mundo y la ciencia: metro (m), kilogramo (kg), litro (L), segundo (s), grado Celsius (°C). Es **decimal**: todo va de 10 en 10 (1 km = 1.000 m, 1 kg = 1.000 g). Limpio y predecible.
- **Imperial / US** — el de Estados Unidos y algo del Reino Unido: pulgada (in), pie (ft), libra (lb), galón (gal), grado Fahrenheit (°F). Los factores son "feos" (1 ft = 12 in, 1 lb = 16 oz). Más fácil equivocarse.

La herramienta clave para no fallar se llama **análisis dimensional** o **cancelación de unidades**: tratamos las unidades como si fueran números que se multiplican y se simplifican (tachan) entre sí.

## Fórmulas / método

**Regla de oro — multiplicar por 1:**

Un **factor de conversión** es una fracción que vale exactamente 1 porque arriba y abajo es la misma cantidad. Ejemplos (todos = 1):

$$\frac{1\ \text{kg}}{1000\ \text{g}} = 1 \qquad \frac{1000\ \text{g}}{1\ \text{kg}} = 1 \qquad \frac{2.54\ \text{cm}}{1\ \text{in}} = 1$$

Multiplicar por 1 no cambia el valor, solo la unidad. La conversión general:

$$\text{valor}_{\text{destino}} = \text{valor}_{\text{origen}} \times \frac{\text{unidad}_{\text{destino}}}{\text{unidad}_{\text{origen}}}$$

**Cancelación de unidades:** ordena los factores para que la unidad que quieres eliminar quede una vez arriba y una vez abajo, y se *tache*. Lo que sobra es tu respuesta:

$$5\ \cancel{\text{kg}} \times \frac{1000\ \text{g}}{1\ \cancel{\text{kg}}} = 5000\ \text{g}$$

**Definiciones exactas que conviene memorizar** (son definiciones, no medidas aproximadas):

| Conversión | Factor EXACTO |
|---|---|
| 1 pulgada (in) | 2.54 cm (por definición desde 1959) |
| 1 pie (ft) | 12 in = 30.48 cm |
| 1 milla (mi) | 1.609344 km |
| 1 libra (lb) | 0.45359237 kg |
| 1 onza (oz, masa) | 28.349523125 g |
| 1 galón US (gal) | 3.785411784 L |
| 1 litro (L) | 1000 cm³ = 1 dm³ |

**Temperatura** (NO es proporcional, lleva suma — ojo):

$$°C = (°F - 32) \times \tfrac{5}{9} \qquad °F = °C \times \tfrac{9}{5} + 32 \qquad K = °C + 273.15$$

**Unidades al cuadrado y al cubo:** el factor se eleva al mismo exponente. 1 m = 100 cm, pero 1 m² = (100)² = 10.000 cm², y 1 m³ = (100)³ = 1.000.000 cm³. Este es uno de los errores más comunes.

## Verificación en código

```python
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 40  # alta precisión para dinero/medidas

# --- Factores EXACTOS como fracciones (cero error de float) ---
IN_A_CM   = Fraction(254, 100)            # 1 in = 2.54 cm exacto
LB_A_KG   = Fraction(45359237, 100000000) # 1 lb = 0.45359237 kg exacto
GAL_A_L   = Fraction(3785411784, 1000000000)  # 1 gal US = 3.785411784 L

def lb_a_kg(libras):
    return Fraction(libras) * LB_A_KG

def millas_a_km(millas):
    return Fraction(millas) * Fraction(1609344, 1000000)  # 1 mi = 1.609344 km

# Ejemplo: una receta pide 3 lb de harina -> ¿cuántos kg?
kg = lb_a_kg(3)
print("3 lb =", float(kg), "kg")          # 1.36077711 kg

# Conversión de área: 1 m2 a cm2 (factor AL CUADRADO)
m2_a_cm2 = (Fraction(100))**2
print("1 m2 =", int(m2_a_cm2), "cm2")      # 10000

# Temperatura (lleva suma, no es proporcional)
def f_a_c(f):
    return (Fraction(f) - 32) * Fraction(5, 9)
print("212 F =", float(f_a_c(212)), "C")   # 100.0
```

```python
# --- VERIFICACIÓN POR SEGUNDA VÍA: la conversión inversa debe devolver el original ---
# Si convierto ida y vuelta, tengo que volver EXACTO al punto de partida.
ida   = lb_a_kg(3)            # lb -> kg
vuelta = ida / LB_A_KG        # kg -> lb (inversa)
assert vuelta == Fraction(3), f"Roundtrip falló: {vuelta}"

# Sanity check de orden de magnitud: 1 milla es algo MÁS que 1.6 km
assert 1.6 < float(millas_a_km(1)) < 1.7

# Temperatura: punto de congelación del agua 32 F = 0 C
assert f_a_c(32) == 0

# Área al cuadrado: 1 m2 NO es 100 cm2 (error típico), es 10000
assert m2_a_cm2 == 10000
print("Todas las verificaciones OK")
```

Usar `Fraction` garantiza que los factores definidos como exactos (2.54, 0.45359237) no se contaminen con el error binario de los `float`. Para dinero convertido entre monedas, usar `Decimal` y redondear **una sola vez** al final.

## Ejemplo trabajado

**Contexto LatAm:** Un proveedor de EE. UU. te vende aceite a **3.20 USD por galón**. Quieres saber el costo **en COP por litro** para tu calculadora de costos. Tasa de cambio: **1 USD = 4.000 COP** (ejemplo).

Paso 1 — convertir galón a litro (cancelación de unidades):

$$\frac{3.20\ \text{USD}}{1\ \cancel{\text{gal}}} \times \frac{1\ \cancel{\text{gal}}}{3.785411784\ \text{L}} = \frac{3.20}{3.785411784}\ \frac{\text{USD}}{\text{L}} = 0.845360\ \tfrac{\text{USD}}{\text{L}}$$

Paso 2 — convertir USD a COP:

$$0.845360\ \tfrac{\cancel{\text{USD}}}{\text{L}} \times \frac{4000\ \text{COP}}{1\ \cancel{\text{USD}}} = 3381.44\ \tfrac{\text{COP}}{\text{L}}$$

```python
from decimal import Decimal, ROUND_HALF_UP
usd_por_gal = Decimal("3.20")
litros_por_gal = Decimal("3.785411784")
cop_por_usd = Decimal("4000")

cop_por_litro = (usd_por_gal / litros_por_gal) * cop_por_usd
# redondear UNA vez, al final, a pesos enteros
print(cop_por_litro.quantize(Decimal("1"), rounding=ROUND_HALF_UP))  # 3381 COP/L
```

**Resultado: ≈ 3.381 COP por litro.**

Verificación de orden de magnitud: un galón cuesta 3.20 × 4.000 = 12.800 COP; un galón son ~3.79 L; 12.800 ÷ 3.79 ≈ 3.378 COP/L. Coincide con 3.381 (la pequeña diferencia es el redondeo). ✓

## Errores comunes / trampas

- **Confundir el sentido del factor** (multiplicar cuando había que dividir). Antídoto: escribe siempre la cancelación de unidades; si la unidad vieja no se tacha, el factor está al revés.
- **Unidades al cuadrado/cubo sin elevar el factor.** 1 m³ = 1.000.000 cm³, no 100. Pasa mucho en áreas (packaging, terrenos) y volúmenes.
- **Temperatura tratada como proporción.** 20 °C NO es "el doble" de 10 °C, y °F lleva el +32. La conversión tiene suma, no solo multiplicación.
- **Litro vs. kilogramo.** 1 L de agua ≈ 1 kg, pero 1 L de aceite ≈ 0.92 kg y 1 L de miel ≈ 1.4 kg. Volumen y masa solo se igualan con la **densidad**.
- **Galón US vs. galón imperial (UK).** 1 gal US = 3.785 L, pero 1 gal UK = 4.546 L. Confirma cuál.
- **Onza de masa vs. onza líquida.** "oz" puede ser peso (28.35 g) o volumen (29.57 mL). No son lo mismo.
- **Redondear en cada paso.** Acumula error. Redondea solo al final (regla del módulo).

✅ **Mini-checklist de exactitud**
1. ¿Las unidades viejas se cancelaron y quedó SOLO la unidad destino? (escribe la cadena con `cancel`).
2. ¿El roundtrip (ida y vuelta) devuelve el valor original exacto?
3. ¿El orden de magnitud del resultado tiene sentido (estimación rápida a mano)?

## Cruces
- [[04-notacion-unidades-y-dimensiones]] — fundamentos de unidades y análisis dimensional.
- [[05-cifras-significativas-y-redondeo]] — redondear una sola vez, al final.
- [[06-estimacion-y-sanity-checks]] — verificar el orden de magnitud del resultado.
- [[36-transformaciones-y-escalas]] — factores de escala (relacionado con cuadrados/cubos).
- [[79-moneda-inflacion-y-devaluacion]] — conversión entre monedas con Decimal.
