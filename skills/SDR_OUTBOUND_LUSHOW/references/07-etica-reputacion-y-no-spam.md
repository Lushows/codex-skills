# 07 — Ética, reputación y no-spam

Este módulo defiende una tesis incómoda pero rentable: **el spam es mal negocio, no solo mala ética.** El outbound que respeta al destinatario —relevancia real, permiso implícito, salida fácil, datos legales— es el único que escala por años sin quemarte el dominio, la marca ni meterte en problemas legales. El spray-and-pray (rociar mensajes genéricos a miles al azar) muere en semanas. Aquí está el porqué y cómo hacer outbound ético que además rinde más.

## El principio: tres reputaciones que el spam destruye

Cuando spameas, no "arriesgas un poco": quemas tres activos, dos de ellos difíciles o imposibles de recuperar:

1. **Reputación de dominio (deliverability)** — Los proveedores de correo (Gmail, Outlook) puntúan tu dominio. Si mucha gente te marca como spam o tus correos rebotan, tu dominio entra en listas negras y **todos** tus correos —incluso los buenos— caen en spam. Recuperar un dominio quemado es lento y a veces imposible (ver `40`, `117`). Un dominio quemado puede costarte meses de pipeline.
2. **Reputación de marca** — La gente asocia tu nombre con basura. En B2B, donde el boca a boca entre pares pesa, ser "el que manda spam" te cierra puertas que ni sabías que existían.
3. **Reputación legal** — En muchos países el cold email/WhatsApp mal hecho es **ilegal** (Habeas Data en Colombia, GDPR en Europa, CAN-SPAM en USA). Multas reales, no teóricas (ver `49`).

El outbound relevante protege las tres. Por eso la ética aquí **no es moralina: es la estrategia que hace que la máquina dure.**

## Spam vs outbound legítimo: la diferencia real

No es "cold email = spam". El cold email B2B relevante es legítimo. La línea la marcan cuatro cosas:

| | Spam | Outbound legítimo |
|---|---|---|
| **Destinatario** | Comprado/al azar, no encaja | Elegido por ICP, se beneficia de verdad (ver `10`) |
| **Mensaje** | Genérico, masivo, sobre ti | Relevante a *esa* cuenta, sobre su problema (ver `52`) |
| **Volumen por persona** | Bombardeo sin parar | Cadencia acotada, con break-up (ver `60`, `63`) |
| **Salida** | Sin opt-out o falso | Opt-out claro y respetado siempre |
| **Datos** | Lista comprada ilegal | Datos conseguidos legalmente (ver `27`, `49`) |
| **Intención** | Rociar a ver quién cae | Iniciar una conversación con quien encaja |

El "permiso" en B2B es distinto al B2C: un contacto comercial relevante a un decisor sobre su área de trabajo, con salida fácil, se considera legítimo en la mayoría de marcos (interés legítimo bajo GDPR, B2B bajo Habeas Data colombiano con matices; ver `49`, `181`). Rociar 10.000 correos a compras genéricas de listas piratas, no.

## Las reglas de oro del outbound ético (y rentable)

1. **Contacta solo a quien de verdad se beneficia.** Si tu mensaje no tendría sentido para esa persona, no lo mandes. La relevancia es el permiso.
2. **Opt-out siempre, y respétalo al instante.** Una línea clara para salir ("si no es para ti, respóndeme 'no' y no vuelvo a escribir"). El que pide salir se quita **para siempre**, de inmediato. No respetarlo es ilegal y quema tu reputación.
3. **Datos conseguidos legalmente.** Nada de listas compradas de origen dudoso. Fuentes legítimas y verificación (ver `27`, `28`, `49`).
4. **Volumen humano y parejo.** ~30–50 correos por buzón/día (ver `44`), cadencias acotadas (5–8 toques, no infinitos). Los picos y el acoso te delatan como spam.
5. **No engañes.** Nada de asuntos falsos ("RE: nuestra reunión" cuando no hubo ninguna), nombres falsos ni promesas mentirosas. El engaño viola CAN-SPAM y quema la marca.
6. **Personaliza la relevancia, no el truco.** Investiga la cuenta y demuéstralo (ver `52`, `53`). Eso es respeto y sube el reply rate a la vez.

## Por qué el spam pierde en números

El spam parece atractivo ("mando 10.000 y algo caerá"). No cae:

```
Spray-and-pray: 10.000 correos genéricos desde 1 dominio
  → spam complaints altos → dominio quemado en días
  → reply rate <0.5%, la mayoría negativos
  → resultado: dominio muerto + marca dañada + casi cero reuniones

Outbound relevante: 500 correos a cuentas que encajan, 10 buzones, mensaje por cuenta
  → complaints casi cero → deliverability sana por meses
  → reply rate 5–8%, positivos reales
  → resultado: pipeline sostenible que puedes escalar sin quemar nada
```

Menos correos, mejor elegidos, ganan en reuniones **y** en durabilidad. La relevancia no es lo "correcto": es lo que **funciona a escala**.

## Errores comunes (qué NO hacer)

- **Comprar listas.** Origen ilegal, datos sucios, altísimo bounce → dominio quemado y multa potencial. Nunca (ver `49`).
- **Ignorar los opt-out.** Seguir escribiéndole a quien pidió salir es la forma más rápida de una queja formal y de que te reporten.
- **Asuntos engañosos / suplantación.** Sube aperturas un día, hunde tu reputación para siempre y viola la ley.
- **Bombardear al que no responde.** Silencio no es "sí, insiste 15 veces". Cadencia acotada y break-up (ver `63`).
- **Un solo dominio a todo volumen.** Cuando cae, cae todo tu correo, incluido el de tu empresa. Usa dominios secundarios (ver `41`).

## Las fronteras

- **Ley concreta por país** (Habeas Data, GDPR, CAN-SPAM, opt-out) → `49` y, para Colombia, `181`.
- **Deliverability técnica** (dominios, SPF/DKIM/DMARC, warmup) que sostiene la reputación → Bloque 4 (`40`–`49`).
- **Persuasión ética dentro de la venta** → `ventas_lushows` (misma filosofía: ética que además cierra).

## Siguiente paso

Audita tu outbound actual contra las 6 reglas de oro. Si compras listas, mandas genérico o desde tu dominio principal, para eso primero — es lo que más te está costando en reuniones y reputación. Luego lee `49` (cumplimiento legal) y `41` (dominios secundarios) para montar la infraestructura que hace el outbound ético *y* sostenible.
