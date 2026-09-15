# 33 — Sequencers y sending tools

El sequencer (o "sending tool") es la herramienta que **manda tus correos en frío y corre las cadencias** automáticamente: define "correo 1 el día 0, seguimiento el día 3, break-up el día 8", conecta tus buzones y envía por ti a cientos de prospectos sin que toques cada uno. Es la categoría 3 del stack (`30`). Elegir mal aquí te cuesta caro: la diferencia entre las dos familias de herramientas no es de precio, es de **filosofía de envío**, y usar la equivocada quema tu reputación o desperdicia tu inversión. Este módulo te dice cuál usar cuándo.

## El principio: dos familias distintas

Hay dos tipos de sequencer y confundirlos es el error #1:

1. **Herramientas de cold email a volumen** (Instantly, Smartlead, Lemlist). Nacieron para enviar **correo frío desde muchos buzones/dominios secundarios** con rotación y warmup integrado. Su obsesión es la **deliverability** (llegar a bandeja). Se conectan a decenas de buzones baratos de Google Workspace/Outlook y reparten el volumen para no quemar ninguno (ver `44`, `110`).

2. **Plataformas de engagement / cadencia** (Outreach, Salesloft, y Apollo/HubSpot en parte). Nacieron para que un **equipo de SDRs con AEs** orqueste multicanal (email + llamada + LinkedIn + tareas) desde **buzones reales de la empresa**, con analítica, coaching y CRM profundo. Su obsesión es la **productividad del rep y el proceso**, no el envío masivo desde dominios quemables.

La regla: **volumen frío desde dominios secundarios → familia 1. Equipo estructurado tocando cuentas desde el buzón real → familia 2.**

## Comparativa

| Herramienta | Familia | Fuerte en | Ideal para | Precio aprox 2026 |
|---|---|---|---|---|
| **Instantly** | Cold email volumen | Simple, buzones ilimitados, warmup incluido, red de leads | Solistas/agencias, arrancar rápido | ~$37–97/mes |
| **Smartlead** | Cold email volumen | Rotación de buzones, master inbox, API potente, multi-cliente | Agencias, escala, muchos dominios | ~$39–94/mes+ |
| **Lemlist** | Cold email + multicanal | Personalización visual (imágenes/video), LinkedIn integrado | Personalización creativa, medio volumen | ~$69–99/asiento |
| **Apollo** | Datos + sequencer ligero | Todo-en-uno (datos+envío), barato | Arrancar con un solo tool | incluido en plan (~$49–99) |
| **Outreach** | Engagement enterprise | Cadencias multicanal, analítica, coaching | Equipos SDR/AE medianos-grandes | $$$ (contrato, por asiento) |
| **Salesloft** | Engagement enterprise | Cadence + conversation intelligence | Equipos enterprise con proceso | $$$ (contrato) |

Herramientas a fondo: Instantly `103`, Smartlead `104`, HubSpot para SDR `105`, Outreach/Salesloft/Salesforce `106`, Apollo `100`.

## Cuándo cada uno (árbol de decisión)

- **¿Estás validando outbound, solo o con 1–2 personas, y tu problema es "no tengo con qué mandar en frío sin caer en spam"?** → **Instantly** (el más simple) o **Apollo** si quieres datos+envío en uno.
- **¿Eres agencia o vas a manejar volumen alto / varios clientes con dominios separados?** → **Smartlead** (rotación y multi-cliente son su fuerte, ver `194`).
- **¿Tu diferenciador es personalización visual (imágenes/video dinámico) y medio volumen?** → **Lemlist**.
- **¿Tienes un equipo de SDRs + AEs, envías desde los buzones reales de la empresa, y necesitas cadencias multicanal con analítica y coaching?** → **Outreach** o **Salesloft**.
- **¿Ya vives en HubSpot y el volumen es moderado?** → las **Sequences de HubSpot** (`105`) pueden bastar sin sumar otra herramienta.

Punto clave: **no uses Outreach/Salesloft para spamear frío a volumen desde dominios quemables** —no es para eso y es carísimo— **ni uses Instantly como si fuera tu CRM/plataforma de equipo**. Cada familia en su carril.

## El detalle que decide todo: deliverability

Un sequencer de la familia 1 sirve **solo si lo alimentas con la infraestructura correcta**: dominios secundarios, buzones calentados, autenticación SPF/DKIM/DMARC y volumen seguro por buzón (~20–40/día). La herramienta envía; **tú** montas la fontanería. Sin eso, la mejor herramienta cae en spam igual. Todo esto vive en el Bloque 4:
- Dominios secundarios → `41`
- SPF/DKIM/DMARC → `42`
- Warmup → `43`
- Límites y rotación → `44`
- Evitar spam (spintax, links) → `45`

## Ejemplo: configuración de una campaña en Instantly/Smartlead

```
Campaña: "Clínicas dentales MX — Q1"
Buzones conectados: 6 (3 dominios × 2 buzones), todos con warmup ON
Límite por buzón:   25 correos/día  → 150 envíos/día máx
Rotación:           reparte los envíos entre los 6 buzones
Spintax en asunto:  {Pregunta rápida|Una duda|Idea para {company}}
Secuencia:
  Día 0  → Email 1 (opener personalizado con dato de Clay, ver 31/53)
  Día 3  → Email 2 (bump / valor, ver 63)
  Día 7  → Email 3 (caso o prueba social, ver 123)
  Día 12 → Email 4 (break-up, ver 63)
Stop on reply: ON   ← si responde, la secuencia se detiene sola
Tracking de apertura: OFF (los pixeles dañan deliverability en 2026)
```
`Stop on reply: ON` es obligatorio: nada peor que seguir enviando a alguien que ya respondió. La conversación que sigue a esa respuesta —convencer, manejar la objeción, cerrar— **no es tarea del sequencer**: eso es `ventas_lushows` (ver `64`).

## Errores comunes

- **Enviar desde el dominio principal** "porque ya lo pagué". Familia 1 = dominios secundarios siempre (ver `41`).
- **Apagar el warmup para "enviar más".** Quemas el buzón en días.
- **Dejar el tracking de apertura activado** — el pixel de apertura hoy penaliza deliverability; mídelo por respuestas, no por aperturas (ver `80`).
- **Elegir Outreach/Salesloft siendo solista.** Pagas miles por features de equipo que no usas.
- **No conectar el sequencer al CRM.** Los estados no fluyen y duplicas contactos (ver `32`, `34`).

## Siguiente paso

Elige tu familia (volumen frío → Instantly/Smartlead; equipo estructurado → Outreach/Salesloft) y **antes de enviar el primer correo** monta la infraestructura de deliverability del Bloque 4 (`41`–`45`). Conecta el sequencer al CRM (`32`) vía integración (`34`). Diseña la cadencia día-por-día en `60`; escribe el copy en el Bloque 5 (`50`+).
