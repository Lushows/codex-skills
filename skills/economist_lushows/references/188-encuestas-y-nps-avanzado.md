# 188 — Encuestas y NPS avanzado

Medir bien satisfacción y lealtad para que el feedback se convierta en decisiones, no en gráficos bonitos que nadie usa. Aquí ves qué métrica usar, cómo preguntar sin sesgar, y cómo actuar.

## Las 3 métricas que importan (y cuándo usar cada una)

| Métrica | Qué mide | Pregunta núcleo | Cuándo usarla |
|---|---|---|---|
| **NPS** (Net Promoter Score) | Lealtad / probabilidad de recomendar | "Del 0 al 10, ¿qué tan probable es que recomiendes [marca] a un amigo?" | Salud de la relación a largo plazo. Periódico (trimestral). |
| **CSAT** (Customer Satisfaction) | Satisfacción con UNA interacción | "¿Qué tan satisfecho quedaste con [esta compra/atención]?" (1-5) | Justo después de un evento: compra, entrega, soporte. |
| **CES** (Customer Effort Score) | Cuánto esfuerzo le costó al cliente | "¿Qué tan fácil fue resolver tu problema?" (1-7) | Procesos: soporte, devoluciones, checkout. Mejor predictor de recompra que NPS. |

Regla simple: **CSAT y CES** miden el momento (transaccional); **NPS** mide la relación (relacional). No mezcles las tres en una sola encuesta larga — bajas la tasa de respuesta.

## Cómo se calcula el NPS (ejemplo numérico)

El cliente responde 0-10 y se clasifica:
- **Promotores**: 9-10 (te aman, te recomiendan)
- **Pasivos**: 7-8 (satisfechos pero no leales)
- **Detractores**: 0-6 (insatisfechos, hablan mal de ti)

**Fórmula:** NPS = % Promotores − % Detractores. Los pasivos NO suman ni restan, pero sí cuentan en el total.

**Ejemplo ilustrativo** (cifras inventadas para mostrar el método):
- 100 respuestas. 55 promotores (9-10), 30 pasivos (7-8), 15 detractores (0-6).
- % Promotores = 55/100 = 55%
- % Detractores = 15/100 = 15%
- **NPS = 55 − 15 = +40**

El NPS va de −100 a +100. No es un porcentaje, es un número. Un "+40" se lee "NPS de cuarenta", nunca "40%".

### Cómo interpretarlo sin engañarte
- Lo absoluto importa poco; **tu propia tendencia** importa mucho. Subir de +30 a +45 en 6 meses es la señal real.
- Pregúntate país/sector: el NPS "bueno" varía enormemente entre banca, retail y software. No copies un benchmark de internet como verdad — consíguelo de tu sector real (ver 21).
- Con **menos de ~30 respuestas** el número baila demasiado; trátalo como cualitativo, no como dato duro.

## La pregunta abierta es donde está el oro

El número solo te dice *cuánto*; la pregunta que sigue te dice *por qué* y *qué arreglar*:
- A promotores (9-10): "¿Qué es lo que más valoras?" → tu mensaje de marketing sale de aquí (ver 25, 129).
- A pasivos (7-8): "¿Qué nos faltó para darnos un 9 o 10?" → tu hoja de ruta de mejoras.
- A detractores (0-6): "¿Qué salió mal?" → tu prevención de fuga (churn, ver 89).

Sin la pregunta abierta, el NPS es un termómetro sin diagnóstico. Inútil para decidir.

## Diseñar preguntas SIN sesgo (lista negra)

- **Preguntas que dirigen la respuesta**: "¿Qué tanto te encantó nuestro servicio excepcional?" → induce. Neutro: "¿Cómo describirías nuestro servicio?".
- **Doble pregunta en una**: "¿Fue rápida y amable la atención?" → si fue rápida pero grosera, no sabe qué responder. Sepáralas.
- **Escalas desbalanceadas**: 3 opciones positivas y 1 negativa inflan el resultado. Usa escalas simétricas.
- **Jerga**: pregunta en el idioma del cliente, no en el tuyo.
- **Encuesta eterna**: cada pregunta extra baja la tasa de respuesta. Apunta a < 2 minutos.
- **Sesgo de momento**: si preguntas justo después de un descuento, el ánimo está alto. Controla *cuándo* preguntas.
- **Anonimato mal puesto**: si pides datos sensibles sin anonimato, responden lo "correcto", no lo real.

## Trampas estadísticas que distorsionan el resultado

- **Sesgo de no-respuesta**: responden sobre todo los muy contentos y los muy molestos; el "medio" calla. Tu NPS puede verse más extremo de lo real.
- **Cherry-picking de canal**: encuestar solo a quienes abren el email excluye a los desconectados (que suelen ser detractores).
- **Promediar el NPS de varios meses**: no se promedia un promedio sin ponderar por número de respuestas. Recalcula sobre el total.
- **Confundir señal con ruido**: un movimiento de ±5 con pocas respuestas casi siempre es azar.

## Actuar sobre el feedback (el "Close the Loop")

El 80% del valor está en cerrar el ciclo, no en medir:

1. **Loop interno (días):** contacta a cada detractor que dejó datos. Una llamada honesta recupera más clientes que cualquier campaña. Pregunta, repara, ofrece solución concreta.
2. **Loop externo (semanas):** agrupa los "por qué" en 3-5 temas. ¿Qué problema se repite? Ese es tu próximo proyecto de mejora.
3. **Loop estructural (trimestre):** lleva los 2-3 temas más caros a la dirección. Cambia procesos, no solo apaga incendios.

### Mini-checklist de implementación
- [ ] Elegí UNA métrica por momento (CSAT post-compra, CES post-soporte, NPS trimestral).
- [ ] Cada encuesta tiene la pregunta numérica + UNA abierta.
- [ ] Defino umbral de alerta (ej. cualquier 0-3 dispara un contacto en 48h).
- [ ] Asigné un responsable de leer las respuestas cada semana (si nadie lee, no midas).
- [ ] Etiqueto los "por qué" en categorías para verlos como tendencia, no caso a caso.

## Conectar el NPS con dinero (lo que de verdad convence)

Una métrica de "sentimiento" sin plata detrás no mueve decisiones. Liga NPS a comportamiento real:
- ¿Los promotores recompran más / tienen mayor LTV que los detractores? (ver 89 para churn y LTV).
- ¿Cuántas referencias reales trajo cada promotor? Mide, no asumas.

**Ejemplo ilustrativo:** si un promotor compra en promedio 4 veces/año y un detractor 1.2, y tienes 200 clientes, subir 10 detractores a promotores podría sumar ~28 compras extra/año. Calcula el tuyo con tus datos reales, no con estos.

## Cuándo y cada cuánto preguntar

- **Transaccional (CSAT/CES):** automático, justo después del evento. Inmediato = memoria fresca.
- **Relacional (NPS):** cada 3-6 meses. Más seguido satura ("fatiga de encuestas") y baja la respuesta.
- **No encuestes al mismo cliente dos veces en pocas semanas.** Lleva control.

## Errores comunes

- Medir y no hacer nada: la peor opción; el cliente respondió esperando ser escuchado.
- Obsesionarse con el número y olvidar la pregunta abierta.
- Comparar tu NPS contra benchmarks de otro país/sector como si fueran ley (verifica el real, ver 21).
- Encuestas larguísimas que matan la tasa de respuesta.
- Premiar al equipo por subir el NPS → empiezan a "rogar" notas altas y contaminan el dato.
- Confundir satisfacción (momento) con lealtad (relación): un cliente puede estar satisfecho hoy y aun así irse.
- Sacar conclusiones con 10 respuestas.

## Siguiente paso típico

Elige UNA métrica para tu momento más crítico (normalmente CSAT post-entrega o post-soporte), lanza una micro-encuesta de 2 preguntas (número + "¿por qué?"), y agenda media hora cada semana para leer respuestas y llamar a cada detractor. Cuando tengas ritmo, agrega el NPS trimestral y conéctalo a recompra (ver 89) y a tu mensaje de marca (ver 25, 129).
