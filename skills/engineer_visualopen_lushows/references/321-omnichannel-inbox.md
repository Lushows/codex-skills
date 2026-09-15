# 321 · Inbox omnicanal (unificar canales, asignación, estados, métricas)

> Cuando el negocio vende por WhatsApp + Instagram + Telegram, el cliente es uno solo pero llega por tres puertas.
> La bandeja omnicanal es donde el bot y los humanos colaboran sobre una sola línea de tiempo por contacto — el dashboard que convierte canales sueltos en operación.

## El problema de los silos
Tres apps abiertas, tres historiales, cero memoria compartida: el operador no sabe que el "@juan" de Instagram es el mismo "+57 300..." de WhatsApp que ya compró. Resultado: respuestas duplicadas, contexto perdido, el bot pisando al humano. La bandeja unificada resuelve **identidad, estado y enrutamiento** en un solo lugar.

## Arquitectura: normalizar al núcleo
Cada canal entra por su adapter (ver [[320-telegram-discord-instagram-messaging]]) y se normaliza a un **evento interno común**: `{contacto_id, canal, direccion, tipo, contenido, timestamp}`. El núcleo (LLM, memoria, funnel, store) no sabe de qué canal viene. La bandeja lee de un **store por conversación** (in-memory + persistido a disco) que un EventEmitter empuja al dashboard por WebSocket en vivo — patrón exacto de `src/store.js` + Socket.IO en BIO-SETA.

## Identidad de contacto
Clave: **un perfil por persona, no por canal**. Si el mismo humano escribe por WA y por IG, idealmente fusionas (por teléfono/email capturado). Mínimo viable: perfil por número con historial, ciudad, compras, presentación preferida — para que el bot retome sin re-preguntar. El merge cross-canal real es difícil (no hay llave común garantizada) → empieza por canal y fusiona cuando tengas señal fuerte (mismo teléfono).

## Estados de conversación
Toda conversación tiene **estado explícito**, sin esto hay doble respuesta:

| Estado | Quién responde | Disparador |
|---|---|---|
| `ia_activa` | el bot | default |
| `ia_pausada` | humano | operador toma control |
| `esperando_operador` | nadie aún | intención de compra / escalamiento |
| `fuera_horario` | auto-reply de horario | fuera del horario configurado |

El flag de pausa va **por contacto**, persistido. Re-activación manual o por timeout (no la dejes pausada para siempre).

## Asignación y enrutamiento
- **Round-robin / por carga** si hay varios operadores; mínimo: una cola única.
- **Por etapa de funnel**: contactos "en negociación" → operador senior; "explorando" → el bot.
- **Por canal/idioma** si aplica.
La intención de compra dispara una **notificación al operador** con contexto completo (últimos mensajes, perfil, etapa), no un "tienes un chat".

## Métricas que importan (el dashboard)
| Métrica | Por qué |
|---|---|
| Funnel por etapa | dónde se cae la venta |
| Tasa de fallback del bot | falta conocimiento/prompt malo (ver [[318-chatbot-conversational-ux]]) |
| Tiempo a primera respuesta humana | SLA del handoff |
| % mensajes gratis vs template | costo real (cruza pricing de [[317-whatsapp-cloud-api-deep]]) |
| Recompras / clientes recurrentes | salud del negocio |
| Actividad por hora / ciudad | cuándo y dónde está la demanda |

Mide el **costo por conversación** leyendo `pricing.billable` de los webhooks de status, no lo estimes.

## Antipatrones
- Mostrar canales en pestañas separadas en vez de una línea de tiempo por contacto.
- No persistir el estado de pausa → el bot responde encima del humano al reiniciar.
- Métricas de vanidad (total de mensajes) en vez de funnel + costo.

## Cierre
El diseño del handoff y la intención que alimentan esta bandeja están en [[318-chatbot-conversational-ux]]. Para gestionar la media que circula por todos los canales cruza con [[263-asset-gallery-management]].
