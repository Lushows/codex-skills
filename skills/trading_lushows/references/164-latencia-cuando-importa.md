# 164 — Latencia: cuándo importa y cuándo es paranoia

## Qué es latencia

Latencia = el tiempo entre que algo pasa en el mercado y tu sistema reacciona. Se mide en
milisegundos (ms) o segundos. El error típico del principiante es obsesionarse con ella
("¡necesito un servidor al lado de Binance!") cuando su estrategia opera en horas.

## La latencia del bot, capa por capa

| Capa | Latencia típica | Comentario |
|---|---|---|
| Vela por WebSocket (Binance → bot) | decenas–cientos de ms | Irrelevante para velas de 1h |
| Cálculo de indicadores (JS local) | milisegundos | Gratis |
| Análisis con Claude (Haiku + Sonnet con thinking) | **segundos, a veces decenas** | La capa más lenta por mucho |
| Envío de orden al exchange (live futuro) | cientos de ms | Depende de región (Frankfurt ayuda) |
| Ciclo del auto-trader | corre **cada 2h** | La verdadera "latencia" estratégica del sistema |

Lectura honesta: el bot decide en una escala de **horas**. Que Claude tarde 20 segundos en
razonar una convicción es el 0.3% de una vela de 1h. Optimizar milisegundos aquí sería pulir
el retrovisor de un barco.

## Por qué el swing 1h tolera segundos

El swing trading busca movimientos de días. La diferencia entre entrar a $60.000 y entrar a
$60.030 (lo que se movió el precio en los segundos de análisis) es 0.05% — menos que la comisión
(0.1%) y el slippage que el propio simulador ya cobra. La ventaja del sistema no está en la
velocidad sino en la **selección** (convicción ≥8) y el **sizing** (riesgo 1.5%).

Quien sí necesita microsegundos: market makers, arbitraje, HFT. Ese juego exige colocación
física junto al exchange y equipos enteros — no es este proyecto ni debe intentar serlo.

## Dónde la latencia SÍ importa en este proyecto

1. **Los stops en vivo.** Hoy `watcher.js` vigila stops localmente revisando el precio. En paper
   da igual; en live es peligroso: si el bot está caído, redeployando o el WS está zombie durante
   un desplome, el stop **no se ejecuta**. La latencia relevante no es de ms, es de *minutos u
   horas de bot muerto*. Solución: órdenes **OCO** (One-Cancels-the-Other: stop y target viven
   juntos EN el exchange; se dispara uno y cancela al otro) — el exchange reacciona en ms aunque
   el bot esté apagado. Es requisito de Fase 8, no opcional.
2. **Datos viejos.** Peor que datos lentos son datos zombie (módulo 161): decidir con una vela
   de hace 40 minutos creyendo que es actual.
3. **Gaps de fin de semana no existen en cripto** (mercado 24/7), pero los desplomes de madrugada
   sí — otra razón para OCO.

## Cómo aplica al AGENTE TRADING

Regla del proyecto: **la latencia de análisis no se optimiza; la latencia de protección se
elimina delegándola al exchange.** Claude puede pensar 30 segundos tranquilamente. Lo que jamás
puede depender de que el bot esté vivo es el stop-loss con dinero real. Frankfurt (Fase 8) mejora
de paso la latencia de órdenes hacia Binance, pero el motivo real de la mudanza es el geo-bloqueo,
no la velocidad.
