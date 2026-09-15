# 27 · Pagos y cobro

> Fuentes: engineer_visualopen 42-pagos-latam y 295-pagos-latam-wompi-mercadopago · código real `src/lib/bold.ts`, `src/lib/suscripcion.ts` y `api/bold/webhook/route.ts`. La verdad del cobro está en el código; este archivo lo destila para que AVIS hable con seguridad.

## ⚠️ ACTUALIZACIÓN 24-jun-2026 (esto MANDA sobre lo de abajo)
- **Pasarela = MercadoPago** (suscripción/preapproval), NO Bold. Env en Vercel: `MP_ACCESS_TOKEN`, `MP_WEBHOOK_SECRET`. Webhook `https://avispao.app/api/mercadopago/webhook` (valida firma en suscripción y pago). Lo de **Bold** de aquí abajo queda como referencia histórica.
- **Precios y nombres (1:1 web↔bot):** Plus **39.900** · Premium **79.900** · Negocio **149.900** · Multi **199.900**. Anual = paga 10, lleva 12. (Los nombres viejos "Emprende/Empresarial" ya NO se usan.)
- **IVA por segmento** (`ivaIncluidoDeComercio`): **persona natural / no responsable de IVA → precio IVA INCLUIDO** (paga $39.900 tal cual); **empresa / responsable de IVA → +IVA** ($47.481, que descuenta). Se deduce del `perfil_tributario` o de la estructura/registro.
- **Confirmación de compra:** al activar, AVISPAO envía el correo **"🎉 Tu plan AVISPA'O ya está activo"** (`enviarPlanActivo`), además del recibo automático de MercadoPago.

### Pago por WEB → enlazar el WhatsApp (CÓMO GUÍA AVIS si preguntan)
Quien paga por la web tiene su WhatsApp **aún sin enlazar**; el plan vive en su cuenta (correo). Para que AVIS lo reconozca por WhatsApp:
1. El **correo de confirmación** trae un botón **"Conéctate con AVIS"** que YA lleva el **código de vínculo (AV-)** → al tocarlo y escribirle a AVIS, su WhatsApp queda enlazado y AVIS reconoce el plan al instante (`vincularComercio`).
2. O entra a **avispao.app con el MISMO correo** con que pagó → su panel muestra el plan + un botón para **conectar WhatsApp**.

**Regla de AVIS:** si un cliente dice *"ya pagué / no me reconoce / pagué por la web / cómo conecto"* y **este número NO está activo**, AVIS **NO responde "plan activo"** — da el **paso a paso** de arriba (correo+botón, o panel con el mismo correo). Si el número **YA está activo**, celebra y sigue. (Handler real en `conversacion.ts`: `dicePago`/`pideEnlace` + `servicioActivo`.)

**Recuperación si paga y se cierra:** el pago **no se pierde** (vive en su comercio, identificado por la referencia del cobro); reentra con el **mismo correo** y ve el plan activo + el código. Único caso de soporte manual: si pagó con un **correo distinto** al de su cuenta → fusión a mano.

## Cómo cobra AVISPA'O hoy (Bold)
El plan de AVISPA'O es una **suscripción mensual** que se cobra con **Bold** (pasarela colombiana). Flujo real:
1. AVIS/panel llama `iniciarCobro` → registra un **cobro pendiente** en la tabla `cobros` (su `id` es la **referencia única**) y pide a Bold un **link de pago** (`crearLinkPago`, monto cerrado en COP).
2. El cliente abre el link y paga con el método que prefiera.
3. Bold dispara el **webhook** `SALE_APPROVED` → verificamos la firma → `activarCobro` marca el cobro `activo`, fija `proximo_cobro` (+1 mes), pone el comercio en `plan: activo` y manda la **bienvenida automática por WhatsApp**.

El precio vive en `PLAN_MONTO` (`BOLD_PLAN_AMOUNT`, por defecto **$29.900 COP/mes**). Cambiarlo NO requiere tocar código.

## Medios de pago en Colombia
En Colombia el dinero local vive en estos rieles (Bold los habilita todos por defecto al no fijar `payment_methods`):

| Método | Cómo se siente para el cliente | Recurrente |
|---|---|---|
| **Tarjeta** (débito/crédito) | la más simple, se tokeniza | sí (token) |
| **PSE** | redirige al login del banco | no nativo |
| **Nequi** | push a la app, celular 10 dígitos | limitado |
| **Bancolombia Transfer / otros** | según la pasarela | varía |

Pasarelas que usan los negocios colombianos: **Bold** (la nuestra), **Wompi** (de Bancolombia, default del país) y **MercadoPago** (dominante regional). Todas cobran en **COP enteros** (sin decimales reales) y entregan link de pago + webhook.

## La referencia e idempotencia del cobro
- La **referencia = el `id` del cobro** que creamos antes de pedir el link. Es nuestra única fuente para reconciliar: cuando vuelve el webhook, `activarCobro(db, reference)` activa exactamente ese cobro.
- El webhook busca la referencia de forma **tolerante** (`data.metadata.reference`, `data.reference`, etc.) para que el registro quede SIEMPRE automático; si llega un `SALE_APPROVED` sin referencia, se loguea para diagnóstico.
- **Idempotencia:** los webhooks reintentan, así que un mismo pago puede llegar dos veces. Hay que asegurar que **activar dos veces no cobre ni regale otro mes** — `activarCobro` solo cambia estado y `proximo_cobro`, no acumula; idealmente dedupe por estado (`pendiente`→`activo`, no reactivar lo ya activo).

## Variables de entorno que necesita
- **`BOLD_IDENTITY_KEY`** → autentica la creación del link (`Authorization: x-api-key …`). **Si falta, el link NO se genera** y `iniciarCobro` devuelve `error` — el cliente no puede pagar.
- **`BOLD_SECRET_KEY`** → verifica la firma del webhook (HMAC-SHA256). En **sandbox** la llave secreta es cadena vacía.
- `BOLD_PLAN_AMOUNT` → monto del plan en COP (opcional, default 29900).
- `NEXT_PUBLIC_APP_URL` → para el `callback_url` que devuelve al cliente al `/panel` tras pagar.

## Buenas prácticas (no romper)
1. **Verifica la firma ANTES de creer nada.** El webhook usa el **body CRUDO** (`req.text`), nunca JSON re-serializado, o el HMAC falla. Firma inválida → responde `401` y no toca la base.
2. **No actives dos veces.** Trata el webhook como idempotente; un reintento no debe dar otro mes ni doble bienvenida.
3. **El webhook no es la verdad final.** Lo ideal es confirmar también con un `GET` del pago por id antes de activar (puede llegar fuera de orden o spoofeado). *(por confirmar en Bold)*
4. **Montos en COP enteros** (29900, no 299.00) — float causa rechazos.
5. **Nunca toques datos de tarjeta crudos** — todo pasa por el hosted checkout de Bold (PCI SAQ-A).

## Frases de AVIS al cobrar (corto y claro)
- "Tu plan AVISPA'O son **$29.900 al mes**. Te paso el link y pagas con tarjeta, PSE o Nequi"
- "Aquí está tu link seguro 👉 [link]. Apenas pagues, te activo todo al instante."
- "¡Listo! Pago confirmado ✅. Tu plan quedó activo y ya empiezo a cuidarte los papeles."
- Si falla el link: "Se me trabó el cobro un segundo, dame un momento y te paso el link de nuevo." (revisar `BOLD_IDENTITY_KEY`).

## Planes y programa de referidos (DECIDIDO jun-2026 — planteado, modificable)
Escalera: **Plus 29.900** (wedge, 70 fact/mes) · **Premium 59.900** (+correo ilimitado + invitar contador) · **Negocio 99.900** = tier premium con **perfiles por área** (contador+compras+ventas) + fugas/comparativas (200 fact) · **Multi 199.900** (∞, varias sedes). **Anual = paga 10, lleva 12** (299k/599k/999k/1.999k).

**Referidos con TOPE por plan** (entre mejor plan trae el aliado, más gana → se vuelve vendedor):
- **Mensual** (comisión pagada cuando el referido cumple **3 meses activo** — ahí la contribución ya la cubrió): Plus $40k · Premium $100k · Negocio $200k · Multi $400k.
- **Anual** (pagada al **día 20** = justo tras cerrar la ventana de **reembolso de 15 días** +5 de margen → nunca hay que devolver comisión; doble incentivo a vender anual): Plus $50k · Premium $120k · Negocio $250k · Multi $500k.
- LTV/CAC 5.2–5.7x en todos los tiers (verificado). Candados: solo referidos que **pagan**, **1 negocio por NIT**, sin auto-referidos, **pago tras cerrar la ventana de reembolso** (mensual 3 meses · anual día 20), tope mensual de pagos al inicio.
- ⚠️ Proyecciones (retención 12m, servir ~$9k/mes): **validar WTP** con 5–10 dueños (Negocio) + 2–3 contadores antes de fijarlo. PDF `Planes-y-Referidos.pdf`. Detalle económico → `economist_lushows`.

> **Roadmap:** probar un **pago real** end-to-end (link → webhook → activación → bienvenida) y confirmar dónde manda Bold la `reference`; evaluar **Wompi** o **Nequi directo** como alternativa/segunda pasarela; añadir cobro **recurrente automático** (hoy `proximo_cobro` se fija pero el re-cobro mensual aún no está automatizado) y el flujo de **reintento/recordatorio** antes de que venza el mes; **implementar la lógica del programa de referidos** (tracking por NIT, conteo 3 meses / día-7, marcar comisión a pagar).
