# Contracargos y cómo prevenirlos

> El contracargo no te quita una venta: **te puede quitar el negocio**. Suficientes contracargos
> cancelan la pasarela, y sin pasarela no hay tienda prepago. No es un problema de atención al
> cliente: es un problema de supervivencia.

## Qué es exactamente

El cliente le dice a su banco "no reconozco este cargo" o "no recibí lo que compré". El banco le
devuelve el dinero y se lo quita a tu pasarela, que te lo quita a ti **más una comisión de
penalización**. Tú puedes disputarlo con evidencia; el proceso dura 30-90 días y lo decide el banco
emisor, no la pasarela.

| | Reembolso | Contracargo |
|---|---|---|
| Quién decide | Tú | El banco del comprador |
| Costo | El monto | El monto + comisión + producto perdido |
| Cuenta contra ti | No | **Sí** |
| Duración | Días | 30-90 días |
| Probabilidad de ganar | — | Baja si no tienes evidencia; media-alta con evidencia completa |

## El umbral que te cierra la cuenta

Las redes de tarjetas y las pasarelas vigilan tu **ratio de contracargos**: contracargos ÷
transacciones del mes. Los programas de monitoreo suelen activarse alrededor del **1%** y el riesgo
de cierre crece rápido por encima de eso. Verifica el umbral exacto de tu pasarela y de tu país
antes de asumir un número.

| Ratio mensual | Qué pasa |
|---|---|
| < 0,5% | Zona normal |
| 0,5-1% | Vigílalo; corrige causas |
| ≥ 1% | Programa de monitoreo, multas, retención de fondos |
| Sostenido arriba | **Cancelación de la cuenta** |

Ojo: el denominador es el volumen. En una tienda nueva con 80 pedidos al mes, **un solo contracargo
te pone en 1,25%**. Los primeros meses eres estructuralmente frágil.

## Las tres causas principales (verificado)

| Causa | Qué la dispara | Prevención |
|---|---|---|
| **1. Entrega tardía** | Plazo prometido incumplido, o expectativa de "envío rápido" que no cumples | Stock local, plazos honestos, comunicación proactiva |
| **2. Producto distinto al anunciado** | Creativo exagerado, foto engañosa, tamaño real diferente | Creativo honesto, medidas, video real |
| **3. No responder al cliente** | Escribió y nadie contestó | Respuesta < 2 h, canal visible |

Hay una cuarta de otra naturaleza: **fraude real** (tarjeta robada). Esa se previene en el filtro de
pedidos, no en la atención. Ver `283`.

## El escudo: 12 medidas concretas

| # | Medida | Ataca |
|---|---|---|
| 1 | **Stock local** en el país de venta | Entrega tardía (la causa #1) |
| 2 | Plazo publicado en la página de producto, no solo en el checkout | Entrega tardía |
| 3 | Correo/WhatsApp automático al confirmar el pedido, con plazo | Todas |
| 4 | Correo con la guía apenas se despacha (`157`) | Entrega tardía |
| 5 | Aviso proactivo si se atrasa, **antes** de que pregunte (`278` plantilla 3) | Entrega tardía |
| 6 | **Nombre en el estado de cuenta** igual al nombre de la tienda | "No reconozco el cargo" |
| 7 | Teléfono y correo visibles en la página y en el correo de confirmación | No responder |
| 8 | Respuesta < 2 h en horario hábil (`277`, `279`) | No responder |
| 9 | Fotos y video reales, con medidas y escala (`182`, `254`) | Producto distinto |
| 10 | Políticas claras y aceptadas en el checkout (`197`) | Evidencia en disputa |
| 11 | Reembolso voluntario ante la primera amenaza (`280`) | Todas |
| 12 | Prueba de entrega con firma o foto en ticket alto | Evidencia en disputa |

La medida #6 parece menor y es de las que más disputas de "no reconozco" evita: si en el estado de
cuenta aparece el nombre de tu proveedor de pagos o una razón social que el cliente nunca vio, él
honestamente no lo reconoce.

## Cómo se gana una disputa: el expediente

Cuando llega la notificación tienes un plazo corto (a menudo 7-10 días). Responde **siempre**, aunque
creas que vas a perder: no responder cuenta como aceptación y el ratio igual te pega.

Expediente completo:

| Evidencia | Por qué pesa |
|---|---|
| Número de pedido, fecha, monto, IP y correo del comprador | Identifica la transacción |
| Comprobante de autorización de la pasarela (AVS/CVV/3DS) | Prueba que fue autorizada |
| **Prueba de entrega**: guía, estado "entregado", fecha, dirección, firma o foto | Lo más determinante |
| Que la dirección de entrega coincida con la de facturación | Mata el argumento de fraude |
| Capturas de **toda** la conversación con el cliente | Prueba que respondiste |
| Términos y política de devolución aceptados en el checkout, con marca de tiempo | Prueba de acuerdo |
| Descripción y foto del producto tal como se anunció | Mata "no es lo que pedí" |

Un párrafo de resumen al inicio, en el idioma de la pasarela, con hechos y fechas. Sin emociones.

## 3D Secure: el interruptor que traslada el riesgo

Con autenticación fuerte (3DS/SCA), la responsabilidad de un contracargo por fraude pasa al banco
emisor. Cuesta algo de conversión (fricción en el pago) y no cubre contracargos por "no recibí" o
"no es lo que pedí".

| Situación | ¿Activar 3DS? |
|---|---|
| Ticket alto (> USD 100) | Sí |
| Tienda nueva con ratio subiendo | Sí |
| Pedidos con señales de fraude | Sí, selectivo |
| Volumen normal, ticket bajo, ratio sano | Selectivo, no a todo |
| Europa | Obligatorio por SCA |

## El calendario del riesgo

El contracargo llega **tarde**. Lo que vendes en Black Friday explota en enero-febrero.

| Momento | Qué pasa |
|---|---|
| 27 nov - 24 dic 2026 | Pico de ventas y de promesas de entrega |
| Enero 2027 | Llegan los estados de cuenta; sube "no reconozco el cargo" |
| Ene-feb 2027 | **Pico de contracargos** sobre un denominador de ventas que ya cayó → tu ratio se dispara |

Por eso el ratio de enero puede cerrarte la cuenta aunque diciembre haya sido excelente: menos
transacciones abajo, más contracargos arriba. **Prepararlo es parte del plan de guerra (`294`) y del
plan de enero (`295`).**

## Monitoreo mínimo

| Cada | Revisa |
|---|---|
| Día | Notificaciones de disputa nuevas (responder en 24 h) |
| Semana | Contracargos abiertos y su plazo |
| Mes | **Ratio** = contracargos ÷ transacciones, y la causa dominante |

Si el ratio pasa de 0,5%: frena la escala, arregla la causa, y considera pausar la categoría o el
creativo que la genera.

## Relacionados
`281` devoluciones · `283` fraude y pedidos sospechosos · `280` cliente molesto · `277` atención ·
`157` comunicar la entrega · `171` envío atrasado · `192` pasarelas México · `197` políticas ·
`294` temporada alta · `295` después de diciembre
