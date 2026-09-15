# 128 — DeFi: tokens y yield

## Qué es DeFi

**DeFi** (finanzas descentralizadas) = servicios financieros que corren en contratos inteligentes
sobre una blockchain, sin banco ni empresa en el medio: exchanges descentralizados (Uniswap),
préstamos (Aave), stablecoins cripto-backed (DAI/Maker), etc.

Dos cosas distintas que suelen confundirse:

1. **Tokens DeFi** — el token de gobernanza/valor del protocolo (UNI, AAVE...). Se compran y
   venden como cualquier altcoin.
2. **Yield farming** — depositar cripto EN los protocolos para ganar rendimiento (intereses,
   comisiones de trading, recompensas en tokens).

## Tokens DeFi como activo de trading

Son altcoins mid cap con un extra de complejidad: su valor depende de que el protocolo capture
ingresos Y de que el token tenga derecho real sobre esos ingresos (muchos no lo tienen — son
"gobernanza" sin flujo). Para el bot aplican las mismas reglas de los módulos 123 y 126: casi
ninguno pasa el filtro de liquidez/correlación, y su historia de velas está llena de eventos
idiosincráticos (hackeos, cambios de tokenomics) que el análisis técnico no puede anticipar.

## Yield farming: de dónde sale el rendimiento (pregunta obligatoria)

Todo yield tiene una fuente. Si no puedes nombrarla, la fuente eres tú.

| Fuente del yield | Qué tan real es |
|---|---|
| Intereses de prestatarios reales | Real, pero bajo (parecido a tasas de mercado) |
| Comisiones de trading del pool | Real, pero compite con el **impermanent loss** (pérdida frente a simplemente holdear cuando los precios de los dos activos del pool divergen) |
| Recompensas en el token del protocolo | Inflación: te pagan imprimiendo un token que se diluye; el APY alto de hoy suele ser el gráfico en caída de mañana |
| "APY 80% garantizado" | Esquema. Sin excepciones que valga la pena buscar |

## Los riesgos que no aparecen en el APY

- **Riesgo de smart contract**: un bug y los fondos desaparecen. Los hackeos de protocolos DeFi
  han costado miles de millones de dólares acumulados (casos concretos, verificar al día). La
  auditoría reduce el riesgo, no lo elimina.
- **Rug pull**: los creadores drenan la liquidez y desaparecen. Endémico en protocolos nuevos
  con APYs llamativos.
- **Riesgo de depeg y de colateral** (módulo 124), **riesgo de oráculo** (el protocolo lee un
  precio manipulado y liquida mal), **riesgo regulatorio**.
- **Complejidad compuesta**: farms sobre farms sobre stablecoins algorítmicas — cada capa
  multiplica los puntos de falla. UST/Anchor (un "yield estable" de ~20%) fue exactamente esto.

## La frontera del bot: CEX spot, punto

El AGENTE TRADING opera en un **CEX** (exchange centralizado, Binance) comprando y vendiendo
**spot** (el activo real, sin apalancamiento, sin préstamos, sin depósitos en protocolos). Esa
frontera es de diseño:

- El riesgo del bot es UNO y medible: el precio del par. Nada de riesgo de contrato, de rug,
  de oráculo ni de impermanent loss.
- La liquidez y los costos son observables y modelables (módulo 07).
- El sistema se audita con velas y trades — no con la seguridad de contratos ajenos.

## Cómo aplica al AGENTE TRADING

- El bot NO deposita en protocolos, NO farmea yield, NO opera tokens DeFi. Su universo es spot
  en Binance sobre pares que pasen el módulo 126.
- Si algún día hay caja ociosa en stablecoins y se evalúa "ponerla a rendir", eso es una decisión
  de tesorería SEPARADA del sistema de trading, con su propio análisis de riesgo — y con la
  pregunta obligatoria de este módulo: ¿de dónde sale el yield?
