# Dominio, correo y confianza

> Vigencia: 14-sep-2026.

El dominio y el correo son la primera prueba de que existes. Cuestan menos de USD 20 al año y
deciden si el visitante cree que le vas a entregar.

## El dominio

### Reglas de elección

| Regla | Por qué |
|---|---|
| Corto, pronunciable, fácil de escribir al oído | Se comparte por WhatsApp y se dicta por teléfono |
| **Marca, no producto** | "cortadordeverduras.com" muere cuando muere el producto. `177` |
| Sin guiones ni números | Señal universal de sitio improvisado |
| Sin marcas registradas ajenas | Te cierran la tienda y pierdes el dominio. `07` |
| Que suene bien en el idioma del mercado | En México, un nombre en inglés forzado resta |

### Qué extensión

| Extensión | Cuándo |
|---|---|
| `.com` | Siempre que esté libre. Es la que la gente asume por defecto |
| `.com.mx` / `.mx` | México, cuando el `.com` está tomado. Suma confianza local |
| `.com.co`, `.cl`, `.es` | Igual, para su país |
| `.shop`, `.store`, `.online` | Último recurso. Resta confianza: se asocian a tiendas efímeras |

Si vendes solo en México y el `.com` está tomado, **`.mx` es mejor que un `.shop`**. La señal local
vale más que la extensión genérica.

### Lo que no importa

- Que el dominio tenga la palabra clave del producto: el SEO no es tu canal. `175`.
- Pagar por un dominio de reventa a USD 2.000. Con capital bajo USD 500, es absurdo.

## El correo

**Nunca uses gmail/hotmail en la tienda.** Un `tiendaventas2026@gmail.com` en la página de contacto
destruye más confianza que un diseño feo.

| Buzón | Para qué |
|---|---|
| `hola@tudominio.com` | Contacto público, pie de página, legales |
| `pedidos@tudominio.com` | Correos transaccionales que envía la tienda |
| `soporte@tudominio.com` | Reclamos, cambios, devoluciones |

Con capital corto, uno solo (`hola@`) y alias hacia él basta.

### Autenticación de correo (lo que casi nadie hace y cuesta ventas)

Si tus correos de confirmación y de carrito abandonado caen en spam, la tienda pierde dinero en
silencio. Configura en el DNS del dominio:

| Registro | Qué hace |
|---|---|
| **SPF** | Autoriza a quién puede enviar correo en tu nombre |
| **DKIM** | Firma criptográfica que prueba que el correo es tuyo |
| **DMARC** | Le dice al receptor qué hacer si falla lo anterior |

Shopify y Tiendanube dan las instrucciones exactas en su panel. Es media hora y cambia la tasa de
entrega de los correos de recuperación. `198`.

## Las señales de confianza que sí mueven la aguja

Ordenadas por impacto real en una tienda nueva:

| Señal | Impacto | Costo |
|---|---|---|
| Plazo de entrega claro y creíble en la página | **Alto** — ~18% abandona el checkout por entrega lenta (Baymard) | 0 |
| Política de devoluciones concreta y sin letra chica | Alto | 0 |
| Correo del dominio contestado en menos de 24 h | Alto | 0 |
| Teléfono o WhatsApp de atención visible | Alto en LatAm | 0 |
| Reseñas con foto real de cliente | Alto. `185` | Tiempo |
| Dirección física y razón social en el pie | Medio-alto | 0 |
| Candado HTTPS (obligatorio, no opcional) | Su ausencia es fatal | 0 |
| Sellos de pago (logos de Visa/MC/pasarela) | Medio | 0 |
| Sellos genéricos tipo "100% seguro" inventados | **Negativo si son falsos** | — |

## El teléfono y el WhatsApp

En México y Colombia, un número visible sube la confianza de forma notoria. Dos condiciones:

1. Que alguien conteste. Un WhatsApp sin responder es peor que no ponerlo.
2. Que no te robe la venta prepago: en una tienda que cierra en la web, pon el WhatsApp en el pie y
   en la FAQ, **no** como botón flotante gigante que compite con "Comprar". Si el flujo es COD por
   WhatsApp, es al revés. `191`.

## Errores que matan la confianza en 3 segundos

| Error | Lo que lee el cliente |
|---|---|
| Fotos con marca de agua de AliExpress | "Esto lo compro más barato allá" |
| Texto con caracteres raros o mal traducido | "Esto no es de aquí" |
| Precios en dólares con tienda en español mexicano | "Me va a llegar en dos meses" |
| Contador regresivo que se reinicia al recargar | "Me están mintiendo". `189` |
| "Envío desde nuestro almacén" sin decir dónde | "China" |
| Página de contacto con formulario que no responde nadie | "Si algo sale mal, estoy solo" |

## Para el proyecto de México (diciembre 2026)

1. Dominio de marca de nicho, `.com` o `.mx`. Comprado el día 1.
2. Buzón `hola@` con SPF, DKIM y DMARC configurados el mismo día.
3. En el pie: razón social o nombre del responsable, ciudad, correo del dominio, WhatsApp de
   atención con horario.
4. Frase de stock local visible arriba: es el mayor diferencial contra la competencia que envía
   desde China. Redáctala honesta: "Enviamos desde México. Recibe en 2-4 días hábiles."

## Relacionados
`178` montar en un día · `197` sellos y políticas · `198` carrito abandonado · `207` la tienda legal · `209` errores que matan ventas
