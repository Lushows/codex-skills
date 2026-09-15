# Diagnosticar una página que no convierte

> Vigencia: 14-sep-2026. Árbol de diagnóstico completo. Recórrelo **en orden**: cada paso descarta
> el siguiente.

La frase "mi página no convierte" casi nunca es cierta. En el 80% de los casos el problema está
antes (medición, tráfico, oferta) o después (checkout, pago). Este módulo encuentra el culpable real.

## PASO 0 — ¿Tienes datos suficientes?

| Sesiones en la página de producto | Veredicto |
|---|---|
| Menos de 300 | **Para aquí.** No tienes un problema de conversión, tienes falta de datos. `203` |
| 300-500 con **0** ventas | Hay algo roto. Sigue al paso 1 |
| 500+ con conversión bajo 1,5% | Sigue al paso 1 |

## PASO 1 — ¿Está roto el checkout? (5 minutos, descarta el 30% de los casos)

Haz una **compra real**, desde tu celular, con datos móviles, con tarjeta propia.

| Resultado | Diagnóstico |
|---|---|
| No pudiste completar la compra | **Ahí está el problema.** `190`, `192` |
| El pago se rechazó | Pasarela mal configurada o antifraude agresivo. `192` |
| No llegó el correo de confirmación | Entregabilidad rota. `179` |
| El total cambió respecto a lo que decía la página | Costo inesperado: causa número uno de abandono. `190` |
| Tardaste más de 90 segundos | Sobran campos o pasos. `190` |
| Todo funcionó | Sigue al paso 2 |

## PASO 2 — ¿Está rota la medición?

| Comprobación | Si falla |
|---|---|
| ¿Los pedidos del panel coinciden con los `Purchase` del píxel? | Medición rota. `201` |
| ¿El evento de compra trae valor y moneda correctos? | ROAS ficticio. `200` |
| ¿La moneda es la de cobro (MXN, no USD)? | Estás leyendo números falsos por ~18x |
| ¿Hay dos píxeles instalados? | Duplicación. `200` |
| ¿Tienes GA4 y plataforma reportando lo mismo? | Discrepancias normales bajo 15%; más que eso, investiga |

**Si la medición está rota, no puedes diagnosticar nada más. Arréglala primero.**

## PASO 3 — ¿Es el tráfico o es la página?

Mira el embudo. `199`.

| Señal | Diagnóstico | Ve a |
|---|---|---|
| Rebote altísimo, tiempo en página bajo 10 s, casi nadie baja | **Es el tráfico.** El anuncio promete otra cosa, o el público está mal | `facebook_ads_lushows` |
| La gente baja, lee, pero no añade al carrito | **Es la página** | PASO 4 |
| Añaden al carrito pero no inician checkout | **Es el costo o el plazo** | PASO 6 |
| Inician checkout y no compran | **Es el checkout o el pago** | PASO 7 |

**La prueba de la promesa rota:** pon el anuncio y el encabezado de la página uno al lado del otro.
¿Dicen lo mismo? Si el anuncio promete "adelgaza" y la página dice "masajeador cervical", la
conversión nunca va a subir. Ese desajuste es la causa más frecuente de "el tráfico no sirve".

## PASO 4 — El encabezado

Muestra una captura del encabezado en móvil a alguien que no conoce el producto. Cuatro preguntas:

| Pregunta | Si no la responde |
|---|---|
| ¿Qué es? | La promesa no comunica. `181` |
| ¿Qué gano yo? | Estás escribiendo características. `184` |
| ¿Cuánto cuesta? | El precio no se ve sin bajar |
| ¿Cuándo me llega? | Falta la frase de envío. ~18% se va por eso (Baymard) |

| Comprobación | Si falla |
|---|---|
| ¿El botón se ve sin bajar en móvil? | `181`, `196` |
| ¿La primera foto muestra el producto **en uso**? | `182` |
| ¿Hay marca de agua de proveedor? | Confianza destruida. `182` |

Si el encabezado está bien, sigue.

## PASO 5 — La oferta

Esta es la causa más común de páginas "bonitas que no venden".

| Comprobación | Si falla | Módulo |
|---|---|---|
| ¿El texto habla del dolor o del producto? | Reescribe desde el dolor | `183` |
| ¿Hay video de demostración con toma continua? | Sin prueba visual no hay creencia | `186` |
| ¿Hay prueba social con foto y nombre? | Falta credibilidad | `185` |
| ¿Hay bundle, o vendes el producto suelto? | Puede ser rentabilidad, no conversión | `195` |
| ¿La garantía está escrita con plazo y procedimiento? | Riesgo no revertido | `188` |
| ¿Hay una tabla comparativa contra la alternativa? | El cliente compara por precio y pierde | `180` |
| ¿La FAQ responde las objeciones reales? | Dudas sin resolver = abandono | `187` |

### El diagnóstico del precio
El precio es sospechoso cuando la gente llega hasta abajo, vuelve a subir al precio, y se va (se ve
en las grabaciones de sesión). Opciones, en orden:

1. **Sube el valor percibido** antes que bajar el precio: mejor bundle, mejor video, mejor garantía.
2. **Ofrece cuotas.** En México, los MSI suben la conversión de 2,2% a 3,0% sin tocar el precio.
   `195`.
3. **Baja el precio solo al final**, y solo si la utilidad lo aguanta. Con ticket de 699 MXN sin
   bundle, la utilidad cae a USD 2,63: ahí ya no hay negocio.

## PASO 6 — Del carrito al checkout

| Comprobación | Si falla |
|---|---|
| ¿El costo de envío aparece **por primera vez** en el carrito? | Sorpresa = abandono. Anúncialo arriba. `190` |
| ¿El plazo de entrega se ve antes del carrito? | `181` |
| ¿Hay impuestos o comisiones que se suman al final? | `190`, `194` |
| ¿El carrito obliga a crear cuenta? | Invitado siempre |

## PASO 7 — El checkout y el pago

| Comprobación | Si falla | Módulo |
|---|---|---|
| ¿Está el método de pago que usa tu país? | Falta PSE/Nequi/OXXO/SPEI/PIX/Bizum | `192`, `193`, `194` |
| ¿Están los MSI visibles y activos? | México pierde ~36% de conversión | `195` |
| ¿Cuántos campos tiene el formulario? | Cada uno de más cuesta | `190` |
| ¿La pasarela rechaza pagos buenos? | Antifraude agresivo | `192` |
| ¿El checkout es rápido en móvil? | `196` |

## PASO 8 — La confianza

Si todo lo anterior está bien y sigue sin convertir, el problema es que no te creen.

| Señal | Módulo |
|---|---|
| Correo de gmail en la página de contacto | `179` |
| Sin razón social ni dirección en el pie | `197` |
| Páginas legales vacías o con marcadores sin llenar | `207` |
| Contador regresivo que se reinicia | `189` |
| Sin reseñas, sin teléfono, sin nada verificable | `185`, `197` |

**La prueba definitiva:** pídele a alguien escéptico que busque razones para no comprarte. Su lista
es tu plan de trabajo.

## PASO 9 — Velocidad

| Comprobación | Módulo |
|---|---|
| ¿Cuánto tarda en móvil con datos, no wifi? | `196` |
| ¿Cuántas apps tienes instaladas? | `196` |
| ¿El contenido salta al cargar? | `196` |

## PASO 10 — Si todo está bien y aun así no vende

Entonces el problema no es la página: **es el producto o el mercado**.

| Señal | Lectura |
|---|---|
| Buena página + buen creativo + 2.000 sesiones + menos de 0,8% | El producto no tiene demanda real. `60` |
| Está saturado y todos venden más barato | Entraste tarde. `61`, `63` |
| El margen no aguanta el CAC del país | El modelo no cierra. `11`, `42` |

Esta es la conclusión que nadie quiere aceptar y la que más dinero ahorra. **Mata el producto y
prueba otro.** Un mal producto no se arregla con una buena página.

## El orden de reparación (si tienes poco tiempo)

Checkout roto (1) → medición rota (2) → desajuste anuncio-página (3) → promesa del encabezado (4) →
oferta y bundle (5) → método de pago faltante y MSI (7) → todo lo demás.

## Relacionados
`180` estructura · `190` checkout · `199` analítica · `203` conversión esperada · `209` errores que matan ventas
