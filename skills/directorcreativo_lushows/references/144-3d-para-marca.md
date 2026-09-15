# 144 — 3D para marca

El 3D le da a la marca volumen, materiales y profundidad: un isotipo que parece de vidrio, un producto que rota, una escena con luz real. En 2026 es accesible (Spline corre en el navegador) y un sello de modernidad. Pero el 3D mal usado es el camino más rápido a lo genérico: la "burbuja iridiscente flotando" que todas las startups copiaron. La pregunta no es "¿puedo hacer 3D?" sino "¿qué aporta el volumen que el 2D no?".

## Cuándo el 3D aporta (y cuándo no)

**Aporta cuando:**
- El producto es físico y rotarlo ayuda a entenderlo (un envase, un equipo).
- La marca quiere transmitir innovación/tecnología con materiales reales.
- Necesitas profundidad e interacción en una web (hero que reacciona al mouse).
- El isotipo gana sentido con volumen (una forma que solo se entiende en 3D).

**No aporta cuando:**
- Es decoración sin concepto (la "blob" iridiscente por moda).
- Una marca artesanal/cálida que pide textura plana e ilustración (ver 57).
- Recarga una UI que debe ser rápida y clara.
- El 3D malo (plástico, luz plana) se ve peor que un buen 2D.

## Conceptos básicos (en simple)

| Término | Qué es |
|---|---|
| **Malla (mesh)** | La "piel" geométrica del objeto, hecha de polígonos |
| **Material / shader** | Cómo se ve la superficie: mate, metálico, vidrio, emisivo |
| **Iluminación** | Las luces de la escena; definen el mood (igual que en foto, ver 63) |
| **Render** | El cálculo final que convierte la escena 3D en imagen/video |
| **PBR** | "Physically Based Rendering": materiales que reaccionan a la luz como en la realidad |
| **HDRI** | Una imagen 360° que ilumina y refleja en la escena |

## Materiales y formas de marca

El 3D es otra capa del sistema visual, no un mundo aparte:
- **Materiales de marca**: define 2–3 (ej. "vidrio esmerilado + metal cepillado en el color primario"). Repítelos. Igual que la paleta (ver 33).
- **Formas**: deriva el lenguaje 3D de tu isotipo y geometría (ver 23). Si la marca es de esquinas redondeadas, el 3D también.
- **Color**: el 3D debe respetar la paleta. Una escena con colores fuera de marca rompe el sistema.
- **Luz**: cálida vs. fría, dura vs. difusa — comunica personalidad (ver 63 iluminación).

## Herramientas reales (por capacidad)

| Herramienta | Para qué | Nivel |
|---|---|---|
| **Spline** | 3D interactivo para web, en el navegador, exporta a código | Accesible — ideal para empezar |
| **Blender** | Suite 3D completa, gratis y potente (modelado, render, animación) | Profesional, curva alta |
| **Cinema 4D** | Estándar de motion 3D en estudios, muy pulido | Profesional, de pago |
| **Womp / Vectary** | 3D simple en navegador | Principiante |
| **KeyShot** | Render fotorrealista de producto | Especializado |

Para Lushows: **Spline** para web interactiva, o encargar a un freelance en Blender un render de producto. No necesitas dominar C4D para tener buen 3D.

## 3D en la web

- **Hero interactivo**: objeto que rota o reacciona al mouse (Spline → exporta a React/embed).
- **Cuidado con el peso**: el 3D web puede ser pesado. Optimiza polígonos, usa carga diferida, da un fallback (imagen) para móviles lentos.
- **Rendimiento > espectáculo**: un hero 3D que traba el scroll arruina la experiencia.

La skill hermana **desingweb-lushows** cubre la implementación de 3D en web (Spline/Three.js) dentro de interfaces premium.

## Render para piezas estáticas y video

- **Producto estático**: render de alta calidad para catálogo, redes, packaging mockup (ver 79).
- **Producto en loop**: rotación 360° para web/reel.
- **Resolución y formato**: PNG con alfa para componer; MP4/WebM para video; suficiente DPI si va a impresión.

## No abusar: la regla del 3D

El 3D llama mucho la atención. Úsalo como **acento**, no como base de todo. Una web entera de blobs flotando se ve igual a las otras mil. Un solo objeto 3D con concepto, bien iluminado y de marca, vale más que diez efectos.

## Errores comunes
- 3D decorativo sin concepto (la blob de moda).
- Materiales plásticos, luz plana → se ve barato.
- Color/forma fuera del sistema de marca.
- Hero 3D que traba el rendimiento.
- 3D donde la marca pedía calidez plana/ilustración.

## Mini-checklist
- [ ] El 3D aporta algo que el 2D no (no es decoración)
- [ ] Materiales y formas derivan del sistema de marca
- [ ] Iluminación con intención (mood coherente)
- [ ] Color dentro de la paleta
- [ ] En web: optimizado, con fallback, sin trabar
- [ ] Usado como acento, no como base de todo

**Siguiente paso**: cuando la marca sale de la pantalla plana hacia el espacio real y la realidad aumentada —visionOS, AR, experiencias spatial— hay principios nuevos que dominar (ver 145 diseño espacial, AR y spatial).
