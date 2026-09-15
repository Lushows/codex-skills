# 113 — Google Postmaster y monitoreo de reputación real

El módulo `46` te dio la rutina de monitoreo básica. Este es el nivel avanzado: **cómo lees la reputación REAL que los proveedores te asignan** —no la que "sientes" ni la que estima tu plataforma de envío, sino el dato de la fuente—, dominio por dominio y a escala de flota. La herramienta central es **Google Postmaster Tools** porque Gmail/Google Workspace es la mayoría del B2B (ver `40`), y su equivalente en Microsoft para lo demás. La diferencia entre un operador amateur y uno serio es esta: el amateur mira reply rate y adivina; el profesional abre Postmaster, ve "Domain Reputation: Baja" con tres semanas de anticipación, y frena antes de quemar la flota. Sin este dato, escalar a multi-dominio (ver `110`) es volar a ciegas.

## Google Postmaster Tools: tu tablero de verdad en Gmail

Gratis, en postmaster.google.com. Para usarlo debes **verificar cada dominio de envío** (agregar un registro TXT en DNS, igual que en `42`). A escala, verifica **todos** los dominios de la flota — cada uno tiene su propia reputación y debes verlos por separado. Requiere cierto volumen a Gmail (~algunas decenas/día por dominio) para mostrar datos, así que empieza a mirarlo unas 2 semanas después de que el dominio entre a producción.

Los paneles y cómo leerlos:

| Panel | Qué te dice | Umbral sano | Si está mal |
|---|---|---|---|
| **Domain Reputation** | Alta / Media / Baja / Mala. Tu termómetro nº1 | Alta o Media | Baja/Mala = estás cayendo a spam. Frena volumen ya |
| **IP Reputation** | Reputación de las IPs que envían por ti | Alta | Relevante si usas IP dedicada; en Workspace es compartida |
| **Spam Rate** | % de usuarios Gmail que te marcaron spam | < 0.10% | > 0.30% crítico. Baja volumen, revisa lista+copy |
| **Authentication** | % de correos que pasan SPF, DKIM, DMARC | ~99–100% | < 100% → revisa autenticación (`42`, `111`) |
| **Delivery Errors** | Por qué Gmail rechazó/difirió correos | ~0% | Picos = volumen alto, contenido, o reputación |
| **Encryption (TLS)** | % de correo cifrado en tránsito | ~100% | Bajo = raro; revisa config del proveedor |

**El Spam Rate de Postmaster es el dato más honesto que tienes.** Es el % real de gente de Gmail que te marcó spam — la señal que más destruye reputación (ver `40`). Google recomienda mantenerlo bajo 0.1%; por encima de 0.3% te limita. Si lo ves subir, es lista mala o copy irrelevante: para y diagnostica antes de mandar un correo más.

## Microsoft / Outlook: el punto ciego

Microsoft **no tiene un Postmaster tan rico como Google**. Lo que hay:

- **SNDS** (Smart Network Data Services): datos por IP, útil solo si tienes IP dedicada (no en 365 compartido).
- **JMRP** (Junk Mail Reporting Program): te reenvía las quejas de spam de usuarios Outlook/Hotmail — regístrate si mandas volumen a dominios @outlook/@hotmail/@live.
- En la práctica, para Outlook te guías más por **bounce rate, códigos de rechazo** (busca `S3150`, `550 5.7.1`, referencias a spam) y **spam testing con seed lists** que incluyan Outlook (ver `116`).

Outlook es más severo y opaco que Gmail: si tu lista es muy pesada en dominios corporativos con Microsoft 365, monitorea sobre todo por códigos de rechazo y seed testing, no esperes un tablero.

## Monitoreo a escala: por buzón y por dominio, no el promedio

El error mortal a escala es mirar solo el **promedio global** de la plataforma (Instantly/Smartlead). Un buzón podrido se esconde en el promedio y contamina a sus vecinos de dominio. La disciplina:

- **Vigila por dominio** en Postmaster (uno verificado por dominio).
- **Vigila por buzón** en tu plataforma: bounce rate, health score, respuestas.
- **Segmenta la caída:** cuando algo baja, identifica *qué dominio/buzón* lo causa y aíslalo (pausa/jubila) antes de que arrastre a la flota.

Herramientas que centralizan el monitoreo de flota (además de Postmaster): las propias plataformas de envío traen tableros, y hay especializadas — **GlockApps** (inbox placement + reputación; ver `116`), **MailReach**, **Google Postmaster** vía agregadores como **EmailGuard** o el panel de tu revendedor de infraestructura.

## Rutina de monitoreo avanzada (calendario)

```
DIARIO (plataforma de envío):
  [ ] Bounce rate de campañas activas < 2% (sube → pausa esa campaña)
  [ ] Ningún buzón "desconectado" o auto-pausado por la plataforma
  [ ] Health/warmup score de cada buzón sigue verde (ver 112)

SEMANAL (Postmaster + herramientas):
  [ ] Google Postmaster por dominio: Domain Reputation Alta/Media, Spam Rate < 0.1%
  [ ] Authentication ~100% en todos los dominios
  [ ] Blacklist check de dominios e IPs (MXToolbox; ver 114)
  [ ] Inbox placement test con seed list (GlockApps/mail-tester; ver 116)
  [ ] Reply rate por campaña vs semana anterior (¿cayó? diagnostica: 83)

MENSUAL:
  [ ] Auditar SPF/DKIM/DMARC de toda la flota intactos (ver 111)
  [ ] Jubilar buzones/dominios degradados; activar los del colchón (ver 112)
  [ ] Revisar tendencia de Domain Reputation de cada dominio (¿alguno bajando?)
```

## El árbol de decisión cuando la reputación cae

Si Postmaster marca reputación a la baja, actúa en orden (deliverability primero; si estás en spam nada más importa):

1. **¿Authentication < 100%?** → arregla SPF/DKIM/DMARC (ver `42`, `111`) antes que nada.
2. **¿Spam Rate subiendo?** → lista/copy irrelevante. Baja volumen, aprieta ICP (ver `10`), revisa copy (ver `45`).
3. **¿Bounce alto?** → lista sucia. Limpia (ver `28`) y detén hasta arreglar.
4. **¿En blacklist?** → ve a `114` (diagnóstico y delisting).
5. **¿Reputación Baja/Mala sostenida pese a todo?** → dominio quemándose. Ve a `117` (descansar/reconstruir/jubilar).
6. **¿Todo verde pero reply rate bajo?** → *ahora sí* es lista o copy fino (ver `83`), no deliverability.

## Errores comunes (qué NO hacer)

- No verificar los dominios en Postmaster: vuelas ciego sobre la mayoría de tu audiencia B2B.
- Mirar solo el promedio de la plataforma y no Postmaster por dominio: el buzón podrido se esconde.
- Esperar a "sentir" que las respuestas se secaron. Para entonces llevas semanas en spam.
- Tratar Outlook como Gmail: no hay tablero equivalente; guíate por bounces/códigos/seed tests.
- Reaccionar reescribiendo copy cuando Postmaster grita Spam Rate alto o Authentication rota. Arregla la fontanería primero.

## Siguiente paso

Con la reputación real a la vista, cuando detectes una caída fuerte revisa listas negras: `114` (detectar en MXToolbox y salir de Spamhaus). Para auditar dónde caen tus correos (inbox vs Promociones vs spam) con seed lists, `116`. Para recuperar un dominio ya quemado, `117`. La rutina básica de monitoreo está en `46`. Para números exactos de tasas, `Matematicas_lushows`.
