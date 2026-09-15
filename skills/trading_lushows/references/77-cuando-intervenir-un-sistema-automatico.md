# 77 — Cuándo intervenir un sistema automático

El problema de tener el botón de apagado es que SIEMPRE hay una razón emocional para apretarlo.
La solución es la misma que para todo en trading: criterios OBJETIVOS escritos en frío, antes de
necesitarlos. Este módulo es ese documento.

## Intervenciones LEGÍTIMAS (objetivas)

| Criterio | Ejemplo real | Acción |
|---|---|---|
| **Bug confirmado** | Un trade se ejecutó con convicción 0 y régimen unknown (caso real del bot, jul-2026) | Pausar auto-trader, investigar, arreglar, test de regresión, reanudar |
| **Violación de protocolo** | Trade con convicción <8, riesgo >1.5%, 3ª posición simultánea, trade durante cooldown | Pausar, auditar la capa que falló (módulo 85), arreglar |
| **Falla de infraestructura** | WebSocket muerto sin reconectar, datos corruptos, stops sin vigilar porque el watcher murió | Pausar hasta restaurar; con posiciones abiertas, gestionarlas manualmente ANTES de nada más |
| **Evento extremo de mercado** | Exchange hackeado, par deslistado, flash crash con datos rotos, cambio regulatorio que afecta la operación | Pausar; el sistema no fue diseñado para ese entorno |
| **Kill switch alcanzado** | El drawdown superó el límite ESCRITO de antemano (p. ej. −X% definido en frío) | Pausar y auditar — no es castigo, es el protocolo cumpliéndose |

## Intervenciones ILEGÍTIMAS (emocionales)

- P&L rojo esta semana / este mes ← ruido; el edge se mide en muestras grandes.
- "Este trade se ve mal, lo cierro" ← el stop existe por diseño.
- "El mercado está raro" sin definición medible de "raro".
- Un tuit / un video / un influencer dice que viene el crash.
- Racha ganadora → "subo el riesgo mientras dure" (también es intervención, módulo 73).
- Aburrimiento: "lleva 2 semanas sin operar, le bajo el threshold" ← no operar ES una decisión del sistema.

Prueba rápida: si la intervención no puede escribirse como "la regla X se violó" o "el componente
Y falló", es emocional. Ciérrale la puerta.

## Protocolo de intervención (cuando SÍ toca)

1. **Congelar**: `POST /api/auto-trader/stop`. No tocar nada más todavía.
2. **Capturar evidencia**: logs, el análisis del trade (`/api/analyses`), estado del portfolio.
   Primero se documenta, después se arregla — si arreglas primero, pierdes la escena del crimen.
3. **Gestionar posiciones abiertas**: decidir con las reglas del sistema (respetar stop/target),
   no con el P&L del momento.
4. **Diagnosticar en frío**: ¿qué capa debió impedirlo y no lo hizo? (prompt, JS, broker — módulo 85).
5. **Arreglar + test**: el fix incluye un test que reproduce el caso. Sin test, no hay fix.
6. **Anotar en el backlog/memoria**: qué pasó, qué se cambió, qué señal lo habría detectado antes.
7. **Reanudar** y vigilar de cerca la primera semana post-fix.

## Cómo aplica al AGENTE TRADING

- El caso convicción-0 es el ejemplo canónico de intervención legítima: bug confirmado → pausa →
  investigación (backlog `11`) → el fix debe hacer imposible repetirlo (validación en el
  auto-trader, no solo en el prompt).
- Los criterios de este módulo deben poder chequearse en la rutina semanal (módulo 75): el paso 4
  de la rutina ("¿hubo violaciones?") es el detector; este módulo es el manual de respuesta.
- Falta definir por escrito el kill switch de drawdown para la fase live — es tarea de Luis en
  frío, no de la noche en que haga falta.
