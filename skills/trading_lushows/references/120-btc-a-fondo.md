# 120 — BTC a fondo (como activo de trading)

## Qué es BTC para un trader

Dejando la filosofía a un lado: para un trader, Bitcoin es **el activo más líquido, más
vigilado y más "institucional" de cripto**. No es "una cripto más" — es el punto de
referencia contra el que se mide todo lo demás, como el índice S&P 500 lo es para acciones.

## Sus propiedades como instrumento

| Propiedad | Qué significa para operar |
|---|---|
| **Liquidez máxima** | Los spreads más finos y los libros más profundos de cripto: entrar y salir cuesta menos y el slippage es mínimo |
| **Menos manipulable** | Mover el precio de BTC exige capital enorme; los juegos de pump & dump viven en activos chicos, no aquí |
| **Cobertura de datos** | Más de una década de velas, derivados, ETFs, métricas on-chain: el activo con más historia analizable |
| **Volatilidad "baja" (para cripto)** | Se mueve menos que las alts — menos setups de swing, pero también menos mechas traicioneras |
| **Dominancia** | Su peso en el mercado total; cuando sube, el capital se refugia en BTC y las alts sangran (ver `112`) |

## BTC y el macro: ya no es una isla

Desde la entrada institucional (futuros regulados, ETFs spot), BTC se comporta cada vez más
como **activo de riesgo global**: tiende a correlacionar con el Nasdaq, sufre cuando suben
las tasas de interés y respira con la liquidez global. La correlación no es constante —
va y viene por épocas (verificar al día, nunca asumirla) — pero ignorar el macro al operar
BTC es operar con un ojo cerrado. Por eso el régimen incluye `risk-on`/`risk-off` (ver `03`).

## El "índice" del mercado cripto

Regla empírica del mercado:

```
BTC estornuda → las alts se resfrían.  BTC lateral y aburrido → las alts a veces corren.
BTC cae fuerte → cae TODO (la correlación va a 1 en pánico).
```

Por eso, aunque no operes BTC, **siempre se analiza BTC**: es el contexto de cualquier
trade de cualquier alt. Un LONG en ETH con BTC rompiendo soportes es nadar contra el río.

## Como activo del bot: el par "aburrido" en el buen sentido

Para un sistema de trend-following, BTC ofrece señales menos frecuentes pero más limpias:
sus tendencias, cuando existen, son las más respetadas del mercado porque las mueve el
capital más grande. Es el par de menor octanaje y mayor confiabilidad estructural del menú.

## Cómo aplica al AGENTE TRADING

- BTC es uno de los dos pares del bot — y aunque los 10 trades ejecutados hasta ahora
  fueron en ETH (ver `121`), su rol no es decorativo: menos volatilidad = menos setups que
  crucen el umbral de convicción ≥8. Eso es el sistema filtrando, no fallando.
- BTC cumple doble función: **par operable + termómetro de mercado**. Su tendencia y su
  dominancia son contexto obligatorio incluso para los trades de ETH.
- Cuando el bot pase a capital real, BTC es el par donde los errores cuestan menos en
  ejecución (spread y slippage mínimos) — punto a favor para el go-live.
