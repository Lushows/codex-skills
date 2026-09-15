# 167 — Color engineering (OKLCH, P3, contraste)

**CRAFT, code-heavy.** El lado técnico/matemático (distinto de paletas/02): OKLCH, P3 wide-gamut, contraste APCA, generación de escalas, CSS Color 4/5. Pareja de 02 (color systems), 148 (gradients/glow), 15 (tokens), 16 (a11y). Regla de oro: **guarda el token en OKLCH nunca en hex; deriva todo de un seed con relative color; interpola gradientes `in oklch` (no sRGB, que cruza el gris muerto).**

## 1. OKLCH/OKLab — por qué ganó

Hex/RGB y HSL **no son perceptualmente uniformes**: en HSL `hsl(60 100% 50%)` (amarillo) y `hsl(240 100% 50%)` (azul) comparten `L=50%` pero el amarillo se ve luminoso y el azul casi negro → una rampa variando `L` tiene saltos irregulares y los gradientes cruzan una **zona gris muerta**. OKLab (Ottosson 2020) resuelve: distancias iguales ≈ diferencias iguales *percibidas*. OKLCH = forma cilíndrica: **L** (lightness perceptual 0-100%, igual L = igual luminosidad sin importar el hue), **C** (chroma 0 a ~0.37), **H** (hue 0-360). `oklch(70% 0.15 250)`. **Workflow brand-hex → OKLCH:** no a mano — usa oklch.com o `culori`: `oklch("#3b82f6")` → `{l:0.62, c:0.19, h:259}`. Guarda el token en OKLCH; todo lo demás se deriva.

## 2. Generando escalas (la rampa 1→12)

Técnica Radix/Tailwind: 12 pasos (1-2 fondos sutiles, 3-5 componentes/hover, 6-8 bordes, 9 sólido principal, 11-12 texto). Clave: **L en pasos perceptualmente uniformes** y **C sube hacia el medio y baja en los extremos** (claros/oscuros no soportan chroma alto sin salirse del gamut):
```js
import { oklch, formatCss, clampChroma } from "culori";
function ramp(seedHex){
  const base = oklch(seedHex);
  const Ls = [0.98,0.95,0.91,0.86,0.80,0.72,0.64,0.56,base.l,0.46,0.38,0.27];
  return Ls.map((l,i)=>{ const t=i/11; const cScale = 1 - Math.abs(0.72-t)*1.1; // campana, pico ~paso 9
    return formatCss(clampChroma({mode:"oklch", l, c: base.c*Math.max(cScale,0.25), h: base.h}, "oklch")); });
}
```
`clampChroma` reduce C hasta caer dentro del gamut **preservando L y H** (gamut mapping correcto, no el clamp ingenuo de RGB que cambia el hue).

## 3. Wide-gamut P3

sRGB cubre ~35% del visible; **Display P3** (pantallas Apple/OLED desde ~2021) ~25% más, sobre todo verdes/rojos vívidos. OKLCH puede *direccionar* esos colores (si subes C más allá del límite sRGB cae naturalmente en P3):
```css
.accent{ background:#e60073; }                         /* fallback sRGB primero */
@supports (color: oklch(0% 0 0)){ .accent{ background:oklch(63% 0.29 13); } } /* rosa que sRGB no muestra */
@media (color-gamut: p3){ .accent{ background:color(display-p3 0.96 0 0.4); } }
```
Regla: define el fallback sRGB **primero**, luego sobreescribe. Un `C > ~0.21` en rojo/magenta ya sale de sRGB — déjalo, el browser hace gamut mapping en pantallas estrechas.

## 4. Relative color syntax (2026, ~90% soporte)

Cambia cómo se construye un tema: **derivas todo de un token** sin hardcodear hover/tints:
```css
:root{ --brand:oklch(62% 0.19 259); }
.btn{ background:var(--brand); }
.btn:hover{ background:oklch(from var(--brand) calc(l - 0.06) c h); }   /* más oscuro */
.btn-subtle{ background:oklch(from var(--brand) 95% calc(c * 0.4) h); } /* tint */
.btn-ghost{ border:1px solid oklch(from var(--brand) l c h / 25%); }
--brand-tint: color-mix(in oklch, var(--brand) 10%, white);
```
Tema completo desde un acento: define `--brand`, genera surface/border/text con `oklch(from …)` ajustando solo `L`; para dark mode invierte la dirección de `L` sin tocar `C`/`H` — **mantener H constante es lo que hace que un tema se sienta coherente**.

## 5. Contraste — APCA vs WCAG 2

**WCAG 2.x** (ratio 4.5:1 texto, 3:1 grande) usa una fórmula de 1996 que falla en **dark mode** y **texto fino** (aprueba combos ilegibles sobre negro, rechaza claros legibles), pero **sigue siendo el estándar legal** (ADA/EAA). **APCA** (futuro WCAG 3) modela contraste como **Lc** (-108 a +106) considerando polaridad y peso: **Lc 90** texto fino pequeño · **Lc 75** mínimo body · **Lc 60** grande/bold (≈4.5:1) · **Lc 45** UI no-texto. `APCAcontrast(sRGBtoY([20,20,20]), sRGBtoY([255,255,255]))` → ~106. **Estrategia 2026:** pasa WCAG 2.2 AA "para los abogados", tunea a **APCA Silver (Lc 75 body / Lc 60 large)** "para los usuarios"; en OKLCH, texto `L≈0.30` sobre fondo `L≈0.98` cumple cómodo — verifica con APCA, no a ojo.

## 6. Gradients & gamut — el color "caro"

Interpolar **en OKLab/OKLCH**, no sRGB (que cruza el gris muerto):
```css
background: linear-gradient(90deg, #ff0080, #00d4ff);            /* gris muerto en el medio (malo) */
background: linear-gradient(in oklch longer hue, #ff0080, #00d4ff); /* brillante, sin gris (bueno) */
```
`shorter hue` (default) camino corto; `longer hue` barrido arcoíris; `in oklab` (cartesiano) para evitar virajes raros entre colores cercanos. **Banding** en 8-bit → añade grano sutil (noise SVG + `mix-blend-mode:overlay`, ~3-5%; ver ref 147). En P3 el banding es menos visible.

## Color anti-patterns — blacklist
**generar rampas variando `L` en HSL/hex** (pasos perceptuales desiguales, hues 6-8 demasiado oscuros) · **gradientes en sRGB entre colores opuestos** (gris muerto/lodo; siempre `in oklch`/`in oklab`) · **hardcodear hover como otro hex** (usa `oklch(from … calc(l - .06) …)`) · **clamp ingenuo de chroma** —recortar RGB— (desplaza el hue; usa `clampChroma`) · **confiar solo en WCAG 2 en dark mode** (texto ilegible "aprobado"; cross-check APCA Lc) · **subir C uniforme en toda la rampa** (claros/oscuros se salen del gamut y se aplanan) · **olvidar el fallback sRGB** antes de `oklch()`/`color(display-p3 …)` · **cambiar H entre pasos de una misma escala** (la familia se siente "sucia"/incoherente) · **8-bit gradients sin grano** en superficies grandes (banding visible).
