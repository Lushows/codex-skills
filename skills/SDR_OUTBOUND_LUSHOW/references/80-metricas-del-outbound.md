# 80 — Las métricas del outbound

Lo que no mides no lo puedes arreglar, y en outbound todo se puede medir. Este módulo define las métricas que importan de verdad —de la actividad al costo por reunión— con benchmarks realistas para 2026. La regla de oro: **mides para diagnosticar, no para sentirte bien.** Un tablero de "correos enviados" te miente; un tablero de "reuniones calificadas por cuenta tocada" te dice si tu máquina funciona. Cada métrica aquí conecta con un diagnóstico (ver `83`): cuando un número está mal, sabes exactamente dónde mirar.

## El principio: métricas de actividad vs. métricas de resultado

Hay dos familias y confundirlas es el error #1.

- **Actividad (input, lo que tú controlas):** correos enviados, llamadas hechas, toques de cadencia completados. Sirven para saber si el equipo *está trabajando*, no si está *ganando*. Un SDR puede enviar 1.000 correos y agendar 0.
- **Resultado (output, lo que el negocio quiere):** respuestas positivas, reuniones agendadas, reuniones realizadas, oportunidades calificadas (SQL). Estas pagan las cuentas.

Un buen tablero mide **actividad para diagnosticar** (¿por qué no hay resultado? ¿es que no hubo actividad, o hubo actividad sin conversión?) y **resultado para decidir**. Nunca premies solo actividad: el SDR aprende a "hacer números" mandando basura (ver comp en `84`).

## Las métricas, en orden del embudo

| Métrica | Qué es | Cómo se calcula | Para qué sirve |
|---|---|---|---|
| **Cuentas/contactos tocados** | Personas únicas que entraron a una cadencia | Conteo | El input real (no "correos", que infla con reintentos) |
| **Activity** | Toques ejecutados (emails, llamadas, DMs) | Conteo por día/SDR | Diagnóstico de esfuerzo |
| **Open rate** | % que abre el correo | Abiertos ÷ entregados | Débil en 2026 (ver abajo) |
| **Reply rate** | % que responde (cualquier cosa) | Respuestas ÷ contactos tocados | Salud de lista + copy |
| **Positive reply rate** | % que responde con interés | Respuestas positivas ÷ contactos tocados | **La métrica reina del outbound** |
| **Meetings booked** | Reuniones agendadas | Conteo | El entregable del SDR |
| **Meetings held** | Reuniones que sí ocurrieron | Conteo | Descuenta los no-show |
| **SQL** | Reuniones que el AE acepta como oportunidad real | Conteo | Calidad del handoff (ver `78`, `73`) |
| **Cost per meeting** | Costo de conseguir una reunión | Gasto total ÷ reuniones held | Eficiencia económica |

## Benchmarks realistas 2026 (cold email B2B)

Estos son rangos defendibles para outbound frío bien hecho. Varían por industria, país y qué tan nicho sea tu ICP. Trátalos como brújula, no como ley.

| Métrica | Malo | Aceptable | Bueno | Élite |
|---|---|---|---|---|
| **Reply rate** | <2% | 3–5% | 6–10% | >10% |
| **Positive reply rate** | <0.5% | 1–2% | 2–4% | >4% |
| **Meetings / 100 contactos** | <0.5 | 1–2 | 2–4 | >4 |
| **Reply → meeting** | <10% | 15–25% | 25–40% | >40% |
| **Meeting held / booked** | <65% | 70–80% | 80–90% | >90% |
| **SQL / meeting held** | <40% | 50–65% | 65–80% | >80% |

Traducción práctica: **una campaña sana de cold email agenda 1 a 3 reuniones por cada 100 contactos bien elegidos.** Si necesitas 10 reuniones/mes, tocas ~500–1.000 contactos/mes. Esa es la ecuación del pipeline en acción (ver `05`, y el funnel completo en `81`).

Sobre **open rate**: cada vez sirve menos. Apple Mail Privacy Protection y filtros similares disparan "aperturas" falsas y los píxeles de tracking cada vez llegan menos. Un open rate del 60% ya no te dice nada útil, y peor: el píxel de tracking **daña tu deliverability** (ver `45`). En 2026 muchos equipos de élite **apagan el tracking de aperturas** y miden solo desde reply rate hacia abajo. Usa open rate, si acaso, como señal cruda de deliverability, no de interés.

## Cost per meeting (el número que une todo con el negocio)

```
Costo por reunión = (costo del stack + costo de datos + costo de tiempo del SDR) ÷ reuniones realizadas
```

Ejemplo LatAm, un solista con stack bootstrap (ver `30`):
- Stack + datos: ~$250/mes
- Tiempo: si te pagas $2.000/mes por el rol de SDR y le dedicas medio tiempo → ~$1.000
- Reuniones realizadas en el mes: 12

```
Cost per meeting = ($250 + $1.000) ÷ 12 ≈ $104 por reunión
```

Ese número solo tiene sentido comparado con lo que **vale** una reunión: si cierras 1 de cada 4 reuniones y tu ticket deja $1.500 de margen, cada reunión vale ~$375. Pagas $104 para generar $375 → la máquina es rentable. Cuando el cost per meeting se acerca al valor por reunión, la máquina deja de tener sentido y hay que arreglar conversión o bajar costos. **Para que este cálculo sea exacto y no de servilleta, apóyate en `Matematicas_lushows`; para conectarlo con CAC/LTV y unit economics del negocio, `economist_lushows`.**

## Qué medir por SDR vs. por campaña

- **Por campaña/segmento:** reply rate y positive reply rate. Aquí aíslas si un ICP o un ángulo de copy funciona (ver `52`). Si la campaña A convierte 3% y la B 0.5%, mata la B.
- **Por SDR:** meetings held y SQL/mes. Aquí evalúas a la persona, no al mensaje. Cuidado: un SDR con lista mala se ve "malo" sin serlo — por eso separas las dos vistas.
- **Por buzón/dominio:** reply rate y bounce rate, para cazar problemas de deliverability antes de que hundan todo (ver `83`, `46`).

## El tablero mínimo (lo que revisas cada semana)

```
INPUT       Contactos tocados: 480   |  Toques ejecutados: 1.920
FUNNEL      Replies: 34 (7.1%)  |  Positivas: 14 (2.9%)  |  Meetings booked: 9
CALIDAD     Meetings held: 7 (78%)  |  SQL: 5 (71% de held)
ECONOMÍA    Cost/meeting: $178  |  Bounce rate: 1.8%  |  Spam complaints: 0.02%
```

Con solo estas líneas ya puedes diagnosticar el 90% de los problemas (ver la tabla síntoma→causa→fix en `83`).

## Errores comunes

- **Medir enviados en vez de tocados.** Reenvíos y follow-ups inflan "enviados"; mide personas únicas.
- **Obsesionarte con open rate.** Es ruido en 2026. La verdad empieza en reply.
- **No separar "positivo" de "respondió".** Un "quítame de tu lista" es una respuesta, no una positiva. Etiqueta cada reply (positiva / neutra / negativa / OOO) o tus números mienten.
- **No medir held ni SQL.** Booked sin held es humo (no-shows); held sin SQL es pasar basura al AE (ver `78`).

## Siguiente paso

Arma tu tablero mínimo con estas líneas. Luego lee `81` para ver el funnel completo con sus ratios, `82` para proyectar revenue desde estos números, y `83` para el diagnóstico cuando un número esté bajo. La conversación de venta que ocurre *dentro* de la reunión (y su tasa de cierre) es oficio de vendedor → `ventas_lushows`.
