# 47 — Infraestructura de WhatsApp para outbound

En LatAm, WhatsApp no es un canal secundario: **es el canal**. La gente vive ahí, responde ahí y compra ahí — reply rates muy por encima del email frío. Pero es también el canal donde más fácil te **banean el número** si lo usas mal. Este módulo explica la infraestructura: API oficial vs no oficial (Baileys y similares), cómo montar números sin quemarlos, el riesgo real de baneo, y cómo hacer outbound por WhatsApp en LatAm sin perder tu línea. Ojo con la frontera: aquí montamos la **tubería** (números, API, límites, anti-baneo); la conversación de venta por WhatsApp —qué decir, cómo manejar el "cuánto cuesta", cerrar— es oficio de vendedor → `ventas_lushows`. Cómo entra WhatsApp en la cadencia multicanal está en `48` y `61`.

## Las dos vías: API oficial vs no oficial

Hay dos formas de mandar WhatsApp programáticamente, y elegir mal te cuesta el número o la cuenta.

| | **API oficial (WhatsApp Cloud API / Business Platform, de Meta)** | **No oficial (Baileys, whatsapp-web.js, etc.)** |
|---|---|---|
| Qué es | La API que Meta ofrece oficialmente para empresas | Librerías que simulan WhatsApp Web / un teléfono |
| Legalidad ToS | Permitida, es el camino oficial | **Viola los Términos de Servicio** de WhatsApp |
| Riesgo de baneo | Bajo si respetas las reglas | **Alto** — Meta detecta y banea |
| Iniciar conversación en frío | Solo con **plantillas aprobadas** (message templates) | Texto libre, cualquier cosa |
| Costo | Por conversación (~$0.01–0.08 según país/tipo) | "Gratis" (pero riesgo altísimo) |
| Número | Un número dedicado registrado en Meta/BSP | Cualquier chip / número |
| Escala | Alta, estable | Frágil, no escala sin quemar números |

**Regla honesta:** para un negocio que quiere durar, la **API oficial** es el camino. La no oficial (Baileys) sirve para prototipos, volumen bajo, o pruebas — es lo que usa el propio bot de GastroLatam en local (ver el `whatsapp.js` del proyecto) — pero **no la construyas como tu máquina de outbound en frío a escala**: te banean el número y pierdes los chats. Si igual la usas, trátala como desechable (números que puedes perder).

## El punto crítico: WhatsApp NO es email

El error que quema números es tratar WhatsApp como correo masivo. WhatsApp es **mucho más celoso** con el outbound frío porque su valor es que la gente confía en que ahí solo le escribe conocidos. Diferencias clave:

1. **En frío, con API oficial, solo puedes iniciar con plantillas aprobadas.** No puedes mandar texto libre a alguien que no te escribió primero. Envías una **message template** que Meta revisó y aprobó (utility o marketing). Texto libre solo dentro de la ventana de 24h después de que ELLOS respondan.
2. **La señal de baneo nº1 es que la gente te bloquee o reporte.** Si mandas a gente que no te conoce y te bloquean/reportan, Meta baja tu **quality rating** y te limita o banea. Igual que el spam complaint del email (ver `40`), pero más rápido y menos perdonador.
3. **El consentimiento importa (y es ley en LatAm).** Habeas Data / Ley 1581 en Colombia exige base legal para tratar el dato y contactar (ver `49`). WhatsApp en frío puro a números comprados es la zona más gris/riesgosa — hazlo solo con leads que mostraron algún interés o tienen relación con tu negocio.

## Cómo montar la infraestructura oficial

Para hacerlo bien con la API oficial (WhatsApp Cloud API):

1. **Meta Business Manager + WhatsApp Business Platform.** Registras un número dedicado (no tu personal). Se hace directo con Meta o vía un **BSP** (Business Solution Provider — un socio que te da la API más fácil: Twilio, 360dialog, Gupshup, Wati, Zenvia, o plataformas como ManyChat/Callbell para no-técnicos).
2. **Verifica el negocio** (business verification) — sube documentos de la empresa. Sube tu límite de mensajes.
3. **Crea y aprueba plantillas** (templates) para el primer toque en frío. Meta las revisa (horas a 1 día). Categorías: *utility* (transaccional) o *marketing* (promocional — más restringida, requiere opt-in claro).
4. **Warmup del número (sí, también aplica):** número nuevo empieza en tier bajo (1.000 conversaciones/día iniciadas) y sube a 10k/100k/ilimitado según calidad y volumen. No dispares el máximo el día uno.
5. **Vigila el quality rating** (verde/amarillo/rojo en el panel de Meta) — es tu "reputación" de WhatsApp. Rojo = te van a limitar/banear. Baja el ritmo y mejora la relevancia.

## Números: cuántos y cómo protegerlos

| Práctica | Recomendación |
|---|---|
| Número | Dedicado, registrado en Meta. NUNCA tu personal para outbound |
| Warmup | Número nuevo: empieza bajo, sube gradual (como email; ver `43`) |
| Volumen inicial | Decenas/día, no miles. Sube con quality rating verde |
| Señal de opt-in | Ten cómo probar que el contacto aceptó/tiene relación (ver `49`) |
| Opt-out | SIEMPRE ofrece salida fácil ("responde STOP para no recibir más") |
| Si usas no-oficial | Números desechables, volumen bajísimo, asume que los perderás |

## Outbound por WhatsApp en LatAm: la realidad

- **Reply rates altísimos** vs email (la gente abre WhatsApp casi siempre) — por eso vale la pena montarlo bien.
- **Lo mejor: WhatsApp como segundo o tercer toque**, no como primer contacto en frío puro. Ejemplo: correo → LinkedIn → y si mostró algo de interés, WhatsApp. O Click-to-WhatsApp desde un anuncio (ahí el prospecto inicia, y ya no es frío — no necesitas plantilla y no hay riesgo de baneo). El Click-to-WhatsApp por pauta es terreno de las skills de ads (`facebook_ads_lushows`, `tiktok_ads_lushows`).
- **Integración con tu operación:** el proyecto GastroLatam ya corre sobre Cloud API — misma lógica: webhook, plantillas, ventana de 24h.

## Errores comunes (qué NO hacer)

- Usar tu número personal para outbound masivo. Lo pierdes y pierdes tus chats.
- Comprar una base de números y dispararles WhatsApp en frío con Baileys. Baneo casi seguro + ilegal sin base legal (ver `49`).
- Iniciar en frío con texto libre por la API oficial: no se puede, necesitas plantilla aprobada.
- Ignorar el quality rating hasta que se pone rojo.
- Tratar WhatsApp como email (mismo volumen, misma frialdad). Es más celoso: menos volumen, más relevancia, más consentimiento.

## Siguiente paso

WhatsApp es un canal de tu cadencia, no una isla: ve a `48` para combinarlo con email, LinkedIn y teléfono sin quemar ninguna cuenta (límites por canal), y a `61` para el diseño de la secuencia multicanal. Para el cumplimiento legal del outbound por WhatsApp en Colombia (Habeas Data, opt-in, opt-out) ver `49`. Para *qué decir* en el chat y cerrar → `ventas_lushows`. Para Click-to-WhatsApp pagado → skills de ads.
