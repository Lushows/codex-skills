# 104 — Ganancia ocasional

No todo lo que entra a tu bolsillo es "renta" en el sentido tributario. La **renta** es lo que ganas con tu actividad **del día a día** (vender comida, prestar servicios). La **ganancia ocasional** es una utilidad que llega de forma **extraordinaria, no del giro normal del negocio**: vender la casa, ganarse una lotería, recibir una herencia, vender un activo que tenías hace años. Como es ocasional, la ley la grava **aparte**, normalmente con una **tarifa distinta** (a menudo más baja que la renta ordinaria), y con su propio renglón en la declaración.

Este módulo da el **concepto** y la diferencia con renta. La declaración de renta básica vive en el módulo **42**; aquí explicamos por qué algunas ganancias se separan y cómo distinguirlas.

## Conceptos clave (despacio)
- **Renta ordinaria:** utilidad de la actividad habitual del negocio o persona.
- **Ganancia ocasional:** utilidad de un hecho **extraordinario y no recurrente**.
- **Hecho generador:** el evento que la origina (venta de activo fijo poseído ≥ cierto tiempo, herencia, donación, lotería, etc.).
- **Costo fiscal:** lo que te costó el bien que vendes; la ganancia es **precio de venta − costo fiscal**.
- **Tarifa de ganancia ocasional:** porcentaje propio, distinto al de renta. *Verifica el vigente en la DIAN.*

## Hechos generadores típicos (concepto)
| Hecho | Por qué es ocasional |
|---|---|
| Vender un **activo fijo** poseído por más del tiempo que fija la ley | No es tu negocio diario; es un evento puntual |
| Recibir una **herencia, legado o donación** | Llegada extraordinaria de patrimonio |
| Ganar **loterías, rifas, apuestas** | Suelen tener su propia tarifa (a veces más alta) |
| **Liquidación** de una sociedad (sobre ciertos valores) | Evento extraordinario |

> Si vendes un activo que poseíste por **menos** del tiempo mínimo de ley, esa utilidad suele tratarse como **renta ordinaria**, no como ganancia ocasional. El tiempo de tenencia es clave. *Verifica el umbral vigente.*

## Diferencia con renta (la clave)
```
¿La utilidad viene de tu actividad habitual?
   SÍ → renta ordinaria (tarifa de renta)
   NO, es un evento extraordinario (¿activo poseído el tiempo mínimo? ¿herencia? ¿lotería?)
       → ganancia ocasional (tarifa de ganancia ocasional)
```

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Una persona vende un local que tuvo por más del tiempo mínimo de ley.
- Precio de venta: **$300.000.000** (inventado).
- Costo fiscal (lo que le costó, ajustado): **$200.000.000** (inventado).
- Ganancia ocasional: **$100.000.000**.
- Tarifa ilustrativa 15%: impuesto = 100.000.000 × 15% = **$15.000.000** (inventado).

> Tarifa y cifras ilustrativas. El cálculo real (con costo fiscal y posibles exenciones, como parte del valor de la vivienda) va a `Matematicas_lushows` con valores vigentes.

## Errores comunes
- Meter la venta de un activo de largo plazo como **renta** (suele tributar más caro así).
- Olvidar restar el **costo fiscal**: se grava la utilidad, no todo el precio de venta.
- No verificar el **tiempo mínimo de tenencia** que separa renta de ganancia ocasional.
- Ignorar **exenciones** legales (parte de la herencia o de la venta de vivienda puede estar exenta).
- No declarar la ganancia ocasional creyendo que "no es renta".

## Conexión con otros módulos
- **42 (Renta)** — la ganancia ocasional se declara en la misma declaración, en renglón aparte.
- **31, 32** — activos fijos y depreciación (definen el costo fiscal del activo que vendes).
- **103** — impuesto al patrimonio (los activos que vendes salían de tu patrimonio).
- **100** — planear el momento y la forma de la venta es legal; ocultarla no.
- **Matematicas_lushows** — cálculo de costo fiscal, ganancia y tarifa.

## Siguiente paso típico
Identificar si la utilidad es ocasional o renta ordinaria (tiempo de tenencia y tipo de hecho), determinar el costo fiscal, revisar exenciones aplicables, calcular en `Matematicas_lushows` y declarar en el renglón correcto. Confirmar con el contador titulado, sobre todo en herencias y ventas de inmuebles.
