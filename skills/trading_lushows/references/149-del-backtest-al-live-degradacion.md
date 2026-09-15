# 149 — Del backtest al live: la degradación

## La ley empírica

**Todo sistema rinde menos en vivo que en backtest y en paper.** No es pesimismo: es una
regularidad tan consistente que conviene tratarla como ley. Un plan que no la incorpora no es un
plan — es la versión optimista de uno.

## Por qué se degrada (las cinco fuentes)

### 1. Sobreajuste (overfitting)

El backtest se construyó MIRANDO el pasado. Aunque nadie haga trampa a propósito, cada decisión
de diseño (qué indicador, qué umbral, qué stop) se tomó sabiendo qué funcionó. Parte del
resultado es edge real y parte es ruido memorizado — y el ruido no se repite en vivo. Es la
fuente más grande de degradación (cómo detectarla: módulo 146).

### 2. Costos reales > costos modelados

El modelo asume comisión + slippage fijos (módulo 07). En vivo, el slippage es peor justo en los
momentos importantes: velas rápidas, stops ejecutándose, spread abriéndose. El peaje real
promedio casi siempre supera al modelado.

### 3. Fricciones de ejecución

Fills parciales, latencia, API caída, rate limits, órdenes rechazadas, reinicios. Cada fricción
es pequeña; la suma es un impuesto permanente que ni el backtest ni el paper pagan (módulo 147).

### 4. El mercado cambia

El backtest midió un edge en el mercado de AYER. Los regímenes rotan, la volatilidad cambia, los
patrones que otros también explotan se van agotando. El edge en vivo opera sobre un mercado que
ya no es exactamente el medido.

### 5. Interferencia humana

La fuente más evitable y más común: apagar el bot en drawdown, "ayudarle" saltándose señales,
subir el riesgo tras una racha buena. Cada intervención convierte el sistema medido en otro
sistema — uno sin backtest. Con dinero real, la tentación se multiplica (módulo 147).

## La regla práctica: descontar 30-50% del PF

Esperar en vivo un **PF entre 30% y 50% menor** (medido sobre el exceso por encima de 1, que es
donde vive la ganancia) que el del backtest/paper. Tabla de referencia — verificación exacta de
cada caso con `Matematicas_lushows`:

| PF en backtest/paper | PF esperable en vivo (desc. 30-50% del exceso sobre 1) | ¿Sobrevive? |
|---|---|---|
| 1.1 | ~1.03 – 1.07 | No: era humo con margen cero |
| 1.3 | ~1.15 – 1.21 | Apenas: rentable pero frágil |
| 1.5 | ~1.25 – 1.35 | Sí: hay colchón real |
| 2.0 | ~1.5 – 1.7 | Sí — y sospechar overfitting: verificar con módulo 146 |

Dos lecturas: (a) el sistema debe ser rentable DESPUÉS del descuento, no antes; (b) un backtest
demasiado bueno no es motivo de celebración sino de auditoría — los PF estratosféricos casi
siempre son sobreajuste, no genialidad.

Lo mismo aplica al drawdown, en la otra dirección: esperar en vivo un DD peor que el observado
en paper (el Monte Carlo del módulo 145 pone números a "cuánto peor").

## Cómo aplica al AGENTE TRADING

- El criterio de go-live (PF > 1.3 con ≥30 trades) es exactamente esta regla hecha política:
  1.3 en paper deja un sistema en vivo esperable de ~1.15-1.2 — vivo, pero justo. Si al examen
  del 22-ago-2026 el paper llega a 1.3 raspando, considerar seguir en paper hasta 1.4-1.5.
- La etapa testnet y el "live chico" del ciclo (módulo 00) existen para pagar las fuentes 2 y 3
  con dinero mínimo: medir el slippage REAL del bot y compararlo contra el modelado antes de
  poner capital que duela.
- La fuente 5 se combate con reglas escritas ANTES del go-live: qué drawdown apaga el bot
  (módulo 145), qué NO se toca en caliente, y que todo cambio pase por A/B (módulo 148). Lo que
  no está escrito antes, se negocia con el miedo después — y el miedo negocia mal.
