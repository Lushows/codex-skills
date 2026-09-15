# 132 — Identidad de marca con IA: el reto de la CONSISTENCIA

Generar UNA imagen linda es fácil. Generar VEINTE que parezcan de la misma marca, con el mismo personaje, el mismo producto y el mismo estilo, es el verdadero reto — y es donde el 90% falla. Una marca no es una imagen bonita: es **repetición reconocible**. Si cada post se ve distinto, no hay marca, hay ruido. Este módulo es tu arsenal de consistencia.

> Las técnicas duran; los nombres de features cambian — verifica el estado actual.

---

## Por qué la IA es inconsistente por naturaleza

Cada generación es un nuevo "sueño" del modelo. Misma palabra "mujer feliz" = cara distinta cada vez. Para una marca esto es veneno. Necesitas **anclas** que fuercen la repetición. Hay cinco, de menos a más potentes:

| Técnica | Qué fija | Esfuerzo | Potencia |
|---|---|---|---|
| **Librería de prompts** | Estilo verbal | Bajo | ★★ |
| **Seed fija** | La "semilla" de la imagen | Bajo | ★★ |
| **Referencia de estilo (sref)** | El look general | Medio | ★★★ |
| **Referencia de personaje/producto** | El sujeto exacto | Medio | ★★★★ |
| **Fine-tuning ligero (LoRA)** | Personaje/producto/estilo entrenado | Alto | ★★★★★ |

---

## 1. Librería de prompts de marca (empieza aquí)

Crea un documento con tus "prompts madre" — el ADN visual escrito. Reúsalos siempre.

```
ESTILO BIO-SETA (pegar en cada prompt):
fotografía editorial de bienestar natural, luz suave de ventana,
paleta tierra cálida con acento verde esmeralda, fondos limpios de madera
o lino, sensación premium, calma y confianza, sin plástico brillante
```

> Ver 131 prompting visual avanzado y la librería de prompts; ver 92 sistema de marca (núcleo) para conectar con tu manual.

---

## 2. Seed: la misma semilla

La **seed** es el número que inicializa la imagen. Misma seed + mismo prompt = misma base. Cámbiala para variar, fíjala para mantener. Útil para mantener una escena mientras cambias detalles menores.

---

## 3. Referencia de estilo (style reference)

Subes 1-3 imágenes que representan tu look y la IA imita el lenguaje visual (no el contenido). Es la forma más rápida de que TODO se vea de la misma familia. Guarda tu código de estilo (`--sref` en Midjourney) y úsalo en cada generación.

---

## 4. Referencia de personaje / producto

Para mascota de marca, vocero recurrente o producto:

- **Character reference**: subes la cara/figura y la IA la mantiene entre escenas. Imperfecto, pero sirve para una mascota o personaje ilustrado.
- **Producto**: lo mejor casi nunca es generarlo de cero, sino **partir de una foto real** del producto e integrarla por edición (ver 135). La IA inventa etiquetas falsas.

---

## 5. Fine-tuning ligero (LoRA) — el nivel pro

Un **LoRA** es un mini-entrenamiento: le das ~15-30 fotos de tu producto, personaje o estilo y el modelo "aprende" a reproducirlo con fidelidad alta. Se usa en Stable Diffusion/Flux (ComfyUI). Es lo más potente para consistencia seria de marca, pero requiere ayuda técnica.

- **Cuándo vale la pena**: mascota recurrente, vocero, estilo de ilustración propio, producto que aparece en muchas piezas.
- **Cuándo NO**: si solo harás 5 imágenes, no montes un LoRA — usa sref + seed.

> Para montar LoRAs/ComfyUI en serio, esto cruza con ingeniería — apóyate en alguien técnico (ver skill engineer_visualopen).

---

## Sistema de marca para IA (tu "manual de IA")

Documenta esto UNA vez y reúsalo siempre:

```
[ ] Prompt madre de estilo (texto fijo)
[ ] Código de referencia de estilo (sref guardado)
[ ] Paleta exacta (HEX) que debe aparecer
[ ] Tipo de luz fijo (ej. "ventana lateral suave")
[ ] Negativos de marca (lo que NUNCA debe verse)
[ ] Seeds de escenas aprobadas
[ ] (Pro) LoRA de producto/personaje/estilo
```

---

## El criterio: consistencia ≠ rigidez

Consistencia no es clonar la misma imagen. Es que todo pertenezca a la misma **familia** — como una sesión de fotos coherente. Varía el encuadre, el sujeto, la escena; mantén fijos luz, paleta, mood y tratamiento. Eso es dirección de arte (ver 139).

---

## Checklist de consistencia

- [ ] Tengo prompt madre de estilo escrito y lo reúso.
- [ ] Uso referencia de estilo (sref) en todas.
- [ ] Mi paleta HEX aparece consistente.
- [ ] Producto real va por foto/edición, no generado de cero.
- [ ] Si hay personaje/producto recurrente, evalué un LoRA.
- [ ] Curo: todo se ve de la misma familia, no idéntico.

---

**Siguiente paso:** lee 133 para montar el pipeline profesional completo — de la idea a la pieza lista para producción, combinando IA con Photoshop e Illustrator.
