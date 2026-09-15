# 268 — VFX con IA (agosto 2026)

**Qué resuelve:** qué partes del trabajo de efectos hace hoy la IA de verdad, cuáles promete y no
cumple, y cuáles de esas herramientas puedes usar tú —con celular, CapCut y ffmpeg— sin montar un
laboratorio. Verificado en agosto de 2026.

La conclusión corta, para que no leas 300 líneas si tienes prisa:

> **Separar está resuelto. Borrar está a medias. Generar fondo funciona en foto y a medias en video.
> Reiluminar funciona en foto y mal en video. Y nada de esto es reproducible: si mañana reexportas, no
> te da lo mismo.**

---

## 1. El mapa: qué está resuelto y qué no

| Tarea | Estado a ago-2026 | ¿La puedes usar tú? |
|---|---|---|
| **Segmentar / recortar sujeto** | ✅ resuelto | Sí — CapCut lo trae |
| **Seguir un objeto en video** | ✅ resuelto | Sí — CapCut lo trae |
| **Borrar objeto quieto, fondo simple** | ✅ funciona | Sí — CapCut AI object remover |
| **Borrar objeto con sombra o reflejo** | ⚠️ no resuelto | No confíes |
| **Reiluminar una FOTO** | ✅ funciona muy bien | Sí — modelos de imagen |
| **Reiluminar un VIDEO** | ⚠️ inestable | Solo Runway, y con cuidado |
| **Generar fondo (imagen)** | ✅ funciona | Sí — cualquier generador |
| **Generar fondo (video en bucle)** | ⚠️ caro y variable | A veces |
| **Editar un video con instrucciones** | ⚠️ funciona, regenera el plano | Runway, con créditos |
| **Precisión al píxel / repetibilidad** | ❌ no existe | No |

---

## 2. Segmentación: lo que sí está resuelto

**SAM 3 (Segment Anything Model 3, Meta, nov-2025)** es el estado del arte. La novedad frente a SAM 2:
acepta **conceptos** como instrucción —le escribes "la jarra de cerveza" o le señalas un ejemplo— y
detecta, segmenta y **rastrea todas las apariciones** de eso en imágenes y video. Duplica la precisión
de los sistemas anteriores en esa tarea.

**Qué significa para ti:** no vas a correr SAM 3 tú. Pero **es el motor detrás de lo que ya usas**: el
"Quitar fondo" de CapCut, los borradores de objetos, las herramientas de enmascarado de las apps. Que
esta pieza esté resuelta es la razón por la que el recorte de sujeto de CapCut, que hace tres años era
un desastre, hoy funciona en un clic.

**El límite que sigue ahí:** la segmentación es buena **por fotograma**. La coherencia **entre**
fotogramas sigue siendo el punto débil, y por eso el contorno hierve en tramos largos (`261`). Mejoró
mucho; no desapareció.

---

## 3. Borrado de objetos: el frente activo

Aquí es donde hay más movimiento y más marketing engañoso.

**Lo que puedes usar hoy:**

- **CapCut — eliminador de objetos con IA.** En la app y en la web. Marcas y quita. Funciona bien con
  objetos pequeños, quietos, sobre fondo simple. Se le nota en fondos con detalle.
- **Runway Gen-4 Aleph** (jul-2025). Editas video con instrucciones: dibujas una máscara sobre el
  micrófono o el transeúnte y lo rellena. Es lo más capaz disponible al público. **Aleph 2.0** salió en
  Picsart hacia finales de mayo de 2026, con la promesa de reescribir solo los fotogramas que pides
  —luz, objetos, personas, clima, hora del día— manteniendo sombras, reflejos y movimiento coherentes.
  Y desde diciembre de 2025 hay una alianza Adobe–Runway que mete esa tecnología dentro de Firefly.
- **Modelos abiertos** (necesitan GPU y montaje): **ProPainter**, **DiffuEraser**, **MiniMax-Remover**.
  Fuera de tu flujo salvo que quieras el proyecto aparte.

**Lo que NO está resuelto, y es importante:** borrar el objeto **y sus efectos** —su sombra, su reflejo
en la mesa, la luz que proyecta—. Es un problema tan difícil que tiene línea de investigación propia:
**EffectErase**, aceptado en **CVPR 2026**, existe precisamente porque los borradores actuales
(ProPainter, DiffuEraser, ObjectClear, OmniPaint, ROSE) fallan en eso.

> **La regla práctica:** si lo que vas a borrar proyecta sombra o se refleja, ningún borrador de hoy te
> va a dejar el plano limpio. Tápalo o reencuadra (`265`).

---

## 4. Reiluminar (relighting)

**En imagen fija: funciona muy bien.**

- **IC-Light V2** (basado en Flux) es el referente abierto: reilumina una imagen desde texto ("luz
  cálida desde la izquierda") o desde un fondo dado (le pasas la escena nueva y ajusta la luz del
  sujeto para que corresponda). Recibió puntuación perfecta en ICLR 2025.
- **Nano Banana Pro** (Gemini 3 Pro Image, Google) hace reiluminación, reemplazo de fondo y cambio de
  hora del día por instrucción, con salida hasta 4K, y es rapidísimo.
- **Flux.1 Kontext** (may-2025) hace edición en contexto: le das imagen + instrucción y edita conservando
  el resto.

**Para qué te sirve esto de verdad:** para **el elemento**, no para el plano. Generas el PNG del
producto, la ilustración o el fondo, y le pides que la luz venga del mismo lado que en tu video. Eso
resuelve, gratis, el problema número uno de `260`: que la luz no coincida.

**En video: todavía no.** Runway Aleph lo intenta y a veces sale bien, pero regenera el plano: la
textura cambia, la cara cambia sutilmente entre fotogramas, y el material deja de ser el que grabaste.
Para un talking head de marca es un riesgo alto.

---

## 5. Generar el fondo

**Imagen fija: sí, y es tu mejor uso de la IA en compositing.** Un fondo generado, desenfocado y bien
pedido (`266`, sección 5) es rápido, barato y funciona. Consejos que ya deberías tener claros:

- Pide **"vacío, sin personas"**.
- Pide el **lente**: "lente de 26 mm de celular".
- Pide la **dirección de la luz** que coincida con tu material.
- Pide **9:16 vertical** y **profundidad de campo corta**.

**Video en bucle: a medias.** Se puede generar un fondo en movimiento (nubes, gente pasando desenfocada,
fuego), pero: cuesta créditos por segundo, no controlas el bucle, y el movimiento a veces "respira" de
forma antinatural. Alternativa mucho más barata: **una imagen fija con parallax y un zoom lentísimo**
(`89`) — el 80% del efecto, cero créditos, y es reproducible.

---

## 6. Edición de video por instrucción (video-a-video)

**Runway Gen-4 Aleph** es la categoría entera hoy: le das un video y una instrucción ("quita a la
persona del fondo", "ponlo de noche", "cámbiame el ángulo de cámara") y te devuelve el plano editado.

**Lo que cumple:** es impresionante y para ciertos casos no hay alternativa.

**Lo que hay que saber antes de meterlo en un flujo de marca:**

1. **Regenera el plano.** No es una corrección: es una reinterpretación. La textura, el grano y hasta
   los rasgos cambian sutilmente. Si en el mismo reel mezclas planos tratados y sin tratar, se nota.
2. **No es reproducible.** Dos ejecuciones con la misma instrucción dan resultados distintos. Para una
   marca que reexporta piezas, eso es un problema real, no teórico.
3. **Cuesta créditos por segundo** y los reels tienen muchos segundos.
4. **La identidad se mueve.** En primeros planos de una persona conocida —tú, en tus reels— cualquier
   deriva de rasgos se percibe. Es el uso más arriesgado de todos.

> **Dónde sí conviene:** un plano corto, imprescindible, que no se puede volver a grabar, y donde el
> arreglo es imposible por otros medios. No como paso rutinario del pipeline.

---

## 7. La tabla honesta de promesa vs. cumplimiento

| Lo que promete el marketing | Lo que pasa de verdad |
|---|---|
| "Quita cualquier objeto en un clic" | quita objetos pequeños, quietos, sobre fondo simple. La sombra se queda |
| "Recorta perfecto cualquier video" | recorta muy bien; el contorno hierve en tramos largos |
| "Cambia la iluminación de tu video" | en foto sí; en video regenera el plano y cambia la textura |
| "Fondos cinematográficos con IA" | fondo bonito, luz que no corresponde con tu material. Tú tienes que pedir la luz |
| "Edición profesional sin saber editar" | edición no determinista sin control al píxel |
| "Ahorra horas de post" | ahorra horas **si el caso es el que la herramienta hace bien**; si no, quema créditos |

---

## 8. Cómo meter IA en tu flujo sin arruinarlo

Cuatro reglas que salen de todo lo anterior:

**1. Usa IA para GENERAR elementos, no para EDITAR el plano.** Generar un fondo, un PNG de producto, una
ilustración: barato, controlable, reutilizable. Reeditar el video grabado: caro, no reproducible,
cambia el material.

**2. Cualquier resultado de IA se congela como archivo.** En cuanto te sirva, guárdalo (`fondo_v3.png`,
`plano_limpio_v2.mp4`) y trátalo como material grabado. No dependas de poder volver a generarlo igual.

**3. La IA no respeta tu marca.** Ya está dicho en `125`: los colores no van a salir exactos, la
tipografía no va a ser la tuya. **La marca se impone en post**, con ffmpeg o CapCut, sobre lo que la IA
te devolvió.

**4. Antes de pagar créditos, pregúntate si `265`, `266` o `269` lo resuelven gratis.** Reencuadrar,
tapar con diseño y desenfocar el fondo real resuelven una barbaridad de casos por cero pesos.

---

## 9. Lo que sigue sin funcionar (agosto 2026)

Para que no lo intentes:

- **Borrar objetos con sus sombras y reflejos.** Es investigación en curso.
- **Coherencia perfecta entre fotogramas** en cualquier edición generativa. Siempre hay deriva.
- **Precisión al píxel.** No puedes decir "mueve eso 4 píxeles a la derecha".
- **Repetir exactamente un resultado.** No hay determinismo.
- **Video con canal alfa desde un generador.** Sigue sin haber salida con transparencia confiable
  (`81`).
- **Respetar un color de marca exacto.** Pediste `#00FF00` y te dio `#94BF6F` (`81`). Sigue igual.
- **VFX largo y complejo sin supervisión.** Todo lo que dure más de unos segundos hay que revisarlo
  fotograma a fotograma.

---

## 10. Qué revisar dentro de seis meses

Este módulo caduca rápido. Lo que hay que volver a verificar:

- Si el borrado **con efectos** (sombras/reflejos) llegó a producto: sería el cambio más grande.
- Si la reiluminación de video se estabilizó lo suficiente para talking heads.
- Si aparece salida con **canal alfa** confiable desde un generador: eso cambiaría todo el flujo de
  recortes.
- Si la integración Adobe–Runway abarata el acceso.
- Si CapCut incorpora borrado y reiluminación decentes de fábrica: sería lo que más te afecta a ti,
  porque es donde editas.

**Cómo verificarlo:** no leas anuncios. Prueba con **tu** material, el peor plano que tengas, y compara
con lo que ya haces gratis. Si no le gana a reencuadrar y desenfocar, no cambió nada.

---

## Fuentes verificadas (agosto 2026)

- SAM 3 — [arXiv 2511.16719](https://arxiv.org/abs/2511.16719) · [AI at Meta](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/)
- Runway Gen-4 Aleph — [CineD](https://www.cined.com/runway-aleph-ai-edits-real-footage-with-camera-angles-object-removal-and-relighting/) · Aleph 2.0 en [Picsart](https://picsart.com/ai-models/runway-aleph-2-0/)
- Borrado en video — [ProPainter](https://github.com/sczhou/ProPainter) · [MiniMax-Remover](https://arxiv.org/pdf/2505.24873) · EffectErase (CVPR 2026)
- IC-Light V2 — [discusión oficial](https://github.com/lllyasviel/IC-Light/discussions/98) · [fal.ai](https://fal.ai/models/fal-ai/iclight-v2)
- Nano Banana Pro — [blog de Google](https://blog.google/innovation-and-ai/products/nano-banana-pro/)
- CapCut — [eliminador de objetos con IA](https://www.capcut.com/es-es/create/ai-object-remover)

---

## Errores comunes

1. **Creer que "quita cualquier objeto" es literal.** Quita objetos pequeños y quietos sobre fondo
   simple. La sombra se queda.
2. **Usar edición generativa de video como paso rutinario.** Regenera el plano, cuesta créditos y no es
   reproducible.
3. **Mezclar en un mismo reel planos tratados por IA y planos crudos.** La diferencia de textura se ve.
4. **Contar con poder regenerar el mismo resultado mañana.** No hay determinismo. Congela el archivo.
5. **Pedir un fondo bonito sin especificar la dirección de la luz.** Es el error de `266` con esteroides:
   pagaste por un fondo que no puedes usar.
6. **Pedirle al generador "fondo transparente".** Sigue sin dar alfa confiable. Croma y `colorkey`
   (`81`).
7. **Esperar que respete el color exacto de la marca.** No lo hace. La marca se impone en post (`125`).
8. **Reiluminar video de un talking head propio.** La identidad deriva y en primer plano se nota.
9. **Pagar créditos antes de probar reencuadrar, tapar o desenfocar.** Gratis y muchas veces mejor.
10. **Aceptar un resultado de IA sin revisarlo fotograma a fotograma.** La deriva aparece en el segundo
    3, no en el 1.
11. **Tomar este módulo como verdad permanente.** Caduca. Verifica con tu propio material.

---

## Checklist

Antes de meter IA en un trabajo de VFX:

- [ ] Comprobé que **el caso concreto** es de los que la herramienta hace bien, no de los que promete.
- [ ] Si voy a borrar algo, verifiqué si **proyecta sombra o reflejo**. Si sí, cambié de estrategia.
- [ ] Estoy usando la IA para **generar un elemento**, no para reeditar el plano grabado.
- [ ] Si pedí un fondo, especifiqué **vacío, lente de celular, dirección de la luz y 9:16**.
- [ ] **Congelé el resultado como archivo** y no dependo de poder regenerarlo igual.
- [ ] Los colores de marca los impuse **yo en post**, no la IA.
- [ ] Revisé el resultado **fotograma a fotograma** en los tramos de movimiento.
- [ ] Comprobé que no se nota la diferencia de textura con los planos sin tratar del mismo video.
- [ ] Antes de pagar créditos, probé **reencuadrar, tapar y desenfocar** (`265`, `266`).
- [ ] Si es un talking head mío, **no** usé edición generativa sobre mi cara.
- [ ] Anoté la fecha: este módulo caduca y hay que volver a verificarlo.
