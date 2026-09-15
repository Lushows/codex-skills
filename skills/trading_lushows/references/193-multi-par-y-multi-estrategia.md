# 193 — Multi-par y multi-estrategia

Agregar pares (SOL, etc.) o estrategias nuevas es la forma más fácil de DESTRUIR un sistema que
funciona: se contamina la muestra, se rompe la atribución y de repente nadie sabe qué parte gana
y qué parte pierde. Este módulo define cómo crecer sin perder el hilo.

## El concepto clave: atribución

**Atribución** = poder responder con datos "¿de dónde vienen las ganancias y las pérdidas?".
Si el bot opera ETH+SOL con 2 estrategias y el mes cierra en −2%, ¿fue SOL? ¿la estrategia nueva?
¿ambas? Sin atribución, la respuesta es una opinión — y las decisiones sobre opiniones son azar.

Regla técnica: **cada trade se etiqueta** con su par Y su estrategia/versión en traderMemory, y
las métricas (PF, expectancy, DD) se calculan POR etiqueta además del total. Esto se construye
ANTES de agregar el segundo par, no después.

## Las reglas de expansión

1. **Un cambio a la vez.** Nuevo par O nueva estrategia, nunca ambos en el mismo período.
   Si se agregan juntos y algo falla, es imposible saber qué fue.
2. **Todo lo nuevo nace en paper**, aunque el sistema base ya esté live. El par nuevo corre
   en paralelo con capital simulado y su PROPIO contrato de graduación (mini go-live: ≥30
   trades, PF >1.3, igual que el `08`).
3. **El riesgo total no se suma alegremente.** 1.5% por trade en ETH + 1.5% en SOL puede ser
   casi la MISMA apuesta: BTC, ETH y SOL suelen moverse juntos (correlación alta — cuando cae
   uno, caen todos; verificar al día). El techo de riesgo total expuesto (≤6%, ver `02`) manda
   sobre la suma de pares, y pares correlacionados deberían compartir presupuesto de riesgo.
4. **Cada par tiene su personalidad**: SOL se mueve más fuerte que ETH (más volatilidad) →
   el stop a 1.5× volatilidad ya lo adapta automáticamente (buen diseño), pero la memoria de
   trades y los patrones de precio NO se transfieren: la memoria de ETH no sabe nada de SOL.

## Multi-estrategia: la vara es más alta

Una **estrategia** nueva (ej. reversión a la media, o el mismo swing con otro filtro) es un
sistema completo nuevo: su propio edge que demostrar, su propia muestra de 30+, su propio journal.
Preguntas antes de agregarla:

- ¿La estrategia actual ya demostró edge? (Si no: arreglar la casa antes de comprar otra.)
- ¿La nueva cubre un régimen que la actual no opera? (Eso sí suma — ej. SHORT, ver `194`.)
- ¿Puedo mantener DOS journals y DOS revisiones semanales? El costo de atención se duplica.

## El orden natural del proyecto

```
1 par + 1 estrategia con edge demostrado  →  SHORT (mismo par, duplica regímenes, `194`)
→  2º par en paper con atribución  →  multi-estrategia (mucho después)
```

## Cómo aplica al AGENTE TRADING

- Hoy: 1 par operado en la práctica (los 10 trades fueron ETH), 1 estrategia, solo LONG, y el
  edge AÚN no está demostrado (PF 0.89). Traducción honesta: **este módulo es para después del
  22-ago como mínimo** — agregar SOL hoy sería sumar ruido a una pregunta sin responder.
- Trabajo preparatorio que sí se puede hacer ya (barato): confirmar que traderMemory y analyses
  etiquetan par + versión de estrategia en cada registro. Es una línea de código hoy, un dolor
  de cabeza retroactivo mañana.
- Cálculos de correlación entre pares y riesgo combinado → `Matematicas_lushows`.
