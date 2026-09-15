# 130 — Fuentes de datos de mercado

> El trading es una guerra de información. Antes de pagar por datos "premium", entender qué existe,
> qué es gratis y qué de verdad mueve la aguja para un sistema como el nuestro.

## Los 4 tipos de datos de mercado

| Tipo | Qué es | Para qué sirve |
|---|---|---|
| **Velas OHLCV** | Open/High/Low/Close/Volumen por período (ej: 1 hora) | La base de casi todo: indicadores, backtests, régimen |
| **Trades (tick data)** | Cada operación individual ejecutada | Microestructura, análisis fino de ejecución |
| **Libro de órdenes** | Órdenes de compra/venta esperando en cada precio | Liquidez, muros, profundidad — cambia cada milisegundo |
| **Funding / OI** | Datos de futuros perpetuos (ver módulo 135) | Termómetro de apalancamiento del mercado |

**Vela (candle)**: resumen de un período. "Vela 1h" = el precio de apertura, máximo, mínimo,
cierre y volumen de esa hora. Es el formato más compacto y suficiente para swing trading.

## Gratis vs pago — la verdad

- **Gratis y suficiente para swing**: las APIs públicas de los exchanges (Binance, Coinbase, etc.)
  regalan velas OHLCV históricas y en tiempo real. Para operar velas 1h no necesitas pagar nada.
- **De pago**: tick data histórico completo, libro de órdenes histórico, datos on-chain curados
  (Glassnode, CryptoQuant), agregadores multi-exchange. Precios cambian — verificar al día.
- **Regla honesta**: si tu estrategia no gana con velas gratis, datos caros no la van a salvar.
  Los datos premium mejoran sistemas que YA funcionan; no crean edge de la nada.

## Trampa común

Comprar suscripciones a datos "institucionales" antes de tener una estrategia validada es el
equivalente a comprarse guayos profesionales sin saber patear. Primero el sistema, luego el dato fino.

## Cómo aplica al AGENTE TRADING

- El bot usa **solo velas 1h de BTCUSDT y ETHUSDT**: WebSocket público de Binance para tiempo real
  y el mirror REST `data-api.binance.vision` para histórico/relleno. Costo de datos: **$0**.
- Las velas se guardan en JSON local (`candlesStore`) — ese archivo es nuestro dataset propio y
  la materia prima del backtesting pendiente (backlog).
- No usamos tick data ni libro de órdenes: para swing en velas 1h no aportan y complican todo.
- Si algún día se agregan datos on-chain o de derivados, entrarían como **contexto para Claude**
  en el análisis, no como disparador automático (ver módulos 132-137 para sus límites).
