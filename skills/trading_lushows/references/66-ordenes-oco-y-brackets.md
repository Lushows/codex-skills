# 66 — Órdenes OCO y brackets

## Qué es una OCO

**OCO = One-Cancels-the-Other** ("una cancela a la otra"). Es un paquete de dos órdenes de
salida atadas entre sí, viviendo en el exchange:

1. **Take-profit**: una limit de venta en el precio objetivo (arriba).
2. **Stop-loss**: un stop (idealmente stop-market, ver `61`) en el precio de protección (abajo).

Si el precio toca el objetivo, se vende con ganancia y el stop se cancela solo. Si toca el
stop, se vende con pérdida controlada y el target se cancela solo. Nunca quedan las dos
vivas (que sería vender dos veces lo que solo se tiene una vez).

A la estructura completa entrada + stop + target se le llama **bracket** ("horquilla"): la
posición nace con sus dos salidas ya definidas. Binance spot soporta OCO de forma nativa
en su API.

## Por qué el watcher local NO basta (el argumento de la Fase 8)

Hoy en paper, el propio bot vigila stop y target por software (un "watcher": un proceso que
mira el precio y decide cerrar). En paper es inofensivo. En vivo es una bomba de tiempo,
porque el watcher muere con cualquiera de estos:

| Falla posible | ¿Probable? |
|---|---|
| Render reinicia el servicio (deploys, mantenimiento, free tier durmiendo) | Muy probable |
| Se cae la conexión o la API de Binance rechaza por rate limit | Probable |
| Bug del propio bot (excepción no manejada a las 3 a.m.) | Probable |
| Latencia: el watcher ve el precio tarde y ejecuta tarde | Constante |

Mientras el watcher está muerto, la posición queda **desnuda**: sin stop, expuesta a un
catalizador nocturno (`56`). Una sola noche mala sin stop puede costar más que meses de edge.

La OCO invierte la carga: la protección vive en la infraestructura de Binance, que opera
24/7 con redundancia de exchange. **El servidor del bot puede morirse tranquilo: el stop
sigue armado.** Por eso en live las OCO no son una mejora — son un requisito de entrada.

## Detalles de implementación que muerden

- **Precio de stop vs precio límite**: en la pata stop de una OCO spot de Binance se definen
  ambos; si se usa variante limit, dejar colchón suficiente para no quedarse sin llenar en
  una vela violenta (la trampa del `61`).
- **minNotional y redondeos**: cada par tiene mínimos de cantidad y decimales (tick size /
  step size); la OCO se rechaza si no se respetan — validar antes de enviar.
- **Mover el stop = cancelar y recrear la OCO** (no se edita en sitio). Hay una ventana de
  segundos sin protección: hacerlo poco y con reintentos.
- **Reconciliación**: al arrancar, el bot debe preguntarle al exchange qué órdenes y
  posiciones existen realmente, y ajustar su estado interno a esa verdad — no al revés.

## Cómo aplica al AGENTE TRADING

- Regla de oro de la Fase 8: **ninguna posición real existe sin su OCO confirmada por la
  API**. Si la OCO falla al crearse, se cierra la posición de inmediato — sin excepciones.
- Probar todo el ciclo (crear, tocar stop, tocar target, cancelar, reconciliar tras reinicio)
  en **testnet** antes del primer peso real.
- El watcher local no se elimina: queda como respaldo y como el que decide MOVER la OCO
  (trailing, break-even), pero la protección de base vive en Binance.
