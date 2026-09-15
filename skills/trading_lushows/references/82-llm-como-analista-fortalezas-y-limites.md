# 82 — El LLM como analista: fortalezas y límites

Un **LLM** (modelo de lenguaje, como Claude) es un motor de razonamiento sobre texto. En un bot
de trading puede ser un analista excelente o un desastre caro — depende de si se le asignan las
tareas correctas. Este módulo traza esa línea sin humo.

## Lo que un LLM hace BIEN

| Fortaleza | Ejemplo en trading |
|---|---|
| **Sintetizar contexto heterogéneo** | Combinar régimen + RSI/MACD + lecciones pasadas + estructura de velas en UN juicio coherente — eso es literalmente el prompt de convicción |
| **Razonar sobre reglas** | "El régimen es risk-off y hay una lección en contra de este setup → aunque el técnico sea alcista, convicción baja" |
| **Explicar sus decisiones** | El campo `reasoning` permite auditar CADA trade — un modelo estadístico clásico da un número sin explicación |
| **Clasificar con matices** | Etiquetar régimen de mercado leyendo un resumen, tolerando ambigüedad |
| **Detectar patrones narrativos** | El meta-análisis que encontró el patrón FOMO 0/3 leyendo su propia semana (módulo 84) |

## Lo que un LLM hace MAL (y no se arregla con mejores prompts)

| Límite | Por qué | Consecuencia si lo ignoras |
|---|---|---|
| **Aritmética** | Genera texto plausible, no calcula; puede errar un RSI o un tamaño de posición y sonar seguro | Un sizing mal calculado = riesgo real equivocado. Por eso TODO número del bot se calcula en JS |
| **Predecir precios** | El precio futuro no está en sus datos de entrenamiento ni en ningún patrón textual estable. NADIE — humano o IA — predice precios consistentemente | Preguntarle "¿a cuánto llega BTC?" produce ficción con tono de informe |
| **Datos frescos** | Su conocimiento tiene fecha de corte; no sabe el precio de hoy ni la noticia de ayer salvo que se lo pases en el prompt | Alucina contexto de mercado si no se lo das explícito |
| **Consistencia perfecta** | El mismo input puede dar 7 hoy y 8 mañana (variabilidad de muestreo) | Decisiones limítrofes oscilan; se mitiga con formato estricto, escala anclada y umbrales con margen |
| **Saber que no sabe** | Tiende a responder con confianza aunque el caso sea ambiguo | Sin regla "en la duda, HOLD/convicción baja", la ambigüedad se vuelve trades |

## La división de trabajo correcta

**Los números se calculan en JS; Claude interpreta.** El bot calcula RSI, MACD, SMAs, tamaños y
stops en código determinista y testeable (145 tests), y le pasa los resultados a Claude como
contexto. Claude nunca produce un número operativo — produce un JUICIO (`conviction`, `action`,
`reasoning`) que luego el código valida y convierte en órdenes.

La analogía: Claude es el analista senior que lee el reporte y opina; JS es el back office que
hace las cuentas y ejecuta. Jamás dejes al analista sumando la caja.

## Cómo aplica al AGENTE TRADING

- El pipeline entero respeta esta división: técnico (JS) → convicción (Sonnet) → sizing (JS).
- El bot NO le pregunta a Claude "¿va a subir BTC?"; le pregunta "dado este régimen, este técnico
  y estas lecciones, ¿qué tan fuerte es ESTE setup del 1 al 10?" — juicio sobre evidencia
  presente, no adivinación del futuro.
- Cuando alguien proponga "que Claude calcule X" o "que Claude prediga Y", este módulo es el
  filtro: ¿es síntesis/juicio/explicación (sí) o aritmética/predicción/dato fresco (no — va a JS
  o no va)?
