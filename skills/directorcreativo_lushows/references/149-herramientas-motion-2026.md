# 149 — Herramientas de motion 2026

El panorama de motion en 2026 va de lo manual y preciso (After Effects) a lo generativo (IA de video), pasando por formatos ligeros para web (Lottie, Rive). La trampa del principiante es enamorarse de una herramienta; lo correcto es **elegir la herramienta según la pieza y el destino**. Este módulo es el mapa para no equivocarse y para entender cómo exportar bien. Es el cierre del bloque de motion y la versión ampliada de las herramientas vistas en el núcleo (ver 84, 90).

## El mapa rápido: qué usar para qué

| Necesito… | Herramienta | Por qué |
|---|---|---|
| Logo intro/outro, video de marca | **After Effects** | Estándar, control total |
| Animación ligera para web/app (logo, icono) | **Lottie** | Pesa kB, escala sin pixelar, se anima por código |
| Animación interactiva (reacciona al usuario) | **Rive** | Estados y interacción reales, muy ligera |
| Microinteracciones en web React | **Framer Motion** | Springs, gestos, layout — ver motion-framer |
| 3D interactivo en web | **Spline** | 3D en navegador, exporta a código |
| 3D/render serio | **Blender / Cinema 4D** | Modelado y render profesional (ver 144) |
| Reels/TikTok del día a día | **CapCut / Canva** | Accesible, plantillas, subtítulos auto |
| Generar/extender video con IA | **IA de video** (ver abajo) | Acelera B-roll, fondos, conceptos |

## Las herramientas, por capacidad

**After Effects (AE)** — el estándar profesional de motion graphics. Control fotograma a fotograma, expresiones, integración con todo. Curva de aprendizaje alta. Lo usa el motion designer, no el cliente. De aquí salen los logos animados, lower-thirds, plantillas.

**Lottie** — formato de animación vectorial (archivo `.json`) que se exporta desde After Effects (con el plugin Bodymovin) o desde herramientas como LottieFiles. Ventaja enorme para web/app: **pesa kilobytes, escala sin pixelarse y se controla por código** (reproducir, pausar, cambiar al hover). Ideal para: logo animado en la web, iconos animados, loaders, ilustraciones. Si el logo animado va a la web, casi siempre la respuesta es Lottie.

**Rive** — como Lottie pero con **interactividad y estados** reales (un botón que tiene estados normal/hover/activo animados, un personaje que reacciona). Muy ligero, pensado para producto. Más potente que Lottie cuando necesitas que la animación responda al usuario.

**Spline** — 3D en el navegador, sin instalar nada, exporta a embed o código React. La puerta de entrada accesible al 3D de marca (ver 144).

**Blender / Cinema 4D** — suites 3D completas. Blender es gratis y potentísimo; C4D es el favorito de estudios de motion por su pulido. Para render de producto, escenas 3D, objetos de marca.

**Framer Motion** — librería de animación para React. Springs naturales, gestos (drag, tap), animaciones de layout automáticas. Es la herramienta para microinteracciones y motion de UI en web moderna. **La skill hermana motion-framer genera este código** y la skill desingweb-lushows la usa en interfaces premium.

**CapCut / Canva** — nivel accesible para el dueño/community manager: edición de reels, subtítulos automáticos, plantillas animadas de marca. Aquí se vive el día a día del contenido (ver 146).

## IA de video en 2026

La IA de video maduró: genera clips a partir de texto/imagen, extiende tomas, crea B-roll y fondos. Úsala como **acelerador**, no como reemplazo del criterio:
- **Casos buenos**: B-roll genérico, fondos abstractos, conceptos rápidos, extender una toma, quitar fondo, upscaling.
- **Cuidado**: consistencia de marca (la IA inventa detalles fuera de tu sistema), manos/texto deformes, derechos de uso. Revisa siempre que respete tu paleta, tipografía y tono.
- **Flujo realista**: IA para material base → AE/CapCut para componer, poner tu marca, subtítulos y motion propio. La marca la pones tú, no la IA.

(Para foto/imagen con IA, ver 68; para flujos generativos de marca, ver 91.)

## Exportación: que no se arruine al final

| Destino | Formato | Notas |
|---|---|---|
| Redes / video general | **MP4 (H.264)** | Universal, buen peso |
| Sobreponer logo (con transparencia) | **MOV ProRes 4444** o **WebM** | Canal alfa = fondo transparente |
| Web ligera (logo/icono) | **Lottie (.json)** | Kilobytes, escalable, por código |
| Web interactiva | **Rive (.riv)** o Spline embed | Estados/interacción |
| Avatar/firma animada | **GIF** | Cuidado con el peso y los colores |
| Calidad máxima / archivo | **ProRes / sin compresión** | Para editar después, no para publicar |

Reglas de exportación:
- Exporta a la **resolución del destino** (1080×1920 para reels; 2x para pantallas retina en web).
- **No subexportes** un MP4 muchas veces (cada reexport degrada calidad).
- Para web, **siempre prefiere vector (Lottie/SVG/Rive)** sobre video cuando se pueda: pesa menos y escala.
- Guarda el **archivo fuente** (proyecto de AE/Spline) para editar después.

## Flujo recomendado (negocio pequeño)

1. **Marca**: motion designer hace logo intro/outro + plantillas en AE → entrega MP4, MOV alfa y Lottie.
2. **Web/app**: desarrollador implementa con Framer Motion + Lottie/Rive (skills motion-framer y desingweb-lushows).
3. **Contenido diario**: dueño/CM edita reels en CapCut con las plantillas (ver 146).
4. **3D si aplica**: Spline para web, Blender/freelance para render (ver 144).

## Errores comunes
- Usar video pesado en web donde un Lottie pesaría 50× menos.
- Reexportar MP4 muchas veces (calidad se degrada).
- Esperar que el cliente no técnico anime en After Effects.
- Confiar el resultado final a la IA sin pasar el control de marca.
- Exportar sin canal alfa cuando se necesita sobreponer.
- No guardar el archivo fuente.

## Mini-checklist
- [ ] Herramienta elegida según pieza y destino (ver tabla)
- [ ] Web ligera con Lottie/Rive, no video pesado
- [ ] Versión con alfa cuando hay que sobreponer
- [ ] Exportado a la resolución correcta del destino
- [ ] IA usada como acelerador, con control de marca encima
- [ ] Archivos fuente guardados
- [ ] Entrega final lista para el cliente (MP4 + plantillas)

**Siguiente paso**: con el bloque 14 completo, integra el motion en el sistema de marca documentado —guidelines, tokens y consistencia omnicanal— volviendo a 141 (sistemas de motion) y conectando con 87 (design tokens) y 88 (consistencia omnicanal). Para producir el código de animación web, apóyate en la skill hermana **motion-framer**.
