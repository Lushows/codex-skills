# 41 — Dominios secundarios de envío

La primera decisión física del outbound es *desde dónde* envías. La respuesta correcta casi nunca es "desde mi dominio principal", y este módulo explica por qué y cómo montar la alternativa: **dominios secundarios de envío** (dominios que compras solo para mandar campañas de outbound, separados del que usas para tu correo real y tu web). Es la primera capa de protección de tu reputación (ver `40`): si un experimento de outbound sale mal y quemas la reputación, quemas un dominio desechable de $12, no el dominio del que dependen tus ventas, tus facturas y tu equipo.

## El principio: nunca quemes el dominio principal

Tu **dominio principal** (ej. `tuempresa.com`) es el que usas para tu web, tu correo diario, tus clientes. Si su reputación cae a spam, dejas de llegar a bandeja de entrada **con todo el mundo**, incluidos clientes que te escribieron primero. Es un daño que puede tardar meses en revertirse, o ser permanente.

El outbound en frío es, por definición, la actividad de mayor riesgo de reputación: mandas a gente que no te conoce, algunos te marcan spam, algunos correos rebotan. Meter ese riesgo en tu dominio principal es como probar los frenos de un carro con tu familia adentro. **Solución: compras dominios "espejo" — variantes de tu marca — y todo el outbound sale de ahí.** Si uno se quema, lo jubilas y lo reemplazas sin que tu operación real sienta nada.

## Cómo elegir los dominios secundarios

La regla: que **evoquen tu marca sin ser tu dominio principal**, para que el prospecto vea un remitente creíble ("ah, es de esa empresa") y tú protejas el original.

Variantes que funcionan (ejemplo con marca `gastrolatam.com`):

| Tipo | Ejemplo | Nota |
|---|---|---|
| Cambiar el TLD | `gastrolatam.co`, `gastrolatam.io`, `gastrolatam.net` | El más limpio y recomendado |
| Agregar palabra corta | `getgastrolatam.com`, `trygastrolatam.com`, `gastrolatam-app.com` | "get"/"try" son estándar en B2B |
| Guion / variante regional | `gastro-latam.com`, `gastrolatam.com.co` | Útil en LatAm por país |

**Qué NO comprar:** dominios que no se parecen en nada a tu marca (`mejoresofertas123.com` — se ve a spam y no genera confianza), ni guiones raros que parezcan phishing. La `.com` con TLD alterno (`.co`, `.io`) suele ser la más segura para reputación.

## La redirección: por qué y cómo

Cuando alguien recibe tu correo desde `getgastrolatam.com` y hace clic para ver "quién es esta empresa", va a escribir el dominio en el navegador. Si `getgastrolatam.com` no muestra nada, se ve sospechoso. **Configuras una redirección 301** (una regla que reenvía automáticamente ese dominio a tu web real): quien visite `getgastrolatam.com` aterriza en `gastrolatam.com`. Así el dominio de envío tiene una web "real" detrás y suma credibilidad sin que mantengas sitios separados.

Se hace en un clic desde donde compras el dominio (Namecheap, Cloudflare, GoDaddy): buscas "Redirect / Forwarding" → 301 permanente → destino tu dominio principal. Cloudflare (gratis) es el más limpio para esto.

## Cuántos dominios y cuántos buzones

Aquí está la matemática que casi todos hacen mal. La unidad real de envío no es el dominio, es el **buzón** (mailbox — una cuenta de correo, ej. `luis@getgastrolatam.com`). Cada buzón manda con seguridad **~30–50 correos/día** (ver `44`). Entonces trabajas hacia atrás desde tu meta de volumen:

- **Regla práctica:** 2–3 buzones por dominio (más de 3 en un dominio nuevo se ve raro y concentra riesgo).
- **Cada buzón:** ~40 correos/día sostenible.
- Por lo tanto, 1 dominio ≈ 3 buzones ≈ **~120 correos/día**.

Dimensiona así:

| Meta de envío/día | Dominios | Buzones (≈3/dominio) | Correos/día (≈40/buzón) |
|---|---|---|---|
| Prueba / arranque | 1 | 2–3 | 80–120 |
| Operación pequeña | 2–3 | 6–9 | 240–360 |
| Volumen serio | 5 | 15 | ~600 |
| Escala | 10 | 30 | ~1.200 |

**Costo real 2026:** dominio ~$10–15 USD/año; buzón de Google Workspace ~$6–7 USD/mes o Microsoft 365 ~$6 USD/mes. Existen proveedores especializados en buzones para outbound (Google Workspace revendido, o servicios como Maildoso / MailReef / Zapmail) que salen más baratos por volumen (~$3–4/buzón). Ejemplo: 3 dominios + 9 buzones ≈ $45 dominios/año + ~$55/mes buzones. Es la inversión más rentable del outbound: protege el activo que de verdad importa.

## Ejemplo de montaje (arranque real)

```
Dominio principal (NO tocar):  gastrolatam.com
Dominios de envío comprados:   getgastrolatam.co, trygastrolatam.com, gastrolatam.io
  → cada uno redirige 301 a gastrolatam.com
Buzones (3 por dominio):
   luis@getgastrolatam.co, maria@getgastrolatam.co, ventas@getgastrolatam.co
   ...igual en los otros dos dominios = 9 buzones
Capacidad total: 9 × 40 = ~360 correos/día una vez calentados
Siguiente: autenticar los 3 dominios (ver 42) y calentar los 9 buzones (ver 43)
```

## Errores comunes (qué NO hacer)

- Mandar outbound desde `@gastrolatam.com`. El error más caro. Nunca.
- Comprar 1 dominio y meterle 10 buzones para "ahorrar": concentras riesgo y se ve a granja de spam. Mejor 3 dominios con 3 buzones cada uno.
- Comprar el dominio y empezar a enviar el mismo día. Sin autenticar (ver `42`) y sin calentar (ver `43`) vas directo a spam.
- Usar el mismo buzón para outbound y para responder soporte/clientes. Separa funciones.

## Siguiente paso

Ya tienes los dominios: ahora **autentícalos** con SPF, DKIM y DMARC (ver `42`) — sin eso, hasta el dominio secundario mejor elegido cae en spam. Luego caliéntalos (ver `43`). Para estrategias avanzadas de arquitectura de dominios a gran volumen (sub-dominios, aislamiento de reputación por segmento) ver `110`–`119`.
