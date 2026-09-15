# 18 — Flujo de decisión del bot (end-to-end)

El AGENTE TRADING corre su protocolo completo **cada 2 horas**, 24/7, en Render. Este módulo lo
recorre paso a paso con un ejemplo numérico realista de un trade LONG en ETH. (Los precios del
ejemplo son ilustrativos del rango real del proyecto; los de hoy, verificar al día.)

## El pipeline, paso a paso

```
1. Psicología (JS)  →  2. Régimen (Haiku)  →  3. Memoria  →  4. Técnico (JS)
→  5. Convicción (Sonnet)  →  6. Sizing (Kelly)  →  7. Ejecución (solo si ≥8)
```

**Diseño clave**: los filtros gratis (JS) van primero y pueden vetar; los pasos con costo
(Claude) solo corren si vale la pena. Así el costo de IA se queda en ~$5/mes.

## Ejemplo numérico: un ciclo que termina en trade

| Paso | Qué pasa | Resultado del ejemplo |
|---|---|---|
| 1. Psicología | Gate JS revisa: ¿≤5 trades hoy? ¿≤2 posiciones abiertas? ¿sin cooldown por 3 pérdidas? | ✅ 1 trade hoy, 0 posiciones, sin cooldown → sigue |
| 2. Régimen | Haiku 4.5 lee velas 1h de ETH y clasifica el estado del mercado | "Tendencia alcista moderada, volatilidad normal" → operable para LONG |
| 3. Memoria | traderMemory: ¿qué pasó en condiciones parecidas? | Recuerda: entradas bajo $1.760 fueron 4/4; sobre $1.788, 0/3 → contexto para el paso 5 |
| 4. Técnico | JS calcula RSI, MACD, SMA sobre velas 1h | RSI 47 (ni sobrecomprado ni sobrevendido), MACD cruzó al alza, precio sobre SMA → señal LONG |
| 5. Convicción | Sonnet 5 recibe régimen+memoria+técnico y devuelve JSON con nota 1-10 (criterio Druckenmiller: pocas apuestas, solo las claras) | `{"conviccion": 8, "razon": "confluencia técnica + precio no extendido"}` |
| 6. Sizing | Kelly fraccional, techo duro 1.5% de $1.000 = $15 de riesgo. Volatilidad reciente 1.4% → stop a 1.5×1.4% = 2.1% | Notional = $15 / 2.1% ≈ **$714 de posición** |
| 7. Ejecución | Convicción 8 ≥ umbral 8 → auto-ejecuta LONG ETH | Entrada $1.750 · stop $1.713 (−2.1%) · target $1.824 (+4.2%, R:R 1:2) |

## Qué pasa después de entrar

- Un **watcher** (vigilante en código) revisa el precio y cierra en stop o target.
- Costos reales descontados: 0.1% comisión + 0.05% slippage por lado ≈ **0.30% redondo**
  (~$2.1 en este ejemplo). Por eso el target debe ser ambicioso (1:2): un R:R 1:1 con estos
  costos es casi regalar el edge.
- El trade cerrado se escribe en traderMemory con todo su contexto (ver `15`).

## Los dos finales posibles del ejemplo

- **Target**: +$30 de ganancia bruta − ~$2.1 costos ≈ **+$27.9** (+1.86R neto).
- **Stop**: −$15 − ~$2.1 ≈ **−$17.1** (−1.14R neto). Nota honesta: los costos hacen que el
  1:2 nominal sea ~1:1.6 neto. Está contemplado, pero explica por qué PF 0.89 con pocos
  trades no sorprende.

## Los ciclos que NO terminan en trade (la mayoría)

Cada 2h hay 12 ciclos/día y el bot promedia ~1 trade cada 4 días: **más del 97% de los ciclos
deciden NO operar**. Eso es diseño, no fallo — Druckenmiller: la plata se hace esperando.
Cada análisis se guarda en `analyses` igual, para auditar los no-trades.

## Cómo aplica al AGENTE TRADING

- Este ES el bot; el módulo sirve para explicárselo a cualquiera (incluido el Luis del futuro).
- El bug conocido (1 trade con convicción 0) violó el paso 7 → falta aserción dura en código:
  ejecutar sin convicción ≥8 debe ser IMPOSIBLE, no improbable. Ver `14`.
- Cálculos de sizing/costos verificables → `Matematicas_lushows`.
