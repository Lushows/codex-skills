# Montar Shopify en un día

> Vigencia: 14-sep-2026. Los nombres de menú de Shopify cambian; los pasos conceptuales no.

Un día de trabajo real (8 horas) basta para tener una tienda que cobra. Lo que no cabe en el día es
el texto y el video: eso va aparte y es lo que de verdad vende. `183`, `186`.

## El plan de las 8 horas

| Bloque | Tiempo | Qué se hace |
|---|---|---|
| 1. Cuenta y ajustes base | 0:45 | Alta, país, moneda, zona horaria, unidades |
| 2. Dominio y correo | 0:45 | Comprar, conectar, crear el buzón. `179` |
| 3. Tema | 0:30 | Instalar tema gratis, colores y tipografía. Nada más |
| 4. Producto y variantes | 0:45 | Producto, bundle, precios, inventario |
| 5. Pagos | 1:00 | Pasarela, prueba real, MSI si aplica. `192`, `195` |
| 6. Envíos | 0:45 | Zonas, tarifas, plazos reales |
| 7. Páginas legales | 1:00 | Envíos, devoluciones, privacidad, términos, contacto. `207` |
| 8. Checkout y notificaciones | 0:45 | Campos, correos transaccionales, abandono. `190`, `198` |
| 9. Píxel y analítica | 0:45 | Píxel, API de conversiones, GA4. `199`, `200` |
| 10. Prueba de compra real | 0:30 | Comprar con tarjeta propia de punta a punta |

## Bloque 1 — ajustes base

1. Crea la cuenta con el correo que vas a usar para siempre.
2. País de la tienda y **moneda de cobro**: MXN para México. Si cobras en dólares en México, matas
   la conversión.
3. Zona horaria local: los informes se leen mal si está en UTC.
4. Formato de peso y medidas del país.
5. Datos fiscales de la tienda: nombre, dirección, teléfono. Aparecen en las facturas y en las
   legales. Si hay duda fiscal, invoca `contador_lushows`.

## Bloque 3 — tema (la trampa de las horas perdidas)

Regla: **tema gratis, 30 minutos, y sales**. Ajusta solo tres cosas:

- Color principal y color del botón de compra.
- Tipografía (una para títulos, una para texto).
- Logo o, si no lo tienes, el nombre en texto.

No toques nada más hasta el primer pedido. El diseño fino se hace después, y cuando llegue el
momento, invoca `desingweb-lushows`.

## Bloque 4 — producto y variantes

| Campo | Cómo llenarlo |
|---|---|
| Título | El nombre del beneficio, no el del proveedor. `181` |
| Descripción | Estructura de `183`. Nunca pegues el texto de AliExpress |
| Precio | El del bundle. Precio tachado solo si es real. `189` |
| Inventario | Actívalo con la cantidad real que tienes |
| SKU | Uno por variante, te salva la vida en logística |
| Peso | Real: define la tarifa de envío |
| Variantes | El bundle como **variante por defecto seleccionada** |

## Bloque 5 — pagos (el bloque que no se puede apurar)

1. Elige la pasarela según país. `192` México, `193` LatAm, `194` Europa.
2. Sube los documentos que pidan (RFC / NIT / identificación). Esto puede tardar días: **empiézalo
   el primer día**.
3. Activa **MSI** si vendes en México y configura desde qué monto aplican. `195`.
4. Deja los métodos que la gente realmente usa. Cada método muerto en el checkout es ruido.
5. **Compra tú mismo** con tarjeta real. Si el cobro no llega a tu cuenta, no tienes tienda.

## Bloque 6 — envíos con plazos reales

Baymard: "entrega demasiado lenta" hace abandonar el checkout a **~18% de los usuarios de
inmediato**. Así que el plazo se comunica temprano y se cumple.

| Zona | Plazo que publicas | Regla |
|---|---|---|
| Ciudad principal | El real + 1 día de colchón | Nunca prometas lo que depende de un milagro |
| Resto del país | El real + 2 días | |
| Zonas remotas | Rango honesto | Mejor decirlo que sorprender |

Si el envío es gratis, dilo en el encabezado, no solo en el checkout. `181`.

## Bloque 7 — páginas legales

Escríbelas de verdad, no las generes con un clic y las dejes con marcadores sin llenar. Mínimo:
envíos y entregas, cambios y devoluciones, aviso de privacidad, términos y condiciones, contacto con
un correo del dominio. Detalle en `207`.

## Bloque 10 — la prueba de compra real

Esta es la única prueba que importa. Con tu celular, con datos móviles (no wifi), como un
desconocido:

1. Entra por el enlace del anuncio.
2. Compra el bundle con tarjeta real.
3. Verifica: cobro correcto, correo de confirmación, pedido en el panel, evento de compra en el
   píxel. `201`.
4. Emite el reembolso y verifica que también funcione.

Si algo falla aquí, no enciendas los anuncios.

## Lo que NO haces el primer día

| No lo hagas | Cuándo sí |
|---|---|
| Instalar 10 apps | Cuando una necesidad concreta lo exija |
| Diseñar el logo perfecto | Después del primer pedido |
| Escribir el blog | Nunca en este proyecto |
| Configurar multi-idioma | `206`, y solo si un mercado ya funciona |
| Retocar el tema | Después de leer `204` con datos reales |

## Relacionados
`176` elegir plataforma · `179` dominio y correo · `190` checkout · `192` pasarelas México · `208` lista de verificación
