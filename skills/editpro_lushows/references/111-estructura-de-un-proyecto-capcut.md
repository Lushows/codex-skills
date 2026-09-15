# 111 — Anatomía de un proyecto de CapCut

Cuando creás un proyecto en CapCut, la app crea **una carpeta** en tu disco. No un archivo: una
carpeta. Y adentro hay media docena de archivos, de los cuales **uno solo importa de verdad**.

Este módulo es el plano de esa carpeta. Todo lo que sigue está verificado sobre CapCut 8.3.0 en
Windows, agosto de 2026.

---

## La carpeta

```
%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\
└── 2408041930123456\              ← una carpeta por proyecto (nombre = marca de tiempo)
    ├── draft_content.json         ← EL MONTAJE COMPLETO. Es el que importa.
    ├── draft_content.json.bak     ← respaldo que hace CapCut solo
    ├── draft_meta_info.json       ← nombre, fechas, rutas de los materiales importados
    ├── draft_agency_config.json   ← config interna, casi siempre vacío
    ├── draft_biz_config.json      ← config comercial/plantillas, casi siempre vacío
    ├── draft_cover.jpg            ← la miniatura que ves en la lista de proyectos
    ├── draft_settings             ← ajustes binarios/planos del proyecto (sin extensión)
    └── (subcarpetas de caché, proxies, adjuntos según la versión)
```

### Qué hace cada uno

| Archivo | Para qué sirve | ¿Lo tocás? |
|---|---|---|
| **`draft_content.json`** | La línea de tiempo entera: pistas, cortes, textos, audio, efectos | **Sí. Es todo el juego.** |
| `draft_content.json.bak` | Copia que CapCut guarda del estado anterior | Solo para rescatar |
| `draft_meta_info.json` | Nombre visible, fecha de creación/edición, duración, lista de materiales con su ruta en disco | A veces (rutas rotas) |
| `draft_cover.jpg` | Miniatura de la lista | Casi nunca |
| `draft_settings` | Preferencias del proyecto | No |
| `draft_agency_config.json` | Restos de funciones de agencias/plantillas | No |
| `draft_biz_config.json` | Restos de funciones comerciales | No |

**La regla:** si copiás la carpeta completa a otra máquina con CapCut instalado, el proyecto aparece.
Si copiás solo el `draft_content.json`, no aparece — CapCut necesita el `draft_meta_info.json` para
listarlo.

---

## `draft_content.json`: las claves de nivel superior

Estas son las claves reales, tal como aparecen en CapCut 8.3.0. Están en orden alfabético porque así
las escribe la app:

```
canvas_config          color_space              config
cover                  create_time              draft_type
duration               extra_info               fps
free_render_index_mode_on                       function_assistant_info
group_container        id                       is_drop_frame_timecode
keyframe_graph_list    keyframes                last_modified_platform
lyrics_effects         materials                mutable_config
name                   new_version              path
platform               relationships            render_index_track_mode_on
retouch_cover          smart_ads_info           source
static_cover_image_path                         time_marks
tracks                 uneven_animation_template_info
update_time            version
```

Parece mucho. En la práctica **manejás siete**:

| Clave | Qué es | Importancia |
|---|---|---|
| **`tracks`** | Las pistas de la línea de tiempo, con sus segmentos | ★★★★★ |
| **`materials`** | El almacén de todo lo que puede aparecer: videos, audios, textos, efectos | ★★★★★ |
| **`duration`** | Largo total del proyecto **en microsegundos** | ★★★★★ |
| **`canvas_config`** | Ancho, alto y proporción del lienzo | ★★★★ |
| **`fps`** | Fotogramas por segundo | ★★★★ |
| **`id`** | UUID del proyecto | ★★★ (hay que cambiarlo al clonar) |
| **`name`** | Nombre visible | ★★ |

El resto son metadatos de la app, banderas internas y restos de funciones. **Los copiás tal cual desde
la plantilla y no los tocás.** Ese es exactamente el argumento del módulo 112: no inventes el archivo,
clonalo.

### Las que sí conviene entender aunque no las toques

- **`version` / `new_version`** — versión del esquema. Es lo primero que hay que mirar cuando algo no
  abre: si difiere entre tu plantilla y tu CapCut, ahí está el problema.
- **`platform` / `last_modified_platform`** — qué app escribió esto (`"cc"` = CapCut, `"lv"` =
  JianYing). Si dice `lv`, estás con la versión china.
- **`is_drop_frame_timecode`** — importa a 29.97 y 59.94 fps (módulo 117).
- **`free_render_index_mode_on` / `render_index_track_mode_on`** — cómo decide CapCut el orden de
  dibujo. Dejalas como vengan; cambiarlas mueve capas de lugar.
- **`keyframes` / `keyframe_graph_list`** — animación por fotogramas clave. El terreno más frágil de
  todo el formato.
- **`relationships`** — vínculos entre elementos (texto pegado a un clip, por ejemplo).
- **`create_time` / `update_time`** — actualizá `update_time` al escribir para que CapCut ordene bien
  la lista de proyectos.

---

## `materials`: el almacén

`materials` es un objeto donde **cada clave es un tipo y cada valor es un arreglo**. Los grupos
verificados en 8.3.0:

```
videos                      audios                  texts
text_templates              canvases                speeds
material_animations         material_colors         placeholder_infos
sound_channel_mappings      vocal_separations       audio_fades
beats                       effects                 realtime_denoises
vocal_beautifys
```

Según la versión y lo que hayas usado, pueden aparecer también `transitions`, `masks` (que en versiones
9.6+ pasa a llamarse `common_masks`), `stickers`, `video_effects`, `filters`.

### El concepto clave: material ≠ segmento

Esto es lo que más cuesta y lo que todo lo demás depende:

> **Un `material` es la *definición* de algo. Un `segment` es *una aparición* de eso en la línea de tiempo.**

Ejemplo: importás `entrevista.mp4`. Eso crea **un** material en `materials.videos` con su ruta, su
duración y su resolución. Si usás tres pedacitos de ese clip en el montaje, tenés **tres segmentos**
en la pista, todos apuntando al **mismo** `material_id`.

Es la misma idea que un bin en Premiere: el archivo está una vez, los cortes son muchos.

Lo mismo vale para lo pequeño: una velocidad de 1.5x no vive en el segmento, vive en
`materials.speeds` como su propio objeto con su propio ID, y el segmento lo referencia. Un
desvanecido de audio vive en `materials.audio_fades`. Esto es raro pero es consistente: **casi todo lo
que le pasa a un segmento vive afuera como material y se conecta por ID**.

### Cómo se conectan

```
tracks[0].segments[2].material_id        → materials.videos[i].id      (el material principal)
tracks[0].segments[2].extra_material_refs[] → materials.speeds[j].id   (compañeros:
                                              materials.audio_fades[k].id  velocidad, fades,
                                              materials.material_animations[l].id  animaciones,
                                              ...)                       máscaras, transiciones
```

**Si un ID de `extra_material_refs` apunta a un material que no existe, CapCut no abre el proyecto o
lo abre roto.** Esa es, lejos, la causa número uno de "no me abre". Los IDs huérfanos son el enemigo.

### `materials.videos` guarda también las imágenes

No te confunda el nombre. Las fotos PNG/JPG que metés en la línea de tiempo también viven en
`materials.videos`; lo que las distingue es el campo `type` (`"video"` vs `"photo"`). Es una decisión
rara de diseño pero es así.

---

## `tracks`: la línea de tiempo

`tracks` es un **arreglo de pistas**. Cada pista tiene:

```json
{
  "id": "...",
  "type": "video",
  "attribute": 0,
  "flag": 0,
  "segments": [ ... ]
}
```

Los `type` que vas a ver: `"video"`, `"text"`, `"audio"`, `"filter"`, `"effect"`, `"sticker"`.

**El orden del arreglo define el apilado.** La pista en la posición 0 es la de abajo (el fondo); las
siguientes se dibujan encima. Si tu texto no aparece, casi siempre es porque su pista quedó debajo del
video.

Cada `segments[]` tiene el `material_id`, dónde empieza y cuánto dura en la línea de tiempo, y qué
pedazo del material original usa. El detalle completo está en el **módulo 113**.

---

## Microsegundos: la unidad de todo

**Todos los tiempos en el `draft_content.json` van en microsegundos.** Un microsegundo es una
millonésima de segundo.

```
1 segundo   = 1.000.000
1 minuto    = 60.000.000
```

Verificado: un proyecto de 51,4 segundos tiene `"duration": 51400000`.

Conversión mental rápida: **quitale seis ceros y tenés segundos** (`51400000` → 51,4 s).

Y ojo con los fotogramas: a 25 fps uno dura 40.000 µs exactos, pero a 24, 30 y 60 fps el número no es
entero (41.666,66 · 33.333,33 · 16.666,66). CapCut redondea al fotograma más cercano al mostrar, así
que un desfase de unos pocos miles de microsegundos es invisible — pero si acumulás el redondeo en
cincuenta cortes, el proyecto termina desincronizado del audio. **Trabajá con enteros y calculá
siempre desde el cero, nunca sumando duración tras duración.**

---

## Cómo mirar adentro sin romper nada

### Con el Bloc de notas

Sirve para el chequeo de treinta segundos: ¿es texto o es binario? Nada más. El archivo viene en una
sola línea gigante y es ilegible así.

### Con `jq` (recomendado)

`jq` lee JSON desde la línea de comandos. Se instala con `winget install jqlang.jq`.

```bash
jq '{name, duration, fps, canvas: .canvas_config}' draft_content.json   # lo básico
jq '.tracks[] | {type, segmentos: (.segments|length)}' draft_content.json
jq -r '.materials.videos[] | .path' draft_content.json                  # qué archivos usa

# la línea de tiempo en segundos, legible
jq -r '.tracks[] | select(.type=="video") | .segments[] |
  "\(.target_timerange.start/1000000) → \((.target_timerange.start + .target_timerange.duration)/1000000)"' \
  draft_content.json

# ¿hay IDs huérfanos? si devuelve algo distinto de [], el proyecto va a fallar
jq '[.materials[][]?.id] as $ids |
    [.tracks[].segments[].extra_material_refs[]?] |
    map(select(. as $r | $ids | index($r) | not))' draft_content.json
```

### Con PowerShell (si no querés instalar nada)

```powershell
$d = Get-Content "draft_content.json" -Raw | ConvertFrom-Json
$d.duration / 1000000            # duración en segundos
$d.tracks | Select-Object type, @{n='segs';e={$_.segments.Count}}
```

### Formatear una copia para leerlo cómodo

```bash
jq . draft_content.json > legible.json
```

**Nunca formatees el archivo original.** CapCut lo escribe en una línea; devolvérselo con saltos de
línea normalmente funciona, pero es un riesgo gratis. Trabajá sobre copias.

---

## `draft_meta_info.json`: el que se olvida

Este archivo es más chico y más aburrido, pero es el que hace que el proyecto **aparezca en la lista**
de CapCut. Guarda:

- El nombre visible del proyecto
- Fechas de creación y modificación
- La duración
- **La lista de materiales importados con su ruta absoluta en disco**

Esa última parte es la que te va a morder. Si movés los videos de carpeta, o si copiás el proyecto a
otro computador donde los archivos están en otra ruta, CapCut abre el proyecto con todos los clips en
gris diciendo "material faltante". La solución es corregir las rutas **en los dos archivos**:
`draft_meta_info.json` y `draft_content.json`.

**Consejo que ahorra dolor: guardá siempre los materiales en una ruta fija y corta, la misma para
todos los proyectos.** Por ejemplo `C:\media\<proyecto>\`. Nada de rutas del escritorio con nombres
largos y acentos.

---

## Un mapa mental de todo

```
carpeta del proyecto
│
├── draft_meta_info.json ─── "existo, me llamo X, uso estos archivos de aquí"
│
└── draft_content.json
    │
    ├── canvas_config ── 1080 × 1920, 9:16
    ├── fps ─────────── 30
    ├── duration ────── 51400000 µs  (51,4 s)
    │
    ├── materials ───── ALMACÉN (¿qué cosas existen?)
    │   ├── videos[]        entrevista.mp4, broll_01.mp4, logo.png
    │   ├── audios[]        musica.mp3, voz.wav
    │   ├── texts[]         "3 errores que te cuestan plata"
    │   ├── speeds[]        1.0x, 1.5x
    │   ├── audio_fades[]   fade de 500 ms
    │   └── ...
    │
    └── tracks ──────── LÍNEA DE TIEMPO (¿qué se ve y cuándo?)
        ├── [0] video   ▮▮▮▮▮▯▯▯▮▮▮▮▮▮▮▯▯▯▮▮▮   ← se dibuja abajo
        ├── [1] video   ░░▮▮▮░░░░▮▮▮░░░░░░░░░   ← b-roll encima
        ├── [2] text    ░▮▮░░░░▮▮▮░░░░░▮▮▮░░░
        └── [3] audio   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬   ← se dibuja arriba
```

Con este mapa en la cabeza, el módulo 112 (generar el draft) y el 113 (pistas y segmentos) se leen
solos.

---

## Errores comunes

**Creer que hay un archivo `.capcut`.** No existe. Es una carpeta con varios archivos, y hay que
copiarla entera.

**Tocar el `draft_content.json` con CapCut abierto.** CapCut tiene el proyecto cargado en memoria y lo
va a reescribir encima al guardar o al cerrar, borrando lo que escribiste. **Cerrá CapCut siempre
antes de escribir.**

**Editar el original sin copia.** El `.bak` que hace CapCut te salva una vez, no dos. Copiá la carpeta
entera antes de la primera línea de código (módulo 119).

**Confundir material con segmento.** Duplicar el material completo para usar dos pedazos del mismo
clip. Funciona a veces, pero infla el archivo y rompe cosas. Un material, muchos segmentos.

**Dejar IDs huérfanos.** Borrás un segmento pero dejás su velocidad o su fade en `materials`, o al
revés: dejás una referencia a algo que ya no existe. La segunda mata el proyecto. Corré la consulta de
huérfanos antes de abrir.

**Confundir microsegundos con milisegundos.** Es el error más común y el más humillante: tu clip de 5
segundos aparece de 5 milésimas o de 83 minutos. Un segundo son **un millón**, no mil.

**Sumar duraciones para calcular posiciones.** A 30 fps el fotograma no es entero y el error se
acumula. Calculá cada posición desde el cero.

**Mover los archivos de video después de crear el proyecto.** Las rutas son absolutas y quedan
escritas en dos archivos distintos. Definí la ruta de los materiales antes de empezar y no la muevas.

**Reformatear el JSON original con `jq .`.** Es un riesgo que no compra nada. Formateá copias.

**Asumir que estas claves son iguales en tu versión.** Están verificadas en 8.3.0 Windows. Si tu
versión es otra, abrí el tuyo y comparé. En Mac el archivo puede llamarse `draft_info.json`.

---

## Checklist

- [ ] Encontré la carpeta del proyecto y reconozco sus archivos
- [ ] Sé cuál es el archivo que importa (`draft_content.json`) y cuáles son ruido
- [ ] Confirmé que es texto plano legible, no binario
- [ ] Tengo una copia de seguridad de la carpeta completa antes de tocar nada
- [ ] CapCut está **cerrado** antes de cualquier escritura
- [ ] Entiendo la diferencia entre `materials` (definiciones) y `tracks[].segments` (apariciones)
- [ ] Tengo `jq` instalado o sé leerlo con PowerShell
- [ ] Verifiqué `duration`, `fps` y `canvas_config` del proyecto real
- [ ] Tengo internalizado que **todos los tiempos son microsegundos** (÷1.000.000 = segundos)
- [ ] Sé que el orden de `tracks[]` define qué capa va encima de cuál
- [ ] Corrí la consulta de IDs huérfanos y devolvió `[]`
- [ ] Los materiales están en una ruta fija, corta y sin acentos, y no la voy a mover
- [ ] Si cambio rutas, las cambio en `draft_content.json` **y** en `draft_meta_info.json`
