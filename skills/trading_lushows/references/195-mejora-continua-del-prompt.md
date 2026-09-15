# 195 — Mejora continua del prompt

Los prompts de régimen (Haiku) y convicción (Sonnet) SON parte de la estrategia — cambiarlos
cambia el sistema tanto como cambiar el RSI. Por eso se iteran con el mismo rigor que cualquier
variable: hipótesis → prueba → medición → decisión. Nunca "se me ocurrió mejorarlo anoche".

## El método (5 pasos, sin atajos)

1. **Hipótesis escrita ANTES de tocar nada.** Formato: "Creo que [cambio X] mejorará [métrica Y]
   porque [evidencia del journal Z]". Ejemplo real disponible: "agregar al prompt de convicción
   la regla de penalizar precio extendido mejorará el PF, porque el journal muestra 0/3 sobre
   $1.788 vs 4/4 bajo $1.760".
2. **Un solo cambio.** Si se tocan la temperatura, la instrucción anti-FOMO y el formato JSON en
   la misma versión y el PF mejora... ¿cuál de los tres fue? Imposible saberlo. Dos cambios a la
   vez = cero información.
3. **Versionar**: cada prompt tiene número de versión (v1, v2...) y cada trade/análisis registra
   con QUÉ versión se decidió (etiqueta en analyses/traderMemory). Sin esto no hay comparación
   posible después.
4. **Medir en paper, nunca en live.** El prompt nuevo corre su período en paper y se compara
   contra la versión anterior con métricas (`16`) y muestra suficiente (`17`). Si el sistema ya
   está live, el prompt nuevo corre en un paper paralelo (shadow) antes de tocar producción.
5. **Decidir con umbral pre-registrado**: definir antes qué significa "ganó" (ej. PF mayor con
   ≥20 análisis comparables). Si no gana claro, se descarta y se anota — descartar también es
   aprender.

## Formas de A/B para este bot

- **Secuencial** (v1 corre 4 semanas, luego v2 corre 4 semanas): simple, pero el mercado cambia
  entre períodos — comparación imperfecta. Aceptable si se anota el régimen de cada período.
- **Paralelo/shadow** (v1 decide de verdad, v2 opina en silencio sobre los MISMOS datos y se
  registra qué habría hecho): mejor comparación, mismo mercado. Cuesta el doble en llamadas a
  Claude — con ~$5/mes de base, duplicar el costo de un paso sigue siendo barato y suele valerlo.
- **Replay histórico** (correr el prompt nuevo sobre los analyses guardados): gratis y rápido
  para descartar ideas malas, pero cuidado con el sobre-ajuste: afinar el prompt hasta que
  "acierte el pasado" no garantiza nada del futuro. Sirve de filtro, no de veredicto.

## Trampas específicas de iterar prompts

- **El prompt-Frankenstein**: cada mes se le agrega una regla más hasta que son 40 instrucciones
  que se contradicen. Revisar largo total y podar; menos suele decidir mejor.
- **Cambiar el prompt por UNA mala racha**: 3 pérdidas no son evidencia (`17`), son varianza.
- **No-determinismo**: el mismo prompt puede dar notas distintas en llamadas idénticas. Por eso
  el formato JSON estricto y las muestras grandes; una diferencia de PF chica entre versiones
  puede ser solo ruido del modelo.
- **Cambio de modelo = cambio de prompt**: migrar de un modelo a otro (como se hizo a Sonnet 5)
  cuenta como UNA variable y se mide igual.

## Cómo aplica al AGENTE TRADING

- Primer candidato oficial con este método: **el filtro anti-extensión** (hipótesis del paso 1,
  ya con evidencia del journal). Es el pivote natural si el 22-ago el PF sigue <1.3.
- Verificar que analyses guarde la versión del prompt en cada registro — si no, agregarlo YA
  (mismo argumento que la atribución en `193`).
- Significancia de la comparación entre versiones (¿la mejora es real o ruido?) → `Matematicas_lushows`.
  Detalles de la API de Anthropic (modelos, precios, JSON estricto) → skill `claude-api`.
