# 88 — Costos de IA en trading: economía de tokens

Un bot que usa IA paga por **tokens** (los pedacitos de texto que el modelo lee y escribe;
~3-4 caracteres por token en español). En trading esto crea una tensión sana: el bot analiza
muchas veces y opera pocas, así que el costo de IA es por ANÁLISIS, no por trade. Si no se
diseña, la factura crece con el reloj, no con las ganancias.

## El principio: el modelo caro solo para la decisión cara

No todas las tareas del pipeline valen lo mismo. Clasificar un régimen de mercado en
trending-up / lateral / bajista es una tarea simple; decidir una entrada con contexto técnico,
memoria y psicología es la decisión que arriesga plata. Asignar modelos según eso:

| Tarea | Modelo | Lógica |
|---|---|---|
| Clasificar régimen (c/2h) | Haiku (barato, rápido) | Tarea simple y frecuente: la hace bien un modelo chico |
| Decidir convicción de entrada | Sonnet (capaz) | Decisión de dinero: aquí no se escatima |
| Calcular indicadores | JS puro (gratis) | Los números NUNCA se le piden a la IA (ver `04`) |

Este ruteo por dificultad suele recortar la mayor parte del costo sin tocar la calidad de la
decisión final, porque la llamada frecuente es la barata y la cara es la escasa.

## Adaptive thinking: pagar por pensar solo cuando hay que pensar

Los modelos con razonamiento pueden "pensar" más o menos según la dificultad. Pensar cuesta
tokens de salida. La configuración sana: presupuesto de pensamiento acotado, generoso solo en
la llamada de convicción (donde un razonamiento mejor puede cambiar la decisión) y mínimo en
tareas mecánicas. Señal de despilfarro: razonamientos larguísimos para concluir "mercado
lateral, no operar" — eso debía resolverlo la capa barata.

## Caching: cuándo aplica y cuándo no

El **prompt caching** descuenta la parte REPETIDA del prompt entre llamadas (el proveedor la
recuerda y cobra una fracción por releerla). Pero tiene un mínimo: prompts por debajo del
umbral de cacheo (en Claude, 2048 tokens por bloque en los modelos grandes) no son cacheables.

Caso real del AGENTE TRADING: sus prompts son cortos (<2048 tokens) → **el caching no aplica y
no vale la pena engordar el prompt solo para alcanzar el mínimo**. Esa es la trampa clásica:
inflar el contexto para "ahorrar" con caché y terminar pagando más en total. Un prompt corto y
bueno le gana a un prompt largo cacheado. Detalles finos de caching/routing → skill
`optimizer_tokens_lushows`.

## Presupuesto: techo definido, realidad medida

- **Techo del bot: $15 USD/mes. Realidad actual: ~$5 USD/mes.** Tener techo explícito convierte
  "gastamos mucho?" en una pregunta con respuesta.
- La cuenta de servilleta: análisis cada 2h = ~360 análisis/mes; cada uno = 1 llamada Haiku
  chica + 1 llamada Sonnet mediana. El costo por análisis multiplicado por 360 debe caber bajo
  el techo — cálculo exacto con precios del día → `Matematicas_lushows` (precios de API cambian:
  verificar al día, no citar de memoria).
- Perspectiva honesta: $5/mes es irrelevante frente a UN trade mal dimensionado en live. El
  objetivo del control de costos no es ahorrar centavos, es **evitar la deriva** (un cambio de
  prompt que triplica tokens sin que nadie lo note) y mantener el hábito de medir.

## Cómo aplica al AGENTE TRADING

- Arquitectura ya alineada con la teoría: Haiku clasifica régimen, Sonnet decide convicción,
  los indicadores se calculan en JS gratis, caching descartado con razón (prompts <2048).
- Vigilar: si el prompt de convicción crece (más memoria, más contexto), recalcular el costo
  mensual — y recién si cruza el umbral de cacheo, reevaluar caching.
- Métrica a loguear (ver `86`): tokens de entrada/salida por análisis. Un salto brusco = algo
  cambió (bug, prompt inflado, respuesta descontrolada), y es más fácil verlo en el log que en
  la factura a fin de mes.
