# 180 — Druckenmiller a fondo: el padre intelectual del bot

## Quién es

Stanley Druckenmiller es considerado uno de los mejores gestores macro de la historia. Fundó
**Duquesne Capital Management** en 1981 y la manejó hasta cerrarla en 2010, con un historial
famoso por dos cosas: retornos altos sostenidos durante décadas y **ningún año perdedor** en
Duquesne — un récord de consistencia casi único. Además fue la mano derecha de George Soros en
el Quantum Fund entre finales de los 80 y 2000.

"Macro" significa que opera sobre las fuerzas grandes — tasas de interés, bancos centrales,
divisas, liquidez — y luego elige el instrumento. El activo es el vehículo; la tesis es el motor.

## El trade de la libra (1992)

El episodio más citado: la libra esterlina estaba atada al sistema monetario europeo a un nivel
que la economía británica no aguantaba. El análisis central del trade contra la libra fue de
Druckenmiller dentro del Quantum Fund; la lección famosa vino de Soros, que al ver la convicción
de la tesis empujó a apostar mucho más grande ("go for the jugular" — ve a la yugular). El Banco
de Inglaterra tuvo que dejar caer la libra ("Miércoles Negro", septiembre 1992) y el fondo ganó
en torno a mil millones de dólares (cifra ampliamente citada; el número exacto varía por fuente).

La lección NO es "apuesta enorme siempre": es la asimetría — **cuando tienes razón con convicción
máxima, el tamaño hace la carrera; cuando no la tienes, el tamaño te la quita.**

## Los principios (los que gobiernan al bot)

1. **Concentración con convicción, no diversificación tibia.** Pocas apuestas grandes cuando
   todo se alinea; nada cuando no. "Ponen los huevos en una canasta y vigilan la canasta."
2. **Preservar capital primero.** Su récord no viene de años espectaculares sino de **no tener
   años malos**. La defensa compone más que el ataque.
3. **El macro manda.** La liquidez y el régimen mueven a todos los activos; pelear contra el
   régimen con un "buen setup" es perder con estilo.
4. **En racha mala, reducir; jamás promediar abajo.** Cuando algo va mal, el tamaño baja hasta
   recuperar claridad.
5. **Estar dispuesto a cambiar de opinión rápido.** La convicción es sobre la evidencia actual,
   no un matrimonio con la posición.

## Cómo el bot implementa cada principio

| Principio Druckenmiller | Implementación en el bot |
|---|---|
| Convicción concentrada | Score 1-10; BUY solo ≥6; **auto-ejecución solo ≥8** (`AUTO_EXECUTE_THRESHOLD`) — la mayoría de los análisis terminan en HOLD, por diseño |
| Preservar capital | Riesgo máx 1.5% por trade, máximo 2 posiciones simultáneas |
| Macro primero | `macroRegime` (Haiku) corre ANTES que el análisis del activo; contra régimen no hay BUY |
| Reducir en racha mala | `tradingPsychology`: cooldown 4h tras 3 pérdidas seguidas; bloqueo >5 trades/24h |
| Aprender del historial | `traderMemory` inyecta lecciones de setups similares filtradas por régimen |

## La parte que el bot NO puede copiar (honesto)

Druckenmiller apalancaba las apuestas de máxima convicción muy por encima del capital — con
décadas de oficio detrás. El bot deliberadamente **no** hace eso: el umbral 8 concentra la
*selección*, pero el sizing sigue capado a 1.5% de riesgo. Es Druckenmiller en la filosofía de
cuándo actuar, con humildad de novato en cuánto arriesgar. Esa combinación es intencional y no
debe "mejorarse" subiendo el riesgo antes de años de track record.

## Cómo aplica al AGENTE TRADING

Es el system prompt del skill de convicción (`druckenmiller.js`) hecho persona. Cuando el bot
pasa semanas sin operar en un régimen malo, eso no es un bug: es el principio 3 más el 1.
La vara para evaluarlo también es druckenmilleriana: primero medir los años sin pérdidas grandes,
después las ganancias.
