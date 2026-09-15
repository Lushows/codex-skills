# 27 — Versiones y variantes

Un logo no es **un** archivo: es un **sistema** de versiones. El logo principal no cabe en un favicon cuadrado, ni se ve sobre fondo negro, ni en una factura a blanco y negro. Entregar una sola versión es entregar el trabajo a medias. Esto es lo que un sistema completo debe incluir.

## Por qué se necesitan varias versiones

El logo vive en contextos que tienen formas, fondos y tamaños distintos:
- Avatar de WhatsApp / Instagram → **cuadrado**, pequeño.
- Favicon del dashboard → **16–32px**.
- Encabezado web → **horizontal**, ancho.
- Etiqueta de frasco impresa a un color → **monocromo**.
- Sobre foto oscura → versión en **blanco**.

Una sola versión nunca cubre todo. Por eso se diseña un **sistema**.

## Las versiones del sistema

| Versión | Qué es | Dónde se usa |
|---|---|---|
| **Principal (primaria)** | La composición preferida, completa, óptima. | Web, papelería, presentaciones |
| **Secundaria / horizontal** | Reacomodo (símbolo a la izquierda, texto a la derecha) para espacios anchos y bajos. | Encabezados web, firmas de correo |
| **Vertical / apilada** | Símbolo arriba, texto abajo. Para espacios altos y angostos. | Banners verticales, bolsas |
| **Isotipo solo** | Solo el símbolo, sin texto. | Avatar, favicon, app, marca de agua |
| **Logotipo solo** | Solo el nombre, sin símbolo. | Cuando el símbolo no aporta o no cabe |
| **Monocromo positivo** | Todo en negro (un solo color) sobre fondo claro. | Sellos, grabado, fax, impresión a 1 tinta |
| **Monocromo negativo** | Todo en blanco sobre fondo oscuro/color/foto. | Fondos oscuros, fotos |
| **Favicon** | Símbolo simplificado a 16/32px. | Pestaña del navegador |
| **Responsive** | Versiones progresivamente simplificadas según el tamaño. | App, pantallas chicas |

> Tener un **imagotipo** (símbolo + texto separables, ver 20) te regala este sistema casi gratis: ya puedes usar el símbolo solo, el texto solo, o juntos en horizontal/vertical. Un isologo fundido te complica esto — otra razón para preferir imagotipo en marcas nuevas.

## Positivo y negativo: la regla del monocromo

- **Positivo** = logo oscuro sobre fondo claro.
- **Negativo** (o "en reserva") = logo claro/blanco sobre fondo oscuro.

**Regla de oro:** el logo debe funcionar a **un solo color**. Si solo se entiende a todo color o con degradado, está mal resuelto (ver 26). Diseña siempre la versión de una tinta; si esa funciona, la de color también.

## Logo responsive (la lección de Chermayeff)

Igual que una web se adapta al tamaño de pantalla, un logo debe **simplificarse** a medida que se achica. No metas el logo completo en 16px: a esa escala los detalles se vuelven barro.

```
Grande   → símbolo detallado + nombre completo + tagline
Mediano  → símbolo + nombre
Pequeño  → símbolo simplificado
Mínimo   → inicial o forma esencial
```

Ejemplo célebre: la rosa de **Chanel** o el monograma se reducen a las dos "C". Heineken simplifica la etiqueta a la estrella. Diseña 2–3 niveles de detalle, no uno solo estirado/encogido.

## Ejemplo trabajado: sistema de BIO-SETA
1. **Principal:** isotipo (hongo) + "BIO-SETA" + tagline opcional.
2. **Horizontal:** hongo a la izquierda, nombre a la derecha (para el encabezado del dashboard).
3. **Vertical:** hongo arriba, nombre abajo (para bolsa/etiqueta alta).
4. **Isotipo solo:** el hongo → avatar de WhatsApp y app.
5. **Favicon:** sombrero del hongo simplificado a 16px (sin el tallo si no se lee).
6. **Monocromo positivo:** todo verde oscuro/negro a 1 tinta para grabado en frasco.
7. **Monocromo negativo:** todo blanco para fondo verde oscuro o foto del producto.

## Formatos de archivo a entregar
- **Vector:** SVG y PDF (escalan sin pixelarse — indispensables).
- **Raster:** PNG con fondo transparente, en varios tamaños (favicon 16/32/48, redes 512×512).
- **Favicon:** .ico o PNG según plataforma.
- Carpeta ordenada: `/principal`, `/horizontal`, `/isotipo`, `/monocromo`, `/favicon`, cada una con sus formatos.

## Checklist del sistema
- [ ] ¿Tengo principal, horizontal y vertical?
- [ ] ¿Isotipo solo para avatar/favicon?
- [ ] ¿Monocromo positivo y negativo?
- [ ] ¿Funciona a 1 solo color?
- [ ] ¿Versión responsive simplificada para tamaños chicos?
- [ ] ¿Todos los archivos en vector (SVG/PDF) + PNG transparente?

## Errores comunes
- [ ] Entregar solo el PNG a color y nada más.
- [ ] Estirar/encoger el logo completo en vez de simplificarlo (favicon ilegible).
- [ ] No tener versión blanca → el logo desaparece sobre fondos oscuros.
- [ ] Mezclar versiones al azar sin regla de cuándo usar cuál (eso se define en 28).

## Siguiente paso
Arma la carpeta del sistema con todas las versiones y formatos. Luego define las **reglas de uso** (área de seguridad, tamaño mínimo, fondos permitidos, qué no hacer) en 28.
