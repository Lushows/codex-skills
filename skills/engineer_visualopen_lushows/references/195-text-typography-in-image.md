# 195 · Texto y tipografía DENTRO de la imagen generada (carteles, packaging, logos)

> Generar imágenes con texto **legible y correcto** (headline de un póster, copy en packaging, marca en un letrero)
> es un subproblema aparte: casi todos los modelos lo alucinan. Hay un puñado que lo clava — y un patrón pro: el texto crítico **no se generación, se compone**.

## Quién renderiza texto bien (2026)
| Modelo | Precisión texto | Nota |
|---|---|---|
| **Ideogram v3** | **~90%** (módulo tipográfico dedicado) | rey del texto: pósters, packaging, signage, concepto de logo. Open-weight con asteriscos |
| **Nano Banana Pro** | muy alta | imbatible junto a Ideogram; fuerte en etiqueta/packaging |
| **FLUX.1 Pro / FLUX 2** | 2º lugar (ELO ~1068); FLUX 2 ya rivaliza con Ideogram | **open-weight self-host**, LoRA <$2 → única opción seria para auto-hospedar texto |
| Midjourney v6.1 | ~30% | realismo sí, texto no |

Patrón profesional real: **multi-tool** — Ideogram/Nano Banana para lo text-heavy, FLUX cuando manda el fotorrealismo. Para auto-hospedaje, FLUX 2 es el camino (ver [[149-flux-serving-a-fondo]]).

## Por qué falla el texto (y cómo mitigar en el prompt)
- El modelo aprende glifos como **textura**, no como caracteres → confunde letras, dobla, inventa. Cuanto más largo el string, peor.
- **Reglas que suben el acierto**: texto **corto** (1-4 palabras), **entre comillas** en el prompt, tipografía simple/sans, alto contraste, no manuscritas, no idiomas raros para el modelo.
- Acepta que **>6 palabras** casi siempre saldrá con errores → no pelees con el modelo, compón.

## El patrón ganador: generar fondo, COMPONER texto
Para producción seria (packaging real, ad con copy legal, logo de marca) **no generes el texto crítico**:
1. Genera el **fondo/escena** con el modelo (sin texto, o con placeholder).
2. **Superpón el texto/logo real** como capa vectorial (la fuente correcta, el pantone correcto, el logo .svg de marca).
   → tipografía perfecta, kerning real, marca exacta, editable y reproducible.
Reservas la generación de texto solo cuando el texto *es* el arte (póster estético donde la imperfección no importa).

## Logos: caso especial
- **No "generes el logo de la marca"** — lo deforma. Inyecta el logo real como cutout/overlay (cruza con [[193-product-photography-pipeline]]).
- Para **conceptos/ideación** de logo nuevo: Ideogram/FLUX sirven como bocetador; el vector final lo hace el diseñador.
- En packshot/packaging, la marca debe quedar **char-por-char idéntica** → composición, no generación.

## Decisión rápida: ¿generar o componer el texto?
| Caso | Acción |
|---|---|
| Texto **es** el arte (póster estético, fondo decorativo) | generar (Ideogram/FLUX) |
| Copy legal, precio, ingredientes, marca | **componer** (capa vectorial) |
| Logo de marca existente | **overlay del .svg**, nunca generar |
| Concepto/mood de logo nuevo | generar como boceto, vectorizar aparte |
| Etiqueta de producto real (BIO-SETA, packaging) | fondo generado + texto/marca compuestos |

## Self-host (FLUX, lo serio para texto open)
- FLUX.1/2 dev en GPU propia; LoRA de marca para fijar estilo tipográfico recurrente (barato, <$2 de entrenamiento).
- Sube **guidance** y baja temperatura/variación para texto más estable; texto vive mejor en resolución alta (renderiza ≥1024 el área del texto).
- Sirve el modelo warm; el texto requiere a veces varios seeds → batchea y filtra por OCR (valida el string con un OCR rápido antes de entregar).

## Gotchas
1. **String largo = basura** — parte en piezas cortas o compón.
2. **Logo deformado** — nunca lo generes; overlay del .svg real.
3. **Idioma/acentos** — tildes (español), ñ, caracteres no-latinos fallan más; verifica con OCR.
4. **Kerning/espaciado roto** — si necesitas tipografía perfecta, es señal de componer, no generar.
5. **Pantone de marca** — el color del texto generado se desvía; texto de marca → capa vectorial con color exacto.
6. **"Casi bien"** — una letra mal en packaging real es un reprint; OCR-gate obligatorio antes de aprobar.

Cruza con [[149-flux-serving-a-fondo]].

**Fuentes:** mindstudio.ai/blog/what-is-ideogram-v3 · blog.segmind.com/ideogram-vs-flux-1-typography-images · imagine.art/blogs/flux-2-overview · goenhance.ai/blog/ideogram-4-review · tooldirectory.ai/blog/best-ai-image-generator-2026-midjourney-flux-ideogram
