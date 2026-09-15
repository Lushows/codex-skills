# 119 — Deliverability en WhatsApp y SMS

El Bloque 11 fue "no quemar dominios de correo". Este módulo traslada la misma disciplina a los canales de mensajería que dominan LatAm: **WhatsApp y SMS**, donde lo que se quema no es un dominio sino un **número de teléfono** — y perder un número duele más (te llevas los chats, el histórico y a veces el WhatsApp Business entero). El módulo `47` cubrió la infraestructura (API oficial vs Baileys, cómo montar números). Aquí el foco es la **"deliverability" de mensajería**: cómo calientas números, qué límites respetas, cómo lees tu reputación (quality rating), y cómo evitas el baneo. Ojo con la frontera: montamos la **tubería y la salud del canal**; qué decir en el chat, manejar el "¿cuánto cuesta?" y cerrar es oficio de vendedor → `ventas_lushows`.

## Por qué WhatsApp es MÁS celoso que el email

En email, caer en spam es "el correo no se ve"; en WhatsApp, usar mal el canal es "Meta te banea el número y lo pierdes". Es menos perdonador porque **el valor de WhatsApp es que la gente confía en que ahí solo le escribe conocidos** (ver `47`). La señal de muerte nº1 es que **te bloqueen o reporten**: equivale al spam complaint del email (ver `40`), pero actúa más rápido y más duro. Por eso el outbound frío puro por WhatsApp es la zona más riesgosa de todo el outbound.

## Warmup de un número de WhatsApp (sí, existe)

Un número nuevo en WhatsApp Business API arranca en **tier bajo** y sube por calidad y volumen — igual que un buzón de correo se calienta (ver `43`, `112`). Los tiers de la Cloud API (conversaciones **iniciadas por ti** en 24h):

| Tier | Conversaciones iniciadas/día | Cómo subes |
|---|---|---|
| Sin verificar | 250 | Verifica el negocio en Meta |
| Tier 1 | 1.000 | Buen quality rating + volumen sostenido |
| Tier 2 | 10.000 | Sigue con calidad verde |
| Tier 3 | 100.000 | Igual |
| Tier 4 | Ilimitado | Igual |

**Rampa de warmup del número (aunque el tier permita más):**

```
Semana 1:  10-20 conversaciones/día iniciadas, a gente que probablemente responda bien
Semana 2:  30-50/día, vigilando quality rating verde
Semana 3:  80-150/día
Semana 4+: sube gradual mientras el rating siga verde; NUNCA dispares el máximo del tier el día 1
```

La clave del warmup de WhatsApp: **empieza mandando a leads tibios/calientes** (gente que ya mostró interés, clientes, opt-ins), no a fríos puros. Respuestas positivas tempranas construyen quality rating; bloqueos tempranos lo destruyen.

## Quality rating: tu "reputación" de WhatsApp

Meta te asigna un **quality rating** por número, visible en el panel (WhatsApp Manager / tu BSP):

| Color | Significa | Acción |
|---|---|---|
| **Verde (High)** | Buena calidad, pocos bloqueos/reportes | Puedes subir volumen |
| **Amarillo (Medium)** | Advertencia; los usuarios se están quejando | Baja el ritmo, mejora relevancia YA |
| **Rojo (Low)** | Crítico; Meta va a limitar o banear | Detén outbound, revisa todo |

Si el rating cae a rojo, Meta baja tu tier o suspende el número. Se recupera con días de buen comportamiento (mensajes relevantes, cero reportes) — pero como en email, **prevenir es infinitamente más barato que recuperar** (ver `117` para la lógica análoga en dominios).

## Las reglas que no se rompen (API oficial)

1. **En frío solo con plantillas aprobadas** (message templates que Meta revisó). No puedes mandar texto libre a alguien que no te escribió primero (ver `47`). Texto libre solo dentro de la ventana de 24h tras su respuesta.
2. **Categoría correcta:** *utility* (transaccional, más permitida) vs *marketing* (promocional, más restringida y requiere opt-in claro). Una plantilla de marketing disfrazada de utility te baja el rating.
3. **Opt-in demostrable + opt-out fácil.** Ten cómo probar que el contacto aceptó o tiene relación contigo, y ofrece salida siempre ("responde SALIR para no recibir más"). En Colombia esto es **ley** (Habeas Data / Ley 1581; ver `49`).
4. **Relevancia brutal.** Menos volumen, más pertinencia. Un mensaje irrelevante a WhatsApp genera bloqueo mucho más rápido que un email irrelevante.

## SMS: reglas propias

SMS tiene su propia deliverability, más regulada por operadores que por una sola plataforma:

- **A2P 10DLC / números registrados:** en muchos mercados el envío empresarial (Application-to-Person) exige registrar el número/campaña con el operador (vía Twilio, Zenvia, Infobip). Sin registro, los operadores filtran o bloquean.
- **Opt-in obligatorio y opt-out (STOP)** por ley y por reglas de operador. Sin STOP funcional, te bloquean.
- **Números:** short codes, long codes o toll-free según país. Mezclar mal el tipo de número con el volumen te filtra.
- **Costo por mensaje** (a diferencia del email), así que el volumen basura además de quemar, cuesta.
- **Reputación por número/operador:** alto % de fallos o quejas degrada la entrega, igual que en email.

SMS en LatAm suele ser secundario frente a WhatsApp (menor engagement, más costo), útil para recordatorios/confirmaciones más que para prospección fría.

## Cómo NO quemar números en LatAm (el resumen operativo)

| Práctica | Regla |
|---|---|
| Número | Dedicado, registrado (WhatsApp API / A2P). NUNCA tu personal para outbound |
| Warmup | Rampa como en email: empieza bajo, sube con rating verde |
| Primer toque | **WhatsApp como 2º/3er toque**, no frío puro. Ideal: Click-to-WhatsApp (el prospecto inicia → no es frío, sin riesgo de plantilla ni baneo; eso es terreno de `facebook_ads_lushows`/`tiktok_ads_lushows`) |
| Volumen | Decenas→cientos/día subiendo, no miles el día 1 |
| Opt-in / opt-out | Demostrable + salida fácil siempre (ley; ver `49`) |
| Monitoreo | Quality rating verde (revisar a diario); tasa de bloqueo/reporte |
| Si usas no-oficial (Baileys) | Números desechables, volumen bajísimo, asume que los perderás (ver `47`) |

## Errores comunes (qué NO hacer)

- Comprar una base de números y dispararles WhatsApp frío con Baileys: baneo casi seguro + ilegal sin base legal (ver `49`).
- Usar tu número personal para outbound: lo pierdes y pierdes tus chats.
- Iniciar en frío con texto libre por la API oficial: no se puede, necesitas plantilla aprobada.
- Disparar el máximo del tier el día 1 sin warmup: rating a rojo, número limitado.
- Ignorar el quality rating hasta que se pone rojo.
- SMS sin registro A2P ni opt-out: filtrado por operador y sancionable.
- Tratar WhatsApp como email masivo: es más celoso — menos volumen, más relevancia, más consentimiento.

## Siguiente paso

Con la salud del canal cubierta, integra WhatsApp/SMS en la cadencia sin quemar cuentas: ve a `48` (infraestructura multicanal, límites por canal) y `61` (diseño de la secuencia multicanal). Para el cumplimiento legal en Colombia (Habeas Data, opt-in/opt-out), `49`. Para la infraestructura base de WhatsApp (API oficial vs Baileys, BSP), `47`. Para *qué decir* en el chat y cerrar la conversación → `ventas_lushows`. Para Click-to-WhatsApp pagado → las skills de ads. Con esto cierra el Bloque 11.
