# Automatizar la atención con IA

> El objetivo no es "que el bot conteste todo". Es que **el 70-80% de los mensajes se resuelvan solos
> y tú solo veas los que deciden dinero**. Un bot mal puesto pierde más ventas de las que ahorra en
> tiempo: contesta mal la duda de compra, molesta al que ya está enojado y te mete en contracargos.

## Qué se automatiza y qué no

| Tipo de mensaje | % típico | ¿Automatizar? | Por qué |
|---|---|---|---|
| "¿Dónde está mi pedido?" | 30-40% | **Sí, total** | Es una consulta de datos |
| "¿Cuánto tarda?" / "¿envían a X?" | 10-15% | **Sí, total** | Respuesta fija |
| Precio, formas de pago, garantía | 10-15% | **Sí, con guion** | Respuesta fija |
| Dudas de producto que cierran venta | 10-20% | **Sí, con IA real** | Aquí gana o pierde plata |
| Confirmación de pedido COD | — | **Sí** | Sube entrega 45-60% → 65-78% (`160`) |
| Cambio, devolución, reembolso | 5-10% | **Híbrido** | Bot recoge datos, humano decide |
| Cliente molesto | 3-8% | **Nunca** | Escalar de inmediato (`280`) |
| Amenaza de contracargo / legal | <2% | **Nunca** | Humano, y rápido (`282`) |

## Los tres niveles de automatización

| Nivel | Qué es | Costo | Cuándo |
|---|---|---|---|
| **1. Respuestas fijas** | Menú, autorespuesta fuera de horario, FAQ con botones | Casi cero | Desde el día 1 |
| **2. Bot con datos** | Consulta el pedido y el tracking en tu tienda | Bajo | Desde 10 pedidos/día |
| **3. Bot con IA** | Conversa, resuelve dudas de producto, cierra y confirma | Medio (API + servidor) | Desde 20-30 pedidos/día o antes si ya tienes el bot |

> **Ventaja del proyecto actual:** el dueño ya tiene construido un bot de WhatsApp con IA propio
> (Node + WhatsApp Cloud API + Claude, con panel de conversaciones, base de conocimiento editable,
> pausa de IA por número y notificación al operador). No hay que comprar nada ni pagar por asiento:
> se **reutiliza cambiando el contexto de tienda, el catálogo y las reglas de escalamiento**. Eso
> ahorra el costo típico de una plataforma de chat y, sobre todo, no te amarra a un proveedor. Ver
> también `162`.

## Cómo se adapta un bot existente a una tienda nueva

| Pieza | Qué cambiar | Nota |
|---|---|---|
| Contexto de tienda / system prompt | Nombre, producto, precio, plazos, garantía, política de devolución | Es el 80% del resultado |
| Catálogo | Producto, bundle, precios, fotos | `218` |
| Base de conocimiento | FAQ, objeciones, textos de `278` | Editable sin tocar código |
| Horario | Mensaje fuera de horario | `277` |
| Escalamiento al humano | Palabras y situaciones que pausan la IA | Ver tabla abajo |
| Consulta de pedido | Conectar al número de pedido y guía | Evita el 35% de los mensajes |
| Registro | Motivo y resultado por conversación | Alimenta `276` |

> **Trampa de producción conocida:** si el bot lee su conocimiento desde archivos semilla en el
> repositorio, editar esos archivos **no** actualiza el bot en vivo cuando ya existen en el disco
> persistente. Se edita desde el panel de producción o por la API. Es la causa #1 de "lo cambié y
> sigue igual".

## Reglas de escalamiento (no negociables)

El bot **para y llama al humano** cuando aparece cualquiera de estas:

| Señal | Ejemplo |
|---|---|
| Emoción fuerte | "estafa", "ladrones", "denuncia", mayúsculas sostenidas |
| Amenaza formal | "contracargo", "disputa", "profeco", "sic", "demanda", "banco" |
| Dinero | reembolso, cancelación, cobro duplicado |
| Reincidencia | 3 turnos sin resolver la misma duda |
| Duda que el bot no tiene en su base | mejor decir "lo confirmo y te escribo" que inventar |
| Ticket alto o compra mayorista | oportunidad de venta grande |

Y cuando escala, **el humano debe responder en menos de 30 minutos**. Un escalamiento que nadie
atiende es peor que no escalar.

## Lo que un bot no puede inventar nunca

| Prohibido | Consecuencia |
|---|---|
| Fechas de entrega exactas que no vienen de la guía | Contracargo por entrega tardía (`282`) |
| Disponibilidad de stock que no consultó | Venta que no puedes cumplir |
| Propiedades de salud o resultados del producto | Riesgo regulatorio (`143`, `293`) |
| Descuentos fuera de política | Rompe la economía unitaria (`223`) |
| Que ya se hizo un reembolso | Fraude percibido |

La instrucción explícita en el prompt: *"si no está en tu base de conocimiento, no lo inventes: di
que lo confirmas y escala."*

## Confirmación automática de pedidos (COD)

Si operas COD, esto es lo que más dinero mueve de todo el módulo.

| Configuración | Tasa de entrega |
|---|---|
| Sin confirmación | 45-60% |
| Con confirmación (bot o llamada) | 65-78% |
| Urbano con confirmación | 70-85% |

Flujo mínimo: mensaje a los 15-30 min del pedido → confirmar dirección y hora → botón "sí / cambiar
/ cancelar" → los "no confirmados" en 24 h se reintentan una vez y se cancelan. Ver `160`, `161`.

## Métricas del bot

| Métrica | Bueno | Qué significa si está mal |
|---|---|---|
| % resuelto sin humano | 65-80% | Base de conocimiento pobre |
| Tiempo de 1ª respuesta | < 30 s | Infraestructura |
| % escalado | 15-30% | Muy bajo = está inventando; muy alto = no sabe nada |
| Conversión de conversaciones pre-compra | 15-30% | Guion de venta débil (`277`) |
| Reclamos por "el bot me dijo mal" | < 1% | Alucinación: endurecer el prompt |
| Costo de IA por conversación | centavos de USD | Si duele, revisa contexto y caché |

Para bajar el costo de tokens sin degradar calidad (caché de prompt, contexto, ruteo de modelo),
**invoca `optimizer_tokens_lushows`**. Una advertencia práctica: recortar el prompt para ahorrar
suele costar más en ventas perdidas que lo que ahorra en API.

## Errores que hacen que el bot te cueste plata

| Error | Síntoma | Corrección |
|---|---|---|
| Bot sin acceso al pedido | "dame tu número de pedido" y no hace nada con él | Conectar la tienda |
| Menú de 8 opciones | La gente escribe igual | Menos botones, conversación libre |
| No dice que es un bot cuando preguntan | Desconfianza y quejas | Ser honesto si preguntan |
| Sin pausa manual | El humano y el bot escriben encima | Pausa por número desde el panel |
| Nunca se revisan las conversaciones | El bot se degrada callado | 10 conversaciones leídas cada semana |
| Se automatiza al cliente molesto | Escalada y reseña de 1 estrella | Regla de escalamiento |

## Checklist de puesta en marcha

- [ ] Contexto de tienda con precio, plazos, garantía y política escritos
- [ ] Las 16 plantillas de `278` cargadas en la base de conocimiento
- [ ] Consulta de pedido y guía conectada
- [ ] Reglas de escalamiento activas y probadas con mensajes reales
- [ ] Alerta al operador cuando hay intención de compra o escalamiento
- [ ] Horario y mensaje fuera de horario configurados
- [ ] Prohibición explícita de inventar fechas, stock y descuentos
- [ ] 20 conversaciones de prueba antes de abrirlo al público
- [ ] Revisión semanal de 10 conversaciones reales

## Relacionados
`277` atención que vende · `278` plantillas · `280` cliente molesto · `289` delegar la atención ·
`160` confirmación por WhatsApp · `161` confirmación por voz con IA · `162` reusar un bot propio ·
`272` email y WhatsApp · invoca `optimizer_tokens_lushows` (costo de IA)
