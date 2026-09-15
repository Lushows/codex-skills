# 129 — Evaluar un activo nuevo (checklist)

## Para qué sirve este módulo

El 126 define el proceso para agregar un par al bot. Este es el paso anterior: el filtro rápido
para decidir si un activo siquiera MERECE ese proceso. La mayoría muere aquí, y eso es lo que
debe pasar — decir no rápido es barato; decir sí mal es caro.

## El checklist (en orden: lo barato de verificar primero)

### 1. Liquidez (eliminatorio)

- ¿Está en el top de volumen spot de Binance, comparable a las large caps? (verificar al día)
- ¿La profundidad del libro al ±1-2% aguanta las órdenes del bot sin slippage relevante?
- ¿El volumen es honesto? (señales de wash trading → módulo 127)

Si falla aquí, se descarta y no se gasta ni un minuto más. La liquidez no se negocia.

### 2. Historia

- ¿Hay ≥1-2 años de velas 1h disponibles, cubriendo al menos un ciclo alcista y uno bajista?
- ¿La historia está "limpia"? Migraciones de token, redenominaciones, splits o relistados parten
  la serie de velas y hacen el backtest inservible.
- ¿El activo ya sobrevivió a un mercado bajista completo? Los que no, son apuestas, no datos.

### 3. Catalizadores conocidos

**Catalizador** = evento programado que puede mover el precio con violencia ajena al análisis
técnico: desbloqueos grandes de tokens a insiders (ver supply diluido, módulo 127), decisiones
judiciales o regulatorias pendientes, actualizaciones mayores del protocolo, halvings. No hay que
predecirlos — hay que saber que existen, porque un swing de 1h puede quedar atrapado en uno.
Fuente: el calendario público del proyecto (verificar al día).

### 4. Correlación

- ¿Correlación con BTC y con los pares ya activos <0.9 (ideal <0.8), medida sobre retornos
  diarios de 6-12 meses? → cálculo con `Matematicas_lushows`.
- Pregunta honesta: ¿qué trade ofrece este activo que ETH no ofrece ya? Si la respuesta es
  "es lo mismo pero más volátil", eso es más costo, no más edge.

### 5. Riesgo regulatorio

- ¿Tiene litigios o investigaciones abiertas de reguladores grandes? (el caso XRP-SEC mostró que
  esto domina el precio por años; estado actual de cualquier caso: verificar al día)
- ¿Riesgo de deslistado del exchange? Un deslistado de Binance es un evento de −30%+ inmediato
  y la muerte de la liquidez del par.
- ¿Depende de una sola empresa/persona cuyo problema legal sería el problema del token? (BNB y
  Binance son el ejemplo de riesgo concentrado; estado al día, verificar)

## Regla de decisión

| Resultado | Acción |
|---|---|
| Falla el punto 1 o 2 | Descarte definitivo (re-evaluable en 6-12 meses) |
| Pasa 1-2, dudas en 3-5 | Va a lista de espera con la duda anotada |
| Pasa los 5 | Recién ahí entra al proceso del módulo 126 (backtest + paper) |

Pasar el checklist NO significa operar el activo: significa ganarse el derecho al backtest.

## Cómo aplica al AGENTE TRADING

- SOL, el candidato del backlog, se evalúa con este checklist ANTES del proceso 126. Los puntos
  1-2 son casi seguros; el trabajo real está en 4 (correlación con ETH, que será alta — la
  pregunta es cuánto) y 5 (estado regulatorio al día).
- Este checklist también protege del entusiasmo propio: cuando aparezca "la moneda del momento",
  se le pasa el checklist por escrito y casi siempre muere en el punto 1 o 2. El documento
  decide, no el ánimo.
