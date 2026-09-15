# 106 — Outreach, Salesloft y Salesforce (el stack enterprise)

Este es el stack de las **empresas grandes con equipos de venta estructurados**: **Salesforce** como CRM (la fuente de verdad), y **Outreach** o **Salesloft** como plataforma de *sales engagement* (donde los SDRs y AEs ejecutan cadencias multicanal con analítica y coaching). Es potente, caro y **pensado para operación de equipo, no para un solista mandando frío**. Este módulo te dice qué hace cada pieza, en qué se diferencian de la familia de cold email a volumen (`33`, `103`, `104`), y —clave para Lushows— **cuándo justifica el costo y cuándo es sobre-ingeniería**.

## El principio: engagement enterprise, no envío masivo frío

Las plataformas de *sales engagement* (Outreach, Salesloft) nacieron para un problema distinto al de Instantly/Smartlead. No buscan "mandar 1.000 correos fríos desde dominios quemables". Buscan que **un equipo de reps toque cuentas de forma orquestada desde los buzones reales de la empresa**, con:

- **Cadencias multicanal** (email + llamada + LinkedIn + tareas) gobernadas por el proceso (ver `61`).
- **Marcador integrado** (dialer) para llamadas con grabación.
- **Conversation intelligence** (IA que transcribe y analiza llamadas para coaching).
- **Analítica profunda** de qué cadencia, qué rep y qué mensaje funcionan (ver `65`, `80`).
- **Sincronía total con el CRM** (Salesforce), que sigue siendo la verdad.

Su obsesión es la **productividad del rep y el proceso**, no la deliverability a volumen. Meterle cold email masivo a Outreach desde el dominio principal quema tu reputación *y* te sale carísimo — herramienta equivocada (ver `33`).

## Las tres piezas

| Pieza | Categoría | Qué hace | Rol |
|---|---|---|---|
| **Salesforce** | CRM | Fuente de verdad: cuentas, contactos, oportunidades, reporting | El "sistema de registro" de toda la empresa |
| **Outreach** | Sales engagement | Cadencias multicanal, dialer, conversation intelligence, deal insights | Donde el rep ejecuta y se le coachea |
| **Salesloft** | Sales engagement | Cadence, dialer, Conversations (grabación/IA), analítica | Competidor directo de Outreach, muy parejo |

Outreach y Salesloft son **casi intercambiables**; la elección suele ser por preferencia, precio negociado e integraciones existentes. Los dos se montan **encima** de Salesforce (o a veces HubSpot Enterprise, ver `105`).

## Salesforce: por qué es el estándar (y su peso)

Salesforce es el CRM dominante en enterprise porque es **infinitamente configurable**: objetos custom, reglas de validación, automatización (Flows), permisos granulares, reporting a la medida y un ecosistema (AppExchange) enorme. Esa potencia es también su costo: **requiere un admin dedicado**, la implementación es larga y cara, y para un equipo chico es como comprar un camión para ir al mercado. Para el SDR, Salesforce es donde viven las cuentas y donde escribe la disposición de cada actividad (ver `77`); Outreach/Salesloft es la **capa de ejecución** que le evita vivir dentro de la complejidad de Salesforce.

## Cuándo justifica el costo (el corazón del módulo)

Estas herramientas cobran **por asiento y por contrato anual** (miles de dólares al año, con mínimos de asientos). Se justifican **solo** cuando:

- Tienes **un equipo real** de SDRs/AEs (varias personas), no una sola.
- El **valor del cliente (LTV/ticket) es alto** y una reunión más al mes paga con creces la licencia — B2B de ticket medio-alto (ver `82`, `96`).
- Necesitas **coaching y analítica** para gestionar y hacer rampa de reps (ver `85`, `86`).
- Ya operas sobre **Salesforce** y necesitas la capa de ejecución encima.

**NO se justifica** cuando:

- Eres **solista o 1–2 personas** validando outbound → usa Apollo (`100`) o Instantly (`103`) + un CRM ligero (HubSpot, `105`).
- Tu juego es **volumen frío desde dominios secundarios** → familia cold email (`33`, `103`, `104`), no engagement enterprise.
- El ticket es bajo y una licencia enterprise se comería tu margen (calcula el punto con `economist_lushows` y `Matematicas_lushows`).

Regla brutal y honesta: **la herramienta no consigue reuniones; el sistema (lista + oferta + deliverability + cadencia) las consigue.** Un equipo con Apollo + Instantly bien montado supera a uno con Outreach mal usado. No compres enterprise para "verte serio"; cómpralo cuando el volumen de personas y el valor del deal lo pidan.

## Ejemplo: cómo se ve el stack en operación

```
Empresa B2B SaaS, 6 SDRs + 4 AEs, ticket anual $15k+:
  Salesforce   → cuentas, contactos, oportunidades, forecast (verdad)
  Outreach     → cadencias multicanal por segmento (email+call+LinkedIn)
                 dialer con grabación · conversation intelligence
                 sincroniza cada actividad a Salesforce en tiempo real
  Data:        ZoomInfo/Apollo + Clay para enriquecer (ver 29, 100, 101)
  Reporting:   Salesforce dashboards + analítica de Outreach (ver 80, 65)
El SDR vive en Outreach; el manager coachea con las grabaciones (ver 85);
Salesforce es la fuente de verdad para forecast (ver 82).
```
La conversación de venta, el discovery profundo y el cierre que ocurren en esas llamadas → `ventas_lushows`. Este stack **ejecuta y mide** el proceso; el arte de vender sigue siendo del vendedor.

## Alternativas más baratas que hacen 80% del trabajo

Antes de firmar enterprise, considera el escalón intermedio:
- **HubSpot Sales (Pro/Enterprise)** con Sequences + Workflows (ver `105`): cadencias y automatización decentes a fracción del costo.
- **Apollo** todo-en-uno para equipos chicos (ver `100`).
- **Instantly/Smartlead** para el músculo de cold email a volumen (ver `103`, `104`).

Muchas operaciones no necesitan Outreach/Salesforce hasta pasar cierto tamaño de equipo y ticket.

## Errores comunes

- **Comprar enterprise siendo pyme/solista** → miles al año en features que nadie usa.
- **Usar Outreach/Salesloft para spamear frío a volumen** desde el dominio principal → deliverability quemada + costo absurdo (herramienta equivocada, ver `33`).
- **Salesforce sin admin** → se convierte en un caos de campos y datos sucios; peor que una hoja de cálculo.
- **No calcular el punto de equilibrio** de la licencia contra reuniones extra → `Matematicas_lushows`, `economist_lushows`.

## Siguiente paso

Si eres Lushows validando outbound, **este stack no es para ti hoy**: quédate en Apollo/Instantly + HubSpot (`100`, `103`, `105`). Guarda este módulo como mapa para cuando tengas equipo y ticket alto. Para decidir la herramienta según tu etapa → `33`; para el modelo económico de la decisión → `economist_lushows`.
