# 116 — Spam testing e inbox placement

Puedes estar limpio de blacklists (ver `114`), autenticado al 100% (ver `111`) y con reputación "Media" en Postmaster, y **aun así caer en la carpeta de spam o en Promociones**. Estar entregado no es lo mismo que estar en la bandeja principal. **Inbox placement** = dónde cae de verdad tu correo: Primary/Principal, Promociones, Spam, o el vacío. Este módulo es cómo lo **auditas con evidencia** en vez de suponer: spam testing con herramientas de puntuación y **seed lists** (listas semilla — buzones de prueba tuyos en cada proveedor a los que te envías para ver dónde aterrizas). Es la diferencia entre "creo que llego" y "sé que el 82% de mis correos cae en Primary de Gmail y el 40% en spam de Outlook, y voy a arreglar Outlook". Sin esto, optimizas a ciegas.

## Los dos tipos de prueba: puntuación vs placement

Son cosas distintas y necesitas ambas:

| Tipo | Qué mide | Herramienta típica | Limitación |
|---|---|---|---|
| **Spam score** | Qué tan "spam" se ve tu correo (contenido, autenticación, config) | Mail-Tester, SpamAssassin | No te dice DÓNDE cae, solo qué tan riesgoso se ve |
| **Inbox placement** | En qué carpeta cae de verdad, por proveedor | GlockApps, seed lists | Es lo que importa de verdad, pero requiere más setup |

Un correo puede sacar 10/10 en Mail-Tester y aun así caer en Promociones de Gmail o spam de Outlook — porque la puntuación evalúa el mensaje, no la reputación real de tu dominio frente a cada proveedor. Por eso el placement manda.

## Herramientas de spam score (rápidas, para el mensaje)

| Herramienta | Qué hace | Precio |
|---|---|---|
| **Mail-Tester** (mail-tester.com) | Te da un correo, le escribes, te da /10 con todo lo que falla (SPF/DKIM/DMARC, contenido, blacklists) | Gratis (3/día) o barato |
| **SpamAssassin score** | El motor que muchos servidores usan; muchas herramientas lo reportan | Incluido en varias |
| **MxToolbox Deliverability** | Chequeo de autenticación + blacklist + config | Gratis / pago |

Úsalas para **validar el mensaje antes de lanzar**: apunta a 9–10/10 en Mail-Tester. Pero recuerda: es condición necesaria, no suficiente.

## Inbox placement con seed lists (lo que de verdad importa)

Una **seed list** es un conjunto de buzones de prueba repartidos entre proveedores (Gmail, Outlook, Yahoo, Workspace, 365, gateways). Le mandas tu campaña a esa lista y ves **exactamente en qué carpeta cayó en cada proveedor**. Dos formas:

**A. Herramienta dedicada (recomendado a escala):**

| Herramienta | Qué hace | Precio aprox. |
|---|---|---|
| **GlockApps** | Seed list amplia (Gmail, Outlook, Yahoo, corporativos), reporta placement por proveedor + spam score + blacklist + DMARC | desde ~$59/mes |
| **MailReach** | Test de placement + warmup + monitoreo | desde ~$25/mes |
| **Inbox Insight / Emailable / EmailGuard** | Placement testing, algunas integradas a plataformas de envío | varía |
| **Instantly/Smartlead (integrado)** | Algunas traen "spam test / placement" nativo con su propia seed list | incluido en el plan |

GlockApps es el estándar del rubro: mandas el correo a su lista semilla y en minutos ves "Gmail: Inbox 80% / Spam 15% / Promotions 5%; Outlook: Inbox 45% / Spam 55%" — con el detalle de por qué.

**B. Seed list propia (barato, casero):** crea tus propios buzones de prueba en Gmail, Outlook, Yahoo, un Workspace y un 365 tuyos. Mándate la campaña e inspecciona a mano dónde cayó. Menos escalable pero gratis y real. Útil para probar Outlook, que no da tablero (ver `115`).

## Cómo leer un test de placement

```
EJEMPLO de reporte GlockApps:
  Gmail:            Inbox 84%  | Promotions 10% | Spam 6%     ✅ sano
  Google Workspace: Inbox 78%  | Spam 22%                     ⚠️ revisar
  Outlook/Hotmail:  Inbox 41%  | Spam 59%                     🔴 problema Outlook
  Office 365:       Inbox 55%  | Spam 45%                     🔴 problema Microsoft
  Yahoo:            Inbox 90%                                 ✅
  Autenticación:    SPF ✅ DKIM ✅ DMARC ✅
  Spam score:       9.2/10
  Blacklist:        limpio
```

Diagnóstico del ejemplo: autenticación y contenido bien, Gmail sano, pero **Microsoft te manda a spam**. Eso apunta a: rampa muy rápida para Outlook, links/contenido que Microsoft castiga, o reputación de dominio joven frente a Defender (ver `115`). Acción: bajar volumen hacia Outlook, quitar links acortados, texto más plano, más warmup.

## Cuándo y con qué frecuencia testear

| Momento | Prueba |
|---|---|
| Antes de lanzar una campaña nueva | Mail-Tester al mensaje (9–10/10) |
| Antes de cargar volumen en buzones recién calentados | Placement test (seed list) por buzón/dominio |
| Semanal, en producción | Placement test a una muestra de la flota (ver rutina en `113`) |
| Al cambiar copy, dominio o subir volumen | Re-testear placement (el cambio pudo moverte a spam) |
| Cuando el reply rate cae sin causa clara | Placement test ANTES de reescribir copy (¿estás en spam?) |

**Regla de oro del diagnóstico:** cuando las respuestas bajan, el placement test responde la primera pregunta —"¿estoy llegando a la bandeja?"— antes de tocar el copy. Si caes en spam, ningún copy te salva; si llegas bien y no responden, ahí sí es lista o copy (ver `83`).

## Errores comunes (qué NO hacer)

- Confiar solo en Mail-Tester 10/10 y asumir que llegas a Primary. Mide el mensaje, no el placement real.
- No testear Outlook por separado: es donde más caes y donde no hay tablero (ver `115`).
- Reescribir copy cuando el problema es placement (estás en spam). Testea placement primero.
- Testear una vez y nunca más: el placement cambia con reputación, volumen y contenido.
- Usar los mismos buzones semilla que ya "conocen" tu correo como si fueran neutrales (se acostumbran). Las herramientas serias rotan su seed pool.
- Optimizar por open rate como proxy de placement: el tracking de aperturas es poco fiable y hasta daña deliverability (pixel; ver `45`).

## Siguiente paso

Con el placement auditado sabes exactamente qué proveedor te falla y por qué. Si un dominio sale mayormente en spam pese a arreglar contenido y rampa, ya está quemado: ve a `117` (recuperar o jubilar un dominio quemado). Para las diferencias por proveedor que explican un mal placement en Outlook, `115`. Para blacklists, `114`. Para leer la reputación de Gmail, `113`. Para diagnosticar si es lista/copy una vez confirmado que llegas, `83`.
