# 89 · Trampas de métricas y dashboards

> **Qué resuelve / cuándo usarlo** — Cuando un panel (dashboard) o un reporte muestra un número y vas a tomar una decisión con dinero o esfuerzo basándote en él. Te enseña a preguntar "¿qué significa exactamente este número, y me está engañando?" antes de actuar.

## Concepto (para no-experto)

Un **dashboard** (panel) es una pantalla con números y gráficos que resumen tu negocio: ventas, visitas, seguidores, conversiones. El problema: **un número bonito no es lo mismo que un número verdadero o útil.** Muchos paneles muestran cifras que se sienten bien pero no sirven para decidir nada — o peor, te empujan a la decisión equivocada.

Definamos los términos clave la primera vez:

- **Métrica de vanidad (vanity metric):** número grande que sube fácil y hace sentir bien, pero no se conecta con dinero ni con una decisión. Ejemplo: "tenemos 50.000 seguidores". ¿Y cuánto venden esos seguidores? Si la respuesta es "no sé", es vanidad.
- **Métrica accionable:** número que, al cambiar, te dice claramente qué hacer distinto. Ejemplo: "el 60% de los carritos se abandonan en el paso de pago" → revisar la pasarela de pago.
- **Promedio (media aritmética):** sumas todos los valores y divides por cuántos hay. Sensible a valores extremos (outliers).
- **Mediana:** el valor del medio cuando ordenas los datos de menor a mayor. La mitad está por debajo, la mitad por encima. No le afectan los extremos.
- **Ratio (razón):** un número dividido por otro, ej. ventas ÷ visitas = tasa de conversión. Sin saber el **denominador** (el de abajo), el ratio miente.

**Analogía cotidiana:** imagina un bar donde "el cliente promedio gasta $200.000". Suena a clientela rica. Pero si 9 clientes gastaron $20.000 y uno (un cumpleaños) gastó $1.820.000, el promedio se dispara por ese único caso. El cliente *típico* (la mediana) gastó $20.000. Decidir el menú "para clientes de $200.000" sería un error caro. El promedio te engañó; la mediana te dijo la verdad.

## Fórmulas / método

Sea un conjunto de datos x₁, x₂, …, xₙ (n = cantidad de datos).

- **Media:** x̄ = (Σ xᵢ) / n
- **Mediana:** valor central de los datos ordenados. Si n es impar, el del medio; si n es par, el promedio de los dos centrales.
- **Tasa / ratio:** r = numerador / denominador — *siempre* declara qué es cada uno y sus unidades (ej. ventas [pedidos] / sesiones [visitas]).
- **Regla de oro de auditoría de un panel:** para cada número responde 4 preguntas:
  1. **Definición:** ¿qué cuenta exactamente? (¿"usuarios" = personas únicas o sesiones?)
  2. **Denominador:** ¿sobre qué base se calcula? ¿es el correcto?
  3. **Periodo:** ¿qué ventana de tiempo? ¿comparable con lo anterior?
  4. **Distribución:** ¿es un promedio que esconde extremos? ¿debería ser mediana o percentil?

- **Percentil p (Pₚ):** valor por debajo del cual cae el p% de los datos. P50 = mediana. Útil para latencia, gasto, tiempos: el **P90** (el 90% está por debajo) describe la "mala experiencia típica" mejor que el promedio.

Unidades: una tasa de conversión va en % (adimensional, pero declara base); un ticket promedio va en COP/pedido; latencia en ms.

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP
from statistics import median

getcontext().prec = 28

# --- Caso: gasto de 10 clientes en un bar (COP, centavos enteros via Decimal) ---
gastos = [Decimal(x) for x in
          [20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 1820000]]
n = len(gastos)

# Media (promedio): suma / n  -- exacta con Decimal, sin float
media = (sum(gastos) / Decimal(n)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# Mediana: valor central. n=10 (par) -> promedio de los dos del medio
ordenados = sorted(gastos)
medio_bajo = ordenados[n//2 - 1]   # posicion 5 (indice 4)
medio_alto = ordenados[n//2]       # posicion 6 (indice 5)
mediana = ((medio_bajo + medio_alto) / Decimal(2)).quantize(Decimal("0.01"))

print(f"Media   = {media} COP/cliente")   # 200000.00
print(f"Mediana = {mediana} COP/cliente") # 20000.00

# --- Ratio con denominador claro: tasa de conversion ---
pedidos = Decimal(48)
sesiones = Decimal(3200)
conv = (pedidos / sesiones * Decimal(100)).quantize(Decimal("0.01"))
print(f"Conversion = {conv}%  (= {pedidos} pedidos / {sesiones} sesiones)")  # 1.50%
```

```python
# --- VERIFICACION POR SEGUNDA VIA ---

# 1) Media por via inversa: media * n debe reconstruir la suma total
assert media * Decimal(n) == sum(gastos), "La media no reconstruye el total"

# 2) Mediana cruzada con libreria independiente (statistics.median sobre floats)
assert abs(float(mediana) - median([float(g) for g in gastos])) < 1e-6

# 3) Sanity check de orden de magnitud: 9 clientes de ~20k + 1 de ~1.8M
#    total ~ 2.0M, /10 ~ 200k -> la media DEBE ser ~200k, la mediana ~20k
assert Decimal("190000") < media < Decimal("210000")
assert mediana == Decimal("20000.00")

# 4) Conversion por inversa: conv% * sesiones / 100 debe dar los pedidos
assert (conv / Decimal(100) * sesiones).quantize(Decimal("1")) == pedidos

print("Todas las verificaciones OK")
```

La doble vía confirma: **media = 200.000 COP/cliente, mediana = 20.000 COP/cliente.** El mismo dato cuenta dos historias opuestas según la métrica elegida.

## Ejemplo trabajado

**Situación (GastroLatam):** el dashboard del bot de WhatsApp dice "Ticket promedio: $200.000". El dueño piensa subir el precio de la Calculadora porque "la gente gasta harto". ¿Decisión correcta?

Paso 1 — **Definición:** ¿"ticket promedio" sobre qué? Resulta ser el gasto por cliente en una promo cruzada con un restaurante asociado, no por la Calculadora ($10.000).

Paso 2 — **Distribución:** 10 transacciones; 9 de $20.000 y 1 de $1.820.000 (un evento corporativo).

Paso 3 — Calculamos ambas (código arriba):
- Media = **200.000,00 COP/cliente**
- Mediana = **20.000,00 COP/cliente**

Paso 4 — **Interpretación:** el cliente *típico* gasta $20.000, no $200.000. La media está inflada por **un solo outlier** (el evento corporativo). Subir precios "porque gastan $200.000" perdería a los 9 clientes reales.

Paso 5 — **Decisión correcta:** reportar mediana (o media recortada quitando el extremo), y tratar el evento corporativo como un segmento aparte. Con unidades: **mediana = 20.000 COP/cliente**, no 200.000.

Resultado verificado por la operación inversa (media × n = total) y por orden de magnitud. ✔

## Errores comunes / trampas

- **Reportar media cuando la distribución es asimétrica.** Gasto, ingresos, latencia, tiempo en página casi siempre tienen cola larga → usa **mediana o percentiles**.
- **Vanity metrics:** seguidores, impresiones, "vistas totales", descargas acumuladas. Suben solo con el tiempo y no se atan a dinero. Pregunta: "si este número se duplica mañana, ¿qué decido distinto?". Si nada → es vanidad.
- **Ratio sin denominador o con denominador cambiante:** "conversión 5%" sin decir sobre qué base; o comparar dos periodos donde el denominador cambió (tráfico pagado vs orgánico).
- **Totales acumulados vs. tasa actual:** "1.000 ventas históricas" oculta que este mes vendiste 3. Mira el *delta* del periodo, no solo el acumulado.
- **Promedio de promedios** (promediar tasas de conversión de varios días sin ponderar por tráfico): da un número falso. Suma numeradores y suma denominadores, luego divide.
- **Ejes de gráfico truncados** (que no empiezan en 0) que exageran subidas; cambiar la escala entre paneles.
- **Métrica sin periodo ni comparación:** un número solo no dice nada; necesita "vs periodo anterior" o "vs meta".
- **Doble conteo / unidades mezcladas:** sumar "usuarios" y "sesiones" como si fueran lo mismo.

## Cruces

- [[60-estadistica-descriptiva]] — media, mediana, moda y cuándo usar cada una.
- [[61-medidas-de-dispersion]] — por qué dos paneles con igual promedio pueden ser muy distintos.
- [[69-estadistica-enganosa]] — gráficos y resúmenes que mienten.
- [[88-embudos-y-tasas-de-conversion]] — ratios con denominador correcto a lo largo del funnel.
- [[98-presentar-numeros-sin-enganar]] — cómo mostrar tus propios números con honestidad.

---

**Mini-checklist de exactitud:**
1. ¿El número tiene definición clara, denominador correcto, periodo y comparación?
2. ¿Es un promedio sobre datos asimétricos? Entonces calcula también la **mediana/percentil**.
3. ¿Pasa la prueba accionable: si cambia, sé qué hacer? Si no → es vanidad, no lo pongo a decidir.
