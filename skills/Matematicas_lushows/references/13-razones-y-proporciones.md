# 13 · Razones y proporciones

> **Qué resuelve / cuándo usarlo** — Cuando dos cantidades se relacionan en una proporción fija y quieres encontrar una desconocida: escalar una receta, repartir utilidades entre socios, ajustar un presupuesto, convertir "tantos por tantos". Es la base de la regla de tres.

## Concepto (para no-experto)

Una **razón** (en inglés *ratio*) es la comparación entre dos cantidades por división. Si en una mezcla hay 3 partes de café por cada 1 de leche, la razón café:leche es **3:1**, que también se escribe como la fracción 3/1 = 3.

Una **proporción** es la afirmación de que **dos razones son iguales**: a/b = c/d. Se lee "a es a b como c es a d".

Dentro de una proporción a/b = c/d hay dos tipos de relación:

- **Directamente proporcional** (regla de tres directa): cuando una cantidad sube, la otra sube en la misma medida. *Si 2 kg de harina cuestan $8.000, 4 kg cuestan $16.000* — al doble de harina, el doble de precio. El cociente entre ambas (la **constante de proporcionalidad** k) se mantiene fijo: precio/kg = $4.000/kg siempre.
- **Inversamente proporcional** (regla de tres inversa): cuando una cantidad sube, la otra **baja** en la misma medida. *Si 4 cocineros tardan 6 horas en algo, 8 cocineros tardan 3 horas* — al doble de gente, la mitad de tiempo. Aquí lo que se mantiene fijo es el **producto**: cocineros × horas = 24 siempre.

Analogía cotidiana: la regla de tres directa es como una receta (más comensales = más ingredientes, en bloque). La inversa es como repartir una pizza fija entre amigos (más amigos = menos porción por cabeza; el total de pizza no cambia).

> **Término clave — "proporcional" no es "lineal cualquiera".** Proporcional directo significa que pasa por el cero: 0 kg cuestan $0. Si hay un costo fijo de envío de $2.000 *aunque compres 0 kg*, ya NO es proporcional puro y la regla de tres simple miente. Ver Errores comunes.

## Fórmulas / método

**Razón:** `r = a / b`  (a y b en las mismas unidades si es razón pura; o con unidades si es una tasa, ej. $/kg).

**Proporción directa** — incógnita `x`:

```
 a     c                      b · c
─── = ───      ⇒      x = ─────────
 b     x                      a
```

Equivale al **producto cruzado**: a·x = b·c (los productos en cruz de una proporción son iguales).

**Proporción inversa** — el producto se conserva:

```
a · b = c · x      ⇒      x = (a · b) / c
```

Ejemplo de lectura: a = obreros1, b = días1, c = obreros2, x = días2.

**Reparto proporcional** (repartir un total T en partes con pesos p₁, p₂, …, pₙ):

```
                pᵢ
parteᵢ = T · ─────────        con  S = p₁ + p₂ + … + pₙ
                 S
```

La suma de todas las partes debe dar exactamente T (esa es la verificación natural).

Símbolos y unidades: `T` = total a repartir (en $ u otra unidad), `pᵢ` = peso/cuota de cada parte (mismas unidades entre sí, ej. % de sociedad o aportes), `S` = suma de pesos. Cada `parteᵢ` queda en las unidades de `T`.

## Verificación en código

Patrón de la skill: ejecutar en código exacto + verificar por segunda vía. Para dinero usamos `Decimal`, nunca `float`.

```python
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

# ─── 1) Regla de tres DIRECTA ───────────────────────────────
# "2 kg de harina cuestan $8.000. ¿Cuánto cuestan 4.5 kg?"
a = Decimal("2")       # kg de referencia
b = Decimal("8000")    # $ que cuestan esos 2 kg
c = Decimal("4.5")     # kg que quiero cotizar
x = b * c / a          # producto cruzado
print("Directa  x =", x, "COP")          # 18000

# Verificación 2ª vía: la constante $/kg debe ser idéntica en ambos lados
k_ref = b / a
k_x   = x / c
assert k_ref == k_x, "la razón $/kg no se conserva"
print("  k = $/kg:", k_ref, "==", k_x, "OK")

# ─── 2) Regla de tres INVERSA ───────────────────────────────
# "4 cocineros tardan 6 h. ¿Cuánto tardan 8 cocineros?"
ob1, d1, ob2 = Fraction(4), Fraction(6), Fraction(8)
d2 = ob1 * d1 / ob2                       # producto se conserva
print("Inversa  d2 =", float(d2), "h")    # 3.0

# Verificación 2ª vía: trabajo total (cocineros·horas) constante
assert ob1 * d1 == ob2 * d2, "el producto no se conserva"
print("  trabajo:", ob1*d1, "==", ob2*d2, "OK")

# ─── 3) REPARTO proporcional de utilidades entre socios ─────
# Utilidad total $10.000.000; sociedad 55% / 23% / 22%
T = Decimal("10000000")
pesos = [Decimal("55"), Decimal("23"), Decimal("22")]
S = sum(pesos)
partes = [(T * p / S) for p in pesos]
# redondear UNA sola vez al final, al peso
partes_red = [v.quantize(Decimal("1"), rounding=ROUND_HALF_UP) for v in partes]
print("Reparto:", [str(v) for v in partes_red])

# Verificación 2ª vía: la suma de las partes debe ser EXACTA al total
suma = sum(partes_red)
print("  suma:", suma, "vs total:", T, "->", "OK" if suma == T else f"AJUSTE {T-suma}")
```

Salida esperada:
```
Directa  x = 18000.0 COP
  k = $/kg: 4000 == 4000 OK
Inversa  d2 = 3.0 h
  trabajo: 24 == 24 OK
Reparto: ['5500000', '2300000', '2200000']
  suma: 10000000 vs total: 10000000 -> OK
```

> El reparto con porcentajes exactos cuadra solo. Cuando los pesos NO dividen limpio (ej. 1/3, 1/3, 1/3 de $100), la suma redondeada puede quedar a 1 centavo del total: hay que asignar ese residuo a una parte (método del **mayor resto**) para que cuadre al centavo. Ver checklist.

## Ejemplo trabajado

**Escalar una receta y su costo.** La receta de pan rinde **20 panes** y usa **5 kg de harina**. Quieres producir **35 panes** para un pedido. La harina cuesta **$4.000/kg**. ¿Cuánta harina y cuánto costo?

1. **Relación directa** (más panes ⇒ más harina, pasa por cero): 20 panes / 5 kg = 35 panes / x.
2. Producto cruzado: x = (5 kg · 35 panes) / 20 panes = 175/20 kg = **8,75 kg de harina**.
3. Costo = 8,75 kg × $4.000/kg = **$35.000 COP**.
4. **Verificación 1 (constante):** harina por pan = 5/20 = 0,25 kg/pan, y 8,75/35 = 0,25 kg/pan. Idéntica → correcto.
5. **Verificación 2 (orden de magnitud):** 35 panes es ~1,75× los 20 originales; 5 kg × 1,75 = 8,75 kg. Coincide.

**Resultado: 8,75 kg de harina, costo $35.000 COP** (unidades presentes, doble verificación pasada).

## Errores comunes / trampas

- **Confundir directa con inversa.** Pregúntate: "si X sube, ¿Y sube o baja?". Sube→directa (producto cruzado). Baja→inversa (producto constante). Aplicar la fórmula equivocada da números absurdos; el sanity check de orden de magnitud lo delata.
- **Usar regla de tres cuando hay un término fijo.** Si hay costo fijo (envío, mínimo, cuota base), la relación no pasa por cero y NO es proporcional. Modela `y = k·x + fijo`, no regla de tres.
- **Invertir la posición de los datos.** En a/b = c/x, `a` y `c` deben ser de la misma naturaleza (ambos "panes"), y `b` y `x` de la misma (ambos "kg"). Mezclarlos invierte el resultado.
- **Redondear a mitad de camino.** Redondea solo el resultado final. Redondear la constante k antes de multiplicar arrastra error.
- **Reparto que no cuadra por centavos.** Sumar las partes redondeadas y no verificar contra el total; asignar el residuo con mayor resto.
- **Dinero en float.** `0.1 + 0.2 != 0.3`. Usa `Decimal` o centavos enteros — ver [[12-fracciones-decimales-y-precision]].

## Cruces

- [[14-porcentajes-sin-errores]] — un porcentaje es una razón con denominador 100; el reparto proporcional suele venir en %.
- [[12-fracciones-decimales-y-precision]] — toda razón es una fracción; precisión exacta del cálculo.
- [[37-conversion-de-unidades]] — convertir unidades es regla de tres con factores de conversión.
- [[36-transformaciones-y-escalas]] — escalar figuras/diseños usa proporciones (factor de escala).
- [[81-costeo-y-costo-unitario]] — escalar recetas y presupuestos para costear lotes.

---

**Mini-checklist de exactitud**
- [ ] ¿Identifiqué bien directa (producto cruzado) vs inversa (producto constante)?
- [ ] ¿La constante k o el producto se conserva en ambos lados (segunda vía)?
- [ ] En repartos: ¿la suma de las partes (redondeadas) es EXACTAMENTE el total?
