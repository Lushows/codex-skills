# 157 — QA de calls y emails

El módulo `87` da los checklists de calidad y el ritmo del QA dentro del coaching. Este módulo formaliza el **sistema de QA**: el scorecard con puntajes ponderados que hace la revisión consistente entre evaluadores y en el tiempo, las herramientas de conversation intelligence que graban y transcriben para revisar a escala, y las sesiones de calibración que evitan que "calidad" signifique cosas distintas según quién revisa. El QA es el sensor que detecta la deriva de calidad antes de que se vea en los números; sin él, coacheas a ciegas.

## El principio: sin scorecard, "calidad" es una opinión

Revisar sin rúbrica escrita produce QA inconsistente: hoy apruebas un correo que ayer habrías rechazado, y dos líderes puntúan al mismo SDR distinto. Un **scorecard ponderado** (cada criterio con un peso) convierte la calidad en algo medible, comparable y coacheable. Dos cosas lo hacen funcionar:

1. **Criterios observables**, no juicios vagos ("¿la personalización es sobre algo real de la cuenta?" — sí/no; no "¿es bueno el correo?").
2. **Pesos** que reflejan qué importa de verdad (la personalización relevante pesa más que el saludo).

El QA mira hacia atrás (control); el coaching (`87`) usa lo que el QA vio para mirar hacia adelante (desarrollo). Son inseparables: QA sin coaching es fiscalizar; coaching sin QA es opinar sin datos.

## Scorecard de cold email (ponderado)

Formaliza el checklist de `87` en puntaje. Ejemplo sobre 100:

```
COLD EMAIL — scorecard QA                              Peso   Puntaje
  Personalización relevante (algo real de la cuenta)    30    ___/30
  Fit con ICP (¿le escribimos a quien encaja? 10)       15    ___/15
  Brevedad y escaneabilidad (<100 palabras)             15    ___/15
  Claridad de la propuesta de valor (54)                15    ___/15
  CTA de micro-compromiso, no la venta (55)             15    ___/15
  Gramática, tono, sin errores                          10    ___/10
  ───────────────────────────────────────────────────────────────
  TOTAL                                                       ___/100
  Umbral de calidad del equipo: ≥ 80/100
```

## Scorecard de cold call / respuesta manejada

Para llamadas y manejo de respuestas (ver `58`, `64`), puntúa la conducta, no el resultado (agendar o no depende también de suerte y timing):

```
CALL / RESPUESTA — scorecard QA                        Peso   Puntaje
  Apertura clara y con permiso/gancho (53)              15    ___/15
  Escuchó (ratio hablar/escuchar sano, no atropelló)    20    ___/20
  Hizo preguntas de descubrimiento apropiadas (71)      20    ___/20
  Manejó la objeción TEMPRANA sin empujar (68)          15    ___/15
  Calificó lo justo (ni de menos ni interrogatorio)     15    ___/15
  Avanzó hacia el siguiente paso concreto               15    ___/15
  ───────────────────────────────────────────────────────────────
  TOTAL                                                       ___/100
```

Nota de frontera: aquí evalúas **manejo temprano y escucha**, no cierre ni negociación profunda —eso es del AE y su QA vive en `ventas_lushows`.

## Scorecard de calificación / SQL (el más importante)

La mejor señal de calidad no es cómo suena el correo, sino si el SQL que el SDR entrega es **real**. Cruza con el AE:

```
CALIFICACIÓN / SQL — QA
  ¿El SQL cumple la definición escrita y acordada? (78)          sí/no
  ¿El handoff al AE tenía el contexto necesario? (73)            sí/no
  ¿El AE lo ACEPTÓ o lo rebotó?  ← la señal madre
  → Métrica clave: TASA DE ACEPTACIÓN del AE (% de SQL aceptados)
    Sana: ≥ 70–80%.  Baja: el SDR agenda basura o califica flojo (68, 78).
```

La tasa de aceptación del AE es tu QA de calificación *automático*: no requiere que revises nada manualmente, sale del loop SDR↔AE (ver `79`). Aliméntala al comp con un gate de calidad (ver `154`) y el SDR se autocorrige.

## Herramientas: conversation intelligence

Para hacer QA de llamadas a escala necesitas que las llamadas queden **grabadas y transcritas**. No puedes escuchar todo en vivo:

| Herramienta | Qué hace | Nota |
|---|---|---|
| **Gong** | Graba, transcribe, analiza llamadas; detecta patrones | El estándar enterprise; caro |
| **Chorus (ZoomInfo)** | Similar a Gong | Alternativa fuerte |
| **Avoma / Fathom / tl;dv** | Grabación + transcripción + resumen IA | Más accesibles para equipos chicos/LatAm |
| **La grabación del dialer/CRM** | Muchos dialers y CRMs ya graban | Lo mínimo; revísalo aunque no tengas IA |

Para email, el QA es directo: el sequencer (ver `33`) guarda cada envío; exportas una muestra y la puntúas. La IA (ver `35`) puede pre-clasificar correos por calidad de personalización para que revises los dudosos, pero **la decisión final es humana** —la IA no distingue bien relevancia genuina de cosmética.

## Tamaño de muestra y frecuencia

No revises todo (imposible) ni muy poco (no ves patrones). Escala la intensidad con la madurez del SDR (ver el ramp en `86`):

| Etapa | Muestra | Frecuencia |
|---|---|---|
| Mes 1 | Cada correo antes de enviar | Diario |
| Mes 2 | ~10–15 correos + 2–3 llamadas | Semanal |
| Maduro | ~5–10 correos + 2–3 llamadas + alertas | Semanal/quincenal |

Además, deja que **alertas automáticas** hagan parte del trabajo: si el reply rate de alguien cae bajo cierto umbral o su tasa de aceptación del AE se desploma, eso dispara una revisión enfocada sin esperar al muestreo (ver `83`).

## Calibración: que "calidad" signifique lo mismo para todos

Cuando hay más de un evaluador (varios líderes o pods, ver `150`), sus criterios derivan. Corre una **sesión de calibración** cada 4–6 semanas:
- Todos puntúan **el mismo** correo/llamada por separado con el scorecard.
- Comparan puntajes. Donde hay diferencia grande (uno 90, otro 65), discuten *por qué* → ajustan el criterio compartido.
- Se actualiza el scorecard si hace falta.

Sin calibración, un SDR "aprueba" con un líder y "reprueba" con otro por el mismo trabajo — injusto y confuso. La calibración mantiene el estándar único.

## La review de equipo (multiplica el aprendizaje)

Además del QA individual, corre una sesión quincenal donde el equipo revisa junto **un caso ganador y uno perdedor** (anónimos si hace falta), usando el scorecard. Todos aprenden de un solo caso y alimentan la **biblioteca de swipe** compartida (los mejores correos, respuestas y openers). Es lo que sube al equipo entero, no solo a un individuo (clave al escalar, ver `150`).

## Errores comunes

- **QA sin scorecard escrito.** "Calidad" se vuelve opinión; inconsistente entre revisores y en el tiempo.
- **Puntuar el resultado, no la conducta.** Agendar depende también de timing; puntúa cómo jugó.
- **No cruzar con la aceptación del AE.** Es tu mejor QA de calificación y sale gratis del loop (ver `79`, `78`).
- **Confiar el QA de personalización 100% a la IA.** No distingue bien relevancia real de cosmética; la decisión es humana.
- **No calibrar entre evaluadores.** El estándar deriva; el SDR recibe señales contradictorias.
- **QA como policía.** Si el SDR esconde su trabajo por miedo, perdiste; el QA es para mejorar, no castigar (ver `87`).
- **Revisar todo o casi nada.** Usa muestreo por madurez + alertas automáticas.

## Siguiente paso

Escribe tus tres scorecards (email, call, calificación) con pesos y umbrales, y define el tamaño de muestra por etapa del SDR. Prende grabación de llamadas (aunque sea la del dialer) y usa la tasa de aceptación del AE como QA de calificación automático. Corre calibración entre evaluadores cada 4–6 semanas. El QA alimenta el coaching semanal → `87` y el foco de desarrollo de carrera → `156`; para elegir qué métrica atacar con lo que ves → `83`; para atar la calidad al bolsillo del SDR → gate de calidad en `154`.
