# 157 — Gradientes y color generativo

Un buen gradiente se ve como una transición de luz natural; uno malo tiene una "zona gris muerta" en el medio o colores que chillan. Y el color generativo — paletas creadas por algoritmo — es una de las firmas visuales de las marcas más frescas de hoy (Stripe, Linear, Vercel, Arc). Este módulo te enseña a hacer gradientes que se vean caros y a usar color algorítmico sin caer en el cliché de "blob morado de startup". Continúa el 37 gradientes y color avanzado con la tecnología 2026.

## Por qué tus gradientes se ven sucios
Cuando vas de un color a otro, el navegador interpola por defecto en sRGB, y eso suele PASAR POR EL GRIS. Ejemplo clásico: azul → amarillo en sRGB pasa por un gris-verdoso lavado en el medio. Feo.

La solución (2026): interpolar en un **espacio perceptual** como OKLCH (ver 154). El gradiente mantiene brillo y saturación parejos en TODO el recorrido. Sin zona muerta.

```css
/* sucio (sRGB por defecto) */
background: linear-gradient(90deg, #2563eb, #f59e0b);

/* limpio: interpolación en OKLCH */
background: linear-gradient(in oklch 90deg, #2563eb, #f59e0b);

/* aún más vivo: ruta de matiz larga, colores luminosos todo el recorrido */
background: linear-gradient(in oklch longer hue 90deg,
  oklch(65% 0.2 250), oklch(80% 0.18 90));
```
`in oklch`, `in oklab` o `in hsl` cambian el espacio. `longer hue` / `shorter hue` deciden por qué lado del círculo de color gira. Esta es la mejora más fácil y de mayor impacto que puedes hacer hoy.

## Tipos de gradiente y cuándo usarlos
| Tipo | CSS | Para qué |
|---|---|---|
| **Lineal** | `linear-gradient()` | Fondos, botones, sutilezas |
| **Radial** | `radial-gradient()` | Focos de luz, viñetas, halos |
| **Cónico** | `conic-gradient()` | Gráficos, ruedas, efectos |
| **Mesh** (malla) | Varios radiales superpuestos / SVG | Fondos ricos y orgánicos tipo Stripe |

### Mesh gradient (el "fondo caro")
Un **mesh gradient** mezcla varias manchas de color suaves en distintas posiciones, creando un fondo fluido y orgánico. Se logra apilando varios `radial-gradient` translúcidos:
```css
.hero {
  background:
    radial-gradient(at 20% 30%, oklch(70% 0.18 280 / .6), transparent 50%),
    radial-gradient(at 80% 20%, oklch(72% 0.16 200 / .5), transparent 50%),
    radial-gradient(at 50% 80%, oklch(75% 0.15 330 / .5), transparent 50%),
    oklch(20% 0.03 280);
}
```

## Reglas para gradientes premium
- [ ] **Pocos colores** (2–3). Más = arcoíris baboso.
- [ ] **Colores ANÁLOGOS o cercanos en matiz** se ven sofisticados; opuestos puros son arriesgados (ver 30 teoría del color).
- [ ] **Interpola en OKLCH** para evitar la zona muerta.
- [ ] **Ángulo con intención** (la luz suele venir de arriba: 180deg o diagonales suaves).
- [ ] **Sutil > dramático** para fondos de UI; dramático solo para héroes/portadas.
- [ ] **Texto encima:** verifica contraste sobre la zona MÁS clara y la MÁS oscura del gradiente (ver 35, 156).
- [ ] **Cuidado con el banding** (escalones visibles): añade un poco de ruido/grano si aparece en pantallas grandes.

## Color generativo / algorítmico
Es construir color por REGLAS, no eligiendo a mano cada tono. Usos de marca:
1. **Escalas sistemáticas** (ver 154): fija L y C, gira el matiz H por algoritmo → familia infinita coherente.
2. **Color por dato:** asignar un color único y repetible a cada usuario/proyecto a partir de su nombre (hash → matiz). Los avatares de colores de GitHub/Linear funcionan así.
3. **Fondos generativos:** mesh o patrones que cambian por semilla, siempre dentro de la paleta de marca.
4. **Arte de marca paramétrico:** identidades "vivas" (ver el caso de marcas como la del MIT Media Lab) donde un sistema genera variaciones infinitas con reglas fijas.

```css
/* color repetible a partir de un id (se calcula el matiz, L y C fijos de marca) */
/* h = (hash(nombre) % 360); */
.avatar { background: oklch(65% 0.15 var(--h)); }
```

## Anti-cliché (qué EVITAR)
- El gradiente morado→rosa→azul "de toda startup 2018–2021". Está quemadísimo.
- Mesh genéricos que vienen en plantillas (todos los han visto).
- Gradientes en TODO (logo, botones, texto, iconos). Elige uno o dos lugares.
- Color generativo sin restringir a la paleta de marca → caos de tonos.
Para diferenciarte: ancla el gradiente en TU paleta (33, 34), no en la moda; usa un matiz inesperado; combínalo con grano/textura o con tipografía fuerte para que sea TUYO.

## Ejemplo trabajado
SaaS con marca índigo `oklch(55% 0.2 270)`. Para el hero: mesh de 3 radiales en índigo, violeta `oklch(60% 0.18 300)` y cian `oklch(70% 0.14 220)` sobre fondo `oklch(18% 0.04 270)`, interpolado en OKLCH → fondo profundo, fluido, sin gris muerto, claramente "de la marca" y no del template. Avatares de usuario con color generativo (L y C fijos de marca, matiz por hash del nombre) → coherentes y únicos. Botones con gradiente lineal sutil índigo→violeta `in oklch`. Cero morado-rosa cliché.

## Siguiente paso
Reescribe tus gradientes actuales añadiendo `in oklch` y reduce a 2–3 colores anclados en tu paleta (154, 33). Si usas color por usuario/categoría, fija L y C de marca y deja que solo el matiz varíe por algoritmo. Verifica contraste del texto sobre las zonas extremas (156).
