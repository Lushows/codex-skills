# 130 — Panorama de IA visual 2026: el mapa de herramientas

La IA generativa visual ya no es un truco: es parte del taller del director creativo. Pero hay docenas de herramientas y cambian cada mes. Lo que NO cambia es el criterio: saber qué categoría sirve para qué problema, y cuándo NO usar IA. Este módulo es tu mapa mental. Tú diriges; la herramienta ejecuta.

> Verifica el estado actual de cada herramienta: nombres, planes y capacidades se mueven rápido. Aquí describimos CATEGORÍAS y CAPACIDADES duraderas, no versiones.

---

## Las 6 categorías que importan

| Categoría | Qué hace | Herramientas (ejemplos reales) | Cuándo la usas |
|---|---|---|---|
| **Generación de imagen** | Crea imágenes desde texto/referencia | Midjourney, Adobe Firefly, DALL·E, Ideogram, Flux, Recraft, Stable Diffusion | Moodboards, conceptos, ilustración, fondos, campañas |
| **Texto en imagen / vector** | Render fiable de letras y formas vectoriales | Ideogram, Recraft, Illustrator (IA) | Posters con texto, exploración de logo, íconos |
| **Upscale / mejora** | Sube resolución y añade detalle real | Magnific, Topaz, upscalers de Krea | Llevar un concepto a calidad de impresión |
| **Edición / inpainting** | Cambia partes de una imagen existente | Firefly (Generative Fill), Photoshop, Krea | Retoque, quitar/poner objetos, ajustar packshot |
| **Video / motion** | Genera o anima clips | Runway, Kling, Luna, Sora, Pika | B-roll, transiciones, animar un still |
| **3D / producto** | Genera mallas, materiales, escenas 3D | Spline IA, herramientas 3D generativas | Packaging 3D, mockups, producto rotando |

> Ver 68 fotografía e imagen con IA (núcleo) y 91 flujos IA (núcleo) para la base; aquí ampliamos.

---

## Cómo elegir herramienta: 4 preguntas

1. **¿Qué necesito producir?** Imagen, texto-en-imagen, vector, video, 3D. Empieza por la categoría correcta — usar Midjourney para un logo vectorial es pelear contra la herramienta.
2. **¿Necesito CONTROL o EXPLORACIÓN?**
   - Exploración rápida y "wow" estético → Midjourney, Krea.
   - Control fino (seeds, refs, máscaras, capas) → Stable Diffusion/ComfyUI, Firefly.
3. **¿Importa el tema legal/comercial?** Si es para un cliente que paga, prioriza herramientas con derechos comerciales claros e indemnización (ver 138). Firefly se entrena con stock licenciado; otras, no tanto.
4. **¿Reemplaza foto real o la complementa?** Si el producto debe verse EXACTO (etiqueta, color de marca), la IA sola casi nunca basta (ver 135).

---

## Perfiles de las grandes (por capacidad, no por versión)

- **Midjourney** — el rey del "se ve hermoso". Estética cinematográfica, luz y textura superiores. Débil en texto, control fino y reproducir un producto exacto. Ideal para mood, conceptos, campañas estilizadas.
- **Adobe Firefly** — integrado a Photoshop/Illustrator. Derechos comerciales e indemnización (entrenado con Adobe Stock). Generative Fill para edición. Menos "wow" que Midjourney pero más seguro y editable.
- **DALL·E** — sigue instrucciones complejas y conversacionales muy bien (vive dentro de ChatGPT). Bueno para iterar hablando.
- **Ideogram** — el mejor render de TEXTO dentro de imagen. Posters, tipografía, lettering.
- **Recraft** — orientado a diseño: genera y exporta en **vector (SVG)**, estilos consistentes, íconos. Puente entre IA y diseño gráfico real.
- **Stable Diffusion / Flux + ComfyUI** — open source, control TOTAL (seeds, LoRAs, ControlNet, workflows). Curva de aprendizaje alta. Para consistencia de marca seria (ver 132).
- **Krea / Magnific** — tiempo real, upscale y "enhance" que añade detalle creíble. Llevan un concepto a calidad final.

---

## El error #1 del no-técnico

Creer que "la herramienta hace el diseño". No. La herramienta genera **opciones**; tú aportas el **concepto, la dirección y el filtro de calidad**. Una imagen de IA sin dirección se ve genérica ("look de IA": simetría rara, piel plástica, luz de stock, composición vacía). Tu trabajo es matar el look de IA con criterio (ver 139).

---

## Mini-flujo recomendado para Lushows

```
1. Concepto claro (qué quiero comunicar, para quién) ← SIN herramienta
2. Mood/exploración → Midjourney o Krea
3. Si hay texto → Ideogram; si hay vector → Recraft
4. Curaduría: elijo 1-3 de 30 ← criterio humano
5. Edición/retoque → Firefly/Photoshop
6. Upscale → Magnific/Topaz para producción
```

---

## Checklist de selección

- [ ] ¿Identifiqué la categoría correcta (imagen/vector/video/3D)?
- [ ] ¿Necesito control o exploración? Elegí la herramienta acorde.
- [ ] ¿Es uso comercial? Verifiqué derechos (ver 138).
- [ ] ¿El producto debe ser EXACTO? Entonces foto real o edición sobre foto real (ver 135).
- [ ] ¿Tengo el concepto ANTES de abrir la herramienta?

---

**Siguiente paso:** lee 131 para aprender a escribir prompts visuales que de verdad controlen el resultado, y deja de "darle a generar" a ciegas.
