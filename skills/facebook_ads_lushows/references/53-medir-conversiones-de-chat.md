# 53 — Medir conversiones de chat: cerrar el loop cuando vendes por WhatsApp

El problema central de vender por chat: **el píxel no ve lo que pasa dentro de WhatsApp**. Meta sabe que alguien inició conversación; no sabe si compró. Sin cerrar ese loop, optimizas y escalas a ciegas: la campaña "ganadora" puede ser la que trae más curiosos. Lee este módulo apenas tu pauta CTWA (ver 50) tenga 2+ semanas corriendo. Hay tres niveles — empieza donde estés. Jerga: "CAPI" = *Conversions API*, el canal server-side que manda eventos a Meta; "`ctwa_clid`" = el click-id único de la conversación que nació de un ad.

## Nivel 1 — Básico: etiquetas manuales + conteo honesto (pyme sin stack)

- En WhatsApp Business app, crea etiquetas: `Nuevo`, `Interesado`, `Pedido`, `Cliente`, `No calificado`.
- Quien atiende etiqueta CADA chat al cambiar de estado. Disciplina, no tecnología.
- Cada semana (mismo día, misma hora) cuentas: conversaciones nuevas, pedidos, ventas, plata. Cruzas contra gasto por campaña en Ads Manager.
- Limitación: si corren varias campañas a la vez, no sabes cuál trajo cada venta — mitígalo con mensajes pre-llenados distintos por campaña ("Hola, vi el anuncio del combo X") y anota de cuál vino cada pedido.
- Es burdo pero infinitamente mejor que nada. Te da CPA real aproximado por semana.

## Nivel 2 — Medio: el referral del CTWA (atribución por conversación)

Cuando alguien llega a tu WhatsApp desde un ad, el **primer mensaje llega con metadata del anuncio** (objeto `referral` en el webhook de la Cloud API): `source_id` (ID del ad), `source_url`, headline, body y **`ctwa_clid`** (el click ID de esa conversación, la llave de oro para el nivel 3).

```json
"referral": {
  "source_type": "ad",
  "source_id": "120210000000000",      // ID del ad → qué campaña
  "headline": "Combo Melena + Reishi 20% off",
  "ctwa_clid": "AffdEj2...",            // 🔑 la llave para CAPI nivel 3
  "media_type": "image"
}
```

- Tu bot/CRM **guarda esa metadata en el perfil del contacto** en el primer mensaje. Es un campo más en tu JSON/base de datos — pídeselo explícitamente a quien construye el bot (specs completas: ver 54).
- Al cerrar una venta, ya sabes **qué ad exacto la trajo**. Atribución real por anuncio sin píxel.
- Con la app de WhatsApp Business (sin API) ves un banner "viene del anuncio X" en el chat: anótalo a mano — versión artesanal del mismo dato.
- Esto resuelve la medición. Lo que aún no hace: enseñarle a Meta. Para eso, nivel 3.

## Nivel 3 — Pro: CAPI for business messaging (Meta optimiza por TUS ventas de chat)

CAPI for business messaging: tu sistema **envía eventos de vuelta a Meta** vía API, asociados al `ctwa_clid` guardado en nivel 2. Meta deja de optimizar por "conversaciones" y aprende a traer **gente que compra en chat**.

Eventos típicos a enviar (defínelos UNA vez y nunca cambies la definición):

| Evento | Cuándo lo dispara tu bot/CRM |
|---|---|
| `LeadSubmitted` / lead calificado | Respondió calificación: ciudad + producto + intención real |
| `OrderCreated` / pedido | Dio datos de envío / confirmó pedido en chat |
| `Purchase` | Pago confirmado (Nequi/Wompi/contraentrega entregada), con `value` y `currency` |

### Estructura del evento CAPI (lo crítico)

```jsonc
{
  "action_source": "business_messaging",
  "messaging_channel": "whatsapp",        // 🔴 obligatorio para chat
  "event_name": "Purchase",
  "event_time": 1718300000,
  "user_data": {
    "ctwa_clid": "AffdEj2...",            // 🔑 del referral (nivel 2)
    "phone": "<sha256 del teléfono>"      // teléfono = oro en LatAm (EMQ)
  },
  "custom_data": { "value": 90000, "currency": "COP" }
}
```

- Setup: dataset en Events Manager conectado a tu número de WhatsApp Business → tu backend hace POST a la Conversions API con el evento + `ctwa_clid` + timestamp. Lo implementa quien tenga el bot en Cloud API (ver 96).
- 2026: en Events Manager el "píxel" se llama ahora **Dataset**, y hay botón **"Activate Conversions API"** (Meta-hosted) de un clic. Manda **8+ identificadores hasheados** — el EMQ práctico subió a 8+ y en LatAm el **teléfono es el dato de oro** (ver `actualizacion-2026-06` §7).
- El premio: puedes crear campañas **Sales → WhatsApp optimizando por Purchase de chat** (ver 50). Es la diferencia entre pagar por saludos y pagar por compradores.
- Señales nativas que también ayudan: **orders in chat / carrito de WhatsApp** (pedidos desde el catálogo, ver 55) — Meta los ve como señal de compra dentro del ecosistema.

## El embudo de chat medible

Define estos 4 eventos y mídelos SIEMPRE igual, semana a semana:

```
Conversación iniciada → Respondió al bot (engagement real) → Dato de pedido → Venta
        100%                    ~60-80%                        ~10-25%        ~5-15%
```

Los % son referenciales; lo importante es TU línea base. Cuando un escalón cae, sabes dónde mirar: caen conversaciones → ad/segmentación (ver 30); cae respuesta al bot → saludo incongruente (ver 54); cae pedido→venta → cierre/precio/stock (ventas_lushows 82).

## Dashboard mínimo semanal

Una hoja de cálculo, una fila por campaña, cada lunes:

| Campaña | Gasto | Conversaciones | Costo/conv | Ventas | Ingresos | CPA real | ROAS |
|---|---|---|---|---|---|---|---|
| Combo A | $300.000 | 75 | $4.000 | 14 | $1.260.000 | $21.428 | 4,2 |
| Combo B | $300.000 | 110 | $2.727 | 9 | $810.000 | $33.333 | 2,7 |

Lectura: Combo B tiene **costo por conversación más barato** ($2.727 vs $4.000) pero **CPA real peor** ($33.333 vs $21.428) y ROAS más bajo. Si solo miraras costo/conv, escalarías al perdedor. Decisiones que salen de ahí: apagar la campaña de costo/conv barato pero CPA real caro; escalar la de ROAS sano (ver 13/15 para no romper aprendizaje). 30 minutos a la semana que valen más que cualquier columna de Ads Manager.

## Nota sobre atribución 2026

Meta quitó las ventanas view-through de 7 y 28 días del Insights API (12-ene-2026); el estándar es **7d-click / 1d-view** (ver `actualizacion-2026-06` §6). En chat esto importa poco — tu fuente de verdad es el `ctwa_clid` + tu conteo de ventas, no el reporte view-through. Si escalas fuerte, valida con un geo-holdout (ver 65) en vez de creerle ciegamente al número de Ads Manager.

## Errores comunes — blacklist

- Escalar por "costo por conversación" sin ventas atribuidas: premias al ad de los curiosos.
- No guardar el `referral`/`ctwa_clid` desde el día 1: la atribución no es retroactiva; cada conversación sin metadata es ciega para siempre.
- Cambiar la definición de "lead calificado" cada mes: rompes la serie histórica Y confundes al algoritmo si mandas CAPI.
- Enviar a CAPI eventos basura (todo chat = "Lead"): Meta optimiza hacia basura con precisión industrial.
- Montar nivel 3 sin nivel 1 de disciplina: la tecnología no arregla un equipo que no etiqueta ni registra ventas.
- No mandar `value` en el Purchase: sin valor no hay ROAS por campaña ni optimización por valor.
- Olvidar `messaging_channel: "whatsapp"` o el hash del teléfono en el evento: el EMQ cae y Meta atribuye mal (ver `actualizacion-2026-06` §7).
