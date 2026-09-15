# 126 — Seleccionar pares para el bot

## El principio

Agregar un par no es "más oportunidades gratis": es más costos, más ruido, más código que mantener
y más formas de perder. Un par nuevo debe GANARSE su lugar con criterios objetivos, medidos, no
con entusiasmo. La carga de la prueba es siempre del par candidato.

## Los 4 criterios objetivos

### 1. Volumen diario (liquidez)

Volumen alto = entrar y salir sin mover el precio. Regla práctica: el par debe estar entre los de
mayor volumen spot de Binance, en el mismo orden de magnitud que ETH/USDT (cifras exactas:
verificar al día en Binance, no de memoria). Y volumen HONESTO — cómo detectarlo, en el módulo 127.

### 2. Spread

El **spread** (diferencia entre mejor compra y mejor venta) es un costo invisible que se paga en
cada trade. Medirlo en el par candidato en horas normales Y en horas de baja actividad. Si el
peaje total redondo (comisión + slippage + spread) supera claramente el ~0.30% modelado para
BTC/ETH, recalcular el win rate mínimo con `Matematicas_lushows` (módulo 07) antes de seguir.

### 3. Historia de velas

Mínimo 1-2 años de velas 1h que cubran al menos un mercado alcista Y uno bajista. Backtest sobre
solo buenos tiempos = autoengaño con gráficas. Sin historia suficiente, no hay evaluación posible
— el par espera, sin excepciones.

### 4. Correlación con los pares existentes

**Correlación** = qué tanto se mueven dos activos juntos (de −1 a +1). Si el candidato tiene
correlación >0.9 con ETH, es casi el mismo trade: duplica exposición, no diversifica. Calcularla
sobre retornos diarios de 6-12 meses con `Matematicas_lushows`. Ideal: <0.8 con cada par activo.
En cripto casi todo está correlacionado con BTC; la pregunta honesta es "¿cuánto MENOS?".

## Proceso para agregar un par (aplicado a SOL)

| Paso | Qué se hace | Criterio de paso |
|---|---|---|
| 1. Liquidez | Verificar volumen spot SOL/USDT al día | Top de Binance, orden de magnitud de ETH |
| 2. Costos | Medir spread real; recalcular peaje | Win rate mínimo no sube más de ~1-2 puntos vs ETH |
| 3. Historia | Descargar ≥1-2 años de velas 1h al JSON | Cubre régimen alcista y bajista |
| 4. Correlación | Retornos diarios SOL vs ETH y vs BTC | Aporta algo que ETH no da |
| 5. Backtest | Correr la estrategia actual sobre SOL, con costos de SOL | PF y DD comparables o mejores que ETH |
| 6. Paper | Operar SOL solo en paper, en paralelo | ≥30 trades antes de contar para go-live |

Si falla un paso, se detiene ahí. No se "compensa" un criterio malo con otro bueno.

## Cómo aplica al AGENTE TRADING

- Hoy el bot opera BTC y ETH (y en la práctica, los 10 trades han sido todos ETH — dato que ya
  dice algo sobre qué régimen filtra la estrategia en BTC).
- SOL es el candidato del backlog: correr este proceso completo antes de escribir una línea de
  código de integración. El paso 3 (velas al JSON) es el único trabajo técnico previo.
- Regla de prioridad: con PF actual 0.89, arreglar el edge va ANTES que agregar pares. Un tercer
  par sobre un sistema perdedor solo acelera la pérdida.
