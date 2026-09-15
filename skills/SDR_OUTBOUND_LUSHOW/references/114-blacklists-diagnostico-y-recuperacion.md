# 114 — Blacklists: diagnóstico y recuperación

Una **blacklist** (lista negra / DNSBL — DNS-based blocklist) es una lista pública de dominios e IPs señalados por enviar spam. Los proveedores de correo la consultan en milisegundos: si tu dominio o la IP desde la que envías está en una lista importante, tus correos se bloquean o degradan de golpe, y ni el mejor copy ni el warmup te salvan. El módulo `46` mencionó las blacklists; este es el nivel operativo: **cómo detectas que caíste, en qué lista específica, qué la causó, y el procedimiento exacto para salir (delisting) sin volver a caer.** A escala de flota (ver `110`), revisar blacklists es parte del monitoreo semanal, porque un dominio en Spamhaus contamina la entrega de todo lo que envíe.

## Qué listas importan (y cuáles ignorar)

Hay cientos de DNSBL, pero solo unas pocas mueven la aguja. No entres en pánico por caer en una lista oscura que nadie consulta:

| Lista | Peso | A quién afecta | Delisting |
|---|---|---|---|
| **Spamhaus** (SBL, XBL, CSS, DBL) | **El nº1.** La consultan casi todos | IPs y dominios | Formulario; suele quitar en días si dejas de enviar mal |
| **Barracuda** (BRBL) | Alto (muchos Outlook corporativos) | IPs | Formulario de removal |
| **SpamCop** (SCBL) | Medio; caduca solo | IPs | Expira ~24h si paras; o solicitud |
| **SORBS** | Medio-bajo | IPs y rangos | Formulario |
| **UCEPROTECT** (L2/L3) | **Ignorable** casi siempre | Rangos enteros de IP | Cobran por salir; no te obsesiones |
| **Microsoft/Outlook (interna)** | Alto para @outlook/@hotmail | Su propio filtro | Vía formularios de Microsoft (no es DNSBL pública) |

**Spamhaus DBL** (Domain Block List) es la más peligrosa para outbound porque señala **dominios**, no solo IPs — y como usas dominios secundarios (ver `41`), un dominio tuyo en la DBL queda inservible. IP suele importar menos porque en Google Workspace/365 compartes IP con miles (no controlas ni ves esa reputación de IP tan directo).

## Cómo detectar que caíste

**Nunca esperes a "sentirlo".** El chequeo va en tu rutina semanal (ver `113`). Herramientas gratis:

| Herramienta | Qué hace |
|---|---|
| **MXToolbox Blacklist Check** (mxtoolbox.com/blacklists.aspx) | Metes dominio o IP, revisa ~80 listas de una, marca en cuáles estás |
| **Spamhaus Check** (check.spamhaus.org) | Consulta directa a la lista más crítica; te dice el motivo |
| **MultiRBL** (multirbl.valli.org) | Chequeo exhaustivo contra decenas de RBL |
| **Google Postmaster** | No es blacklist, pero "Domain Reputation: Mala" suele acompañar un listado (ver `113`) |

Cómo saber **qué IP revisar:** manda un correo de prueba a Gmail, abre "Mostrar original" y busca la IP de envío (`Received-SPF` / la IP del último servidor). Esa es la que consultas. Para el dominio, usas el dominio de envío directo.

## Diagnóstico: por qué caíste (arréglalo ANTES de pedir salida)

Salir de una lista sin arreglar la causa = vuelves a caer en días y la segunda vez es más difícil salir. Causas típicas, en orden de frecuencia:

1. **Lista sucia → bounce alto.** Mandaste a correos inválidos/spam-traps. La causa nº1. Arréglalo: verifica SIEMPRE la lista antes de enviar (NeverBounce/ZeroBounce/MillionVerifier; ver `28`, `44`).
2. **Spam-trap.** Correos "señuelo" que las listas siembran; si les escribes, te marcan como spammer que compra listas. Nunca compres listas; enriquece y verifica (ver `29`, `28`).
3. **Volumen brusco.** Disparaste sin rampa (ver `112`). Un buzón nuevo a 100/día grita spam.
4. **Quejas de spam altas.** Gente te marcó (ver Spam Rate en `113`). Lista/copy irrelevante.
5. **Buzón comprometido / mala config.** Autenticación rota (ver `42`) o cuenta hackeada enviando por ti.

## El procedimiento de delisting (paso a paso)

```
1. PARA. Pausa TODO envío desde ese dominio/IP inmediatamente.
         Seguir enviando mientras estás listado empeora todo y bloquea el delisting.
2. DIAGNOSTICA la causa (tabla arriba). No sigas sin saber por qué caíste.
3. ARREGLA la causa:
      - Lista sucia → limpia toda la base con verificador, quita hard bounces (ver 28)
      - Volumen → baja a rampa lenta cuando reinicies (ver 112)
      - Autenticación → repara SPF/DKIM/DMARC (ver 42, 111)
4. SOLICITA el delisting en el sitio de CADA lista donde estés:
      - Spamhaus: check.spamhaus.org → busca tu dominio/IP → "Request removal"
      - Barracuda: barracudacentral.org/rbl/removal-request
      - SpamCop: suele auto-expirar en ~24h si paras; o su formulario
      Sé honesto en el formulario: describe la causa y qué corregiste.
5. ESPERA. Spamhaus suele quitar en horas-días si dejaste de enviar mal.
   No re-solicites en loop (empeora). No reenvíes hasta salir.
6. REINICIA con warmup lento (ver 112), volumen mínimo, lista limpísima.
   Vigila Postmaster + blacklists a diario la primera semana (ver 113).
```

## ¿Recuperar o jubilar el dominio?

Depende de la lista y la reincidencia:

| Situación | Acción |
|---|---|
| Primera vez, SpamCop/lista menor | Delisting + arreglar causa. Recuperable, sigue usándolo |
| Spamhaus DBL, primera vez, causa clara y corregida | Delisting + descanso + warmup lento. Suele recuperarse |
| Reincidente (2ª–3ª vez en Spamhaus), o Domain Reputation "Mala" sostenida | **Jubila el dominio.** No vale la pena; cómpralo de nuevo y aísla (ver `117`) |
| IP compartida de Workspace listada | Poco que hagas tú; suele ser masivo y Google lo resuelve. Vigila que no sea tu dominio el listado |

La regla de flota: **los dominios de outbound son desechables** (ver `110`). Si recuperar cuesta más esfuerzo que jubilar y calentar uno nuevo, jubila. Guarda el esfuerzo de recuperación para tu **dominio principal**, que ese sí es irreemplazable.

## Errores comunes (qué NO hacer)

- Seguir enviando mientras estás listado: bloquea el delisting y hunde la IP compartida (perjudicas a otros y a ti).
- Pedir salida sin arreglar la causa: vuelves a caer y la reincidencia complica el delisting.
- Re-solicitar delisting en loop: algunas listas lo penalizan.
- Obsesionarte con UCEPROTECT o listas oscuras que nadie consulta (y que cobran por salir).
- No revisar blacklists en la rutina semanal: te enteras cuando ya llevas semanas bloqueado.
- Recuperar a toda costa un dominio secundario reincidente en vez de jubilarlo (ver `117`).

## Siguiente paso

Salir de blacklists resuelve el bloqueo duro. Pero muchas veces no estás listado y aun así caes en la carpeta de spam o Promociones — eso es **inbox placement**, y se audita distinto: ve a `116` (spam testing con seed lists). Si el dominio ya no se recupera, `117` (recuperar o jubilar un dominio quemado). Para leer la reputación que dispara los listados, `113`. Para limpiar la lista que te metió en la blacklist, `28`.
