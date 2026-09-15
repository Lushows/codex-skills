# 42 — SPF, DKIM y DMARC: autenticación de correo

Estos tres registros son la **cédula de identidad de tu dominio para enviar correo**: le prueban a Gmail y Outlook que el correo viene de verdad de tu dominio y que tú autorizaste ese envío. Sin ellos, **tu correo cae en spam o lo rechazan directamente** — desde febrero de 2024 Google y Microsoft los exigen a cualquiera que envíe en volumen. Es el requisito de entrada de todo el Bloque 4 (ver `40`): puedes tener dominios perfectos (ver `41`) y buzones calientes (ver `43`), pero sin autenticar no llegas. La buena noticia: se configura una sola vez por dominio, en el panel DNS, en 20–30 minutos, y muchas plataformas de outbound hoy lo hacen casi solo.

## Qué es cada uno (en simple)

Los tres son **registros DNS** — líneas de texto que agregas en el panel donde administras tu dominio (Cloudflare, Namecheap, GoDaddy). Cada uno responde una pregunta distinta:

| Registro | La pregunta que responde | Analogía |
|---|---|---|
| **SPF** | ¿Qué servidores tienen permiso de enviar correo en nombre de este dominio? | La lista de invitados en la puerta |
| **DKIM** | ¿El correo llegó intacto y firmado por el dominio real? | El sello de cera / la firma digital |
| **DMARC** | Si SPF o DKIM fallan, ¿qué hago con el correo? Y avísame por reporte. | La política de seguridad + el CCTV |

Los tres juntos le dicen al proveedor: "este remitente es legítimo, autorizó este envío, y el correo no fue alterado". Eso sube tu reputación (ver `40`) y te deja entrar a la bandeja.

## SPF — Sender Policy Framework

Es un registro que **lista los servidores autorizados a enviar correo desde tu dominio**. Si el correo llega de un servidor que no está en la lista, es sospechoso.

Es un registro **TXT** en la raíz de tu dominio. Ejemplo para un dominio que envía con Google Workspace:

```
Tipo:   TXT
Nombre: @   (la raíz del dominio)
Valor:  v=spf1 include:_spf.google.com ~all
```

- `include:_spf.google.com` autoriza a los servidores de Google. Cada plataforma te da su `include:` (SendGrid, Microsoft, etc.).
- `~all` = "todo lo demás, márcalo como sospechoso (softfail)". Es el estándar seguro.
- **Regla crítica:** solo puedes tener **UN** registro SPF por dominio. Si usas varios servicios, combinas todos los `include:` en la misma línea. Dos registros SPF separados = SPF roto = correos a spam.

## DKIM — DomainKeys Identified Mail

Es una **firma criptográfica** que se agrega a cada correo. El servidor que envía firma con una llave privada; el proveedor que recibe verifica con la llave pública que publicas en tu DNS. Si coinciden, prueba dos cosas: el correo salió de tu dominio de verdad **y** nadie lo alteró en el camino.

Es un registro **TXT** (o CNAME, según el proveedor) en un subdominio con un "selector". Tu plataforma (Google, Instantly, etc.) te genera la llave; tú solo la pegas:

```
Tipo:   TXT
Nombre: google._domainkey     (el "google" es el selector, lo da el proveedor)
Valor:  v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQ...  (llave larga)
```

En Google Workspace se activa en Admin → Apps → Gmail → Autenticar correo → "Generar registro" → pegas lo que te da en tu DNS → "Iniciar autenticación". No inventes la llave: siempre la genera el proveedor.

## DMARC — el que amarra todo

DMARC hace dos cosas. Primero, define **qué debe hacer el proveedor cuando un correo dice ser tuyo pero falla SPF y DKIM** (ignorarlo, mandarlo a cuarentena/spam, o rechazarlo). Segundo, te **manda reportes** de quién está enviando correo con tu dominio — así detectas suplantación.

Es un registro **TXT** en el subdominio `_dmarc`:

```
Tipo:   TXT
Nombre: _dmarc
Valor:  v=DMARC1; p=none; rua=mailto:dmarc@tudominio.com; adkim=s; aspf=s
```

La `p=` es la política, y aquí va la estrategia:

| Política | Qué hace | Cuándo usarla |
|---|---|---|
| `p=none` | Solo monitorea y reporta, no bloquea nada | **Empieza aquí** las primeras 2–4 semanas |
| `p=quarantine` | Manda a spam lo que falle | Cuando confirmes que tu correo legítimo pasa bien |
| `p=reject` | Rechaza lo que falle | El objetivo final, máxima protección |

Empieza en `p=none` para no bloquear por accidente tu propio correo mientras terminas de configurar, revisa los reportes, y sube gradualmente a `quarantine` y luego `reject`.

## Extra crítico para outbound: BIMI no, pero PTR y "friendly-from" sí

- **Alineación (`adkim=s; aspf=s`):** el "From" que ve el prospecto debe coincidir con el dominio que firma. Las plataformas de outbound serias lo hacen solo, pero verifícalo.
- **Un correo bien autenticado** muestra en Gmail el candado / "el correo se envió por tudominio.com" sin advertencias. Esa es la prueba visual de que quedó bien.

## Cómo verificar que quedó bien (haz esto siempre)

No confíes en que "lo pegaste": **compruébalo**. Herramientas gratis:

- **MXToolbox** (mxtoolbox.com) → pruebas SPF, DKIM, DMARC uno por uno.
- **Mail-Tester** (mail-tester.com) → te da un correo, le escribes, y te da un puntaje /10 con todo lo que falla. Apunta a **10/10** antes de enviar en volumen.
- **Google Postmaster Tools** para monitoreo continuo (ver `46`).

```
Checklist de verificación por dominio:
[ ] SPF: un solo registro, con el include correcto, termina en ~all
[ ] DKIM: firma verificada, coincide el selector
[ ] DMARC: existe, empieza en p=none, con rua para reportes
[ ] Mail-Tester da 9-10/10
[ ] Gmail no muestra advertencia "vía" ni candado abierto
```

## Errores comunes (qué NO hacer)

- **Dos registros SPF** en el mismo dominio: rompe SPF. Combina en uno solo.
- Inventar la llave DKIM o copiarla de otro dominio: no funciona, cada dominio tiene la suya.
- Poner DMARC directo en `p=reject` sin monitorear: puedes bloquear tu propio correo legítimo. Sube gradual.
- Configurar todo y no verificar con Mail-Tester. Un error de tipeo en el DNS te deja en spam sin que lo sepas.
- Olvidar autenticar **cada** dominio secundario (ver `41`). Cada uno necesita sus tres registros.

## Siguiente paso

Con los dominios autenticados, el siguiente paso obligatorio antes de enviar un solo correo real es **calentar los buzones** (ver `43`): un dominio recién autenticado sigue teniendo reputación neutra-baja. Para monitorear la reputación una vez en marcha, ver `46`. Para deliverability avanzada (rotación de llaves DKIM, sub-dominios con reputación aislada) ver `110`–`119`.
