# 02 — Sistemas de Color (Color Systems)

Guía de sistemas de color premium para web de élite: paletas nombradas listas para producción, arquitectura de tokens CSS, gradient mesh, dark mode y accesibilidad AA.

---

## 1. Cómo construir tokens CSS

Toda paleta debe exponerse como **tokens semánticos** (qué hace el color) apoyados en **tokens primitivos** (qué color es). El semántico es lo que consumes en componentes; el primitivo es lo que cambias al re-tematizar.

### 1.1 Tokens semánticos mínimos

```css
:root{
  /* Superficies */
  --color-bg:        #07120E;   /* fondo de página */
  --color-surface:   #0F1F18;   /* tarjetas, paneles */
  --color-surface-2: #16291F;   /* surface elevada / hover */
  --color-border:    #25382E;   /* divisores, outlines */

  /* Texto */
  --color-text:      #E8F5EE;   /* texto principal */
  --color-text-muted:#A7BFB3;   /* secundario, captions */
  --color-text-inv:  #07120E;   /* texto sobre accent */

  /* Marca */
  --color-accent:    #34D399;   /* acción primaria */
  --color-accent-2:  #A7F3D0;   /* acción secundaria / glow */
  --color-muted:     #5B7A6B;   /* deshabilitado, placeholder */

  /* Estados */
  --color-success:#34D399; --color-warning:#FBBF24;
  --color-danger:#F87171;  --color-info:#60A5FA;
}
```

### 1.2 Reglas de nomenclatura

| Capa | Prefijo | Ejemplo | Se consume en componentes |
|------|---------|---------|---------------------------|
| Primitivo | `--c-` / escala | `--c-green-500` | No (solo dentro de tokens) |
| Semántico | `--color-` | `--color-accent` | Sí |
| Componente | `--btn-` | `--btn-bg` | Solo en ese componente |

Patrón recomendado: el semántico **referencia** al primitivo.

```css
:root{
  --c-green-500:#34D399;
  --color-accent: var(--c-green-500); /* re-tematizar = cambiar 1 línea */
}
```

### 1.3 Escala 50–900 (cómo generarla)

Una escala se construye fijando un **color base** (normalmente el paso 500) y variando **luminosidad** (en HSL o, mejor, en OKLCH) manteniendo el matiz casi constante y ajustando la saturación: más saturación en los tonos medios, menos en los extremos.

Tabla de pasos para generar una escala desde un color base (base = paso 500):

| Paso | Uso típico | L (lightness) aprox. | Saturación vs base | Cómo obtenerlo desde el base |
|------|-----------|----------------------|--------------------|------------------------------|
| 50   | fondos sutiles, washes | ~97% | −40% | base mezclado 92% con blanco |
| 100  | hover claro, badges | ~93% | −30% | base mezclado 82% con blanco |
| 200  | bordes claros | ~86% | −20% | base mezclado 68% con blanco |
| 300  | disabled claro | ~76% | −10% | base mezclado 50% con blanco |
| 400  | iconos secundarios | ~66% | −5%  | base mezclado 25% con blanco |
| 500  | **BASE / accent** | ~56% | 0% | el color base tal cual |
| 600  | hover de accent | ~48% | +3%  | base mezclado 15% con negro |
| 700  | active / pressed | ~40% | +5%  | base mezclado 30% con negro |
| 800  | texto sobre claro | ~30% | +5%  | base mezclado 50% con negro |
| 900  | fondos profundos dark | ~20% | +3%  | base mezclado 70% con negro |

Con CSS moderno puedes derivar la escala sin pre-calcular usando `color-mix`:

```css
:root{
  --base:#34D399;
  --c-50:  color-mix(in oklab, var(--base) 8%,  white);
  --c-100: color-mix(in oklab, var(--base) 18%, white);
  --c-200: color-mix(in oklab, var(--base) 32%, white);
  --c-300: color-mix(in oklab, var(--base) 50%, white);
  --c-400: color-mix(in oklab, var(--base) 75%, white);
  --c-500: var(--base);
  --c-600: color-mix(in oklab, var(--base) 85%, black);
  --c-700: color-mix(in oklab, var(--base) 70%, black);
  --c-800: color-mix(in oklab, var(--base) 50%, black);
  --c-900: color-mix(in oklab, var(--base) 32%, black);
}
```

> Tip de élite: trabaja la escala en **OKLCH** (`oklch(L C H)`). A diferencia de HSL, la luminosidad percibida es uniforme entre matices, así que los pasos se ven "iguales de oscuros" entre verde, azul y rojo.

---

## 2. Paletas premium (8+)

Cada paleta trae su bloque de tokens listo para pegar. Mezcla dark-tech, editorial claro, luxury, pastel, brutalist, retail, fintech y organic.

### 2.1 Dark-tech

```css
/* Paleta: "Emerald Lab" */
:root{
  --color-bg:#07120E; --color-surface:#0F1F18; --color-text:#E8F5EE;
  --color-accent:#34D399; --color-accent-2:#A7F3D0; --color-muted:#5B7A6B;
}
```

```css
/* Paleta: "Midnight Cobalt" (dark-tech, glow azul) */
:root{
  --color-bg:#070B16; --color-surface:#0E1424; --color-surface-2:#161E33;
  --color-text:#E6ECFF; --color-text-muted:#9AA8CC; --color-border:#222B45;
  --color-accent:#5B8DEF; --color-accent-2:#8AB4FF; --color-muted:#4A5578;
}
```

### 2.2 Editorial claro

```css
/* Paleta: "Editorial Ink" (claro, alto contraste, prensa digital) */
:root{
  --color-bg:#FBFAF7; --color-surface:#FFFFFF; --color-surface-2:#F2F0EA;
  --color-text:#16140F; --color-text-muted:#5C574C; --color-border:#E2DED4;
  --color-accent:#C2410C; --color-accent-2:#1D4ED8; --color-muted:#9C9486;
}
```

### 2.3 Luxury

```css
/* Paleta: "Noir Gold" (luxury, negro profundo + oro) */
:root{
  --color-bg:#0B0B0C; --color-surface:#151517; --color-surface-2:#1E1E21;
  --color-text:#F5F2EA; --color-text-muted:#B6B0A1; --color-border:#2C2C30;
  --color-accent:#C8A04B; --color-accent-2:#E6CE8E; --color-muted:#6E6857;
}
```

### 2.4 Pastel

```css
/* Paleta: "Soft Studio" (pastel, suave, lifestyle/beauty) */
:root{
  --color-bg:#FDF7F4; --color-surface:#FFFFFF; --color-surface-2:#F7EDF1;
  --color-text:#3A2F33; --color-text-muted:#8A7A80; --color-border:#F0E1E7;
  --color-accent:#E8A0BF; --color-accent-2:#A8C5E0; --color-muted:#C9B6BD;
}
```

### 2.5 Brutalist

```css
/* Paleta: "Raw Concrete" (brutalist, alto contraste, sin curvas suaves) */
:root{
  --color-bg:#FAFAF5; --color-surface:#FFFFFF; --color-surface-2:#ECEAE1;
  --color-text:#0A0A0A; --color-text-muted:#3D3D3D; --color-border:#0A0A0A;
  --color-accent:#FF4D00; --color-accent-2:#1500FF; --color-muted:#7A7A70;
}
```

### 2.6 Retail / e-commerce

```css
/* Paleta: "Market Coral" (retail, cálido, conversión) */
:root{
  --color-bg:#FFFFFF; --color-surface:#FFFBFA; --color-surface-2:#FFF1EE;
  --color-text:#221A18; --color-text-muted:#6B5A55; --color-border:#F0DBD5;
  --color-accent:#FF5A3C; --color-accent-2:#0EA5A0; --color-muted:#C2A79F;
}
```

### 2.7 Fintech

```css
/* Paleta: "Vault Indigo" (fintech, confianza, datos densos) */
:root{
  --color-bg:#0A0C12; --color-surface:#121622; --color-surface-2:#1A2030;
  --color-text:#EAEEF7; --color-text-muted:#94A0B8; --color-border:#252C3D;
  --color-accent:#6366F1; --color-accent-2:#22D3A8; --color-muted:#4A5468;
}
```

### 2.8 Organic / natural

```css
/* Paleta: "Terra Sage" (organic, tierra + salvia, wellness/alimentos) */
:root{
  --color-bg:#F7F4EC; --color-surface:#FFFFFF; --color-surface-2:#EEE9DB;
  --color-text:#2B2A20; --color-text-muted:#6F6A57; --color-border:#DED7C4;
  --color-accent:#7A8B5A; --color-accent-2:#C08552; --color-muted:#A8A38C;
}
```

### 2.9 Extra — neón saturado

```css
/* Paleta: "Cyber Magenta" (dark-tech, neón, gaming/creative) */
:root{
  --color-bg:#0A0410; --color-surface:#160A22; --color-surface-2:#21103300;
  --color-text:#F4E9FF; --color-text-muted:#B79ED0; --color-border:#33204A;
  --color-accent:#E839FF; --color-accent-2:#22E0FF; --color-muted:#6B4D85;
}
```

---

## 3. Gradient mesh (técnica)

El **gradient mesh** simula los degradados orgánicos de herramientas de diseño superponiendo varios `radial-gradient` con posiciones, tamaños y colores distintos, opcionalmente difuminados con `filter: blur()`. Es la base de los fondos "aurora" de webs premium (Linear, Stripe, Vercel).

### 3.1 Mesh estático con múltiples radial-gradient

```css
.mesh{
  position:relative;
  background-color:#07120E;
  background-image:
    radial-gradient(40% 50% at 15% 20%, rgba(52,211,153,.55) 0%, transparent 60%),
    radial-gradient(45% 55% at 85% 15%, rgba(99,102,241,.45) 0%, transparent 60%),
    radial-gradient(50% 60% at 70% 85%, rgba(34,224,255,.40) 0%, transparent 65%),
    radial-gradient(35% 45% at 25% 80%, rgba(167,243,208,.35) 0%, transparent 60%);
  background-repeat:no-repeat;
}
```

### 3.2 Mesh con blur (look más orgánico)

Pon las manchas en una capa separada y aplícale `blur` grande; así los bordes de cada `radial-gradient` se funden sin pixelar el contenido.

```css
.mesh-bg{ position:relative; overflow:hidden; background:#070B16; }

.mesh-bg::before{
  content:"";
  position:absolute; inset:-20%;
  background:
    radial-gradient(30% 30% at 20% 30%, #5B8DEF 0%, transparent 70%),
    radial-gradient(35% 35% at 80% 25%, #22E0FF 0%, transparent 70%),
    radial-gradient(40% 40% at 60% 80%, #8AB4FF 0%, transparent 70%);
  filter:blur(80px);
  opacity:.6;
  z-index:0;
}

.mesh-bg > *{ position:relative; z-index:1; } /* contenido por encima del gradient */
```

### 3.3 Mesh animado (aurora viva)

```css
@keyframes meshDrift{
  0%   { transform:translate(0,0)        scale(1);   }
  50%  { transform:translate(4%, -3%)    scale(1.1); }
  100% { transform:translate(0,0)        scale(1);   }
}
.mesh-bg::before{ animation:meshDrift 18s ease-in-out infinite; }

@media (prefers-reduced-motion: reduce){
  .mesh-bg::before{ animation:none; }
}
```

> Performance: anima solo `transform`/`opacity` de la capa de gradient (compositable en GPU), nunca las posiciones `at x% y%` de cada radial-gradient (forzarían repaint).

---

## 4. Reglas de dark mode

1. **No uses negro puro (#000) para el fondo.** Usa un tono muy oscuro tintado hacia el accent (ej. `#07120E` verdoso). El negro puro genera halos y fatiga visual sobre pantallas OLED brillantes.
2. **No uses blanco puro (#FFF) para el texto** sobre dark. Usa `#E8F5EE`/`#EAEEF7` (~90% L) para reducir el deslumbramiento.
3. **Eleva con luz, no con sombra.** En dark las superficies más "altas" son más **claras** (`--color-surface-2` > `--color-surface` > `--color-bg`), porque las sombras casi no se ven.
4. **Baja la saturación de los accent saturados** en dark (un coral 100% saturado vibra y cansa); súbela ligeramente en light.
5. **Implementación**: define ambos esquemas y respeta la preferencia del SO; permite override manual con `data-theme`.

```css
:root{ color-scheme: light dark; }

/* Light por defecto */
:root{
  --color-bg:#FBFAF7; --color-surface:#FFFFFF; --color-text:#16140F;
  --color-accent:#0E7C66;
}

/* Dark según SO */
@media (prefers-color-scheme: dark){
  :root{
    --color-bg:#07120E; --color-surface:#0F1F18; --color-text:#E8F5EE;
    --color-accent:#34D399;
  }
}

/* Override manual (toggle del usuario) */
[data-theme="dark"]{
  --color-bg:#07120E; --color-surface:#0F1F18; --color-text:#E8F5EE; --color-accent:#34D399;
}
[data-theme="light"]{
  --color-bg:#FBFAF7; --color-surface:#FFFFFF; --color-text:#16140F; --color-accent:#0E7C66;
}
```

---

## 5. Contraste y accesibilidad (WCAG AA)

WCAG AA exige **4.5:1** para texto normal y **3:1** para texto grande (≥24px, o ≥18.66px bold) y para componentes UI / iconos significativos. AAA pide 7:1.

### 5.1 Reglas prácticas

- **Texto principal sobre fondo**: siempre verifica ≥ 4.5:1. Texto muted incluido — no bajes de 4.5:1 solo porque "es secundario".
- **Texto sobre el accent** (botón primario): elige `--color-text-inv` (negro o blanco) según cuál dé más contraste contra el accent. Verifica el par real.
- **No comuniques estado solo con color.** Añade icono, texto o patrón (daltonismo). Ej.: error = color rojo **+** icono **+** mensaje.
- **Focus visible**: outline de ≥ 3:1 contra el fondo adyacente y ≥ 2px de grosor.

```css
:focus-visible{
  outline:2px solid var(--color-accent);
  outline-offset:2px;
}
```

### 5.2 Verificación rápida de pares

| Par a verificar | Mínimo |
|-----------------|--------|
| `--color-text` sobre `--color-bg` | 4.5:1 |
| `--color-text-muted` sobre `--color-bg` | 4.5:1 |
| texto del botón sobre `--color-accent` | 4.5:1 |
| `--color-border` / iconos sobre `--color-surface` | 3:1 |
| outline de focus sobre fondo adyacente | 3:1 |

Herramientas: DevTools (panel de contraste en el color picker), WebAIM Contrast Checker, o `APCA` para una evaluación percibida más fina. En CI puedes auditar con Lighthouse/axe.

> Regla de oro: si la paleta es bonita pero un par no llega a 4.5:1, **ajusta la luminosidad del token** (sube/baja con `color-mix` hacia blanco/negro) antes de aceptar el diseño. La accesibilidad no es opcional.
