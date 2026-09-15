# 153 — Sistemas de estilo visual nombrados (2026)

**CRAFT/art-direction.** Léelo para elegir y ejecutar una estética nombrada coherente. Pareja de 01 (aesthetic systems), 10 (art-direction pro), 06 (anti-slop), 24 (brand identity), 15 (tokens). Regla de oro: **un estilo nombrado = dirección de arte instantánea; mezclar al azar (glass + brutal + aurora) = slop. Los tokens SON el estilo — cámbialos todos juntos o ninguno.**

## 1. Por qué los estilos nombrados importan

Condensan decisiones de color/tipo/sombra/radio/movimiento en un sistema coherente reconocible sin explicación. Cuando eliges "esto es Swiss editorial", cada decisión posterior tiene una vara: o pertenece al sistema o no. Mezclar al azar produce **slop** (la incoherencia que delata un sitio sin criterio). El panorama 2026 ya no tiene **un** estilo dominante; es **cultura de recombinación** sobre fundamentos sólidos (dark-first, bento, glass refinado). El subtexto nuevo: tras la inundación de "AI slop", el mercado premia la **prueba de mano humana** (textura, grano, imperfección deliberada, type expresivo) → el estilo nombrado bien ejecutado es una **señal anti-IA**.

## 2. Los estilos + receta de ejecución

**Glassmorphism / Liquid Glass** (Apple 2025-26: translúcido que refracta el fondo, specular highlights):
```css
.glass{ background:rgba(255,255,255,.08); backdrop-filter:blur(12px) saturate(160%);
  border:1px solid rgba(255,255,255,.18); border-radius:20px;
  box-shadow:0 8px 32px rgba(0,0,0,.25), inset 0 1px 0 rgba(255,255,255,.25); }
```
Firma: blur 8-15px, borde superior claro (luz), sombra de elevación. **Cuándo:** nav bars, modals, tooltips, CTAs sobre fondo vibrante. **Warning a11y:** el blur destruye contraste — nunca texto largo encima; `@supports not (backdrop-filter)` fallback opaco; respeta `prefers-reduced-transparency`. **Dated cuando** lo aplicas a TODO (niebla ilegible).

**Neubrutalism / brutalism** (bordes duros, sombras sólidas desplazadas sin blur, color saturado, mono):
```css
.brutal{ background:#FFE600; color:#0A0A0A; border:3px solid #000; border-radius:0;
  box-shadow:6px 6px 0 #000; font-family:"Space Mono",monospace; }
.brutal:hover{ transform:translate(-2px,-2px); box-shadow:8px 8px 0 #000; }
```
**Cuándo:** portfolios creativos, dev/indie, marcas que provocan. **Overdone cuando:** SaaS B2B serio o e-commerce de conversión (la fricción mata la confianza).

**Bento grid** (celdas de tamaños desiguales, estilo caja bento; Apple/Vercel): `display:grid; grid-template-columns:repeat(4,1fr); grid-auto-rows:180px;` + una celda "héroe" `grid-column:span 2; grid-row:span 2`. Cada celda = una idea autocontenida (un número, un gráfico, una imagen); radio uniforme (16-24px), gap consistente. **No es estilo visual sino estructura** — se combina con glass/dark/etc.

**Claymorphism** (3D suave "puffy", doble sombra externa + dos luces internas):
```css
.clay{ background:#6C5CE7; border-radius:32px;
  box-shadow:8px 8px 16px rgba(0,0,0,.18), inset -6px -6px 12px rgba(0,0,0,.20), inset 6px 6px 12px rgba(255,255,255,.30); }
```
**Cuándo:** retail, apps infantiles, onboarding, mascotas. **Dated cuando:** financiero/editorial serio (se ve de juguete).

**Editorial / Swiss revival** (grid riguroso, serif, restraint, type gigante, whitespace — el default "caro"):
```css
.editorial h1{ font-family:"GT Sectra","Canela",serif; font-size:clamp(3rem,8vw,7rem); line-height:.95; letter-spacing:-.02em; }
.editorial{ max-width:72ch; color:#111; background:#FAFAF7; }
```
Firma: serif display + sans neutral para body, jerarquía por escala no por color, casi sin sombras. **Cuándo:** agencias, moda, medios, lujo, B2B premium (el camino más seguro a "expensive"). **Casi nunca dated** (el riesgo: frío/estéril si no añades textura o un detalle humano).

**Aurora / gradient-glow** (Linear/Stripe — gradientes luminosos difusos sobre fondo oscuro; ver ref 148 para el sistema completo). **Cuándo:** SaaS, dev tools, AI. **Dated cuando:** gradiente morado-rosa genérico sin intención (el cliché #1 del "AI look").

**Y2K / maximalismo / anti-design** (chrome, blur, glitch, neón, monospace, deliberadamente "demasiado"): `linear-gradient(135deg,#FF00C8,#00E5FF,#FFE600)` + `font-family:"VT323"` + chrome-text con `background-clip:text`. **Cuándo:** música, moda joven, eventos, marcas "imposibles de confundir con output IA". **Peligroso cuando:** necesitas conversión/claridad.

**Dark-first + glow** (true black #000 ahorra batería OLED, acentos neón que brillan; estándar 2026). **Organic / analog (grain + serif)** (grano de película, serif, formas orgánicas, asimetría — la respuesta cálida y humana al slop; **exactamente el lenguaje BIO-SETA**: serif + grano + verdes orgánicos vende "natural y humano").

## 3. La dirección 2026

**Sube:** textura y grano, movimiento con intención (kinetic type, scroll-driven), **craft humano distinguible de IA**, type expresivo (oversized, wavy, variable, "imperfect by design"), glass refinado y funcional, dark-first OLED, bento, recombinación culta. **Datado:** flat corporate estéril, gradientes morado-rosa genéricos, ilustraciones blob de stock, layouts perfectamente simétricos sin alma — todo lo que parece **AI slop** (la perfección suave sin fricción ya no impresiona; delata generación automática).

## 4. Cómo elegir y comprometerse

Empareja vertical → estética: **Aurora/glass** = SaaS/AI/dev; **Claymorphism** = retail/kids; **Swiss editorial** = lujo/agencia/medios; **Neubrutalism** = creativo/indie; **Organic+grain** = wellness/artesanal/comida. Elige **UN** sistema, no una ensalada. Codifica el estilo en **tokens** (son la firma):
```css
:root{
  --radius: 20px;        /* glass 20 · brutal 0 · clay 32 · swiss 4 */
  --shadow: 0 8px 32px rgba(0,0,0,.25);  /* o 6px 6px 0 #000 en brutal */
  --font-display: "Canela", serif;
  --ease: cubic-bezier(.22,1,.36,1);     /* motion signature */
  --accent: #00FFA3;
}
```
Si cambias el radio de 20px a 0px y la sombra difusa a dura, cambiaste de estilo entero. **Los tokens son el estilo.**

## 5. Anti-slop — blacklist
**gradiente morado→rosa genérico de fondo "porque sí"** · **ilustraciones blob 3D de stock + íconos line genéricos** mezclados sin sistema · **glass aplicado a todo** (niebla ilegible; texto largo sobre blur) · **sombras inconsistentes** (difusa en una card, dura en la vecina) · **radios mezclados** (8px aquí, 24px allá) sin lógica de token · **simetría perfecta, espaciado uniforme robótico, cero textura** ("huele a IA") · **mezclar tres estilos nombrados** en una página (clay + brutal + glass) · **centrar todo, hero con un solo H1 + subtítulo + dos botones** idénticos a 10.000 landings · **stock photography sonriente + lorem real** (ausencia de prueba de mano humana). **El tell de un sitio art-directed:** una decisión audaz y coherente repetida con disciplina (una familia type peculiar, un grano, un motion-ease firmado, un grid asimétrico intencional) — un estilo nombrado previene la genericidad porque convierte mil micro-decisiones en una sola convicción visible.
