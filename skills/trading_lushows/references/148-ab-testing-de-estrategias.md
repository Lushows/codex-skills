# 148 — A/B testing de estrategias

## El problema que resuelve

Cada vez que se cambia algo del bot (el prompt de análisis, una regla, un filtro, un parámetro),
nace la misma pregunta: ¿la versión nueva es MEJOR, o solo tuvo mejor suerte? Cambiar sin medir
es la forma elegante de dar vueltas en círculos: se acumulan cambios "que se sintieron bien" y
nadie sabe cuál ayudó, cuál estorbó y cuál no hizo nada.

**A/B testing** = comparar la versión vieja (A) y la nueva (B) bajo condiciones lo más iguales
posibles, con suficientes trades, y dejar que los datos decidan.

## Regla de oro: UN cambio a la vez

Si se cambia el prompt Y el stop Y se agrega un filtro, y el PF mejora... ¿cuál de los tres fue?
Imposible saberlo — y peor: uno pudo ayudar mucho y otro restar. Cada versión del bot debe
diferir de la anterior en UNA cosa nombrable. Es más lento y es la única forma de aprender de
verdad. (Es el mismo principio del pilar 4, módulo 00: el sistema aprende de su historia solo si
la historia es interpretable.)

## Cómo comparar honestamente (en un bot secuencial)

El A/B clásico (mitad de usuarios ve A, mitad ve B, al mismo tiempo) no aplica directo: el bot
opera una línea de tiempo. Opciones, de mejor a peor:

1. **En paralelo sobre las mismas velas (ideal).** Correr A y B como dos instancias de paper
   simultáneas sobre el mismo mercado. Mismas condiciones exactas, comparación limpia. Es la
   gran ventaja de estar en paper: duplicar bots es gratis.
2. **Períodos alternados.** Una semana A, una semana B, varias rondas. Aceptable, pero el
   mercado de la semana de B pudo ser más fácil — por eso se alterna varias veces, nunca "un
   mes A y luego un mes B".
3. **Backtest de B sobre la historia + paper.** Útil como filtro previo (si B pierde en
   backtest, ni se prueba), pero no reemplaza verla operar en tiempo real.

Lo que NO es un A/B test: "cambié el prompt el martes y desde entonces va mejor" (3 trades).

## Muestra mínima y significancia

- Con menos de ~30 trades POR VERSIÓN, la diferencia observada es casi siempre ruido. Que B
  lleve PF 1.4 en 8 trades contra PF 0.9 de A no dice nada todavía.
- **Significancia estadística** = qué tan improbable es que la diferencia observada sea pura
  suerte. El cálculo (test sobre las distribuciones de R de cada versión, o bootstrap de la
  diferencia) se ejecuta SIEMPRE con `Matematicas_lushows` — nunca "a ojo se ve que B es mejor".
- Honestidad previa: definir ANTES del test qué métrica decide (PF, expectancy en R, DD) y
  cuántos trades se esperarán. Elegir la métrica después de ver los datos es hacer trampa
  sin darse cuenta.

## Qué hacer con el resultado

| Resultado | Acción |
|---|---|
| B mejor, con muestra y significancia | B se vuelve la nueva A; se registra el cambio y su evidencia |
| Diferencia no significativa | Se queda A (la versión vigente tiene el beneficio de la duda); B a la lista de ideas |
| B peor | Se descarta B y se ANOTA por qué se creyó que funcionaría — ese error enseña |

## Cómo aplica al AGENTE TRADING

- Con PF 0.89 en 10 trades, la tentación es cambiar cinco cosas ya. Disciplina: diagnosticar
  primero (¿dónde pierde? ¿stops barridos? ¿salidas tempranas?), proponer UN cambio, y probarlo
  contra la versión actual — idealmente como segunda instancia de paper en paralelo.
- Cada versión del bot merece nombre y fecha (v1, v2...) y su registro de trades separado; sin
  eso, el A/B es imposible retroactivamente.
- El proyecto GASTROWHATS ya usa A/B de prompts (`src/abTest.js`): el concepto es el mismo,
  aplicado a decisiones de trading. La significancia, siempre vía `Matematicas_lushows`.
