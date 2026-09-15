# 314 · MCP a fondo — Model Context Protocol sin humo

> MCP es "USB-C para LLMs": un protocolo estándar para que cualquier agente hable con cualquier
> herramienta/dato sin escribir un adaptador por integración. Function-calling es el qué; MCP es el cómo conectarlo.

## Por qué existe
Sin MCP, cada combinación agente×herramienta es código a medida (N×M). MCP lo vuelve N+M: la tool se
expone **una vez** como server; cualquier client (Claude Desktop, tu IDE, tu agente) la consume igual.

## Las tres primitivas del server
| Primitiva | Qué es | Controlado por | Ejemplo |
|---|---|---|---|
| **Tools** | funciones que el LLM invoca (con side-effects) | el modelo | `crear_issue`, `query_db` |
| **Resources** | datos de solo-lectura que el host inyecta al contexto | la app/usuario | un archivo, una fila |
| **Prompts** | plantillas reutilizables que el usuario dispara | el usuario | "/resumir-pr" |

La distinción importa: **tools** las decide el modelo (riesgo), **resources** y **prompts** los controla
el humano. No metas un borrado destructivo como resource "inocente".

## Transporte (lo que cambió en 2026)
- **stdio**: server local como subproceso. Cero red, mínima latencia. Para herramientas de tu máquina/CLI.
- **Streamable HTTP**: server remoto, **un solo endpoint** POST+GET que opcionalmente upgradea a SSE
  para respuestas largas. Es el recomendado para red desde el spec 2025-03-26, retenido en la revisión
  nov-2025; reemplazó al viejo HTTP+SSE de doble endpoint. [no verificado] el próximo release del spec
  apunta a ~jun-2026 con mejoras de escalado horizontal.

```jsonc
// Cliente: registrar un server stdio
{ "mcpServers": { "github": {
  "command": "npx", "args": ["-y","@modelcontextprotocol/server-github"],
  "env": { "GITHUB_TOKEN": "${GH_TOKEN}" } } } }
```

```ts
// Server mínimo (TypeScript SDK)
server.tool('buscar_pedido', { id: z.string() },
  async ({ id }) => ({ content: [{ type:'text', text: JSON.stringify(await db.find(id)) }] }));
```

## Auth y seguridad
- Streamable HTTP usa **OAuth 2.1** para servers remotos; stdio hereda los permisos del proceso local.
- **Confused-deputy / SSRF**: un server remoto que reenvía a tu red interna es un agujero → valida hosts.
- **Tool poisoning**: descripciones maliciosas que engañan al modelo. Solo monta servers en los que confías.
- **Sesiones stateful** pelean con load-balancers → sticky sessions o estado externo (Redis) al escalar.

## Cuándo usar MCP y cuándo no
| Usa MCP | Salta MCP |
|---|---|
| Reusar la misma tool en varios agentes/hosts | Una sola app con 2 funciones internas |
| Cliente de terceros (Claude Desktop, IDE) | Latencia ultra-crítica, todo in-process |
| Ecosistema de servers ya hechos (GitHub, Slack, DB) | Prototipo desechable |

Para un agente único y cerrado, function-calling directo (ver [[313-tool-use-function-calling-patterns]])
es más simple. MCP brilla cuando hay **reuso y múltiples hosts**.

Cruza con [[66-agentes-avanzados-computer-use]] y [[308-agentes-produccion-orquestacion]].
