# Fraude y pedidos sospechosos

> El fraude en prepago te cuesta el producto, el flete **y** el contracargo. El fraude en COD te
> cuesta dos fletes y el tiempo. Son problemas distintos con defensas distintas. Y el error caro no
> es dejar pasar un fraude: es **cancelar pedidos buenos por paranoia**.

## Los dos mundos

| | Prepago | COD |
|---|---|---|
| Qué roban | Tu producto con una tarjeta ajena | Tu flete con un pedido falso |
| Quién paga | Tú, vía contracargo (`282`) | Tú, vía flete ida + vuelta (`163`) |
| Cuánto pesa | 0,3-1,5% de los pedidos | 10-25% de los pedidos no entregados incluyen falsos |
| Defensa principal | Filtro de señales + 3DS | **Confirmación previa** (`160`) |

## Las 12 señales en prepago

Ninguna sola condena. **Dos o más juntas** justifican verificar.

| # | Señal | Peso |
|---|---|---|
| 1 | Dirección de envío ≠ dirección de facturación | Alto |
| 2 | Varios intentos de pago con tarjetas distintas | **Muy alto** |
| 3 | Correo recién creado, cadena de números aleatorios | Medio |
| 4 | Pedido de monto mucho mayor al ticket promedio | Alto |
| 5 | Varios pedidos al mismo lugar con tarjetas distintas | **Muy alto** |
| 6 | IP de país distinto al de la dirección | Medio |
| 7 | Pide envío urgente sin importar el costo | Alto |
| 8 | Dirección de entrega es una oficina de paquetería o "casillero" | Medio |
| 9 | Nombre del titular distinto al del comprador | Medio |
| 10 | Pedido en la madrugada, primera vez, monto alto | Bajo |
| 11 | Teléfono inválido o imposible | Medio |
| 12 | El cliente presiona para que lo envíes antes de verificar | Alto |

> Cuidado con leer una señal como culpa: el envío a dirección distinta es normal en Q4 (regalos) y
> "correo raro" no significa nada. Por eso: dos señales, no una.

## El semáforo de decisión

| Nivel | Señales | Acción |
|---|---|---|
| 🟢 Verde | 0-1 señal de peso bajo | Despachar normal |
| 🟡 Amarillo | 1 alta o 2 medias | **Verificar**: llamar o escribir al cliente antes de despachar |
| 🟠 Naranja | 2 altas, o monto alto + dirección distinta | Pedir 3DS / otro medio de pago / confirmación escrita |
| 🔴 Rojo | Muy alta (2, 5) o coincidencia con lista negra propia | **Cancelar y reembolsar**, con mensaje neutro |

## Cómo verificar sin ofender

> Hola [nombre], soy [tú] de [tienda]. Tu pedido **[#1234]** está listo para salir.
>
> Como es la primera compra y el monto es alto, hacemos una verificación rápida: ¿me confirmas que
> **[últimos 4 dígitos de la tarjeta]** y la dirección **[dirección]** son correctos?
>
> Con eso lo despacho hoy mismo.

Un comprador real responde en minutos y agradece el cuidado. Un defraudador desaparece o se irrita.
**El silencio es la respuesta.**

## Cancelar sin acusar

> [nombre], no pudimos completar la verificación de tu pedido **[#1234]**, así que lo cancelamos y
> ya procesamos la devolución del 100% a tu medio de pago (llega en [X-Y] días hábiles).
>
> Si quieres volver a intentarlo, puedes hacerlo con [otro medio] y lo procesamos de inmediato.

Nunca escribas "creemos que es fraude". No lo puedes probar, y si te equivocaste acabas de perder un
cliente bueno y ganado una reseña mala.

## Herramientas

| Nivel | Qué |
|---|---|
| Incluido | El análisis de riesgo de tu plataforma (Shopify marca pedidos de riesgo alto/medio/bajo) y las señales de la pasarela (AVS, CVV, coincidencia de país) |
| Añadido | 3D Secure selectivo por monto o por señal (`282`) |
| Pagado | Apps de antifraude con reglas. Justifícalas solo cuando el fraude supere el 1% de tus pedidos |

No pagues una app antifraude con 15 pedidos al día. Revisa a mano.

## Fraude y pedidos falsos en COD

Aquí no hay tarjeta: hay direcciones inventadas, bromas, competidores y personas que pidieron y se
olvidaron. Es la razón de que la entrega sin confirmación viva en 45-60%.

| Señal en COD | Acción |
|---|---|
| Teléfono inválido o apagado tras 2 intentos | Cancelar antes de despachar |
| Dirección incompleta o imposible | Pedir corrección; si no responde, cancelar |
| Varios pedidos del mismo teléfono sin recibir ninguno | **Lista negra propia** |
| Nombre obviamente falso | Confirmar por llamada |
| Zona con tasa de entrega históricamente < 40% | Exigir prepago o anticipo del flete |

Defensas ordenadas por impacto:

| Defensa | Efecto en la tasa de entrega |
|---|---|
| Confirmación previa por WhatsApp o voz | 45-60% → 65-78% |
| Confirmación + limitar a zonas urbanas | → 70-85% |
| Lista negra propia por teléfono | Evita el reincidente |
| Anticipo del flete en pedidos de riesgo | Filtra al que no pensaba recibir |
| Segunda visita programada con el cliente | Recupera parte de los "no estaba" |

Ver `158`, `159`, `160`, `161`, `172`.

## Tu lista negra

Un archivo tuyo, no de nadie más: `teléfono · correo · dirección · motivo · fecha`. Se consulta antes
de despachar. Con 200 pedidos ya tiene valor; con 2.000 te ahorra dinero real. No compartas datos
personales de clientes con terceros: eso tiene implicaciones legales (`293`).

## El error de la paranoia

| Costo | Magnitud |
|---|---|
| Un fraude que se te cuela | 1 producto + 1 flete + comisión |
| Cancelar 10 pedidos buenos por miedo | 10 ventas + 10 clientes + reseñas malas |

**Cancelar es la opción cara.** Verificar es barato. Ordena tu proceso para verificar mucho y
cancelar poco.

## Checklist antes de despachar (pedidos 🟡 o más)

- [ ] Dirección de envío y facturación comparadas
- [ ] Teléfono con formato válido y contactado
- [ ] Búsqueda del correo/teléfono en la lista negra propia
- [ ] Monto comparado con el ticket promedio
- [ ] Intentos de pago fallidos revisados
- [ ] Respuesta del cliente recibida (o 24 h de espera cumplidas)
- [ ] Decisión registrada en el pedido

## Relacionados
`282` contracargos · `281` devoluciones · `172` fraude en COD · `160` confirmación de pedidos ·
`159` subir la tasa de entrega · `163` el costo oculto de los rechazos · `192` pasarelas ·
`293` riesgos legales
