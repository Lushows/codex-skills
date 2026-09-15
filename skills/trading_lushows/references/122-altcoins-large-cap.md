# 122 — Altcoins large cap (SOL, BNB, XRP y similares)

## Qué son

**Altcoin** = cualquier criptomoneda que no es Bitcoin. **Large cap** = las de mayor capitalización
de mercado (el valor total de todas sus monedas en circulación). Después de BTC y ETH, el grupo
grande suele incluir SOL, BNB, XRP y unas pocas más — verificar el ranking al día, porque rota.

No son "el siguiente Bitcoin". Son activos distintos, con dinámicas propias:

| Activo | Qué es (resumen honesto) |
|---|---|
| SOL (Solana) | Blockchain de contratos inteligentes, rápida y barata; historial de caídas de red en sus primeros años |
| BNB | Token del exchange Binance; su suerte está atada a la de Binance (riesgo regulatorio concentrado) |
| XRP | Token de Ripple, enfocado en pagos; años de litigio regulatorio en EE.UU. marcaron su precio |

## En qué se diferencian de BTC/ETH para un bot de swing

1. **Más volatilidad.** Un día "normal" en una large cap puede mover lo que BTC mueve en una semana.
   Eso agranda tanto las ganancias como los stops barridos por ruido.
2. **Menos liquidez.** Hay menos compradores y vendedores en el libro de órdenes. El **spread**
   (diferencia entre el mejor precio de compra y el de venta) es mayor, y el **slippage** (lo que
   el precio se mueve en tu contra al ejecutar) también. Los costos modelados del bot (módulo 07)
   asumen BTC/ETH; en una altcoin serían mayores — recalcular, no reciclar.
3. **Beta alta contra BTC.** Cuando BTC cae, las altcoins suelen caer más. Agregar SOL no
   diversifica tanto como parece: en pánico, todo cae junto (correlación alta).
4. **Riesgo idiosincrático.** Caídas de red, demandas, decisiones de una empresa central. BTC y ETH
   también tienen riesgos, pero mucho más repartidos.

## Criterios mínimos para que una large cap entre al bot

- Volumen diario en spot de Binance comparable en orden de magnitud al de ETH (verificar al día).
- Spread típico que no se coma el edge: si el sistema busca +3% por trade y el peaje redondo sube
  de ~0.30% a ~0.5%+, el win rate mínimo sube — pasar los números por `Matematicas_lushows`.
- Historia de velas 1h suficiente (mínimo 1-2 años) para backtest en varios regímenes de mercado.
- Que aporte algo que BTC/ETH no dan: si su correlación con ETH es >0.9, es casi el mismo trade
  con más costos.

El proceso completo de evaluación está en el módulo 126.

## Cómo aplica al AGENTE TRADING

- SOL es el candidato natural a tercer par: la más líquida del grupo después de BTC/ETH
  (verificar al día) y con historia de velas suficiente en Binance.
- Pero es un candidato, no una decisión: antes debe pasar el checklist del módulo 126 y un
  backtest propio con los costos reales de SOL, no los de ETH.
- Prioridad honesta: primero que el sistema demuestre edge en ETH (PF > 1.3 con ≥30 trades).
  Agregar pares a un sistema que aún no gana es multiplicar una expectancy negativa.
