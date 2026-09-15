# 115 — Gmail vs Outlook: deliverability por proveedor

No todos los proveedores de correo filtran igual, y a escala eso te obliga a estrategia. **Google (Gmail / Google Workspace) y Microsoft (Outlook / Office 365 / Hotmail / Live) concentran más del 90% del correo B2B**, y son bestias distintas: Gmail premia el engagement y te da un tablero transparente (Postmaster; ver `113`); Outlook es más severo, más opaco, y castiga el volumen y el contenido con reglas rígidas. Mandar la misma campaña a los dos como si fueran uno solo es por qué muchos ven "buen inbox en Gmail, spam total en Outlook". Este módulo explica las diferencias reales y cómo ajustas tu operación a cada uno. Saber a qué proveedor le escribes (dato que sacas del dominio del prospecto; ver `28`) se vuelve una palanca de deliverability.

## El mapa: quién usa qué

Del dominio del correo del prospecto puedes inferir su proveedor y por tanto cómo filtra:

| Dominio del prospecto | Proveedor real | Filtro |
|---|---|---|
| `@gmail.com` | Google (personal) | Gmail |
| Dominio corporativo con MX de Google | Google Workspace | Gmail (empresarial) |
| `@outlook.com`, `@hotmail.com`, `@live.com` | Microsoft (personal) | Outlook consumer (durísimo) |
| Dominio corporativo con MX de Microsoft | Office 365 / Exchange Online | Microsoft Defender (durísimo) |
| Otros (Zoho, Proofpoint, Mimecast, etc.) | Varía | Gateways de seguridad, muy estrictos |

**Cómo saber el proveedor de un dominio:** revisa su registro MX (MXToolbox → "MX Lookup"). `google.com` en el MX = Workspace; `outlook.com`/`protection.outlook.com` = Microsoft; `mimecast`/`pphosted` = gateway de seguridad corporativo (los más difíciles). Herramientas de enriquecimiento (Clay; ver `31`) pueden etiquetar el ESP de cada contacto para segmentar.

## Gmail: premia engagement, es transparente

Cómo piensa Google:

- **La señal reina es el engagement:** aperturas, respuestas (la más fuerte), rescate de spam, "marcar importante". Un buzón con buen engagement entra a Primary aunque el volumen sea decente (ver `40`).
- **Te da datos:** Google Postmaster (ver `113`) te muestra Domain Reputation, Spam Rate y Authentication. Es el proveedor donde **puedes pilotar con instrumentos**.
- **Pestañas:** Primary / Promotions / Social / Updates. Caer en **Promociones** no es spam, pero baja mucho la respuesta. Lo que te manda a Promociones: muchos links, imágenes, HTML pesado, lenguaje de marketing, firmas con logos/tracking. Correo texto plano, 1 link, tono 1-a-1 → Primary.
- **Umbral de queja:** Spam Rate < 0.1% sano, > 0.3% crítico.

Ajuste para Gmail: texto plano, personal, un solo link, cero imágenes, foco en **provocar respuesta** (el engagement que Gmail premia). Verifica dominios en Postmaster y guíate por ese tablero.

## Outlook / Microsoft: severo, opaco, castiga volumen y contenido

Cómo piensa Microsoft (Defender / SmartScreen):

- **Menos ponderado al engagement, más a reglas y reputación de IP/dominio + contenido.** Outlook puede mandarte a "Correo no deseado" por señales que a Gmail no le importan tanto.
- **Castiga el volumen brusco con dureza** y difiere/rechaza con códigos (`550 5.7.1`, `S3150`, referencias a spam). Rampa aún más lenta y conservadora que para Gmail.
- **Opaco:** no hay Postmaster equivalente rico. Tienes SNDS (si IP dedicada) y JMRP (te reenvía quejas de usuarios) — regístrate si mandas volumen a @outlook/@hotmail (ver `113`). En la práctica te guías por **bounce/códigos de rechazo y seed testing** (ver `116`).
- **Muy sensible al contenido:** links acortados (bit.ly), muchos links, dominios de tracking, palabras spam, y adjuntos lo disparan más rápido que en Gmail.
- **Gateways corporativos (Mimecast, Proofpoint)** delante de Office 365 son lo más estricto que hay: sandboxean links, bloquean por reputación de dominio de envío joven. Contra estos, la antigüedad del dominio y cero links sospechosos importan muchísimo.

Ajuste para Outlook: rampa más lenta, volumen por buzón más conservador (25–35, no 40+), **cero links acortados**, texto plano estricto, y no esperes tablero — audita con seed lists que incluyan Outlook.

## Tabla comparativa práctica

| Factor | Gmail / Workspace | Outlook / Microsoft 365 |
|---|---|---|
| Señal que más pesa | Engagement (respuestas) | Reputación + contenido + volumen |
| Transparencia | Alta (Postmaster) | Baja (SNDS/JMRP limitados) |
| Tolerancia a volumen | Media-alta si hay engagement | Baja; castiga picos |
| Sensibilidad al contenido | Media (pestaña Promociones) | Alta (spam directo) |
| Links acortados | Mal, pero tolera 1 link normal | Muy mal; evítalos por completo |
| Rampa recomendada | Estándar (ver `112`) | Más lenta y conservadora |
| Cómo auditar | Postmaster + seed list | Seed list + códigos de rechazo (ver `116`) |

## Estrategia a escala: segmentar por proveedor

Cuando tu volumen lo justifica, **separa tus envíos por ESP del destinatario**:

1. **Etiqueta cada contacto** con su proveedor (MX lookup vía Clay/enriquecimiento; ver `31`, `29`).
2. **Campañas o sub-listas separadas** para Gmail vs Outlook, con ritmo y contenido afinados a cada uno (Outlook más lento, más limpio).
3. **Aísla buzones/dominios por destino si algo se degrada:** si Outlook te empieza a rebotar, puedes bajar solo el flujo hacia Microsoft sin frenar Gmail.
4. **Mezcla tu flota de envío entre Google y Microsoft** (ver `110`): un buzón de Outlook a veces entrega mejor a destinatarios Outlook (misma "familia"), aunque no es regla dura.

Ojo: no te compliques de más si tu volumen es bajo. Segmentar por proveedor es palanca de gran escala; en volúmenes chicos, texto plano + lista limpia + rampa cuidada te resuelve el 90% en ambos.

## Errores comunes (qué NO hacer)

- Tratar Outlook como Gmail: misma rampa y contenido → spam en Microsoft.
- Usar links acortados (bit.ly) — Outlook y gateways corporativos los castigan durísimo.
- Esperar un "Postmaster de Microsoft": no existe rico; audita con seed lists (ver `116`).
- Ignorar los códigos de rechazo de Outlook (`S3150`, `550 5.7.x`): son tu único feedback claro ahí.
- No mirar el MX del prospecto y mandar todo igual: pierdes la palanca de segmentar por proveedor.

## Siguiente paso

Como Outlook no te da tablero, la forma de saber realmente dónde caes en cada proveedor es probar con cuentas semilla: ve a `116` (spam testing e inbox placement con seed lists de Gmail + Outlook + otros). Para leer la reputación de Gmail, `113`. Para la arquitectura de flota que mezcla proveedores, `110`. Para etiquetar el ESP de cada contacto, `29` y `31`.
