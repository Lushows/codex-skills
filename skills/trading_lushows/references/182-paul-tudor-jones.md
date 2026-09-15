# 182 — Paul Tudor Jones: la defensa como identidad

## Quién es

Paul Tudor Jones II (PTJ) fundó **Tudor Investment Corporation** en 1980 y es uno de los macro
traders más respetados de la historia. Su fama mundial viene del **crash de octubre de 1987**
("Lunes Negro", el Dow cayó ~22% en un día): anticipó el desplome —comparando la estructura del
mercado con la de 1929— y su fondo tuvo un retorno enorme ese mes mientras el mundo se
incendiaba (se citan cifras alrededor del +60% en octubre y ~triple dígito en el año; los números
exactos varían por fuente). El documental *Trader* (1987) lo muestra en plena preparación de esa
jugada.

En años recientes también es conocido por haber destinado parte de su portafolio a Bitcoin como
cobertura ante la inflación (lo comparó con invertir temprano en un activo naciente).

## Su filosofía: defensa ante todo

PTJ se define por el ataque evitado, no por el golpe dado. Sus ideas más citadas:

- *"La regla más importante es jugar una gran defensa, no un gran ataque."*
- *"No promedies perdedores"* — la nota **"Losers average losers"** (los perdedores promedian
  posiciones perdedoras) que tenía pegada a la vista es probablemente el post-it más famoso del
  trading. Promediar abajo = comprar más de algo que te está demostrando que te equivocaste.
- **Asimetría 5:1** — busca trades donde lo que puedes ganar sea unas cinco veces lo que
  arriesgas. Con esa asimetría puedes equivocarte la mayoría de las veces y aun así ganar:
  la rentabilidad viene de la geometría del trade, no de adivinar bien seguido.
- Decidir el punto de salida **antes** de entrar, y asumir que cada posición puede estar
  equivocada ("todos los días asumo que todo lo que tengo está mal").

## La matemática del 5:1 (por qué funciona)

| Si aciertas... | Con R:R 5:1 tu resultado es |
|---|---|
| 20% de las veces | Aproximadamente empate (1×5 − 4×1 = +1 por cada 5 trades, antes de costos) |
| 30% de las veces | Claramente positivo |
| 50% de las veces | Excelente |

El mensaje: con buena asimetría **no necesitas tener razón seguido**. Lo que te mata es lo
inverso: arriesgar 5 para ganar 1, donde un solo error borra cinco aciertos.

## Su regla en el bot: no promediar abajo

La wisdom library inyecta a PTJ **cuando el R:R propuesto es débil** — el momento exacto donde
un trade tibio tienta. Y su regla estrella está cableada en la filosofía base (principio 4 del
skill Druckenmiller): una racha mala pide REDUCIR tamaño, **jamás promediar abajo**. El bot,
por diseño, no tiene ninguna rutina de "recomprar más barato para bajar el promedio": si el
precio va contra la posición, el camino es el stop, no la esperanza.

Complementos ya implementados que son PTJ puro: el stop se calcula **antes** de entrar (sale de
`positionSizing`, no de la angustia del momento) y el sizing parte de "cuánto pierdo si me
equivoco" (1.5% máx), no de "cuánto gano si acierto".

## Cómo aplica al AGENTE TRADING

PTJ es el auditor de calidad de cada trade del bot: ¿el ratio recompensa/riesgo justifica entrar?
¿El stop existe antes que la orden? ¿Hay algún mecanismo promediando perdedores? (no debe
haberlo jamás, ni en live). Cuando se evalúe el desempeño del bot, mirar primero la métrica PTJ:
el tamaño de las pérdidas individuales frente al de las ganancias — la defensa se mide ahí,
no en el win rate.
