# El checkout que no pierde ventas

> Vigencia: 14-sep-2026.

El checkout es donde muere el dinero que ya pagaste por traer. Cada peso invertido en arreglarlo
rinde más que cualquier optimización del anuncio, porque actúa sobre gente que **ya decidió
comprar**.

## Por qué abandonan

| Causa | Qué hacer |
|---|---|
| Costos inesperados (envío, impuestos, comisión) | Muestra el total real desde la página de producto |
| **"Entrega demasiado lenta"** — ~18% abandona de inmediato (Baymard) | Plazo visible antes del checkout y en el checkout |
| Obligan a crear cuenta | Invitado siempre. La cuenta se ofrece después de pagar |
| Formulario largo | Recorta campos. Ver más abajo |
| No confían en el sitio | Sellos de pago, política visible, correo del dominio. `197` |
| No está su método de pago | `192`, `193`, `194` |
| Errores o lentitud | `196` |
| Solo estaban comparando | Recuperación por correo y remarketing. `198` |

## Los campos que de verdad necesitas

| Campo | ¿Obligatorio? |
|---|---|
| Correo | Sí. Es tu único canal de recuperación |
| Nombre y apellido | Sí |
| Teléfono | Sí en LatAm: la transportadora lo exige |
| Calle y número | Sí |
| Colonia / barrio | Sí en México |
| Código postal | Sí. Autocompleta estado y ciudad con él |
| Ciudad y estado | Sí, pero **autocompletados** |
| Referencias de entrega | Opcional, pero súbelo: reduce entregas fallidas |
| Empresa | No. Quítalo |
| Segunda línea de dirección | No como campo separado; opcional |
| RFC / datos de factura | **Opcional y después de pagar**, nunca en el flujo principal |

Regla: cada campo que quitas sube la conversión. Cada campo que dejas tiene que justificar su
existencia en una frase.

## Las 12 reglas del checkout

1. **Invitado por defecto.** Nada de "crea tu cuenta para continuar".
2. **Un solo paso si la plataforma lo permite**, o pasos claramente numerados.
3. **Móvil primero**: teclado numérico para teléfono y código postal, autocompletado del navegador
   habilitado, campos grandes.
4. **Total visible siempre**, actualizándose en vivo.
5. **Sin sorpresas**: si hay costo de envío, ya lo sabía desde la página de producto.
6. **Resumen del pedido visible** con la miniatura del producto. Recuerda qué está comprando.
7. **Plazo de entrega repetido** dentro del checkout.
8. **Garantía repetida** junto al botón de pago. `188`.
9. **Sellos de pago** visibles: los logos de las tarjetas y de la pasarela.
10. **Sin menú ni enlaces de salida.** El checkout no tiene navegación.
11. **Errores en línea y en español claro**: "Falta el código postal", no "Error 400".
12. **Botón que dice lo que hace**: `Pagar 1.099 MXN`, no `Continuar`.

## El texto del checkout (listo para copiar)

| Lugar | Texto |
|---|---|
| Encabezado del checkout | `Falta poco. Llena tus datos de envío.` |
| Sobre el campo de correo | `Te mandamos la confirmación y la guía aquí.` |
| Junto al teléfono | `Solo lo usa la paquetería para entregarte.` |
| Bajo el resumen | `Llega en 2 a 4 días hábiles. Envío gratis.` |
| Junto al botón de pago | `Pago seguro. Garantía de 30 días: si no te sirve, te devolvemos tu dinero.` |
| Botón | `Pagar 1.099 MXN` |
| Si hay MSI | `Elige 3, 6, 9 o 12 meses sin intereses en el siguiente paso.` `195` |
| Página de gracias | `¡Listo! Tu pedido quedó confirmado. Te llega en 2 a 4 días hábiles y te mandamos la guía por correo y WhatsApp apenas salga.` |

## Lo que nunca va en el checkout

| Elemento | Por qué |
|---|---|
| Campo de cupón grande y visible | Manda al cliente a Google a buscar un cupón y no vuelve |
| Menú de navegación | Fuga |
| Pop-ups | Interrupción en el peor momento |
| Chat flotante que tapa el botón en móvil | Cuesta ventas medibles |
| Upsells que confunden antes de cobrar | El upsell va **después** del pago |
| Casilla de suscripción marcada por defecto | Ilegal en varios países y mala señal |

### El cupón
Si tu plataforma no deja esconder el campo, hazlo pequeño, en texto, plegado: `¿Tienes un código?`.
Y no menciones cupones en ningún lado si no los estás repartiendo.

## Upsell y order bump: dónde sí

| Momento | Qué ofrecer | Riesgo |
|---|---|---|
| En la página de producto | El bundle como opción preseleccionada. `180` | Ninguno |
| **Order bump** (casilla dentro del checkout) | Accesorio barato, sin desmarcar nada por defecto | Bajo |
| **Post-compra** (después de cobrar) | La segunda unidad, el complemento | Cero: la venta ya está hecha |

El upsell post-compra es dinero gratis: no toca la conversión porque ya cobraste. Si vas a hacer
uno solo, haz ese.

## Los correos transaccionales

Se configuran una vez y trabajan para siempre.

| Correo | Cuándo | Qué debe decir |
|---|---|---|
| Confirmación | Inmediato | Qué compró, cuánto pagó, cuándo llega, cómo contactarte |
| Pedido enviado | Al generar guía | Número de guía + enlace de rastreo + plazo |
| En reparto | Si la transportadora lo avisa | Reduce entregas fallidas |
| Entregado + reseña | 7 días después | Pide la reseña con foto. `185` |

Todos con remitente del dominio y con SPF/DKIM/DMARC configurados, o caen en spam. `179`.

## Prueba obligatoria antes de encender los anuncios

1. Compra real con tarjeta propia, desde el celular, con datos móviles.
2. Cronometra: del clic en "Comprar" al pago confirmado. **Si pasa de 90 segundos, sobra algo.**
3. Verifica que llegue el correo de confirmación y que no caiga en spam.
4. Verifica el evento de compra en el píxel. `201`.
5. Reembolsa y verifica que el reembolso también funcione.
6. Repite con otro método de pago y con MSI.

## Relacionados
`187` FAQ · `191` formulario COD · `192` pasarelas México · `195` MSI · `198` carrito abandonado
