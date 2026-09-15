# 24 — Trailing stops

**Trailing stop** = un stop loss que persigue al precio cuando este se mueve a favor, pero
nunca retrocede. En un LONG: si el precio sube, el stop sube con él (a una distancia fija);
si el precio baja, el stop se queda quieto y eventualmente lo toca — cerrando la posición
con la ganancia acumulada (o la pérdida limitada).

## Cómo funciona (ejemplo)

Compra a $100 con trailing del 3%:

| Precio llega a | Stop queda en | Qué pasa |
|---|---|---|
| $100 (entrada) | $97.00 | Stop inicial |
| $105 | $101.85 | Ganancia ya asegurada (+1.85%) |
| $112 | $108.64 | Persigue el máximo |
| Cae a $108.64 | — | Cierra con ~+8.6% |

La distancia puede ser un % fijo o un múltiplo de volatilidad/ATR (mejor: respira con el
mercado, igual que el stop inicial del módulo 22).

## Cuándo ayuda: tendencias largas

En una tendencia sostenida, el target fijo a 2R cobra $30 y se baja del tren; el trailing se
queda montado y puede cobrar 5R, 8R o más. Los sistemas seguidores de tendencia viven de
esto: muchos trades pequeños perdedores pagados por pocos ganadores enormes que solo el
trailing deja correr. Si el mercado tiende, el trailing convierte una salida buena en una
excelente.

## Cuándo mata: rangos

En un mercado lateral (**rango** = el precio rebota entre un techo y un piso sin dirección),
el trailing es una máquina de devolver plata: el precio sube un poco, el stop lo persigue,
el precio recae al rango y toca el stop — una y otra vez. Resultado típico: trades que iban
+1.5R terminan en +0.2R o en cero. El target fijo a 2R, en cambio, cobra en la parte alta
del rebote y listo.

No hay trailing "bueno" o "malo": hay trailing en el mercado correcto o incorrecto. Y como
nadie sabe con certeza si viene tendencia o rango, la distancia del trailing es el
compromiso: ceñido = asegura rápido pero lo sacan temprano; amplio = deja correr pero
devuelve más antes de cerrar.

## Variantes que valen la pena conocer

- **Trailing por ATR (chandelier)**: stop a N× ATR bajo el máximo alcanzado. El estándar serio.
- **Breakeven primero**: mover el stop a la entrada cuando el trade llega a +1R, y solo
  entonces activar el trailing. Elimina la posibilidad de que un ganador se vuelva perdedor.
- **Trailing por estructura**: subir el stop bajo cada nuevo mínimo relevante. Potente en
  manual, difícil de codificar bien.

## Cómo aplica al AGENTE TRADING

El bot HOY no usa trailing: sale por target fijo 2R o stop — correcto para la fase de
validación (datos limpios, módulo 23). El trailing es la **mejora candidata #1
post-validación**, con este diseño sugerido: breakeven en +1R, luego trailing por múltiplo
de volatilidad (coherente con el stop de entrada de 1.5× volatilidad). Requisitos antes de
activarlo: (1) los 30 trades del criterio go-live completos, (2) backtest comparando target
fijo vs trailing sobre el MISMO historial — números vía `Matematicas_lushows`, (3) decidir
con la expectativa medida, no con el recuerdo de "ese trade que siguió subiendo". Ojo:
BTC/ETH pasan más tiempo en rango que en tendencia; el trailing no es upgrade garantizado.
