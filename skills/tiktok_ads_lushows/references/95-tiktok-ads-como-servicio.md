# 95 — TikTok Ads como servicio

Lee este módulo cuando vayas a manejar pauta de TikTok para clientes (no para tu propio negocio), cuando no sepas cuánto cobrar en COP, o cuando un cliente te eche la culpa de que "los ads no funcionan" cuando el problema es que él no te da creativo. Operar TikTok para terceros es un negocio bueno, pero solo si pones las reglas claras desde el día 1. TikTok es **descubrimiento**: tú optimizas la máquina, pero sin creativo nativo del cliente no hay nada que optimizar (ver 92).

## Setup: Business Center y quién pone la tarjeta

El **TikTok Business Center** es el panel que te deja administrar varias cuentas publicitarias, clientes y miembros de equipo desde un solo lugar — el equivalente del Business Manager de Meta. Reglas de oro:

| Tema | Lo correcto | Por qué |
|---|---|---|
| **Dueño de la cuenta publicitaria** | El **cliente** crea su cuenta y te da acceso desde SU Business Center | Si te vas, el cliente conserva su historial, pixel y aprendizaje |
| **Quién pone la tarjeta** | El **cliente** (su tarjeta a nombre de su negocio verificado) | No financias pauta ajena; evitas líos de flujo y de ban (ver 93) |
| **Verificación** | El cliente verifica SU negocio (ver 93) | Reduce baneos y te quita responsabilidad legal |
| **Tu rol** | Eres miembro/admin invitado a su cuenta | Acceso para operar, sin ser el dueño del activo |
| **Pixel/Events API** | Vive en el dominio y servidor del cliente | El dato es del cliente; tú lo configuras (ver 06, 96) |

**Nunca** crees la cuenta a tu nombre ni pongas tu tarjeta "para arrancar rápido". Si el cliente no paga, te quedas con la deuda; si te baneas, arrastras a otros clientes en el mismo BC (ver 93); y el día que se vaya, se lleva el activo que tú construiste. El pixel, el historial y la cuenta son del cliente — tú vendes la **operación**, no eres dueño de la plata.

### Aislamiento de clientes

Cada cliente, su propio activo. No metas dos clientes en una misma cuenta publicitaria ni mezcles pixeles. Si un BC frágil cae, no quieres que arrastre a todos (ver 93 mapa de severidad). Tu BC de agencia puede recibir acceso a los BC de cada cliente sin ser dueño — esa es la estructura limpia.

## Pricing y retainers en COP

Hay tres modelos. Para Colombia/LatAm, valores de referencia jun-2026 (ajusta a tu experiencia y al tamaño del cliente):

| Modelo | Cómo cobras | Referencia COP | Cuándo usarlo |
|---|---|---|---|
| **Retainer fijo (fee)** | Mensual fijo por gestionar la cuenta | $800.000–$3.000.000/mes | Lo más común y sano; ingreso predecible |
| **% del ad spend** | Un % de lo que el cliente invierte en pauta | 10–20% del spend | Clientes que invierten fuerte ($10M+/mes) |
| **Fee + bonus por resultado** | Fijo bajo + premio por metas (ROAS, leads) | Fijo + 5–15% sobre meta | Cuando confías en el funnel completo |

Reglas de pricing:

- **No cobres solo % en cuentas chicas.** El 15% de $1.000.000 son $150.000 — no paga tu trabajo. Pon un fee mínimo.
- **El presupuesto de pauta NO es tu ingreso.** Sepáralo siempre: el cliente paga la pauta (a TikTok) Y tu fee (a ti). Que quede por escrito.
- **Cobra setup aparte** la primera vez (instalar pixel/Events API, estructura, primer banco de creativos, automatización de leads): $500.000–$1.500.000 COP one-time.
- **Cobra la producción de creativos aparte** si tú la haces (o que el cliente la asuma). Briefear es tu trabajo; grabar/editar es producción y se cobra o se delega (ver 91 para escalar con IA).
- Antes de cerrar un cliente, valida que su negocio **aguanta el CAC** y que la unit economics da (→ `economist_lushows`). No tomes clientes cuyo producto no puede ser rentable en pauta — vas a quedar mal por algo que no es tu culpa.

Para cerrar y estructurar la oferta de servicio (propuesta, manejo de "está caro", contrato, follow-up) → `ventas_lushows`.

### Modelo de escalera de servicio

| Etapa cliente | Qué le vendes | Fee referencia |
|---|---|---|
| Arranque (mes 1) | Setup + testeo de creativos manual (ver 98) | Setup one-time + fee base |
| Tracción (mes 2–3) | Optimización + escalado + reporte semanal | Retainer pleno |
| Maduro (mes 4+) | Omnicanal (Meta+Google) + sistematización | Retainer + % spend o bonus |

## Expectativas: el cliente DEBE producir creativo

Esta es la conversación que evita el 80% de los conflictos. Déjalo claro **antes de firmar**:

> "En TikTok el creativo es el 80% del resultado (ver 92). Yo optimizo la pauta, pero **el creativo nativo lo produces tú o tu creator** — yo te doy el brief, los ángulos y los hooks (ver 38), tú me das las grabaciones. Sin creativo nuevo cada semana, ninguna optimización salva la cuenta. La IA (Symphony) escala variantes de tus ganadores, pero el primer ganador lo grabamos con humano real (ver 91)."

Pon por escrito qué entrega cada quién:

| Tú entregas | El cliente entrega |
|---|---|
| Estructura, pixel/Events API, optimización, escalado | Acceso a su cuenta y su tarjeta |
| Briefs de creativos, ángulos, hooks (ver 38) | Las grabaciones nativas / el creator / el presupuesto de UGC |
| Reportes y recomendaciones | Velocidad para aprobar y producir |
| Spy de competencia (Creative Center, ver 94) | Producto/landing que aguanten la conversión |
| Conversión offline configurada (ver 96) | Que su equipo marque "vendido" en el CRM |

El cliente que cree que "tú haces los videos" y no quiere grabar ni pagar creator **no es buen cliente para TikTok**. Mejor decirlo antes que pelear después. Si insiste, ofrécele un paquete de producción aparte (con costo) o un creator de tu red — pero nunca lo escondas en el fee.

## Reportes que sí sirven

No mandes capturas del panel. Manda un reporte que el cliente (no técnico) entienda: spend, leads/ventas, CPA, ROAS/MER (ver 64, 97), qué creativo ganó y qué vas a hacer la próxima semana. La plantilla de reporte ejecutivo en HTML→PDF está en 99. Reporta **cadencia fija** (semanal o quincenal) — la consistencia genera confianza y renueva retainers.

Reporta por **MER global**, no por el ROAS inflado del panel (ver 97). Si le muestras al cliente el ROAS de TikTok solo, le mientes (las plataformas se solapan, ver 16). El cliente honesto valora que le digas la verdad, incluso "esto aún no es rentable, ajustamos así". Eso renueva contratos; el humo los pierde.

## Errores comunes — blacklist

- **Crear la cuenta a tu nombre / poner tu tarjeta.** Te quedas con la deuda y el cliente se lleva el activo. La cuenta es del cliente (ver 93).
- **Mezclar varios clientes en un mismo BC/cuenta.** Un ban arrastra a todos; aísla activos (ver 93).
- **Cobrar solo % en cuentas chicas.** No paga tu trabajo; pon fee mínimo.
- **No separar el presupuesto de pauta de tu fee.** El cliente debe ver claro qué paga a TikTok y qué te paga a ti.
- **No dejar por escrito quién produce el creativo.** Es el conflicto #1; el cliente produce, tú briefeas (ver 38, 92).
- **Tomar clientes cuya unit economics no da.** Quedas mal por algo que no es tu culpa; valida antes (→ `economist_lushows`).
- **Reportar con capturas del panel** o con el ROAS inflado. El cliente no técnico no entiende capturas; el ROAS solo miente (ver 97, 99).
- **No tener cadencia fija de reporte.** Sin consistencia, el cliente desconfía y no renueva.
