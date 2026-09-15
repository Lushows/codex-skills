# Espiar tiendas, no solo anuncios

> Vigencia: 14-sep-2026.

## Por qué el anuncio es solo la mitad

El anuncio te dice cómo consiguen el clic. La **tienda** te dice cómo consiguen el dinero. Entre el
clic y el cobro hay: precio, bundle, upsell, garantía, prueba social, envío, método de pago. Ahí se
decide el margen, y ahí es donde el 90% de los principiantes no mira.

> Un competidor con el mismo producto y el mismo CPM que tú, pero con una tienda que convierte 3,1%
> en vez de 1,4%, tiene la mitad de tu CAC. No le ganas con creatividad: le ganas con oferta.

## Las ocho cosas que hay que sacar de cada tienda

| # | Qué | Dónde está | Módulo |
|---|---|---|---|
| 1 | Catálogo completo y orden de venta | `/collections/all?sort_by=best-selling` | `93` |
| 2 | Precio y precio tachado | Ficha de producto | `103` |
| 3 | Bundle y cantidades | Selector de variantes | `104` |
| 4 | Upsell y order bump | Carrito y checkout | `104` |
| 5 | Garantía y política de devolución | Pie de página | `104` |
| 6 | Prueba social (nº de reseñas, fechas) | Ficha de producto | `94` |
| 7 | Estructura de la landing | La página completa | `102` |
| 8 | Envío y plazos | Checkout / política de envíos | `102` |

## Procedimiento base (15 min por tienda)

1. Desde el anuncio en la biblioteca, clic al **enlace de destino**. Anota la URL final (ojo: suele
   llevar parámetros UTM que revelan el nombre de campaña del competidor; guárdalos, ver abajo).
2. Navega la landing **en móvil** (es el 90% del tráfico). Usa el modo dispositivo del navegador.
3. Captura pantalla completa de la landing. Guárdala en tu swipe file (`99`).
4. **Agrega el producto al carrito** y avanza hasta el checkout SIN pagar. Ahí aparecen los upsells,
   los order bumps y el costo de envío real.
5. Abre `/products.json` y el sitemap (`93`).
6. Llena la ficha de competidor de abajo.
7. Sal. No compres salvo que decidas la compra-espía (ver más adelante).

## Lo que revelan los parámetros UTM

Muchos anuncios llevan la URL con UTMs sin limpiar. Ejemplo de lo que puedes encontrar:

```
?utm_source=facebook&utm_medium=cpc&utm_campaign=MX-BF-VIDEO3-ABO&utm_content=hook_dolor_v2
```

De ahí sacas gratis: que segmenta México, que lo llama BF (Buen Fin), que va con ABO, que el creativo
es el video 3 y que el hook es de dolor en su versión 2. **Es la nomenclatura interna de su cuenta
publicitaria.** Guarda siempre la URL completa, no la acortada.

## Ficha de competidor (plantilla)

| Campo | Valor |
|---|---|
| Tienda / dominio | |
| Plataforma (Shopify / WooCommerce / Tiendanube / otra) | |
| Producto principal | |
| Precio simple (MXN) | |
| Precio tachado | |
| Bundle 2x / 3x y su precio | |
| Envío (gratis desde X / fijo / costo) | |
| Métodos de pago visibles | |
| **¿MSI?** ¿cuántos meses? | |
| Garantía | |
| Nº de reseñas del producto principal | |
| Fecha de la reseña más antigua / más reciente | |
| Upsell post-compra | |
| Order bump en carrito | |
| Apps visibles (contador, ruleta, chat) | |
| Nº de anuncios activos en Meta MX | |
| Anuncio activo más antiguo (fecha) | |
| Fecha de esta ficha | |

Esa última fila es obligatoria. Una ficha sin fecha no sirve dentro de un mes.

## Detectar la plataforma en 10 segundos

| Señal | Plataforma |
|---|---|
| `/cdn/shop/` en las imágenes, `/cart` y `/products/` | **Shopify** |
| `/wp-content/` | WooCommerce |
| `cdn.tiendanube.com` | Tiendanube / Nuvemshop |
| `myshopify.com` en algún enlace | Shopify sin dominio propio (operación novata) |

Saber la plataforma te dice qué trucos tienes disponibles: con Shopify tienes `/products.json` y
`/collections/all` (ver `93`), que es el 80% del valor.

## La compra-espía

Comprar UN pedido al competidor principal. Cuesta el precio del producto y te da lo que ninguna
herramienta vende:

| Lo que aprendes | Por qué importa |
|---|---|
| Plazo real de entrada | Si promete 3 días y tarda 12, esa es tu ventaja con stock local |
| Desde dónde envía | Guía con remitente en México o en China |
| Empaque y calidad real | Sabes si el producto aguanta el precio |
| Secuencia de correos post-compra | Su flujo de email y upsell, tal cual |
| Quién es el proveedor | A veces viene la factura o el remitente del proveedor |
| Experiencia de devolución | Si te atreves a devolverlo |

Con capital bajo esto se hace **una vez**, con el competidor más fuerte, y se documenta a fondo. Es
de las mejores inversiones de investigación que existen: por ~1.000 MXN aprendes su operación
completa. Ver `20`.

## Límites

- No intentes acceder a paneles, cuentas o datos privados. Eso ya no es inteligencia competitiva, es
  intrusión. Ver `106`.
- No hagas scraping agresivo de una tienda ajena. Peticiones manuales y ocasionales, sí. Ver `108`.
- No copies sus textos, fotos ni video. Ver `105`.

## Relacionados
`93` productos de una tienda Shopify · `94` estimar ventas · `102` landing pages · `103` precios · `104` oferta y bundles · `106` legalidad
