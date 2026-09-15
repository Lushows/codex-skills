# 58 — Leads high-ticket: servicios y productos de alto valor

Cuando lo que vendes vale millones (>$1M COP: remodelaciones, clínicas estéticas, maquinaria, consultoría, inmobiliaria — caso completo en 87), la lógica de leads se invierte: **no quieres el lead más barato, quieres el comprador más probable**. Lee este módulo antes de pautar cualquier ticket alto; aplicar mentalidad de e-commerce barato aquí destruye equipos de venta y presupuestos. Jerga: "evento de oro" = la acción que mejor predice la venta y tiene volumen para optimizar (casi siempre la cita agendada); "nurturing" = secuencia que madura al lead que aún no compra.

## La métrica: costo por lead CALIFICADO y costo por VENTA

El CPL es la métrica más engañosa del high-ticket. **Un CPL barato de curiosos es caro**:

```
Campaña A: CPL $15.000, 10% califica, cierra 20% → venta cada $750.000
Campaña B: CPL $45.000, 50% califica, cierra 25% → venta cada $360.000
```

La campaña "3× más cara" produce ventas a la mitad del costo. Reporta SIEMPRE las tres columnas: CPL / costo por calificado / costo por venta (dashboard: ver 53). Define "calificado" por escrito: presupuesto mínimo + zona de cobertura + decisión en X tiempo.

## Fricción intencional: filtra ANTES de que llegue al humano

En high-ticket la fricción es tu amiga — cada paso extra espanta curiosos y deja compradores:

1. **Instant forms con preguntas filtro** (setup completo: ver 52): presupuesto en rangos, zona, cuándo. Tipo "mayor intención" con pantalla de revisión, siempre. Aprovecha la **calificación de leads con IA** 2026 de Advantage+ Leads (ver `actualizacion-2026-06` §9) para descartar antes del humano.
2. **CTWA con pre-calificación en el chat** (ver 50/54): el bot pregunta presupuesto y zona ANTES de pasar al humano/agenda. El asesor de $X/hora solo habla con gente que pasó el filtro. Aquí el "interrogatorio" que prohibimos en ticket bajo (ver 54) sí se justifica — hazlo con tacto, no con formulario seco.
3. **Landing con cotizador o agenda** (desingweb-lushows): más fricción aún, leads de máxima intención.

## Lead magnets: intención alta vs baja

| Tipo | Ejemplos | Qué produce |
|---|---|---|
| **Intención ALTA** | Cotizador, agenda tu visita técnica/valoración, simula tu crédito | Menos volumen, ciclo corto, listo para vender |
| **Intención BAJA** | Guía gratis, checklist, webinar | Más volumen, lead frío, ciclo largo — exige nurturing (ver 88) |

Receta: arranca con intención alta (valida la matemática rápido); agrega intención baja solo cuando tengas máquina de nurturing que la digiera.

## El embudo y el evento de oro

```
Ad → Lead → Calificación (bot/SDR) → CITA AGENDADA → Cierre humano
```

- **La cita agendada/valoración es el evento de oro**: es el mejor predictor de venta con volumen suficiente para optimizar. Envíala a Meta vía CAPI (ver 53 nivel 3 / 06) y optimiza campañas por "cita agendada", no por lead. Es el salto de calidad más grande disponible en high-ticket.
- La venta misma suele tener muy poco volumen mensual para optimizar directo (ver 14): la cita es tu proxy.
- El cierre es humano y consultivo — guiones, descubrimiento y negociación high-ticket: **ventas_lushows 58**. El media buyer entrega citas calificadas; no improvisa el cierre.

### Qué evento mandar a Meta según tu volumen

| Ventas/mes | Optimiza por | Por qué |
|---|---|---|
| < 10 | Cita agendada / valoración | La venta no junta señal suficiente (ver 13/14) |
| 10-30 | Cita agendada (principal) + Purchase como secundario | Empiezas a poder validar con Purchase |
| 30+ | Purchase directo, con valor | Ya hay volumen para que el algoritmo aprenda de la venta real |

## Nurturing del no-listo

El 70-85% de tus leads calificados NO compra este mes — y vale oro a 6 meses:

- Secuencia de valor por WhatsApp/email (casos antes/después, respuesta a la objeción típica, invitación recurrente a valoración). Automatízala (ver 96); cadencia quincenal, no spam.
- En WhatsApp esto son **plantillas de Utility/Marketing** fuera de ventana (ver 50/51): cuestan centavos en Colombia pero cuidan el quality rating del número — solo a quien dio permiso.
- Retargeting a leads no cerrados con testimonios y casos (ver 21/23).
- El CRM separa "perdido" de "todavía no": revívelos cada trimestre.

## La matemática completa (ejemplo)

Remodelaciones, ticket promedio $8.000.000 COP, margen 35% ($2.800.000):

```
Cierre: 20% de citas → 1 venta cada 5 citas
Citas: 50% de calificados agenda → 10 calificados por venta
Calificación: 30% de leads califica → 33 leads por venta

Tope racional (gastando hasta 1/3 del margen en adquisición):
$2.800.000 × 33% ≈ $930.000 por venta en ads
→ hasta ~$28.000 por lead | ~$93.000 por calificado | ~$186.000 por cita
```

Corre TUS números con TUS tasas reales (si el margen o el tope no están claros: economist_lushows). Un CPL de $28.000 que parecería "carísimo" en e-commerce es excelente aquí.

### Plantilla de tablero high-ticket (mensual, por campaña)

| Campaña | Gasto | Leads | CPL | Calif. | Costo/calif. | Citas | Costo/cita | Ventas | Costo/venta |
|---|---|---|---|---|---|---|---|---|---|
| A | $1.5M | 100 | $15.000 | 10 | $150.000 | 6 | $250.000 | 1 | $1.5M |
| B | $1.5M | 33 | $45.000 | 17 | $88.000 | 12 | $125.000 | 3 | $500.000 |

Misma lectura que el ejemplo de arriba: B es "más caro por lead" y mucho mejor por venta. Sin las columnas de la derecha, escalarías al perdedor.

## Speed-to-lead high-ticket: el SDR y la cita

En high-ticket el contacto rápido importa tanto como en ticket bajo (regla 21×, ver 52), pero el objetivo del primer contacto NO es vender — es **agendar la cita**:

- **SDR (humano o bot) en <5 min**: confirma datos, valida presupuesto/zona, y propone día y hora concretos ("¿te queda mejor jueves 3pm o viernes 10am?"). Dar dos opciones cerradas agenda más que "¿cuándo te queda bien?".
- **Recordatorio de cita** por WhatsApp (plantilla Utility, centavos en Colombia): 24h antes y 1h antes. La tasa de no-show en high-ticket puede ser 30-40% sin recordatorio; con dos recordatorios baja a la mitad.
- **El asesor de cierre entra leyendo todo**: presupuesto, zona, qué pidió. Cero "cuéntame qué necesitas" tras pasar el filtro — eso quema la confianza del que ya invirtió tiempo (ver 54).

## Frío vs caliente: dos campañas, dos mensajes

| Capa | Audiencia | Creativo | Objetivo |
|---|---|---|---|
| Prospecting | Broad + interés ligero (ver 20) | Caso/transformación + propuesta de valor | Lead calificado / cita |
| Retargeting | Leads no cerrados, visitantes de landing (ver 21/23) | Testimonios, antes/después, respuesta a objeción típica | Reactivar la cita |

El frío educa y filtra; el caliente vence la objeción que frenó la compra. Para high-ticket el retargeting con prueba social (testimonios reales, obras terminadas) es de lo más rentable que tienes — el comprador de millones necesita confianza antes que descuento.

## Errores comunes — blacklist

- Optimizar y celebrar CPL: el incentivo exacto para llenarte de curiosos.
- Form "más volumen" sin filtros para un servicio de $10M: el equipo comercial quema horas y moral en humo.
- Pasar todo lead directo al asesor sin pre-calificación: tu hora de venta más cara gastada en "solo preguntaba".
- No medir tasa de calificación POR CAMPAÑA: dos campañas con igual CPL pueden diferir 4× en calidad.
- Optimizar por venta con 3 ventas/mes: sin volumen de señal no hay aprendizaje (ver 13/14); usa la cita.
- Botar a los no-listos: en tickets altos el ciclo es de meses; sin nurturing pagas dos veces por el mismo cliente.
- Lead magnet de guía gratis sin máquina de nurturing: compras una base de datos que nadie trabajará (ver 88).
- No mandar la cita agendada a Meta por CAPI: dejas al algoritmo optimizando por leads pelados (ver 53).
