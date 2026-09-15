# 82 — Identidad digital

La marca en pantalla vive en piezas diminutas y hostiles: un favicon de 16 px, un avatar circular, un banner que se recorta distinto en cada red. Adaptar la identidad a digital no es "subir el logo": es rediseñar el sistema para que sobreviva al pixel, al recorte y al modo oscuro.

## El reto del digital vs. el impreso
| | Impreso | Digital |
|---|---|---|
| Color | CMYK / Pantone | RGB / HEX |
| Resolución | 300 dpi fijo | Variable, retina 2x/3x |
| Tamaño | Controlado | Desde 16 px hasta 4K |
| Fondo | El que tú eliges | Claro y oscuro (dark mode) |
| Forma | Libre | A menudo forzada a círculo/cuadrado |

Conclusión: el logo principal casi nunca funciona tal cual en digital chico. Necesitas un **isotipo** (símbolo solo, sin texto) que aguante a tamaño mínimo.

## Las piezas digitales y sus medidas
| Pieza | Medida | Nota |
|---|---|---|
| Favicon | 16, 32, 48 px (+ .ico y 180 px apple-touch, 512 px PWA) | Solo el isotipo, simplificado |
| Avatar (perfil) | 400 × 400 px mín, cuadrado | Se ve circular en IG/WhatsApp: centra el símbolo |
| Banner IG / cover FB | FB 820 × 312, X 1500 × 500, LinkedIn 1584 × 396 | Zona segura central (se recorta en móvil) |
| OG image (link preview) | 1200 × 630 px | Lo que se ve al compartir el link |
| Logo web header | SVG (vectorial, escala perfecto) | Versión clara y oscura |

## Adaptar el logo a digital: el sistema de versiones
Una marca digital madura tiene un **escalado responsivo del propio logo**:
- **Completo**: logotipo + isotipo (web grande, header).
- **Reducido**: solo isotipo (favicon, avatar, app icon).
- **Monocromo**: una tinta (sobre foto, sobre color).
- **Negativo**: para fondo oscuro / dark mode.

Esto es lo que hace MailChimp, Spotify, Slack: el símbolo solo funciona porque fue diseñado para vivir sin el texto. Si tu isotipo no se lee a 16 px, simplifícalo (menos detalle, más contraste de forma).

## Favicon y app icon: las trampas
- A 16 px desaparece el detalle fino. Prueba el isotipo en blanco y negro a ese tamaño ANTES de aprobarlo.
- Usa SVG donde se pueda (escala infinito) + PNG en tamaños fijos para compatibilidad.
- App icon: respeta el "safe area" — iOS recorta esquinas, Android puede enmascarar a círculo o squircle. Nunca pongas detalle clave en los bordes.

## Consistencia físico ↔ digital
La misma marca debe reconocerse en la tarjeta y en el avatar. Para lograrlo:
- Mismo HEX en digital que el equivalente del CMYK impreso (especifícalos juntos, ver 87 sobre tokens).
- Misma tipografía o su equivalente web (si la impresa no es web font, define la sustituta).
- Mismo "aire" y proporción del logo.

El cliente debe poder pasar de tu tarjeta a tu Instagram a tu web sin dudar de que es la misma marca (ver 88 sobre omnicanal).

## Dark mode y fondos variables
La pantalla no controla el fondo. Diseña:
- Versión para fondo claro y para fondo oscuro.
- Si el color de marca pierde contraste en oscuro, define una variante (un verde más luminoso para dark, por ejemplo).
- Logo monocromo blanco como salvavidas universal.

## Perfiles de redes (consistencia de cuenta)
- Mismo avatar en TODAS las redes (reconocimiento).
- Mismo @usuario donde sea posible.
- Banner adaptado a cada medida pero con el mismo concepto.
- Bio con el mismo tono de voz (ver 80, sección tono).

## Web: la marca como experiencia
La web no es un folleto: es la marca interactuando. Color, tipografía, espacio y motion (ver 84) deben ser el sistema, no un tema genérico. Referentes de cómo se documenta marca para producto digital: **Material Design (Google)**, **Polaris (Shopify)**, **Carbon (IBM)**. No los copies — estúdialos para ver el nivel de rigor (ver 89 sobre design ops).

## Mini-checklist
- [ ] Isotipo que se lee a 16 px en blanco y negro
- [ ] Favicon en .ico + PNG (32/180/512) y SVG donde aplique
- [ ] Avatar centrado para recorte circular (400 px+)
- [ ] Banners con zona segura central por red
- [ ] OG image 1200×630 para previews de link
- [ ] Versión clara, oscura, monocroma y negativa del logo
- [ ] HEX coincide con el CMYK impreso equivalente
- [ ] Mismo avatar y @usuario en todas las redes

**Siguiente paso**: con la identidad digital base lista, construye el sistema de contenido recurrente — plantillas de redes escalables (ver 83) que mantengan la marca viva sin rediseñar cada post.
