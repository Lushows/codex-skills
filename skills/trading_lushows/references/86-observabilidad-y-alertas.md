# 86 — Observabilidad y alertas

**Observabilidad** = poder responder "¿qué está haciendo el bot y por qué?" sin abrir el código.
Un bot de trading corre solo, de madrugada, con dinero (aunque sea de papel). Si para saber si
está vivo hay que revisar a mano, no está listo para dinero real. La meta: **que el bot cuente
lo que hace, y que grite solo cuando algo importa.**

## Las 3 herramientas básicas

| Herramienta | Qué responde | Ejemplo en el bot |
|---|---|---|
| **/status** | "¿Estás vivo y en qué estado?" | Posiciones abiertas, último análisis, conexión al feed, PnL |
| **Logs estructurados** | "¿Qué pasó exactamente y cuándo?" | Cada decisión con timestamp, convicción, source, resultado |
| **Alertas** | "Despiértame si esto ocurre" | Violación de protocolo, error repetido, feed caído |

**Log estructurado** = registrar en formato fijo (JSON: evento, hora, datos) en vez de frases
sueltas. La diferencia práctica: sobre logs estructurados se puede preguntar "¿cuántos errores
de API hubo en 24h?" con una línea de código; sobre texto libre, toca leer a ojo.

## Qué loguear en un bot de trading (mínimo viable)

- **Cada decisión, incluidas las de NO operar**: régimen detectado, convicción, filtros que
  bloquearon. Las no-entradas son la mitad de la historia del sistema — sin ellas no se puede
  auditar si los filtros ayudan o estorban (ver `89`).
- **Cada orden y su ciclo de vida**: creada → ejecutada → stop/target tocado, con precios y hora.
- **Cada error con contexto**: qué llamada falló, qué respondió, si se reintentó (ver `87`).
- **Cada rechazo de guardrail**: qué capa rechazó qué valor (ver `85`). Estos logs son oro:
  son los bugs contándose solos.

## Alertas: pocas y que importen

La regla de oro: **una alerta que se ignora entrena a ignorar todas.** Si el bot notifica cada
análisis, en una semana nadie lee las notificaciones — incluida la que decía "posición sin stop".
Clasificar sin piedad:

| Nivel | Criterio | Ejemplo |
|---|---|---|
| 🔴 Despiértame | Dinero o protocolo en riesgo AHORA | Violación de guardrail, posición abierta sin stop, orden rechazada |
| 🟠 Hoy | Degradación que aguanta horas | Feed reconectando repetidamente, errores de API acumulándose |
| 🟢 Resumen | Información, no acción | Trade cerrado, reporte diario de PnL y errores 24h |

El "errores 24h" en el resumen diario cumple una función específica: los fallos que no ameritan
alerta individual (un timeout suelto) sí ameritan atención cuando se acumulan (40 timeouts =
algo cambió en la API).

## Paper vs live: qué cambia en el monitoreo

En paper, un silencio de 6 horas cuesta cero; en live puede costar la cuenta. Cambia el
énfasis:

- **Paper**: monitorear para APRENDER — que no se pierdan datos (cada análisis y trade quede
  registrado limpio), que los guardrails rechacen bien. Un hueco de datos en paper daña la
  validación (ver `48`).
- **Live**: monitorear para SOBREVIVIR — además de lo anterior: heartbeat (señal periódica de
  "sigo vivo"; su ausencia ES la alerta), verificación de que cada posición abierta tiene su
  stop puesto en el exchange, y reconciliación estado-interno vs exchange (ver `87`).

## Cómo aplica al AGENTE TRADING

- Ya existe: /status para consultar el bot, análisis cada 2h que deja registro, y los datos de
  trades en JSON con etiqueta `source` (que fue precisamente lo que permitió cazar el bug de
  convicción-0 — la observabilidad pagándose sola).
- Para el go-live (22-ago-2026): resumen diario con errores 24h, alerta inmediata por violación
  de protocolo o rechazo de orden, heartbeat, y chequeo automático "toda posición tiene stop".
- Prueba de fuego antes de live: simular un fallo (matar el feed, corromper una respuesta) y
  cronometrar cuánto tarda el sistema en avisar. Si la respuesta es "cuando Luis revise", no
  está listo.
