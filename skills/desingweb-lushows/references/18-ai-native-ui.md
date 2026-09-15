# 18 — UI AI-native & conversacional (chat, agentes, WhatsApp commerce)

Patrones para UIs donde la IA es el núcleo: bots de venta WhatsApp (GASTROWHATS), herramienta de agencia AI (AGENTE STUDIO), SaaS de facturación AI (FACTUM) y sus dashboards. **Léelo cuando construyas chat, asistente, copiloto, o cualquier interfaz con IA generativa/agente.** Términos y librerías en inglés.

## 0. Stack de referencia 2026

- **Vercel AI Elements** (`npx ai-elements@latest`): 40+ componentes React sobre **shadcn/ui** + **AI SDK** (`useChat`), editables como código tuyo. Familias: *Chatbot* (Conversation, Message, PromptInput, Response, Reasoning, Tool, Task, Sources, InlineCitation, Suggestion, Confirmation, Plan, Checkpoint, Model Selector, Chain of Thought), *Code* (Artifact, CodeBlock, WebPreview, Terminal), *Voice*, *Workflow* (Canvas, Node, Edge).
- **assistant-ui**: primitivas sobre Radix ("el Stripe del chat AI"), streaming + auto-scroll + typing + a11y. Adaptadores AI SDK/LangGraph/Mastra.
- **prompt-kit / shadcn.io AI**: 50+ bloques copy-paste.
- Patrón pragmático: arranca con **Vercel AI Chatbot** y reemplaza su UI con **AI Elements** a medida que madura tu design system.
- Catálogos de patrones (nombres canónicos): **Shape of AI** (shapeof.ai), AI UX Playground, NN/g.

## 1. Anatomía de la conversación

- **Lista de mensajes:** tendencia frontier = **asistente full-width SIN burbuja**, usuario en burbuja a la derecha (ChatGPT/Claude/Perplexity). Columna de lectura `max-width:640-768px` centrada (~65-75 car/línea). Espaciado entre turnos `24-32px`; burbuja usuario padding `12px 16px`, `border-radius:18px` (esquina del "tail" ~6px). Tipo 15-16px, `line-height:1.6`. Avatar asistente 24-28px.
- **Streaming de texto** (estándar token-by-token): NO rendericees crudo el chunk de red (llega a ráfagas) — desacopla con buffer typewriter ~**5ms/carácter** vía rAF (AI SDK v5: `smoothStream`/`experimental_transform`). Cursor `▍` parpadeante mientras `status==="streaming"`. Palabras nuevas con `fade/blur-in` ~120ms (lib **flowtoken**). Rápido = "pensando"; lento = fake.
- **Render de contenido:** detecta code fences durante el stream. CodeBlock con header (lenguaje + copy) y syntax highlight. Tablas con scroll horizontal en mobile. **Citations** inline `[1]` que abren la fuente + bloque "Sources" (favicon + título + dominio).
- **Composer (PromptInput):** multiline auto-grow (max ~40vh→scroll). `Enter` envía, `Shift+Enter` salto (en mobile, botón explícito). Botón: idle (disabled si vacío) → **Stop** (cuadrado) en streaming → Send. Toolbar: attach 📎, mic, model selector. Adjuntos como chips (thumbnail+nombre+X).
- **Acciones por mensaje:** fila ghost en hover bajo cada respuesta: **Copy, Regenerate, Thumbs up/down**, a veces **Branch** (re-prompt manteniendo el original) y Read aloud. Threads en sidebar agrupados ("Today / Yesterday / Previous 7 days").

## 2. UX generativa y de streaming

- **Generative UI** (AI SDK 3.0+, `streamUI`): el modelo devuelve **componentes React**, no solo texto. Tool call → data → componente (tool `getProduct` → `<ProductCard>`, tool `createInvoice` → `<InvoicePreview>`). AI SDK 6: abstracción **Agent** (streaming multi-step + tool calls).
- **Tool/step visualization:** muestra los pasos del agente como *cards intermedias inline* (no en debug panel). Componente `Tool`: `pending→running→complete/error` (spinner→check), nombre, args colapsados, output. `Task`/`Plan`: checklist que el agente va tachando. `Reasoning`/`Chain of Thought`: panel **colapsado por defecto** ("Thought for 4s") expandible.
- **Loading:** para generación, **skeleton shimmer** de 3-5 líneas de ancho decreciente (comunica proceso activo, no espera pasiva) — reduce ~40% el tiempo percibido vs spinner. Primer token <1s o el usuario abandona.
- **Optimistic UI:** pinta el mensaje del usuario ya; si falla, rollback + toast.
- **Action Plan** (Shape of AI): el agente muestra los pasos ANTES de ejecutarlos, en tareas largas.

## 3. Confianza, control y transparencia

**Reemplaza "¿Estás seguro?" por preview del resultado** (el confirm binario genera *confirmation fatigue*). Modelo **risk-tiered** (estándar 2026):
- **Low** (leer/buscar/ordenar): auto-ejecuta + log en activity feed.
- **Medium** (enviar mensaje/crear/agendar): **preview + one-click approve**.
- **High** (cobrar tarjeta/borrar/acción pública): **preview completo + confirmación explícita + ventana de undo**.

Aplica directo: enviar WhatsApp masivo o **cobrar una factura** = high → muestra mensaje/monto/destinatario exactos + "Deshacer" 5-10s. Patrones Shape of AI: *Verification, Controls* (pausar mid-stream), *Caveat, Consent, Disclosure* (marcar contenido AI), *Memory/Data Ownership*. Componentes **Confirmation**/**Checkpoint** en AI Elements. Nota: EU AI Act Art. 14 (oversight humano) obligatorio desde ago-2026 — HITL no es opcional.
**"AI can make mistakes"** bien hecho: línea sutil gris 12px bajo el composer ("Addrian puede equivocarse. Verifica datos importantes."), no banner amarillo.

## 4. Patrones AI-native más allá del chat

- **Inline AI / ghost text:** autocomplete estilo Copilot (sugerencia gris, `Tab` acepta).
- **Command palette + AI** (`⌘K`): añade modo "ask anything" (lenguaje natural ejecuta acciones o responde).
- **AI en forms:** *Auto-fill* (un prompt llena varios campos), *Prompt Enhancer*, *Madlibs*. Útil para crear producto/factura desde lenguaje natural.
- **Summarization UI** + *Suggestions/Sample Prompts* (chips de arranque para el "blank canvas"). *Initial CTA*: input grande y abierto como primera interacción.
- **Multimodal:** SpeechInput + Transcription (voz), drop de imagen/archivo, *Connectors*.
- **Identifiers** (Shape of AI): Avatar, Name (tu bot "Addrian"), Personality, Color/Iconography consistentes para señalar lo que es AI.

## 5. Diseño conversacional WhatsApp commerce (directo)

- **Botones vs texto libre:** quick replies (≤3 botones), **list messages** (>3 opciones), **CTA buttons** (links/llamada), **carousel** (hasta 10 productos: imagen+título+desc+URL c/u), **catálogo/product cards** nativos. Botones para decisiones cerradas/rutas; texto libre para intención/datos.
- **Product card:** imagen (sube CTR, ven sin salir del chat) + nombre + precio + botón "Pedir"/"Más info". No >2-3 botones; alterna con listas o video corto.
- **Pacing:** typing indicator antes de responder, pero **delay corto y honesto** (no fake delays largos). Trocea respuestas largas en 2-3 mensajes cortos, no un muro.
- **Handoff a humano:** anúncialo explícito ("Te paso con un asesor 👤"), haz 1-2 preguntas que llenan la espera y dan contexto. Taggea cada selección de botón para segmentar (CRM/campañas).
- **Flujo de venta:** saludo → quick replies de categoría → carousel de productos → card con CTA → recolección de datos (texto guiado) → **confirmación de pedido (preview, high-risk)** → handoff/cierre.

## 6. Frescura 2026 vs AI UI dateado

**Current:** limpio, rápido, transparente, *calm interfaces* (claridad > riqueza sensorial), generative UI, IA como **copilot reflexivo** (no autopilot omnisciente), tipografía sobria, neutros + 1 acento, animación que comunica **estado/estructura**, streaming veloz, citations verificables, disclosure honesto.

### AI-UI anti-slop blacklist
- ❌ Emoji **✨** en cada botón/feature "AI".
- ❌ **Gradiente morado→azul** como sinónimo de "AI" (el default de las herramientas AI = slop).
- ❌ **Liquid glass/glassmorphism** por todos lados, glows "premium".
- ❌ **Fake typing delays** largos para "parecer humano".
- ❌ **Muros de texto** sin listas/headings/cards.
- ❌ Confetti en hover, motion "kinetic" decorativo.
- ❌ Tono robótico/over-formal, o over-friendly con exceso de emoji.
- ❌ Spinners genéricos donde va skeleton shimmer.
- ❌ "¿Estás seguro?" en vez de preview real.
- ❌ Reasoning/tool steps crudos y verbosos por defecto (colápsalos).
- ❌ Avatar 🤖 metálico genérico como identidad del bot.

**Regla de oro:** cada elemento de UI AI debe **comunicar estado, fuente o acción** — si solo decora "para parecer AI", elimínalo.
