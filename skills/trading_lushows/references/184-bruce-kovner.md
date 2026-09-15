# 184 — Bruce Kovner: el tamaño de la posición es (casi) todo

## Quién es

Bruce Kovner fundó **Caxton Associates** (1983), uno de los macro hedge funds más exitosos y
longevos, y lo dirigió hasta retirarse en 2011. Su historia de origen es famosa: siendo taxista
en Nueva York, hizo su primer trade a fines de los 70 con dinero prestado de una tarjeta de
crédito — le fue bien al inicio, luego vio evaporarse buena parte de la ganancia por no saber
salir, y esa primera montaña rusa le enseñó de golpe la lección que definiría su carrera:
el problema no era el análisis, era el **tamaño**. Su entrevista en *Market Wizards* es una de
las más citadas de la historia del trading.

## Idea 1: el sizing es el 90%

Kovner sostiene que la gestión del riesgo y del tamaño de posición importa más que la selección
del trade. Su observación sobre los novatos (parafraseada de *Market Wizards*): los traders
principiantes operan **3 a 5 veces demasiado grande**, tomando riesgos de 5-10% por trade cuando
deberían arriesgar 1-2%. Con tamaño excesivo, hasta una buena estrategia muere: basta una racha
normal de pérdidas para un hueco del que no se vuelve.

| Riesgo por trade | 6 pérdidas seguidas te dejan en | ¿Sobrevivible? |
|---|---|---|
| 10% | ~53% del capital | Necesitas +88% solo para volver — casi nunca se vuelve |
| 5% | ~74% | Doloroso pero posible |
| 1.5% (el bot) | ~91% | Un mal mes, no una tragedia |

(La matemática es multiplicativa: perder 50% exige ganar 100% para recuperar. Por eso el tamaño
no es un detalle: define si existe un "después".)

## Idea 2: "Undertrade, undertrade, undertrade"

Su consejo textual más famoso: *sub-opera, sub-opera, sub-opera* — sea cual sea el tamaño que
crees correcto, **ponte la mitad**. No es timidez: es reconocer que todos (humanos y modelos)
sobreestimamos nuestra ventaja y subestimamos las rachas malas. El costo de ir demasiado chico
es ganar menos; el de ir demasiado grande es dejar de jugar. Asimetría obvia.

## Idea 3: el stop se decide ANTES de entrar

Kovner: sabe **dónde sale antes de entrar** — coloca el stop en el punto donde el mercado le
habría demostrado que su tesis era incorrecta (un nivel técnico con significado), no a un
porcentaje arbitrario del precio. Y de ahí se deriva el tamaño: primero el stop (dónde estaría
equivocado), luego el tamaño (cuánto puedo comprar para que ese stop cueste solo mi riesgo
permitido). **El orden importa**: stop → tamaño. Al revés (tamaño primero, stop donde alcance)
es la receta del novato.

## Cómo aplica al AGENTE TRADING

Kovner está cableado en `positionSizing.js`, que es JS puro a propósito — el tamaño **no lo
decide la IA ni la emoción**, lo decide aritmética: Kelly fraccional con techo duro de 1.5% de
riesgo por trade, máximo 2 posiciones. El orden kovneriano se respeta: el análisis propone el
stop, y de ese stop sale el notional — nunca al revés. La wisdom library lo inyecta cuando la
**volatilidad es alta**, el momento en que un tamaño "normal" se vuelve secretamente grande
(mismo notional, stop más lejano = más riesgo real).

Y "undertrade" es la respuesta oficial a la tentación que llegará con el go-live: "¿y si subimos
el riesgo a 3% para que crezca más rápido?" — No. El 1.5% ya es la mitad prudente de algo. Los
primeros meses en live, si acaso, la duda debería ir en la otra dirección.
