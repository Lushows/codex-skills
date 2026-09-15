# 91 — IA generativa para creativos: volumen sin perder marca

Andromeda (y su capa generativa GEM, ver 92) premia diversidad y volumen creativo, pero producir 20 variantes al mes a mano no es viable para una pyme. La IA generativa es la respuesta — usada como **multiplicadora de un concepto ganador, nunca como reemplazo del concepto**. En 2026 Meta metió la generación dentro de Ads Manager con el **Advantage+ Creative Suite** (image-to-video, variaciones, generación de fondo): el costo de producir cayó a casi cero, lo que mueve la ventaja competitiva de "tener assets" a "curar bien". Lee este módulo cuando necesites más creativos de los que puedes producir, o cuando dudes si un asset hecho con IA va a vender o a quemar tu marca.

## Las herramientas nativas de Meta (gratis, dentro de Ads Manager)

Vienen integradas en el flujo de creación del anuncio (Advantage+ Creative Suite); testéalas siempre **como variantes adicionales, nunca como reemplazo del original**:

| Herramienta nativa | Qué hace | Mejor uso |
|---|---|---|
| **AI backgrounds (generación de fondo)** | Pone tu producto (foto con fondo limpio) en escenarios generados — cocina, baño, exterior | E-com con foto de producto sola; genera 3-5 fondos y deja que la entrega decida |
| **Expansión de imagen** | Rellena con IA los bordes para adaptar tu 1:1 a 9:16 (Reels/Stories) | Fondos simples; revisa el resultado — con fondos complejos inventa cosas raras |
| **Image-to-video** | Anima una estática en un video corto con movimiento de cámara/parallax | Salvar una estática plana o llegar a placements de video sin grabar; revisa que no deforme el producto |
| **Variaciones de texto/headline** | Genera versiones alternativas de tu copy | Revisa cada una antes de aprobar: puede suavizar tu hook o alterar un claim (riesgo policy, ver 44) |

Costo cero y cero fricción: son lo primero que pruebas antes de pagar herramientas externas. **Pero ninguna reemplaza la dirección**: la Creative Suite genera variaciones de TU concepto; el concepto sigue siendo trabajo humano (ver flujo abajo).

## IA externa: qué sirve para ads y qué grita "IA"

| Uso | Funciona | Cuidado |
|---|---|---|
| **Imagen**: producto en contextos nuevos, mockups, fondos | ✅ multiplicador barato de estáticas (ver 35) | Manos deformes, texto ilegible dentro de la imagen, físicas imposibles — un solo detalle deformado grita IA y mata la confianza |
| **Video**: b-roll de relleno, avatares parlantes | ⚠️ b-roll sí; avatar solo para contenido informativo | El UGC humano REAL sigue ganando en confianza para venta (ver 32); un avatar IA vendiendo suplementos = rechazo del público y posible disclosure |
| **Copy**: 20 hooks/ángulos en minutos | ✅ el mejor uso costo/beneficio (ver 37/38) | **La IA propone, tú decides con datos.** Cura: borra lo genérico, quédate con 5, testea |
| **Voz**: locución TTS para video | ⚠️ solo si suena natural en español colombiano | Voz robótica o acento neutro de doblaje = scroll inmediato |

El filtro universal antes de publicar cualquier asset IA: **¿un humano de tu público lo compartiría sin pena ajena?** Si no, no entra a la cuenta.

## El flujo de producción asistida (receta)

1. **Identifica el ganador real** con datos (ver 68/31): qué ángulo, qué hook, qué formato está imprimiendo.
2. **La IA genera 10 variantes** sobre ese ganador: 4 hooks nuevos (mismo ángulo, entrada distinta), 3 fondos/contextos visuales, 3 adaptaciones de formato (estática→Reel guionado, 1:1→9:16, estática→image-to-video).
3. **Curaduría humana**: descarta todo lo que rompa marca, suene a robot o tenga defectos visuales. Sobreviven 4-6.
4. **Test estructurado** (ver 49/17): las variantes compiten con presupuesto controlado; el dato decide. Recuerda: cada variante es un **Entity ID** distinto en Andromeda (ver 92) — si dos son casi idénticas, Meta las colapsa y desperdicias slots.
5. Repite cada 2-4 semanas como rutina anti-fatiga (la vida útil de un creativo es de 2-4 semanas, ver 39).

Si generas a escala con APIs (decenas de imágenes/copys por semana), revisa costos con optimizer_tokens_lushows; para montar pipelines propios de generación (modelos open, GPU serverless), engineer_visualopen_lushows.

## El cálculo de costo: cuándo nativo, cuándo externo, cuándo API

| Volumen mensual | Vía recomendada | Costo aprox |
|---|---|---|
| 4-10 creativos | Advantage+ Creative Suite nativo (gratis) + 1 foto real | $0 + tu tiempo |
| 10-30 creativos | Nativo + herramienta externa de imagen/copy con plan mensual | herramienta SaaS (USD bajo) |
| 30+ creativos / multi-cliente | Pipeline con APIs (imagen/video/TTS) | costo por generación — monitorea con optimizer_tokens (ver) antes de que la factura de tokens se coma el ahorro de producción |

Regla: no montes pipeline de API hasta que el volumen lo exija de verdad; la Creative Suite nativa cubre a la mayoría de pymes sin un peso extra.

## Disclosure: cuándo declarar que es IA

Meta marca automáticamente contenido generado con sus herramientas y **exige declararlo manualmente** ("AI info" al publicar) cuando hay fotorealismo de personas que no existieron o hechos que no ocurrieron, y es especialmente estricto en categorías sensibles (temas sociales, política, salud, finanzas). Reglas prácticas:

- Avatar fotorealista o persona generada hablando a cámara → declara.
- Fondo generado detrás de tu producto real, retoques, expansión de imagen, image-to-video de tu propia foto → no requiere declaración (es edición).
- Testimonio "actuado" por IA presentado como cliente real → **prohibido directamente** (es engaño, no disclosure; ver 08).
- En duda, declara: el costo es cero; el strike por no declarar sí cuesta (ver 93).

## Consistencia de marca con IA

El riesgo silencioso: 20 creativos IA con 20 estilos distintos diluyen la marca. Solución: trabaja con **referencias de estilo** — alimenta cada generación con tus colores, tipografía, fotos reales de producto y 2-3 ads previos como referencia visual (style refs / imagen de referencia; en herramientas avanzadas, un LoRA entrenado con tu marca). La dirección completa de IA de imagen para marca está en directorcreativo_lushows (su módulo 14): úsala antes de producir en serie. Mantén un asset "ancla" humano/real en cada batería: la IA multiplica, lo real ancla la confianza.

## Receta exprés: de 1 ganador a 6 variantes en una tarde

1. Toma el ad ganador y escribe en una línea su ángulo y su hook.
2. Pide a la IA 10 hooks nuevos para ese ángulo, en español colombiano, con la voz de tu marca (pega 2-3 copys previos como referencia de tono).
3. Cura a 4. Genera 2 fondos nuevos para la estática del ganador (Creative Suite nativo o externo); convierte el ganador estático en un image-to-video.
4. Arma: 4 variantes de hook sobre el visual ganador + 2 visuales nuevos con el hook ganador = 6 ads diferenciados (no clones — recuerda el Entity ID, ver 92).
5. Súbelos al ad set/campaña de testing (ver 17), nunca directo a la campaña principal.

## Errores comunes — blacklist

- Usar IA para generar el CONCEPTO en vez de multiplicar un ganador validado: 10 variantes de una hipótesis mala = 10 fracasos más rápidos.
- Publicar la imagen sin zoom a manos, dientes, texto y logos: el detalle deformado lo ve el público aunque tú no.
- Avatar IA genérico vendiendo a cámara como si fuera UGC: el público lo huele y la confianza muere (ver 32).
- Stock-IA sin alma: producto flotando en fondo gradiente "premium" que no dice nada a nadie.
- No declarar personas fotorealistas generadas en categorías sensibles: strike evitable (ver 93).
- Generar 50 creativos y subirlos todos sin curaduría: ahogas la cuenta en mediocridad y le das ruido a Andromeda en vez de diversidad (ver 92).
- Subir 6 "variantes" que Meta colapsa en un solo Entity ID por ser casi idénticas: desperdiciaste la producción y no diste diversidad (ver 92).
- Montar un pipeline de API para 8 creativos al mes: la Creative Suite nativa era gratis y suficiente; revisa el costo con optimizer_tokens antes de sobre-ingenierizar.
- Cada creativo con estilo visual distinto: ganas el clic, pierdes la marca.
