# 95 — Google Ads como servicio

Lee este módulo cuando vayas a cobrarle a alguien por manejarle sus campañas, cuando un conocido te diga "manéjame mi Google Ads" y no sepas qué cobrar ni cómo estructurarlo, o cuando ya tengas un cliente y todo sea un caos de tarjetas, reportes y expectativas. Manejar Google Ads para terceros es un negocio real y bueno en LatAm, pero se hunde por las mismas tres cosas: cobrar mal, prometer de más y mezclar tu plata con la del cliente. Este módulo es la parte de NEGOCIO; la viabilidad y el modelo financiero de TU agencia (cuánto cobrar para que dé, cuántos clientes aguantas) rutea a `economist_lushows`.

## MCC: tu cuartel para manejar clientes

El **MCC** (Manager Account / Cuenta de Administrador, antes "My Client Center") es una cuenta paraguas que controla varias cuentas de Google Ads desde un solo login. Es lo primero que montas como freelancer/agencia (ver 04 para crearlo).

| Regla de oro del MCC | Por qué |
|---|---|
| **El cliente es DUEÑO de su cuenta de Ads; tú solo la administras desde tu MCC** | Si se va, se lleva su cuenta y su historial. NUNCA crees su cuenta dentro de la tuya como si fuera tuya. |
| **La tarjeta que paga es la del CLIENTE** | No pongas tu tarjeta a pagar el gasto de medios. Si lo haces, financias al cliente y el riesgo es tuyo (ver abajo). |
| **Acceso por invitación (vinculación MCC)** | Pides acceso a su cuenta vía el MCC; no le pides usuario y contraseña. |
| **Una cuenta por cliente** | No mezcles dos negocios en una cuenta; arruina datos y políticas (ver 14, 93). |
| **Verificación de anunciante: la hace el cliente con SUS datos** | Es su identidad/negocio; no la "prestes" ni uses la tuya (ver 93). |

El MCC también te da **vista consolidada** (todas las cuentas, gasto y conversiones en un panel), **presupuestos y alertas** por cuenta, y la posibilidad de aplicar reglas/scripts a varias cuentas. Para 5+ clientes, sin MCC es un caos.

## Quién pone la tarjeta: el punto que arruina freelancers

El error que quiebra a los nuevos: **poner su propia tarjeta a pagar el gasto de medios del cliente.** Pasa así: el cliente "te paga después", tú adelantas $2.000.000 COP de pauta con tu tarjeta, el cliente desaparece o paga tarde, y tú quedaste financiando su publicidad. Reglas:

- **El gasto de medios lo paga el cliente, directo a Google, con SU tarjeta.** Tu honorario es aparte.
- Si el cliente no tiene cómo pagarle a Google directo, eso es problema de él, no tuyo de financiar.
- Tu honorario (fee) se cobra **por adelantado o quincenal**, nunca "cuando vendamos". Tú manejas la pauta; no eres socio del riesgo de su negocio.
- Si insiste en que pongas tú la tarjeta, **factura el medio + tu fee por adelantado**, con tope, y nunca por encima de lo que ya te pagó. Mejor: que pague directo a Google.

## Pricing: cómo cobrar

Tres modelos comunes en LatAm:

| Modelo | Cómo funciona | Cuándo |
|---|---|---|
| **Retainer fijo** (mensualidad) | Cobras $X COP/mes por manejar la cuenta | Lo más sano y predecible; el estándar |
| **% del gasto** (ad spend) | Cobras 10–20% de lo que el cliente invierte en medios | Cuentas con presupuesto grande; alinea pero premia gastar más |
| **Fijo + bono por resultado** | Mensualidad base + extra si pegas una meta (CPA, ventas) | Cuando la conversión es medible y limpia (ver 64) |
| **Setup + retainer** | Cobras un fee único de montaje (medición, estructura) + mensualidad | Casi siempre: el setup bien hecho es trabajo real, cóbralo |

Rangos de referencia (Colombia, jun-2026, orientativos, ajusta a tu nivel):
- **Setup inicial** (medición, GA4, conversiones, estructura, primeras campañas): **$600.000 – $2.000.000 COP** único.
- Cuenta pequeña / un solo negocio local: **$800.000 – $1.500.000 COP/mes** de honorario.
- Cuenta mediana (e-commerce, varios productos): **$1.500.000 – $3.500.000 COP/mes**.
- Cuenta grande / multicanal con OCI y reportería: **$3.500.000+ COP/mes**.
- % de gasto típico: **15%** (con piso mínimo, p.ej. $1.000.000 COP, para que cuentas chicas valgan la pena).

No cobres por horas — el cliente no entiende y tú te castigas por ser rápido. Cobras por **resultado/manejo**, no por tiempo. Para fijar TU precio con números reales (tu costo, tu margen, cuántos clientes aguantas), pásalo por `economist_lushows`.

## Onboarding: los primeros 7 días (lo que evita líos después)

1. **Vincula la cuenta a tu MCC** (no la crees tú; si no existe, créala a nombre del cliente, ver 04).
2. **Cliente completa verificación de anunciante** con sus datos (ver 93).
3. **Cierra la medición primero**: GA4, conversiones = venta real (no clic a WhatsApp), Enhanced Conversions, y plan de OCI si cierra offline (ver 05, 06, 53, 64).
4. **Acuerda la meta por escrito**: CPA o ROAS objetivo, derivado de su economía (ver 64). Sin esto, todo resultado es discutible.
5. **Define dónde cae el lead y quién cierra** (WhatsApp/CRM). Deja claro que la venta la cierra el cliente, no tú.
6. **Acuerda fee, forma y fecha de pago, y quién pone la tarjeta del medio** (él). Por escrito.

## Expectativas y reportes: lo que evita que te echen

La mayoría de freelancers no pierde clientes por malos resultados, sino por **mala comunicación**. Blindaje:

1. **Promete proceso, no milagros.** Nunca "te garantizo X ventas" (además es claim riesgoso, ver 93). Promete: "voy a montar la medición bien, lanzar, optimizar semanal y reportarte claro".
2. **Define la meta JUNTOS al inicio**: CPA o ROAS objetivo, basado en su economía (ver 64, `economist_lushows`). Sin meta no hay "bueno" ni "malo".
3. **Reporte mensual simple** (no 40 métricas que no entiende): inversión, conversiones, CPA, MER, qué hiciste, qué sigue. Un ejecutivo de 1 página (ver 99 para generarlo en PDF con chrome headless).
4. **La venta cierra el cliente, no tú.** Google trae el lead al WhatsApp; si el cliente no contesta o vende mal, el CPA "malo" es de él. Déjalo claro desde el día 1 y, si puedes, ayúdalo a cerrar mejor (rutea a `ventas_lushows`).
5. **Devuelve la conversión real a Google** (OCI, ver 53, 96): así el reporte muestra ventas reales, no clics, y el algoritmo optimiza bien. Es tu mejor argumento de valor y de retención.

## Lo que va en el acuerdo (aunque sea un WhatsApp, déjalo por escrito)

No necesitas un contrato de abogado para empezar, pero sí dejar estos puntos claros por escrito para no pelear después:

| Punto | Qué especificar |
|---|---|
| **Alcance** | Qué campañas manejas, qué NO (no manejas la web, ni el cierre de ventas) |
| **Quién paga el medio** | El cliente, directo a Google, con su tarjeta (ver arriba) |
| **Honorario** | Monto en COP, fijo o %, fecha y forma de pago, por adelantado |
| **Meta** | CPA o ROAS objetivo acordado (ver 64); "proceso, no garantía de ventas" |
| **Reporte** | Mensual, 1 página, qué métricas (inversión, conversiones, CPA, MER) |
| **Propiedad** | La cuenta es del cliente; tú la administras vía MCC; si se va, se la lleva |
| **Salida** | Aviso de 15–30 días; le entregas accesos y reporte final |

Esto te protege de los tres conflictos clásicos: "pensé que tú pagabas la pauta", "me prometiste ventas", y "la cuenta es mía, no tuya". Dejarlo claro al inicio vale más que cualquier cláusula sofisticada después. Para fijar el honorario con tu propia economía (cuánto te cuesta atender cada cuenta, cuántas aguantas), pásalo por `economist_lushows`.

## Errores comunes — blacklist

- **Poner tu tarjeta a pagar el gasto de medios del cliente.** Lo financias y cargas su riesgo; el error que más quiebra freelancers. La tarjeta es del cliente.
- **Crear la cuenta del cliente como si fuera tuya.** Él debe ser dueño; vincúlala a tu MCC. Si no, líos cuando se vaya (ver 04).
- **Cobrar "cuando vendamos".** No eres socio del riesgo; cobra honorario fijo/quincenal por adelantado.
- **Regalar el setup.** Montar la medición bien es trabajo real; cobra fee de montaje aparte del retainer.
- **Garantizar resultados.** Promete proceso; garantizar ventas es claim riesgoso y te quema (ver 93).
- **No definir la meta (CPA/ROAS) al inicio.** Sin número acordado, todo resultado es discutible y pierdes al cliente (ver 64).
- **Cobrar por horas.** El cliente no lo entiende y te castiga por ser eficiente; cobra por manejo/resultado.
- **Mezclar dos clientes en una cuenta** o no separar tu plata de la suya. Arruina datos, políticas y contabilidad (ver 14).
