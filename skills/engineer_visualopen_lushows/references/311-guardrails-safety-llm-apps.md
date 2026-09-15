# 311 · Guardrails y safety en apps LLM (I/O validation, jailbreak, PII, hallucination)

> El modelo hará lo que le pidan: si un atacante lo pide, también. Los guardrails son la capa de
> **defensa en profundidad** alrededor del LLM — validan lo que entra, lo que sale y lo que hace.

Distinto de la seguridad del agente/infra ([[28-seguridad-ia-agentes-llm]]); aquí va el filtro de
contenido y comportamiento en runtime. OWASP LLM Top 10 2026 lidera con **prompt injection,
sensitive-information-disclosure y excessive-agency**.

## El sándwich: validación de entrada y salida
```
input → [input guardrails] → LLM/agente → [output guardrails] → usuario
```
Guardrails de **entrada**: detectar prompt injection, off-topic, PII en la query, abuso/toxicidad,
longitud. Guardrails de **salida**: PII filtrada, toxicidad, alucinación, formato, fuga de system prompt.
Nunca confíes solo en uno: el de entrada falla con ataques nuevos; el de salida atrapa lo que pasó.

## Prompt injection (el problema sin solución limpia)
| Tipo | Vector | Defensa |
|---|---|---|
| **Directa** | el usuario escribe "ignora tus instrucciones" | clasificador + system prompt robusto |
| **Indirecta** | instrucción oculta en un doc/web que el agente procesa | tratar datos como datos, sandbox, no ejecutar |
| **Multi-turno** | el ataque se arma a lo largo de varios mensajes | dialog rails que rastrean la conversación |

- **Llama Prompt Guard 2 (86M)** como primer filtro rápido y barato; **Llama Guard 3 (8B)** para
  clasificación de hazards detallada. Combínalos: gate veloz + clasificador profundo.
- **Separa instrucción de datos**: el contenido recuperado (RAG) o de tools va en un bloque claramente
  marcado como *datos no confiables*, nunca como instrucciones. Es el mayor mitigante de injection indirecta.
- **Excessive agency**: no le des al agente tools destructivas sin confirmación. Una injection que solo
  puede *leer* es molesta; una que puede *borrar/pagar* es catastrófica. Mínimo privilegio en las tools.

## PII y datos sensibles
- **Detección+redacción** con **Presidio** (integrado en NeMo Guardrails y Guardrails AI Hub): reconoce
  emails, teléfonos, tarjetas, IDs. Redacta en entrada (no se loguea) y en salida (no se filtra).
- **No loguees prompts crudos** con PII; redacta antes de enviar a observabilidad/trazas.
- **Data-leakage del system prompt**: el output guardrail detecta si el modelo está recitando sus
  instrucciones o secretos. Nunca metas claves/credenciales en el prompt.

## Hallucination guards (sobre todo en RAG)
- **Groundedness/faithfulness check**: tras generar, un verificador comprueba que cada claim se apoya en
  el contexto recuperado. Si una frase no tiene soporte → recórtala, márcala o regenera ([[307-rag-en-produccion-a-fondo]]).
- **Citation enforcement**: obliga a citar `chunk_id`; sin cita verificable, no se sirve el claim.
- **Abstención**: entrena/instruye al modelo a decir "no lo sé" cuando el contexto no cubre la pregunta.
  Una abstención es infinitamente mejor que una respuesta inventada con confianza.

## Frameworks 2026
- **NeMo Guardrails** (NVIDIA): dialog rails que modelan la conversación completa → atrapa injection
  multi-turno que un clasificador de un turno se pierde. v0.17 (oct-2025) es la estable; NVIDIA marca el
  proyecto como **no recomendado para producción tal cual** en su estado beta — úsalo con criterio.
- **Guardrails AI** (Hub de validadores componibles: PII, toxicidad, competidores, regex).
- **LLM Guard** (open-source, scanners de input/output: injection, secretos, sentimiento, tokens).
- **LlamaFirewall** (Meta): sistema open para agentes — alignment-check, prompt-guard, code-scanner.
- **OpenAI Guardrails API**: clasificadores de seguridad gestionados.
- Stack típico de prod: NeMo orquestando Llama Prompt Guard 2 (gate rápido) + Llama Guard 3 (hazards) +
  Presidio (PII) + faithfulness check propio.

## Cómo desplegarlos sin matar la latencia
- Corre los guardrails **baratos en paralelo** (clasificador 86M en GPU/CPU aparte), no en serie sobre el
  camino caliente. El gate rápido decide en ms; el clasificador pesado solo si el gate duda.
- **Fail-closed para acciones críticas** (pagos, borrados), **fail-open con log para lo informativo** —
  no bloquees toda la app porque el guardrail tuvo un timeout.
- **Mide los guardrails como evals** ([[310-evals-llm-apps]]): falsos positivos (bloqueas usuarios legítimos)
  y falsos negativos (dejas pasar ataques). Un guardrail con 30% de FP es inservible aunque sea "seguro".

## Gotchas
1. **Guardrail = otro LLM = otra superficie de ataque**: el clasificador también es jailbreakeable; capas, no bala de plata.
2. **Bloqueo solo en entrada**: los ataques nuevos esquivan tu lista; el guardrail de salida es la red final.
3. **Sobre-bloquear** frustra usuarios reales y los empuja a evadirte; calibra umbrales con datos.
4. **PII redactada en el LLM pero no en logs/trazas**: la fuga ocurre en la observabilidad, no en la respuesta.
5. **Confiar en el prompt de sistema** ("nunca reveles X") como única defensa: es persuasión, no control. Añade clasificadores.

Cruza con [[28-seguridad-ia-agentes-llm]], [[249-adversarial-jailbreak-image-models]], [[310-evals-llm-apps]] y [[308-agentes-produccion-orquestacion]].
