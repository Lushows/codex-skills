# 161 — WebSockets robustos: mantener viva la línea con Binance

## Qué es un WebSocket (en simple)

HTTP normal es como mandar cartas: pides, te responden, se acabó. Un **WebSocket (WS)** es una
llamada telefónica que queda abierta: Binance empuja cada vela nueva al bot sin que este pregunte.
Es la fuente de datos del AGENTE TRADING (velas de 1h de BTCUSDT y ETHUSDT).

El problema: las llamadas se caen. Redes que parpadean, Binance que reinicia servidores, Render
que mueve el proceso. Un bot 24/7 debe asumir que la conexión **se va a caer muchas veces** y
recuperarse solo, sin humanos.

## Los 4 problemas clásicos y su solución

| Problema | Qué es | Solución del bot |
|---|---|---|
| Desconexión | El WS se cierra (evento `close` o `error`) | Reconexión automática con backoff exponencial |
| Tormenta de reconexión | Reintentar cada 100ms machaca al servidor y te banean | Backoff: esperar 1s, 2s, 4s, 8s... con tope máximo |
| Conexión zombie | El socket "parece" abierto pero ya no llega nada | Heartbeat: si no llegan datos en N minutos, matar y reconectar |
| Velas perdidas | Mientras estuviste caído, pasaron velas | Al reconectar, pedir por REST las velas que faltan y rellenar |

## Backoff exponencial (el patrón clave)

"Backoff exponencial" = cada reintento espera el doble que el anterior. Evita dos males:
martillar al servidor (que puede responder baneando tu IP) y quedarse esperando demasiado.
Siempre con un **tope** (p. ej. 60s) para que una caída larga no lleve la espera a horas,
y con **reset**: cuando la conexión vuelve a funcionar, el contador de intentos vuelve a cero.

## La conexión zombie: el enemigo silencioso

Es el peor caso porque **no lanza error**. El TCP quedó colgado en algún router intermedio y el
proceso cree que está conectado, pero llevan 40 minutos sin llegar velas. Un bot ingenuo se queda
"operando" con datos viejos. La defensa es un vigilante de frescura: si la última vela recibida
tiene más edad de la esperada (para velas 1h, unos pocos minutos tras el cierre de cada vela),
se fuerza el cierre del socket y se reconecta. Binance además envía pings de protocolo; hay que
responderlos o el servidor te corta.

## Rellenar huecos (gap filling)

Reconectarse no basta: si estuviste caído 3 horas, te faltan 3 velas. El bot compara el timestamp
de la última vela guardada con la hora actual y pide por **REST** (el mirror
`data-api.binance.vision`) las velas del hueco antes de seguir. Sin esto, los indicadores
(RSI, MACD, SMA) se calculan sobre una serie con agujeros y mienten.

## Cómo aplica al AGENTE TRADING

`src/binance/` implementa exactamente esta receta: reconexión con backoff exponencial, control de
frescura contra zombies, y relleno de velas por REST al volver. Resultado medible: 44 días de
uptime con las caídas de red que hayan ocurrido en el camino, sin intervención manual. Para la
Fase 8 (live) la regla se endurece: si el WS lleva demasiado caído **y hay posición abierta**,
eso es una alerta crítica — por eso los stops deben vivir en el exchange (OCO), no en el bot.
