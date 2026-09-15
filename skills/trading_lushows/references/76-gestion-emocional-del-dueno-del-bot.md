# 76 — Gestión emocional del dueño del bot

Automatizar el trading no elimina las emociones: las muda de lugar. Ya no sufres apretando el
botón de compra — sufres mirando cómo OTRO (tu bot) aprieta botones con tu plata (hoy simulada,
mañana real). Es una emoción distinta y hay que conocerla.

## Ansiedad de delegación

Es la incomodidad de haber cedido el control a un sistema. Se parece a ir de copiloto con alguien
que maneja distinto a ti: aunque maneje bien, cada frenada te tensiona porque TÚ no la decidiste.

Síntomas típicos:
- Abrir el dashboard muchas veces al día "solo a ver".
- Releer el razonamiento de un trade perdedor buscando "el error" (a veces no hay error: los
  buenos trades también pierden — módulo 79).
- Sentir alivio cuando el bot NO opera, aunque operar sea su trabajo.

## La tentación de intervenir

El equity cae una semana y la mano pica: pausar el bot, bajar el riesgo, "ayudarle" cerrando una
posición. Ojo con esto:

| Intervención emocional | Por qué daña |
|---|---|
| Pausar tras una racha roja | Te pierdes la recuperación; los sistemas pagan su edge en rachas y no avisan cuándo |
| Cerrar una posición "porque se ve mal" | Rompes la estadística: el stop y el target existían por diseño |
| Ajustar parámetros en caliente | Conviertes un sistema medible en un frankenstein inmedible (módulo 74) |
| "Solo esta vez" tomar un trade manual | Contaminas el track record: ya no sabes qué rinde el sistema |

La regla: **las intervenciones se deciden con los criterios del módulo 77, nunca con el estómago.**
"P&L rojo una semana" no es criterio; "trade ejecutado violando el protocolo" sí.

## Convivir con drawdowns del sistema

Un **drawdown** es la caída desde el pico de tu capital hasta el valle. TODO sistema los tiene;
son el precio de admisión del edge. Lo que ayuda:

1. **Saber el drawdown esperado de antemano.** Con win rate ~40-50% y riesgo 1.5%, rachas de
   varias pérdidas seguidas son matemáticamente normales (módulo 79). Si un drawdown de −8% te
   sorprende, el problema era la expectativa, no el sistema.
2. **Definir el drawdown de apagado ANTES** (kill switch humano): un número escrito en frío
   ("si el drawdown supera X%, pauso y audito"). Así la decisión de las 3am ya está tomada.
3. **Mirar el proceso, no el resultado**: la pregunta semanal es "¿el bot siguió sus reglas?",
   no "¿ganó?". Un sistema que sigue reglas y pierde una semana está sano; uno que gana violando
   reglas está enfermo.
4. **Recordar el tamaño real**: en paper con $1.000 simulados, un −5% son $50 de mentira. Es el
   mejor momento de la historia para ENTRENAR estas emociones baratas.

## Cómo aplica al AGENTE TRADING

- La rutina de 30 min/semana (módulo 75) es la herramienta anti-ansiedad número uno: convierte
  "mirar cuando siento" en "mirar cuando toca".
- El dashboard muestra el razonamiento de cada trade — úsalo para auditar protocolo, no para
  litigar resultados trade por trade.
- La fase paper es el gimnasio emocional de Luis: si hoy no aguanta un drawdown simulado sin
  intervenir, no está listo para live, sin importar lo que digan las métricas.
