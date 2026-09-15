# 124 — Stablecoins

## Qué son

Una **stablecoin** es una criptomoneda diseñada para valer siempre lo mismo — casi siempre 1 dólar
(USD). Son el "efectivo" del mundo cripto: cuando el bot vende ETH, el resultado queda en una
stablecoin, no en pesos ni en dólares de banco.

## Los tres tipos (de más sólido a más frágil)

| Tipo | Cómo mantiene el valor | Ejemplos | Riesgo principal |
|---|---|---|---|
| **Fiat-backed** (respaldada por dólares) | Una empresa guarda dólares/bonos reales por cada moneda emitida | USDT (Tether), USDC (Circle) | Que el respaldo no sea el que dicen, o que el emisor tenga problemas legales/bancarios |
| **Cripto-backed** (respaldada por cripto) | Sobre-colateral: se depositan ~$150+ en cripto por cada $100 emitidos | DAI | Caída violenta del colateral + fallas del contrato inteligente |
| **Algorítmica** | Ningún respaldo real; un mecanismo de incentivos "debería" sostener el precio | UST (murió en 2022) | Espiral de la muerte: cuando pierde el precio, el mecanismo lo empeora |

## El riesgo de depeg (la lección de UST)

**Depeg** = que la stablecoin deje de valer 1 dólar. La lección histórica es UST (Terra), en mayo
de 2022: una stablecoin algorítmica top-5 por capitalización pasó de $1 a centavos en días, y
arrastró decenas de miles de millones de dólares. No fue un hackeo: el diseño era frágil y una
corrida lo demostró. Moraleja: "stable" es una promesa de diseño, no una garantía.

Las fiat-backed grandes también han tenido depegs breves (por ejemplo, USDC tocó ~$0.87 por horas
en marzo de 2023 cuando quebró un banco donde Circle tenía reservas, y recuperó el peg en días).
Breve no significa imposible de repetir peor.

## USDT vs USDC (resumen honesto)

- **USDT (Tether)**: la de mayor volumen y liquidez en exchanges, especialmente en pares de
  trading. Historial de opacidad sobre sus reservas y multas regulatorias en el pasado; hoy
  publica atestaciones (no auditorías completas). Verificar estado al día.
- **USDC (Circle)**: reputación de mayor transparencia y cumplimiento regulatorio en EE.UU.;
  algo menos de liquidez en pares de trading que USDT.
- Regla práctica: **para operar**, el par con más liquidez (típicamente USDT en Binance);
  **para guardar** saldos grandes por tiempo largo, diversificar entre emisores es razonable.

## Cómo aplica al AGENTE TRADING

- El bot opera pares contra USDT en Binance (BTC/USDT, ETH/USDT): es donde está la liquidez y
  el spread más fino. En paper esto es solo contabilidad; en live será exposición real a Tether.
- El riesgo de depeg es un riesgo de cartera, no de estrategia: cuando el bot está "fuera del
  mercado", en realidad está 100% en USDT. Para el capital chico del go-live es un riesgo
  aceptable y monitoreable; si el capital escala, revisar diversificación de stablecoin.
- El bot NUNCA "invierte" en stablecoins ni persigue rendimientos por prestarlas (eso es DeFi
  yield, módulo 128): su única función aquí es ser la caja registradora.
