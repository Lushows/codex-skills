# 111 — DMARC, BIMI y reputación de dominio

En el Bloque 4 configuraste SPF, DKIM y DMARC en `p=none` para poder empezar sin bloquear tu propio correo (ver `42`). Este módulo es el nivel avanzado: **cómo endureces DMARC hasta `reject`, qué es BIMI y si te conviene, y cómo pilotas la reputación de cada dominio de tu flota** (ver `110`) como un activo que se construye y se cuida. A escala, la autenticación deja de ser "algo que configuras una vez" y se vuelve una postura de seguridad que subes gradualmente y auditas. Un DMARC laxo te deja expuesto a suplantación; un DMARC estricto mal escalonado bloquea tu propio correo legítimo. El arte está en subir el rigor sin cortarte.

## DMARC: de `none` a `reject`, la escalera correcta

**DMARC** (ver `42`) le dice al proveedor qué hacer cuando un correo dice ser tuyo pero falla SPF y DKIM, y te manda reportes de quién envía con tu dominio. La política vive en el valor `p=`. La estrategia avanzada es **subirla en escalera, guiándote por los reportes**, nunca de un salto:

| Fase | Política | Qué logra | Cuándo pasar a la siguiente |
|---|---|---|---|
| 1 | `p=none` | Solo observa y reporta; no bloquea nada | Cuando 2–4 semanas de reportes muestran que tu correo legítimo pasa SPF/DKIM ~100% |
| 2 | `p=quarantine; pct=25` | Manda a spam el 25% de lo que falle (prueba parcial) | Si no aparece correo legítimo tuyo en cuarentena, sube `pct` a 50, 100 |
| 3 | `p=quarantine; pct=100` | Todo lo que falle va a spam | Cuando confirmes cero falsos positivos por varias semanas |
| 4 | `p=reject` | Rechaza en el servidor lo que falle. Máxima protección | Objetivo final de todo dominio de envío maduro |

El `pct=` (porcentaje) es la palanca fina que casi nadie usa: te deja aplicar la política a solo una fracción del correo que falla, para detectar problemas sin romper todo. Registro de ejemplo en fase 2:

```
Tipo:   TXT
Nombre: _dmarc
Valor:  v=DMARC1; p=quarantine; pct=25; rua=mailto:dmarc@tudominio.com;
        ruf=mailto:forense@tudominio.com; adkim=s; aspf=s; fo=1
```

- `rua=` recibe los **reportes agregados** (resumen diario de quién envió y si pasó). `ruf=` recibe reportes forenses (por mensaje; algunos proveedores no lo mandan).
- `adkim=s; aspf=s` = **alineación estricta**: el dominio del "From" que ve el prospecto debe coincidir exactamente con el que firma. A escala súbelo a estricto para que nadie use un subdominio tuyo sin permiso.
- `fo=1` pide reporte forense si falla SPF **o** DKIM (no solo ambos).

**Lee los reportes.** Llegan en XML crudo, ilegible a mano. Usa un lector gratis/barato: **Postmark DMARC** (reportes por email, gratis), **dmarcian**, **Valimail**, **EasyDMARC** o **URIports**. Te muestran en tablero quién envía con tu dominio y qué falla — así detectas suplantación y errores de config antes de subir la política.

## BIMI: qué es y si te conviene

**BIMI** (Brand Indicators for Message Identification) hace que tu **logo aparezca junto a tu correo** en la bandeja de Gmail, Apple Mail, Yahoo. Es señal de marca y confianza. Pero para outbound frío la respuesta honesta es matizada:

| Punto | Realidad |
|---|---|
| **Requisito duro** | Exige DMARC en `p=quarantine` o `p=reject` (por eso vive en este módulo, después de endurecer DMARC) |
| **Logo** | Un SVG en formato específico (SVG Tiny P/S) publicado en tu DNS como registro BIMI |
| **VMC** | Para que Gmail muestre el logo suele exigir un **VMC** (Verified Mark Certificate) — certificado de marca **registrada**, ~$1.000–1.500/año por dominio, emitido por DigiCert/Entrust |
| **¿Conviene en cold email a escala?** | **Casi nunca.** El VMC por dominio × decenas de dominios de flota es carísimo, y tus dominios de envío son variantes desechables sin marca registrada. BIMI brilla en el **dominio principal** de marketing/transaccional, no en la flota fría |

**Regla práctica:** monta BIMI solo en tu **dominio principal** (el real, con tu marca, desde donde mandas transaccionales y newsletters), nunca en los dominios secundarios de outbound. Para el correo frío, DMARC `reject` bien hecho ya te da el 95% del beneficio de reputación; BIMI es cosmético y caro para ese uso.

## Reputación de dominio: el activo que pilotas

Cada dominio acumula un puntaje invisible de reputación (ver `40`). A nivel avanzado lo tratas como un **activo con ciclo de vida**:

1. **Nace neutro-bajo** (dominio recién comprado y autenticado).
2. **Sube con warmup** (ver `112`) y con engagement real (respuestas, no quejas).
3. **Se mantiene** mientras mandes a listas limpias (ver `28`) y gente que encaja (ICP; ver `10`).
4. **Cae** con bounces, quejas de spam, o volumen brusco.
5. **Se jubila** cuando cae y no se recupera rápido (ver `117`).

Lo que mueve la reputación, ordenado por peso:

| Palanca | Efecto | Módulo |
|---|---|---|
| Spam complaints | Devastador (baja reputación rapidísimo) | `113`, `40` |
| Bounce rate | Muy alto (lista sucia = "no sabe a quién escribe") | `114`, `28` |
| Autenticación 100% (SPF/DKIM/DMARC) | Base necesaria; sin esto ni empiezas | `42` |
| Engagement positivo (respuestas) | Sube reputación de forma sostenida | `112` |
| Antigüedad del dominio (age) | Dominios con meses/años pesan más que recién comprados | `41` |
| Consistencia de volumen | Enviar parejo > picos bruscos | `112` |

## Checklist de endurecimiento por dominio

```
[ ] SPF, DKIM, DMARC verificados al 100% en reportes rua (varias semanas)
[ ] DMARC subido en escalera: none → quarantine pct=25 → 100 → reject
[ ] Alineación estricta: adkim=s; aspf=s
[ ] Lector de reportes DMARC activo (Postmark/dmarcian/EasyDMARC)
[ ] BIMI SOLO en dominio principal (si hay marca registrada + VMC), NO en la flota
[ ] Dominio verificado en Google Postmaster para leer reputación real (ver 113)
```

## Errores comunes (qué NO hacer)

- Saltar de `p=none` a `p=reject` de golpe: bloqueas tu propio correo legítimo si algo no estaba alineado.
- No leer los reportes DMARC: son el único lugar donde ves suplantación y errores antes de que te cuesten.
- Pagar VMC + BIMI para dominios de outbound frío desechables: dinero tirado.
- Creer que DMARC estricto "mejora la entrega" por sí solo. Protege contra suplantación y es requisito de reputación, pero no compensa una lista mala ni copy de spam (ver `114`, `45`).

## Siguiente paso

Con DMARC endurecido y la reputación entendida como activo, el motor que la construye es el warmup a escala: ve a `112` (warmup avanzado y rampa de volumen para la flota). Para leer la reputación real que Google te asigna, `113`. Los fundamentos de los tres registros están en `42`.
