# 00 · Método del matemático exacto

> **Qué resuelve / cuándo usarlo** — El protocolo central de TODA esta skill: cómo pasar de una pregunta numérica a una respuesta en la que se puede confiar para decidir con dinero real. Léelo primero; los demás módulos son aplicaciones de este método.

## Concepto (para no-experto)

Imagina que eres el ingeniero que calcula cuánto peso aguanta un puente. Si te equivocas por un 2 %, el puente se cae. En un negocio pasa lo mismo, pero el "puente" es una decisión: poner un precio, pedir un préstamo, lanzar una campaña de ads. **De cada cálculo cuelga una decisión, y de cada decisión cuelga dinero o tiempo real.** Por eso la promesa de esta skill es una sola: **error cero**.

"Error cero" no significa "soy un genio que nunca se equivoca". Significa lo contrario: **doy por hecho que me puedo equivocar, así que construyo un sistema que atrapa el error antes de que llegue a ti.** Un piloto experto no confía en su memoria: usa una *checklist* (lista de verificación) antes de despegar. Nosotros hacemos igual con los números.

Definamos los tres términos que vamos a usar todo el tiempo:

- **Cálculo trivial**: una operación que cualquiera verifica de un vistazo (2 + 2, el 10 % de 100). No necesita código.
- **Cálculo no trivial**: cualquier cosa con varios pasos, dinero, porcentajes encadenados, potencias, tasas, probabilidades o más de 3-4 dígitos. **Estos SIEMPRE van en código real**, nunca "de memoria".
- **Segunda vía** (o doble verificación): comprobar un resultado por un camino *distinto* al que lo produjo. Si dos caminos independientes dan lo mismo, la confianza sube muchísimo. Es como sumar una columna de números de arriba-abajo y luego de abajo-arriba: si coincide, casi seguro está bien.

La analogía cotidiana: cuando pagas en la tienda, el cajero teclea el total **y además** tú miras el vuelto y haces la resta mental. Dos vías. Eso es exactamente lo que hace un matemático profesional, solo que de forma sistemática y con herramientas que no mienten.

## Fórmulas / método

No hay una "fórmula" aquí; hay un **arco de 5 pasos** que se aplica a todo problema no trivial. Llámalo el método EFEVE (Entender, Fórmula, Ejecutar, Verificar, Entregar):

```
1. ENTENDER   ¿Qué se pregunta exactamente? ¿Qué dato es cada número y en qué UNIDAD está?
              Reescribe el problema en una frase. Si es ambiguo, pregunta antes de calcular.

2. FÓRMULA    Elige la fórmula/método correcto y escríbela con cada símbolo definido.
              Verifica que las UNIDADES cuadren (análisis dimensional) ANTES de meter números.

3. EJECUTAR   Corre el cálculo en CÓDIGO REAL (Python con decimal/fractions/sympy/numpy, o Node).
              Dinero -> Decimal o centavos enteros. NUNCA float para plata.

4. VERIFICAR  Confirma el resultado por una 2ª vía independiente:
              (a) operación inversa, (b) estimación de orden de magnitud,
              (c) otro método/fórmula, o (d) un assert que falle si está mal.

5. ENTREGAR   Redondea UNA sola vez al final. Reporta el número CON UNIDADES.
              Explica en lenguaje simple qué significa y declara la incertidumbre si la hay.
```

**Regla del dinero (dura, sin excepción):** los `float` (números decimales binarios del computador) no pueden representar exactamente valores como 0.10. `0.1 + 0.2` da `0.30000000000000004`. Por eso el dinero va con **`decimal.Decimal`** (aritmética decimal exacta) o como **centavos enteros**. El redondeo se hace UNA vez, al final, con una regla declarada (típicamente `ROUND_HALF_UP`: 0.5 sube).

**Cuándo aplicar más o menos rigor** (calibración, no pereza):

| Situación | Rigor |
|---|---|
| Suma trivial, sin dinero, sin decisión | Mental, pero declarando que es trivial |
| Cualquier cosa con dinero, % encadenados, tasas | Código + 2ª vía SIEMPRE |
| Va a un cliente, contrato, inversión, pauta | Código + 2ª vía + sanity check de magnitud |
| Otra skill ya entregó un número | Auditarlo: recalcular desde cero, no confiar |

## Verificación en código

Ejemplo de referencia que demuestra el patrón completo: **"¿Cuánto cobro si mi producto cuesta $7.000 y quiero 30 % de margen sobre el precio?"** (margen sobre venta, el error clásico es confundirlo con markup).

```python
from decimal import Decimal, ROUND_HALF_UP

# --- PASO 2: FÓRMULA ---
# "Margen sobre venta" = (precio - costo) / precio.  Despejando el precio:
#   precio = costo / (1 - margen)
# Símbolos:  costo [COP], margen [adimensional, 0..1], precio [COP]
costo  = Decimal("7000")     # COP  (dinero -> Decimal, NUNCA float)
margen = Decimal("0.30")     # 30 % expresado como fracción

# --- PASO 3: EJECUTAR ---
precio_exacto = costo / (Decimal("1") - margen)        # 7000 / 0.70 = 10000
precio = precio_exacto.quantize(Decimal("1"), rounding=ROUND_HALF_UP)  # redondeo ÚNICO al final
print("Precio de venta:", precio, "COP")               # -> 10000 COP

# --- PASO 4: VERIFICAR, 2ª VÍA (inversa): recomputar el margen desde el precio ---
margen_recomputado = (precio - costo) / precio          # (10000-7000)/10000 = 0.30
assert margen_recomputado == Decimal("0.30"), f"Margen real {margen_recomputado} != 0.30"
print("Verificación inversa OK -> margen real:", margen_recomputado)   # -> 0.30

# --- PASO 4 (b): VERIFICAR por OTRO método (markup) para no confundir conceptos ---
# Markup = ganancia / costo.  No es lo mismo que margen.
markup = (precio - costo) / costo                        # 3000/7000 = 0.428571...
print("Markup equivalente:", round(float(markup)*100, 1), "%")  # 42.9 % (NO 30 %)
```

Salida esperada:

```
Precio de venta: 10000 COP
Verificación inversa OK -> margen real: 0.30
Markup equivalente: 42.9 %
```

La segunda vía (recomputar el margen desde el precio con el `assert`) garantiza que no nos equivocamos al despejar. El bloque de markup demuestra el sanity check conceptual: un margen del 30 % NO es un markup del 30 %.

## Ejemplo trabajado

**Problema (negocio LatAm):** Una cafetería vende 320 almuerzos al mes a $18.000 cada uno. El costo variable por almuerzo es $11.500 y los costos fijos mensuales son $1.900.000. ¿Cuál es la utilidad mensual?

Paso 1 — **Entender**: piden la utilidad (ingresos − costos totales) del mes. Unidades: todo en COP/mes.

Paso 2 — **Fórmula**:
- Ingresos = precio × cantidad
- Costo variable total = costo variable unitario × cantidad
- Utilidad = Ingresos − Costo variable total − Costos fijos

Paso 3 — **Ejecutar** (Decimal, porque es dinero):

```python
from decimal import Decimal
precio   = Decimal("18000"); cant = Decimal("320")
cv_unit  = Decimal("11500"); fijos = Decimal("1900000")

ingresos = precio * cant            # 5_760_000
cv_total = cv_unit * cant           # 3_680_000
utilidad = ingresos - cv_total - fijos
print(ingresos, cv_total, utilidad) # 5760000 3680000 180000
```

Paso 4 — **Verificar, 2ª vía (margen de contribución)**: contribución por almuerzo = 18.000 − 11.500 = **6.500 COP**. Total contribución = 6.500 × 320 = 2.080.000. Utilidad = 2.080.000 − 1.900.000 = **180.000 COP**.

```python
contrib = (precio - cv_unit) * cant - fijos
assert contrib == utilidad   # 180000 == 180000  -> ambas vías coinciden
```

Sanity check de magnitud: vende ~5,76 millones, gasta ~5,58 millones; que sobren ~180 mil es del orden esperado (margen flaco, típico de cafetería). No salió un número absurdo.

**Resultado: utilidad ≈ 180.000 COP/mes** (verificado por dos vías). Lectura para no-experto: el negocio gana plata, pero apenas; un mes con 30 almuerzos menos lo deja casi en cero. Conviene mirar [[76-punto-de-equilibrio]].

## Errores comunes / trampas

- **Calcular "de cabeza" algo no trivial.** El cerebro estima, no calcula exacto. Si tiene dinero o varios pasos, va en código. Sin excepciones.
- **Usar `float` para dinero.** `0.1 + 0.2 != 0.3` en el computador. Usa `Decimal` o centavos enteros.
- **Redondear en pasos intermedios.** Cada redondeo mete error; encadenados se acumulan. Redondea **una sola vez, al final**.
- **No declarar unidades.** "El resultado es 180.000" no sirve: ¿COP? ¿USD? ¿por mes o por año? Sin unidad, el número es peligroso.
- **Confundir margen con markup**, o porcentaje "de" con "más"/"menos" (ver [[14-porcentajes-sin-errores]]).
- **Verificar con la misma vía.** Repetir el mismo cálculo no es verificar: si el método estaba mal, repite el error. La 2ª vía debe ser *independiente*.
- **Confiar en números que llegan de otra fuente o skill** sin recalcularlos. Auditar = recalcular desde los datos crudos.

---

**Mini-checklist de exactitud:**
1. ¿El cálculo no trivial se ejecutó en código real (Decimal para dinero) y mostré el código?
2. ¿Lo confirmé por una **segunda vía independiente** (inversa / estimación / otro método / assert)?
3. ¿El resultado lleva **unidades**, se redondeó **una sola vez** y lo expliqué en lenguaje simple?

## Cruces
- [[02-mentalidad-de-exactitud-error-cero]] — la filosofía detrás de este método.
- [[03-protocolo-de-verificacion-por-codigo]] — cómo montar la ejecución + 2ª vía en detalle.
- [[06-estimacion-y-sanity-checks]] — la verificación por orden de magnitud, paso 4(b).
- [[05-cifras-significativas-y-redondeo]] — la regla de redondear una sola vez al final.
- [[99-protocolo-final-de-verificacion]] — la checklist de cierre antes de entregar cualquier número.
