# 160 — La marca en la web y los sitios

Traducir una marca a un sitio web NO es "poner el logo arriba a la izquierda y usar los colores". Es construir un **sistema visual web** donde cada decisión —el hero, los espacios, los botones, el tipo de movimiento— hace sentir lo mismo que la identidad (ver 82 identidad digital). Un sitio puede usar el logo y la paleta correctos y aun así traicionar la marca si se siente genérico, frío o desordenado. La web es, para la mayoría de negocios, el lugar donde más gente ve la marca: merece dirección de arte, no plantilla.

Términos en simple:
- **Hero**: la primera pantalla que ve el visitante (lo "above the fold", lo visible sin hacer scroll). Decide en 3 segundos si la marca se siente premium o barata.
- **Sistema visual web**: el conjunto de reglas (tipografía, espaciado, color, componentes, movimiento) que hace que todas las páginas se sientan de la misma marca.
- **Coherencia marca↔web**: que el sitio "suene" como la marca en redes, empaque y trato (ver 15 arquitectura de marca).

## El error que casi todos cometen

| Marca en web genérica | Marca en web con dirección |
|---|---|
| Logo + colores aplicados sobre una plantilla | Sistema propio construido desde la identidad |
| Hero con stock genérico y texto centrado | Hero con foto de marca, jerarquía clara, una idea |
| Tipografía por defecto (Arial, Open Sans sueltas) | La tipografía de marca, con escala definida (ver 44, 48) |
| Espaciado apretado, todo lleno | Aire intencional, ritmo (ver 53 espacio en blanco) |
| Botones de plantilla | Botones con el estilo y movimiento de la marca |

Si el sitio se vería igual cambiándole el logo a otra empresa, **no tiene marca**.

## Cómo se traduce cada activo de marca a la web

| Activo de marca | Cómo vive en web |
|---|---|
| Logo | Header (~120–180px ancho), favicon (ver 167), footer; nunca distorsionado |
| Paleta (ver 33, 34) | Color de acento en CTAs/links; neutros para fondo y texto; modo claro/oscuro |
| Tipografía | Fuente web cargada bien (woff2), escala tipográfica fluida (ver 47) |
| Personalidad/tono (ver 14) | Microcopy y voz (ver 161), ritmo del movimiento (ver 140) |
| Fotografía (ver 61) | Hero y secciones; misma dirección de imagen que el resto de la marca |
| Iconografía (ver 56) | Set coherente, no mezclar 3 estilos de íconos |

## Anatomía de un hero que sí dice la marca

Medidas de referencia (desktop):
- **Una sola idea grande**: un titular de 1 línea (máx 2), 48–72px, que diga la promesa, no "Bienvenido".
- **Subtítulo** de apoyo: 18–22px, 1–2 líneas.
- **Un CTA primario** claro (no cinco botones que compiten) (ver 168 landing).
- **Imagen o fondo** que sea de la marca, no stock anónimo.
- **Aire**: márgenes generosos; el hero no debe sentirse apretado.

Jerarquía visual: lo más importante (titular + CTA) gana en tamaño, contraste y posición. Todo lo demás cede (ver 50 composición, 52 layout).

## Sistema visual web: las 6 reglas que dan coherencia

1. **Escala tipográfica** definida (ej. 14 / 16 / 20 / 28 / 40 / 64px) y usada en TODO el sitio.
2. **Escala de espaciado** (ej. múltiplos de 8: 8/16/24/32/48/64) — nunca valores al azar.
3. **Grid** consistente (ver 51): mismo ancho de contenido, mismas columnas.
4. **Componentes** reutilizables: el botón, el card, el input se ven igual en toda página (esto es un mini design system, ver 120).
5. **Color con roles**: un acento para acción, neutros para estructura, no "decorar con todos los colores".
6. **Movimiento de marca**: mismo tipo de easing y duración en todo (ver 140) — discreto y consistente.

## Coherencia entre canales

El sitio debe sentirse hermano de Instagram, del empaque y del email. Prueba rápida: pon lado a lado el feed de la marca (ver 165), el hero del sitio y una foto del producto. ¿Parecen la misma empresa? Si no, falta sistema (ver 19 auditoría de marca).

## Errores frecuentes

- Plantilla genérica con la marca "encima" → se ve como cualquiera.
- Demasiadas fuentes, tamaños y colores → ruido, sin jerarquía.
- Hero con texto vago ("Soluciones de calidad") en vez de la promesa real.
- Logo pixelado o mal espaciado en el header (ver 28 área de seguridad).
- Foto de stock obvia que rompe la credibilidad.
- Cero aire: todo pegado, ilegible (ver 53).

## Mini-checklist

- [ ] El sitio se sentiría DISTINTO si le cambio el logo a otra empresa
- [ ] Hero con una sola idea, un CTA, foto de marca
- [ ] Escala tipográfica y de espaciado definidas y respetadas
- [ ] Componentes (botón, card, input) coherentes en todo el sitio
- [ ] Color con roles, no decoración
- [ ] Se siente hermano del feed, el empaque y el email

## Nota técnica

Para construir el sitio con calidad de élite (HTML/CSS/JS o React+Tailwind), usa la skill hermana **desingweb-lushows**: aquí defines la dirección de marca; allá se materializa la web con motion y detalle premium. Para la capa de UI/UX fina, **ui-ux-pro-max**.

**Siguiente paso**: con el sistema visual definido, baja al detalle de la voz dentro del producto — cómo habla la interfaz (ver 161 UX writing y voz en producto).
