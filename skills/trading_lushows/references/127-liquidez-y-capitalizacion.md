# 127 — Liquidez y capitalización

## Market cap: el número que todos citan y pocos entienden

**Market cap (capitalización de mercado)** = precio actual × monedas en circulación. Es un
termómetro de tamaño, no dinero real que "está adentro": nadie podría vender todas las monedas a
ese precio.

Dos trampas clásicas:

- **Circulante vs diluido.** El *circulating supply* son las monedas ya en el mercado; el *fully
  diluted valuation* (FDV) cuenta también las que se emitirán después (desbloqueos a insiders,
  recompensas futuras). Un token puede verse "barato" por market cap circulante mientras tiene
  5-10x más monedas esperando salir a venderse encima de los compradores. Siempre mirar ambos
  números (verificar al día en el listado del activo).
- **Market cap bajo ≠ barato.** "Solo vale 50 millones, imagina si llega al market cap de ETH"
  es el argumento favorito del vendedor de humo. El tamaño pequeño refleja, en general, que el
  mercado ya evaluó el proyecto — y concluyó eso.

## Volumen honesto vs volumen inflado

El volumen reportado se puede fabricar (**wash trading**: comprarse y venderse a uno mismo).
Señales de volumen inflado:

- Volumen "alto" pero **libro de órdenes** vacío: si hay tanto trading, ¿dónde están las órdenes?
- Volumen concentrado en exchanges pequeños u opacos, no en los grandes.
- Ratio volumen/market cap absurdo (el token "rota" su capitalización entera cada día).
- Spread ancho pese al volumen supuestamente alto — el volumen real aprieta spreads.

En Binance spot con pares grandes (BTC, ETH, large caps) el volumen es de lo más confiable que
hay en cripto. Cuanto más se baja de escalón, menos vale el número reportado.

## Profundidad: la liquidez que importa de verdad

La **profundidad** (depth) es cuánto dinero hay en órdenes reales cerca del precio actual. Es lo
que determina tu **slippage**: si el libro tiene $500.000 en órdenes dentro del ±1% del precio,
una orden de $100 no lo mueve; en un token con $5.000 de profundidad, sí. La profundidad además
se evapora en los momentos de pánico — exactamente cuando el stop loss necesita ejecutarse bien.

Regla práctica: importa la profundidad al ±1-2% del precio, medida también en horas malas, no el
volumen de 24h del ranking.

## Liquidez ES gestión de riesgo

El stop loss del bot es una promesa que solo la liquidez puede cumplir. En un par profundo, un
stop de −1.5% de riesgo cuesta −1.5% más un slippage pequeño y modelable. En un par ilíquido, el
mismo stop puede costar −3% o −5% reales: el riesgo por trade que el sistema cree controlar deja
de ser verdad. Por eso la selección de pares (módulo 126) no es un tema de "oportunidades" sino
el primer eslabón del control de riesgo — antes que el sizing, antes que el stop.

## Cómo aplica al AGENTE TRADING

- BTC/USDT y ETH/USDT en Binance spot están en la élite de liquidez de todo cripto: el modelo de
  costos del bot (0.1% slippage redondo, módulo 07) es realista AHÍ, no en general.
- Al evaluar SOL u otro par: mirar profundidad y spread reales, no el market cap del ranking; y
  revisar el supply diluido para entender presión vendedora futura (verificar al día).
- El riesgo 1.5% por trade solo es verdad si el stop se ejecuta cerca de donde se pidió. La
  liquidez del par es lo que hace honesto ese número.
