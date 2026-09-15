# 67 — Wicks, stop-hunts y microtrampas

## Vocabulario primero

- **Wick (mecha)**: la línea fina de una vela — el precio llegó hasta ahí y se devolvió
  antes del cierre. Una mecha larga = alguien empujó el precio y el mercado lo rechazó.
- **Stop-hunt (caza de stops)**: movimiento que perfora un nivel donde se acumulan stops,
  los ejecuta, y se revierte de inmediato. Los cazados venden abajo y ven el precio volver.
- **Liquidity grab / sweep**: el nombre fino de lo mismo — "barrer la liquidez" que descansa
  bajo un soporte o sobre una resistencia.

## Por qué los stops en niveles obvios se cazan

No hace falta conspiración; es mecánica de mercado:

1. Los stops se acumulan en lugares **predecibles**: justo bajo el mínimo reciente, bajo el
   soporte "de libro", en números redondos ($60.000, $100.000).
2. Un stop de venta ejecutado ES una orden de venta a market: una zona cargada de stops es
   **liquidez garantizada** — combustible.
3. A un jugador grande que quiere comprar barato le conviene empujar el precio hasta esa
   zona: los stops le venden en cascada, él compra el lote, y el precio rebota. En pares con
   libro delgado o en horas ilíquidas (`64`), el empujón cuesta poco.
4. Resultado en el gráfico: la clásica **mecha larga que perfora el soporte y cierra de
   vuelta arriba**. El nivel "aguantó", pero los stops obvios ya no están.

Honestidad: no toda mecha es una cacería — la mayoría es volatilidad normal, noticias o
libro delgado. El punto no es ver manipuladores en cada vela; es aceptar que **poner el
stop en el lugar más obvio del gráfico es regalar la posición al ruido**.

## La defensa (la parte accionable)

| Defensa | Cómo funciona |
|---|---|
| **Stop por volatilidad (ATR)** | Distancia según cuánto se mueve el activo de verdad (ATR = rango promedio de las velas), no según el nivel bonito. Queda fuera del alcance del ruido típico |
| **Colchón bajo el nivel** | Si es bajo el soporte, más allá de donde los pondría todo el mundo |
| **Tamaño prudente** | Stop más lejos = posición más chica para arriesgar el mismo 1.5%. El tamaño se calcula DESDE el stop, nunca al revés |
| **Sin re-entrada emocional** | Si el stop salta y el precio se revierte, la re-entrada requiere señal nueva completa — no revancha |
| **Horas líquidas** | En desierto de liquidez la cacería es más barata; ver `64` y `69` |

Lo que NO es defensa: operar sin stop "para que no me cacen". Eso cambia una pérdida de 1R
por la posibilidad de una pérdida ilimitada. Ser cazado a veces es un costo del negocio;
estar desnudo ante un crash no tiene precio de recuperación (`07`, tabla de recuperación).

## Cómo aplica al AGENTE TRADING

- El bot ya dimensiona posiciones desde el stop con riesgo fijo 1.5% — la mitad de la
  defensa está de fábrica. La otra mitad: asegurar que el stop se calcule **por ATR/estructura
  con colchón**, no en el mínimo exacto de la última vela.
- BTC y ETH, siendo los pares más profundos, son los MENOS cazables del mercado — otra
  dividendo de la elección de universo (`62`, `68`). Aun así, madrugadas y findes elevan el riesgo.
- Métrica reveladora para el diario del bot: cuántos stops saltaron por mecha **y el precio
  cerró de vuelta sobre el nivel en 1-3 velas**. Si es frecuente, los stops están demasiado
  ceñidos u obvios — dato, no intuición.
