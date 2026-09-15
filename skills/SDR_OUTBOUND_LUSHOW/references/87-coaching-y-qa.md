# 87 — Coaching y QA del SDR

Un SDR no mejora solo por acumular meses; mejora por **feedback específico y frecuente sobre su trabajo real**. El coaching (entrenamiento continuo) y el QA (Quality Assurance — revisión de calidad de correos, llamadas y calificación) son el motor que lleva a un SDR de "cumple" a "excelente" y que mantiene sana la máquina completa. Este módulo cubre cómo revisar el trabajo real, cómo correr 1:1s que sirven, y cómo hacerlo sin convertirte en policía. Es la continuación natural del ramp (ver `86`): cuando el onboarding termina, el coaching es lo que sostiene la mejora.

## El principio: revisas el trabajo real, no los promedios

El error del líder novato es coachear con métricas agregadas ("tu reply rate está bajo, súbelo"). Eso no enseña nada —el SDR ya lo sabe, no sabe *qué* cambiar. El coaching efectivo mira **el artefacto real**: *este* correo, *esta* llamada, *esta* respuesta que mandó. Ahí es donde está la lección concreta.

QA y coaching son dos caras:
- **QA (mirar hacia atrás):** revisar una muestra del trabajo para detectar errores y patrones. Control de calidad.
- **Coaching (mirar hacia adelante):** usar lo que viste para desarrollar una habilidad. Desarrollo.

Uno sin el otro falla: QA sin coaching es fiscalizar; coaching sin QA es opinar sin datos.

## QA: qué revisar y cada cuánto

La intensidad del QA baja con la madurez del SDR (ver el ramp en `86`):

| Etapa | Frecuencia de QA | Qué revisas |
|---|---|---|
| Mes 1 | Cada correo antes de enviar | Que no salga basura ni se queme deliverability |
| Mes 2 | Muestra semanal (~10–15 correos) | Personalización, CTA, calidad de lista |
| Maduro | Muestra por muestreo (~5–10/semana) + alertas | Tendencias, deriva de calidad, calificación |

**Checklist de QA de un cold email** (ver `52`, `55`):
- ¿La personalización es *relevante* (algo real de la cuenta) o cosmética?
- ¿Es corto y escaneable (bajo ~100 palabras)?
- ¿El CTA pide una micro-conversación, no la venta?
- ¿El contacto encaja con el ICP (`10`)? (¿o estamos escribiéndole a cualquiera?)
- ¿Gramática y tono cuidados?

**Checklist de QA de una respuesta manejada** (ver `64`):
- ¿Respondió rápido? (velocidad al lead importa)
- ¿Avanzó hacia agendar sin empujar de más?
- ¿Calificó lo justo antes de agendar? (ni de menos → basura al AE, ni de más → interrogatorio)
- La objeción *profunda* o la negociación no se evalúan aquí: eso es del AE → `ventas_lushows`.

**Checklist de QA de calificación / SQL** (ver `78`, `73`):
- ¿Lo que marcó como SQL cumple la definición acordada?
- ¿El handoff al AE tenía el contexto necesario?
- Cruza con el feedback del AE: ¿aceptó los SQL o los rebotó? Eso es tu mejor señal de QA de calificación.

## El 1:1 semanal (la reunión que sí sirve)

30–45 minutos, semanal, estructura fija. No es un reporte de números (eso lo ves en el tablero, `80`); es coaching.

```
Estructura del 1:1 (semanal):
  1. Cómo te sentiste esta semana (2 min)   ← resiliencia, moral (el outbound desgasta)
  2. Números vs. meta (5 min)               ← dónde estamos, sin drama
  3. Revisión de trabajo real (15 min)      ← el corazón: 1–2 correos/llamadas juntos
        → "¿por qué elegiste este ángulo?"  ← que él razone, no que tú dictes
        → UN foco de mejora, no diez
  4. Diagnóstico si algo está bajo (10 min) ← usa la tabla de 83 juntos
  5. Un compromiso concreto para la semana (3 min)
```

**Regla de oro del coaching: un foco por vez.** Diez correcciones = cero cambios. Elige la palanca de mayor impacto (usa `83` para saber cuál) y trabájala hasta que mejore, luego pasa a la siguiente.

**Técnica clave — pregunta, no dictes.** En vez de "cambia esto", pregunta "¿por qué elegiste ese asunto? ¿qué crees que pensó el prospecto al abrirlo?". El SDR que llega solo a la respuesta la retiene; al que se la das, la olvida. Esto también mide coachability (ver `85`).

## Cómo dar feedback que se aplica

- **Específico y sobre el trabajo, no la persona.** "Este correo empieza hablando de ti, no de él" (no "eres egocéntrico escribiendo").
- **Balanceado pero honesto.** Reconoce lo que hizo bien *de verdad* (no elogio vacío) y sé claro con lo que falla. El SDR resiliente quiere la verdad (ver `85`).
- **Accionable esta semana.** "Reescribe tus próximos 10 primeros toques abriendo con algo de la cuenta del prospecto." Medible, chequeable el próximo 1:1.
- **Modela, no solo corrige.** A veces la lección más rápida es "mira, así lo escribiría yo" y desglosar por qué.

## Call/email review en grupo (multiplica el aprendizaje)

Una vez por semana o quincena, sesión de equipo donde revisan juntos **un correo/llamada ganador y uno perdedor** (anónimos si hace falta). Todos aprenden de un solo caso. Construye una **biblioteca de swipe** compartida: los mejores correos, las mejores respuestas a objeciones tempranas, los mejores openers. Es el activo que hace que el equipo entero suba, no solo un individuo (clave al escalar, ver `88`, `89`).

## Ejemplo de sesión de coaching (foco único)

```
Observación (QA): 8 de 10 correos de Ana abren hablando de nuestro producto.
Reply rate de Ana: 2.1% (equipo: 5%).  Diagnóstico (83): copy centrado en nosotros.
1:1:
  Líder: "Leamos este. Si fueras el prospecto, ¿qué sientes en la primera línea?"
  Ana:   "...que le estoy hablando de mí, no de él."
  Líder: "Exacto. ¿Cómo lo reescribirías empezando por SU mundo?"
  Ana reescribe → abre con una señal de la cuenta del prospecto.
  Compromiso: próximos 15 primeros-toques abren con algo del prospecto.
Semana siguiente: reply de Ana sube a 4.3%. Un foco, un cambio, resultado.
```

## Errores comunes

- **Coachear con promedios, no con trabajo real.** No enseña qué cambiar.
- **Diez correcciones a la vez.** Cero cambios. Un foco por vez.
- **Dictar en vez de preguntar.** El SDR no interioriza.
- **1:1 que es solo reporte de números.** Eso ya está en el tablero; el 1:1 es para desarrollar.
- **QA como policía.** Si el SDR esconde su trabajo por miedo, perdiste. QA es para mejorar, no castigar.
- **No cerrar el loop con el AE.** El feedback del AE sobre los SQL es tu mejor QA de calificación (ver `78`).

## Siguiente paso

Instala el 1:1 semanal con estructura fija y arranca una biblioteca de swipe compartida. Usa `83` en cada 1:1 para elegir el foco de la semana con datos. Cuando tengas varios SDRs, el coaching se organiza por pods → `88`; y todo esto es lo que te permite escalar sin perder calidad → `89`. El desarrollo de la habilidad de *cerrar* (para cuando un SDR asciende a AE) → `ventas_lushows`.
