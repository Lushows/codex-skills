# 24 — Identidad de marca & sistemas de logo (de la estrategia a la web)

Playbook 2026 para una agencia multi-marca. El objetivo no es "hacer un logo" sino construir **sistemas de identidad vivos** y traducirlos a web con tokens. **Léelo cuando crees una marca desde cero o definas su dirección visual** (AGENTE STUDIO). Pareja de 02/03 (color/tipo), 14 (imagen IA) y 15 (tokens).

## 1. Anatomía de un sistema de identidad moderno (10 capas)

Un logo es el 10%. Un sistema 2026:
1. **Sistema de logo** (no un logo) — familia responsive: completo → compacto → símbolo/favicon + mono/invertida.
2. **Color** — primario, secundarios, acentos, neutrales + paleta de accesibilidad (WCAG).
3. **Tipografía** — display + texto (+ a veces variable custom). La tipo es el activo de marca #1.
4. **Imagery / dirección de arte** — fotografía/ilustración, tratamiento (grano, color grade), reglas de crop.
5. **Iconografía** — set propio cohesivo (no iconos genéricos sueltos).
6. **Motion identity** — cómo se revela el logo, easings de marca, micro-interacciones. *Se diseña cómo se mueve, no solo cómo se ve.*
7. **Voz / verbal** — tono, vocabulario, do/don't (informa decisiones visuales).
8. **Layout / grid** — columnas, spacing scale, ritmo.
9. **Graphic devices / patterns** — el "pegamento" reconocible (el equivalente al "Bélo" de Airbnb).
10. **Design tokens como marca** — identidad codificada en variables que propagan cambios al build.

**Mentalidad 2026:** el sistema es un **toolkit/ecosistema**, no un rulebook rígido — reconocible incluso adaptando tono/color/motion/formato. Test de validación: *¿funciona como marca estática, como reveal animado, como favicon de 16px y como secuencia full-screen?*
**Traducción a web (concreto):** color→tokens · tipo→escala tipográfica · spacing→escala 4/8px · motion→easings+duraciones · graphic device→componente decorativo reutilizable · voz→microcopy de botones/vacíos/errores.

## 2. Tipos de logo y cuándo

| Tipo | Qué es | Cuándo |
|---|---|---|
| **Wordmark** | Nombre en tipo distintiva (Google) | Nombre corto/memorable |
| **Lettermark** | Iniciales (IBM, NASA) | Nombre largo/difícil; compacidad |
| **Pictorial** | Imagen literal (Apple) | Marca **ya establecida** (arriesgado para nuevos) |
| **Abstracto** | Forma geométrica sin significado literal | Oferta diversa/audiencia global |
| **Combinación** | Símbolo + texto | **La más segura.** Full en packaging, símbolo en favicon/avatar |
| **Emblema** | Tipo dentro de sello | Herencia/credibilidad (pierde nitidez en pequeño) |

**Principios:** simple, memorable, versátil, escalable, apropiado.
**Logo responsive (sistema, no archivo):** Nivel 1 completo (símbolo+wordmark+tagline) · Nivel 2 compacto (sin tagline) · Nivel 3 símbolo solo (avatar/app) · Nivel 4 favicon 16px (sobrevive el "test de 16×16").
**Construcción:** grilla con **unidad base** (trazos/spacing en múltiplos) · **clear space** definido por un elemento del logo · tamaño mínimo documentado · vector siempre.
**Timeless vs trendy:** si quitas el color y el efecto, ¿sigue funcionando? Si no, es trendy. Timeless = simple, basado en grilla, funciona en mono.
**Errores:** demasiado detalle (muere en pequeño) · depender del color (prueba en negro/blanco) · seguir moda literal · sin versión responsive · kerning descuidado en el wordmark.

## 3. Tendencias 2026 (y qué está fechado)

**VIGENTE:** identidades vivas/no-fijas (se adaptan a XR/motion) · sistemas de logo responsive (Spotify, Airbnb Bélo, LA28 variable) · playful & inesperado (rompe la "sea of sans-serif sameness") · iteración sutil que preserva equity (Walmart, Amazon) · earthmarks orgánicos (curvas, tonos tierra — Patagonia, Beyond Meat) · 3D táctil refinado sin skeuomorfismo (Netflix, Adobe Substance) · revival de serifs bold + variable type custom · **anti-AI / craft humano** (dibujado a mano, imperfecto, grano = señal de autenticidad) · motion-first/sensorial.
**FECHADO (evitar):** gradient blobs genéricos (blob morado-azul de startup) · mismidad flat-sans de los 2010s · 3D glossy/realista pesado de los 2000s · símbolos sobreusados (swooshes, gente abstracta tomada de la mano, esfera global, "casa+check") · minimalismo tech intercambiable.

## 4. Color y tipo a nivel de identidad

**Paleta (4-6 colores):** 1-2 neutrales + 1 primario + 1-2 secundarios + 1 acento. <3 limita; >6 diluye.
**Regla 60-30-10:** 60% dominante (base, suele ser neutral, fija el mood) · 30% secundario (tipo, sidebars, botones secundarios) · 10% acento (CTAs, highlights).
**Accesibilidad (no negociable):** contraste WCAG ≥4.5:1 texto normal, 3:1 grande. Cada combo de marca debe pasarlo.
**Dato:** el color sube reconocimiento de marca hasta 80% e influye ~85% de la decisión de compra impulsiva → la inversión de mayor impacto.
**Psicología del color honesta:** punto de partida, no dogma — el contexto y la consistencia construyen el significado más que el color "intrínseco".
**Tipografía:** **Display** (titulares, personalidad) + **Texto** (lectura, neutral) (+ a veces un tercero para datos/UI). Señal de personalidad: serif = herencia/credibilidad · grotesque = neutral/moderno · geometric sans = tech/limpio · humanist = cálido/accesible · variable custom = ownable y premium.

## 5. Estrategia que informa el diseño (práctico)

La estrategia va PRIMERO; la identidad la refleja.
- **Posicionamiento** (statement interno, no tagline): *"Para [audiencia] que [necesidad], [marca] es el [categoría] que [valor único] porque [prueba]."*
- **Archetype (12 de Jung):** elige 1 primario (+1 secundario) → vuelve objetivas las decisiones (cada archetype implica paleta/formas/tipo).
- **Atributos de personalidad:** 3-5 adjetivos ("cálido pero preciso"), cada uno con consecuencia visual.
- **Naming:** corto, pronunciable, distintivo, dominio disponible, sin conflicto de marca, evita siglas genéricas.
- **Brand brief + moodboard** antes de diseñar (traduce adjetivos a referencias).
- **Diferenciación:** audita logos/colores/tipos de 5 competidores → encuentra el "sea of sameness" → posiciónate en el vacío (si todos son azul sans-serif, no seas azul sans-serif).

## 6. Marca → web + guidelines + pipeline

**Tokens en 3 niveles (clave multi-marca):** primitivos (`color-blue-500`, `space-4`) → semánticos (`color-bg-primary`, `font-heading`) → componente (`button-bg`, `card-radius`). Naming: dot notation jerárquica → kebab-case en CSS. Evita genéricos (`--primary`); usa context-based (`--color-brand-primary`). **Multi-marca = theming:** misma estructura, distintos valores; cambiar un token propaga en minutos (ver ref 15).
**Mini brand guideline usable (1 página/sección):** (1) esencia (posicionamiento + archetype + 3 atributos); (2) logo (variantes responsive + clear space + mínimo + don'ts); (3) color (hex + tokens + 60-30-10 + combos accesibles); (4) tipo (familias + escala + pesos); (5) imagery do/don't; (6) iconografía + graphic device; (7) motion (easings/duraciones); (8) voz (tono + 5 do/don't); (9) aplicaciones (web header, avatar, packaging).
**Brand style frame para sitios:** un artboard con hero + tipografía en contexto + paleta aplicada + un componente clave + motion. Es el puente entre la guideline y el diseño web — apruébalo antes de maquetar.
**Pipeline repetible (multi-marca):** brief/descubrimiento → audit competitivo → moodboard (2 direcciones) → logo system → foundations (color 60-30-10+WCAG, tipo, spacing) → sistema (iconos, graphic device, motion, imagery) → tokens (primitivos→semánticos→componente) → style frame → web design system → mini guideline.

## Branding anti-slop blacklist
gradient blobs morado→azul de startup · AI logo tells (simetría perfecta artificial, "gente abstracta", swooshes, esferas/globos, hojas genéricas, degradado iridiscente sobre ícono geométrico) · flat-sans wordmark sameness · iconos de librería con grosores mezclados · color sin sistema (8+ sin jerarquía 60-30-10) · contraste que falla WCAG · logo que muere en 16px o sin versión mono · stock photography corporativa (handshake, equipo riendo) · cero motion / cero graphic device · 3D glossy estilo 2007 · lorem ipsum permanente y microcopy sin voz.
**Antídoto craft 2026:** grano real, tipo variable/custom, imperfección intencional, motion con easings propios, graphic device ownable, paleta tierra/táctil cuando aplique, y el test: *estático + reveal + favicon + full-screen*.
