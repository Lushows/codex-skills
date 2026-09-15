# 132 — Métricas on-chain

> "On-chain" = datos que viven en la blockchain misma, visibles para todos: cuánto se mueve,
> quién acumula, a qué precio compró la gente. Es información que en acciones no existe.
> Suena a superpoder — y tiene su gracia — pero hay que entender sus límites.

## Las 4 métricas más citadas

| Métrica | Qué mide (en simple) | Qué "señala" |
|---|---|---|
| **MVRV** | Precio actual vs precio promedio al que se compró cada moneda | Muy alto = mercado "caro" (todos en ganancia); muy bajo = "barato" |
| **SOPR** | Si las monedas que se mueven hoy se venden con ganancia o pérdida | >1 sostenido = se toma ganancia; <1 = se vende con pérdida (capitulación) |
| **Reservas en exchanges** | Cuánto BTC/ETH está guardado en los exchanges | Bajando = la gente lo saca para guardar (alcista, en teoría) |
| **Direcciones activas** | Cuántas billeteras se mueven al día | Proxy de uso/adopción de la red |

## Los límites — la parte que los vendedores de indicadores no cuentan

1. **Son lentas**: hablan de ciclos de meses, no de la próxima vela. Para swing de días son
   contexto de fondo, no gatillo de entrada.
2. **Son revisionistas**: los proveedores re-etiquetan billeteras constantemente (¿esta dirección
   es de Binance o de una ballena?). El dato histórico que ves HOY puede ser distinto al que se
   veía en ese momento — eso envenena backtests con datos on-chain.
3. **Umbrales arbitrarios**: "MVRV > 3.5 = techo" funcionó en ciclos pasados; nada garantiza que
   el próximo ciclo respete el mismo número (ver módulo 141, sesgo de supervivencia).
4. **ETFs y custodios** distorsionan las reservas en exchanges: monedas que salen a un custodio de
   ETF no son "hodlers acumulando".

## Veredicto honesto

Útiles como **clima macro** (¿estamos en zona históricamente cara o barata?). Inútiles como señal
de entrada precisa. Y de pago en su versión seria (Glassnode, CryptoQuant) — verificar precios al día.

## Cómo aplica al AGENTE TRADING

- El bot **no usa datos on-chain hoy** y está bien así: opera swing en velas 1h, donde estas
  métricas no aportan gatillos.
- Si algún día se integran, sería como **una línea de contexto** en el prompt del análisis de
  régimen (macroRegime), nunca como condición automática de compra/venta.
- Jamás backtestear con on-chain histórico sin entender el problema del re-etiquetado (punto 2).
