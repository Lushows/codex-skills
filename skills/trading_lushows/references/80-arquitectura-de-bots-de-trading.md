# 80 — Arquitectura de bots de trading

Todo bot de trading, desde el script casero hasta el sistema institucional, tiene los mismos 6
componentes. Conocerlos permite entender cualquier bot — y detectar cuál componente falta cuando
algo sale mal.

## Los 6 componentes universales

| Componente | Qué hace | En el AGENTE TRADING |
|---|---|---|
| **Datos** | Traer precios/velas del mercado, en vivo e histórico | WebSocket Binance (velas 1h) + REST mirror `data-api.binance.vision` |
| **Señal** | Decidir SI hay oportunidad y en qué dirección | Pipeline: régimen (Haiku) → memoria → técnico (JS) → convicción Druckenmiller (Sonnet, 1-10) |
| **Riesgo** | Decidir CUÁNTO: tamaño, stop, target, límites | `positionSizing.js` (Kelly fraccional, techo 1.5%) + gate psicológico (cooldowns, máx trades) |
| **Ejecución** | Poner las órdenes en el mercado (o simularlas) | Broker paper (comisión 0.1%, slippage 5bps) + `watcher.js` vigila stops/targets |
| **Persistencia** | Que nada se pierda al reiniciar | Stores JSON atómicos en `data/` (portfolio, velas, memoria, análisis, equity) |
| **Monitoreo** | Saber si el sistema está vivo y obedeciendo | `/status`, logs, errores 24h, dashboard, alertas (módulo 86) |

Regla de diagnóstico: cuando un bot "falla", casi siempre es UN componente el que falló — y saber
cuál cambia todo. Un trade malo es problema de Señal; un trade demasiado grande es de Riesgo; un
trade fantasma tras reinicio es de Persistencia.

## Decisiones de diseño del AGENTE TRADING y sus porqués

1. **Gate psicológico PRIMERO, en JS puro** — si hay cooldown, el pipeline muere antes de gastar
   un token. Lo barato y determinista filtra; lo caro (IA) solo corre cuando vale la pena.
2. **Números en JS, juicio en IA** — RSI/MACD/sizing se calculan en código (exactos, testeables);
   Claude interpreta y decide. Un LLM haciendo aritmética es un riesgo innecesario (módulo 82).
3. **Dos modelos, dos costos** — Haiku (barato) clasifica el régimen; Sonnet (caro, con thinking)
   solo decide convicción. Enrutar por dificultad ahorra ~80% del costo (módulo 88).
4. **Umbral de auto-ejecución (8/10)** — la IA propone, un número duro decide. Sin umbral, cada
   corazonada del modelo sería un trade.
5. **Paper primero, con fricción realista** — comisión y slippage simulados para que las métricas
   de paper no mientan al pasar a live.
6. **Persistencia atómica** — escribir a archivo temporal y renombrar, para que un crash a mitad
   de escritura no corrompa el estado (módulo 87).
7. **Meta-análisis semanal** — el sistema se estudia a sí mismo y produce propuestas; el loop de
   mejora está diseñado, no improvisado (módulo 84).

## Límites honestos del diseño actual

- **Stops vigilados localmente** (`watcher.js`): si el proceso muere, nadie vigila. En live los
  stops DEBEN vivir en el exchange (órdenes OCO). Aceptable solo en paper.
- **Solo LONG**: en mercados bajistas el sistema solo puede no perder, no ganar.
- **Un exchange, un timeframe (1h)**: simple a propósito; la complejidad se gana cuando la
  simplicidad demuestre sus límites con datos, no antes.

## Cómo aplica al AGENTE TRADING

Este módulo ES el mapa del bot. Al depurar, primero pregunta: ¿cuál de los 6 componentes falló?
Al proponer mejoras, pregunta: ¿qué componente toca y qué invariante de diseño (gate primero,
números en JS, umbral duro) debe respetar?
