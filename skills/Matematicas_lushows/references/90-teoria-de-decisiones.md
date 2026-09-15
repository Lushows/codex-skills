# 90 · Teoría de decisiones

> **Qué resuelve / cuándo usarlo** — Cuando hay que elegir entre opciones bajo incertidumbre (lanzar/no lanzar un producto, pagar por una prueba, aceptar un riesgo) y necesitas una forma estructurada y numérica de decidir, no "a ojo".

## Concepto (para no-experto)

Tomar una decisión es elegir una **acción** sin saber con certeza qué va a pasar después. La teoría de decisiones es el método para hacerlo con números en vez de corazonadas.

Tres piezas:

- **Acción (o alternativa):** lo que tú decides hacer. Ej.: "lanzar la calculadora a $10.000" vs. "no lanzar".
- **Estado de la naturaleza:** lo que el mundo hace y tú NO controlas. Ej.: "el mercado responde bien" vs. "responde mal".
- **Resultado (payoff):** el dinero (o lo que te importe) que ganas o pierdes según la combinación acción × estado.

A cada estado le asignamos una **probabilidad** (qué tan creíble es que ocurra; un número entre 0 y 1 que suma 1 entre todos los estados posibles).

El **valor esperado (VE)** es el promedio de los resultados, ponderado por sus probabilidades. Analogía: si lanzo una moneda y gano $100 con cara y pierdo $40 con sello, "en promedio por lanzamiento" gano `0.5×100 + 0.5×(−40) = $30`. No ganaré $30 en ningún lanzamiento concreto, pero es lo que esperaría a la larga.

Un **árbol de decisión** es el dibujo de todo esto: cuadrados (□) = puntos donde TÚ decides; círculos (○) = puntos donde el azar decide. Se resuelve "de atrás hacia adelante" (*backward induction*): calculas el VE de cada nodo de azar y en cada nodo de decisión te quedas con la rama de mayor valor.

Dos refinamientos clave:
- **Valor de la información:** cuánto vale pagar por reducir la incertidumbre antes de decidir (una encuesta, un piloto, un test).
- **Utilidad vs. valor monetario:** $1 millón no "vale" el doble que $500 mil para quien está quebrado. La **utilidad** mide cuánto te importa el dinero, no cuántos pesos son. Por eso compramos seguros (aceptamos perder un poco seguro para evitar una pérdida grande poco probable).

## Fórmulas / método

**Valor esperado de una acción** `a` con estados `s` de probabilidad `p(s)` y resultado `V(a,s)`:

```
VE(a) = Σ_s  p(s) · V(a,s)              [unidad: COP]
con  Σ_s p(s) = 1   y   0 ≤ p(s) ≤ 1
```

**Regla de decisión (maximizar VE):** elige `a* = argmax_a VE(a)`.

**Valor esperado con información perfecta (VECIP):** lo que ganarías si supieras el estado ANTES de actuar (eliges la mejor acción para cada estado):

```
VECIP = Σ_s  p(s) · max_a V(a,s)
```

**Valor esperado de la información perfecta (VEIP)** = el máximo que pagarías por un oráculo que adivine el estado:

```
VEIP = VECIP − VE(a*)        ≥ 0 siempre
```

**Valor de información imperfecta (VEII):** una prueba real (no perfecta) da una señal. Se actualizan probabilidades con **Bayes** (ver [[52-teorema-de-bayes]]) y `VEII = VE(decidir con prueba) − VE(a*)`. Conviene pagar la prueba si `VEII > costo de la prueba`.

**Utilidad esperada (cuando importa el riesgo):** se aplica una función `u(·)` cóncava al dinero (aversión al riesgo). Ejemplo común, utilidad exponencial:

```
u(x) = 1 − e^(−x/R)        (R = tolerancia al riesgo, en COP)
UE(a) = Σ_s p(s) · u(V(a,s))
```

Símbolos: `Σ`=suma; `argmax`=el argumento que maximiza; `e`=número de Euler; `R`=cuánto riesgo aguantas (mayor R = más neutral al riesgo).

## Verificación en código

```python
from decimal import Decimal as D, getcontext
getcontext().prec = 30  # dinero: usamos Decimal, NUNCA float

# --- Caso: ¿lanzar la Calculadora de Costos o no? ---
# Estados de la naturaleza y sus probabilidades (deben sumar 1)
prob = {"alta": D("0.30"), "media": D("0.50"), "baja": D("0.20")}
assert sum(prob.values()) == D("1"), "Las probabilidades NO suman 1"

# Resultados (utilidad económica neta en COP) por acción y estado
payoff = {
    "lanzar":    {"alta": D("8000000"),  "media": D("2000000"), "baja": D("-1500000")},
    "no_lanzar": {"alta": D("0"),        "media": D("0"),        "baja": D("0")},
}

def valor_esperado(accion):
    return sum(prob[s] * payoff[accion][s] for s in prob)

ve = {a: valor_esperado(a) for a in payoff}
print("VE lanzar   :", ve["lanzar"])      # COP
print("VE no_lanzar:", ve["no_lanzar"])   # COP
mejor = max(ve, key=ve.get)
print("Decision    :", mejor)

# --- Valor de la información perfecta ---
estados = list(prob)
vecip = sum(prob[s] * max(payoff[a][s] for a in payoff) for s in estados)
veip  = vecip - ve[mejor]
print("VECIP       :", vecip)
print("VEIP (techo a pagar por saber el futuro):", veip)
```

```python
# === VERIFICACIÓN POR SEGUNDA VÍA ===
# Vía 1 (arriba): suma ponderada con Decimal.
# Vía 2: recalculo a mano, en centavos enteros, y comparo.
P = {"alta": 30, "media": 50, "baja": 20}            # en % (enteros)
PAY = {"alta": 8000000, "media": 2000000, "baja": -1500000}
# VE = Σ (p% * payoff) / 100  -> entero exacto
ve_lanzar_int = sum(P[s] * PAY[s] for s in P) // 100
assert ve_lanzar_int == int(ve["lanzar"]), "Discrepancia entre métodos"
print("Check VE lanzar (centavos/100):", ve_lanzar_int)  # 2.5M COP

# Sanity de orden de magnitud: pesimista -1.5M, optimista 8M -> VE debe caer dentro
assert -1500000 <= ve_lanzar_int <= 8000000
# VEIP nunca negativo
assert veip >= 0
print("Verificaciones OK")
```

Salida esperada: `VE lanzar = 2.500.000 COP`, `VE no_lanzar = 0`, decisión = **lanzar**; `VECIP = 2.800.000`, `VEIP = 300.000 COP`.

## Ejemplo trabajado

**Situación.** GastroLatam evalúa lanzar la Calculadora de Costos. Resultados netos estimados (COP):

| Estado | Prob. | Lanzar | No lanzar |
|---|---|---|---|
| Demanda alta | 0,30 | +8.000.000 | 0 |
| Demanda media | 0,50 | +2.000.000 | 0 |
| Demanda baja | 0,20 | −1.500.000 | 0 |

**Paso 1 — VE de lanzar:**
`0,30·8.000.000 + 0,50·2.000.000 + 0,20·(−1.500.000)`
`= 2.400.000 + 1.000.000 − 300.000 = 2.500.000 COP`.

**Paso 2 — VE de no lanzar:** `0 COP`.

**Paso 3 — Decisión por VE:** lanzar (2,5M > 0). **CON UNIDADES: VE = +2.500.000 COP.**

**Paso 4 — ¿Vale pagar un estudio de mercado?**
Con información perfecta elegirías la mejor opción en cada estado: alta→lanzar (8M), media→lanzar (2M), baja→no lanzar (0).
`VECIP = 0,30·8.000.000 + 0,50·2.000.000 + 0,20·0 = 2.800.000 COP`.
`VEIP = 2.800.000 − 2.500.000 = 300.000 COP`. Un estudio que cueste **menos de $300.000** y prediga bien la demanda puede valer la pena; uno más caro, no (y eso suponiendo predicción perfecta — uno real vale menos).

**Paso 5 — Mirada de riesgo.** Aunque el VE es positivo, hay 20% de perder $1,5M. Si ese golpe te descapitaliza, conviene evaluar con **utilidad** (siguiente sección de la skill) o reducir la apuesta (piloto pequeño).

## Errores comunes / trampas

- **Probabilidades que no suman 1** (o negativas): invalida todo el VE. Siempre `assert sum(p)==1`.
- **Confundir VE con resultado garantizado:** el VE es promedio a largo plazo; en una decisión única "todo o nada" puede no aplicar — ahí pesa la utilidad/riesgo.
- **Usar VE cuando la pérdida es ruinosa:** maximizar VE ignora que quebrar es irreversible. Para apuestas que pueden hundirte, decide por utilidad esperada, no por VE.
- **Doble conteo de costos:** mete los costos UNA vez (en los payoffs) y no otra vez aparte.
- **Float para dinero:** `0.1+0.2 != 0.3`. Usa `Decimal` o centavos enteros (ver [[12-fracciones-decimales-y-precision]]).
- **VEIP negativo:** matemáticamente imposible; si te da negativo, hay un error de cálculo.
- **Pagar por información que no cambiaría tu decisión:** si harías lo mismo pase lo que pase, la información vale $0 — no la compres.
- **Sesgo de optimismo en las probabilidades:** inventarlas a conveniencia. Documenta de dónde salen y haz [[93-analisis-de-sensibilidad-y-escenarios]].

## Cruces

- [[57-valor-esperado-y-varianza]] — base formal del valor esperado y la dispersión del resultado.
- [[52-teorema-de-bayes]] — actualizar probabilidades cuando una prueba da una señal (info imperfecta).
- [[58-simulacion-monte-carlo]] — cuando el árbol es muy grande o las distribuciones continuas.
- [[93-analisis-de-sensibilidad-y-escenarios]] — probar qué tan robusta es la decisión a cambios en probabilidades/payoffs.
- [[94-riesgo-var-y-volatilidad]] — cuantificar la cola de pérdidas que el VE solo no muestra.

**Mini-checklist de exactitud**
- [ ] Las probabilidades suman exactamente 1 y están en [0,1] (con `assert`).
- [ ] Dinero en `Decimal`/centavos; redondeo solo al final; VE verificado por una segunda vía.
- [ ] Si la pérdida puede ser ruinosa, decidí por utilidad/riesgo, no solo por VE.
