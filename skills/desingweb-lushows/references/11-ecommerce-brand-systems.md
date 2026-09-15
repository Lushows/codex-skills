# 11 — E-commerce & sistemas de marca DTC (cómo vender impactando)

Síntesis de la frontera 2026 en páginas de producto premium de marcas DTC (AG1/Athletic Greens, Seed, Ritual, Moon Juice, Aesop, Glossier, Liquid Death, Graza, Magic Spoon, Recess) + ganadores Awwwards/FWA e-commerce. **La tesis: la PDP premium ya no es una ficha de compra utilitaria — es una película de marca scrolleable con un riel de compra pegajoso.** La imagen vende tanto como el producto. Esta referencia se usó para construir la página de BIO-SETA (Melena de León).

---

## 1. Anatomía "momento de marca antes de vender" (orden de secciones que convierte)

El error de la mayoría: arrancar con la grilla de producto/buy-box arriba. Las marcas globales **abren con un manifiesto visual** y dejan que el riel sticky (barra add-to-cart móvil / columna derecha desktop) cargue precio+CTA durante TODO el scroll, para que el momento de marca nunca cueste la venta.

1. **Hero / declaración de marca (80–100vh).** UNA afirmación gigante sobre la *transformación* (no la feature). Empaque-como-héroe (foto del producto protagonista). UN CTA suave. La tipografía hace el trabajo: 1 línea, `clamp(2.5rem,7vw,7rem)`, tracking `-.02em`/`-.04em`. Sin lista de features todavía.
2. **Tira de prueba bajo el fold (primeros 600px).** Badges de confianza aquí reciben ~3.4× más engagement que abajo: ★ rating + nº reseñas, "como se vio en", certificaciones (testeo de 3ros, vegano, original). Capa de *facilidad cognitiva* estilo AG1.
3. **El problema / "por qué existe".** Cliente = héroe, problema = villano, marca = guía. Copy editorial + 1 imagen grande. El encuadre personal/específico convierte más que la estadística de mercado.
4. **Ingrediente / mecanismo.** La transparencia gana: desglose con cantidades, origen, *call-outs con líneas conectoras* sobre el render. Declarar protocolos de testeo puede subir CVR ~156% en suplementos.
5. **Prueba social.** Reseñas que citan *resultados específicos* convierten ~2.8× vs elogio genérico. UGC en video, antes/después, nota del fundador.
6. **Suscripción como *control*** ("salta, cambia, cancela cuando quieras"), nunca como default forzado (el sub forzado baja CVR aunque suba LTV).
7. **Garantía + FAQ en acordeón** (disclosure progresivo; ~73% de compras wellness son móvil).
8. **CTA final** repitiendo el empaque-héroe.

**CRO horneado:** rating sobre el fold · CTA sticky siempre visible · cards de bundle/best-seller seleccionables · video hero 30–60s (emocional > spec). Las 5 columnas de confianza (certs, lab tests, reseñas reales, móvil, value-prop claro) reportan hasta +312% CVR vs páginas incompletas.

> **En BIO-SETA aplicamos:** hero cinemático oscuro con frasco flotante → marquee → PDP con buy-box + sticky bar → manifiesto con contadores → trust strip → beneficios numerados → "el hongo" editorial → ritual → reseñas → colección/cross-sell → FAQ → CTA final de marca.

## 2. Dos mundos de identidad DTC (elige UNO, comprométete)

- **A. Mundo mono-color audaz** (Graza verde, Magic Spoon violeta, Liquid Death negro-metal, Recess pastel). UN color de marca saturado y apropiable, inundando edge-to-edge — el color *es* la marca. Voz casual y humana. Ideal Gen-Z / consumibles divertidos. Paletas para versionar:
  - Graza: oliva `#1F5C2E`, crema `#F4EFE1`, acento `#FF5C39`.
  - Recess (calma pastel): lavanda `#C9B8E8`, durazno `#FFD2B8`, menta `#B8E0C8`, off-white `#FBF7F2`.
  - Magic Spoon (candy-pop): violeta `#6B4EFF`, rosa `#FF4FA3`, cyan `#36D6E7` sobre casi-negro.
- **B. Neutros editoriales** (Aesop, Glossier, Ritual). Tierra apagada + 1 neutro héroe, tratado como galería. Aesop: marrón ámbar `#6B4A2B`, hueso `#E8E2D6`, tinta `#1A1A17`, espacio negativo abundante, producto como escultura. Ideal prestigio/beauty/longevidad.

**BIO-SETA** mezcló ambos: mundo oscuro inmersivo (violeta noche `#190E27` + oro `#C9A24B`) para el hero/marca + crema editorial `#F0EAE0` para el cuerpo. Funciona porque cada zona se compromete con una.

## 3. Foto de producto que se ve "cara" en web

- **Producto flotante + sombra de contacto suave.** Nunca elipse dura; nunca flotar SIN sombra (lee a "IA falsa"). La sombra "restaura la física" y dispara el impulso de compra.
- **Pedestal/escenario en gradiente.** Luz desde abajo/lados → centro brillante que cae a bordes oscuros = profundidad cinematográfica. Un producto, un pedestal, centrado, sin clutter = lujo por defecto.
- **PNG recortado (fondo transparente)** sobre campos de color de marca o fondos oscuros.
- **Call-outs con líneas conectoras finas** al render para la narrativa de ingredientes.
- **Motion:** giro 360, rotación scrubbeada al scroll, empaque que hace parallax contra la tipografía.

### ⚙️ Receta de producción: recortar fondo blanco (renders Higgsfield/IA)
Los renders suelen venir sobre blanco. `mix-blend-mode:multiply` los limpia **solo sobre fondos claros**; sobre un hero OSCURO necesitas transparencia real. Genera el recorte con `sharp` (umbral por brillo + saturación):

```js
// node _cutout.js  (sharp). Quita blanco/gris-claro -> alpha 0, con borde suave.
const sharp = require('sharp');
async function cutout(src,out){
  const {data,info}=await sharp(src).ensureAlpha().raw().toBuffer({resolveWithObject:true});
  const {width,height,channels}=info, px=Buffer.from(data);
  for(let i=0;i<px.length;i+=channels){
    const r=px[i],g=px[i+1],b=px[i+2];
    const bright=(r+g+b)/3, sat=Math.max(r,g,b)-Math.min(r,g,b);
    if(bright>236 && sat<16) px[i+3]=0;                          // fondo -> transparente
    else if(bright>205 && sat<26) px[i+3]=Math.max(0,Math.round(255-(bright-205)*(255/31))); // borde suave
  }
  await sharp(px,{raw:{width,height,channels}}).png().toFile(out);
}
```
Regla: **multiply para tarjetas claras, PNG transparente para heros oscuros.** Verifica el recorte con el visor antes de embeberlo.

## 4. Confianza & conversión (suplementos/wellness/consumibles)

- ★ Rating + nº sobre el fold; certs en los primeros 600px.
- Reseñas con resultados medibles (energía, sueño, enfoque) > genéricas; sube 3–5 al copy del hero.
- Citas clínicas/de practicantes + links a lab-tests = el foso de transparencia.
- Antes/después + testimonios en video; muro de prensa "como se vio en".
- Suscripción = lenguaje de control; cards de bundle; garantía con número ("60 días").
- Móvil-first, disclosure progresivo (acordeones), touch targets ≥44px.
- **Checkout por WhatsApp** (LatAm): arma el mensaje con el pedido codificado (`wa.me/<num>?text=...`), contra-entrega como señal de confianza local.

## 5. Frescura 2026 (esto lee NUEVO, no cliché 2022)

- **Bento grids evolucionados** — default high-end para PDPs/bloques densos (linaje Apple/Linear/Notion). 1 celda héroe ancha + celdas asimétricas de apoyo.
- **Maximalismo editorial** — color rico, capas superpuestas, tipo gigante, composiciones densas reemplazando al minimalismo apagado.
- **Textura granulada/táctil** — overlay de grano SVG/CSS sobre rellenos sólidos → sensación fílmica/papel impreso (barato, sin lag WebGL).
- **Coreografía motion-on-scroll** — Lenis + GSAP ScrollTrigger, stages `pin:true` donde el scroll avanza *el tiempo* (el producto se arma, los ingredientes vuelan), `scrub:1.1`, snap para ritmo.
- **Anti-design/brutalismo como acento** — HTML crudo, monoespaciada, marcas hechas a mano que rechazan el gloss perfecto de IA (con moderación, como personalidad).
- **Fuentes variables + tipo cinética** como estándar, no garnish.

## 6. Lista negra e-commerce (se ve barato / "IA" / dated)

- Formas serpenteantes, gradientes con glow, "estallidos de luz", frutas/vegetales glossy con splash → el delator de suplemento legacy.
- Sombra elíptica dura, o producto flotado por IA **sin sombra**.
- Hero stock centrado + bullets de features apilados ANTES de cualquier momento de marca.
- Suscripción default forzada; pop-ups antes de mostrar valor.
- Sopa de badges arcoíris, countdowns falsos, "#1 del mundo" sin prueba.
- Minimalismo plano sin textura (hoy lee estéril) → agrega grano.
- Carruseles hero, gradientes full-width turbios, spacing del tema Shopify default.
- Fila de "3 íconos features" estilo Bootstrap, body en system-font, bullets con emoji genérico.
- Todo sobre-animado (motion sin coreografía); stutter por no sincronizar Lenis con el ticker de GSAP.

---

## Métricas por defecto (aplicar mañana)

```
Padding vertical sección:  clamp(80px, 12vh, 160px)
Ancho contenido:           1200–1280px · gutters 1.5–2rem
Body:                      16–18px · line-height 1.5–1.65 · medida 60–70ch
Tracking titular:          -.02em
Reveal:                    .6–.9s · cubic-bezier(.16,1,.3,1) · stagger .06–.1s
Scrub scroll:              1.1
Grano:                     opacity 4–8%
```

## ⚠️ Bug de producción aprendido (motion + reveals)
`gsap.from(el,{opacity:0})` lee el valor **actual** como destino. Si el CSS ya tiene `.reveal{opacity:0}`, anima de 0→0 y el elemento queda invisible para siempre. **Usa `gsap.fromTo(el,{opacity:0,y:40},{opacity:1,y:0,...})`** con destino explícito. Además: al testear con Lenis activo, `scrollIntoView()` nativo NO actualiza ScrollTrigger (deja reveals colgados) — usa `lenis.scrollTo(el)` o el clic de ancla cableado a Lenis.
