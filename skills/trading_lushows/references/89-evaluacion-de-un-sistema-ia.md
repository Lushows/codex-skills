# 89 — Evaluación de un sistema con IA en el circuito

Cuando una IA participa en las decisiones de trading, hay DOS cosas que evaluar: la estrategia
(¿tiene edge?) y el evaluador (¿la IA decide bien y de forma estable?). El backtest clásico
(ver `46`) mide lo primero; este módulo es sobre lo segundo. La IA es la pieza más difícil de
auditar porque no es determinista: el mismo prompt puede dar respuestas distintas.

## Las 3 preguntas para auditar la IA del sistema

### 1. Consistencia: ¿la misma situación produce la misma decisión?

Si le muestras a la IA el mismo contexto de mercado dos veces y una vez dice convicción 8 y
otra convicción 4, el "edge" del sistema incluye una lotería interna. Cómo medirlo: tomar N
casos fijos, pasarlos varias veces por el pipeline y medir cuánto varía la convicción. Algo de
variación es normal; que la decisión de operar/no-operar cambie entre corridas idénticas es
inaceptable — para eso existe el umbral duro ≥8 verificado en código (ver `85`): la frontera la
pone el JS, no el humor del modelo.

### 2. Calibración: ¿los 8 ganan más que los 6?

**Calibración** = que el número de convicción signifique algo. Si el bot ejecuta con ≥8, la
promesa implícita es que un 9 es mejor apuesta que un 8, y un 8 mejor que un 6 (que no se
ejecuta). Eso es medible: agrupar los análisis por convicción y comparar cómo les fue —
incluyendo a los que NO se ejecutaron (¿qué habría pasado?; por eso se loguean las no-entradas,
ver `86`).

| Si los datos muestran... | Significa... |
|---|---|
| Convicción alta gana más que baja | La escala informa: el umbral ≥8 tiene sentido |
| Todas las convicciones rinden igual | El número es decorativo — el filtro real está en otra parte |
| Convicción alta rinde PEOR | Alarma: la IA se entusiasma justo donde no debe (patrón FOMO) |

Advertencia de muestra: con 10 trades no hay calibración medible — se necesitan decenas de
casos POR NIVEL. Mientras tanto se acumulan datos limpios (por eso el bug de convicción-0 era
grave: ensuciaba justo esta tabla). Cálculos → `Matematicas_lushows`.

### 3. Evals: ¿el prompt nuevo es mejor que el viejo, o solo distinto?

Un **eval** es un examen fijo para la IA: una colección de casos históricos con la respuesta
esperada (o al menos con el resultado conocido). Ejemplos de casos para el set del bot:

- Los 3 trades FOMO de julio (precio >3% sobre SMA20) → convicción esperada: BAJA.
- Un retroceso ordenado a la SMA20 en tendencia alcista → convicción esperada: ALTA.
- Régimen lateral claro → esperado: no operar.
- Casos trampa: datos incompletos o contradictorios → esperado: abstenerse (fallar cerrado).

La regla que lo cambia todo: **ningún cambio de prompt entra a producción sin correr el eval
completo con prompt viejo y nuevo, lado a lado.** Sin eval, "mejoré el prompt" significa "lo
cambié y me gustó cómo se leyó" — y un prompt que arregla el caso de hoy puede romper tres
casos de ayer sin que nadie lo note. Es la versión IA del test de regresión.

## El eval crece con las cicatrices

Cada trade malo con causa identificable se convierte en caso del eval (la lección FOMO ya
aporta 3). Así el sistema no solo "recuerda" sus errores en la memoria del trader: los usa como
examen permanente para cada versión futura de sí mismo. Es la defensa contra reintroducir un
error ya pagado.

## Cómo aplica al AGENTE TRADING

- Ya hay materia prima: convicción registrada por trade (limpia desde el fix de source), las
  no-entradas del ciclo c/2h, y 3 casos FOMO listos para fundar el eval.
- Antes del go-live (22-ago-2026): armar el eval mínimo (10-15 casos de las velas guardadas),
  correrlo contra el prompt actual como línea base, y adoptar la regla "sin eval no hay cambio
  de prompt".
- La calibración (¿los 8 ganan más que los 6?) queda como métrica permanente del reporte
  semanal: no se responde hoy por falta de muestra, pero cada análisis logueado la acerca.
