# 46 — Monitoreo de reputación

El outbound sin monitoreo es manejar de noche con los ojos cerrados: cuando "sientes" que algo va mal (las respuestas se secaron), ya llevas semanas en spam quemando lista y buzones. Este módulo cierra el Bloque 4: **cómo vigilar la salud de tu envío en tiempo real** —bounce rate, spam complaint rate, blacklists y Google Postmaster Tools— para detectar problemas *antes* de que te hundan y saber exactamente qué apagar. Monitorear es lo que convierte la deliverability de "espero que llegue" a un sistema con tablero (el principio de todo el outbound; ver `00`). Sin esto, no sabes si tu problema es lista, copy o deliverability (diagnóstico en `83`).

## Las métricas que importan y sus umbrales

Cuatro números deciden la salud de tu envío. Míralos **por buzón y por dominio**, no solo el promedio global (un buzón podrido arrastra al resto):

| Métrica | Qué es | Sano | Alarma → acción |
|---|---|---|---|
| **Bounce rate** | % de correos que rebotan (dirección inválida/servidor los rechaza) | < 2% | > 4% → **detén todo**, limpia la lista |
| **Spam complaint rate** | % de destinatarios que te marcan "spam" | < 0.1% | > 0.3% → baja volumen, revisa lista+copy |
| **Reply rate** | % que responde (proxy de que llegas y eres relevante) | 3–8% | < 1% → puede que estés en spam, no solo mal copy |
| **Open rate** (si trackeas) | % que abre — úsalo con cuidado (ver `45`) | 40–60% | caída brusca → problema de deliverability |

**El bounce rate es la alarma nº1.** Un bounce alto = lista sucia = los proveedores lo ven como "este remitente no sabe a quién le escribe" = reputación destruida rapidísimo. Por eso se limpia la lista **antes** de enviar (NeverBounce/ZeroBounce/MillionVerifier; ver `44` y `23`), y se vigila el bounce en cada campaña.

### Hard bounce vs soft bounce
- **Hard bounce:** la dirección no existe / dominio inválido. Permanente. Estos matan reputación — quítalos de la lista de inmediato.
- **Soft bounce:** temporal (buzón lleno, servidor caído). Reintentable, menos grave. Pero si un contacto rebota suave varias veces, sácalo.

## Blacklists: qué son y cómo revisarlas

Una **blacklist** (lista negra / DNSBL) es una lista pública de dominios e IPs señalados por enviar spam. Si tu dominio o la IP de tu servidor de envío caen en una, los proveedores que consultan esa lista bloquean o degradan tus correos. Las principales: **Spamhaus** (la más importante), Barracuda, SpamCop, SORBS.

**Cómo revisar (gratis):**
- **MXToolbox Blacklist Check** (mxtoolbox.com/blacklists.aspx): metes tu dominio o IP y te dice si estás en alguna de ~80 listas.
- **Spamhaus** (check.spamhaus.org): consulta directa a la más crítica.

**Si caes en una blacklist:** casi todas tienen un formulario de **delisting** (remoción) — pausas el envío, arreglas la causa (lista sucia, volumen alto, buzón comprometido) y solicitas la remoción. Spamhaus suele quitar solo en días si dejas de enviar mal. Pero prevenir > curar: respeta límites (ver `44`) y limpia listas (ver `23`) y rara vez caerás.

## Google Postmaster Tools: tu tablero de reputación en Gmail

Como Gmail/Google Workspace es la mayoría del B2B, **Google Postmaster Tools** (gratis, postmaster.google.com) es tu instrumento más valioso: te muestra cómo ve Google tu dominio. Para usarlo debes **verificar tu dominio** ahí (agregar un registro TXT, igual que en `42`) — hazlo con cada dominio de envío.

Lo que te muestra:

| Panel | Qué te dice |
|---|---|
| **Domain Reputation** | Alta / Media / Baja / Mala. Tu termómetro principal. Baja o mala = estás cayendo a spam |
| **Spam Rate** | % que te marcó spam en Gmail. **Mantenlo bajo 0.1%**; arriba de 0.3% es crítico |
| **Authentication** | % de correos que pasan SPF, DKIM, DMARC. Debe ser ~100% (si no, revisa `42`) |
| **IP Reputation** | Reputación de las IPs que envían por ti |
| **Delivery Errors** | Por qué Gmail rechazó correos |

**Requisito:** Postmaster necesita cierto volumen a Gmail (~algunas decenas/día) para mostrar datos, así que empieza a verlo unas semanas después de lanzar. Revísalo semanalmente.

## Rutina de monitoreo (qué revisar y cuándo)

```
DIARIO (en tu plataforma Instantly/Smartlead):
  [ ] Bounce rate de campañas activas < 2% (si sube, pausa)
  [ ] Que no haya buzones "desconectados" o pausados por la plataforma
  [ ] Warmup score de cada buzón sigue verde (ver 43)

SEMANAL:
  [ ] Google Postmaster: Domain Reputation en Alta/Media, Spam Rate < 0.1%
  [ ] Blacklist check (MXToolbox) de dominios e IPs
  [ ] Reply rate por campaña vs semana anterior (¿cayó? ver 83)
  [ ] Mail-Tester a un buzón: sigue en 9-10/10 (ver 42)

MENSUAL:
  [ ] Revisar buzones de bajo rendimiento: jubilar los degradados, sumar nuevos calientes
  [ ] Auditar autenticación de todos los dominios (SPF/DKIM/DMARC intactos)
```

## Cómo leer una caída: el árbol de decisión

Si las respuestas se secan, no reescribas el copy de una: **diagnostica en orden** (deliverability primero, porque si estás en spam nada del resto importa):

1. **¿Bounce rate alto?** → lista sucia. Limpia (ver `23`) y detén hasta arreglar.
2. **¿Domain Reputation baja / spam rate alto en Postmaster?** → estás cayendo a spam. Baja volumen, refuerza warmup (ver `43`), revisa contenido (ver `45`).
3. **¿En blacklist?** → pausa, delisting, arregla causa.
4. **¿Todo lo técnico verde pero reply rate bajo?** → *ahora sí* es lista (ICP; ver `10`) o copy (ver `52`). Ese diagnóstico fino está en `83`.

## Errores comunes (qué NO hacer)

- Mirar solo el promedio global y no por buzón/dominio: un buzón podrido se esconde en el promedio.
- Ignorar el bounce rate hasta que "algo se siente mal". Para entonces ya quemaste la reputación.
- No verificar los dominios en Google Postmaster: vuelas ciego sobre la mayoría de tu audiencia.
- Reescribir el copy cuando el problema es que estás en spam. Diagnostica deliverability primero.
- No limpiar la lista antes de cada campaña grande (ver `44`).

## Siguiente paso

Con el monitoreo montado cierras el correo. Pero el outbound es multicanal: pasa a `47` (infraestructura de WhatsApp — API oficial vs no oficial, riesgo de baneo, clave en LatAm) y `48` (cómo combinar email + LinkedIn + teléfono + WhatsApp sin quemar cuentas). Para deliverability avanzada (segmentación de reputación, recuperación de dominios quemados, estrategias a gran volumen) ver `110`–`119`. Para números exactos de tasas y proyecciones, `Matematicas_lushows`.
