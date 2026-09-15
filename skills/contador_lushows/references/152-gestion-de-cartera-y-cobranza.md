# 152 — Gestión de cartera y cobranza

La **cartera** es la plata que tus clientes te deben porque les vendiste a crédito (lo que en libros llamamos *cuentas por cobrar*). La **cobranza** es el conjunto de acciones para que esa plata efectivamente entre. Vender es solo la mitad del trabajo: una venta que no se cobra no es una venta, es un regalo con factura. Por eso una buena gestión de cartera es lo que convierte las ventas en **efectivo** que puedes usar.

Aquí vemos la **operación y el control** de la cartera: cómo darle crédito al cliente con cabeza, cómo organizarla por edades y cómo recuperarla. El registro contable detallado de las cuentas por cobrar está en el módulo **33**.

## Políticas de crédito

Una **política de crédito** son las reglas claras de a quién le fías, cuánto y por cuánto tiempo. Sin política, le terminas fiando a todo el mundo y nadie te paga.

| Elemento | Decisión que define |
|---|---|
| Cupo de crédito | Máximo que un cliente puede deberte a la vez |
| Plazo | Cuántos días tiene para pagar (ej. 30, 60 días) |
| Requisitos | Qué pide para aprobar el crédito (referencias, historial) |
| Condiciones de mora | Qué pasa si se atrasa (interés, suspensión de despachos) |

## Edades de cartera (aging)

El **reporte de edades de cartera** ordena lo que te deben según **cuántos días llevan sin pagar**. Entre más vieja la deuda, más difícil de cobrar.

| Rango | Estado | Acción típica |
|---|---|---|
| Por vencer (al día) | Sana | Recordatorio amable antes del vencimiento |
| 1–30 días vencida | Atención | Llamada o mensaje firme |
| 31–60 días | Riesgo | Gestión intensa, acuerdo de pago |
| 61–90 días | Grave | Suspender crédito, escalar |
| +90 días | Muy difícil | Evaluar provisión / cobro jurídico |

Cuando una deuda lleva mucho sin cobrarse y es probable que no la paguen, contablemente se reconoce una **provisión** (módulo **36**): se acepta que parte de esa cartera puede perderse.

## Escala de cobranza

Cobrar es un proceso, no un solo correo. La secuencia típica: recordatorio antes de vencer → mensaje al día 1 de mora → llamada → acuerdo de pago por escrito → suspensión de crédito → cobro jurídico. Lo clave es ser **constante y respetuoso**, y dejar todo por escrito.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Tu cartera total es $20.000.000 repartida así (cifras inventadas):

| Rango | Monto |
|---|---|
| Al día | $12.000.000 |
| 1–30 días | $5.000.000 |
| 31–60 días | $2.000.000 |
| +60 días | $1.000.000 |

El $1.000.000 de +60 días es tu foco rojo: gestión intensa hoy y, si aplica, evaluar provisión. Cifras inventadas; cualquier suma o cálculo de provisión se verifica con `Matematicas_lushows`.

## Errores comunes

- **Vender sin política de crédito**: le fías a quien no debías.
- **No tener el reporte de edades**: no sabes qué cobrar primero.
- **Cobrar solo cuando ya falta plata**: la cartera vieja casi no se recupera.
- **No dejar los acuerdos por escrito**: luego el cliente "no recuerda" lo pactado.
- **Calcular intereses de mora de cabeza**: cualquier interés va a `Matematicas_lushows`.

## Conexión con otros módulos

- El registro contable de lo que te deben está en cuentas por cobrar (**33**).
- La cartera incobrable se reconoce como provisión (**36**).
- Lo que cobras alimenta las entradas del flujo de caja (**151**) y se confirma en la conciliación (**35**).
- Estrategia de precios y condiciones comerciales → `economist_lushows`. Intereses y cálculos → `Matematicas_lushows`.

## Siguiente paso típico

Saca el reporte de edades de cartera, define una política de crédito por escrito, monta una rutina de cobranza por etapas y conecta los cobros esperados al flujo de caja (**151**).
