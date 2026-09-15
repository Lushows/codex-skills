# 75 — Rutinas del trader (versión dueño-de-bot)

Un trader manual necesita rutina diaria de pantalla. El dueño de un bot necesita lo contrario:
una rutina CORTA y FIJA que le impida sobre-mirar. El trabajo del bot es operar; el trabajo de
Luis es supervisar el proceso — y supervisar bien toma 30 minutos a la semana, no 30 vistazos al día.

## Por qué mirar mucho es contraproducente

- Cada vistazo al P&L intradía es una invitación a intervenir (módulo 76). El P&L de un día es
  ruido puro en un sistema de swing con pocas operaciones.
- Mirar mucho no agrega información: los datos que importan (métricas acumuladas, meta-análisis)
  se producen semanalmente.
- La ansiedad crece con la frecuencia de chequeo, no con el riesgo real. Mismo drawdown, mirado
  20 veces, duele 20 veces.

## La rutina semanal de Luis (~30 min, día fijo)

| Paso | Qué mirar | Dónde | Pregunta clave |
|---|---|---|---|
| 1. Salud (5 min) | uptime, WebSocket, errores 24h, costo Claude | `GET /status` | ¿El sistema está VIVO y dentro de presupuesto? |
| 2. Meta-análisis (10 min) | El reporte semanal que Claude escribió sobre su propia semana | `GET /api/meta-analyses` / tab Reportes | ¿Qué patrón detectó? ¿Propone algo? |
| 3. Métricas (5 min) | drawdown máximo, Sharpe, curva de equity, win rate acumulado | `GET /api/metrics`, `GET /api/equity` | ¿La MUESTRA acumulada sigue sana? (no la semana) |
| 4. Protocolo (5 min) | trades de la semana vs reglas: ¿todos con convicción ≥8? ¿respetó cooldowns? | `GET /api/trades` | ¿Hubo alguna violación de protocolo? (si sí → módulo 77) |
| 5. Backlog (5 min) | anotar lecciones y propuestas de cambio EN FRÍO | backlog del proyecto | ¿Algo amerita cambio? Se anota, no se aplica hoy |

## Reglas de la rutina

1. **Día y hora fijos** (p. ej. domingo en la mañana). La rutina en horario aleatorio degenera en chequeo compulsivo.
2. **Fuera de la rutina, no se abre el dashboard** — salvo alerta real (caída del servicio, notificación de violación).
3. **Nada se cambia durante la rutina.** La rutina produce anotaciones; los cambios se aplican después, en frío, uno a la vez (módulo 84).
4. **Registrar la rutina misma**: una línea por semana ("semana 12: sano, 2 trades, sin violaciones, propuesta X anotada"). En 6 meses ese registro vale oro.

## Cómo aplica al AGENTE TRADING

- El sistema está diseñado para esta rutina: `/status` resume la salud en una llamada, el
  meta-análisis semanal hace la reflexión pesada por Luis, y las métricas viven en endpoints fijos.
- El caso FOMO 0/3 se detectó exactamente así: no mirando velas todos los días, sino leyendo el
  meta-análisis de la semana. La rutina corta FUNCIONA.
- Si Luis nota que está entrando al dashboard a diario "solo a ver", eso es una señal emocional,
  no una necesidad del sistema — módulos 76 y 78.
