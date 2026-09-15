# 87 — Manejo de fallos: el bot que sobrevive a su infraestructura

Todo lo que el bot toca puede fallar: el WebSocket se cae, la API no responde, el proceso se
reinicia, un archivo se corrompe. En trading esto no es teoría — es rutina. La pregunta de
diseño no es "¿y si falla?" sino "**cuando** falle, ¿el bot queda en un estado seguro?".

## Los 4 fallos clásicos y su antídoto

| Fallo | Qué pasa | Antídoto |
|---|---|---|
| **WebSocket caído** | El feed de precios se corta; el bot queda ciego | Reconexión con backoff exponencial |
| **API caída** | Una llamada (exchange, Claude) falla o expira | Retry con límite + fallar cerrado |
| **Reinicio del proceso** | El bot muere y renace sin memoria de corto plazo | Reconciliación al arrancar |
| **Datos corruptos** | Un JSON quedó a medio escribir | Persistencia atómica |

## WebSocket: reconexión con backoff

**Backoff exponencial** = reintentar esperando cada vez más: 1s, 2s, 4s, 8s... hasta un techo.
Por qué no reintentar cada segundo para siempre: si el servidor está saturado, mil clientes
martillando cada segundo lo empeoran (y te pueden banear). Reglas extra:

- Mientras el feed está caído, **el bot está ciego: no abre posiciones nuevas**. Operar con el
  último precio conocido es operar con una foto vieja.
- Al reconectar, rellenar el hueco de velas perdidas (pedir histórico) antes de volver a analizar.
- Si la ceguera supera un umbral (ej. 15 min con posición abierta), alertar (ver `86`).

## API caída: retry con juicio

No todo error merece reintento. Distinguir:
- **Transitorio** (timeout, error 5xx, red): reintentar con backoff, 2-3 veces máximo.
- **Permanente** (clave inválida, parámetro mal formado, fondos insuficientes): reintentar es
  inútil — loguear y fallar cerrado.
- **El caso peligroso**: la orden se envió, la respuesta se perdió. ¿Se ejecutó o no? NUNCA
  reenviar a ciegas (riesgo de orden duplicada) — primero **consultar** el estado de la orden
  en el exchange, luego decidir. En live esto es obligatorio.

Fallar cerrado (ver `85`): si tras los reintentos no hay respuesta confiable, la decisión por
defecto es NO operar y avisar. Un ciclo de análisis perdido cuesta nada.

## Reinicio: reconciliación al arrancar

Cuando el proceso renace, su memoria RAM está vacía pero el mundo siguió: puede haber una
posición abierta de antes. **Reconciliar** = al arrancar, comparar el estado guardado en disco
contra la fuente de verdad (en paper: los JSON; en live: el exchange) y resolver diferencias
antes de tomar decisiones nuevas. El orden importa: primero saber dónde estoy parado, después
analizar. Un bot que arranca "en blanco" con una posición viva y sin stop es una bomba.

## Datos corruptos: persistencia atómica

Si el proceso muere a mitad de escribir un JSON, el archivo queda truncado: se pierde el estado
Y su historial. **Escritura atómica** = escribir a un archivo temporal y, solo cuando terminó
completo, renombrarlo sobre el original. El renombrado es instantáneo para el sistema operativo:
o está la versión vieja completa o la nueva completa — nunca una mezcla rota. Complementos:
respaldo periódico de los JSON y validación al leer (si no parsea, usar el respaldo y alertar,
no arrancar con estado vacío como si nada).

## Qué tiene el bot hoy y qué falta para live

- **Hoy (paper)**: estado y velas en JSON persistidos a disco, ciclo de análisis c/2h que
  tolera perderse una ronda, /status para verificar vida. El costo de un fallo es datos
  perdidos, no dinero.
- **Falta para live (22-ago-2026)**, en orden de importancia:
  1. Reconciliación completa al arrancar contra el exchange (posiciones, órdenes, stops).
  2. Consulta de estado antes de reintentar cualquier orden (anti-duplicados).
  3. Escritura atómica + respaldo de todos los JSON de estado.
  4. Regla "feed ciego = no abrir posiciones" con alerta si hay posición abierta.
  5. Ensayo de caos: matar el proceso y la red a propósito en testnet y verificar que revive
     en estado seguro. Si nunca se ensayó el fallo, el plan de fallo es una esperanza.
