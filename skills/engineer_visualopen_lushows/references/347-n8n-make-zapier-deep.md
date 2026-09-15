# 347 · n8n vs Make vs Zapier a fondo (y cuándo graduar a código)

> El no/low-code te da glue en horas, no en sprints. El error caro es quedarte ahí cuando el
> workflow ya es producto: entonces pagas la fuga de cada plataforma (lock-in, opacidad, throughput).

## La decisión en una tabla (precios 2026 [no verificado al céntimo])

| Eje | Zapier | Make | n8n |
|---|---|---|---|
| Modelo de cobro | por **task** (cada paso) | por **operation** (cada módulo) | por **execution** (workflow entero) |
| Free tier | 100 tasks/mes | ~1.000 ops/mes, 2 escenarios | **self-host ilimitado** |
| Entrada paga | ~$30/mes (750 tasks) | más barato que Zapier | €24/mes cloud · self-host ~$15-40 infra |
| Apps integradas | 8.000+ (máx.) | miles | cualquiera vía HTTP |
| AI / agentes | Zapier Agents | Maia (NL→escenario) | **LangChain nativo, 70+ nodos**, loops/memory/RAG/tools |
| Self-host | no | no | **sí (Docker)**, soberanía de datos |
| Webhooks | premium | sí | sí, trigger de primera clase |
| Código custom | limitado (Code step) | funciones | nodos JS/Python, ejecutar cualquier API |

**El golpe económico:** un workflow IA de 20 pasos cuesta lo mismo que uno de 2 en n8n (cobra por
ejecución), pero **20×** en Zapier (cobra por task). Migraciones reales: de $800-2.000/mes en Zapier a
$15-40/mes en n8n self-host, mismos flujos, ~95% de ahorro. [no verificado el caso concreto]

## Regla de elección
- **No-técnico + SaaS comunes + bajo volumen** → Zapier (máxima cobertura de apps, cero fricción).
- **Visual con lógica de ramas + presupuesto medio** → Make (branching, mejor relación ops/precio).
- **AI workflows, datos sensibles, alto volumen, self-host** → **n8n** (control y costo a escala).

## El nodo AI Agent de n8n (lo que lo separa)
No es un "LLM call": es un **agente** con system prompt, **tools** (sub-nodos que el modelo invoca:
HTTP, Postgres, Vector Store, sub-workflow), **memory** (buffer/Postgres/Redis) y **RAG** (embeddings
+ vector DB). Patrón: el agente decide qué tool llamar según la intención → tú expones tu backend como
tools y dejas que el modelo orqueste. Para Claude, fija `claude-*` en el credential y limita las tools
a las imprescindibles (menos superficie de error).

## Webhooks: receive → transform → fan-out
Un endpoint **Webhook** recibe, un **Set** normaliza, un **Switch/IF** ramifica a N acciones. Regla de
oro de producción: **responde 200 en <1s y procesa async** (el emisor —Meta, Stripe— reintenta y
duplica si tardas). Verifica **siempre** la firma HMAC del proveedor antes de procesar (ver gotcha 1).

## Cuándo graduar de n8n a código real
Migra a un servicio propio cuando: el workflow pasa de ~15-20 nodos y es ilegible; necesitas
tests/CI/versionado serio; hay estado transaccional complejo; el throughput satura n8n; o el flujo es
**core del producto**, no glue. n8n brilla en integración y pegamento, **no** como motor de negocio
crítico de alto volumen. Patrón híbrido sano: n8n dispara y orquesta, pero la lógica pesada vive en un
endpoint tuyo que n8n llama vía HTTP (testeable, deployable, con cola propia).

## Gotchas que cuestan dinero o datos
1. **Webhook sin verificar firma** → cualquiera POSTea pedidos falsos. Valida HMAC (Meta
   `X-Hub-Signature-256`, Stripe `Stripe-Signature`) antes de tocar nada.
2. **`N8N_ENCRYPTION_KEY` no persistida** → tras un redeploy, **todas** las credenciales quedan
   ilegibles. Móntala como secret estable.
3. **URL de test vs producción** → la de *test* solo dispara con el editor abierto; usarla en prod = nada corre.
4. **Sin retries** → un fallo de red pierde el mensaje del cliente en silencio. `retryOnFail` + Error Workflow global.
5. **Estado crítico solo en el workflow** → persiste en Postgres; n8n no es tu base de datos.
6. **Cobro por operación en Make** → un loop sobre 500 ítems = 500 ops; vigila el contador.

## Veredicto operativo
Empieza en la plataforma que desbloquea hoy; instrumenta el costo por ejecución desde el día 1; y
ten escrito **el criterio de graduación** antes de que el workflow se vuelva insostenible.

**Fuentes:** [pxlpeak n8n pricing 2026](https://pxlpeak.com/blog/ai-tools/n8n-pricing-vs-free) · [digitalapplied Make/Zapier/n8n 2026](https://www.digitalapplied.com/blog/marketing-automation-ai-agents-make-zapier-n8n-2026) · [Automation Labs, Medium](https://medium.com/@automation.labs/zapier-vs-make-vs-n8n-in-2026-where-ai-agents-actually-fit-1edbbeff85f3) · docs.n8n.io.

Cruza con [[65-automation-workflow-n8n]], [[348-workflow-automation-patterns]] y [[351-rpa-integraciones]].
