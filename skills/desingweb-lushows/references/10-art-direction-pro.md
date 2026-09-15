# Art direction profesional — cómo verse "premium" y no plantilla

Síntesis de análisis de mercado real (estudios de arquitectura/interiorismo premiados, landings de servicios de alta conversión, tendencias 2026, motion de élite). **La lección central: lo premium en la mayoría de nichos serios es RESTRICCIÓN, no acumulación de efectos.** El lujo digital es espacio, fotografía, tipografía y timing — no glows, ni cursores con confeti, ni gradientes plásticos.

Referencias maestras a estudiar: **Mersi Architecture** (quiet luxury), **Norm Architects**, **1508 London**, **Studio KO**, **Vaulk**.

---

## 1. La receta editorial "Atelier" (la apuesta más segura para marcas serias)

- **Lienzo:** 3 neutros cálidos + 1 acento tierra. NUNCA blanco puro `#FFFFFF` ni grises azulados fríos. Ej.: papel `#F0EEE9` (Cloud Dancer, color 2026), tinta cálida `#1C1A17`, neutro medio `#8A8278`, acento terracota `#C26B4A` o verde bosque `#2F4A3C`.
- **Tipografía:** 1 serif display de alto contraste (Fraunces gratis; Canela/Tiempos Headline premium) para titulares + 1 grotesca para body (Instrument Sans, Neue Montreal, Söhne). Etiquetas/eyebrows en **monoespaciada mayúsculas con tracking** (`01 / SERVICIOS`) — detalle muy 2026. Una sola pareja, jamás 3 familias sueltas.
- **Whitespace agresivo:** 120–160px de padding vertical por sección en desktop. El vacío comunica calma y lujo. Cada bloque "respira".
- **Fotografía full-bleed protagonista:** ratios editoriales alternados (4/5 vertical + 16/11 horizontal), curaduría asimétrica (no grid de cuadrados uniformes). Color grading cálido coherente en TODAS. Fotos propias > stock (el stock genérico es el delator #1 de "marca falsa").
- **Grano/textura sutil:** overlay de ruido SVG al 3–5% con `mix-blend-mode:multiply`. Rompe la perfección plástica digital → tactilidad de papel. Es lo que más separa "hecho a mano premium" de "template de IA".
- **Numeración editorial:** secciones e ítems con índice (`01 / 02 / 03`) estilo revista de arquitectura.

## 2. Escala tipográfica que se ve cara

```
Hero/H1:  clamp(2.8rem, 7vw, 6.6rem)  line-height: .96   letter-spacing: -.035em
H2:       clamp(2.1rem, 4.6vw, 3.6rem) line-height: 1.02
Body:     1.0625–1.125rem (17–18px)    line-height: 1.55–1.6   medida 60–72ch
Eyebrow:  .74rem  MONO MAYÚSCULAS  letter-spacing: .18em
```
Regla: display grande pide **tracking negativo**; cuerpo pide medida de línea contenida (`max-width:65ch`).

## 3. Paletas premium 2026 (con hex)

- **Crema editorial + terracota:** bg `#F0EEE9` · tinta `#1C1A17` · stone `#8A8278` · acento `#C26B4A` · sage `#6B6F5E`.
- **Dark mode cálido + latón:** base `#09090B`→`#18181B`(cards)→`#27272A` · texto `#FAFAFA`/`#A1A1AA` · acento latón `#C9A24B`/bronce `#B08D57`. (El dark mode 2026 NO es invertir: es base casi-negra con tinte cálido.)
- **Piedra + verde profundo:** bg `#EDEAE3` · tinta `#22251F` · acento `#2F4A3C`.

## 4. Motion que se lee como "caro" (timing > efecto)

**El mismo efecto se siente premium, de juguete o mecánico solo por la curva de easing y la duración.** Animación como guarnición, no como plato principal.

- **Image reveal con `clip-path` + scale lento** (la firma de Active Theory/Locomotive): el contenedor recorta `inset(100% 0 0 0)→inset(0)` mientras la `<img>` interior baja de `scale(1.28)→1`, **un poco más lenta** que la cortina (1.3s vs 1.6s, empezando juntas). La imagen NUNCA aparece con fade de opacidad.
- **Texto:** titulares con reveal por línea con máscara (`overflow:hidden` + `yPercent:115→0`); párrafos largos NO se animan por línea (pretencioso) — fade o blur-in del bloque.
- **Smooth scroll Lenis** calibrado: `duration:1.1`, easing expo. >1.4 se siente flotante/lento.
- **Hover refinado:** escala ≤1.06 dentro de `overflow:hidden`; underline que entra por un lado y sale por el otro (cambia `transform-origin` right→left); magnético factor **≤0.25** (no 0.5). Entrada 0.3–0.4s, **salida más lenta** 0.5–0.7s.
- **Easings PRO** (casi siempre `out`/`inOut`): `expo.out` = `cubic-bezier(.16,1,.3,1)` (hero) · `power3.out` = `cubic-bezier(.22,1,.36,1)` · transiciones `cubic-bezier(.76,0,.24,1)`.
- **Duraciones:** micro-hover .3–.4s · reveal elemento .8–1s · reveal imagen grande 1.2–1.6s · stagger .06–.12s.
- **Siempre `once:true`** en reveals de entrada (re-animar al scrollear es el tic de plantilla). **Siempre** respetar `prefers-reduced-motion` (desactivar Lenis con `lerp:1`, quitar clip/scrub, dejar todo visible).

## 5. Estructura CRO para landings de servicio (alta conversión)

Orden: **Hero** (beneficio + zona/ciudad + 1 CTA + foto real + micro-confianza) → **barra de confianza** (licencia, seguro, garantía, años, # proyectos, ★ rating) → **servicios** (separa rutas: alto ticket vs mantenimiento rápido) → **antes/después real** (driver #1; mejor video) → **proceso numerado** → **prueba social** (testimonios con nombre) → **garantía + financiación + zonas** → **cotización** (form corto 3–4 campos + WhatsApp + sticky CTA) → **FAQ** (mata objeciones) → **footer con NAP**.
- CTA repetido cada ~1.5 pantallas + sticky bar siempre visible. Mobile-first (70% del tráfico) y <3s de carga: innegociables.
- Copy humano (como habla el cliente, sin jerga), CTAs específicos ("Agenda tu visita gratis", no "Enviar"), oferta clara, urgencia honesta. Transparencia de precios/rangos genera confianza.
- Señales de confianza verificables (licencia con número, seguro, garantía escrita) son lo que más convierte en nichos de "dejo entrar gente a mi casa y gasto mucho".

## 6. Lista negra — lo que se ve barato / "IA" / dated (evitar)

- Blanco puro `#FFFFFF` + azul corporativo plano → "plantilla de contratista".
- Gradiente violeta→cian (`#8B5CF6`→`#06B6D4`) → bandera de "hecho por IA".
- Stock genérico ("constructor con casco sonriendo") → mata credibilidad al instante.
- Grids de cuadrados uniformes sin jerarquía; sombras drop-shadow gruesas; bordes muy redondeados → estética SaaS barata.
- Motion gimmick: rebotes `back`/`elastic` con overshoot, parallax pesado/mareante, carruseles automáticos rápidos, cursores enormes con partículas, blur pesado sobre párrafos, animaciones que re-disparan al scrollear.
- Misma sans para todo (look "dashboard genérico"); demasiadas fuentes/colores/iconos; Y2K/chrome/pixel ya fatigados.
- CTAs múltiples gritando ("¡Llama ya!" + "¡WhatsApp!" + "¡Cotiza!") sin jerarquía; emojis y signos de exclamación en titulares de marca premium.

## 7. Tres moodboards listos para usar

1. **Atelier** (editorial revista de arquitectura) — crema `#F0EEE9` + tinta + terracota `#C26B4A` + sage; Fraunces/Canela + Söhne/Instrument Sans; smooth scroll, reveals con stagger, full-bleed, hover lento. *La apuesta más segura y diferenciadora.*
2. **Materia oscura** (lujo, materiales nobles) — base `#09090B`/`#18181B` + latón `#C9A24B`; Tiempos/Fraunces dorado + Aeonik; page transitions con barrido, parallax sutil sobre madera/mármol, grano cinematográfico.
3. **Casa cálida** (lifestyle premium, cercano) — `#EDEAE3` + verde bosque `#2F4A3C` + clay; Editorial New + Neue Montreal; anti-grid editorial, fades cálidos, luz natural dorada full-bleed.

---

**Regla de oro de este archivo:** cuando el usuario pida algo "más profesional / estético / moderno", la respuesta NO es agregar más efectos — es **subir la dirección de arte**: mejor tipografía y jerarquía, más whitespace, fotografía full-bleed, paleta cálida disciplinada, grano sutil, y motion lento y contenido. Menos, pero impecable.
