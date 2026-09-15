# 122 — Figma avanzado

Figma es, a 2026, la herramienta donde vive casi todo design system del mundo. Saber dibujar en Figma es básico; saber **construir un sistema** en Figma —con variables, modes, auto-layout y components— es lo que convierte un archivo bonito en una fábrica de pantallas. Este módulo es el flujo profesional, explicado para que entiendas qué hace cada pieza y por qué.

## El cambio de mentalidad
Principiante: dibuja cada pantalla a mano, copia y pega botones.
Profesional: construye **una vez** el botón, lo reutiliza, y al editarlo se actualiza en 200 pantallas. Figma premia la pereza inteligente: invertir al inicio para no repetir nunca.

## Variables (los tokens dentro de Figma)
Las **variables** de Figma son design tokens nativos: valores con nombre que reutilizas. Cuatro tipos: color, número, texto y booleano.
- `color/action` = #1B5E20
- `space/md` = 16
- `radius/button` = 12

Ventaja sobre los viejos "estilos": las variables se pueden **referenciar entre sí** (semántico → primitivo, ver 121) y agrupar en colecciones. Conéctalas a tu JSON de tokens con el plugin **Tokens Studio** para que Figma y el código compartan la misma verdad.

## Modes (la pieza que desbloquea theming)
Un **mode** es una variante de los valores de una misma variable. Una variable `color/bg` puede tener:
- mode **Claro** → blanco
- mode **Oscuro** → casi negro

Cambias el mode de un frame entero y todo se reviste solo. Mismo mecanismo sirve para **multi-marca**: mode "Marca A" / "Marca B" (ver 125). Esto es lo más potente de Figma para sistemas: theming real sin duplicar pantallas.

## Auto-layout (maquetar como lo hace el código)
**Auto-layout** hace que los elementos se acomoden solos: defines dirección (fila/columna), espacio entre ítems y padding, y Figma reordena al cambiar contenido. Es la forma de diseñar como piensa el navegador (flexbox).
- Un botón con auto-layout crece si el texto es más largo, sin romperse.
- Una tarjeta empuja su contenido al agregar una línea.
- Usa variables de `space/` como gap y padding → espaciado consistente y editable.

Sin auto-layout, cada cambio de texto te obliga a reacomodar a mano. Con él, el diseño se comporta como el producto final (clave para el handoff, ver 127).

## Components y variants (el corazón reutilizable)
- Un **component** es una pieza maestra. Sus copias son **instances**: editas el maestro, cambian todas.
- **Variants** agrupan los estados de un componente en uno solo, controlado por propiedades:

| Propiedad | Opciones |
|---|---|
| Tipo | primary / secondary / ghost |
| Tamaño | sm / md / lg |
| Estado | default / hover / disabled |

Así un solo "Botón" cubre decenas de combinaciones desde un panel de propiedades. Añade **component properties** (texto editable, mostrar/ocultar icono, swap de icono) para que una instancia se adapte sin desconectarse del maestro.

## Libraries (compartir el sistema)
Una **library** (biblioteca) publica tus components, variables y estilos para que otros archivos los usen. Flujo típico:
```
Archivo "Design System" (la fuente)  →  publica library
        ↓ se consume en
Archivo "Producto / Pantallas"       →  usa los componentes
```
Cuando actualizas el sistema, los archivos que lo consumen reciben aviso de actualización. Una marca, muchos proyectos, un solo origen (ver 124 para gobernanza).

## Dev Mode (el puente a código)
**Dev Mode** es la vista para programadores: inspeccionan medidas, colores (como tokens), tipografías y exportan assets sin tocar el diseño. Si conectaste variables a tokens, el dev ve `color/action` en vez de un hex suelto → habla el mismo idioma que el sistema (ver 127). Marca "ready for dev" en los frames listos para que el equipo sepa qué entregar.

## Flujo profesional a 2026 (orden recomendado)
1. Define **variables** (tokens) con sus **modes** (temas/marcas).
2. Construye **components** base con **variants** y **auto-layout**.
3. Arma patrones combinando componentes.
4. Diseña pantallas solo con instancias (nunca dibujes un botón a mano de nuevo).
5. Publica como **library**.
6. Entrega por **Dev Mode** marcando frames listos.

## Errores comunes
- Estilos sueltos en vez de variables → no hay theming ni referencias.
- Botones "detached" (desconectados del maestro) → la actualización no llega.
- Cero auto-layout → todo se rompe al cambiar texto/idioma.
- Mil variants innecesarias → simplifica a las que de verdad existen.
- No publicar library → cada quien copia y el sistema se fragmenta.

## Para Lushows (no técnico)
No necesitas dominar todo. El 80% del valor: **variables de color/espacio + auto-layout + un componente de botón con variants**. Con eso ya construyes pantallas coherentes y editables. Lo demás se suma cuando el proyecto crece.

## Mini-checklist
- [ ] Variables por rol, con modes (claro/oscuro o marcas)
- [ ] Components con variants y properties
- [ ] Auto-layout usando variables de espacio
- [ ] Library publicada como fuente única
- [ ] Frames marcados "ready for dev" en Dev Mode
- [ ] (Pro) Tokens Studio conectando a JSON

**Siguiente paso**: un sistema sin documentación se olvida. Pasa a 123 documentación viva para que el equipo sepa cómo y cuándo usar cada pieza.
