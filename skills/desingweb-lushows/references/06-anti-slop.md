# 06 — Anti-Slop: lo que NUNCA hacemos

"AI slop" es ese diseño genérico que grita "lo generó una IA en 10 segundos". Un director de arte de élite reconoce esos patrones de inmediato y los elimina. Esta es la lista negra. Si tu diseño contiene cualquiera de estos, vuelve atrás y arréglalo antes de entregar.

## Lista negra de anti-patrones

- **Gradiente morado→azul (#7C3AED → #2563EB) sobre fondo blanco.** Es la firma visual del slop. Si necesitas un gradiente, derívalo de la paleta de marca y baja la saturación; mejor aún, usa color plano o un gradiente sutil tono-sobre-tono.
- **Tipografía Inter / Roboto / Arial por defecto** sin decisión consciente. Elige un display con carácter (Fraunces, Clash, Space Grotesk, una serif editorial) y reserva la sans neutra solo para cuerpo, ajustando tracking y line-height.
- **Hero centrado genérico** con título, subtítulo de una frase y un solo botón flotando en el vacío. Rompe la simetría: asimetría editorial, imagen a sangre, dato fuerte, o layout en dos columnas con tensión.
- **Cards idénticas en grid de 3 columnas** sin jerarquía: misma altura, mismo peso, mismo icono. Da jerarquía — una card destacada, tamaños distintos (bento), o convierte el grid en una lista con ritmo.
- **Emojis usados como iconos** de UI (🚀 ✨ 💡 en features). Usa un set de iconos coherente (Lucide, Phosphor) o ilustración propia; los emojis renderizan distinto en cada SO y abaratan la pieza.
- **`box-shadow` por defecto de Tailwind** (`shadow-md`, `shadow-lg`) sin tunear. Las sombras genéricas se ven planas y grises. Diseña sombras con color del fondo, capas múltiples y blur intencional, o elimina la sombra y usa borde/contraste.
- **"Lorem ipsum" sin reemplazar** en la entrega. Escribe copy real y específico de la marca; el texto placeholder mata la credibilidad y oculta problemas de longitud.
- **Iconos de stock incoherentes**, mezclando estilos (outline + filled + 3D) de librerías distintas. Un solo set, un solo grosor de línea, un solo estilo.
- **`transition: all`.** Anima propiedades explícitas (`transform`, `opacity`, `background-color`). `all` provoca jank, anima cosas que no querías y arruina el rendimiento.
- **`border: 1px solid #E5E7EB` (border-gray-200) por todos lados** delimitando cada caja. El borde gris omnipresente es slop puro. Separa con espacio, fondo o sombra; reserva los bordes para donde aportan estructura real.
- **Secciones Features / Testimonials / Pricing calcadas** del mismo template de siempre, en el mismo orden, sin personalidad. Reordena, fusiona, inventa una sección propia de la marca; que la estructura cuente una historia.
- **Texto gris claro (#9CA3AF) sobre blanco** con contraste pobre que no pasa AA. El cuerpo va en un gris profundo (#1F2937 o más oscuro); el gris claro solo para metadatos diminutos, nunca para contenido legible.
- **Falta de dark mode** cuando la audiencia o el sector lo esperan (dev-tools, SaaS, cripto), o peor, un dark mode que es solo `invert` sin recalibrar contrastes y sombras.
- **Espaciado inconsistente**: 13px aquí, 27px allá, 19px más abajo. Usa una escala (4/8px) y respétala religiosamente; la consistencia del ritmo vertical es lo que separa pro de amateur.
- **Ausencia de estados `:focus` visibles** (o un `outline: none` sin reemplazo). Cada elemento interactivo necesita un focus ring claro para teclado; quitarlo es un fallo de accesibilidad, no una decisión estética.
- **Botón con `border-radius` gigante tipo píldora + sombra azul difusa** por defecto, idéntico al de cualquier plantilla. Define un radio coherente con la marca y aplícalo a todo el sistema.
- **Animaciones de entrada genéricas** (todo hace fade-up al hacer scroll, con el mismo delay). Si todo se mueve igual, nada destaca; reserva el motion para 1-2 momentos memorables.
- **Paleta de un solo azul corporativo** (#3B82F6) sin acento ni neutros cálidos. Construye paleta completa: fondo, superficie, texto, primario, acento, y al menos un neutro con temperatura.
- **Fondo blanco puro #FFFFFF + texto negro puro #000000.** El contraste duro cansa la vista; usa un off-white (#FAFAF7) y un casi-negro (#111).

## Checklist antes de entregar

- [ ] No hay gradiente morado→azul ni paleta default; los colores salen de la marca.
- [ ] La tipografía display tiene carácter y no es Inter/Roboto/Arial por inercia.
- [ ] El hero NO es el patrón centrado genérico; tiene tensión o un elemento memorable.
- [ ] Ningún `transition: all` ni sombras Tailwind sin tunear en el código.
- [ ] Cero "Lorem ipsum": todo el copy es real y específico de la marca.
- [ ] Bordes gris-200 minimizados; la separación viene de espacio, fondo o sombra intencional.
- [ ] Contraste de texto verificado AA (sin grises claros ilegibles sobre blanco).
- [ ] Estados `:focus` visibles en todo elemento interactivo y navegable por teclado.
- [ ] Espaciado en escala 4/8px, consistente en toda la pieza.
- [ ] Iconos de un solo set coherente; ningún emoji haciendo de icono de UI.
