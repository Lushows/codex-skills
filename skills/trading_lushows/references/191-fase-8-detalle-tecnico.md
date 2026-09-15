# 191 — Fase 8: detalle técnico ejecutable

Complementa el módulo `09` (criterios y filosofía del go-live técnico). Este módulo es el plan de
obra: qué se construye, en qué orden, qué depende de qué, y cómo se sabe que cada pieza está
"hecha". Solo arranca si el 22-ago hay veredicto GO (`08`).

## Orden de construcción (las dependencias mandan)

| # | Tarea | Depende de | Definición de "hecho" |
|---|---|---|---|
| 1 | **Migrar a Render Frankfurt** | Nada — va PRIMERO (Binance geo-bloquea trading desde IPs de EE.UU.; sin esto, nada de lo demás conecta) | El bot corre en Frankfurt ≥1 semana con el paper actual, sin regresiones ni caídas |
| 2 | **Conexión testnet Binance** | 1 | *Testnet* = réplica del exchange con dinero falso. Hecho: leer precios, colocar y cancelar órdenes por API, con manejo de errores (rate limits, timeouts, reconexión) |
| 3 | **Órdenes OCO** | 2 | *OCO* = "one-cancels-the-other": stop y target viven EN el exchange; si toca uno, se cancela el otro. Hecho: cada entrada crea su OCO; si el servidor de Render muere, el stop sigue vivo. Probado matando el proceso a propósito |
| 4 | **Kill switch** | 2 | Botón/comando que cierra toda posición y bloquea nuevas entradas hasta rearme manual. Hecho: probado en testnet con posición abierta; ejecuta en segundos |
| 5 | **Límite de pérdida diaria 3%** | 4 | Si la pérdida del día toca −3% del capital → kill switch automático + no opera hasta el día siguiente. Hecho: probado forzando pérdidas simuladas en testnet |
| 6 | **Modo híbrido** | 2-5 | El bot propone el trade (con toda su checklist) y espera confirmación de Luis; timeout sin respuesta = NO trade. Hecho: probado el flujo completo propuesta→confirmación→OCO en testnet |
| 7 | **Seguridad de API keys** | 2 | Keys SIN permiso de retiro + whitelist de IP (la de Frankfurt) + guardadas como variables de entorno, jamás en el repo. Hecho: intento de retiro por API falla |
| 8 | **Ensayo general en testnet** | TODO lo anterior | ≥2 semanas del sistema completo en testnet sin incidentes (criterio del `08`). Solo entonces: keys reales y $200-500 |

## Reglas de esta fase

- **Una tarea a la vez, en orden.** La tentación de "conectar ya el testnet" antes de migrar a
  Frankfurt produce trabajo que hay que rehacer.
- **Cada tarea se prueba rompiéndola**: el OCO se valida matando el proceso; el kill switch,
  con posición abierta; el límite diario, forzando pérdidas. Lo que no se probó roto, no está hecho.
- **El paper NO se detiene** durante la construcción: la muestra sigue creciendo en paralelo.
- **Testnet ≠ producción**: liquidez y fills del testnet son irreales; sirve para probar la
  TUBERÍA (órdenes, errores, OCO), no para medir el edge. El edge se midió en paper.

## Diferencias que aparecerán con dinero real (esperarlas, no sufrirlas)

- Slippage real puede diferir del 0.05% modelado — medirlo desde el día 1 y comparar.
- Fills parciales (la orden se llena por pedazos): el código debe manejarlos.
- Mínimos de orden de Binance: con $200-500 de capital, verificar al día que el notional
  calculado supere el mínimo del par.

## Cómo aplica al AGENTE TRADING

- Este es el checklist de obra de la fase 8; se marca tarea por tarea y se actualiza con fecha (`199`).
- Presupuesto de tiempo honesto: entre GO (22-ago) y primer trade real hay MÍNIMO ~4-6 semanas
  (construcción + 2 semanas de testnet limpio + arranque híbrido). No se comprime.
- Decisión del monto exacto ($200 vs $500) → `economist_lushows`; implicaciones fiscales de
  operar cripto en Colombia → `contador_lushows`.
