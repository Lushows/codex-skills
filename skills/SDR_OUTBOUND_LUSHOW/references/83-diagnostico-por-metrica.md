# 83 — Diagnóstico por métrica: dónde se rompe tu outbound

Cuando el outbound no da resultados, el error del principiante es cambiar todo a la vez (copy nuevo, herramienta nueva, más volumen) y no aprender nada. El SDR de élite hace lo contrario: **mira qué número está mal y eso le dice exactamente qué componente arreglar.** Cada métrica del embudo es un sensor que apunta a una causa distinta. Este módulo es la tabla de diagnóstico —síntoma → causa probable → fix— para que cambies **una cosa a la vez** y sepas si funcionó. Es el compañero operativo de `80` (métricas) y `81` (funnel).

## El principio: el embudo es un árbol de diagnóstico

La conversión global ("saco 0.3% de SQL") no te dice nada. Pero **dónde** se cae la gente sí. Recorre el embudo de arriba hacia abajo y detente en el **primer** ratio que esté bajo el benchmark: ese es tu cuello de botella. Arreglar algo *debajo* del cuello no sirve —no llega suficiente gente ahí para que importe.

Regla de oro del diagnóstico: **cambia una variable, espera datos suficientes (mínimo ~200–300 contactos por variante para que el número signifique algo), compara.** Cambiar cinco cosas a la vez con 20 correos es adivinar, no diagnosticar. La significancia estadística real de un A/B → `Matematicas_lushows`.

## Tabla maestra: síntoma → causa → fix

| Síntoma (métrica mala) | Causa más probable | Fix | Módulo |
|---|---|---|---|
| **Bounce rate alto** (>3%) | Lista sucia / datos viejos / correos no verificados | Verifica la lista antes de enviar (NeverBounce, ZeroBounce); baja el volumen; revisa la fuente de datos | `24`, `46` |
| **Casi nada entregado / va a spam** | Deliverability: dominios sin warmup, SPF/DKIM/DMARC mal, dominio quemado | Revisa autenticación, warmup, Postmaster Tools; baja envío/buzón a ~20/día | `40`–`46` |
| **Open rate desplomado** (si lo mides) | Deliverability o asunto malo | Primero descarta spam (arriba); luego prueba asuntos | `45`, `54` |
| **Reply rate bajo** (<2%) pero sí entrega | **Lista mala** o **copy irrelevante** | Aísla: mismo copy a lista mejor, o mejor copy a misma lista. Casi siempre es la lista | `20`, `52` |
| **Responden pero casi todo negativo** | Targeting equivocado (ICP mal) o ángulo que no conecta | Revisa ICP (`10`); cambia el ángulo de valor, no solo las palabras | `10`, `53` |
| **Positivas que no agendan** | Fricción para agendar / manejo flojo de la respuesta / no calificaste el interés | Facilita agendar (link directo, propón horas); mejora la respuesta a la positiva | `64`, `69` |
| **Agendan pero no se presentan** (no-show >25%) | Sin recordatorios / interés tibio / agendaste muy lejos | Recordatorio 24h y 1h antes; agenda dentro de 2–3 días; confirma valor | `69` |
| **Se presentan pero el AE los rechaza** (SQL bajo) | Calificaste blando / atraes curiosos, no compradores | Endurece criterios de calificación; ajusta ICP; mejor handoff | `78`, `73` |
| **Todo bien pero cero volumen** | Input insuficiente: lista pequeña, pocos buzones | Construye más lista; agrega buzones/dominios | `29`, `44` |
| **Buenos números que caen con el tiempo** | Fatiga de dominio / lista repetida / warmup detenido | Rota dominios; refresca lista; mantén warmup activo | `41`, `46` |

## El orden correcto de diagnóstico (no lo saltes)

Siempre de arriba hacia abajo, porque un problema arriba envenena todo lo de abajo:

```
1. ¿LLEGAN los correos?      → bounce + entrega + spam  (deliverability, 40–46)
      Si esto está mal, NADA más importa. Arréglalo primero.
2. ¿RESPONDEN?               → reply rate  (lista + copy, 20/52)
3. ¿Responden CON INTERÉS?   → positive reply rate  (ICP + ángulo, 10/53)
4. ¿AGENDAN?                 → positiva→booked  (manejo + fricción, 64/69)
5. ¿SE PRESENTAN?            → held/booked  (recordatorios, 69)
6. ¿CALIFICAN?              → SQL/held  (calificación, 78)
```

El 70% de los "mi outbound no funciona" se resuelven en los pasos 1 y 2: **o los correos no llegan, o la lista está mal.** La gente pierde semanas reescribiendo el copy cuando el problema real es que están en spam.

## Cómo aislar lista vs. copy (la duda más común)

Reply rate bajo puede ser lista o copy. Para separarlos, haz una de dos pruebas controladas:

- **Misma lista, dos copys (A/B):** si un copy convierte mucho más, el problema era el copy. Si ambos convierten igual de mal → es la lista.
- **Mismo copy, dos listas (dos ICP/segmentos):** si un segmento responde y el otro no, el problema es a quién le escribes (lista/ICP).

En la práctica, **empieza sospechando de la lista.** Un copy mediocre a la lista correcta supera a un copy brillante a la lista equivocada. La relevancia vive en a quién le hablas, no en cómo lo dices (ver `20`, `10`).

## Ejemplo de diagnóstico real

```
Situación: campaña con 800 contactos, "no funciona".
Números:   Entregados 92%  |  Reply 1.1%  |  Positivas 0.2%  |  Meetings 0

Paso 1 ¿Llegan?   92% entrega, bounce 3.5% → un poco alto pero llegan. OK-ish.
Paso 2 ¿Responden? 1.1% reply → MUY bajo. Aquí está el cuello.
Hipótesis: lista o copy. Prueba: mando el mismo copy a un segmento
           más nicho (mismo ICP, cuentas con señal de contratación, ver 37).
Resultado: reply sube a 6% → ERA LA LISTA. El copy estaba bien.
Fix:       reconstruir la lista con mejor targeting y señales (29, 37),
           no tocar el copy.
```

Sin este orden, el instinto habría sido reescribir el correo cinco veces sin mover la aguja.

## Errores comunes

- **Cambiar todo a la vez.** No aprendes nada. Una variable por vez.
- **Diagnosticar con muestras diminutas.** 15 correos no dicen nada. Espera ~200–300 por variante.
- **Empezar por el copy.** Casi siempre es deliverability o lista. Diagnostica en orden.
- **Confundir "respondió" con "positivo".** Etiqueta las respuestas o el diagnóstico miente (ver `80`).
- **Arreglar el cuello equivocado.** Optimizar agendamiento cuando no llegan respuestas es pintar una pared que se está cayendo.

## Siguiente paso

Cuando algo no funcione, abre esta tabla, recorre el embudo de arriba hacia abajo y detente en el primer número bajo. Cambia solo esa palanca. Para los benchmarks de qué es "bajo" → `80`; para el embudo completo → `81`; para significancia estadística de tus pruebas → `Matematicas_lushows`. Si el problema es que la *conversación* de venta dentro de la reunión no cierra, eso ya no es diagnóstico de outbound → `ventas_lushows`.
