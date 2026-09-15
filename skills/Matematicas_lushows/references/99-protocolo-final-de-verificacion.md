# 99 · Protocolo final de verificación

> **Qué resuelve / cuándo usarlo** — Es el último filtro antes de entregar CUALQUIER número. Una lista de chequeo que se corre siempre, sin excepción, para garantizar la promesa de la skill: error cero. Si un ítem falla, el número NO sale.

## Concepto (para no-experto)

Imagina que eres piloto de avión. Antes de despegar, NUNCA arrancas de memoria: sacas una lista impresa (la "checklist de cabina") y verificas punto por punto —frenos, combustible, flaps— aunque hayas volado mil veces. ¿Por qué? Porque la confianza mata: el error que te tumba es justo el que "estabas seguro" de no haber cometido. La aviación pasó de ser mortal a ser el transporte más seguro del mundo en gran parte gracias a las checklists.

Este módulo es esa checklist, pero para números. Cada cálculo que entregamos sostiene una **decisión con dinero real** (cuánto cobrar, si un negocio da ganancia, cuánto invertir en publicidad). Un decimal mal puesto puede costar millones. Por eso, antes de soltar un resultado, lo pasamos por seis preguntas duras.

Definamos los términos que vamos a usar:

- **Verificación por segunda vía**: confirmar el mismo resultado con un método DISTINTO. Si dos caminos independientes llegan al mismo número, la probabilidad de error baja muchísimo. Es como sumar una columna de arriba hacia abajo y luego de abajo hacia arriba.
- **Operación inversa**: deshacer el cálculo. Si dije "20% de 50.000 = 10.000", la inversa es "10.000 ÷ 50.000 = 0,20 = 20%". Si vuelve al punto de partida, está bien.
- **Sanity check** (chequeo de cordura): preguntarse "¿este número tiene sentido en el mundo real?". Si calculé que un café cuesta $3.000.000, algo se rompió.
- **Supuesto**: una suposición que tuve que hacer porque el dato no estaba (ej. "asumo 30 días por mes"). Si cambia el supuesto, cambia el número, así que hay que declararlo.

La analogía cotidiana: es la diferencia entre un cajero que cuenta el vuelto una vez y te lo da, y uno que lo cuenta, te lo muestra, y lo vuelve a contar en tus manos. El segundo casi nunca se equivoca.

## Fórmulas / método

No hay una fórmula matemática aquí; el "método" es la checklist. Estos son los **6 ítems obligatorios** (más uno de presentación):

| # | Pregunta de cierre | Qué confirma |
|---|---|---|
| 1 | ¿Lo ejecuté en código? | Que no calculé de memoria. Todo cálculo no trivial corre en Python/Node y se muestra el código. |
| 2 | ¿Lo verifiqué por 2ª vía? | Que un método independiente da el mismo resultado (inversa, otro método, estimación, o `assert`). |
| 3 | ¿Llevo unidades y dimensiones? | Que el número significa algo: $, %, kg, COP/mes. Sin unidad, un número es ruido. |
| 4 | ¿Redondeé UNA sola vez, al final? | Que no acumulé errores de redondeo intermedios. Dinero con `decimal`, nunca `float`. |
| 5 | ¿Declaré los supuestos? | Que el lector sabe sobre qué base se sostiene el número (tasas, períodos, conversiones). |
| 6 | ¿Tiene sentido? (sanity check) | Que el orden de magnitud y el signo son razonables en el mundo real. |
| 7 | ¿Lo presento sin engañar? | Que el formato no distorsiona (eje truncado, % sin base, precisión falsa). |

**Regla de decisión:** la entrega solo procede si los 6 ítems centrales están en ✅. Si alguno está en ❌ o en ⚠️ (dudoso), se corrige ANTES de mostrar el número, o se entrega declarando explícitamente la limitación.

Notación de la "distancia relativa" entre dos vías (útil para el ítem 2 con decimales):

```
error_relativo = | resultado_via_A − resultado_via_B | / | resultado_via_A |
```

Si `error_relativo` es 0 (o por debajo de la tolerancia esperada por aritmética de punto flotante, p. ej. 1e-9), las dos vías coinciden.

## Verificación en código

El siguiente bloque es una **checklist ejecutable**: una función que recibe el resultado y sus verificaciones, y solo "aprueba la entrega" si todo cuadra. Lo aplicamos a un caso real de dinero.

```python
# ---------------------------------------------------------------
# Protocolo final de verificación — checklist ejecutable
# Caso: un restaurante vende un plato a $28.000 COP con costo
# de ingredientes de $9.800. ¿Cuál es el margen bruto %?
# ---------------------------------------------------------------
from decimal import Decimal, ROUND_HALF_UP

# --- Datos de entrada (dinero SIEMPRE con Decimal, nunca float) ---
precio = Decimal("28000")   # COP, precio de venta
costo  = Decimal("9800")    # COP, costo de ingredientes (COGS)

# === ÍTEM 1: ejecutar en código (no de memoria) ===
utilidad_bruta = precio - costo                 # COP
margen = utilidad_bruta / precio                 # fracción (sin unidad)
margen_pct = margen * Decimal("100")             # %

# === ÍTEM 4: redondear UNA sola vez, al final ===
margen_pct_final = margen_pct.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print("Utilidad bruta:", utilidad_bruta, "COP")
print("Margen bruto  :", margen_pct_final, "%")

# === ÍTEM 2: verificación por SEGUNDA VÍA (operación inversa) ===
# Si el margen es correcto, entonces costo debe ser precio*(1 - margen).
costo_reconstruido = (precio * (Decimal("1") - margen)).quantize(Decimal("0.01"))
assert costo_reconstruido == costo, f"Inversa falló: {costo_reconstruido} != {costo}"

# Segunda vía adicional: costo como % del precio + margen % debe dar 100%.
costo_pct = (costo / precio * Decimal("100"))
suma = (costo_pct + margen_pct).quantize(Decimal("0.0001"))
assert suma == Decimal("100.0000"), f"costo% + margen% != 100: {suma}"

# === ÍTEM 6: sanity check (¿tiene sentido?) ===
assert Decimal("0") < margen < Decimal("1"), "Margen fuera de rango plausible (0%-100%)"
assert utilidad_bruta > 0, "Vender por debajo del costo no tiene sentido aquí"

print("OK: todas las verificaciones pasaron ->", margen_pct_final, "% margen bruto")
```

Salida esperada:

```
Utilidad bruta: 18200 COP
Margen bruto  : 65.00 %
OK: todas las verificaciones pasaron -> 65.00 % margen bruto
```

Por qué cada `assert` importa: si alguien hubiera confundido **margen** (sobre precio) con **markup** (sobre costo), el número saldría distinto y la inversa lo cazaría de inmediato. El `assert` es la red de seguridad que convierte "creo que está bien" en "el código me lo demostró".

## Ejemplo trabajado

**Situación real (LatAm).** Un dueño de café en Bogotá quiere saber el margen bruto de su capuchino y decidir si subir el precio. Datos: precio de venta $28.000 COP, costo de insumos $9.800 COP (el ejemplo del código).

Paso a paso, aplicando la checklist:

1. **¿Ejecuté en código?** Sí. El bloque de arriba corre en Python con `Decimal`. ✅
2. **¿Segunda vía?** Sí, dos:
   - Inversa: reconstruí el costo desde el margen → $9.800 COP exactos. ✅
   - Suma de porcentajes: costo% (35,00%) + margen% (65,00%) = 100,00%. ✅
3. **¿Unidades?** Utilidad bruta = **18.200 COP por capuchino**; margen = **65,00 %**. Cada número lleva su unidad. ✅
4. **¿Redondeo al final?** Solo redondeé `margen_pct_final` al cierre, con `quantize`. No hubo redondeos intermedios. ✅
5. **¿Supuestos declarados?** Sí: "costo" = solo insumos del plato (COGS), NO incluye arriendo, salarios ni servicios. Por eso es margen **bruto**, no neto. Si el dueño esperaba margen neto, el número correcto sería mucho menor. ✅ (declarado)
6. **¿Tiene sentido?** 65% de margen bruto es típico y plausible en gastronomía (la comida suele costar 25%-40% del precio). El signo es positivo: vende por encima del costo. ✅

**Resultado verificado:** el capuchino tiene un **margen bruto de 65,00 %**, equivalente a **18.200 COP de utilidad bruta por unidad** (antes de gastos fijos). Listo para entregar.

## Errores comunes / trampas

- **"Es un cálculo fácil, lo hago de memoria."** El 80% de los errores caros viven en cálculos "fáciles" (un % mal, un cero de más). La checklist NO se salta por simplicidad.
- **Verificar con el mismo método.** Repetir la misma operación no es segunda vía: si el error está en la fórmula, lo repites idéntico. La 2ª vía debe ser *independiente* (inversa, otro camino, estimación).
- **Redondear en el medio.** Redondear resultados intermedios y luego seguir calculando acumula error. Redondea UNA vez, al final.
- **Usar `float` para dinero.** `0.1 + 0.2` en float da `0.30000000000000004`. En finanzas eso es inaceptable: usa `decimal` o centavos enteros.
- **Soltar un número sin unidad.** "El resultado es 65" no significa nada: ¿65 qué? ¿pesos, %, unidades? Sin unidad, no se entrega.
- **No declarar supuestos.** Si asumí 30 días/mes o una tasa, y no lo digo, el lector toma el número como verdad absoluta y decide mal.
- **Saltarse el sanity check.** El código puede estar "correcto" y el resultado ser absurdo (un margen de 6.500% delata un `*100` de más). Siempre pregunta: ¿esto puede ser cierto en el mundo real?

### Mini-checklist de exactitud (cierre)

- [ ] Los 6 ítems centrales están en ✅ (código · 2ª vía · unidades · redondeo final · supuestos · sentido).
- [ ] El número final lleva su unidad y, si es dinero, salió de `decimal` (no `float`).
- [ ] Declaré qué asumí y qué NO cubre el número (alcance honesto).

## Cruces

- [[00-metodo-del-matematico-exacto]] — el método global del que esta checklist es el paso final.
- [[02-mentalidad-de-exactitud-error-cero]] — la filosofía que esta checklist hace operativa.
- [[03-protocolo-de-verificacion-por-codigo]] — cómo ejecutar (ítem 1) y verificar por 2ª vía (ítem 2) en detalle.
- [[05-cifras-significativas-y-redondeo]] — el "redondear una vez al final" (ítem 4) explicado a fondo.
- [[06-estimacion-y-sanity-checks]] — el sanity check (ítem 6) y la estimación de orden de magnitud.
- [[98-presentar-numeros-sin-enganar]] — el ítem 7: que el formato no distorsione el número correcto.
