# 138 — Farmacovigilancia y eventos adversos (qué hacer cuando alguien dice "me cayó mal")

Un día un cliente escribe: *"tomé sus cápsulas y me dio dolor de estómago"*. Lo que hagas en las siguientes
dos horas define si eso queda como un dato que te salva de un problema mayor, o como un mensaje borrado que
reaparece dentro de un año en una queja formal. La farmacovigilancia es el oficio de recibir, registrar,
evaluar y actuar sobre esos reportes. No es burocracia: es el único sistema que detecta un problema de un
lote **antes** de que se vuelva un problema de la marca. El error caro que evita: no tener muestra de
retención ni trazabilidad de lote cuando llega el primer reporte serio, y quedarte sin poder demostrar nada.

Términos: **evento adverso (adverse event, AE)** = cualquier cosa desagradable que le ocurre a alguien que
consumió el producto, **haya o no** relación causal. **Reacción adversa (adverse drug reaction, ADR)** = AE
en el que sí se sospecha relación causal. **Evento adverso serio (serious adverse event, SAE)** = muerte,
amenaza para la vida, hospitalización o su prolongación, discapacidad persistente, anomalía congénita, o
intervención necesaria para evitar cualquiera de las anteriores. **Señal (signal)** = patrón que sugiere una
asociación nueva. **Muestra de retención (retention sample)** = porción guardada de cada lote.

## Serio no es lo mismo que grave

Es la confusión #1 y cambia obligaciones legales:

```
"GRAVE"  = intensidad del síntoma (leve / moderado / grave)     → juicio clínico
"SERIO"  = criterio REGULATORIO de la lista de arriba           → dispara obligaciones y plazos

Un dolor de cabeza puede ser GRAVE (muy intenso) y no ser SERIO.
Una hospitalización de 24 h por precaución es SERIA aunque el síntoma haya sido leve.
```

## Los cuatro datos mínimos de un reporte válido

Sin estos cuatro elementos, el reporte no es evaluable. Se piden siempre, en el mismo orden:

1. **Un paciente identificable** (iniciales, edad, sexo — no hace falta nombre completo).
2. **Un reportante identificable** (quién avisa: el consumidor, un familiar, un profesional de salud).
3. **Un producto sospechoso**, con **lote** y fecha de vencimiento. Sin lote, no hay investigación posible.
4. **Un evento** descrito, con fecha de inicio.

Y cinco datos que multiplican el valor del reporte: dosis y frecuencia usada, tiempo desde la toma hasta el
evento, otros medicamentos o suplementos concomitantes (`139`), antecedentes relevantes, y qué pasó al
suspender (**dechallenge**) y, si ocurrió, al volver a tomar (**rechallenge**).

## Cómo se evalúa la causalidad

No se decide por intuición. Hay dos marcos estándar y ambos se pueden aplicar sin ser médico —aunque la
conclusión clínica la firma un profesional de salud:

| Marco | Cómo funciona | Categorías |
|---|---|---|
| **WHO-UMC** | Juicio estructurado sobre plausibilidad temporal, alternativas, dechallenge y rechallenge | Cierta · Probable · Posible · Improbable · Condicional · Inclasificable |
| **Algoritmo de Naranjo** | Cuestionario de 10 preguntas con puntaje | ≥9 definida · 5–8 probable · 1–4 posible · ≤0 dudosa |

Las preguntas que más peso tienen en ambos: ¿el tiempo encaja? ¿hay otra causa evidente (otro medicamento,
una gripa, comida)? ¿mejoró al suspender? ¿reapareció al retomar? ¿está descrito en la literatura para ese
ingrediente?

Honestidad obligatoria: en suplementos la causalidad casi nunca llega a "cierta", porque no hay rechallenge
controlado y suele haber cointervenciones. **"Posible" es un resultado válido y no es una derrota.** Lo que
sí es inaceptable es no evaluar.

## El marco regulatorio — a agosto de 2026

| Jurisdicción | Qué aplica a suplementos | Obligación práctica |
|---|---|---|
| **Estados Unidos** | Dietary Supplement and Nonprescription Drug Consumer Protection Act (2006), sobre DSHEA | Reportar a la FDA los **eventos adversos serios en 15 días hábiles**, incluir una dirección o teléfono de contacto en la etiqueta y **conservar los registros 6 años**. Los no serios se guardan pero no se reportan |
| **Estados Unidos — voluntario** | **CAERS** (CFSAN Adverse Event Reporting System) | Base pública donde consumidores y profesionales reportan; se puede consultar por ingrediente |
| **Unión Europea** | Vigilancia de complementos alimenticios vía autoridades nacionales; EudraVigilance es de medicamentos | Sin sistema centralizado equivalente al de medicamentos; nutrivigilancia nacional en varios países |
| **Colombia** | Programa Nacional de Farmacovigilancia del INVIMA (Resolución 1403 de 2007) — construido para **medicamentos** y aplicable a fitoterapéuticos; para **suplementos dietarios** el marco es el Decreto 3249 de 2006 y la vigilancia sanitaria general | No asumas que "no aplica": el titular del registro responde por la seguridad del producto. **Verificar con INVIMA la vía de reporte vigente para tu categoría** (`266`, `269`) |
| **Global** | **VigiBase** (Uppsala Monitoring Centre, OMS) | Base mundial donde se detectan señales |

Lectura estratégica: aunque tu categoría no tenga una obligación de reporte tan detallada como la de un
medicamento, **el sistema interno te conviene igual**. Es lo que convierte "tres clientes se quejaron" en
"los tres reportes son del lote 2026-041, revisemos su contramuestra".

## El sistema mínimo viable para una marca pequeña

```
1) CANAL ÚNICO de recepción
   WhatsApp, correo y formulario web caen todos en el MISMO registro. Nadie contesta y borra.

2) FORMATO DE REGISTRO (una hoja o una tabla, con estos campos)
   fecha_reporte · reportante · paciente(edad,sexo) · producto · LOTE · vencimiento · dosis
   fecha_inicio_evento · descripción · concomitantes · dechallenge · rechallenge · serio(S/N)
   causalidad(WHO-UMC) · acciones · fecha_cierre

3) TRAZABILIDAD DE LOTE hacia adelante y hacia atrás  (`168`)
   De ese lote: qué materia prima, qué COA, a qué clientes se despachó.

4) MUESTRA DE RETENCIÓN de cada lote, guardada en las condiciones de la etiqueta  (`61`)
   Sin contramuestra no hay contraprueba, y sin contraprueba la discusión se decide por quién grita más.

5) TRIAGE en 24 h
   ¿Es serio? → escalar, evaluar retiro (recall), documentar. ¿No serio? → registrar y monitorear.

6) ANÁLISIS DE TENDENCIA mensual
   Reportes por 1.000 unidades vendidas, agrupados POR LOTE y POR SÍNTOMA. Un pico en un lote es una señal.

7) REVISIÓN ANUAL documentada
   Qué se reportó, qué se hizo, qué cambió en el producto o en la etiqueta.
```

Detección de señal, en versión honesta para una marca pequeña: no vas a calcular PRR ni ROR (las medidas de
desproporcionalidad que usan las agencias con millones de reportes). Lo que sí puedes hacer es **normalizar
por unidades vendidas** y mirar la concentración por lote. Tres reportes en 200 frascos de un lote es una
señal; tres reportes en 20.000 frascos repartidos en dos años, probablemente no.

## Qué se hace con la información

| Hallazgo | Acción |
|---|---|
| Reportes concentrados en un lote | Analizar la contramuestra: contaminación microbiológica (`100`), micotoxinas (`101`), metales (`136`), identidad (`245`). Evaluar bloqueo del lote y retiro |
| Reportes repartidos en todos los lotes | El problema es de la fórmula, la dosis o la población, no del lote. Revisar dosis (`161`) y advertencias |
| Interacción sospechada con un medicamento | Revisar el mecanismo y la literatura (`139`, `124`). Considerar advertencia en etiqueta |
| Reacción alérgica | Ir al alérgeno y a la contaminación cruzada (`137`) |
| Evento serio | Escalar de inmediato, documentar, evaluar retiro y notificar a la autoridad según la vía vigente |

Todo cambio que salga de esto —advertencia nueva, dosis distinta, proveedor distinto— pasa por control de
cambios documentado (`169`). Un cambio sin documentar es un cambio que no ocurrió, a los ojos de un auditor.

## Ejemplo aplicado — tres reportes en dos semanas

**(ILUSTRATIVO)** Marca de extracto de reishi en cápsulas:

```
Reportes: 3 casos de molestia gastrointestinal (náusea, distensión), inicio 1–2 h tras la toma,
          mejoraron al suspender (dechallenge positivo), ninguno serio.
Lotes   : los tres del lote 2026-041. Unidades del lote: 480 frascos → 3/480 = 0,63 %
          Lotes anteriores: 0 reportes en ~2.100 frascos.

Investigación con la contramuestra del 2026-041:
  Microbiología (`100`) ....... conforme
  Metales por ICP-MS (`88`) ... conforme
  β/α-glucano (`221`) ......... α-glucano 27,4 % vs 6,1 % histórico   ← EL HALLAZGO
  Identidad ITS (`245`) ....... Ganoderma confirmado
Conclusión: el lote se hizo con materia prima de un proveedor nuevo, con mucho más sustrato/almidón.
Causalidad WHO-UMC: POSIBLE. Acción: bloquear el lote, volver al proveedor validado, agregar el
α-glucano como criterio de aceptación de entrada (`141`), control de cambios documentado (`169`).
```

Fíjate en lo que hizo posible todo esto: el lote estaba en el reporte, existía la contramuestra y existía un
histórico de α-glucano contra el cual comparar. Sin esas tres cosas, la conclusión habría sido "quién sabe".

## Errores comunes

- Borrar o esconder comentarios negativos. Además de deshonesto, destruye la única evidencia temprana que
  tenías (`03`).
- No pedir el lote. Sin lote no hay investigación, solo opinión.
- No guardar muestra de retención, o guardarla en peores condiciones que el producto en venta.
- Confundir "serio" con "grave" y no escalar un caso que legalmente sí lo era.
- Responder con un diagnóstico o con consejo médico. No eres el tratante: registras, evalúas causalidad y
  remites a un profesional de salud.
- Contar reportes en absoluto, sin normalizar por unidades vendidas. Crecer en ventas sube los reportes sin
  que nada haya empeorado.
- Suponer que "natural" implica "sin eventos adversos". La categoría no cambia la biología (`132`, `250`).
- No cerrar el ciclo: investigar, no cambiar nada y no dejarlo escrito. Un hallazgo sin acción documentada
  es peor que no haber investigado, porque prueba que sabías.

## Conexión con otros módulos

→ `250-seguridad-e-interacciones-de-hongos.md` — qué se ha reportado con hongos funcionales.
→ `209-seguridad-interacciones-y-contraindicaciones.md` — el equivalente en cannabis.
→ `139-interacciones-planta-farmaco.md` — la causa más probable detrás de un evento en un usuario polimedicado.
→ `137-alergenos-e-hipersensibilidad.md` — la otra gran familia de eventos.
→ `168-documentacion-de-lote-y-trazabilidad.md` — sin esto, la farmacovigilancia no funciona.
→ `169-control-de-cambios-y-desviaciones.md` — cómo se documenta lo que se cambia después.
→ `260-screening-de-seguridad-y-contraindicaciones.md` — el modelo riguroso, tomado de la investigación clínica.
→ `295-checklist-de-calidad-quimica.md` — dónde entra este sistema en el conjunto.
