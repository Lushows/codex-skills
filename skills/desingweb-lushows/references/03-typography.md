# Tipografía — pairings, escala y jerarquía

La tipografía es protagonista en 2026: titulares gigantes, fuentes con carácter y motion tipográfico hacen la primera impresión. Una buena pareja display+body resuelve el 70% de la personalidad de un sitio. Este archivo da parejas listas, escala modular y reglas duras.

**Principio rector:** elige UNA display con carácter para titulares y UNA body neutra y legible para texto largo. Nunca dos fuentes con personalidad fuerte compitiendo en el mismo bloque.

---

## 1. Pairings display + body (listos para pegar)

### Editorial serio
- **Display:** Fraunces (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..900&display=swap');`
- **Body:** Inter Tight (Google Fonts) o Söhne (comercial).
- **Uso:** revistas, marcas premium, long-form, restaurantes de autor.

### Tech moderna y nítida
- **Display:** Clash Display (Fontshare) — `<link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&display=swap" rel="stylesheet">`
- **Body:** Hanken Grotesk (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300..800&display=swap');`
- **Uso:** SaaS, dev tools, fintech, IA, dark/neon-tech.

### Lujo refinado
- **Display:** Cormorant Garamond (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&display=swap');` (sustituto libre de Canela/Ogg).
- **Body:** Jost (Google Fonts) en mayúsculas espaciadas para labels + body discreto.
- **Uso:** joyería, hotelería, perfumería, relojería, inmobiliaria premium.

### Brutalist crudo
- **Display:** Space Mono (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');`
- **Body:** la misma Space Mono o un grotesk neutro (Archivo).
- **Uso:** estudios creativos, portafolios anti-marketing, música underground.

### Geométrica con carácter
- **Display:** Cabinet Grotesk (Fontshare) — `<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@400,500,700,800&display=swap" rel="stylesheet">`
- **Body:** General Sans (Fontshare) — `<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600&display=swap" rel="stylesheet">`
- **Uso:** branding moderno versátil, glassmorphism, agencias.

### Wellness orgánico
- **Display:** Sligoil (alternativa libre: Fraunces opsz alta) — usa Fraunces para titulares cálidos: `@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500..700&display=swap');`
- **Body:** Hanken Grotesk (Google Fonts).
- **Uso:** suplementos, hongos funcionales, cosmética natural, sostenibilidad.

### Playful redondo
- **Display:** Hellix (comercial) o libre: Baloo 2 (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700&display=swap');`
- **Body:** Nunito (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap');`
- **Uso:** apps de consumo, edtech, familias, fintech amigable.

### Retro-futurista Y2K
- **Display:** PP Neue Machina (comercial) o libre: Orbitron (Google Fonts) usado con avaricia — `@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&display=swap');`
- **Body:** Space Grotesk solo si es ineludible; preferir Hanken Grotesk para el cuerpo.
- **Uso:** moda joven, drops, gaming, cripto cultural. Reserva la display para 1–2 momentos hero.

### Art-deco elegante
- **Display:** Cormorant (Google Fonts) en caja alta + tracking, o Poppins en caps muy espaciado — `@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap');`
- **Body:** Jost (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&display=swap');`
- **Uso:** bares de cóctel, hoteles boutique, eventos premium, cine/teatro.

### Soft pastel delicado
- **Display:** Reckless (comercial) o libre: Newsreader (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300..600&display=swap');`
- **Body:** Hanken Grotesk light (Google Fonts).
- **Uso:** beauty, bienestar mental, baby, papelería, autocuidado.

### Maximalista expresiva
- **Display:** Bricolage Grotesque (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@10..48,400..800&display=swap');`
- **Body:** Archivo (Google Fonts) — `@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&display=swap');`
- **Uso:** festivales, cultura/arte, moda atrevida, campañas anti-grid.

### Suiza minimal contemporánea
- **Display:** Switzer (Fontshare) — `<link href="https://api.fontshare.com/v2/css?f[]=switzer@400,500,600,700&display=swap" rel="stylesheet">`
- **Body:** Switzer (la misma, en peso regular) — sistema de una sola superfamilia, muy suizo.
- **Uso:** estudios de diseño, consultoras, B2B serio, portafolios minimalistas.

---

## 2. Escala tipográfica modular

Elige el ratio según el tono: **1.25** (Major Third) para interfaces densas/legibles, **1.333** (Perfect Fourth) para marketing equilibrado, **1.5** (Perfect Fifth) para landings dramáticas con titulares enormes. Base = `1rem` (16px).

| Token | Ratio 1.25 | Ratio 1.333 | Ratio 1.5 | Uso típico |
|-------|-----------|------------|-----------|------------|
| xs    | 0.64 rem  | 0.563 rem  | 0.444 rem | legales, captions |
| sm    | 0.8 rem   | 0.75 rem   | 0.667 rem | labels, metadatos |
| base  | 1 rem     | 1 rem      | 1 rem     | cuerpo de texto |
| lg    | 1.25 rem  | 1.333 rem  | 1.5 rem   | lead / intro |
| xl    | 1.563 rem | 1.777 rem  | 2.25 rem  | subtítulos |
| 2xl   | 1.953 rem | 2.369 rem  | 3.375 rem | h3 |
| 3xl   | 2.441 rem | 3.157 rem  | 5.063 rem | h2 |
| 4xl   | 3.052 rem | 4.209 rem  | 7.594 rem | h1 sección |
| 5xl   | 3.815 rem | 5.61 rem   | 11.39 rem | hero |
| 6xl   | 4.768 rem | 7.478 rem  | 17.09 rem | display gigante / número hero |

Implementa la rampa con `clamp()` para fluidez: `font-size: clamp(2.5rem, 6vw + 1rem, 7.5rem);` en los titulares hero.

---

## 3. Reglas de jerarquía

- **Tracking en display:** los titulares grandes necesitan tracking NEGATIVO — `letter-spacing: -0.02em` a `-0.04em` según peso. Cuanto más grande la fuente, más cerrado. Esto evita el aspecto "suelto/amateur".
- **Tracking en labels/caps:** al revés — mayúsculas pequeñas piden tracking POSITIVO `+0.08em` a `+0.12em` para respirar.
- **Line-height del body:** entre **1.5 y 1.7** para texto largo. Titulares grandes bajan a `1.0–1.15` (cuanto mayor el tamaño, menor el interlineado).
- **Medida (line length):** mantén el cuerpo entre **60 y 75 caracteres** por línea (`max-width: 65ch`). Más ancho cansa la vista; más estrecho fragmenta la lectura.
- **Contraste de tamaño:** entre h1 y body debe haber un salto claro (mínimo 3–4 pasos de la escala). La timidez tipográfica mata la jerarquía.
- **Pesos:** no uses más de 3 pesos por familia en una página. Body en `400`, énfasis en `600`, display en `700–900`.
- **Números:** activa `font-variant-numeric: tabular-nums;` en tablas, precios y datos para alineación vertical perfecta.
- **Optical sizing:** en fuentes variables con eje `opsz` (Fraunces, Newsreader, Bricolage), deja `font-optical-sizing: auto;` para que los titulares ganen contraste y el cuerpo gane legibilidad.

---

## 4. Fuentes PROHIBIDAS por defecto

Estas fuentes están **prohibidas** salvo justificación explícita del cliente o requisito técnico. Su uso es la señal #1 del "look de IA genérico":

- **Inter** — prohibida. Sobreexpuesta hasta el agotamiento; es el default de medio internet. Si necesitas un grotesk neutro, usa Hanken Grotesk, General Sans o Switzer.
- **Roboto** — prohibida. Sabor "Android stock", sin personalidad.
- **Arial / Helvetica (web-safe)** — prohibidas como fuente de marca. Helvetica real (Neue Haas) sí vale en proyectos suizos; la Arial de sistema, nunca.
- **system-ui / -apple-system** — prohibida como tipografía de marca. Úsala solo como fallback en la pila, nunca como elección principal.
- **Space Grotesk** — prohibida por sobreuso. Fue fresca, hoy es el cliché del portafolio de dev. Sustituir por Cabinet Grotesk, Clash Display o Switzer.
- **Montserrat, Poppins (como body), Lato, Open Sans** — prohibidas como fuente principal: son las "Inter de hace cinco años", genéricas y delatan plantilla. (Poppins solo se tolera en caps espaciados para labels art-deco).

Regla de oro: si la fuente viene preseleccionada por el builder/tema, probablemente está en esta lista. Cámbiala.
