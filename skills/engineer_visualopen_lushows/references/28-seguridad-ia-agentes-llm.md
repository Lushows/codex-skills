# 28 — Seguridad de IA / agentes (LLM)

**OWASP Top 10 for LLM Applications — 2025:** **LLM01 Prompt Injection** (#1), **LLM02 Sensitive Information
Disclosure**, **LLM03 Supply Chain**, **LLM04 Data & Model Poisoning**, **LLM05 Improper Output Handling**,
**LLM06 Excessive Agency** (muy expandido), **LLM07 System Prompt Leakage** (nuevo), **LLM08 Vector & Embedding
Weaknesses** (RAG), **LLM09 Misinformation**, **LLM10 Unbounded Consumption**.

## Prompt injection — directo e indirecto
**Directo** (el usuario escribe "ignora instrucciones previas") e **indirecto** (instrucciones maliciosas
escondidas en una web/PDF/email/documento RAG que el modelo lee luego). El indirecto es el peligroso para agentes:
el atacante NO es tu usuario. **No hay fix completo** — el LLM no separa instrucciones de data en un canal. Mitiga
**reduciendo el blast radius**, no confiando en el prompt.

## Guardrails
- **Input filtering:** detecta/strip patrones de injection, clasifica intención (NeMo Guardrails, Llama Guard, Rebuff). Trata TODO contenido recuperado/de tool como data no confiable.
- **Output handling (LLM05):** nunca `eval`/exec/render output del modelo sin escapar. Si el output maneja SQL/shell/HTML/tool call, valídalo y codifícalo como input de usuario — **el output del modelo es no confiable.**
- **Allow-list de tools:** el agente solo llama un set fijo de funciones tipadas; valida cada argumento server-side contra schema.
- **HITL (human-in-the-loop)** para acciones riesgosas/irreversibles: pagos, deletes, mensajes externos, gasto. Aprobación explícita.

## Excessive Agency (LLM06)
Least privilege — tools mínimas, scopes mínimos, autonomía mínima. Un agente con acceso amplio DB/file/API +
injection = takeover remoto. Scope de credenciales de tool por tarea; sin agente "admin".

## RAG / multi-tenant (LLM08)
Enforce aislamiento de tenant en el vector store — filtra cada query por `tenant_id` (metadata filter) → los
embeddings nunca cruzan tenants; idealmente colecciones/namespaces separados. **Sanitiza el contenido recuperado**
antes del prompt (puede traer injection indirecto). La inversión de embeddings puede filtrar texto fuente — trata el vector DB como conteniendo la data sensible cruda.

## Tool/function-call safety
Valida args (tipos/rangos/allow-list), **sandbox** de ejecución de código (gVisor/Firecracker/contenedor efímero,
sin red/credenciales del host), enforce **límites de gasto + kill-switch** para agentes autónomos (max calls, max
$, max wall-clock — capa Unbounded Consumption LLM10). Idempotency keys en tools con side-effects.

## Jailbreak / PII
**Jailbreak resistance:** en capas — system prompt hardening + clasificadores input/output + monitoreo + los
controles estructurales. No confíes solo en el system prompt (puede filtrarse LLM07 y bypassearse). **PII:** redacta
antes de mandar al modelo y antes de loguear traces; no entrenes en PII cruda; honra retención/deletion; cuida data residency.

## Gotchas
1. Tratar output del modelo como código/SQL/HTML confiable → injection-to-execution.
2. RAG sin filtro de tenant filtra docs de un cliente a otro.
3. Agente autónomo sin cap de gasto → costo runaway o abuso de recursos por atacante.
4. Injection indirecto vía documento recuperado bypasea TODOS tus filtros de *input* — sanitiza también lo recuperado.

**Fuentes:** genai.owasp.org/llm-top-10 · genai.owasp.org/llmrisk/llm01-prompt-injection · github.com/NVIDIA/NeMo-Guardrails · simonwillison.net/series/prompt-injection.
