# 26 — Gestión activa del drawdown

**Drawdown (DD)** = la caída desde el pico más alto del capital hasta el punto actual,
medida en % del pico. Si el capital tocó $1.050 y hoy está en $1.000, el DD es 4.76%.
El módulo 02 define el drawdown; este módulo define QUÉ HACER mientras se está dentro de uno.
Porque todo sistema, incluso uno rentable, pasa buena parte de su vida en drawdown.

## La matemática de la recuperación (el porqué de todo)

La recuperación es asimétrica: se necesita ganar MÁS de lo que se perdió, en porcentaje.

| Drawdown | Ganancia para recuperar el pico |
|---|---|
| −5% | +5.3% |
| −10% | +11.1% |
| −15% | +17.6% |
| −25% | +33.3% |
| −50% | +100% |

Hasta ~10-15% la cuesta es empinada pero subible. Después de 25% la matemática empieza a
jugar en contra en serio. Por eso los sistemas serios no "aguantan" el drawdown: lo
**gestionan activamente** para que nunca llegue a la zona donde la recuperación es una
hazaña. Números exactos → `Matematicas_lushows`.

## Herramienta 1: reducir tamaño escalonado

Bajar el riesgo por trade a medida que el DD crece. El efecto es doble: frena la caída Y
como el riesgo es % del capital actual (fixed fractional, módulo 20), el freno ya viene
parcialmente incorporado. El escalón lo refuerza:

| Drawdown | Riesgo por trade |
|---|---|
| 0–8% | 1.5% (normal) |
| >8% | 0.75% (mitad) |
| >12% | 0.375% (cuarto) o pausa |
| ≥15% | STOP total — revisar el sistema |

La trampa mortal es hacer lo contrario: subir el tamaño "para recuperar rápido". Esa es la
definición operativa de cómo se muere una cuenta (martingala, módulo 20).

## Herramienta 2: pausas

Parar de operar un tiempo definido tras una racha mala. No porque el mercado "deba una",
sino porque: (a) las rachas de pérdidas a veces señalan un régimen de mercado hostil al
sistema, y (b) en humanos, corta el revenge trading. Un bot no siente, pero su sistema sí
puede estar desalineado del mercado — la pausa compra tiempo de diagnóstico barato.

## Herramienta 3: distinguir drawdown normal de sistema roto

Todo sistema tiene un DD "esperado" según su win rate y R:R (estimable simulando miles de
secuencias — `Matematicas_lushows`). Regla práctica: si el DD actual es mayor que ~1.5-2×
el peor DD esperado, la hipótesis "el sistema dejó de funcionar" pesa más que "mala racha".
Ahí no se reduce tamaño: se apaga y se re-examina el edge.

## Cómo aplica al AGENTE TRADING

El bot ya tiene dos capas vigentes: **cooldown de 4h tras 3 pérdidas seguidas** (pausa) y
fixed fractional (freno automático). El protocolo del proyecto añade: **tras DD >8%, reducir
tamaño a la mitad hasta recuperar el pico**; **DD ≥15% = criterio de NO go-live** y stop
total. Estado real (6-jul-2026): DD 1.84% — zona verde, protocolo sin activar. Pendiente
para antes del 22-ago: verificar que la reducción escalonada esté EN CÓDIGO (no solo en la
spec), y calcular el DD esperado del sistema con los parámetros actuales para saber qué es
"normal" cuando llegue la primera racha fea.
