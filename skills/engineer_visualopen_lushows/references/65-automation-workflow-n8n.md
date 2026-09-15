# 65 — Automation / workflow glue (n8n, webhooks, integraciones)

**n8n** = el favorito 2026 para automatización con IA: open-source, self-hosteable (Docker), workflow visual con
**70+ nodos de IA** (LLMs, embeddings, vector DBs, OCR, LangChain, nodos de *agente*). A diferencia de Zapier, lo
self-hosteas, lo inspeccionas, escribes nodos custom en JS, llamas cualquier API vía HTTP/Webhook — soberanía total de datos.

## Zapier vs Make vs n8n
- **Zapier** — máxima cantidad de apps, cero-código, no-técnicos; webhooks solo en premium; caro a escala; datos en su cloud.
- **Make** — visual intermedio, buena profundidad, más barato que Zapier, branching visual.
- **n8n** — máximo control técnico, self-host, mejor para AI workflows dev-owned; curva mayor.

**Regla:** no-técnico + SaaS comunes → Zapier; visual con lógica + presupuesto → Make; AI workflows/datos sensibles/self-host → **n8n**. **iPaaS** = la categoría (middleware que conecta SaaS sin código).

## Orquestación de webhooks
Patrón **receive → transform → fan-out**: un endpoint recibe, normaliza, dispara N acciones (Slack, Sheet, CRM). El nodo Webhook es el trigger; ramificas con IF/Switch.

## Workflow AI en n8n (caso GastroWhats)
```
[Webhook: WhatsApp inbound] → [Set: normalizar mensaje]
  → [AI Agent node: Claude + system prompt + tools]
  → [Switch: intención]
      ├─ compra → [HTTP: crear pedido en backend] → [WhatsApp: confirmar]
      └─ duda  → [WhatsApp: responder]
  → [Postgres: log conversación]
```

## Cuándo graduarte a código real
Migra de n8n a un servicio propio cuando: el workflow supera ~15-20 nodos y es ilegible; necesitas tests/CI; hay
lógica de estado compleja o transacciones; el throughput satura n8n; o el workflow es core del producto (no glue).
**n8n brilla en *glue* e integraciones, no como motor de negocio crítico de alto volumen.**

## Jobs programados / error handling
**Schedule Trigger** (cron) para recordatorios de recompra, reportes diarios, limpieza. **Error handling:** *Error
Workflow* global (notifica Slack al fallar), `retryOnFail` + `maxTries` por nodo, `continueOnFail` para no abortar el batch. Sin esto, un fallo silencioso pierde mensajes de clientes.

## Security
**Verifica firmas de webhook SIEMPRE:** Stripe (`Stripe-Signature` HMAC), Meta/WhatsApp (`X-Hub-Signature-256`
HMAC-SHA256 con tu app secret), GitHub. Un endpoint público sin verificación es spoofeable. Secretos en **n8n
Credentials** (cifradas con `N8N_ENCRYPTION_KEY`), nunca hardcode. Restringe con Cloudflare (IP allowlist/DDoS).

## Gotchas
1. **Webhook sin verificación de firma** — cualquiera POSTea pedidos falsos; valida HMAC antes de procesar.
2. **`N8N_ENCRYPTION_KEY` no persistida** — si cambia/se pierde, todas las credenciales se vuelven ilegibles tras un redeploy.
3. **Webhook de test vs producción** — n8n distingue URL de *test* (solo activa con el editor abierto) y *production*; usar la de test en prod = nada se dispara.
4. **Sin retries → pérdida silenciosa** — fallos de red dejan mensajes sin responder; configura retry + error workflow.
5. **n8n como base de datos de estado** — no guardes estado crítico solo en el workflow; persiste en Postgres.
6. **Ejecución síncrona larga** — workflows lentos timeoutean el webhook del emisor (Meta reintenta y duplica); responde 200 rápido y procesa async.

**Fuentes:** blog.n8n.io/best-ai-workflow-automation-tools · hatchworks.com/blog (n8n vs Zapier) · docs.n8n.io.
