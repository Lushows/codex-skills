# El portafolio de tests

Con una tasa de 1 ganador por cada 10 testeados, apostar todo el capital a un solo producto no es valentía: es garantizar un 90% de probabilidad de quedarte en cero. El portafolio no es una sofisticación de gente con plata; es lo único que convierte una tasa de acierto baja en un negocio.

## La matemática que nadie quiere ver

Probabilidad de tener **al menos un ganador** con tasa de acierto p = 10%:

| Productos testeados | Probabilidad de ≥1 ganador | Probabilidad de quedar en cero |
|---|---|---|
| 1 | 10,0% | 90,0% |
| 2 | 19,0% | 81,0% |
| 3 | 27,1% | 72,9% |
| 5 | 41,0% | 59,0% |
| 7 | 52,2% | 47,8% |
| 10 | 65,1% | 34,9% |
| 15 | 79,4% | 20,6% |
| 20 | 87,8% | 12,2% |

Fórmula: `P(≥1) = 1 − (1 − p)^n`.

Dos lecturas incómodas:
1. Con 3 tests, lo más probable sigue siendo que no encuentres nada. Eso es **normal**, no fracaso.
2. Ni con 20 tests tienes garantía. Quien te promete certeza te está vendiendo algo.

## Pero el capital no es infinito: la tensión real

| Presupuesto por test | Tests con USD 500 | Calidad de la señal |
|---|---|---|
| USD 300 (completo) | 1,7 | Señal fuerte, pero una sola apuesta |
| USD 200 | 2,5 | Señal aceptable |
| USD 100 (validación) | 5 | Señal débil: solo mide interés |
| USD 50 (validación mínima) | 10 | Solo descarta lo obviamente muerto |

Aquí está el dilema con capital bajo: **ni puedes hacer 10 tests completos, ni puedes permitirte una sola apuesta**. La salida es el embudo por etapas.

## El embudo de dos etapas (la única estructura viable con <USD 500)

| Etapa | Presupuesto por producto | Cuántos productos | Qué mide | Qué pasa el filtro |
|---|---|---|---|---|
| **1. Validación** | USD 50-70 | 5-6 | ¿Alguien hace clic y agrega al carrito? | CTR >1%, al menos 1 venta o 3+ carritos |
| **2. Test real** | USD 150-200 | 1-2 (los que pasaron) | ¿Hay economía positiva? | 3-5 ventas con CPA < break-even |

Reparto ejemplo con USD 480:

| Concepto | USD |
|---|---|
| Etapa 1: 5 productos × 60 | 300 |
| Etapa 2: 1 producto × 170 | 170 |
| Reserva | 10 |

Esto te da 5 disparos de validación (probabilidad razonable de que uno muestre señal) y presupuesto suficiente para confirmarlo de verdad en uno. No es cómodo. Es lo que hay con ese capital.

## Cómo elegir los 5-6 candidatos (no al azar)

Diversifica el **tipo de riesgo**, no solo el producto:

| Slot | Perfil | Ejemplo para diciembre MX |
|---|---|---|
| 1 | El más seguro: scorecard alto, nicho probado, competencia media | Bundle cocina/hogar |
| 2 | El de mejor margen aunque más competido | Bundle tecnología de escritorio |
| 3 | El de temporada pura | Bundle de regalo con empaque |
| 4 | El de ángulo nuevo sobre producto conocido | Producto saturado con dolor distinto (`63`) |
| 5 | La apuesta: menos validado, mayor upside | Producto en fase 2 (`62`) |

Error clásico: testear 5 variantes del mismo producto y creer que es un portafolio. Eso es un test con 5 creativos, que es otra cosa (y la mecánica la cubren `facebook_ads_lushows` y `tiktok_ads_lushows`).

## Secuencial vs paralelo

| Modo | Ventaja | Desventaja | Cuándo |
|---|---|---|---|
| Paralelo (5 a la vez) | Rápido, comparas en las mismas condiciones de subasta | Atención dividida, más caro en aprendizaje de plataforma | Tienes calendario apretado (diciembre) |
| Secuencial (uno tras otro) | Aprendes de cada uno, aplicas al siguiente | Lento: 5 tests × 5 días = 25 días mínimo | Tienes tiempo y estás aprendiendo |

Para el proyecto de diciembre 2026: **paralelo en etapa 1**, porque en octubre-noviembre tienes semanas, no meses, y porque comparar bajo el mismo CPM es más limpio. Calendario: validación del 1 al 20 de octubre, test real del 21 de octubre al 10 de noviembre, escalado del 13 de noviembre (Buen Fin) al 20 de diciembre.

## Reglas de gestión del portafolio

1. **Presupuesto por producto fijado antes de lanzar.** No se mueve por corazonada (`78`).
2. **Ningún producto recibe más de 40% del capital total** hasta que muestre economía positiva.
3. **Corta rápido en etapa 1, sé paciente en etapa 2.** En validación, 3-5 días bastan. En test real, aguanta las 3-5 ventas necesarias.
4. **El ganador se lleva la reinversión, no capital nuevo.** Las primeras ventas financian el escalado.
5. **Reserva del 10%** para el imprevisto: una cuenta bloqueada, un lote fallado, un envío perdido.
6. **Un producto a la vez en escalado.** Escalar dos con capital bajo es la forma más común de quedarse sin flujo.

## Qué esperar de verdad

| Con 5 validaciones (USD 300) | Resultado probable |
|---|---|
| 3-4 productos sin ninguna señal | Normal |
| 1-2 con señal de interés | Normal |
| 0-1 que pase a ganador en etapa 2 | Lo más probable es 0 en la primera ronda |

Esto no es pesimismo: es la tasa real. Si tu plan financiero necesita que el primer producto sea ganador, tu plan no aguanta la realidad del negocio. La viabilidad del proyecto completo la evalúa `economist_lushows`.

## La segunda ronda

Si la primera ronda de 5 no da ganador y todavía tienes capital (o llegó más), la segunda ronda es **mucho mejor** que la primera: ya tienes proveedor, pixel con datos, creativo propio, página que funciona y 5 autopsias escritas (`78`). Tu costo por test baja y tu tasa de acierto sube — no al 50%, pero sí por encima del 10% de partida. Ahí es donde el negocio empieza a existir.

## Relacionados

`60` demanda real · `62` ciclo de vida · `63` temprano vs tarde · `67` temporada · `76` scorecard · `78` matar a tiempo
