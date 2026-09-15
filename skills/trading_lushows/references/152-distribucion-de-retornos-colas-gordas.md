# 152 — Distribución de retornos: colas gordas

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## La campana que no es

La **distribución normal** (la "campana de Gauss") es el modelo cómodo: la mayoría de los retornos
cerca del promedio, los extremos casi imposibles. Bajo una normal, un movimiento de 5 desviaciones
estándar ocurriría una vez cada ~14.000 años de días hábiles.

**Los retornos cripto no son normales.** BTC ha tenido caídas diarias de −30% o más varias veces
en su historia. Bajo el modelo normal esos días "no deberían existir". Existen.

## Colas gordas y curtosis

- **Cola** de una distribución = la zona de los eventos extremos (muy lejos del promedio).
- **Colas gordas** (fat tails) = los extremos ocurren MUCHO más seguido de lo que predice la normal.
- **Curtosis** = el número que mide qué tan gordas son las colas. La normal tiene curtosis 3
  (exceso 0). Los retornos diarios de BTC suelen mostrar curtosis de dos dígitos: los días
  extremos son la regla del juego, no la excepción.

| Modelo | "Día de −10%" en BTC | Realidad |
|---|---|---|
| Normal (vol diaria ~4%) | Rarísimo (evento de 2.5σ, pero los de 5σ+ "imposibles") | Pasa varias veces por año en mercados feos |

## Por qué el "evento imposible" siempre llega

1. **Apalancamiento en cascada**: liquidaciones forzadas venden, lo que baja el precio, lo que
   liquida a más gente. El mercado se retroalimenta — la normal asume que no.
2. **Liquidez que desaparece**: en pánico, los compradores se van justo cuando más se necesitan;
   el precio salta huecos (gaps) en vez de moverse suave.
3. **Correlación que sube en crisis**: todo cae junto (módulo 157), así que "diversificado" no
   amortigua.

Conclusión práctica: cualquier cálculo que asuma normalidad (VaR normal, Sharpe leído ingenuamente)
**subestima el riesgo real** en cripto.

## Implicaciones para el sizing

- El stop-loss limita la pérdida **si el precio pasa por ahí**. En un gap o flash crash, la
  ejecución real puede ser bastante peor que el stop (slippage extremo).
- Por eso el riesgo por trade debe calcularse asumiendo que a veces perderás **más de 1R**:
  un techo conservador (1-2%) deja margen para que un evento de cola no sea letal.
- Nunca dimensionar como si la pérdida máxima posible fuera el stop teórico.

## Cómo aplica al AGENTE TRADING

- El techo de 1.5% de riesgo por trade y máximo 2 posiciones está pensado para sobrevivir colas
  gordas: incluso si un flash crash duplica la pérdida esperada en ambas posiciones, el golpe
  queda en un dígito bajo del capital.
- En paper trading el slippage modelado (5 bps) es un promedio de días tranquilos; en un evento
  de cola real sería mucho mayor. El paper es **optimista por diseño** en los extremos.
- Para la fase live: stops como órdenes OCO en el exchange (módulo 164) mitigan, pero no eliminan,
  el riesgo de gap.
