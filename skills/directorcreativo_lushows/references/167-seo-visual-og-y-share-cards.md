# 167 — SEO visual, Open Graph y share cards

Cuando alguien pega el enlace de tu sitio en WhatsApp, Twitter/X, LinkedIn o Slack, aparece una **tarjeta** con imagen, título y descripción. Eso es la **Open Graph card** (OG). La mayoría de negocios la ignora y su enlace se ve como un cuadro gris roto, sin imagen, con una URL fea —justo en el momento en que alguien recomienda la marca a otros—. Cuidar cómo se ve tu marca **al compartirse** es de las acciones de mayor impacto por menos esfuerzo: es publicidad gratis que viaja sola, y o luce premium o luce abandonada.

Términos en simple:
- **Open Graph (OG)**: el estándar que define qué imagen/título/texto muestra un enlace al pegarse en redes y chats.
- **Share card / OG image**: la imagen (1200×630px) que aparece en esa tarjeta.
- **Favicon**: el iconito de la pestaña del navegador y de los favoritos.
- **Metadatos**: trozos de texto en el código de la página que las plataformas leen.

## Los activos que debes definir

| Activo | Medida (px) | Dónde aparece |
|---|---|---|
| OG image | 1200×630 | WhatsApp, X, LinkedIn, Slack, Facebook |
| Twitter/X card | 1200×628 (summary_large_image) | X |
| Favicon | 32×32 + 16×16, y 180×180 (apple-touch) | Pestaña, marcadores, pantalla inicio |
| Title (meta) | ~50–60 caracteres | Título de la tarjeta y de Google |
| Description (meta) | ~110–160 caracteres | Bajo el título en la tarjeta y Google |

## La OG image: tu mini-cartel

Es lo primero que se ve. Reglas de diseño:
- **1200×630px**, formato horizontal.
- **Logo** presente pero no protagonista solo.
- **Titular grande y legible** incluso en miniatura (en el chat se ve pequeña): texto ≥ 48px en ese lienzo.
- **Color y tipografía de marca** (ver 34, 44).
- **Zona segura**: deja margen; algunas plataformas recortan los bordes.
- **Contraste alto**: debe leerse en cualquier fondo de chat (claro/oscuro).

Evita: meter párrafos, fotos saturadas con texto encima ilegible, o dejar la imagen por defecto del sistema (gris/rota).

## Generar OG images a escala

Si tienes muchas páginas (productos, artículos), no diseñes una a mano cada vez:
- **Plantilla de OG** con zonas variables (título, foto de producto, categoría) sobre base de marca.
- Genera dinámicamente (herramientas/servicios que arman la imagen desde una plantilla + datos).
- Mantén **una sola estética** para todas: el sistema visual de marca aplicado (ver 59).

Una plantilla bien hecha = miles de share cards coherentes sin trabajo manual.

## El favicon

Pequeño pero muy visto (pestañas, marcadores). Mismo criterio que el ícono de app (ver 162):
- Un solo símbolo, sin texto.
- Legible a 16px.
- Fondo que funcione en pestañas claras y oscuras.
- Versión apple-touch (180×180) para "agregar a inicio".

## Title y description: el texto de la tarjeta

- **Title**: claro, con la marca y la promesa, no clickbait. Ej.: "BIO-SETA — Hongos funcionales para tu energía y enfoque".
- **Description**: una frase que da ganas de entrar, con voz de marca (ver 161). Distinta por página clave.
- Sin esto, las plataformas inventan texto cortado y feo de la página.

## Verificar antes de presumir

Antes de lanzar, **prueba cómo se ve realmente**:
- Pega el enlace en un chat de WhatsApp contigo mismo.
- Usa validadores (debuggers de OG de las plataformas) para forzar el refresco de la tarjeta.
- Revisa en móvil y desktop.

Las plataformas **cachean** la tarjeta: si cambias la imagen, a veces sigue mostrando la vieja hasta que la refrescas en su validador.

## Errores frecuentes

- Sin OG image → cuadro gris roto al compartir.
- OG image con texto diminuto ilegible en miniatura.
- Imagen por defecto genérica para todas las páginas.
- Sin favicon o favicon pixelado.
- Title/description vacíos → texto inventado y cortado.
- No probar: descubrir el enlace feo cuando un cliente ya lo compartió.

## Mini-checklist

- [ ] OG image 1200×630 con marca, titular legible en miniatura
- [ ] Plantilla de OG para generar a escala con estética única
- [ ] Favicon legible a 16px + apple-touch 180×180
- [ ] Title (~55c) y description (~150c) con marca y promesa
- [ ] Probado pegando el enlace en WhatsApp y validadores
- [ ] Coherente con el sistema visual del sitio (ver 160)

## Nota técnica

La implementación de metadatos OG va en el `<head>` del sitio; **desingweb-lushows** y **engineer_visualopen_lushows** cubren el cómo técnico. Aquí defines la dirección visual de las tarjetas.

**Siguiente paso**: el enlace lleva a algún lado, y ese lugar suele ser una landing — diseñar páginas de aterrizaje que convierten (ver 168 landing pages de conversión).
