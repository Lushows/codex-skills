# 96 — Escalado de capital (de $200 a más, sin volarse la cabeza)

> El capital inicial es $200-500 por la "regla de la quiebra": la primera cuenta live de casi
> todo el mundo sufre errores que el paper no mostró. Se escala con hitos, no con emociones.

## Por qué empezar tan chico

- Los primeros meses live van a revelar costos reales (slippage, fees, fricciones) que el paper
  subestima. Mejor pagar esa matrícula con $300 que con $3.000.
- Con riesgo 1.5% por trade, en $300 cada trade arriesga ~$4.50. El objetivo del primer
  tramo NO es ganar plata: es validar que el sistema en vivo se comporta como en paper.
- Un error de software con $300 es una anécdota. Con $5.000 es una crisis.

## La escalera de hitos

| Nivel | Capital | Condición para subir al siguiente |
|---|---|---|
| 0 | $200-500 | 3 meses live con PF > 1.3 real, DD < 15%, cero incidentes técnicos graves |
| 1 | ~2x el anterior | Otros 3 meses cumpliendo lo mismo CON el capital nuevo |
| 2+ | Incrementos graduales (≈2x máx.) | Igual: cada nivel se gana con meses, no con semanas |

Reglas de la escalera:

1. **Nunca saltar niveles**, ni "porque el mes fue buenísimo".
2. **Nunca escalar justo después de una racha ganadora reciente.** Las rachas buenas son cuando
   más ganas dan de subir y cuando estadísticamente más cerca puede estar la racha mala. Se
   escala por CALENDARIO + criterios cumplidos, en frío, no por euforia.
3. **Bajar es válido**: si un nivel nuevo rompe los criterios (DD se dispara, PF cae), se vuelve
   al nivel anterior sin drama. La escalera funciona en ambos sentidos.
4. El dinero que se agrega debe ser dinero que Luis puede perder completo sin afectar su vida.
   Esa regla no caduca nunca, en ningún nivel.

## Retiros periódicos (pagarse a uno mismo)

Cuando el sistema es rentable de verdad, retirar una fracción de las ganancias periódicamente
(ej. cada trimestre) en vez de recomponer todo:

- Convierte ganancias de pantalla en dinero real en el bolsillo — la única prueba definitiva.
- Limita cuánto capital está expuesto a un fallo catastrófico (bug, exchange, hackeo).
- Psicológicamente ancla que el bot es un negocio que paga, no un casino que crece.

Una política simple: retirar ~50% de la ganancia neta del trimestre, dejar el resto componiendo.
El porcentaje exacto importa menos que tener la política ESCRITA antes de la primera ganancia.

## Anti-trampas

- "Le meto $2.000 de una porque el paper dio bien" → NO: paper ≠ live (módulo 90 explica qué
  no valida el testnet; lo mismo aplica al paper).
- "Repongo la pérdida agregando capital" → NO: eso es promediar la cuenta hacia abajo, la
  versión macro del error prohibido de promediar posiciones.
- "Escalo porque el riesgo por trade se siente muy chiquito" → esa sensación es exactamente lo
  que la escalera existe para contener.

## Cómo aplica al AGENTE TRADING

- Módulo 08 ya lo fija: capital inicial $200-500, escalar solo tras 3 meses live rentable.
- Los criterios de cada nivel son los MISMOS del go-live (PF, DD) medidos en vivo — la portería
  no se mueve tampoco después del go-live.
- Los retiros se coordinan con el tema impuestos (módulo 98) cuando haya ganancias reales.
