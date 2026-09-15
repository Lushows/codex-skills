# 363 · Monitoreo, alerting y on-call (alertas que se accionan, no que se ignoran)

> Monitorear no es tener mil gráficas: es saber **antes que el cliente** que algo está roto y poder dormir.
> Una alerta que no requiere acción humana inmediata no debería despertar a nadie — debería ser un ticket o un dashboard.

## La regla de oro: cada alerta que pagina = una acción clara AHORA
Si recibes una alerta y tu respuesta es "ah, ya se arregló solo" o "no sé qué hacer con esto", esa alerta está mal.
Toda página debe ser: **urgente** (no puede esperar a mañana), **accionable** (hay un runbook) y **real** (no flaky).
Lo demás va a un canal de Slack o a un dashboard, no al busca del on-call.

## Síntomas, no causas: alerta sobre lo que el usuario siente
No alertes "CPU al 90%" (¿y qué? quizá está trabajando bien). Alerta sobre el **síntoma de usuario**:
latencia p95 del job > X, tasa de error > Y%, cola de jobs creciendo sin drenar. La causa la investigas con métricas;
la **alerta** se dispara por el dolor real. Esto recorta drásticamente el ruido.

## Las 4 señales de oro (golden signals) para un servicio GPU
| Señal | Qué medir en el endpoint | Alerta típica |
|---|---|---|
| **Latencia** | p50/p95/p99 de duración del job (separar éxitos de fallos) | p95 > 2× baseline 10 min |
| **Tráfico** | jobs/min entrantes, profundidad de cola | cola > N y no drena |
| **Errores** | tasa de fallo, OOM, timeouts, 5xx del webhook | error-rate > 5% |
| **Saturación** | VRAM %, GPU util, RAM, workers ocupados/total | VRAM > 95% sostenido |

Para GPU: usa **DCGM exporter** → Prometheus (util, mem, temp, ECC errors). Sin saturación instrumentada,
los OOM te sorprenden siempre.

## SLO + error budget: el contrato que decide cuándo parar
Define un objetivo medible: ej. "99% de jobs completan < 90s en 30 días". El complemento (1%) es tu **error budget**.
Mientras quede presupuesto → envías features rápido. Si se agota → **congela releases** y gasta el sprint en fiabilidad.
El SLO convierte "¿está bien el servicio?" de discusión emocional a número objetivo.

```
error_budget_restante = 1 - (errores_observados / errores_permitidos_en_ventana)
# < 0 → freeze de deploys, foco en estabilidad
```

## Runbooks: la alerta enlaza al cómo-arreglarlo
Cada alerta paginadora lleva link a un runbook: qué significa, cómo confirmar, pasos de mitigación, a quién escalar.
El on-call a las 3am no debería **pensar desde cero** — debería ejecutar. Runbook mínimo: síntoma → dashboards a mirar →
3 causas más probables → mitigación rápida (rollback, kill-switch, escalar workers) → cómo cerrar.

## Fatiga de alertas: el asesino silencioso del on-call
Demasiadas alertas → el humano las silencia por reflejo → se pierde la real. Combátela: borra alertas que nunca
accionaste, agrupa las correlacionadas (1 incidente ≠ 50 páginas), pon umbrales sobre **tendencia sostenida** no
sobre picos instantáneos, y revisa mensualmente "¿qué alertó y qué hicimos?". Una alerta ignorada 3 veces se elimina o se arregla.

## Observabilidad mínima del worker GPU
- **Logs estructurados** (JSON) con `job_id` en cada línea → correlación trivial.
- **Métricas** (Prometheus/StatsD): duración por etapa, contadores de OOM/retry/fallback.
- **Trazas** para jobs multi-etapa (descarga → inferencia → encode → upload): ves **dónde** se va el tiempo.
- Heartbeat del worker: si deja de emitir, está colgado aunque el proceso "viva".

## Errores que muerden
- Alertar sobre métricas de host (CPU/disco) sin atar a impacto de usuario → ruido puro.
- Umbrales sobre valores instantáneos → flapping (alerta/resuelve/alerta) que entrena a ignorar.
- No tener on-call definido ni escalado → la alerta llega a un canal muerto un domingo.
- Medir solo el "happy path": tu p95 se ve hermoso porque excluye los jobs que murieron.

Cruza con [[159-monitoreo-slo-servicio-gpu]] y [[300-observabilidad-web-sentry-otel]].
