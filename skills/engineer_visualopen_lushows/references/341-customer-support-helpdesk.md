# 341 · Soporte y helpdesk: tickets, IA de soporte, SLAs y deflection

> "Deflection" es la métrica que te engaña: un ticket que el bot cierra sin resolver no se
> deflectó, se enterró — y vuelve enojado. La métrica que decide el ROI es **resolución**,
> no desvío. Mide eso o estarás celebrando que escondes problemas.

## El esqueleto de un helpdesk
- **Ticket**: unidad de trabajo con estado (open → pending → resolved → closed), prioridad, asignado, canal (email, WhatsApp, chat, in-app).
- **Cola + enrutamiento**: por skill, idioma, prioridad o SLA. Round-robin satura; mejor por capacidad y especialidad.
- **Macros / respuestas guardadas**: para los intents repetitivos (reset, estado de pedido) antes de pensar en IA.
- **Base de conocimiento**: el self-service que alimenta tanto al humano como al bot. Sin KB buena, la IA alucina.

## IA de soporte: deflection vs resolución
| Métrica | Qué mide | Trampa |
|---|---|---|
| **Deflection rate** | % tickets que no llegaron a humano | incluye los que el usuario abandonó frustrado |
| **Resolution rate** | % consultas **realmente resueltas** por IA | la que importa para ROI |
| **FCR** (first-contact resolution) | resuelto en el primer contacto | el norte de calidad |
| **Escalation rate** | % que la IA pasa a humano | sano que exista; 0% es sospechoso |

**Benchmarks 2026 [verificado]:** deflection tier-1 mediana **41%**, top-quartile **59%**; password reset/acceso desvían >70%, billing/order-status 50-70%. Resolución IA promedio industria **~45%**, pero agentes con integración backend profunda alcanzan **70-93%** y chatbots legacy se quedan en 10-30%. **Costo: ~$0.62 por resolución IA vs ~$7.40 humano**. **CSAT: IA pura 4.1/5 vs humano 4.3/5**; flujos híbridos con escalación cierran la brecha a ~0.05 puntos. Solo **27%** de equipos tenían un canal agentic en producción plena (64% pilotearon) → la mayoría aún no madura.

## Diseño del agente de soporte IA
- **RAG sobre tu KB**, no el modelo a pelo: respuestas ancladas a artículos versionados, con citación de la fuente para auditar.
- **Tool-calling para acciones** (estado de pedido, reembolso, reenvío): un bot que solo "informa" desvía poco; uno que **actúa** resuelve 80-93%. La diferencia de resolución viene de la integración backend, no del modelo.
- **Escalación con contexto**: al pasar a humano, llevá la conversación completa + lo que la IA intentó. Re-preguntar lo mismo destruye CSAT.
- **Confianza/abstención**: si el modelo no está seguro, escala — no inventes. Intents sentiment-heavy (quejas, disputas) puntúan bajo en CSAT (~3.3-3.6); rutéalos a humano antes.
- En WhatsApp (caso BIO-SETA/Addrian): el bot resuelve FAQ y consulta de pedido; **escala a operador** ante intención de compra o duda compleja, exactamente el patrón de `operatorNotifier`.

## SLAs y satisfacción
- **First Response Time (FRT)** y **Resolution Time** por prioridad: define targets (ej. P1: respuesta <1h, resolución <8h) y mide cumplimiento, no promedios que esconden colas.
- **CSAT** (post-ticket, 1-5) y **CES** (Customer Effort Score: ¿cuánto esfuerzo te costó?) — CES predice retención mejor que CSAT.
- **Backlog / aging**: tickets viejos sin tocar son la deuda invisible; alerta por antigüedad, no solo por volumen.

## Arquitectura de un agente de soporte que actúa
```
mensaje → clasificar intent + sentiment
  → si sentiment negativo fuerte O intent crítico → escalar a humano (con contexto)
  → RAG sobre KB versionada → respuesta candidata
  → ¿requiere acción? → tool-call (estado pedido / reembolso / reenvío) con confirmación
  → confianza baja → escalar; alta → responder + ofrecer "¿resolvió tu duda?"
  → registrar: resuelto / escalado / abandonado (para medir resolución REAL)
```
La señal de "¿resolvió tu duda?" es lo que separa deflection de resolución: sin ese cierre explícito, no sabés si ayudaste o el usuario se fue a buscar a un humano por otro canal.

## Deflection económico (la cuenta que importa)
Con costo IA ~$0.62 vs humano ~$7.40 por resolución, cada punto de resolución real ahorra ~$6.78/ticket. Pero un ticket "deflectado" que vuelve cuesta **doble** (re-trabajo + cliente molesto + posible churn). Por eso optimizás **resolución neta**, no desvío bruto: `ahorro = tickets_resueltos_IA × $6.78 − costo_de_reaperturas`. Si las reaperturas suben, tu "ahorro" es negativo aunque el deflection se vea alto.

## Operación: lo que sostiene el CSAT
- **Triage por SLA, no FIFO**: P1 y clientes enterprise saltan la cola; el resto por antigüedad.
- **Plantillas + KB vivas**: cada ticket recurrente que no tiene macro/artículo es deuda; agrega uno tras resolverlo.
- **Loop de mejora**: los tickets que la IA **escaló** son tu mejor dataset para ampliar la KB y subir resolución el mes siguiente.
- **CES post-resolución** (1 pregunta): predice retención mejor que CSAT y molesta menos al cliente.

## Gotchas
1. **Optimizar deflection a ciegas** → escondés tickets no resueltos que vuelven peor; mide resolución.
2. **IA sin tool-calling** → solo informa, desvía 10-30%; el salto a 80% es por actuar sobre el backend.
3. **Escalar sin contexto** → el humano re-pregunta todo, CSAT se desploma.
4. **KB desactualizada** → la IA cita info vieja con confianza; versioná y revisá la KB.
5. **0% de escalación** → el bot está cerrando tickets a la fuerza; mide CSAT post-bot para detectarlo.
6. **SLA sobre promedios** → un promedio de 2h oculta P1 de 12h; mide percentiles y por prioridad.

**Fuentes:** notch.cx (AI resolution rate benchmarks 2026) · lorikeetcx.ai (resolve not deflect) · clarityarc.com (ticket deflection 2026) · digitalapplied.com (agentic AI support playbook 2026).

Cruza con [[318-chatbot-conversational-ux]].
