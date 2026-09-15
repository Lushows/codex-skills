# 84 — Meta-análisis y auto-mejora

El **meta-análisis** es el componente más raro y más valioso del AGENTE TRADING: una vez por
semana, Claude (Sonnet, con thinking) recibe TODO lo que el sistema hizo — trades, análisis,
convicciones, resultados, régimen de cada momento — y escribe un informe sobre su propia semana.
El sistema se estudia a sí mismo, como un trader serio revisa su diario de trading.

## Qué produce el meta-análisis

| Salida | Qué es | Ejemplo |
|---|---|---|
| **Narrativa de la semana** | Qué pasó y por qué, en texto legible para Luis | "Semana dominada por tendencia alcista; 5 análisis, 2 trades, 1 win 1 loss" |
| **Patrones detectados** | Regularidades en los datos de la semana (y contra semanas previas) | "Las 3 pérdidas recientes comparten entrada con precio >X% sobre la SMA" |
| **Propuestas de mejora** | Cambios concretos a reglas, prompts o filtros | "Agregar penalización por extensión al prompt de convicción" |
| **Lecciones** | Se escriben a `traderMemory` (módulo 83) | "Entradas extendidas post-racha: 0/3" |

Se guarda en `data/` (FIFO de 52 semanas) y se lee en `GET /api/meta-analyses` o el tab Reportes.
También puede forzarse manual: `POST /api/meta-analysis/run`.

## La regla de oro: propuestas → backlog, NUNCA en caliente

El meta-análisis **propone, no ejecuta**. Sus propuestas van a un backlog donde Luis las evalúa
en frío. ¿Por qué este freno, si la propuesta viene "del propio sistema"?

1. **Muestras chicas**: una semana son un puñado de trades. Auto-aplicar conclusiones de n=3 es
   institucionalizar el sesgo de recencia (módulo 70) a velocidad de máquina.
2. **Un cambio a la vez**: si el sistema se auto-modificara semanalmente, en 2 meses nadie sabría
   qué versión produjo qué resultados — adiós medición (módulo 89).
3. **El proponente no se aprueba a sí mismo**: mismo principio que en cualquier organización
   seria. Claude propone, Luis (con datos acumulados) decide, y el cambio se versiona.

El circuito completo: **meta-análisis → propuesta → backlog → revisión en frío (rutina semanal,
módulo 75) → si procede: cambio versionado → evaluación del cambio (módulo 89)**.

## El caso real: el bot detectó su propio FOMO

Jul-2026: tras una racha de 4 wins, el bot encadenó 3 pérdidas. Fue el **meta-análisis** el que
detectó el patrón común — las 3 entradas eran en precio extendido — y lo nombró: comportamiento
FOMO producido por un prompt sin filtro de extensión. Ni Luis mirando velas ni una alerta lo
habían visto; lo vio el sistema leyéndose a sí mismo. La lección entró a `traderMemory` y el fix
estructural entró al backlog. Ese es el loop de auto-mejora funcionando exactamente como se diseñó:
detección automática, corrección deliberada.

## Límites honestos

- El meta-análisis hereda los límites del LLM (módulo 82): puede narrar patrones donde solo hay
  varianza (módulo 79). Por eso las propuestas se contrastan con la muestra acumulada, no solo
  con la semana.
- Es tan bueno como los datos que recibe: si los análisis no guardaran contexto completo
  (convicción, régimen, lecciones inyectadas), no habría nada que estudiar. La observabilidad
  (módulo 86) alimenta la auto-mejora.

## Cómo aplica al AGENTE TRADING

Leer el meta-análisis es el paso 2 de la rutina semanal de Luis. La disciplina a proteger:
disfrutar las propuestas, resistir aplicarlas el mismo día. En frío, por backlog, una a la vez.
