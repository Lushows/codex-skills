# 164 — Email y newsletter de marca

El email es el canal más subestimado y, a la vez, el de mayor retorno: es el único lugar donde la marca llega directo, sin algoritmo de por medio. Pero diseñar para email es diseñar **con las manos atadas**: los clientes de correo (Gmail, Outlook, Apple Mail) renderizan HTML de forma vieja e inconsistente, muchos bloquean fuentes y a veces las imágenes. Un email de marca bien hecho se ve fiel a la identidad, carga rápido, se lee aunque se bloqueen imágenes y funciona perfecto en el móvil donde se abre la mayoría.

Términos en simple:
- **Newsletter**: correo periódico de contenido/novedades a suscriptores.
- **Preheader**: el texto que se ve junto al asunto en la bandeja, antes de abrir. Es un segundo titular.
- **Modo oscuro**: muchos leen el correo con fondo negro; tu diseño debe sobrevivir a eso.
- **Fuente de respaldo (fallback)**: la fuente que se muestra si la de marca no carga.

## Las limitaciones técnicas (que mandan en el diseño)

| Limitación | Consecuencia de diseño |
|---|---|
| Outlook usa motor de Word | Layouts con tablas, no CSS moderno; nada de flexbox/grid |
| Fuentes web a veces no cargan | Define fallback web-safe (Arial, Georgia, etc.) |
| Imágenes a veces bloqueadas | El mensaje debe entenderse SIN imágenes (texto real, no todo imagen) |
| Modo oscuro variable | Evita texto negro puro sobre fondo que se invierte raro |
| Ancho seguro | Cuerpo de **600px** máximo |

Regla de oro: **nunca pongas el mensaje principal solo dentro de una imagen.** Si se bloquea, el correo queda vacío.

## Estructura de un email de marca

1. **Preheader** (oculto/discreto): 40–90 caracteres que complementan el asunto.
2. **Cabecera**: logo (~120–160px), sobre fondo de marca o neutro.
3. **Bloque principal**: una idea, un titular, una imagen.
4. **CTA único y claro**: botón "bulletproof" (con fondo de color, no imagen), verbo de acción (ver 161).
5. **Bloques secundarios** (si aplica): jerarquía descendente.
6. **Footer**: datos del negocio, redes, y **link de desuscripción** (obligatorio por ley en muchos países).

## Jerarquía: una idea por correo

El error más común es meter 8 mensajes en un solo email. Funciona mejor: **un objetivo, un CTA principal.** Si hay varios temas, jerarquízalos —el principal grande arriba, los demás como bloques menores—. La gente escanea, no lee (ver 52 layout).

## Marca en la bandeja de entrada (antes de abrir)

La marca empieza ANTES de abrir el correo:
- **Nombre del remitente** reconocible ("BIO-SETA", no "noreply@...").
- **Asunto** con voz de marca (ver 14), claro, sin clickbait barato.
- **Preheader** que suma, no que repite el asunto.

Estas tres líneas deciden si lo abren. El mejor diseño interno no sirve si nadie abre.

## Tipografía y color en email

- Cuerpo legible: **16px** mínimo, line-height generoso.
- Fuente de marca con fallback declarado: `font-family: 'Marca', Arial, sans-serif`.
- Color de acento de marca en el botón CTA.
- Contraste alto; cuidado con grises claros (ver 35).
- Botón CTA "bulletproof": fondo de color con texto, no una imagen-botón.

## Tipos de email y su diseño

| Tipo | Objetivo | Diseño |
|---|---|---|
| Bienvenida | Primera impresión | Cálido, una promesa, un CTA |
| Newsletter | Relación, contenido | Varios bloques jerarquizados |
| Promocional | Venta | Foto de producto, precio, CTA fuerte (ver 163) |
| Transaccional (confirmación) | Informar | Sobrio, datos claros, marca discreta |
| Carrito abandonado | Recuperar venta | Producto + recordatorio + CTA |

## Móvil primero

La mayoría abre el correo en el teléfono. Diseña a 1 columna, botones grandes (≥44px), texto ≥16px, imágenes que escalan. Lo que se ve apretado en móvil pierde aperturas y clics.

## Errores frecuentes

- Email que es una sola imagen gigante → se bloquea y queda vacío; pesa mucho.
- Sin fallback de fuente → texto roto en Outlook.
- 8 mensajes y 6 botones compitiendo.
- Remitente "noreply" sin nombre de marca.
- Sin link de desuscripción → ilegal y daña reputación de envío.
- Texto negro puro que se ve mal en modo oscuro.

## Mini-checklist

- [ ] El mensaje se entiende SIN imágenes (texto real)
- [ ] Cuerpo a 600px, móvil a 1 columna
- [ ] Fuente de marca con fallback declarado
- [ ] Un objetivo, un CTA principal "bulletproof"
- [ ] Remitente, asunto y preheader con marca
- [ ] Footer con datos y link de desuscripción

**Siguiente paso**: del correo a la presencia diaria — cómo sostener un sistema de redes coherente y escalable sin aburrir (ver 165 social media a escala).
