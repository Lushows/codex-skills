# 318 · UX conversacional (intención, fallback, handoff a humano)

> Un bot de IA que "responde bien" no basta: el negocio se pierde en los bordes — cuando el cliente quiere comprar, cuando el bot no entiende, cuando hay que pasar a un humano.
> El diseño conversacional es decidir qué pasa en esos bordes, no el prompt feliz del centro.

## Las tres preguntas de cada turno
En cada mensaje entrante el sistema decide: **(1) ¿qué quiere?** (intención), **(2) ¿puedo resolverlo?** (capacidad), **(3) ¿debo escalar?** (handoff). El caso BIO-SETA/Addrian las resuelve con una sola llamada al LLM que devuelve respuesta + señales (etapa de funnel, intención de compra), no con un clasificador separado.

## Detección de intención: keyword vs LLM
| Método | Cuándo | Costo | Falla en |
|---|---|---|---|
| Keywords ("quiero pedir", "cómo compro") | señales binarias de alto valor (notificar operador) | $0 | sarcasmo, typos, español regional |
| LLM con salida estructurada | etapa de venta, sentimiento, extracción de pedido | 1 call | latencia, costo por token |
| Híbrido (recomendado) | keyword dispara la alerta barata; LLM enriquece | bajo | — |

Para LatAm: el cliente escribe "me regala el precio", "a cómo", "tiene domicilio" — un keyword en inglés o español neutro no lo capta. Entrena tu lista con la jerga real del país (CO/MX/AR difieren).

## Fallback: qué hace el bot cuando no sabe
Nunca alucines stock/precio/envío. Jerarquía de fallback:
1. **Reformula** ("¿te refieres a la presentación en cápsulas o en polvo?") — recupera sin escalar.
2. **Acota a opciones** (interactive buttons, max 3) — reduce el espacio de error.
3. **Deriva a humano** con contexto, no con "no entendí".
Un bot que dice "no comprendo" 3 veces pierde la venta. Mide la **tasa de fallback** como KPI: si sube, falta conocimiento (ver [[41-whatsapp-cloud-api]] base de datos del bot) o el prompt está mal acotado.

## Handoff a humano: el momento crítico
Tres disparadores de escalamiento:
- **Intención de compra** detectada → notifica al operador (no necesariamente pausa el bot).
- **Operador toma el control** → **pausa la IA para ese contacto** (flag por número, in-memory + persistido). El bot NO debe responder encima del humano — el bug más común.
- **Frustración / fuera de alcance** (queja, reembolso, caso legal) → escala y silencia IA.

Reglas de oro del handoff:
- El humano recibe **el contexto completo** (últimos N mensajes, perfil, etapa), no solo "cliente espera".
- **Estado explícito por conversación**: `ia_activa | pausada | fuera_horario`. Sin esto, doble respuesta.
- **Re-entrega al bot**: cuando el operador cierra, reactiva la IA manualmente o por timeout. No la dejes pausada para siempre.

## Memoria y continuidad
El cliente no repite su nombre/dirección cada vez. Perfil persistente por número (historial de compras, ciudad, presentación preferida) → el bot retoma "¿otra vez Melena de León a la misma dirección?". Esto sube conversión de recompra más que cualquier prompt. Dos capas:
- **Memoria de sesión** (ventana de mensajes recientes) → coherencia dentro del chat.
- **Memoria de perfil** (persistida por contacto) → continuidad entre chats separados por días.
No metas todo el historial al prompt: resume el perfil a hechos (compró X, vive en Y, objeción fue Z) y pasa solo eso + últimos N turnos. Ahorra tokens y evita que el LLM se pierda.

## Media entrante
El cliente manda fotos (¿este producto?), audios (nota de voz en vez de escribir) y documentos. El bot debe: transcribir audio (Whisper) a texto antes del LLM, describir/analizar imagen con visión, y **persistir la media** (las URLs de Meta expiran ~5 min, ver [[317-whatsapp-cloud-api-deep]]). Un bot que ignora la nota de voz pierde al cliente que no escribe.

## Antipatrones que matan la conversión
- Menús de árbol rígido ("digite 1 para...") cuando ya tienes LLM — usa lenguaje natural.
- Responder fuera de horario con la IA en vez del mensaje de horario → promesas que el humano no cumple.
- Mensajes-muro: WhatsApp es chat, parte en burbujas cortas.
- Pedir datos que ya tienes en memoria.

## Cierre
Las plantillas/ventana 24h que limitan el reenganche están en [[317-whatsapp-cloud-api-deep]]. Para orquestar el bot como agente de producción con tools y estado, cruza con [[308-agentes-produccion-orquestacion]].
