# 114 — Texto y plantillas animadas en CapCut

El texto es lo que más valor agrega por línea de código en el puente. Un reel con veinte apariciones de
texto animado, escritas a mano en CapCut, son cuarenta minutos de arrastrar cajitas. Escritas desde
afuera, son cuatro segundos.

También es la parte **más frágil** del formato. Este módulo te dice por qué y cómo no quemarte.

---

## Cómo se guarda un texto

Un texto vive en dos lugares, igual que todo lo demás:

- **`materials.texts[]`** → la definición: qué dice, con qué letra, de qué color, de qué tamaño.
- **`tracks[i].segments[]`** en una pista `type: "text"` → la aparición: cuándo entra, cuándo sale,
  dónde está en la pantalla.

Un material de texto se ve, simplificado, así:

```json
{
  "id": "AAAA-BBBB-...",
  "type": "text",
  "content": "{\"text\":\"3 errores que te cuestan plata\",\"styles\":[...]}",
  "font_path": "C:/Users/.../fonts/Montserrat-Bold.ttf",
  "font_size": 8.0,
  "text_color": "#FFFFFF",
  "alignment": 1,
  "line_spacing": 0.02,
  "letter_spacing": 0,
  "background_color": "",
  "background_alpha": 0.0,
  "border_color": "",
  "border_width": 0.08,
  "has_shadow": false,
  "shadow_color": "#000000",
  "typesetting": 0,
  "check_flag": 7
}
```

Y el segmento, en su pista:

```json
{
  "id": "CCCC-...",
  "material_id": "AAAA-BBBB-...",
  "target_timerange": { "start": 1000000, "duration": 3000000 },
  "extra_material_refs": ["DDDD-..."],
  "clip": {
    "alpha": 1.0,
    "scale": { "x": 1.0, "y": 1.0 },
    "transform": { "x": 0.0, "y": -0.35 },
    "rotation": 0.0
  },
  "render_index": 14000
}
```

**Fijate:** un segmento de texto **no tiene `source_timerange`**. El texto no viene de ningún archivo,
así que no hay nada que recortar. Solo `target_timerange`: cuándo aparece y cuánto dura.

---

## `content`: la trampa del JSON adentro del JSON

Este es el campo que rompe a todo el mundo. `content` **no es el texto**. Es **una cadena que contiene
otro JSON**, escapado.

Es decir: adentro de tu archivo JSON hay un campo cuyo valor es texto, y ese texto es a su vez JSON.

Desescapado, ese JSON interno se ve así:

```json
{
  "text": "3 errores que te cuestan plata",
  "styles": [
    {
      "range": [0, 9],
      "fill": { "content": { "solid": { "color": [1.0, 0.85, 0.1] } } },
      "size": 10.0,
      "bold": true,
      "font": { "path": "...", "id": "..." }
    },
    {
      "range": [9, 30],
      "fill": { "content": { "solid": { "color": [1.0, 1.0, 1.0] } } },
      "size": 8.0
    }
  ]
}
```

`text` es lo que dice. `styles` es un arreglo de tramos con estilo distinto. Así es como CapCut te
deja pintar dos palabras de amarillo y el resto de blanco dentro del mismo bloque.

### Los `range` son offsets **UTF-16**, no caracteres

Esta es la trampa dentro de la trampa, y es la que hace que tus subtítulos en español queden con los
colores corridos.

Los índices de `range` cuentan **unidades de código UTF-16**, no caracteres visibles.

Las tildes, la ñ y los caracteres chinos cuentan **1**, así que ahí estás bien. **Los emoji no:** uno
simple cuenta **2**, y los compuestos con modificador de piel o secuencias ZWJ (`👨‍🍳`) cuentan 4, 5 o
más. Si tu texto tiene un 🔥 al principio y calculás los rangos contando caracteres, todo lo que viene
después queda con el estilo equivocado.

**Cómo calcularlo bien:**

```python
# Python: len() cuenta puntos de código, no unidades UTF-16
def utf16_len(s):
    return len(s.encode("utf-16-le")) // 2

texto = "🔥 3 errores"
len(texto)        # 11  ← MAL para CapCut
utf16_len(texto)  # 12  ← BIEN
```

```javascript
// JavaScript: length YA cuenta unidades UTF-16. Acá tenés suerte.
"🔥 3 errores".length   // 12  ← correcto de una
```

**Consejo honesto: si podés, evitá emoji dentro del texto de CapCut.** Poné el emoji como sticker
aparte o como imagen. Te ahorra una clase de bug que es horrible de depurar porque solo se ve en
ciertas frases.

### Escapar bien

Al meter ese JSON interno como cadena, todas las comillas se escapan:

```
"content": "{\"text\":\"Hola\",\"styles\":[...]}"
```

Si escribís esto a mano vas a equivocarte. **Usá el serializador de tu lenguaje dos veces:**

```python
import json
interno = {"text": "3 errores que te cuestan plata", "styles": [...]}
material["content"] = json.dumps(interno, ensure_ascii=False)
# y luego json.dumps() del draft completo escapa lo que haga falta
```

`ensure_ascii=False` importa: sin eso, las tildes salen como `\u00e1` y aunque CapCut normalmente las
entiende, es ruido innecesario.

---

## Tipografía: el campo que rompe en la otra máquina

`font_path` es una **ruta absoluta a un archivo de fuente en ese computador**.

```
"font_path": "C:/Users/luis/AppData/Local/CapCut/User Data/Cache/effect/.../Montserrat-Bold.ttf"
```

Si le pasás el proyecto a otra persona, **la fuente no está en esa ruta** y CapCut cae a una
tipografía por defecto: tu diseño se desarma. Y las fuentes que descargás desde CapCut viven en su
caché, con nombres de carpeta que son hashes, inestables entre versiones.

**Cómo evitar el problema:**

1. **Usá una fuente del sistema**, instalada en `C:\Windows\Fonts\`. La ruta es estable.
2. **Definí una sola tipografía de marca** y usala en todo. Menos superficie de falla.
3. **En el molde, elegí la tipografía a mano en CapCut** y copiá la ruta que escribió la app.

Ese último punto es el método general del puente: **cuando no sepas qué valor va, ponelo a mano en
CapCut y copiá lo que escribió.**

### Tamaño de letra

`font_size` **no está en píxeles ni en puntos**: es una escala interna relativa al lienzo. En un
1080×1920, 8.0 se ve razonable para un subtítulo y 15.0 es un titular grande. No hay fórmula
publicada. Hacé tres textos a mano en el molde (subtítulo, destacado, titular) y usá esos tres números
como tus tamaños fijos. No adivines.

---

## Posición: coordenadas normalizadas

La posición sale del `clip.transform` del **segmento**, no del material. `(0, 0)` es el centro del
lienzo y los bordes andan por ±1. El signo del eje Y ha variado entre versiones: **movelo a mano en
CapCut y mirá qué número quedó** antes de escribir cincuenta textos al revés.

**Zona segura en vertical** (módulo 45): en 1080×1920, los últimos ~560 píxeles de abajo los tapan el
caption y los botones de la app, y los primeros ~220 de arriba la barra de estado. Un subtítulo
cómodo va hacia el tercio inferior visible, nunca pegado al borde.

---

## `text_templates`: los textos animados bonitos

`materials.text_templates[]` guarda las plantillas de texto de la biblioteca de CapCut — esas cajas
animadas con fondos, brillos y entradas.

**La verdad sobre estas:** son paquetes de recursos que CapCut descarga y guarda en su caché, con IDs
internos y rutas locales. No son algo que puedas construir desde afuera con conocimiento del formato.

**Estrategia correcta:**

1. En el molde, aplicá a mano la plantilla de texto que querés usar.
2. Guardá y cerrá.
3. En tu código, **duplicá ese objeto de `text_templates` y su segmento**, y cambiá solo el `content`
   (el texto) y el `target_timerange` (cuándo aparece).

Así reutilizás una plantilla que ya funciona sin entender su formato. Es exactamente el mismo principio
del módulo 112, aplicado al detalle.

**Limitación real:** si el usuario que abre el proyecto no tiene esa plantilla descargada en su caché,
va a aparecer sin el efecto. Las plantillas Pro además solo funcionan con Pro.

---

## Animaciones de texto

Las animaciones de entrada, salida y bucle viven en `materials.material_animations[]`, referenciadas
desde `extra_material_refs` del segmento de texto.

```json
{
  "id": "EEEE-...",
  "type": "sticker_animation",
  "animations": [
    { "type": "in",   "name": "Typewriter", "duration": 500000, "start": 0, "resource_id": "..." },
    { "type": "out",  "name": "Fade",       "duration": 300000, "start": 2700000, "resource_id": "..." }
  ]
}
```

El `resource_id` es un identificador del catálogo de ByteDance. **No lo podés inventar.** Aplicá la
animación a mano una vez en el molde, copiá el `resource_id` y el `name`, y guardalos como constantes
en tu código. Cinco animaciones bien elegidas cubren el 95% del trabajo; no necesitás las trescientas.

**Cuidado con la duración:** entrada + salida no pueden sumar más que la duración del segmento. Si el
texto dura 800 ms y le ponés 500 de entrada y 500 de salida, CapCut lo recorta o se ve mal.

---

## Subtítulos: el caso de uso estrella

Acá es donde el puente paga solo. El flujo completo:

```
audio del video
   ↓  Whisper (módulo 124)
transcripción con timecodes por palabra
   ↓  agrupar en frases de 3-5 palabras (módulo 46)
lista de {texto, inicio_us, fin_us}
   ↓  generar materiales de texto + segmentos en una pista "text"
draft_content.json
   ↓
CapCut abre con los subtítulos puestos, editables
```

El humano abre, lee, corrige las tres palabras que Whisper entendió mal, y listo.

**Dos caminos, ambos válidos:**

1. **Generar los textos vos** con el estilo exacto de la marca (control total, más trabajo).
2. **Generar un SRT** y usar `capcut-cli import-srt`, o importar el SRT a mano desde CapCut. Más rápido
   y menos frágil, pero el estilo lo ponés después.

Para volumen alto y estilo consistente de marca, el camino 1. Para una entrega puntual, el camino 2.

**Regla de rendimiento:** un video de 60 segundos con subtítulos palabra por palabra puede generar 150
segmentos de texto. CapCut se pone lento con eso. Agrupá en frases de 3 a 5 palabras; se lee mejor y
el proyecto pesa la tercera parte.

---

## Colores

Dos formatos conviven, y confundirlos es normal:

- En el material: `"text_color": "#FFFFFF"` — hexadecimal, como en web.
- Dentro de `content.styles[].fill`: `"color": [1.0, 0.85, 0.1]` — **arreglo RGB de 0.0 a 1.0**.

```python
def hex_a_rgb_normalizado(h):
    h = h.lstrip("#")
    return [int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4)]

hex_a_rgb_normalizado("#FFD91A")   # [1.0, 0.850..., 0.101...]
```

Si ponés `[255, 217, 26]` en vez de `[1.0, 0.85, 0.1]`, el color se satura a blanco puro y no entendés
qué pasó.

---

## Errores comunes

**Escribir `content` como texto plano.** No es el texto: es un JSON escapado dentro de una cadena.
Meter `"content": "Hola"` da un texto vacío o un proyecto roto.

**Calcular los `range` contando caracteres en vez de unidades UTF-16.** Con emoji, los estilos se
corren. Con tildes y ñ estás bien, pero un solo 🔥 al principio te desalinea todo.

**Meter emoji sin necesidad.** Si podés evitarlos dentro del texto de CapCut, evitalos: usalos como
sticker o imagen.

**Poner un `font_path` inventado o de otra máquina.** CapCut cae a la fuente por defecto y tu diseño se
desarma. Copiá la ruta de un molde real.

**Adivinar `font_size`.** No es ni píxeles ni puntos. Sacá tus tres tamaños del molde, a ojo, una vez.

**Poner la pista de texto debajo del video.** No se ve. Es la causa más frecuente de "el texto no
aparece".

**Ponerle `source_timerange` a un texto.** No existe. Un texto no viene de ningún archivo.

**Inventar `resource_id` de animaciones o plantillas.** Son del catálogo de ByteDance. Se copian del
molde o no funcionan.

**Animaciones más largas que el segmento.** Entrada + salida no pueden superar la duración del texto.

**Usar RGB 0-255 en `styles[].fill`.** Ahí van valores de 0.0 a 1.0. Se satura todo a blanco.

**Texto pegado al borde inferior en vertical.** Los últimos ~560 px los tapa la interfaz de la app.

**Generar subtítulos palabra por palabra en un video largo.** Cientos de segmentos, CapCut arrastrando.
Agrupá en frases.

**Asumir que las plantillas de texto se ven igual en otra máquina.** Si no está descargada en el caché
del otro usuario, o si es Pro y el otro no lo tiene, no se ve.

---

## Checklist

- [ ] Los textos están en pistas `type: "text"` **encima** de las de video
- [ ] Los segmentos de texto tienen `target_timerange` y **no** tienen `source_timerange`
- [ ] `content` es un JSON serializado correctamente, no texto plano
- [ ] Los `range` de `styles` los calculé en **unidades UTF-16**, no en caracteres
- [ ] Verifiqué el resultado con una frase que tenga tildes y ñ (y emoji, si los uso)
- [ ] `font_path` sale de un molde real y apunta a una fuente que existe en la máquina destino
- [ ] Los tamaños de letra los saqué del molde, no los inventé
- [ ] Las posiciones están en coordenadas normalizadas y verifiqué el signo del eje Y
- [ ] El texto respeta la zona segura del formato vertical (nada pegado a los bordes)
- [ ] Los colores dentro de `styles[].fill` van de 0.0 a 1.0, no de 0 a 255
- [ ] Los `resource_id` de animaciones y plantillas los copié de un molde, no los inventé
- [ ] Entrada + salida de animación no superan la duración del segmento
- [ ] Los subtítulos están agrupados en frases de 3-5 palabras, no palabra por palabra
- [ ] Abrí el proyecto en CapCut y **leí** los textos en pantalla, no solo verifiqué que abre
