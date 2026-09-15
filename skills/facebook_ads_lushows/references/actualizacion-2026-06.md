# ⏱️ Actualización Meta Ads — snapshot 13-jun-2026 (LEER PRIMERO si dudas si algo cambió)

Changelog fechado de lo que cambió en Meta Ads en 2025–2026. La verticalidad de la subasta y "el creativo
es el targeting" siguen igual; lo que cambió son **features, precios, atribución y políticas concretas**.
Cada ítem dice **[CONFIRMADO]** (fuente Meta/regulador) o **[RODANDO/vendor]** (reportado, verifica en TU cuenta).
Cruza con el módulo de fondo indicado. Re-verifica trimestral: en Meta lo "nuevo" caduca rápido.

## 1. Estructura de campaña — la unificación Advantage+ (ver 10, 12, 90)
- **[CONFIRMADO] Las campañas "manuales" desaparecieron como objeto separado (overhaul ~feb-2026).** Hoy hay
  **un solo flujo de creación** con toggles Advantage+ **encendidos por default** por sección (audiencia,
  ubicaciones, presupuesto, creativo). **Opt-OUT por sección**, ya no opt-in. Ya no eliges "Manual vs ASC".
- **[CONFIRMADO] ASC se llama ahora "Advantage+ Sales"** (renombrado 2025) y su alcance se amplió de e-com a
  también **leads y app installs**. Existe **Advantage+ Leads** (lead-gen automatizado) y **Advantage+ App**.
- **[CONFIRMADO] Cap de clientes existentes (mar-2026):** puedes limitar el **% de presupuesto** que va a
  compradores actuales → fuerza adquisición de NUEVOS. **Pon 25–30%.** Arregla el viejo truco de ASC que
  inflaba ROAS retargeteando a quien ya iba a comprar.
- **[CONFIRMADO] Omnichannel Advantage+:** optimiza ventas online + tienda física juntas (útil para local, ver 57).

## 2. El algoritmo — GEM encima de Andromeda (ver 92)
- **[CONFIRMADO] Andromeda** (motor de retrieval) terminó su rollout global ~oct-2025. Sigue: **creativo = targeting**.
- **[CONFIRMADO] GEM (Generative Ads Recommendation Model, paper nov-2025):** modelo generativo grande que se
  sienta ENCIMA del stack y **enseña a los modelos de entrega por destilación**; evalúa el anuncio dentro del
  **journey completo** del cliente, no aislado. Meta dobló las GPUs de GEM en Q4-2025. Implicación: pensar
  "optimizo este ad solo" quedó viejo.
- **[CONFIRMADO] Entity ID:** creativos casi-iguales se COLAPSAN en una sola entidad y compiten entre sí →
  **10–15 creativos CONCEPTUALMENTE distintos**, no 100 casi-duplicados. **Vida útil del ad bajó a ~2–4 semanas**
  (antes 6–8) → pipeline de refresco más rápido (ver 39).
- **[OJO] "Lattice"** aparece en blogs de agencias como "capa de ranking unificada" pero **Meta NO usa ese
  nombre** en fuentes primarias. La consolidación de ranking es real; el nombre es jerga — no lo cites a clientes.

## 3. Creativo con IA — qué está VIVO (ver 91, 90)
- **[CONFIRMADO] Vivo en Ads Manager:** **image-to-video ("Video Generation 2.0")** — hasta 20 fotos de producto
  → video multi-escena (Meta arma secuencia/transiciones/formatos); **variaciones de texto**, generación de
  fondo/imagen, mejora de audio — todo en **Advantage+ Creative Suite** al crear el ad.
- **[ANUNCIADO, NO ENTREGADO] "Creación de anuncios de punta a punta por IA"** (visión de Zuckerberg: subes
  foto + presupuesto + objetivo + cuenta bancaria y Meta hace TODO) — prometido **para fin de 2026**, hoy las
  herramientas tienen reseñas mixtas. No le vendas esto a un cliente como si ya existiera.
- **[CONFIRMADO] Anuncios con visuales generados por IA deben llevar etiqueta** (lote de políticas 2026, ver 8/44).

## 4. 🔴 Meta Business Agent — relevante DIRECTO a tus bots (ver 50, 96; GASTROWHATS/AVISPA'O)
- **[CONFIRMADO] Lanzado global el 3-jun-2026:** agente de IA de Meta que corre dentro de **WhatsApp Business,
  Instagram DMs, Messenger y Business Suite**. Responde, recomienda del catálogo, **agenda citas, califica leads**,
  resume chats perdidos, y avisa cuándo entra un humano.
- **Es el PRIMER agente de IA que Meta COBRA** (gratis al inicio → pago: pymes vía **WhatsApp Business Premium**;
  grandes por **tokens**). **Implicación estratégica:** Meta ahora compite de frente con bots de WhatsApp a la
  medida (como los tuyos). Decisión de producto, no de pauta — vigílalo, no lo ignores.

## 5. Placements — qué entró y qué murió (ver 02, 33)
- **[CONFIRMADO] Threads es placement DEFAULT y a escala** (400M+ MAU, CPMs bajos): sirve automático en
  Advantage+ salvo que lo excluyas. Hay **Threads video ads** (NewFronts 2026).
- **[CONFIRMADO] Instagram Explore ELIMINADO como placement (ene-2026)** — ya no se selecciona en campañas nuevas.
- **[CONFIRMADO] Reels post-loop ads ELIMINADO (nov-2025)** — quedan los overlay ads de Reels.
- **[CONFIRMADO] WhatsApp Status ads** — nuevo placement en la pestaña Updates (~1.5B usuarios/día).
- **Reels Trending Ads** (junto al top de Reels). Para tu pyme: sigue dejando placements en **Advantage+ (automático)**.

## 6. Pujas y medición (ver 15, 16, 65)
- **[CONFIRMADO] 5 estrategias de puja:** Highest Volume, Highest Value, Cost Cap, Bid Cap y **Minimum ROAS /
  ROAS Goal** (optimización por valor; necesita ~100+ compras con valor; solo puja en subastas que cree que
  cumplen tu piso de ROAS).
- **[CONFIRMADO] Value Rules:** multiplicadores sobre tu estrategia base (ej. +50% sobre un cost cap de $10 →
  hasta $15 de CPA para ese segmento). **Solo con estrategias automáticas** (Highest Volume/Value), no con cap/bid manual.
- **[CONFIRMADO] Atribución incremental (nuevo ajuste en Ads Manager):** usa ML contrafactual (entrenado con
  Conversion Lift) para optimizar por las conversiones que el anuncio **causó de verdad**, no last-touch. **Reporta
  MENOS conversiones** (quita las que igual iban a pasar) — no te asustes, es la verdad. Pruébalo en cuentas con volumen.
- **🔴 [CONFIRMADO] 12-ene-2026: Meta QUITÓ las ventanas view-through de 7 y 28 días del Ads Insights API.** Solo
  quedan ventanas por CLIC. También recortó retención: conteos únicos a **13 meses**, frecuencia a **6 meses**,
  breakdowns MMM solo por job asíncrono. **Implicación:** deja de juzgar retargeting/WhatsApp por view-through (ya
  casi no existe en el reporte); estándar = **7d-click / 1d-view**, y valida escalado con geo-holdouts (ver 65).

## 7. 🔴 Señal / CAPI — el piso subió (ver 05, 06, 62)
- **[CONFIRMADO] "Píxel" se llama ahora "Dataset"** en Events Manager (el Pixel ID = Dataset ID; paraguas de
  píxel + CAPI + offline).
- **[CONFIRMADO/RODANDO] CAPI de un clic (Meta-hosted):** botón **"Activate Conversions API"** en Events Manager
  → Meta levanta el server-side y pone el `event_id` para dedup solo. Se amplió a anunciantes solo-píxel ~may-2026.
  Sigue existiendo el **Conversions API Gateway** (sin código).
- **[RODANDO/vendor] EMQ: el piso práctico subió a 8+** (antes 6). En la era Andromeda la calidad de datos pesa
  tanto que píxel-solo (EMQ 3–5) ya no compite. Manda 8+ identificadores hasheados (en LatAm: **teléfono** es oro).

## 8. WhatsApp / CTWA — cambió el PRECIO (ver 50, 53) — lo más importante para Colombia
- **🔴 [CONFIRMADO] 1-jul-2025: WhatsApp pasó de cobro por-conversación (sesión 24h) a cobro POR-MENSAJE.** Pagas
  por **plantilla entregada**, según categoría × país. 4 categorías: **Marketing** (cara), **Utility**,
  **Authentication**, **Service** (gratis dentro de la ventana de 24h de atención).
- **[CONFIRMADO] Colombia = de los más baratos de LatAm:** Marketing ≈ **$0.0125/msg**, Utility/Auth ≈
  **$0.0008/msg** (subieron poco el 1-oct-2025, siguen bajísimos). Ventaja de costo real para ti.
- **[CONFIRMADO] Ventana gratis de 72h del CTWA:** al responder dentro de 24h a quien llegó por un ad CTWA, se
  abre una **ventana de 72h gratis** que cubre **todas las categorías, incluido marketing**. Economía excelente para tu bot.
- **🔴 [CONFIRMADO] Medición CTWA correcta:** por default optimiza "conversaciones iniciadas" (trae saludadores).
  Para optimizar por COMPRADORES, tu bot debe **capturar el `ctwa_clid`** (click id que llega al iniciar el chat)
  y disparar un **evento CAPI con `action_source`/evento = `business_messaging` y `messaging_channel: "whatsapp"`**
  cuando el lead califica/paga. Sin esos campos, Meta no atribuye la venta al ad. Es el upgrade #1 de un buyer
  WhatsApp-first (ver 53).
- **[CONFIRMADO] Señales de chat con IA en Advantage+:** Meta inyecta intención conversacional de Meta AI a la entrega.

## 9. Lead ads (ver 52, 58)
- **[CONFIRMADO] Doble ubicación de conversión:** una campaña sirve **instant form** a los rápidos y **form web**
  a los que buscan contexto (Meta reporta −60% CPL / +125% volumen vs solo-web). **Advantage+ Leads** automatiza todo.
- Añadidos: calificación de leads con IA, verificación, más integraciones CRM.

## 10. Políticas / compliance (ver 08, 87)
- **[CONFIRMADO] Nueva categoría especial "Financial Products and Services" (14-ene-2025)** (US/US-targeted) que
  reemplaza "Credit" y amplía a banca, ahorro, seguros, inversión, préstamos. Restringe targeting (sin ZIP/radio,
  sin edad/género, sin lookalikes, 18–65+).
- **[CONFIRMADO/RODANDO] Enforcement más duro de HEC (vivienda/empleo/crédito)** con detección automática:
  correr una categoría que DEBÍA marcarse como especial es hoy causa común de restricción de cuenta (ver 93).
- **[RODANDO/vendor] "Data Source Declaration":** quien use remarketing/custom audiences deberá **declarar el
  origen del dato y probar consentimiento**; audiencias sin consentimiento demostrable quedan inelegibles (verifica en tu BM).
- **[CONFIRMADO] EU "consentir o pagar" / DMA:** multa €200M (abr-2025); opción "Less Personalized Ads" viva en
  EEA desde ene-2026. **Para Colombia: NO aplica** (solo afecta audiencias residentes en la UE).

## Cómo usar este módulo
Es la **capa de actualidad** sobre los módulos de fondo. Si un módulo viejo y este snapshot chocan en un dato
fechado (precio WhatsApp, ventana de atribución, nombre de ASC), **manda este**. Re-verifica con búsqueda fresca
cada trimestre — y cuando un cambio de Meta cueste plata o confunda, agrega su fila aquí con fecha y fuente.
