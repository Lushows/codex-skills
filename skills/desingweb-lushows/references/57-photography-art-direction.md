# 57 — Fotografía & dirección de arte para web (la artesanía no-IA)

La imagen es el ~60% del "premium feel" antes de que nadie lea una palabra. La IA genera pixeles; lo que diferencia un sitio caro de uno barato es **dirección de arte**: el criterio humano de decidir qué mundo visual habita la marca y mantenerlo coherente imagen tras imagen. **Léelo para dirigir/elegir/usar imágenes reales** (complementa 14 AI image). Pareja de 10 (art-direction), 11, 24 (marca).

## 1. Fundamentos de dirección de arte

**Qué es:** definir el *mundo visual cohesivo* de una marca (mood, estilo, treatment, sujetos, luz, color) y aplicarlo con disciplina. **Regla #1: consistencia.** Test definitivo: pon 20 imágenes del sitio en una grilla — si parecen de marcas distintas, no tienes DA, tienes una carpeta de fotos.
**El style frame (6 ejes antes de disparar):** (1) **luz/mood** (bright & airy vs dark & moody) · (2) **color grade** (cálido/neutro/frío, saturación, con HEX) · (3) **composición** (simétrica vs editorial, negative space) · (4) **sujetos** (casting: edad real, asimetría, character, wardrobe) · (5) **props & styling** · (6) **locations** (estudio seamless vs en-contexto vs exterior).
**El moodboard** = contrato visual: 15-30 referencias que *muestran* el mundo (no lo describen) + "las últimas 20 imágenes publicadas" para auditar inconsistencias.
**El shoot:** el **brief al fotógrafo** (ángulos, luz, styling, casting, retoque, specs) *antes* de producción · el **shot list** (cada toma: front/back/detail/lifestyle/packaging/hero — para no faltar tomas para el grid). Glossier (soft light, piel real), Aesop (simetría, negative space, muted), Patagonia (luz natural, exteriores) — reconocibles *solo por la foto*. Eso es DA funcionando.

## 2. Tipos de fotografía de marca & cuándo

| Tipo | Qué es | Rol en el sitio |
|---|---|---|
| **Product (studio/seamless)** | Producto sobre fondo limpio (~85% del frame) | Grid de catálogo, PDP |
| **Product styled / in-context** | Producto con props/superficie/ambiente | Hero de producto, features |
| **Lifestyle** | La persona-usando-el-producto (aspiracional) | Hero emocional |
| **Editorial / campaign** | Storytelling, riesgo, luz dramática | Hero de campaña/lanzamiento |
| **Flat-lay** | Composición cenital | Grids, "qué incluye" |
| **Detail / macro** | Textura/material/primerísimo plano | Demuestra calidad/craft/ingrediente |
| **Environmental / location** | En lugar real | Storytelling de origen, "about" |
| **Portrait** | Rostro con character | Equipo, testimonios, founders |
| **Hero shot** | La imagen ancla, alto impacto | Lo primero que ve el usuario |
Para BIO-SETA: macro de la textura del hongo + lifestyle cálido del ritual + product seamless limpio de las cápsulas.

## 3. Luz, composición & el "look caro"

**Luz:** natural (golden hour/overcast/morning = autenticidad/calidez/lifestyle) vs estudio (softbox 45°, 5000-5500K = control/product/consistencia) · soft (softbox grande difuso = premium, halagador) vs hard (flash directo = editorial deliberado, o amateur si es accidental) · **lateral** revela textura/volumen (el caballo de batalla del look caro) · mood bright&airy (fresco/wellness) vs dark&moody (lujo/gourmet).
**Composición:** tercios como base + **negative space generoso** (el vacío *es* lo que lee caro/editorial) · frame editorial (descentrado, asimétrico) · **profundidad** (foreground/background, bokeh, capas — una foto plana lee barata) · leading lines · appetite/desire appeal (food/wellness: frescura, vapor, textura).
**Tells de fotografía barata:** flash directo on-camera (sombra dura detrás) · sobre-saturación/HDR agresivo · mezcla de temperaturas de color · fondo cluttered · sin punto focal, todo plano · poses staged ("laughing alone with salad") · baja resolución/compresión · white balance roto.
**Color grade/LUT:** define un LUT/preset de marca con nombre y aplícalo a *todo* — la consistencia del treatment convierte fotos de fuentes distintas en "una sola marca".

## 4. Curación & sourcing

**El ojo del editor:** curar es rechazar (por cada foto que entra, rechaza 10). Criterios: ¿pasa el cohesion test? ¿tiene punto focal? ¿buena luz? ¿casting real, no genérico?
**Stock bien hecho (evita el "generic-stock tell"):** fuentes premium **Stocksy/Unsplash+/Death to Stock** (no lo sobre-usado de bancos masivos). **Cómo hacer que no parezca stock:** (1) aplica TU color grade/LUT, (2) crop agresivo para reencuadrar, (3) duotone/overlay de marca, (4) elige menos "modelos sonriendo a cámara" y más detalle/textura/candid. El tell mortal: corporativos dándose la mano.
**Custom shoots:** valen la pena cuando la imagen es el producto (food/wellness/moda/lujo) — exclusividad que ningún competidor tiene. Mínimo viable: medio día con shot list → hero + 8-10 grid + macros.
**Biblioteca de marca:** organiza por tipo (hero/product/lifestyle/detail), naming `SKU_angle_colorway_version`.
**AI vs real:** en 2026 la foto *real* es diferenciador por la saturación de IA (§6). Usa IA para texturas/fondos/conceptos; real para rostros, producto, autenticidad. Cuida licencias.

## 5. Photo treatment & integración web

**Post para web:** color grade a marca (mismo LUT en toda imagen — el unificador #1) · grain/texture sutil (calidez analógica, "humaniza", anti-AI) · retoque con límite (lo natural lee premium en 2026, no piel plástica).
**Preparar para web:** crops/ratios por contexto (PDP 1:1 ≥2048², IG 4:5, hero 16:9/full-bleed) · **responsive art direction** con `<picture>`+`media` (crops *distintos* por breakpoint — móvil close-up vertical, desktop wide — no la misma imagen reescalada) · **focal point cropping** (`object-fit:cover` + `object-position` al punto focal para que el smart-crop nunca corte el sujeto) · sRGB, WebP/AVIF comprimido.
**Treatments de diseño:** **scrim** (gradiente semi-transparente negro 40%→transparente para type-over-image legible) · gradient overlay coloreado · **duotone** (mapea highlights/shadows a 2 colores de marca vía `mix-blend-mode:color` — cohesión instantánea, oculta inconsistencias) · blend modes en CSS · imagen como elemento (full-bleed, hero fotográfico).
**Type sobre imagen (legibilidad = accesibilidad):** nunca texto sobre zona busy; usa scrim/gradiente/overlay para contraste AA; reserva una zona "calma" (negative space) para el texto **desde el shoot** (el art director lo planifica en el shot list).

## 6. Sistemas de lenguaje visual & 2026

**La guideline de fotografía:** define cada decisión *antes* (lighting, composición, color treatment, sujetos, fondos, specs) con **library de ejemplos** (imágenes, no solo texto), **treatment specs** (softbox 45°/5000-5500K/HEX/saturación/LUTs nombrados/límites de retoque), **do's & don'ts con imágenes** (muestra el "no"), **flexibilidad modular** (reglas + espacio para creatividad — rígido = imágenes stale). Corre la guía en un shoot real antes del rollout.
**Tendencias 2026:** **authentic > polished** (lo crudo/íntimo/real gana; imperfección como *feature*: missed focus, motion blur, grano) · **backlash a la saturación de IA** (la imperfección visible es el marcador que distingue foto humana de máquina → la foto real es el diferenciador competitivo) · documentary/candid · casting real (edad visible, asimetría, "lived-in faces", diversidad) · film aesthetic (grano/tono analógico) · motion-aware (imágenes pensadas para moverse) · **multi-marca (AGENTE STUDIO):** cada marca su propio style frame + LUT + casting; el sistema garantiza que cada una sea coherente *y* distinguible de las demás (la DA evita que todas las marcas del studio se vean igual).

## Photography/art-direction anti-patterns — blacklist
stock genérico obvio (corporativos dándose la mano, "laughing with salad") · **treatment inconsistente** (cada imagen con color grade distinto — el peor pecado de cohesión) · mala luz (flash directo, sombras duras, white balance roto) · fondos cluttered / sin punto focal / todo plano · el **AI-tell** (piel plástica, manos raras, perfección irreal, fondos "demasiado limpios") · sobre-saturación/HDR reventado · **type sobre imagen busy** sin scrim/overlay (ilegible, falla AA) · low-res/pixelado/sobre-comprimido · misma imagen reescalada en todos los breakpoints (sujeto cortado en móvil) · poses staged/sonrisas forzadas (lee falso/"IA" en 2026) · mezclar verticalidad de marcas (lujo dark+moody junto a wellness bright+airy sin sistema).
