# 184 — Outbound en España y Europa

Europa es el mercado más lucrativo por ticket y el más peligroso por regulación. Si le vendes a empresas europeas —o a España como puerta de entrada hispanohablante al continente— este módulo es tu escudo y tu manual. La diferencia central con USA y LatAm es una sola palabra: **GDPR**, la ley de protección de datos más estricta del mundo, con multas de hasta €20 millones o el 4% de la facturación global. Aquí el outbound no se juega en "¿cómo destaco?" sino en "¿tengo base legal para escribirle a esta persona?". Hacer outbound europeo sin entender la base legal es jugar a la ruleta rusa con la caja de la empresa.

## El principio: la base legal es el punto de partida, no el detalle

En USA CAN-SPAM te deja escribir primero y preguntar después. En Europa es al revés: **antes de tocar un dato personal necesitas una base legal que lo justifique.** Un email `nombre@empresa.com` es dato personal bajo GDPR. Para cold outreach B2B, la base que se usa normalmente es **interés legítimo** (legitimate interest) — no consentimiento previo — pero solo se sostiene si el contacto es genuinamente relevante para el trabajo de esa persona y no aplasta sus derechos. El ICP afilado (ver `10`) deja de ser solo estrategia comercial y se vuelve tu **defensa legal**: escribirle a la persona correcta sobre algo pertinente es lo que hace legítimo el interés.

## GDPR aplicado al outbound (lo que importa)

Detalle general en `49`; aquí lo operativo para no equivocarte:

| Requisito | Qué significa para tu outbound |
|---|---|
| **Base legal** | Interés legítimo para B2B relevante; documenta por qué le escribes a ese rol |
| **Balance de intereses (LIA)** | Registra que tu interés no vulnera los derechos del contacto (un Legitimate Interest Assessment simple) |
| **Transparencia** | Si preguntan de dónde sacaste el dato, debes decirlo |
| **Derecho de oposición / olvido** | Si pide no ser contactado o borrado, cumples de inmediato y para siempre |
| **Opt-out en cada mensaje** | Salida clara y honrada, siempre |
| **ePrivacy** | Para email a **personas físicas/autónomos** algunos países exigen opt-in; el B2B a roles corporativos suele ir por interés legítimo |

**Regla de oro europea:** cuanto más se parezca el destinatario a un consumidor (autónomo, email personal, sin relación con tu oferta), más cerca estás de necesitar consentimiento (opt-in). Cuanto más claramente sea un rol corporativo relevante, más sólido tu interés legítimo. Ante la duda en Europa, tira hacia lo conservador.

## Matices por país (Europa no es un bloque uniforme)

- **España**: interés legítimo aceptado para B2B; la **LOPDGDD** complementa el GDPR y la **LSSI** regula comunicaciones comerciales electrónicas (tiende a exigir consentimiento para email comercial a personas, con excepción de relación contractual previa). Vigila la **AEPD**.
- **Alemania**: de los más estrictos. La jurisprudencia suele exigir **opt-in incluso para B2B** por email/llamada en frío. Trátalo como consentimiento requerido salvo que un abogado local diga lo contrario.
- **Francia**: la **CNIL** distingue B2B (interés legítimo posible al rol profesional) de B2C (opt-in). Más permisivo que Alemania.
- **Reino Unido** (post-Brexit): **UK GDPR + PECR**. Similar a la UE; el B2B a empresas (limited companies) tiene margen, a autónomos/sole traders se acerca al opt-in.
- **Países nórdicos y Benelux**: generalmente estrictos y con alta cultura de privacidad.

No memorices los 27 países: la regla práctica es **B2B relevante a rol corporativo = zona de interés legítimo; cualquier cosa que huela a consumidor = opt-in**. Para un caso serio o volumen grande en un país concreto, abogado local. Esto es orientación, no asesoría jurídica.

## El estilo europeo del mensaje

- **Formal y sobrio.** Europa (y España en negocios) es más formal que USA y menos efusiva que LatAm. Nada de emojis en frío corporativo, nada de exceso de entusiasmo.
- **Directo pero respetuoso.** Ve al punto como en USA, pero con cortesía y sin agresividad de CTA.
- **España**: "usted" en el primer contacto formal; español peninsular ("vale", "vosotros" — ojo, esto chirría en LatAm y viceversa, ver `189`).
- **Prueba y precisión** convencen más que el hype; el europeo desconfía del bombo.

## Ejemplo: cold email B2B (España/Europa, formal)

```
Asunto: consulta — {Empresa}

Buenos días {Nombre}:

Vi que {Empresa} ha abierto una segunda sede en Valencia. Suele
ser el momento en que el control de costes por producto empieza a
complicarse con las hojas de cálculo.

En {tu empresa} ayudamos a compañías de su tamaño a ver el margen
real por producto sin esa fricción. {Cliente similar} redujo un 8%
de merma en un trimestre.

¿Le encajaría una llamada breve la próxima semana?

Un saludo,
{Firma}

Si prefiere no recibir más correos, respóndame y le doy de baja de
inmediato. [Datos de la empresa / base del contacto]
```

Formal, "usted", sobrio, prueba concreta, opt-out explícito y transparencia. La conversación de venta → `ventas_lushows`.

## Errores comunes (qué NO hacer)

- Tratar Europa como USA: enviar en frío sin base legal documentada = riesgo de multa GDPR real.
- Asumir que "B2B no aplica GDPR": aplica siempre por el dato personal (ver `49`).
- Meter a Alemania en una campaña genérica de interés legítimo: ahí tira a opt-in.
- Usar tono LatAm efusivo o español de España con audiencia latina (y viceversa): rompe credibilidad (ver `189`).
- No tener LIA ni registro de fuente del dato: si te auditan, no tienes defensa.

## Siguiente paso

Antes de enviar a Europa: define tu base legal por segmento (interés legítimo B2B vs. opt-in), documenta un LIA simple, ajusta la lista para excluir países estrictos si no puedes cumplir opt-in (Alemania), y monta opt-out honrado + supresión global (ver `49`). Infra técnica igual de exigente que USA: SPF/DKIM/DMARC (`42`), warmup (`43`). Para vender desde LatAm hacia Europa (arbitraje, husos) ver `187` y `186`. La localización multi-idioma en `185`. La venta → `ventas_lushows`.
