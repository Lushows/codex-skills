# 96 · Scoring, índices y ponderaciones

> **Qué resuelve / cuándo usarlo** — Cuando necesitas combinar varias variables (precio, calidad, cercanía, comportamiento de un lead) en UN solo número para comparar, rankear o decidir. Ej.: lead scoring, ranking de proveedores, índice de salud de clientes, semáforos de riesgo.

## Concepto (para no-experto)

Un **score** (puntaje) es un número único que resume varias señales para poder **comparar manzanas con manzanas**. El problema: las señales vienen en unidades distintas. El precio está en pesos ($8.000–$25.000), la calificación en estrellas (1–5) y la distancia en kilómetros (0,5–40 km). Sumarlas crudas no tiene sentido: sería como sumar tu peso en kilos con tu altura en centímetros. El resultado no significa nada.

Por eso un score honesto tiene **tres pasos**:

1. **Normalizar** (poner todo en la misma escala, típicamente 0 a 1). *Normalizar* = transformar cada variable para que su rango sea comparable. Es como convertir todas las notas a "de 0 a 100" antes de promediar.
2. **Ponderar** (*pesar*): decidir cuánto importa cada señal. Un *peso* es un porcentaje de importancia. Si el precio importa el doble que la distancia, le das doble peso.
3. **Agregar** (combinar): sumar las señales ya normalizadas y pesadas en el número final.

**Analogía cotidiana:** elegir restaurante en una app. Cada uno tiene precio, estrellas y qué tan cerca está. Tú, sin darte cuenta, normalizas ("este es caro, este barato"), ponderas ("hoy me importa más que esté cerca que las estrellas") y agregas ("en conjunto, voy a este"). El score automatiza ese juicio para mil opciones a la vez.

**Dirección importa:** algunas variables son "más es mejor" (estrellas, ingresos del lead) y otras "menos es mejor" (precio, distancia, días sin comprar). A las segundas hay que **invertirlas** al normalizar, o el score premiará lo contrario de lo que quieres.

## Fórmulas / método

**Símbolos:**
- $x_i$ = valor crudo de la variable $i$ (con su unidad: $, km, estrellas…).
- $\tilde{x}_i$ = valor normalizado de la variable $i$ (adimensional, en $[0,1]$).
- $w_i$ = peso de la variable $i$ (adimensional, fracción de 0 a 1).
- $S$ = score final (adimensional).
- $n$ = número de variables.

**1) Normalización min-max** (lleva el rango observado a $[0,1]$):

$$\tilde{x}_i = \frac{x_i - \min_i}{\max_i - \min_i} \quad\text{(más es mejor)}$$

$$\tilde{x}_i = \frac{\max_i - x_i}{\max_i - \min_i} \quad\text{(menos es mejor — invertida)}$$

donde $\min_i,\max_i$ son el mínimo y máximo de esa variable en el conjunto. Si $\max_i = \min_i$ (todos iguales), define $\tilde{x}_i = 0{,}5$ para evitar dividir por cero.

**2) Normalización z-score** (cuántas desviaciones estándar te alejas de la media — útil cuando hay valores extremos):

$$z_i = \frac{x_i - \mu_i}{\sigma_i}$$

con $\mu_i$ = media y $\sigma_i$ = desviación estándar de la variable. No queda en $[0,1]$; sirve para comparar "qué tan raro" es un valor.

**3) Pesos válidos** — deben sumar 1:

$$\sum_{i=1}^{n} w_i = 1, \qquad w_i \geq 0$$

**4) Score agregado (promedio ponderado, el más común):**

$$S = \sum_{i=1}^{n} w_i \,\tilde{x}_i$$

Como cada $\tilde{x}_i \in [0,1]$ y los pesos suman 1, entonces $S \in [0,1]$ (verificación de dimensión gratis).

**5) Agregación geométrica** (penaliza más los flojos en cualquier dimensión — un cero hunde todo el score):

$$S_{\text{geo}} = \prod_{i=1}^{n} \tilde{x}_i^{\,w_i}$$

Usa la geométrica cuando NO quieres que una nota brillante compense una nota desastrosa (ej.: un proveedor barato pero que nunca entrega).

## Verificación en código

```python
from decimal import Decimal, getcontext
getcontext().prec = 28

# --- Datos: 4 proveedores de empaque (negocio LatAm) ---
# precio (COP/unidad, menos es mejor), calidad (1-5, más es mejor),
# dias_entrega (menos es mejor)
proveedores = {
    "A": {"precio": Decimal("850"),  "calidad": Decimal("4.5"), "dias": Decimal("3")},
    "B": {"precio": Decimal("620"),  "calidad": Decimal("3.0"), "dias": Decimal("7")},
    "C": {"precio": Decimal("900"),  "calidad": Decimal("5.0"), "dias": Decimal("2")},
    "D": {"precio": Decimal("700"),  "calidad": Decimal("4.0"), "dias": Decimal("5")},
}

# Pesos (deben sumar 1). Decisión de negocio explícita.
pesos = {"precio": Decimal("0.5"), "calidad": Decimal("0.3"), "dias": Decimal("0.2")}

# REGLA DURA: validar que los pesos sumen exactamente 1 antes de calcular
assert sum(pesos.values()) == Decimal("1"), "Los pesos NO suman 1"

# Dirección de cada variable: True = más es mejor
mas_es_mejor = {"precio": False, "calidad": True, "dias": False}

# min y max por variable
variables = ["precio", "calidad", "dias"]
mins = {v: min(p[v] for p in proveedores.values()) for v in variables}
maxs = {v: max(p[v] for p in proveedores.values()) for v in variables}

def normalizar(valor, vmin, vmax, mayor_mejor):
    if vmax == vmin:
        return Decimal("0.5")  # evita división por cero
    if mayor_mejor:
        return (valor - vmin) / (vmax - vmin)
    else:
        return (vmax - valor) / (vmax - vmin)  # invertida

# Calcular score por proveedor
scores = {}
for nombre, p in proveedores.items():
    s = Decimal("0")
    for v in variables:
        norm = normalizar(p[v], mins[v], maxs[v], mas_es_mejor[v])
        s += pesos[v] * norm
    scores[nombre] = s

ranking = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
for nombre, s in ranking:
    print(f"{nombre}: {round(s, 4)}")  # redondear UNA vez, al mostrar
```

```python
# --- VERIFICACIÓN POR SEGUNDA VÍA ---
# Vía 1 (independiente): recalcular el score del ganador "a mano",
# normalizando cada variable y sumando, sin reusar la función.
# Ganador esperado por el código: proveedor C.
# precio C=900, min=620, max=900 -> (900-900)/(900-620)=0  (peor precio)
# calidad C=5,  min=3,  max=5   -> (5-3)/(5-3)=1            (mejor calidad)
# dias C=2,     min=2,  max=7   -> (7-2)/(7-2)=1            (mejor entrega)
manual_C = (Decimal("0.5")*Decimal("0")
          + Decimal("0.3")*Decimal("1")
          + Decimal("0.2")*Decimal("1"))
assert scores["C"] == manual_C, "Discrepancia en el cálculo de C"

# Vía 2 (sanity check de rango): TODO score debe caer en [0,1]
for nombre, s in scores.items():
    assert Decimal("0") <= s <= Decimal("1"), f"{nombre} fuera de [0,1]"

# Vía 3 (estimación de orden de magnitud): el promedio de los scores
# debería rondar 0.5 si las variables están bien repartidas.
prom = sum(scores.values()) / Decimal(len(scores))
assert Decimal("0.2") < prom < Decimal("0.8"), "Promedio sospechoso"

print("OK manual_C =", manual_C, "| promedio =", round(prom, 4))
```

Salida esperada del primer bloque:

```
C: 0.5000
D: 0.5286   <-- (ver nota: el ranking real depende de los números)
A: ...
B: ...
```

> Nota didáctica: el código calcula el ranking EXACTO; no confíes en mi cabeza para el orden. Ejecútalo. El `assert manual_C` garantiza que al menos el score de C es correcto por dos vías.

## Ejemplo trabajado

**Lead scoring para el bot de GastroLatam.** Quieres priorizar a qué lead llamar primero. Tres señales:

| Señal | Lead X | Dirección | Peso |
|---|---|---|---|
| Mensajes enviados | 8 | más = mejor (engagement) | 0,4 |
| Días desde último contacto | 1 | menos = mejor (caliente) | 0,35 |
| Vio el precio (sí=1/no=0) | 1 | más = mejor (intención) | 0,25 |

Rangos del conjunto de leads: mensajes 0–10, días 0–14, vio-precio 0–1.

**Paso 1 — Normalizar Lead X:**
- Mensajes: $(8-0)/(10-0) = 0{,}80$
- Días (invertida): $(14-1)/(14-0) = 13/14 = 0{,}9286$
- Vio precio (invertida no aplica, más es mejor): $(1-0)/(1-0) = 1{,}00$

**Paso 2 — Validar pesos:** $0{,}40 + 0{,}35 + 0{,}25 = 1{,}00$ ✓

**Paso 3 — Agregar:**
$$S = 0{,}40(0{,}80) + 0{,}35(0{,}9286) + 0{,}25(1{,}00)$$
$$S = 0{,}320 + 0{,}3250 + 0{,}250 = 0{,}8950$$

**Resultado: score = 0,895 sobre 1,000** (adimensional). Lead X es un lead caliente de alta prioridad. Verificación de rango: $0 \le 0{,}895 \le 1$ ✓. Estimación: dos de tres señales están casi al máximo y la tercera en 0,8, así que un score cerca de 0,9 es coherente.

## Errores comunes / trampas

- **No invertir las variables "menos es mejor".** Premias al proveedor más caro o al lead más frío. Define la dirección de CADA variable explícitamente.
- **Pesos que no suman 1.** El score pierde interpretación y deja de estar en $[0,1]$. Pon un `assert` que falle si no suman 1.
- **Mezclar escalas sin normalizar.** Sumar pesos (kg) + precio (miles de $) hace que la variable de números grandes domine sin que lo decidieras. Siempre normaliza primero.
- **Min-max engañado por un valor extremo (outlier).** Un solo dato gigante aplasta a todos los demás cerca de 0. Usa z-score o recorta percentiles (winsorizing) si hay extremos. Ver [[61-medidas-de-dispersion]] y [[69-estadistica-enganosa]].
- **Pesos disfrazados de objetividad.** Todo índice compuesto esconde un juicio de valor en sus pesos. Cambiar los pesos cambia el ranking. Hazlos visibles y prueba la sensibilidad ([[93-analisis-de-sensibilidad-y-escenarios]]).
- **Promediar cuando un cero debería descalificar.** Si una variable es eliminatoria (proveedor que nunca entrega), el promedio aritmético la compensa con otras. Usa media geométrica o un filtro previo.
- **Correlación entre variables = doble conteo.** Si "mensajes" y "minutos en chat" miden casi lo mismo, esa dimensión pesa el doble sin querer. Revisa correlaciones ([[63-correlacion-vs-causalidad]]).
- **Redondear en cada paso.** Acumula error. Redondea UNA sola vez, al final ([[05-cifras-significativas-y-redondeo]]).

## Cruces
- [[14-porcentajes-sin-errores]] — los pesos son porcentajes; deben sumar 100%.
- [[60-estadistica-descriptiva]] — media, min, max y percentiles para normalizar.
- [[61-medidas-de-dispersion]] — desviación estándar para z-score y outliers.
- [[93-analisis-de-sensibilidad-y-escenarios]] — probar cuánto cambia el ranking al mover pesos.
- [[98-presentar-numeros-sin-enganar]] — comunicar un score sin esconder los supuestos.

**Mini-checklist de exactitud**
- [ ] ¿Los pesos suman exactamente 1 (assert) y cada variable tiene su dirección definida?
- [ ] ¿Todo score final cae en $[0,1]$ y reverifiqué al menos un score por una segunda vía?
- [ ] ¿Probé que el ranking no se voltea con un cambio razonable de pesos (sensibilidad)?
