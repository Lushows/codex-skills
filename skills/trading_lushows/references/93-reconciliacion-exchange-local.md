# 93 — Reconciliación exchange↔local (el exchange MANDA)

> En paper, el JSON local es la única verdad. En live hay DOS verdades: lo que cree el bot
> (JSON en disco) y lo que dice Binance (la realidad). Cuando difieren, **gana el exchange,
> siempre**. Reconciliar = comparar ambas y corregir el local.

## ¿Por qué pueden divergir?

Render se puede caer, la red se puede cortar, el proceso puede morir a mitad de una operación.
Ejemplos reales que van a pasar tarde o temprano:

| Escenario | Qué queda mal |
|---|---|
| Bot envía orden, Render muere ANTES de recibir la respuesta | El exchange ejecutó; el local no lo sabe |
| El OCO se dispara (stop o target) mientras el bot está caído | Posición cerrada en Binance; abierta en el JSON |
| Orden rechazada por un filtro, pero el bot la marcó enviada | Local cree tener posición que no existe |
| Fill parcial (compró 0.8 de 1.0 pedido) | Cantidad local ≠ cantidad real |

## El reconciliador: qué hace al arrancar

Antes de tomar CUALQUIER decisión de trading, `reconciler.js` (previsto en módulo 09):

1. Pide a Binance: saldos reales, órdenes abiertas, historial reciente de órdenes/fills.
2. Compara con `data/*.json` local: posiciones abiertas, órdenes pendientes.
3. Por cada diferencia, corrige el LOCAL para reflejar al exchange (nunca al revés).
4. Escribe en el log qué corrigió y por qué, y notifica a Luis si hubo divergencias.
5. Solo entonces habilita el trading. **Si la reconciliación falla, el bot NO opera** — arranca
   en modo solo-lectura y avisa.

## Huérfanos: el caso que más duele

Un **huérfano** es una ejecución que ocurrió en el exchange y el bot no registró. El clásico:
el bot manda una orden MARKET, se cae antes de la respuesta, reinicia y "no recuerda" haberla
mandado. Si vuelve a evaluar la señal, puede COMPRAR DOBLE.

Defensas (las tres, no una):
- **clientOrderId propio**: cada orden lleva un ID generado por el bot ANTES de enviarla y
  guardado en disco ANTES del envío. Al reiniciar, se consulta al exchange por ese ID: se sabe
  con certeza si la orden llegó o no.
- **Reconciliar antes de operar** (el paso 5 de arriba).
- **Regla de una posición**: si el exchange muestra saldo del activo que el local no explica,
  bloquear nuevas entradas en ese símbolo hasta que Luis revise.

## Divergencias en caliente (no solo al arrancar)

Reconciliación periódica ligera (ej. cada ciclo de decisión): verificar que las órdenes OCO
que el local cree vivas siguen vivas en el exchange. Si un OCO desapareció (cancelado a mano,
ejecutado, expirado), el bot debe enterarse en minutos, no en horas — una posición sin stop
en el exchange es una emergencia (módulo 94).

## Cómo aplica al AGENTE TRADING

- Es componente obligatorio de Fase 8 (`src/liveTrading/reconciler.js`, módulo 09) y se prueba
  en testnet matando el proceso a propósito a mitad de orden (módulo 90, semana 2).
- El principio ya existe en espíritu: en paper el watcher vigila en memoria; en live los stops
  viven en el exchange y el local es solo un espejo que hay que mantener limpio.
- Checklist go-live (módulo 99): "reiniciar el bot con posición abierta en testnet y verificar
  que la recupera exacta" es prueba obligatoria.
