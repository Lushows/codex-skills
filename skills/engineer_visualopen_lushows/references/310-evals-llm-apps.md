# 310 · Evals de apps LLM (golden sets, LLM-as-judge, regression, online, métricas)

> "Mejoré el prompt" sin números es fe, no ingeniería. Las evals convierten un sistema no-determinista
> en algo que puedes **versionar, comparar y bloquear en CI**. Sin evals no iteras: adivinas.

Aplica a RAG ([[307-rag-en-produccion-a-fondo]]), agentes ([[308-agentes-produccion-orquestacion]]) y
cualquier feature LLM. Complementa la observabilidad de [[58-observabilidad-llm-llmops]].

## Pirámide de evals
| Nivel | Qué mide | Coste | Cuándo |
|---|---|---|---|
| **Assertions/reglas** | formato, JSON válido, regex, longitud, ausencia de PII | ~0 | cada request |
| **Golden set** | precisión vs respuestas esperadas | medio | en CI, cada cambio |
| **LLM-as-judge** | calidad subjetiva (útil, coherente, fiel) | alto | en CI + muestreo online |
| **Online/human** | satisfacción real, 👍/👎, tasa de escalado | continuo | en producción |

Empieza por abajo: las assertions baratas atrapan el 50% de los bugs sin gastar un token de juez.

## Golden set (el activo más valioso)
- 50-300 casos `input → output_esperado` (o rúbrica). Cúbrelos: casos felices, edge cases, los bugs ya
  vistos (cada incidente de prod entra al set como test de regresión).
- **Versionado en git**, no en una hoja de cálculo. Corre en CI; un PR que baje una métrica clave no mergea.
- **Curado, no aleatorio**: 100 casos bien elegidos baten a 10.000 random. Incluye los que el sistema
  falla hoy para medir el avance real.

## LLM-as-judge (escala lo que un humano no puede)
- Un LLM puntúa la salida contra una **rúbrica explícita** (1-5 o pass/fail con criterios). Más barato y
  rápido que anotación humana; correlaciona bien si la rúbrica es concreta.
- **Buenas prácticas**: criterios binarios y específicos > escalas vagas; pide **razonamiento antes del
  score** (juez con CoT); usa un modelo fuerte como juez; **few-shot** con ejemplos calibrados.
- **Sesgos a corregir**: *position bias* (favorece la 1ª opción en comparaciones → aleatoriza orden y
  promedia A-B/B-A), *length bias* (premia respuestas largas), *self-preference* (un modelo se prefiere
  a sí mismo → juez de familia distinta). **Calibra el juez contra labels humanos** antes de confiar en él.

## Métricas por tipo de app
- **RAG**: RAGAS — faithfulness (~0.75), answer-relevance, context-precision (~0.7), context-recall.
  Léelas como **panel de 4**: subir una a costa de otra (menos chunks ↑precision pero ↓recall) es trampa.
- **Agentes**: trajectory eval (¿secuencia eficiente?), tool-correctness (¿tool y args correctos?),
  task-success (¿completó el objetivo?), pasos/coste por tarea.
- **Generación libre**: faithfulness/groundedness, toxicidad, formato, adherencia a instrucciones.
- **Clasificación/extracción**: precision/recall/F1 clásicos contra labels — aquí no necesitas juez LLM.

## Regression testing en CI
- Cada commit que toca prompt, modelo, chunker, k o tools dispara el golden set. **Gating**: bloquea si
  faithfulness o task-success caen del umbral. Trátalo como tests unitarios.
- **Ojo al no-determinismo**: `temperature=0` no garantiza salida idéntica. Usa umbrales con margen y
  promedia N corridas para métricas ruidosas, no asserts de igualdad exacta.
- Frameworks 2026: **RAGAS** (RAG), **DeepEval** (pytest-style, suites unitarias), **Promptfoo**
  (matriz prompt×modelo, side-by-side), **Braintrust/LangSmith/Langfuse** (datasets + tracing + CI).

## Online evals (producción es el único set real)
- **Sampling**: puntúa con juez un % del tráfico vivo; alerta si una métrica deriva (model/data drift).
- **Feedback implícito y explícito**: 👍/👎, reintentos, abandono, escalado a humano. Alimenta el golden set.
- **Guardrail metrics en vivo**: tasa de alucinación detectada, de PII filtrada, de jailbreak bloqueado ([[311-guardrails-safety-llm-apps]]).
- Traza cada eval a su request (Langfuse/LangSmith) para inspeccionar exactamente qué pasó en los fallos.

## Gotchas
1. **Optimizar la métrica del juez en vez del producto** (Goodhart): el juez es proxy; valida con humanos periódicamente.
2. **Golden set que se pudre**: si el dominio cambió, mides contra un pasado irrelevante. Revísalo.
3. **Una sola métrica miente**: agrega varias; faithfulness alta con relevance baja = responde fiel pero inútil.
4. **Eval solo offline**: el golden set nunca cubre la cola larga de prod. Sin online evals, no ves el drift.
5. **Juez sin calibrar**: un juez no validado contra humanos puede estar sistemáticamente sesgado y no lo sabrás.

Cruza con [[58-observabilidad-llm-llmops]], [[164-evals-calidad-avatar-video]], [[307-rag-en-produccion-a-fondo]] y [[308-agentes-produccion-orquestacion]].
