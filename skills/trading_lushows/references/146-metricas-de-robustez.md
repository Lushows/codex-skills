# 146 — Métricas de robustez

## Qué es la robustez

Un sistema es **robusto** cuando su edge no depende de una casualidad: sobrevive a pequeños
cambios en sus parámetros, en los costos y en el período que se mire. Lo contrario es un sistema
**sobreajustado** (*overfitted*): afinado tan al milímetro a los datos del pasado que en realidad
memorizó ruido — y el ruido no se repite. Un PF alto y frágil vale menos que un PF modesto y
robusto.

## Las 4 pruebas de robustez

### 1. Estabilidad de parámetros

Mover cada parámetro del sistema (stop, objetivo, filtros, umbrales) un poco arriba y abajo, y
ver qué pasa con el resultado.

- Robusto: el PF se degrada suave y gradualmente (una "meseta" de parámetros buenos).
- Frágil: el PF colapsa con un cambio pequeño (un "pico" solitario = casi seguro sobreajuste).

Regla práctica: elegir parámetros en el CENTRO de la meseta, nunca en el pico exacto del
backtest. El pico es la versión más optimista del pasado, no la más probable del futuro.

### 2. PF por sub-período

Partir la historia en tramos (por trimestre, o por régimen: alcista / bajista / lateral) y
calcular el PF de cada tramo.

- Robusto: PF > 1 en la mayoría de tramos, aunque ninguno sea espectacular.
- Frágil: todo el edge vive en UN tramo afortunado y el resto pierde. Ese sistema no tiene
  edge; tuvo un buen trimestre.

### 3. Sensibilidad a costos

Recalcular el resultado con costos peores que los modelados (por ejemplo, +50% y +100% de
slippage). Un sistema cuyo PF pasa de 1.4 a 0.9 al duplicar el slippage no tiene edge: tiene una
suposición optimista de costos. Los sistemas de alta frecuencia de señales son los más frágiles
aquí — cada trade paga peaje (módulo 07). Cálculos → `Matematicas_lushows`.

### 4. Degradación esperada paper→live

El paper es la versión amable de la realidad (qué valida y qué no: módulo 147; cuánto esperar de
degradación: módulo 149). La prueba aquí es de humildad: preguntarse "si en vivo rinde 30-50%
menos, ¿sigue valiendo la pena?". Si el sistema solo es viable con sus números de paper intactos,
no es viable.

## Tabla resumen

| Prueba | Pregunta que responde | Señal de fragilidad |
|---|---|---|
| Estabilidad de parámetros | ¿El edge es una meseta o un pico? | Colapso ante cambios pequeños |
| PF por sub-período | ¿Gana en varios regímenes? | Todo el edge en un solo tramo |
| Sensibilidad a costos | ¿Sobrevive a costos reales peores? | PF < 1 con slippage ×2 |
| Degradación paper→live | ¿Aguanta el descuento de realidad? | Solo viable con números de paper |

## Cómo aplica al AGENTE TRADING

- Estas pruebas corren sobre las velas ya guardadas en JSON: es análisis, no infraestructura
  nueva. Todas las corridas y comparaciones, ejecutadas con `Matematicas_lushows`.
- El criterio de go-live (PF > 1.3, DD < 15%, ≥30 trades) mide desempeño; este módulo mide si
  ese desempeño es CONFIABLE. Un PF 1.35 que muere con slippage ×1.5 no debería pasar el examen
  del 22-ago-2026 aunque cumpla la cifra.
- Dato actual que ya habla de robustez: 10/10 trades en ETH y 0 en BTC. Antes de agregar SOL,
  entender POR QUÉ la estrategia no dispara en BTC — puede ser un filtro sano o un sesgo del
  sistema hacia un solo régimen (prueba 2).
