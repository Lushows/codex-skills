# 40 — Fundamentos de deliverability

Este es el módulo raíz del Bloque 4. **Deliverability** = que tus correos lleguen a la bandeja de entrada (Primary/Principal) y no a spam, a Promociones o al vacío. Importa porque es invisible hasta que te hunde: puedes tener el ICP perfecto (ver `10`) y el mejor copy del mundo (ver `52`), pero si el 40% de tus correos cae en spam, ese 40% de tu esfuerzo, tu lista y tu dinero simplemente no existe. Nadie los lee, nadie responde, y tú creerás que "el outbound no funciona" cuando el problema es la fontanería. Los proveedores (Gmail/Google Workspace y Outlook/Microsoft 365 concentran el 90%+ del B2B) deciden dónde cae cada correo con una mezcla de señales. Este módulo explica esas señales; los módulos `41`–`49` son el cómo de cada una.

## La mecánica: por qué un correo cae en spam

El proveedor de tu destinatario (Google, Microsoft) recibe tu correo y en milisegundos decide: Principal, Promociones, Spam o rechazo. Esa decisión se basa en **cuatro pilares**. Si fallas uno, empiezas a caer; si fallas dos, estás muerto.

| Pilar | Qué evalúa | Dónde se arregla |
|---|---|---|
| **Autenticación** | ¿Eres quien dices ser? ¿El dominio autorizó este envío? | SPF/DKIM/DMARC → `42` |
| **Reputación** | ¿Este dominio/IP suele mandar cosas buenas o basura? | Warmup `43`, dominios `41`, monitoreo `46` |
| **Contenido** | ¿El correo parece spam? (palabras, links, imágenes, HTML) | `45` |
| **Engagement** | ¿La gente abre, responde, o te marca como spam y borra? | Todo el sistema: lista `20`, copy `52` |

### 1. Autenticación — la cédula de tu dominio
Antes de mirar nada más, el proveedor verifica que el correo venga de verdad de tu dominio y que tu dominio lo haya autorizado. Son tres registros DNS (SPF, DKIM, DMARC; ver `42`). **Sin ellos, Gmail y Outlook mandan tu correo directo a spam o lo rechazan** — desde febrero de 2024 es obligatorio para cualquiera que envíe en volumen. Es el requisito de entrada, no un extra. Es lo primero que configuras y lo primero que revisas cuando algo falla.

### 2. Reputación — tu historial como remitente
Cada dominio (y cada IP de envío) acumula una **reputación**: un puntaje invisible que dice "este remitente suele mandar correos que la gente quiere / que la gente marca como spam". Se construye con el tiempo y con el comportamiento. Un dominio nuevo tiene reputación **neutra-baja** (por eso se calienta; ver `43`). Un dominio que mandó 500 fríos el día uno tiene reputación **destruida**. La reputación es la razón nº1 por la que **nunca envías outbound desde tu dominio principal** (ver `41`): si lo quemas, dejas de recibir hasta los correos de tus clientes reales.

### 3. Contenido — qué tan "spam" se ve el correo
Los filtros leen el correo: palabras gatillo ("gratis", "garantizado", "gana dinero"), exceso de links, imágenes pesadas, HTML recargado, un solo bloque gigante de texto. Un correo de texto plano, corto, con un solo link y cero palabras spam se ve como un correo humano real (ver `45`).

### 4. Engagement — la señal que más pesa hoy
Es la más importante y la que no puedes falsificar a largo plazo. Los proveedores miden **cómo reacciona la gente**: si abren, si responden (la señal más fuerte), si te archivan sin abrir, o —lo peor— si te marcan como spam. Un **spam complaint rate** (% que te marca como spam) arriba de **0.3%** te hunde la reputación rápido; Google recomienda mantenerlo bajo 0.1%. Por eso la lista bien segmentada (ver `20`, `21`) y el copy relevante (ver `52`) no son solo "buenas prácticas de venta": son **deliverability**. Mandar a gente que no encaja genera quejas y borra tu reputación. **La mejor táctica de deliverability es un buen ICP.**

## El ciclo virtuoso (y el vicioso)

```
VIRTUOSO:  lista buena → copy relevante → responden → reputación sube → llegas a Primary → más respuestas
VICIOSO:   lista mala  → copy genérico  → te marcan spam → reputación baja → caes a spam → nadie responde → "el outbound no sirve"
```

Todo en el Bloque 4 existe para mantenerte en el ciclo virtuoso. No es opcional ni "avanzado": es la condición para que exista todo lo demás.

## El plan de deliverability, de una vez

Este es el orden de montaje para no quemarte (cada paso tiene su módulo):

1. **No uses tu dominio principal.** Compra dominios secundarios de envío (ver `41`).
2. **Autentícalos:** SPF + DKIM + DMARC en cada uno (ver `42`).
3. **Caliéntalos** 2–4 semanas con warmup automático antes de mandar un solo correo real (ver `43`).
4. **Respeta límites:** ~30–50 correos por buzón/día, y rota entre varios buzones (ver `44`).
5. **Cuida el contenido:** texto plano, corto, sin palabras spam (ver `45`).
6. **Monitorea:** bounce rate, spam rate, blacklists, Google Postmaster (ver `46`).
7. **Manda a gente que de verdad encaja** (ICP `10`, lista `20`) — la deliverability empieza en la lista.

## Números que debes vigilar (2026)

| Métrica | Sano | Alerta | Fuente/módulo |
|---|---|---|---|
| Bounce rate (rebotes) | < 2% | > 4% detén todo | `44`, `46` |
| Spam complaint rate | < 0.1% | > 0.3% peligro | `46` |
| Reply rate (respuestas) | 3–8% frío bien hecho | < 1% revisa lista/copy | `80`, `83` |
| Correos por buzón/día | 30–50 | > 50 quemas | `44` |

## Errores comunes (qué NO hacer)

- Creer que la deliverability es "cosa de técnicos" y saltártela. Es el 50% de tu resultado.
- Mandar desde tu dominio principal "solo para probar". Un lote de 50 fríos puede marcarlo para siempre.
- Culpar al copy cuando el problema es que estás en spam. Antes de reescribir, verifica que llegas (ver `46`, prueba de inbox placement).
- Comprar listas y mandarles en frío: bounces altos + quejas = reputación destruida en un día (ver `49`).

## Siguiente paso

Empieza por `41` (dominios secundarios): la primera decisión física es *desde dónde* vas a enviar sin arriesgar tu dominio real. Para el diagnóstico "¿mi problema es lista, copy o deliverability?" ver `83`. Para deliverability avanzada (segmentación de reputación, sub-dominios, estrategias a gran volumen) ver `110`–`119`.
