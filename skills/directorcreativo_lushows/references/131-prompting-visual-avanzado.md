# 131 — Prompting visual avanzado: dirigir, no rogar

Un prompt no es un deseo, es una **dirección de fotografía/arte escrita**. La diferencia entre "perro feliz" y una imagen que parece de una campaña real está en cuánto DIRIGES. Piensa como director: a un fotógrafo no le dices "hazme una foto bonita", le dices el sujeto, la luz, el lente, el encuadre y el mood. Lo mismo aquí.

> Los principios de este módulo duran; la sintaxis exacta de cada herramienta cambia — verifica el estado actual.

---

## Anatomía de un buen prompt visual

Un prompt completo tiene 7 capas. No siempre las usas todas, pero conócelas:

| Capa | Pregunta | Ejemplo |
|---|---|---|
| **1. Sujeto** | ¿Qué/quién es? | "frasco ámbar de cápsulas de melena de león" |
| **2. Acción/estado** | ¿Qué hace o cómo está? | "sobre madera, junto a hongos frescos" |
| **3. Estilo** | ¿Qué lenguaje visual? | "fotografía editorial de bienestar, natural" |
| **4. Luz** | ¿Cómo está iluminado? | "luz lateral suave de ventana, sombras largas" |
| **5. Composición/lente** | ¿Encuadre y óptica? | "primer plano, 50mm, profundidad de campo baja" |
| **6. Color/mood** | ¿Paleta y emoción? | "tonos tierra cálidos, calma, premium" |
| **7. Técnico/negativos** | ¿Qué evitar / formato? | "sin texto, sin manos, fondo limpio, 4:5" |

> Ver 68 fotografía e imagen con IA (núcleo) para el vocabulario de luz, lente y composición.

---

## Plantilla de prompt (cópiala)

```
[SUJETO + detalle exacto], [acción/contexto],
[estilo de imagen], [tipo de luz y dirección],
[encuadre + lente], [paleta de color + mood],
[formato/relación de aspecto], --no [lista de cosas a evitar]
```

Ejemplo real (suplemento BIO-SETA):

```
Frasco de vidrio ámbar con cápsulas de melena de león, etiqueta minimalista
verde esmeralda, sobre tabla de madera clara junto a un hongo Hericium fresco,
fotografía de producto editorial de bienestar, luz natural lateral de ventana
con sombras suaves, primer plano 50mm con fondo desenfocado,
paleta tierra cálida con acento esmeralda, sensación premium y natural,
relación 4:5 --no texto, manos, plástico brillante, fondo recargado
```

---

## El error: prompts cortos y vagos

"hongo bonito fondo bonito" → la IA rellena con sus clichés (look de IA). Cada palabra vaga es una decisión que regalas al algoritmo. **Especifica o el algoritmo decide por ti.**

---

## Iteración: el 80% del trabajo

Nadie acierta al primer prompt. El método:

1. **Genera 4** con el prompt base.
2. **Diagnostica**: ¿qué está mal? ¿luz plana? ¿composición vacía? ¿color frío?
3. **Cambia UNA variable** a la vez (luz, o lente, o mood). Si cambias todo, no sabes qué funcionó.
4. **Fija lo que funciona** con seed (mismo número = misma base) y sigue afinando.
5. **Varía** lo que ya quedó (variations) para opciones finas.

```
[ ] Genero tanda inicial (4-8)
[ ] Diagnostico el problema concreto
[ ] Cambio una sola variable
[ ] Fijo seed cuando algo ya sirve
[ ] Vario para refinar
```

---

## Referencias de imagen: el control real

Texto solo te lleva lejos; **imágenes de referencia** te llevan a la marca.

- **Referencia de estilo** (style reference / `--sref` en Midjourney): "quiero ESTE look". Subes 1-3 imágenes y la IA copia el lenguaje visual, no el contenido.
- **Referencia de personaje/producto** (character/omni reference): "que sea ESTE producto/persona en todas". Clave para consistencia (ver 132).
- **Image-to-image**: partes de una foto real y la transformas — mantiene estructura, cambia estilo. Útil para packshots (ver 135).
- **ControlNet** (en Stable Diffusion): controlas pose, bordes, profundidad con precisión quirúrgica.

> Regla de oro: **referencia de imagen > mil palabras** cuando buscas consistencia de marca.

---

## Negativos y "peso"

- **Negativos** (`--no` / negative prompt): lista lo que NO quieres. Esencial contra el look de IA (manos raras, texto basura, marca de agua).
- **Peso de palabras**: algunas herramientas dejan enfatizar (`palabra::2`) o usar `--stylize` / `--chaos` para más o menos libertad creativa. Súbelo para arte, bájalo para control.

---

## Checklist del prompt profesional

- [ ] Definí sujeto con detalle exacto (no genérico).
- [ ] Especifiqué luz (tipo + dirección).
- [ ] Definí lente/encuadre.
- [ ] Definí paleta y mood alineados a la marca.
- [ ] Usé referencia de imagen si busco consistencia.
- [ ] Puse negativos contra el look de IA.
- [ ] Iteré cambiando una variable a la vez.

---

**Siguiente paso:** lee 132, el reto más difícil de todos — lograr que TODAS tus imágenes parezcan de la misma marca (consistencia de personaje, producto y estilo).
