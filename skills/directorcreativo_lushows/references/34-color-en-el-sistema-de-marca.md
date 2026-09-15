# 34 — Color en el sistema de marca

Tener una paleta bonita no basta: hay que GOBERNARLA para que el color sea consistente en cada pieza, cada soporte y cada persona que toca la marca. Aquí está cómo convertir colores en un sistema con roles, nombres y reglas que aguanta el crecimiento.

## El color es un activo de marca
Las marcas más fuertes son DUEÑAS de un color: el cliente lo reconoce antes de leer el nombre. Tiffany registró su robin-egg blue (**Tiffany Blue 1837**, Pantone propio), Cadbury su púrpura (2685 C), T-Mobile su magenta, UPS su marrón, Coca-Cola su rojo. La consistencia obsesiva es lo que crea ese activo. Color inconsistente = marca que no se fija en la memoria.

## Roles del color (funciones, no solo decoración)
Define qué TRABAJO hace cada color en el sistema:
- **Color de identidad** — el primario; "es la marca". Logo y elementos clave.
- **Colores de apoyo** — secundarios; dan variedad sin diluir.
- **Color de acción** — el acento reservado a botones/CTAs. Si lo usas decorativo, pierdes su poder de "haz clic aquí".
- **Superficies/fondos** — neutros que sostienen todo.
- **Texto** — escala de neutros para jerarquía de lectura.
- **Estados** (digital) — éxito/error/aviso/info. Funcionales, NO decorativos.

## Color tokens (nombres semánticos) — la clave de la consistencia
Un **token** es un nombre con significado que apunta a un color, en vez de usar el HEX suelto. Es la diferencia entre un sistema escalable y un caos.

**Mal (por valor):**
```
botón: #2E7D32
título: #2E7D32
borde: #2E7D32
```
Si cambias el verde, debes cazar cada `#2E7D32` a mano.

**Bien (por rol, en dos capas):**
```
// Capa 1 — tokens base (la paleta cruda)
color-verde-600: #2E7D32
color-gris-900:  #14160F

// Capa 2 — tokens semánticos (el ROL)
color-primario:        → color-verde-600
color-accion:          → color-ambar-500
color-texto-principal: → color-gris-900
color-fondo:           → color-blanco
color-error:           → color-rojo-500
```
Cambias el primario en UN lugar y se actualiza toda la marca. Así trabajan los design systems modernos (la lógica detrás de Material, etc.).

### Convención de nombres recomendada
- **Base:** `color-[matiz]-[peso]` → `color-verde-600` (peso 50=clarísimo, 900=oscurísimo, estilo escala).
- **Semántico:** `color-[rol]` → `color-primario`, `color-accion`, `color-texto`, `color-borde`, `color-superficie`, `color-exito`.
- Nombres en términos de FUNCIÓN, nunca de apariencia ("color-accion", no "color-naranja"; mañana el acento podría volverse otro matiz).

## Color en distintos soportes (consistencia multi-medio)
El mismo color de marca debe definirse para cada contexto (ver 32):
| Soporte | Define en |
|---|---|
| Web / app / redes | HEX / RGB |
| Folletos, tarjetas, empaque | CMYK |
| Color crítico impreso | Pantone C/U |
| Tela / bordado | Pantone textil (TCX) |
| Pintura / pared / rótulo | Pantone como referencia → mezcla |
| Vinilo / señalización | Referencia de catálogo del proveedor |

Documenta los equivalentes en el manual para que NADIE improvise.

## Modo claro y modo oscuro
Si la marca vive en digital, define la paleta para AMBOS modos:
- No inviertas colores a lo bruto. El primario suele necesitar una variante más luminosa en fondo oscuro para mantener contraste (ver 35).
- Tokens semánticos facilitan esto: `color-fondo` y `color-texto` cambian de valor según el modo, el resto del sistema no se entera.

## Gobernanza del color (reglas que evitan el caos)
1. **Una sola fuente de verdad**: un archivo/figma con la paleta oficial. Todo sale de ahí.
2. **Reglas de uso explícitas**: "el acento SOLO en CTAs", "nunca texto de marca sobre fondos saturados", "máximo 3 colores por pieza".
3. **Ejemplos de SÍ y NO** en el manual: muestra usos correctos e incorrectos lado a lado.
4. **Tolerancia definida**: especifica Pantone para que proveedores no "interpreten" el color.
5. **Revisión**: alguien aprueba que las piezas cumplan la paleta antes de publicar.
6. **Accesibilidad como requisito**, no opción (ver 35): cada combinación texto/fondo aprobada cumple contraste.

## Errores típicos
- [ ] Usar HEX sueltos por todas partes → imposible mantener al crecer.
- [ ] Nombrar tokens por apariencia ("verde") en vez de rol ("primario").
- [ ] Quemar el acento en decoración → pierde su función de acción.
- [ ] No definir equivalentes por soporte → cada proveedor inventa su versión.
- [ ] Sin reglas de uso → cada diseñador aplica la paleta a su gusto.
- [ ] Olvidar el modo oscuro hasta que es tarde.

## Mini-checklist
- [ ] Cada color tiene un ROL definido en el sistema.
- [ ] Uso tokens semánticos (base + rol), no HEX sueltos.
- [ ] Definí equivalentes para cada soporte (digital, print, textil...).
- [ ] Hay reglas de uso escritas con ejemplos SÍ/NO.
- [ ] Existe una única fuente de verdad de la paleta.
- [ ] El acento está reservado a la acción.

**Siguiente paso:** valida que cada combinación de tu sistema sea legible y accesible para todos en 35.
