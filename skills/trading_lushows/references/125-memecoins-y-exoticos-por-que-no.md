# 125 — Memecoins y exóticos: por qué NO

## Qué son

Una **memecoin** es un token cuyo único motor de precio es la atención: un chiste, un perro, una
celebridad, una tendencia de redes. Sin flujo de caja, sin uso, sin nada que valorar. Los
"exóticos" son sus primos: tokens nuevos de proyectos diminutos, tokens de nichos de moda,
cualquier cosa que se compra porque "está sonando".

Que DOGE haya hecho millonario a alguien alguna vez no cambia nada de lo que sigue. Los casinos
también tienen ganadores, y los publicitan por la misma razón.

## La matemática de la lotería

El argumento de venta siempre es el mismo: "solo necesitas que UNA haga 100x". Veamos qué exige
eso de verdad (estructura del cálculo; los números exactos, con `Matematicas_lushows`):

- Si compras tokens que pueden hacer 100x pero el 99%+ termina cerca de cero, tu expectancy
  depende por completo de acertar la probabilidad de éxito — que nadie conoce y que está
  sesgada en tu contra (ver exit liquidity abajo).
- Con probabilidad real de éxito del 0.5% y pago 100x, la expectancy es NEGATIVA
  (0.005 × 100 = 0.5 < 1): pierdes la mitad de lo apostado en promedio.
- Y aunque la expectancy fuera positiva, la **varianza** te mata antes: puedes atravesar cientos
  de fracasos seguidos antes del acierto. Un bot con riesgo 1.5% por trade no sobrevive a esa
  distribución, y un humano psicológicamente tampoco.

El swing trading sistemático es el juego opuesto: ventaja pequeña, repetida, sobre activos
líquidos. Lotería y sistema no se mezclan; uno contamina al otro.

## Exit liquidity: tú eres el producto

**Exit liquidity** = el comprador que le da salida al que compró antes y más barato. En una
memecoin, los primeros (creadores, insiders, bots de sniping) compran a precio casi cero. El
precio sube porque entran compradores tardíos — y esos compradores SON el plan de negocio. Cuando
llega el público general, los primeros venden. No hay conspiración que descubrir: es la mecánica
del activo. Si te enteraste por redes sociales, ya eres la fase final del embudo.

## "Me lo dijo un influencer" = la peor señal disponible

- Muchos cobran por promocionar tokens (a veces sin declararlo) o recibieron el token gratis
  antes de recomendarlo: su ganancia es tu compra, no la subida.
- Aunque sea honesto, su información llega tarde por definición: si ya es contenido masivo, el
  movimiento informado ya ocurrió.
- Regla dura: **una recomendación pública masiva de un token pequeño es señal de VENTA de
  atención, no de compra de activo.** No hay excepciones que valga la pena buscar.

## Cómo aplica al AGENTE TRADING

- El bot NO opera memecoins ni exóticos, en paper ni en live, nunca. No es filosofía: es que
  fallan cada criterio del módulo 126 (liquidez honesta, historia de velas, velas no manipuladas).
- Si Luis siente el impulso de "probar con un poquito" fuera del bot: ese impulso es exactamente
  lo que el módulo 00 llama impulso con excusas. Si aun así se hace, que sea con dinero de
  entretenimiento, jamás con el capital del sistema, y sabiendo que la expectancy es de casino.
- Ninguna señal externa (influencer, tendencia, grupo de Telegram) entra jamás al pipeline de
  decisión del bot. Las entradas son velas y reglas, punto.
