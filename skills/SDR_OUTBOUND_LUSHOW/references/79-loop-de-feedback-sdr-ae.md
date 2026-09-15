# 79 — Loop de feedback SDR → AE

El loop de feedback (círculo de retroalimentación) es el mecanismo por el cual el AE le dice al SDR *qué leads sí sirvieron y cuáles no, y por qué*, para que el SDR afine su targeting con lo que realmente cierra. Sin este loop, el SDR prospecta a ciegas: sigue trayendo el mismo tipo de lead sin saber si convierte, y el AE se frustra en silencio hasta que la relación se rompe. Con el loop, el sistema *aprende*: cada trato ganado o perdido enseña quién es tu cliente real y afila la lista, la calificación y el mensaje. Este módulo cierra el Bloque 7 conectando el resultado final (lo que cierra el AE) de vuelta al principio (a quién prospectas, ver `10`, `20`).

## El principio: el AE tiene la data de la verdad, el SDR necesita esa data

El SDR trabaja con hipótesis: "creo que este ICP tiene este dolor". El AE trabaja con la realidad: se sienta con el prospecto, escucha la objeción final, ve quién firma y quién no, sabe cuáles tratos se cierran fácil y cuáles se caen. Esa realidad es el mejor combustible para mejorar el outbound — pero solo si **fluye de vuelta al SDR de forma estructurada**. La mejora del targeting no viene de adivinar mejor; viene de mirar los tratos ganados y preguntar "¿qué tenían en común?" y "¿de dónde salieron?" (la columna `fuente`, ver `20`). Regla: *el SDR optimiza hacia lo que el AE cierra, no hacia lo que agenda.*

## Qué feedback debe fluir (y en qué dirección)

| Del AE al SDR | Para qué le sirve al SDR |
|---|---|
| **¿El SQL era realmente calificado?** (aceptado/rechazado + motivo) | Calibra su umbral (ver `70`, `78`) |
| **¿El contexto del handoff sirvió?** (ver `73`) | Mejora qué info captura |
| **¿Qué tratos GANADOS tenían en común?** | Afina el ICP (ver `10`) y la lista (ver `20`) |
| **¿Qué objeción final apareció?** | Prepara mejor el discovery corto (ver `71`) |
| **¿Qué fuente/segmento cierra mejor?** | Dobla la apuesta en ese sourcing |
| Del SDR al AE: **señales de mercado** | El AE ajusta su pitch a lo que el SDR oye en frío |

El feedback más valioso es el de los **ganados**: analiza tus 10 últimos clientes cerrados y busca el patrón (sector, tamaño, disparador, cargo del que respondió, canal). Ese patrón es tu nuevo ICP afinado — vuelve a `10` y actualízalo.

## El ritual: cómo hacer que el loop ocurra de verdad

El feedback no pasa "cuando haya tiempo"; se agenda. Dos mecanismos:

```
1. FEEDBACK POR LEAD (inmediato, en el CRM):
   Cuando el AE toma un SQL, marca en < 24h (ver 74):
     ✅ Aceptado — calidad buena
     ⚠️ Aceptado con reservas — "faltaba confirmar quién decide"
     ❌ Rechazado — motivo obligatorio ("fuera de ICP", "sin dolor real")
   → El SDR revisa TODOS sus rechazos cada semana.

2. SINCRONÍA QUINCENAL (30 min, SDR + AE, ver 74):
   • Tasa SQL→Opportunity de la quincena (ver 72)
   • Top 3 tratos ganados: ¿qué tenían en común? ¿fuente?
   • Top 3 rechazos: ¿por qué? ¿patrón?
   • 1 ajuste concreto para la próxima quincena (a la lista, al filtro o al mensaje)
```

La clave: **cada sincronía produce UN ajuste accionable**, no una queja. "Los de 1 solo local casi no cierran → subamos el filtro a 2+ locales" es un ajuste. "Los leads están malos" no lo es.

## Ejemplo real del loop funcionando (LatAm)

```
Observación del AE (sincronía): "De los 8 SQL de este mes cerré 3.
  Los 3 ganados eran GRUPOS de 3+ restaurantes con dueño operador.
  Los 5 que no cerraron eran locales de 1 solo punto — les parecía caro
  y no tenían quién montara el sistema."

Ajuste del SDR:
  → ICP (ver 10): priorizar grupos de 3+ locales con dueño operador.
  → Lista (ver 20): filtrar por múltiples sedes en el sourcing.
  → Mensaje: ángulo "estandariza costos entre TUS locales".
  → Umbral (ver 70): para 1 solo local, exigir señal de dolor más fuerte
    o mandarlo a nurture (ver 76).

Resultado esperado: mismo esfuerzo, más SQL que cierran → sube SQL→Opportunity.
```

Ese ciclo —ganado → patrón → ajuste de targeting— es lo que convierte el outbound en una máquina que mejora sola con el tiempo.

## Números que hacen medible el loop

- **SQL→Opportunity** (ver `72`): si sube, tu targeting mejora; si baja, algo se desalineó.
- **% de SQL rechazados por el AE** y su motivo: tu tasa de basura (ver `78`); apúntala a la baja.
- **Fuente de los tratos ganados** (ver `20`): concentra esfuerzo donde cierra.
- **Tiempo SQL→decisión del AE**: si un segmento cierra rápido, priorízalo.

Para que estos números sean confiables, el CRM tiene que estar limpio (ver `77`). Para cálculos finos de conversión o costo por cliente, apóyate en `Matematicas_lushows` y `economist_lushows`.

## La frontera con ventas_lushows

El AE cierra usando el arte de `ventas_lushows` (objeciones, negociación, cierre). Lo que vuelve a ti, el SDR, no es *cómo cerró*, sino *qué tipo de lead cerró* y *por qué se cayeron los otros* — la data de targeting. Tú no aprendes a cerrar aquí; aprendes **a quién traer** para que el cierre sea más fácil.

## Errores comunes

- **No pedir feedback.** El SDR sigue trayendo lo mismo sin saber si sirve. Agéndalo.
- **Feedback como queja, no como ajuste.** "Están malos" no mejora nada; "subamos el filtro a 2+ locales" sí.
- **Ignorar los ganados.** El oro está en el patrón de lo que SÍ cierra, no solo en lo que falló.
- **Rechazar SQL sin motivo.** Sin el porqué, el SDR no puede calibrar (ver `78`, `77`).
- **No cerrar el ciclo en el ICP.** Si el aprendizaje no vuelve a `10` y `20`, se pierde. Actualiza la fuente.

## Siguiente paso

Monta la sincronía quincenal dentro del SLA (ver `74`) y exige motivo en cada rechazo (ver `77`, `78`). Lleva los patrones de los tratos ganados de vuelta al ICP (`10`) y al list building (`20`). Con eso, el Bloque 7 (calificación y handoff) queda cerrado como un círculo que aprende: prospectas mejor → calificas mejor (`70`) → entregas mejor (`73`) → cierras más → y ese resultado afina la próxima prospección.
