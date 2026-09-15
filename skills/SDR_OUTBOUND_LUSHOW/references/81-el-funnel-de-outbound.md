# 81 — El funnel de outbound

El funnel (embudo) es la representación de tu máquina como una serie de etapas donde en cada una se cae gente: tocas 100, responden algunos, agendan menos, se presentan menos, califican menos, cierran unos pocos. Entender tus ratios de conversión entre etapas es lo que te deja **predecir** (cuántos contactos necesito para X reuniones) y **diagnosticar** (¿dónde se está cayendo la gente que no debería?). Este módulo te da las etapas, los ratios típicos 2026 y cómo leer tu propio embudo. Es la versión "operativa" de la ecuación del pipeline (ver `05`).

## Las etapas del embudo de outbound

De arriba (más volumen) hacia abajo (más valor):

```
1. CONTACTOS TOCADOS      ← entraron a una cadencia (Bloque 6, 60–69)
2. RESPUESTAS             ← contestaron algo (reply)
3. RESPUESTAS POSITIVAS   ← contestaron con interés
4. REUNIONES AGENDADAS    ← booked
5. REUNIONES REALIZADAS   ← held (descuenta no-shows)
6. OPORTUNIDADES (SQL)    ← el AE la acepta como real (frontera del SDR aquí)
─────────────────────────────────────────────
7. PROPUESTA / NEGOCIACIÓN  ← ya es trabajo del vendedor
8. CIERRE (cliente)         ← ventas_lushows
```

**La frontera del SDR está en la etapa 6.** El SDR es responsable de llenar las etapas 1 a 6: conseguir la reunión, que se realice, y que sea una oportunidad real. De la 7 en adelante —propuesta, negociación, cierre— es oficio del vendedor y vive en `ventas_lushows`. Medir al SDR por cierres es injusto y contraproducente: no controla la etapa donde ocurren (ver `84`).

## Ratios típicos 2026 (cold email B2B, ICP bien elegido)

| Transición | Ratio típico | Qué lo mueve |
|---|---|---|
| Tocados → Respuestas | 3–7% | Lista + copy + deliverability (`20`, `52`, `40`) |
| Respuestas → Positivas | 25–40% | Calidad de lista + relevancia del ángulo |
| Positivas → Agendadas | 40–60% | Manejo de la respuesta + facilidad de agendar (`64`, `69`) |
| Agendadas → Realizadas | 70–85% | Recordatorios + calificación previa (anti no-show) |
| Realizadas → SQL | 55–75% | Qué tan duro calificaste (`78`) |
| **Tocados → SQL (global)** | **~1–2%** | Todo lo anterior compuesto |

Lee la última fila: **de 100 contactos fríos bien elegidos sacas 1 a 2 oportunidades reales.** Eso es un embudo sano. Si sacas más, o tu ICP es excelente o estás en un mercado caliente; si sacas menos, algo en la cadena está roto (ver `83`).

## Ejemplo trabajado: de 1.000 contactos a 3 clientes

Un negocio de servicios B2B en LatAm, cadencia multicanal sana:

```
1.000  Contactos tocados
   ↓  ×5% reply
   50  Respuestas
   ↓  ×32% positivas
   16  Respuestas positivas
   ↓  ×50% agendan
    8  Reuniones agendadas
   ↓  ×80% se presentan
  6.4  Reuniones realizadas
   ↓  ×65% califican
  4.2  Oportunidades (SQL)  ← aquí termina el SDR
   ↓  ×30% cierran (trabajo del AE / ventas_lushows)
  1.3  Clientes nuevos
```

De 1.000 contactos → ~1.3 clientes. Si tu ticket deja $1.500 de margen, esos 1.000 contactos generaron ~$1.950. Con eso sabes cuánto puedes gastar en datos y tiempo por cada 1.000 contactos y seguir siendo rentable (une con cost per meeting en `80` y con unit economics en `economist_lushows`).

## Cómo leer TU embudo (las tres preguntas)

1. **¿Dónde está mi ratio más flojo comparado con el benchmark?** Ahí está tu cuello de botella. No optimices lo que ya está bien.
2. **¿El problema es de volumen o de conversión?** Si entran pocos contactos, es problema de *input* (más lista, ver `29`). Si entran muchos y no convierten, es problema de *máquina* (lista mala, copy flojo, deliverability, calificación).
3. **¿El embudo se cae arriba o abajo?**
   - **Se cae arriba** (pocas respuestas): mira lista, copy y deliverability. Es lo más común y lo más barato de arreglar.
   - **Se cae en medio** (responden pero no agendan): mira tu manejo de la respuesta y qué tan fácil es agendar contigo.
   - **Se cae abajo** (agendan pero no califican o son no-show): mira tu targeting (atraes curiosos, no compradores) y tu proceso de recordatorio/calificación.

La tabla completa síntoma→causa→fix está en `83`.

## El embudo invertido: empieza por la meta

No planees de arriba hacia abajo ("mando 1.000 correos, a ver qué sale"). Planea **de abajo hacia arriba**, desde la meta de revenue:

```
Meta:            2 clientes nuevos/mes
Cierre del AE:   30%     → necesito 6.7 SQL
SQL/realizada:   65%     → necesito 10.3 realizadas
Realizada/book:  80%     → necesito 12.9 agendadas
Positiva→agenda: 50%     → necesito 25.8 positivas
Reply→positiva:  32%     → necesito 80.6 respuestas
Tocado→reply:    5%      → necesito ~1.612 contactos tocados/mes
```

Eso son ~1.612 contactos/mes ≈ 80 contactos/día hábil. Ahora sabes cuánta lista construir (`29`) y cuántos buzones necesitas para enviar seguro (`44`). **Para que esta cadena de multiplicaciones sea exacta y no acumule error de redondeo, córrela en `Matematicas_lushows`.**

## Errores comunes

- **Optimizar la etapa equivocada.** Mejorar el copy cuando el problema es que entran 100 contactos/mes no mueve nada. Diagnostica primero (`83`).
- **Un solo ratio global.** "Convierto 1%" esconde dónde. Mide cada transición.
- **Ignorar no-shows.** Agendar 10 y que se presenten 5 es un embudo roto en la etapa 4→5, no un problema de volumen.
- **Contar SQL con criterio blando.** Si llamas SQL a cualquier reunión, el ratio miente y el AE deja de confiar (ver `78`).

## Siguiente paso

Dibuja tu embudo con tus números reales de los últimos 30 días. Identifica el ratio más flojo. Luego: para proyectar revenue desde este embudo → `82`; para arreglar el cuello de botella → `83`; para los benchmarks de cada métrica → `80`. El cierre (etapa 7–8) y su tasa → `ventas_lushows`.
