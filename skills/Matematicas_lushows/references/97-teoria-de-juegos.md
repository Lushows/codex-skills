# 97 · Teoría de juegos

> **Qué resuelve / cuándo usarlo** — Decidir cuando tu resultado depende de lo que haga OTRO que también decide (competidor, cliente, socio): guerras de precios, descuentos, entrar o no a un mercado. Sirve para anticipar la jugada del rival y elegir la tuya con cabeza fría, no por corazonada.

## Concepto (para no-experto)

La **teoría de juegos** es la matemática de las decisiones estratégicas: situaciones donde tu beneficio no depende solo de lo que TÚ haces, sino también de lo que hace otra persona que está decidiendo al mismo tiempo. Si bajas el precio pero tu competidor también lo baja, los dos terminan ganando menos. Ese "depende de los dos" es el corazón del tema.

Definamos los términos la primera vez que aparecen:

- **Jugador**: cada uno de los que decide. En negocios suele ser "tú" y "tu competidor". (También: dos clientes, dos socios, etc.)
- **Estrategia**: una opción completa que un jugador puede elegir. Ej.: "precio alto" o "precio bajo".
- **Pago** (*payoff*): el resultado numérico que recibe un jugador según la combinación de estrategias elegidas. En negocios casi siempre es **dinero** (utilidad), por eso lo tratamos con `decimal`, nunca con `float`.
- **Matriz de pagos**: una tabla que cruza las estrategias de los dos jugadores y muestra, en cada celda, los dos pagos `(pago_jugador_fila, pago_jugador_columna)`.
- **Equilibrio de Nash** (por John Nash): una combinación de estrategias donde **nadie gana cambiando su jugada por sí solo**, suponiendo que el otro no cambia. Es un "punto de descanso": ninguno tiene incentivo a moverse unilateralmente. Puede haber cero, uno o varios.
- **Estrategia dominante**: una jugada que te conviene SIEMPRE, sin importar qué haga el otro.

**Analogía cotidiana — el dilema del prisionero.** Dos socios de un delito son interrogados en cuartos separados. Si ambos callan, poca condena para los dos. Si uno delata y el otro calla, el delator sale libre y el otro paga caro. Si ambos delatan, condena media para los dos. Cada uno, pensando solo en sí mismo, delata (es dominante)... y terminan peor que si ambos callaran. Eso es exactamente una guerra de precios: a cada empresa le "conviene" bajar el precio, pero si ambas lo hacen, las dos pierden margen. El equilibrio individualmente racional es colectivamente malo.

## Fórmulas / método

Juego de 2 jugadores con estrategias finitas. Jugador 1 elige fila *i*, jugador 2 elige columna *j*. Pagos: A[i][j] para el jugador 1, B[i][j] para el jugador 2.

- **Estrategia estrictamente dominante** para el jugador 1: una fila *i\** tal que `A[i*][j] > A[k][j]` para toda otra fila *k* y toda columna *j*. (Le gana a cualquier otra opción suya, pase lo que pase el rival.)

- **Equilibrio de Nash en estrategias puras**: un par (i\*, j\*) tal que, simultáneamente:

  ```
  A[i*][j*] >= A[i][j*]   para toda fila i      (el jugador 1 no mejora cambiando solo)
  B[i*][j*] >= B[i*][j]   para toda columna j   (el jugador 2 no mejora cambiando solo)
  ```

- **Pago esperado con estrategias mixtas** (cuando el jugador aleatoriza). Si el jugador 1 juega la fila *i* con probabilidad pᵢ (con Σpᵢ = 1, cada pᵢ ≥ 0) y el jugador 2 la columna *j* con qⱼ:

  ```
  E[pago_1] = Σ_i Σ_j  p_i · q_j · A[i][j]
  ```

  Unidades: el pago va en **unidades monetarias** (ej. COP/mes) o en utilidad relativa; las probabilidades son adimensionales (entre 0 y 1).

**Teorema de Nash (1950):** todo juego finito tiene al menos un equilibrio de Nash, posiblemente en estrategias mixtas. Que exista no significa que sea "bueno" para todos (ver dilema del prisionero).

## Verificación en código

Buscamos equilibrios de Nash en estrategias puras por definición (revisando que ningún jugador mejore al desviarse), y lo verificamos por una **segunda vía**: detección de estrategias dominantes. Usamos `decimal` porque los pagos son dinero.

```python
from decimal import Decimal as D
from itertools import product

# Dilema del prisionero versión "guerra de precios" (utilidad mensual, millones COP).
# Estrategias: 0 = Precio ALTO (cooperar), 1 = Precio BAJO (competir/traicionar).
# Celda = (pago_empresa_fila, pago_empresa_columna).
A = [[D("10"), D("2")],    # fila 0 (yo ALTO):  rival ALTO -> 10 ; rival BAJO -> 2
     [D("12"), D("4")]]    # fila 1 (yo BAJO):  rival ALTO -> 12 ; rival BAJO -> 4
B = [[D("10"), D("12")],   # col 0 (rival ALTO) ; col 1 (rival BAJO), simetrico
     [D("2"),  D("4")]]

nf, nc = len(A), len(A[0])

def es_nash(i, j):
    # El jugador 1 (filas) no debe mejorar cambiando de fila, fijado j:
    mejor_fila = all(A[i][j] >= A[k][j] for k in range(nf))
    # El jugador 2 (columnas) no debe mejorar cambiando de columna, fijado i:
    mejor_col  = all(B[i][j] >= B[i][k] for k in range(nc))
    return mejor_fila and mejor_col

nash = [(i, j) for i, j in product(range(nf), range(nc)) if es_nash(i, j)]
print("Equilibrios de Nash (puros):", nash)          # esperado: [(1, 1)]
print("Pago en el equilibrio:", A[nash[0][0]][nash[0][1]], B[nash[0][0]][nash[0][1]])

# ---- VERIFICACION POR SEGUNDA VIA: estrategia estrictamente dominante ----
# La fila 1 (Precio BAJO) le gana a la fila 0 en TODAS las columnas?
dom_fila1 = all(A[1][j] > A[0][j] for j in range(nc))
# La columna 1 (Precio BAJO) le gana a la columna 0 en TODAS las filas?
dom_col1  = all(B[i][1] > B[i][0] for i in range(nf))
print("Fila 'BAJO' dominante:", dom_fila1, "| Columna 'BAJO' dominante:", dom_col1)

# Si ambos tienen dominante BAJO, el unico Nash debe ser (1,1).
assert dom_fila1 and dom_col1
assert nash == [(1, 1)], "El equilibrio por dominancia debe coincidir con la busqueda directa"

# Tercera comprobacion: (1,1) es PEOR para ambos que (0,0) -> es el dilema.
assert A[0][0] > A[1][1] and B[0][0] > B[1][1]
print("Confirmado: ambos prefieren (ALTO,ALTO)=10 pero caen en (BAJO,BAJO)=4. Dilema verificado.")
```

Salida esperada:

```
Equilibrios de Nash (puros): [(1, 1)]
Pago en el equilibrio: 4 4
Fila 'BAJO' dominante: True | Columna 'BAJO' dominante: True
Confirmado: ambos prefieren (ALTO,ALTO)=10 pero caen en (BAJO,BAJO)=4. Dilema verificado.
```

Las dos vías coinciden: la búsqueda directa encuentra (BAJO, BAJO) y la dominancia lo confirma. El `assert` falla ruidosamente si algún día cambias los números y dejan de cuadrar.

## Ejemplo trabajado

**Situación (LatAm).** Dos restaurantes vecinos en Medellín venden un almuerzo casi idéntico. Cada uno decide el precio del menú: **$18.000 COP (alto)** o **$15.000 COP (bajo)**. La utilidad mensual estimada (millones de COP) según las cuatro combinaciones es la de la matriz de arriba.

Leemos la matriz fila por fila (yo = restaurante de la fila):

| Yo \ Rival | Rival ALTO ($18k) | Rival BAJO ($15k) |
|---|---|---|
| **Yo ALTO ($18k)** | (10, 10) | (2, 12) |
| **Yo BAJO ($15k)** | (12, 2) | (4, 4) |

Paso 1 — ¿tengo estrategia dominante? Si el rival va ALTO: BAJO me da 12 > 10 (ALTO). Si el rival va BAJO: BAJO me da 4 > 2 (ALTO). Conclusión: **BAJO me conviene siempre** → es dominante.

Paso 2 — por simetría, al rival también le conviene BAJO siempre.

Paso 3 — equilibrio de Nash: ambos en BAJO → celda **(BAJO, BAJO) = (4, 4)**, en millones COP/mes. Ninguno gana desviándose solo (si yo subo a ALTO mientras él sigue BAJO, caigo de 4 a 2).

Paso 4 — la trampa: si los dos hubieran mantenido precio ALTO, cada uno ganaría **10 millones COP/mes** en vez de 4. Bajar el precio para "robar" clientes deja a ambos con **6 millones COP/mes menos** cada uno.

**Resultado verificado (código arriba):** único equilibrio puro en (BAJO, BAJO) con pago **4 millones COP/mes** por restaurante; el óptimo cooperativo no alcanzado vale **10 millones COP/mes** cada uno. Lección de negocio: competir solo por precio en un dilema del prisionero destruye margen; diferénciate (calidad, marca, experiencia) para salir del juego en vez de ganarlo.

## Errores comunes / trampas

- **Confundir Nash con "lo mejor para todos".** El equilibrio es estable, no necesariamente eficiente. En el dilema, el Nash es el peor resultado conjunto razonable.
- **Olvidar que el juego se repite.** En la vida real compites mes tras mes; los juegos **repetidos** permiten cooperación (precios altos sostenidos) vía castigo futuro. Un solo cuadro estático puede engañarte.
- **Inventar los pagos.** El análisis vale lo que valen los números de la matriz. Estima utilidades con datos reales (ver costeo y márgenes) y haz análisis de sensibilidad.
- **Asumir que el rival es perfectamente racional.** Puede tener otra función de pago (ego, flujo de caja, presión del dueño). Modela su pago, no el tuyo proyectado en él.
- **Usar `float` para el dinero.** `0.1 + 0.2 != 0.3` en float; usa `decimal` para que los `>=` de las comparaciones de Nash no fallen por basura de redondeo.
- **Acuerdos de precios = colusión ilegal.** "Cooperar en precio alto" suena lindo en la matriz, pero pactarlo con un competidor es ilegal (libre competencia). La salida legal es **diferenciarte**, no coludir.

## Cruces

- [[90-teoria-de-decisiones]] — decisiones cuando el "otro" es el azar, no un rival; base conceptual.
- [[82-pricing-markup-margin-y-elasticidad]] — los pagos de las guerras de precios salen de aquí.
- [[57-valor-esperado-y-varianza]] — calcular el pago esperado en estrategias mixtas.
- [[58-simulacion-monte-carlo]] — simular juegos repetidos y respuestas del rival.
- [[93-analisis-de-sensibilidad-y-escenarios]] — qué pasa con el equilibrio si los pagos cambian.

**Mini-checklist de exactitud**
- [ ] Pagos en `decimal` con **unidades** explícitas (ej. millones COP/mes) y fuente real, no inventada.
- [ ] Equilibrio confirmado por dos vías (búsqueda directa de Nash + dominancia/desviación), con `assert`.
- [ ] Revisado si el juego es **único o repetido** antes de concluir; advertido el riesgo legal de coludir.
