# 23 — Take profit y salidas

**Take profit (TP)** = el precio al que se cierra la posición cobrando la ganancia. La salida
es la mitad olvidada del trading: todo el mundo estudia entradas, pero la salida es la que
convierte (o no) una buena entrada en dinero. Dos traders con las mismas entradas y distintas
salidas pueden terminar uno rentable y otro quebrado.

## Por qué la salida importa tanto como la entrada

- La entrada solo decide DÓNDE empieza el trade; la salida decide CUÁNTO vale.
- El sesgo humano trabaja en contra: cortar ganancias rápido ("no se me vaya") y dejar correr
  pérdidas ("ya vuelve"). Un sistema de salidas definido de antemano existe precisamente para
  anular ese sesgo. En un bot, la salida programada ES la ventaja sobre el humano.
- Sin salida definida no se puede calcular R:R (cuánto gano por cada peso que arriesgo), y
  sin R:R el win rate no significa nada (módulo 07).

## Menú de salidas

| Salida | Cómo funciona | Pro | Contra |
|---|---|---|---|
| Target fijo (R:R) | TP a un múltiplo del riesgo (ej. 2R) | Simple, medible, backtesteable | Deja plata en tendencias largas |
| Parciales | Cerrar por partes (ej. ½ en 1R, ½ en 3R) | Asegura algo + deja correr | Reduce la ganancia promedio; más complejidad |
| Señal contraria | Salir cuando el sistema daría la señal opuesta | Se adapta al mercado | Devuelve mucha ganancia antes de confirmar |
| Tiempo máximo | Cerrar tras N velas sin llegar a TP ni stop | Mata trades zombi, libera capital | Puede cortar trades que iban bien |
| Trailing stop | Stop que persigue al precio | Captura tendencias | Módulo 24 completo |

## Target fijo: el punto de partida correcto

Para un sistema en validación, el target fijo a 2R es la salida correcta, aunque no sea la
"óptima": produce datos limpios (cada trade termina en +2R, −1R o cerca), hace el desempeño
medible y comparable, y es trivial de programar sin bugs. Primero validar con salidas simples;
optimizar salidas después, con datos.

## Parciales: la matemática honesta

Cerrar la mitad en 1R "para asegurar" SE SIENTE bien pero reduce la expectativa si el sistema
realmente corre a 2R+: la mitad de la posición cobra la mitad del recorrido. Las parciales se
justifican psicológicamente (en humanos) o cuando los datos muestran que el precio suele
llegar a 1R pero no a 2R. Un bot no necesita el alivio psicológico — necesita la expectativa.
Comparar expectativas de cada esquema → `Matematicas_lushows`, no intuición.

## Regla de oro

La salida se define ANTES de entrar y no se renegocia con la posición abierta. Cambiar el TP
"porque va muy bien" o cerrarlo antes "por miedo" invalida los datos: ya no se sabe qué
sistema se está midiendo.

## Cómo aplica al AGENTE TRADING

El bot usa **target fijo R:R 1:2** (gana $30 o pierde $15 con capital $1.000) — la elección
correcta para la fase de validación: 30 trades comparables rumbo al criterio go-live
(PF>1.3, DD<15%). No tocar el esquema de salidas antes de los 30 trades: cada cambio
reinicia el reloj estadístico. Después, con datos, evaluar en este orden: (1) stop de tiempo
para trades estancados, (2) trailing para capturar tendencias (módulo 24), (3) parciales
solo si los datos de recorrido lo piden.
