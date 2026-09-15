# 184 — Generative & AI-native UI patterns 2026

**Patrones concretos 2026** (más profundo que 18). Pareja de 18 (AI-native UI), 51 (building AI products), 180 (estados), 36 (realtime). Regla de oro: **el chatbox dejó de ser el destino y pasó a ser el caso más pobre — la IA es un material de interfaz probabilístico/latente/falible; diseñar para la incertidumbre, no para el determinismo del CRUD.**

## 1. El shift AI-native

Tres modos de tejer la IA: **inline assist** (vive dentro del componente que ya usas — ghost text, "rewrite/expand" en selección, autocompletado de celda; `⌘K`/`/slash` contextual), **generative components** (devuelve UI no prosa, §4), **ambient AI** (corre en segundo plano — resúmenes proactivos; riesgo: spam si mal calibrado → dismiss barato + memoria de rechazo). **Determinístico vs probabilístico:** trata cada output como **borrador editable** no verdad; **gradiente de confianza** visible (no binario); tres tácticas ante incertidumbre (preguntar para desambiguar, ofrecer 2-3 alternativas, gradiente visual); **graceful degradation** (fallback determinístico "no pude — aquí los pasos manuales", nunca spinner colgado).

## 2. Streaming & response UX

Streaming token-by-token es **baseline** (perciben 40-60% más rápido). Pero solo enmascara latencia **después** del primer token: si el **TTFT >1.5-2s**, pantalla en blanco y luego ráfaga → cubre el TTFT aparte. **Shimmer skeleton** durante el TTFT (reduce el tiempo percibido ~30% vs spinner). **Status dinámico** si >5s ("Analizando… → Extrayendo entidades…"). **Stop/Regenerate** siempre presentes (interrumpibilidad = control). **Partial-render seguro** (parsear Markdown/código incremental sin romper layout — buffer hasta cerrar bloques, nunca repintar todo). **Autoscroll inteligente** (seguir tokens *salvo* que el usuario haya scrolleado arriba).

## 3. Confianza, citas & transparencia

*"La respuesta es la respuesta; las citas son los recibos."* **Citas inline numeradas** (`¹`) que enlazan a **source cards** (título, dominio, excerpt, fecha). **Señales de calidad** (dominio + freshness "hace 3 días"). **"Show your work"/reasoning toggle** (razonamiento plegado, expandible — el *resumen* de traza, NO el chain-of-thought crudo). **Confidence por afirmación** (marca lo factual con cita; lo no citable = opinión del modelo). **Grounding display** (sobre qué responde: tus docs / la web / su memoria). **Etiqueta "AI-generated"** + feedback 👍/👎.

## 4. Generative UI (la frontera 2026)

La IA devuelve **componentes** no texto (el modelo elige el widget: chart para datos, form para recolectar, card para producto). **Vercel AI SDK** `streamUI`: hace stream de RSC junto a la generación; cada tool define `generate` como **async generator** (`async function*`) que primero hace `yield` de un skeleton y luego `return` del componente con datos. **AI SDK 5** (chat tipado + primitivas de loop de agente). El widget se monta con su skeleton y se rellena progresivamente. Regla: el modelo **decide la intención**, los componentes son **tuyos, deterministas, testeados** (la IA orquesta piezas confiables, no "dibuja" UI libre = slop visual).

## 5. Agentes & visualización de tool-use

Multi-step → el usuario ve el **plan y progreso**, no un spinner de 40s. **Timeline de pasos** ("Buscando… → Leyendo 3 fuentes… → Redactando", cada uno con estado, colapsable). **Tool calls visibles** (qué herramienta, params, resultado resumido; estándar emergente **AG-UI** event-based). **Human-in-the-loop con risk-tiering:** `needsApproval` pausa **antes** del side-effect (regla de oro: *la aprobación va antes del efecto, no después*); bajo riesgo (leer) auto, alto riesgo (enviar/pagar/borrar) **preview + confirm**. **Preview antes de actuar** (el email/pedido exacto, editable, Approve/Edit/Deny). **Interrumpibilidad** (pausar/redirigir sin perder estado).

## 6. Input conversacional, ética & anti-slop

**Empty state del chat** (nunca un cursor en vacío → 3-4 prompt suggestions concretas). **Multimodal** (voz push-to-talk + transcripción visible; imagen con confirmación de lo entendido). **Conversational commerce LatAm/WhatsApp** (in-chat discovery→negociación→checkout, +30% conversión; **política Meta 15-ene-2026:** prohibidos chatbots de propósito general, permitidos solo agentes **task-specific** — el bot declara su propósito acotado, no deriva a conversación abierta). **Disclosure/ética** (etiqueta IA obligatoria, opt-out a humano visible). **Error/refusal UX** (explica el por qué + ofrece salida). **Cuándo NO usar IA:** tareas deterministas (calcular total, navegar) van con UI normal — meter IA añade latencia/costo/incertidumbre sin valor.

## AI-UI anti-patterns — blacklist
**chatbox como única superficie** cuando un botón bastaba ("chatbox tax") · **spinner genérico** en vez de status/skeleton en el TTFT · **pantalla en blanco** con TTFT alto fingiendo que el streaming la cubre · **repintar todo el mensaje** en cada token (jank) · **autoscroll que secuestra** al usuario que subió a leer · **Markdown/código roto** por bloques sin cerrar · **output como verdad** sin permitir edición ni mostrar incertidumbre · **cero citas** en afirmaciones factuales · **exponer chain-of-thought crudo** como "transparencia" · **confianza binaria** · **agente que actúa sin preview** en alto riesgo (aprobación *después* del efecto) · **sin Stop/Regenerate** · **ambient sin dismiss barato** ni memoria del rechazo · **empty state vacío** · **ocultar que es un bot** / sin ruta a humano (ilegal + viola política WhatsApp 2026) · **slop visual** (el modelo "dibuja" UI libre) · **falsa precisión** (timestamps/porcentajes inventados).
