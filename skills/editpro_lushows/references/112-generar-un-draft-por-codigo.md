# 112 — Generar un proyecto de CapCut por código

Este módulo responde una sola pregunta: **¿cómo escribo un montaje desde afuera y logro que CapCut lo
abra sin quejarse?**

La respuesta corta, y es la única que funciona de verdad:

> **No inventes el archivo. Cloná uno que ya funciona y reemplazale las partes.**

El resto del módulo explica por qué, y cómo hacerlo bien.

---

## Por qué no se inventa desde cero

El `draft_content.json` no está documentado por ByteDance. Nadie sabe qué campos son obligatorios,
cuáles tienen valores válidos limitados, ni cuáles se validan al abrir. Lo que sí sabemos, por
experiencia acumulada de la comunidad:

- Hay campos que parecen inútiles y **son obligatorios**. Si falta uno, CapCut no abre el proyecto o
  lo abre vacío.
- CapCut casi nunca te dice qué falta. El error típico es "no se pudo abrir el proyecto" o, peor, un
  proyecto que abre con la línea de tiempo en blanco.
- Los valores por defecto cambian entre versiones.
- Algunos campos tienen que ser consistentes entre sí (por ejemplo, el `render_index` de una pista con
  el modo de renderizado global).

Escribir el archivo desde cero es como escribir un documento de Word abriendo el `.docx` con un editor
de texto: técnicamente posible, prácticamente una pérdida de tiempo.

**La plantilla resuelve todo eso de un golpe:** todos esos campos raros ya están, con valores que
CapCut ya aceptó una vez.

---

## El método de la plantilla, paso a paso

### Paso 1 — Fabricar el molde a mano, una sola vez

Abrí CapCut y armá **a mano** un proyecto mínimo que tenga *todos los tipos de elemento* que tu
automatización va a necesitar. No importa que quede feo: importa que exista cada pieza.

Un molde típico para reels:

1. Nuevo proyecto, lienzo 9:16, 1080×1920, 30 fps.
2. Arrastrá un video cualquiera a la pista principal. Cortalo en **tres** pedazos (para que existan
   varios segmentos de video).
3. A uno de los pedazos, cambiale la velocidad (crea un material en `speeds`).
4. Agregá una **segunda pista de video** con una imagen encima (b-roll / logo).
5. Agregá un **texto** con la tipografía y el estilo que vas a usar siempre.
6. Agregá una **pista de audio** con una música, y ponele un desvanecido de entrada y de salida.
7. Guardá. Cerrá CapCut.

Ese proyecto es tu **plantilla estructural**. Copiá la carpeta entera a un lugar seguro, fuera de la
carpeta de CapCut, y marcala como solo lectura.

```
C:\media\plantillas\reel-9x16-30fps\
├── draft_content.json
├── draft_meta_info.json
├── draft_cover.jpg
└── ...
```

**Regla de oro: si algún día necesitás un elemento que la plantilla no tiene (una transición, una
máscara, un sticker), no lo inventes: volvé a CapCut, agregalo a mano al molde, guardá, y usá el nuevo
molde.** Es más rápido que adivinar el JSON.

### Paso 2 — Copiar la plantilla a una carpeta nueva

```powershell
$origen  = "C:\media\plantillas\reel-9x16-30fps"
$destino = "$env:LOCALAPPDATA\CapCut\User Data\Projects\com.lveditor.draft\reel-gastro-001"
Copy-Item $origen $destino -Recurse
```

El nombre de la carpeta puede ser cualquier cosa. CapCut usa marcas de tiempo, pero acepta nombres
legibles y te va a agradecer el favor cuando tengas veinte proyectos.

### Paso 3 — Cambiar la identidad

Tres cosas mínimas, para que CapCut no crea que es el mismo proyecto de siempre:

| Campo | Dónde | Qué poner |
|---|---|---|
| `id` | `draft_content.json` | Un UUID nuevo (formato `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`, mayúsculas) |
| `name` | ambos archivos | El nombre visible del proyecto |
| `update_time` / `create_time` | ambos | Marca de tiempo actual |

Si dejás el `id` de la plantilla, CapCut puede mostrar el proyecto duplicado o pisarte uno con otro.

### Paso 4 — Reemplazar los materiales

Por cada archivo de video, imagen o audio que vayas a usar:

1. Tomá un objeto existente en `materials.videos` (o `audios`) de la plantilla como base.
2. Cambiale: `id` (UUID nuevo), `path` (ruta absoluta al archivo real), `material_name`, `duration`
   (la del archivo, en microsegundos), y en video también `width` y `height`.
3. Si necesitás más materiales de los que tiene la plantilla, **duplicá** uno existente y cambiale los
   mismos campos. Nunca lo escribas de cero.

Los datos reales del archivo los sacás con `ffprobe` (bloque 100):

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate \
  -show_entries format=duration -of json entrada.mp4
```

Y la duración en microsegundos es `round(duration_en_segundos * 1000000)`.

**Actualizá también `draft_meta_info.json`**, que tiene su propia lista de materiales con sus rutas. Si
solo cambiás uno de los dos archivos, CapCut abre el proyecto con los clips en gris.

### Paso 5 — Escribir los segmentos

Acá es donde vive tu montaje de verdad. Para cada corte:

1. Duplicá un segmento existente de la plantilla (ya trae todos los campos raros).
2. Cambiale: `id`, `material_id` (al material correcto), `target_timerange` (dónde va en la línea de
   tiempo) y `source_timerange` (qué pedazo del original usás).
3. Ajustá `extra_material_refs` si el segmento necesita compañeros (velocidad, fades, animación) — y
   **asegurate de que esos materiales existan**.

El detalle fino de `target_timerange` vs `source_timerange` está en el módulo 113. La regla resumida:

```
source_timerange  = qué pedazo del archivo original           (dónde recorto)
target_timerange  = dónde cae ese pedazo en la línea de tiempo (dónde lo pego)
```

### Paso 6 — Cerrar las cuentas

Antes de guardar, tres ajustes globales:

- **`duration`** = el final del último segmento de todas las pistas. Si esto no cuadra, CapCut muestra
  la línea de tiempo cortada o con un vacío al final.
- **`canvas_config`** = el lienzo real que querés (`width`, `height`, `ratio`).
- **`fps`** = el que corresponda.

### Paso 7 — Abrir y mirar

Abrí CapCut. El proyecto debería aparecer en la lista con su nombre. Abrilo.

- **Aparece y se ve bien** → listo, pasá al humano.
- **Aparece pero la línea de tiempo está vacía** → casi siempre `duration` en cero, o los segmentos
  quedaron fuera del rango, o un `material_id` no coincide con ningún material.
- **Aparece y los clips están en gris** → rutas rotas. Revisá `path` en los dos archivos.
- **No aparece en la lista** → `draft_meta_info.json` mal escrito.
- **No abre / se cierra la app** → JSON inválido o referencias huérfanas.

---

## Usar una librería en vez de hacerlo a mano

Escribir el JSON a mano se justifica una vez, para entender. Para trabajo real, usá una librería.
Estado verificado a agosto de 2026:

### `pyCapCut` (Python)

```bash
pip install pycapcut
```

Del mismo autor que `pyJianYingDraft` (GuanYixuan); `pyCapCut` es la versión para CapCut
internacional. Te da clases `DraftFolder`, `ScriptFile`, `VideoSegment`, `AudioSegment`, `TextSegment`,
y acepta tiempos en texto legible (`"1.5s"`, `"1h3m12s"`) que convierte a microsegundos por vos.

Lo que tenés que saber antes de casarte con ella:

- **Genera drafts en Windows, Mac y Linux.** La exportación automatizada (abrir CapCut y renderizar)
  solo funciona en Windows, porque maneja la interfaz de la app por automatización de UI.
- **No soporta drafts cifrados**, solo `draft_content.json` en texto plano.
- **En modo plantilla**, no te deja agregar segmentos a las pistas importadas: solo a pistas nuevas que
  vos crees. Es una restricción que hay que diseñar alrededor.
- No soporta velocidad con curva, solo velocidad uniforme.

### `capcut-cli` (Node)

```bash
npm install -g capcut-cli     # requiere Node ≥18
```

De renezander030. Es una CLI que lee y escribe el draft directamente, sin servidor ni API. Comandos:
`info`, `lint`, `trim`, `speed`, `volume`, `add-text`, `add-video`, `caption`, `import-srt`,
`export-srt`, `cut`, `detect-scenes`, y un modo `serve` que corre trabajos desde un archivo JSONL.

Dos cosas la hacen especialmente útil para el puente:

- **`lint`** revisa el draft y te dice qué está roto (referencias huérfanas incluidas) *antes* de que
  abras CapCut. Usalo siempre como último paso.
- Exporta a **OpenTimelineIO**, o sea que podés pasarle el mismo corte a DaVinci Resolve (módulo 117).

En versiones recientes detecta y sincroniza *todos* los archivos de línea de tiempo legibles, no solo
`draft_content.json` — importante en Mac, donde manda `draft_info.json`.

### Cuál elegir

| Si… | Usá |
|---|---|
| Ya trabajás en Python y querés construir montajes complejos | `pyCapCut` |
| Querés operaciones puntuales sobre drafts existentes, o validar | `capcut-cli` |
| Querés que la IA maneje el proceso con órdenes simples | `capcut-cli` (`serve` con JSONL) |
| Necesitás algo que la librería no hace | Plantilla + tu propio código |

Ninguna es oficial. **Fijá la versión** (`pip install pycapcut==X.Y.Z`, `npm install -g capcut-cli@X.Y.Z`)
y no dejes que se actualicen en medio de un proyecto con fecha de entrega.

---

## Cómo probar sin quemarte

El ciclo de prueba correcto es corto y barato:

```
1. Escribí el draft
2. Validá el JSON        →  jq . salida.json > /dev/null   (si falla, ni abras CapCut)
3. Validá referencias    →  capcut-cli lint  (o la consulta de huérfanos del módulo 111)
4. CERRÁ CapCut
5. Copiá la carpeta a la carpeta de proyectos
6. Abrí CapCut y mirá
```

**Empezá minúsculo.** No arranques con el reel de 40 cortes. Arrancá con **un** clip de tres segundos
en la pista 0 y nada más. Cuando eso abra, agregá un texto. Cuando eso abra, agregá el audio. Cada
paso que funciona es un cimiento; cada paso que falla te dice exactamente qué lo rompió.

Si generás cincuenta segmentos de un tirón y no abre, no tenés forma de saber cuál fue.

### Un proyecto de laboratorio

Mantené aparte una carpeta `lab` con un proyecto desechable donde probás cosas raras. Si lo rompés, lo
borrás y copiás la plantilla de nuevo. Nunca experimentes en el proyecto real de un cliente.

### Diferencia antes y después

Cuando algo funciona en CapCut y querés saber **cómo se escribe**, el truco es este:

```bash
jq -S . antes.json > a.json      # -S ordena las claves
# hacé el cambio a mano en CapCut, guardá, cerrá
jq -S . despues.json > b.json
diff a.json b.json
```

Eso te muestra exactamente qué campos toca CapCut cuando aplicás una transición, una máscara o lo que
sea. **Es la mejor herramienta de aprendizaje del formato**, mejor que cualquier documentación.

---

## Reglas que no se rompen

**1. CapCut cerrado.** Siempre. La app tiene el proyecto en memoria y lo reescribe al guardar o al
cerrar. Si escribís con CapCut abierto, tu trabajo se evapora sin aviso.

**2. Respaldo antes de la primera línea de código.** La carpeta entera, comprimida, con fecha. Ver
módulo 119.

**3. Rutas absolutas, cortas y sin acentos.** `C:\media\proyecto\clip01.mp4`, no
`C:\Users\Usuario\Desktop\Nueva carpeta\Grabación día 2\clip 01 (copia).mp4`.

**4. Barras invertidas escapadas en JSON.** En Windows, `C:\media\x.mp4` se escribe `"C:\\media\\x.mp4"`.
Si usás una librería, ella lo hace; si escribís a mano, es un error clásico que rompe el archivo.

**5. UTF-8 sin BOM.** Si escribís el archivo con PowerShell, usá `-Encoding utf8` explícitamente. El
BOM al inicio hace que CapCut no reconozca el JSON.

**6. IDs únicos.** Cada material y cada segmento necesita su UUID. Reutilizar un ID es una fuente de
bugs invisibles.

**7. Un cambio a la vez cuando estás depurando.**

---

## Errores comunes

**Escribir el JSON desde cero.** Es la ruta larga hacia un proyecto que no abre. Clonar y reemplazar.

**Escribir con CapCut abierto.** El error que más tiempo hace perder, porque no falla: simplemente tu
trabajo desaparece y no entendés por qué.

**Actualizar `draft_content.json` pero no `draft_meta_info.json`.** El proyecto no aparece en la lista,
o aparece con todos los materiales en gris.

**Dejar el `id` de la plantilla.** Proyectos duplicados, proyectos que se pisan.

**Olvidar recalcular `duration`.** La línea de tiempo se ve cortada, o hay diez minutos de negro al
final.

**Referencias huérfanas en `extra_material_refs`.** Un fade, una velocidad o una animación que apunta a
un material que no existe. CapCut no abre. Corré `lint` antes de abrir, siempre.

**Confundir milisegundos con microsegundos.** Tu clip de 5 segundos dura 5 milésimas. Un segundo es un
millón.

**Rutas relativas.** CapCut usa rutas absolutas. Una relativa no resuelve a nada.

**Barras sin escapar en Windows.** `"C:\media"` es JSON inválido. Va `"C:\\media"`.

**Probar con el montaje completo de una.** Cuarenta segmentos y no abre = cero información. Empezá con
uno.

**Confiar en que la librería seguirá funcionando la semana que viene.** Fijá versiones, tanto de la
librería como de CapCut.

**Experimentar sobre el proyecto de un cliente.** Para eso está el laboratorio.

---

## Checklist

- [ ] Tengo una **plantilla** hecha a mano que contiene todos los tipos de elemento que voy a usar
- [ ] La plantilla está fuera de la carpeta de CapCut, marcada como solo lectura, respaldada
- [ ] Hice copia de seguridad de la carpeta de proyectos antes de escribir nada
- [ ] **CapCut está cerrado** antes de cada escritura
- [ ] Copié la plantilla a una carpeta nueva con nombre legible
- [ ] Cambié `id` (UUID nuevo), `name`, `create_time` y `update_time`
- [ ] Reemplacé los materiales con rutas absolutas reales y duraciones en microsegundos
- [ ] Actualicé las rutas **también** en `draft_meta_info.json`
- [ ] Escribí los segmentos duplicando los de la plantilla, no inventándolos
- [ ] Verifiqué que todo `material_id` y todo `extra_material_refs` apunta a algo que existe
- [ ] Recalculé `duration` global = final del último segmento
- [ ] `canvas_config` y `fps` corresponden al formato de salida
- [ ] El JSON es válido (`jq .` no da error) y está en UTF-8 sin BOM
- [ ] Corrí `capcut-cli lint` (o la consulta de huérfanos) y salió limpio
- [ ] Probé primero con un proyecto mínimo de un solo clip antes del montaje completo
- [ ] Fijé la versión de la librería y desactivé la actualización automática de CapCut
- [ ] Abrí el proyecto en CapCut y verifiqué con los ojos que se ve lo que esperaba
