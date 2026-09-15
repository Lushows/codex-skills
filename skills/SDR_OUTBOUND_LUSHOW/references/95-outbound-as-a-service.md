# 95 — Outbound-as-a-Service (lead gen como servicio)

**Outbound-as-a-Service** —también llamado agencia de lead gen o "appointment setting"— es vender tu máquina de outbound a otras empresas: tú les consigues las reuniones calificadas y les cobras por ello. Importa porque es uno de los negocios de servicios más demandados de 2026: casi toda empresa B2B quiere pipeline pero no sabe (ni quiere) montar la infraestructura de dominios, datos, secuencias y deliverability. Si dominas el núcleo de esta skill, ya tienes el producto; falta empaquetarlo y venderlo. Este módulo es la **introducción al modelo**: qué vendes, cómo cobras a grandes rasgos y qué necesitas para arrancar. El negocio a fondo —montarlo, operar múltiples clientes, infra separada, conseguir tus propios clientes, escalar— vive en el **Bloque 19 (`190`–`199`)**.

## El principio: vendes reuniones, no esfuerzo

Tu cliente no compra "correos enviados" ni "horas de SDR": compra **reuniones calificadas con su cliente ideal en su calendario**. Ese es el producto y la promesa. Tres cosas hacen viable el modelo:

1. **La infraestructura se amortiza entre clientes.** Ya sabes montar dominios, warmup, Clay, secuencias (Bloques 2–6). El costo de aprender ya lo pagaste; ahora lo cobras muchas veces. Ojo: cada cliente necesita **su propia infra de envío** (dominios y buzones separados) para no cruzar reputaciones ni datos (ver `194`).
2. **El dolor es universal y recurrente.** Toda empresa B2B necesita pipeline **todos los meses**. Eso habilita el **retainer** (pago mensual fijo) — ingreso recurrente, como un SaaS pero de servicio (ver `92`).
3. **Es medible, así que es vendible.** Puedes prometer un rango de reuniones y mostrar los números (reply rate, reuniones agendadas; ver `80`). Un servicio medible se vende mejor que uno difuso.

## Qué incluye el servicio (el alcance típico)

| Componente | Qué haces por el cliente | Módulo |
|---|---|---|
| **ICP y lista** | Defines/afinas su ICP y construyes las listas | `10`, `20`, `21` |
| **Datos y correos** | Consigues y verificas contactos por nicho | `23`, `28` |
| **Infra de envío** | Montas dominios, buzones, warmup DEDICADOS por cliente | `41`, `43`, `194` |
| **Copy y secuencias** | Escribes y ejecutas las cadencias multicanal | `50`–`61` |
| **Ejecución y respuestas** | Corres la campaña y manejas las respuestas iniciales | `64` |
| **Agendamiento** | Pones la reunión calificada en el calendario del cliente | `69` |
| **Reporte** | Dashboard de números cada semana/mes | `80`, `144` |

**La frontera del servicio:** tú entregas la **reunión agendada y calificada**. La reunión de venta, el descubrimiento profundo y el **cierre los hace el cliente** (su vendedor). Deja esto explícito en el contrato o generas expectativas falsas ("¿por qué no cerraste?"). El arte de cerrar es de ellos — o si lo ofreces, es otro servicio y otro oficio (`ventas_lushows`).

## Los modelos de cobro (visión general)

Hay tres formas base de cobrar; el detalle y los números están en `191`:

- **Retainer mensual fijo** — cobras $X/mes por operar la máquina, sin importar resultado. Predecible para ti; el cliente asume el riesgo. Lo más común para empezar.
- **Por reunión / por SQL (pay-per-performance)** — cobras por cada reunión calificada agendada. El cliente ama el riesgo bajo; tú necesitas mucha confianza en tus números para no perder.
- **Híbrido** — un retainer base menor + un bono por reunión/reunión-mostrada. Equilibra riesgo. Suele ser el más sano.

> El **pricing estratégico** (cuánto cobrar, márgenes, en qué punto es rentable, tu propio CAC como agencia) es decisión de negocio → llévalo a `economist_lushows`, y los números exactos verifícalos con `Matematicas_lushows`. Aquí solo te doy que existen los tres modelos.

## Lo mínimo para arrancar

1. **Un nicho de cliente definido.** No "hago outbound para cualquiera": "consigo reuniones para agencias de software B2B". El meta-nicho vende (ver `12`, `192`).
2. **Tu propia máquina probada primero.** Antes de vender resultados, consíguelos para ti mismo o un primer cliente piloto. Vender lo que no has probado quema tu reputación.
3. **Infra separable por cliente.** Dominios y buzones nuevos por cada cliente (ver `194`). Nunca mezcles reputaciones.
4. **Un caso/prueba.** Aunque sea el tuyo: "así llené mi propio pipeline". La prueba abre la puerta (ver `123`).
5. **Meta-outbound:** consigues clientes para tu agencia... haciendo outbound. Eres tu propio caso de estudio viviente (ver `192`).

## Errores comunes (qué NO hacer)

- Prometer reuniones antes de tener la máquina probada. Vendes humo y quemas tu nombre.
- Compartir infra entre clientes: un cliente con lista mala hunde la reputación de todos.
- Prometer cierres ("te consigo ventas") cuando solo controlas hasta la reunión. Vende reuniones calificadas, no ventas.
- No definir "reunión calificada" en el contrato: sin criterio, discutes cada factura (ver `193`, SLAs).
- Cobrar por reunión sin conocer tus propios ratios: puedes trabajar gratis o a pérdida.

## Siguiente paso

Si esto te interesa como negocio, entra al **Bloque 19**: `190` (montar la agencia), `191` (pricing a fondo), `192` (conseguir tus clientes), `193` (SLAs), `194` (operar varios clientes). Antes, asegúrate de dominar el núcleo (una máquina que ya funciona para ti). El modelo de negocio y su viabilidad → `economist_lushows`.
