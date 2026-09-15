# 14 — Checklist pre-trade

Una **checklist pre-trade** es la lista de verificación que se repasa ANTES de abrir cualquier
posición. Los pilotos de avión la usan hace 90 años por la misma razón que un trader: bajo presión,
la memoria falla y el impulso manda. Si un punto falla, **no hay trade** — no se "compensa" con
otro punto fuerte.

## La checklist (en el orden del pipeline)

| # | Verificación | Pregunta que responde | Quién la hace en el bot |
|---|---|---|---|
| 1 | Psicología | ¿Estoy en condiciones de operar? (límites diarios, rachas, cooldown) | `tradingPsychology` (gate JS, corre PRIMERO) |
| 2 | Régimen | ¿El mercado está en un estado donde mi estrategia funciona? | Claude Haiku 4.5 clasifica el régimen |
| 3 | Memoria | ¿Qué pasó las últimas veces en condiciones parecidas? | `traderMemory` (historial de trades propios) |
| 4 | Técnico | ¿Los indicadores confirman la entrada? | JS puro: RSI, MACD, SMA |
| 5 | Convicción | ¿Cuánta confianza real merece este setup? (1-10) | Claude Sonnet 5, criterio Druckenmiller, JSON |
| 6 | Sizing | ¿Cuánto arriesgo? (Kelly fraccional, techo 1.5%) | `positionSizing.js` |
| 7 | R:R | ¿La ganancia potencial justifica el riesgo? (mínimo 1:2) | Cálculo de stop (1.5× volatilidad) y target |

**Términos:** *régimen* = estado general del mercado (tendencia alcista, bajista, lateral).
*R:R* = risk:reward, cuánto puedo ganar por cada $1 que arriesgo. *Sizing* = tamaño de la posición.
*Convicción* = nota de 1 a 10 de qué tan bueno es el setup; solo ≥8 dispara ejecución automática.

## Las 3 reglas de oro de una checklist

1. **Es secuencial y con vetos.** Si la psicología dice "no", no importa qué diga el técnico.
   El orden existe porque los filtros baratos (JS gratis) van antes que los caros (Claude).
2. **Es binaria, no negociable.** "Casi cumple" = no cumple. La checklist que se flexibiliza
   una vez ya no es checklist, es sugerencia.
3. **Se audita después.** Cada trade cerrado se compara contra la checklist: ¿se respetó todo?
   Un trade ganador que violó la checklist es un ERROR (que salió bien por suerte).

## La lección real: el filtro que faltaba

El bot cumplió su checklist y aun así compró ETH "extendido" (precio muy por encima de su promedio
reciente): **0/3 ganados sobre $1.788 vs 4/4 bajo $1.760**. Lección: la checklist es un documento
vivo — cuando la evidencia muestra un agujero (aquí, falta un filtro anti-extensión), se AGREGA
un punto, con fecha y razón. Nunca se quita un punto porque "estorba".

## Cómo aplica al AGENTE TRADING

- El pipeline cada 2 horas ES la checklist automatizada: psicología → régimen → memoria →
  técnico → convicción → sizing. Ningún paso se salta.
- El bug del trade con convicción 0 (1 trade fuera de protocolo, en investigación) es exactamente
  lo que una checklist debe imposibilitar: hay que agregar una **aserción dura en código**
  ("si convicción < 8 → prohibido ejecutar, loguear y abortar"), no confiar en el flujo.
- Verificación manual de Luis: revisar en el dashboard que cada trade nuevo tenga los 7 puntos
  registrados. Si falta uno, es bug, no detalle.
- Cálculos de sizing/R:R exactos → skill `Matematicas_lushows`.
