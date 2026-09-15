# 160 — ABM: fundamentos (account-based de verdad, no volumen disfrazado)

Este es el módulo de entrada al **Bloque 16 (ABM & enterprise outbound)**. En `94` viste el mapa general; aquí bajamos al detalle: qué es ABM de verdad, cuándo hacerlo en serio y cómo montar el sistema completo. **ABM (Account-Based Marketing/Experience)** es tratar **una cuenta entera (la empresa) como el mercado**: en vez de perseguir contactos sueltos y ver quién pica, eliges pocas empresas que valen mucho y orquestas un ataque coordinado —marketing, SDR y vendedor— sobre cada una. La palabra clave es **coordinación**: no es "mandar el mismo correo a más gente de la empresa", eso es volumen disfrazado y es el error #1.

## El principio: economía de la cuenta, no del lead

El outbound de volumen (ver `05`) funciona por estadística: mil contactos, X% responde, Y% agenda. Con cuentas grandes esa matemática se rompe por dos razones:

1. **El ticket es alto y las cuentas son pocas.** Si tu cliente ideal son 80 empresas en todo el país y cada contrato vale mucho, no puedes "quemar" cuentas con un correo genérico: cada una es irremplazable. Perder una por spamear al contacto equivocado es carísimo.
2. **No decide una persona, decide un comité.** En una empresa grande la compra la aprueban 4–10 personas (usuario, jefe, finanzas, legal, quien firma; ver `11`, `165`). Contactar solo al gerente y esperar es un único punto de fallo.

La respuesta de ABM: **pocas cuentas, muchos contactos por cuenta, todo coordinado y 1:1 real.** Concentras recursos caros (research manual, ver `164`; multi-threading, ver `162`; el AE metido desde temprano, ver `163`) en las cuentas que de verdad mueven tu número.

| | Outbound de volumen | ABM |
|---|---|---|
| Unidad de trabajo | El contacto | La cuenta (empresa) |
| Nº de cuentas | Miles | 20–150 (por SDR/trimestre) |
| Contactos por cuenta | 1–2 | 4–10 (multi-threading `162`) |
| Personalización | Ligera, a escala (`52`) | Profunda, 1:1 por cuenta (`164`) |
| Quién ejecuta | El SDR solo | SDR + AE + marketing (`163`) |
| Canales | Email (± LinkedIn) | Email + LinkedIn + llamada + eventos + contenido + ads (`168`) |
| Métrica de éxito | Reuniones agendadas | Engagement de cuenta (`169`) |
| Ciclo | Corto | Largo, consultivo |

## Los tres sabores de ABM (según cuántas cuentas)

No todo ABM es el mismo nivel de esfuerzo. Se escala en tres tramos:

| Tipo | Cuentas | Esfuerzo por cuenta | Cuándo |
|---|---|---|---|
| **ABM 1:1 (strategic)** | 5–30 | Máximo: plan por cuenta, research a mano, contenido hecho a medida | Cuentas soñadas, ticket enorme |
| **ABM 1:few (lite)** | 30–150 | Medio: cuentas agrupadas por caso de uso/sector, personalización por cluster | La mayoría de programas B2B |
| **ABM programático** | 150–1.000+ | Bajo: intent data + ads + secuencias segmentadas | Cuando quieres ABM "de arriba del funnel" a más volumen |

Empieza por **1:few**: es donde está el mejor retorno para la mayoría. El 1:1 puro se reserva para tu Tier A de verdad (ver tiering en `16` y `161`).

## Cuándo hacer ABM vs outbound de volumen (la decisión)

Haz **ABM** si marcas la mayoría de estas:
- Ticket alto que justifica investigar cada cuenta a mano (la economía la valida `economist_lushows`; el ACV/CAC en `84`).
- Tu mercado real son **decenas o pocos cientos** de empresas, no decenas de miles (calcula tu TAM en `13`).
- La decisión involucra un **comité** (enterprise, sector regulado, compra técnica; ver `165`).
- Ciclo largo, consultivo, con varias reuniones.
- Ya tienes casos/prueba social en ese nicho para abrir puertas (ver `18`).

Haz **outbound de volumen** (ver `93`) si:
- Vendes a pymes con **decisor único** y ciclo corto.
- Ticket bajo: la personalización profunda no se paga.
- Tu mercado son miles de cuentas parecidas.

Muchos negocios corren **las dos máquinas en paralelo** con SDRs distintos: un equipo de volumen para el grueso y un equipo (o un solista con su Tier A) de ABM para las cuentas grandes. No mezcles los dos en la misma persona el mismo día: los modos mentales chocan (ver `67`).

## Cómo se monta un programa ABM (el sistema, de punta a punta)

1. **Define el ICP de cuenta** (no de contacto) y arma la lista objetivo → `161`.
2. **Tiering** A/B/C de esas cuentas → `16` + `161`.
3. **Mapa del comité** por cuenta: quiénes son los 4–8 contactos clave → `11`, `165`.
4. **Research por cuenta**: señales, iniciativas, prioridades públicas → `164`, `37`.
5. **Multi-threading**: tocar varios contactos a la vez sin quemar → `162`.
6. **Play coordinado**: marketing calienta, SDR prospecta, AE entra → `163`.
7. **Orquestación multicanal** a nivel cuenta → `168`; con eventos `166` y contenido `167`.
8. **Medición por cuenta** (engagement, no leads sueltos) → `169`.
9. **Cierre del deal** (comité, negociación, propuesta) → **`ventas_lushows`**. ABM te mete dentro de la cuenta; el trato grande se cierra allá.

## Errores comunes (qué NO hacer)

- **Llamar ABM a mandar la misma plantilla a más gente.** Sin coordinación ni 1:1 real, es volumen con otro nombre.
- **Arrancar en 1:1 con 200 cuentas.** No escala; te ahogas. Elige el sabor según capacidad.
- **ABM sin el vendedor.** El SDR solo no hace ABM; es esfuerzo de equipo (`163`). Si no tienes AE, tú haces las dos veces pero con el sombrero claro.
- **ABM a pymes de ticket bajo.** El costo de research no se recupera.
- **Medir ABM con métricas de volumen** (nº de correos, reuniones sueltas) en vez de engagement de cuenta (`169`).

## Siguiente paso

Decide con la regla de arriba si tu caso es ABM o volumen. Si es ABM, elige el sabor (empieza 1:few) y ve a `161` a construir la lista de cuentas objetivo con el ICP de cuenta. El comité vive en `11`/`165`; el cierre en `ventas_lushows`.
