# 81 — Diseño de prompts para trading

Un **prompt** es la instrucción que se le da al modelo de IA. En un bot de trading, el prompt es
el equivalente al reglamento de un empleado: si está ambiguo, el empleado improvisa — y en trading
improvisar cuesta plata. Este módulo es la anatomía de un buen prompt de decisión.

## Las 5 piezas de un prompt de decisión de trading

| Pieza | Qué hace | Error típico si falta |
|---|---|---|
| **Rol** | "Eres un analista de régimen macro" / "Piensas como Druckenmiller" — fija el marco mental y el nivel de exigencia | Respuestas genéricas de "depende del mercado" |
| **Reglas duras** | Lo NO negociable: "nunca recomiendes más de X", "si el régimen es unknown, convicción máxima 3", "penaliza entradas extendidas" | El modelo decide "razonablemente" cosas que debían estar prohibidas (el FOMO 0/3 nació de una regla ausente) |
| **Contexto de datos** | Los números YA calculados en JS: RSI, MACD, SMAs, resumen de velas, régimen, lecciones de memoria | El modelo "estima" indicadores → números inventados |
| **Formato de salida** | JSON estricto con campos y rangos definidos: `{"conviction": 1-10, "action": "BUY|HOLD", "reasoning": "..."}` | Texto libre imposible de parsear → el código no puede actuar |
| **Ejemplos** | 1-2 casos resueltos (setup fuerte → 9, setup ambiguo → 4) que calibran la escala | Cada llamada interpreta "convicción 7" distinto |

## Principios que separan un prompt bueno de uno decorativo

1. **El prompt PIDE, el código VERIFICA.** Nunca asumas que el modelo obedecerá el formato o los
   rangos: valida el JSON, valida que conviction ∈ [1,10], y rechaza lo inválido (módulo 85).
2. **Escala anclada, no adjetivos.** "Convicción alta" no significa nada; "9-10 = confluencia de
   régimen + técnico + sin lecciones en contra; 1-3 = señales contradictorias" sí.
3. **Pedir razones EN CONTRA.** Obligar al modelo a listar qué invalidaría el trade combate el
   sesgo de confirmación del propio prompt.
4. **Una decisión por prompt.** Régimen es UNA pregunta (clasificar); convicción es OTRA (juzgar).
   Mezclarlas degrada ambas y encarece la barata.
5. **Versionar y medir.** Cambiar un prompt es cambiar el sistema: se anota la versión, se compara
   contra la anterior con casos (módulo 89), nunca se "retoca y a ver qué pasa".

## Los dos prompts reales del bot

- **Régimen (`macroRegime`, Haiku)**: clasificación pura. Recibe resumen de mercado, devuelve UNA
  etiqueta de un conjunto cerrado: `risk-on | risk-off | trending-up | trending-down | ranging`.
  Sin thinking, sin creatividad: tarea barata para modelo barato.
- **Convicción (`druckenmiller`, Sonnet + adaptive thinking)**: juicio. Recibe régimen + técnico
  (JS) + lecciones de `traderMemory`, y devuelve JSON con `conviction` 1-10, acción y razonamiento.
  El nombre no es decoración: el marco Druckenmiller ordena concentrar solo cuando TODO confluye —
  por eso el umbral de auto-ejecución es 8, no 6.

## Cómo aplica al AGENTE TRADING

- La lección FOMO es la lección de prompts: lo que el prompt no prohíbe explícitamente, el modelo
  lo hará cuando el contexto lo sugiera. Las reglas duras se escriben ANTES de que duelan.
- Todo cambio de prompt pasa por el proceso del módulo 84 (backlog, en frío) y se evalúa con el
  método del módulo 89 (casos históricos, comparación vieja vs nueva).
