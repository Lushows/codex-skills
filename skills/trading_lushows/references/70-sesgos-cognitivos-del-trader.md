# 70 — Sesgos cognitivos del trader

Un **sesgo cognitivo** es un atajo mental que el cerebro usa para decidir rápido y que en trading
sale carísimo, porque el mercado castiga exactamente los errores que esos atajos producen.
No son defectos de gente tonta: son el equipamiento de serie de TODO cerebro humano, incluido
el de los traders profesionales. La diferencia es que los buenos los conocen y ponen reglas encima.

## Los 5 que más cuestan plata

| Sesgo | Qué es | Ejemplo en trading |
|---|---|---|
| **Confirmación** | Buscar solo información que apoye lo que ya crees | Estás LONG en BTC y solo lees analistas alcistas; ignoras que el RSI lleva 3 días divergiendo |
| **Anclaje** | Quedarte pegado al primer número que viste | "BTC estuvo en $100k, a $70k está regalado" — el precio pasado NO es valor; el mercado no te debe volver ahí |
| **Aversión a la pérdida** | Una pérdida duele ~2x más de lo que alegra una ganancia igual | Cierras ganadores a +2% ("aseguro") y aguantas perdedores a −15% ("ya rebota") — exactamente lo contrario de dejar correr ganancias y cortar pérdidas |
| **Recencia** | Sobrevalorar lo que pasó hace poco | Después de 2 semanas de subida crees que "esto solo sube" y entras sin stop; después de 3 rojas crees que "el sistema no sirve" |
| **Dunning-Kruger** | Cuanto menos sabes, más seguro te sientes | Ganar 4 trades en tu primer mes y concluir "esto es fácil, meto más plata" — no distingues suerte de habilidad hasta tener 100+ trades de muestra |

## Por qué no se curan con fuerza de voluntad

Los sesgos operan ANTES de que la parte racional del cerebro se entere. Decirte "no voy a tener
aversión a la pérdida" funciona igual que decirte "no voy a tener hambre". La única defensa
probada es **sacar la decisión del momento emocional**: reglas escritas en frío, checklists,
tamaños de posición fijos, y — la versión extrema — un sistema automático que decide por ti.

## El detalle incómodo: los sesgos también se programan

Un bot no siente, pero hereda los sesgos de quien escribió sus reglas y sus prompts. Si el prompt
no penaliza entradas en precio extendido, el bot exhibe FOMO estructural (ver módulo 71). Si el
dueño ajusta los parámetros después de cada racha, el sesgo de recencia entró por la puerta de atrás.

## Cómo aplica al AGENTE TRADING

- **Aversión a la pérdida / revenge**: cooldown de 4h tras 3 pérdidas seguidas (`tradingPsychology.js`).
- **Recencia**: el sizing es Kelly fraccional con techo 1.5% — no sube tras rachas ganadoras.
- **Confirmación**: el prompt de convicción exige razones EN CONTRA además de a favor.
- **Anclaje**: el análisis técnico se calcula en JS sobre datos actuales; Claude no recibe "el máximo histórico" como referencia de valor.
- **Dunning-Kruger (de Luis)**: la muestra manda — nada se concluye con menos de decenas de trades; el meta-análisis semanal mira proceso, no el P&L de ayer.
- Evidencia real: el FOMO programado (0/3 en entradas extendidas) demostró que los sesgos del diseño son tan caros como los humanos. Se corrigen con reglas, no con regaños.
