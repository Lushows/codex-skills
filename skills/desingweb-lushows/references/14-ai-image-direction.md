# 14 — Dirección de imagen con IA para web (on-brand, premium, "no-AI")

Playbook 2026 para **dirigir** modelos de imagen IA y obtener imágenes web-ready, consistentes y que NO griten "generado por IA". Pensado para el flujo del usuario (agencia multi-marca, imágenes de producto/marca con Higgsfield/OpenAI/Flux). **Léelo cuando haya que generar o tratar imágenes** (heros, producto, fondos, lifestyle) para integrarlas en una web. Pareja natural de 11 (foto de producto premium) y la receta `sharp` de recorte.

---

## 1. Tool landscape 2026 — qué usar y cuándo

Pipeline multi-modelo: bocetar barato, finalizar con el especialista. Ningún modelo gana en todo.

| Tool / versión | Mejor uso | Fortaleza | Debilidad | Comercial |
|---|---|---|---|---|
| **Midjourney v7/v8** | Hero editorial, lifestyle estilizado, moodboards | Mejor "ojo" compositivo, `--sref`/Omni Reference | Texto pésimo, control espacial débil | Sí (Basic+) |
| **Flux 2 Pro** | Producto color-critical, fotorrealismo | Precisión de color por **hex**, prompts largos | Algo plano sin dirección | Sí |
| **Flux.1 Kontext (Pro/Max)** | **Editing**: cambiar fondo/luz, inpaint, meter producto real | Edita zona preservando contexto/luz/**label** | No es generador from-scratch top | Sí |
| **Nano Banana Pro** (Gemini 3 Image) | Mockups producto, texto legible, 4K nativo | 4K real, texto 94-96% en 30+ idiomas, **14 refs**, 5 personajes consistentes | A veces "limpio"/digital de más | Sí (pago) |
| **Ideogram 3.0** | Texto en imagen, posters, packaging con copy | Texto 90-95% multilínea | Fotorrealismo menor | Sí (pago) |
| **Recraft v3/v4** | Logos, iconos, ilustración, **SVG vectorial nativo** | Único que exporta vectores usables; brand kit, paleta lock | No es para fotografía | Sí (Pro; free NO comercial) |
| **Seedream 4.5/5.0** | Alternativa a NB, multi-ref, batch | Buen fotorrealismo, multi-referencia | Texto por detrás de NB | Sí |
| **Higgsfield (Soul 2.0 / Soul ID)** | **Lifestyle a escala on-brand**, social, lanzamientos | 60+ presets que bloquean look; **Moodboards** (tu identidad); **Soul ID** (personaje consistente) | Menos control fino que ComfyUI | Sí |
| **Adobe Firefly** | Trabajo legal-sensible | **Único con indemnización IP** | Estética conservadora | Sí + indemnización |
| **Magnific / Krea Upscale** | Upscale + "reimagine" detalle | Añade textura de piel/poro real, 4K-16K | Puede alucinar (bajar "creativity") | Según fuente |
| **Krea** | Draft real-time, mezcla modelos | Iteración rápida y barata | — | Sí |
| **Freepik AI Suite** | Hub (Flux/NB/Ideogram + stock + retouch) | Todo en un lugar, barato para agencia | No es frontier propio | Sí |

**Regla legal:** cliente regulado/conservador → **Firefly** (indemnización). Resto → plan de pago = derechos comerciales (Recraft free NO sirve).

## 2. Prompting para resultados PREMIUM y on-brand

Estructura (el orden importa): **[sujeto] + [acción/pose] + [encuadre/lente] + [luz nombrada] + [paleta/mood] + [medio de captura] + [imperfección] + [flags]**. Secreto anti-AI: **no describas cómo se ve, describe cómo fue capturada.**

**(a) Producto en seamless/gradiente:**
```
[product] centered on a smooth grey seamless backdrop, single large softbox upper-left,
soft contact shadow beneath, subtle reflection, shot on Canon R5 100mm macro f/8,
matte surface (no AI shine), color-accurate label, studio e-commerce, 4:5 --style raw
```
Flux 2: añade color exacto → `brand background #0F3D2E`.

**(b) Editorial lifestyle:**
```
candid photo of a woman using [product] in a sunlit kitchen, natural window light from left,
slightly out of focus background, unposed, visible skin texture and pores, muted palette,
shot on Leica Q2 28mm f/2.8, ISO 800 visible grain, 1/60 shutter, in the style of Martin Parr
```
Referenciar **fotógrafos reales** (Eggleston, Parr, Tillmans) humaniza más que "cinematic/editorial".

**(c) Fondo/textura abstracta de marca:**
```
abstract soft-focus gradient texture, deep emerald to charcoal #0F3D2E→#101512, organic grain,
subtle film noise, no subject, minimal, large negative space top-left for headline, matte, 16:9 --style raw --stylize 80
```

**(d) Hero:**
```
wide cinematic hero shot of [scene], shot on ARRI Alexa 35mm anamorphic, low golden side-light
(motivated, single source), shallow depth, atmospheric haze, intentional empty space for copy,
muted brand palette, 16:9 --ar 21:9 --style raw
```

**Vocabulario que funciona:** lentes (28/35/50/85/100mm macro), aperturas (f/1.4 retrato, f/8 producto), `softbox / window light / overcast flat light / motivated single source`, `visible grain / ISO 800 / 1/60`, `muted palette`, `negative space`.
**Negative prompt:** `smooth skin, airbrushed, HDR, oversaturated, studio glossy, symmetrical face, centered composition, bokeh balls, perfect teeth, Instagram filter, stock photo, plastic, waxy`.
**Aspect ratios web:** hero `16:9`/`21:9`, card producto `4:5`, thumb `1:1`, banner `3:1`. **Seeds:** fija `--seed N` (MJ) o seed numérico (Flux/NB) para reproducir y variar mínimamente.

## 3. CONSISTENCIA en toda una marca (lo difícil)

Objetivo: que 10 imágenes parezcan **una misma sesión de foto**.

- **Midjourney v7:** `--cref` **deprecado**. Usa **Omni Reference** (fuerza óptima **300-500**) para personaje/producto y `--sref <código numérico>` para estilo (los numéricos son más fiables que URLs). Documenta un **"Brand SREF playbook"**: código sref + `--sw` + `--stylize` por marca. **Máx 2 referencias** (con más, promedia a un punto turbio).
- **Higgsfield:** crea un **Moodboard** por marca (5-10 refs de la identidad) → se aplica a todas las generaciones. **Soul ID** para embajador/personaje recurrente entre presets.
- **Flux Kontext:** la mejor herramienta de coherencia por edición — genera una "key frame" y deriva el resto editando (mismo fondo/luz, distinto ángulo/producto) sin recrear.
- **Nano Banana Pro / Seedream:** alimenta hasta 14 refs (paleta + producto + ambiente) en una sola generación.
- **LoRA / fine-tuning:** vale solo con **>30 imágenes del MISMO producto/persona** y volumen alto. Para campañas puntuales, `--sref`/Moodboard basta.
- **Brand Style Frame:** documento por marca que **bloquea** paleta (hex), dirección de luz, lente fija, mood, sref/seed, fotógrafo ref, presets. Toda generación parte de ahí.

## 4. Fotografía de producto real con IA

El flujo correcto **no es generar desde cero**, es **editar tu foto real**:
1. Foto limpia del producto (incluso de iPhone) sobre fondo neutro.
2. **Flux Kontext** o **Nano Banana Pro**: enmascara fondo, prompt = nueva escena. Kontext **preserva el label/packaging exacto** y la geometría → el texto del empaque no se corrompe.
3. **Ángulos nuevos:** "rotate product 30°, same lighting" (Kontext); o multi-ref con varias tomas reales (NB).
4. **Sombras/reflejos creíbles:** `soft contact shadow + subtle floor reflection, light source upper-left` — verifica que la sombra coincida con la luz.
5. **Cutout/transparencia:** Photoroom / `remove.bg` / Recraft → PNG transparente; o genera sobre `grey seamless` y recorta (ver receta `sharp` en ref 11). Para web: PNG transparente compuesto sobre gradiente CSS.

Para SKUs en serie: **Flux Pro Kontext** procesa lotes en estilo consistente (catálogos e-commerce).

## 5. Post-proceso e integración web (que NO parezca AI)

- **Upscale:** Magnific / Krea / Topaz → 4K, subir textura de piel/poro (Magnific "creativity" bajo). NB Pro ya da 4K nativo.
- **Color grade a LUT de marca** (Lightroom/Photopea): saturación −10-15%, **lift blacks** (negros levantados = look fílmico), cast cálido interior / frío overcast. **Misma curva a todo el set = coherencia instantánea.**
- **Grano:** Add Noise **2-4%, Gaussian, Monochromatic**. Mata el plástico digital.
- **Compositing en web:** producto PNG transparente sobre **gradiente CSS** (no fondo generado) → más limpio y ligero. Blend: `mix-blend-mode:multiply` para fundir sombras de cutout sobre fondo claro; `screen`/`luminosity` para texturas; `overlay` para grano sobre hero. Recorta **off-center** para romper la simetría perfecta.
- **Export:** **AVIF** primero, **WebP** fallback. Hero ≤300-400KB, card ≤100-150KB. 2× retina (hero 2560-3840px). `loading="lazy"` salvo el LCP.

### AI-slop blacklist — tells que gritan IA (eliminar siempre)
1. **Piel de porcelana** sin poros / "wax figure".
2. **AI shine:** brillo uniforme en mate que no debería brillar.
3. **Luz omnidireccional golden-hour** sin fuente; sombras que no apuntan a la luz.
4. **Fondos sobre-detallados** (matte painting en vez de profundidad de campo).
5. **Simetría perfecta** (cara/composición matemáticamente centrada).
6. **Manos/dedos** anómalos, joyería fundida con la piel.
7. **Texto sin sentido** (usar Ideogram/NB si hay copy).
8. **Reflejos imposibles**.
9. **Sobre-saturación** y contraste HDR plano.
10. **Repetición de patrones** en texturas, ojos vidriosos idénticos, dientes "perfectos".

## 6. Workflow para agencia multi-marca

Pipeline repetible: **Brief → Style Frame → Batch → Select → Retouch → Export → Integrate.**
1. **Brief:** objetivo, formato web (hero/card/bg), marca.
2. **Style Frame** (1 vez por marca): paleta hex, lente, dirección de luz, mood, **sref/seed/Moodboard ID**, fotógrafo ref, presets Higgsfield. El contrato visual.
3. **Batch:** draft barato (Flux Schnell / Imagen Fast / Krea real-time) → finales con el especialista (MJ hero, Flux 2 producto, NB texto, Recraft logos).
4. **Select:** descarta por la blacklist de tells.
5. **Retouch:** upscale + grain + LUT de marca + fix manos/texto (inpaint Kontext).
6. **Export:** AVIF/WebP, naming `marca_seccion_v.avif`.
7. **Integrate:** PNG transparente sobre gradiente CSS + blend modes.

**Organización:** carpeta por marca con `STYLE_FRAME.md` (sref + seeds + hex + presets + prompts ganadores). Versiona prompts; guarda seed de cada imagen aprobada para regenerar variantes.
**Legal/ético 2026:** plan de pago = derechos comerciales (Recraft free no). Cliente regulado → Firefly (indemnización). Estilo de fotógrafo OK, copiar obra/trade-dress no. Metadatos **C2PA / Content Credentials** (Firefly, NB los incrustan) — divulgación cuando cliente/plataforma lo exija. No generar caras de personas reales sin consentimiento.

---

**Stack mínimo recomendado (agencia):** Higgsfield (lifestyle + Soul ID/Moodboards on-brand) + Flux Kontext (meter producto real / editing) + Nano Banana Pro (texto + 4K + multi-ref) + Recraft (vectores/logo) + Magnific (upscale) + Firefly (legal-sensible). Midjourney v7 para heros editoriales cuando quieres el mejor "ojo".
