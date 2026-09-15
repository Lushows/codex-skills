# 218 — Escribir efectos, animaciones, keyframes y velocidad por código

Este es el módulo que convierte el puente en algo que vale plata.

Los módulos 111–113 te enseñaron a generar un proyecto de CapCut por código: pistas, segmentos,
cortes. Eso produce un montaje **crudo**: clips uno tras otro, sin gracia. Acá aprendés a meterle
**efectos, animaciones, keyframes, velocidad y transiciones** a ese montaje generado. El resultado es
un proyecto que abrís en CapCut y ya está *editado*, no solo *armado*.

Antes de nada, la advertencia grande, y va en serio:

> **Nada de esto está documentado ni soportado por ByteDance. Puede romperse con cualquier
> actualización. Trabajá siempre sobre copias. Nunca sobre un proyecto que no puedas perder.**

---

## El principio que hace que todo funcione

No vas a **inventar** los identificadores de los recursos. Los vas a **cosechar** de tus propios
proyectos.

Un efecto de CapCut no es un archivo que vos podás crear: es un recurso del servidor de ByteDance,
identificado por un número (`effect_id`), que se descarga a una caché local la primera vez que lo
usás. Ese número no se adivina ni se deduce. Pero **si ya usaste ese efecto alguna vez, el número
está escrito en el archivo de ese proyecto** — y la ruta local también. De ahí sale toda la técnica:

```
1. Armás UN proyecto en CapCut, a mano, con TODO lo que querés usar después.
2. Guardás, cerrás.
3. Leés su draft_content.json y extraés los bloques JSON de cada recurso.
4. Guardás esos bloques en tu propia biblioteca (un archivo JSON tuyo).
5. Al generar drafts por código, pegás esos bloques.
```

A ese proyecto del paso 1 lo vamos a llamar **el proyecto donante**. Es el activo más valioso de todo
este flujo. Armalo una vez, bien, y te sirve para siempre.

---

## Paso 1: armar el proyecto donante

Abrí CapCut y creá un proyecto nuevo. Metele un clip cualquiera de 30 segundos. Y ahora, sobre ese
clip o sobre copias de él, aplicá **todos** los recursos de tu paleta:

- Cada efecto de tu paleta (módulo 211): Blanco y negro brillante, Badbunny, Noches de Río, Cassette
  defectuoso, Iluminar…
- Cada animación de entrada, salida y bucle que uses (módulo 212).
- Al menos una transición de cada tipo que quieras.
- Un par de keyframes de escala y de posición.
- Un clip con velocidad 2.0x y otro con 2.5x.
- Un texto con tu estilo de marca.

Guardá y **cerrá CapCut completamente** antes de leer el archivo: si está abierto, puede tener
cambios sin volcar a disco. Esto hace dos cosas a la vez: (1) fuerza a que todos los recursos queden
descargados en tu caché local, y (2) te da el archivo del que vas a copiar las referencias exactas.

---

## Paso 2: leer el donante

El archivo está en:

```
C:\Users\<vos>\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\<id-proyecto>\draft_content.json
```

Es un JSON grande (varios megas) y en una sola línea. Abrilo con un editor que formatee JSON (VS
Code, `Ctrl+Shift+P` → *Format Document*), o leelo por código. Buscá estas llaves:

| Recurso | Dónde vive |
|---|---|
| Efectos | `materials.video_effects` (a veces `materials.effects`) |
| Animaciones | `materials.material_animations` |
| Transiciones | `materials.transitions` |
| Velocidades | `materials.speeds` |
| Keyframes | dentro de cada segmento, en `common_keyframes` |

---

## Las estructuras exactas

Estas son las formas reales, verificadas en CapCut 8.3.0 en Windows.

### Efecto

Vive en `materials.video_effects`:

```json
{
  "name": "Bokeh",
  "effect_id": "7442221880838197777",
  "resource_id": "...",
  "category_id": "25498",
  "category_name": "Destacado",
  "path": "C:/Users/user/AppData/Local/CapCut/User Data/Cache/effect/<id>/<hash>",
  "adjust_params": [],
  "apply_target_type": 0,
  "item_effect_type": 0
}
```

`effect_id`, `resource_id` y `path` son la identidad del recurso: se copian tal cual. Lo único que
**tenés** que cambiar es el **`id`** del material (el identificador de esta instancia dentro del
proyecto): un GUID nuevo por cada uso.

**Ojo con las barras del `path`:** van con `/` aunque sea Windows. Si escribís `\\`, puede que CapCut
no encuentre el recurso.

### Animación

Viven en `materials.material_animations`. **Están agrupadas**: cada objeto es un grupo de tipo
`sticker_animation` que contiene un arreglo `animations`. Cada animación individual:

```json
{
  "type": "in",
  "name": "Aparición progresiva",
  "duration": 500000,
  "id": "6798320778182922760",
  "resource_id": "6798320778182922760",
  "material_type": "video",
  "panel": "video",
  "start": 0,
  "path": ".../Cache/effect/<id>/<hash>",
  "platform": "all"
}
```

- **`type`**: `in` (entrada), `out` (salida), `loop` (bucle).
- **`duration`: 500000** = medio segundo, en **microsegundos**. Este sí lo podés cambiar a gusto.
- **`start`**: 0 para entradas. Para salidas, CapCut lo calcula desde el final del segmento.
- **`panel`**: `video`, `text` o `sticker`. **No son intercambiables.**
- Un grupo puede llevar entrada **y** salida en `animations`, pero no bucle junto con ellas.

### Transición

Vive en `materials.transitions`:

```json
{
  "name": "Antes y ahora",
  "effect_id": "7012818976015127041",
  "duration": 100000,
  "category_name": "Tendencias",
  "is_overlap": false,
  "path": ".../Cache/effect/<id>/<hash>",
  "type": "transition"
}
```

- **`duration`: 100000** = 0,1 segundos. En microsegundos.
- **`is_overlap`**: en `true` la transición consume tiempo de los dos clips (se solapan); en `false`
  se inserta. Esto **cambia la duración total de tu línea de tiempo**. Cuidado.
- Se referencia desde el segmento del clip **anterior** al corte.

Recordá el dato de tus 51 proyectos: **una sola transición en total**. Si tu estilo es a corte duro,
no metas transiciones por código solo porque podés.

### Keyframe

Van **dentro del segmento**, en `common_keyframes` → `keyframe_list`:

```json
{
  "curveType": "Line",
  "time_offset": 725160000,
  "values": [-0.24043715846994540],
  "left_control": { "x": 0, "y": 0 },
  "right_control": { "x": 0, "y": 0 },
  "id": "<GUID>"
}
```

- **`time_offset`** en microsegundos, **medido desde el inicio del clip**, no del proyecto. Es el
  error de cálculo más frecuente.
- **`values`** es un arreglo. Escala y opacidad → un número. Posición → dos (X, Y). Están
  **normalizados**, no en píxeles: 0 es el centro, y el rango útil suele ir de -1 a 1.
- **`curveType`**: `Line` es lineal. Los valores de las curvas suaves **cosechalos del donante**.
- **`left_control` / `right_control`**: tiradores Bézier. En `{0,0}` están apagados.
- **`id`**: GUID único por keyframe.

Cada grupo de `common_keyframes` lleva además una **propiedad** que dice qué se está animando
(escala, posición, opacidad…). Cosechá esa etiqueta del donante — es distinta por propiedad.

### Velocidad

Vive en `materials.speeds` y se referencia desde el segmento. Para velocidad constante es un objeto
sencillo con un valor (`2.0`, `2.5`). Para curvas trae una lista de puntos.

**Advertencia crítica:** cambiar la velocidad **no cambia solo un número**. Cambia la relación entre
`source_timerange` (qué parte del archivo original se usa) y `target_timerange` (cuánto ocupa en la
línea). Si no recalculás esos dos rangos, el clip queda desincronizado o CapCut lo rechaza. La
fórmula: `duración en la línea = duración del material original ÷ velocidad`. Un clip de 4 segundos
a 2.0x ocupa 2 segundos en la línea.

---

## Paso 3: el eslabón que todo el mundo olvida

Acá está el 80 % de los fracasos con este flujo. **Poner el recurso en `materials` no basta.** El
segmento tiene que **apuntar** a él. CapCut usa un modelo de dos partes:

1. **`materials.*`** — el catálogo con las definiciones de todos los recursos del proyecto.
2. **`tracks[].segments[].extra_material_refs`** — un arreglo de **ids** que dice qué recursos usa
   *este* segmento.

Para aplicarle un efecto a un clip: **(a)** creás el objeto en `materials.video_effects` con un id
nuevo (GUID), y **(b)** agregás ese mismo id al arreglo `extra_material_refs` del segmento.

Si hacés solo (a), el efecto está en el proyecto pero **no se aplica a nada**: CapCut abre bien, no
da error, y no se ve nada. Lo mismo para animaciones (el grupo `sticker_animation`), transiciones y
velocidades. Los keyframes son la excepción: van **dentro** del segmento, así que no necesitan
referencia.

---

## Paso 4: las reglas de los identificadores

- **El `id` de cada material tiene que ser único en todo el proyecto.** Usá GUIDs con el mismo
  formato que ves en el donante. Si repetís un id, CapCut aplica el efecto donde no era o descarta
  uno de los dos.
- **El `effect_id` / `resource_id` NUNCA cambia.** Es el recurso en el servidor de ByteDance, igual
  en todos tus proyectos y en todas las máquinas. Copialo tal cual.
- **El mismo efecto en 10 clips = 10 objetos en `materials`**, cada uno con su GUID y su referencia.
  No podés referenciar un mismo material desde varios segmentos.

---

## Paso 5: tu biblioteca de recursos

Una vez cosechado el donante, guardá los bloques en un archivo tuyo:

```json
{
  "efectos": {
    "bn_brillante": { "name": "Blanco y negro brillante", "effect_id": "...", "path": "..." },
    "badbunny":     { "name": "Badbunny", "effect_id": "...", "path": "..." },
    "cassette":     { "name": "Cassette defectuoso", "effect_id": "...", "path": "..." }
  },
  "animaciones": {
    "entrada_suave": { "type": "in",  "name": "Aparición progresiva", "id": "6798320778182922760", "duration": 500000 },
    "salida_flash":  { "type": "out", "name": "Flash desactivado",    "id": "...", "duration": 300000 }
  }
}
```

Con nombres **en tu idioma de trabajo**, no los de CapCut. Después tu generador dice
`aplicarEfecto(segmento, "bn_brillante")` y no tiene que saber nada de números de 19 dígitos. Ese
archivo es tu paleta hecha código: la conexión directa entre el módulo 211 y este. **Guardalo en
control de versiones** — si CapCut cambia algo, querés poder ver qué había antes.

---

## Paso 6: el ciclo de trabajo seguro

```
1. Cerrá CapCut por completo.
2. Copiá una carpeta de proyecto entera a un nombre nuevo.
3. Escribí tus cambios sobre la COPIA.
4. Verificá que el JSON sea válido (que parsee sin error).
5. Abrí CapCut. Abrí la copia.
6. Mirá.
7. Si algo está mal, cerrá CapCut ANTES de volver a tocar el archivo.
```

Los pasos 1 y 7 no son opcionales. **CapCut mantiene el proyecto en memoria y lo vuelca a disco
cuando quiere.** Si editás el archivo con CapCut abierto, CapCut lo pisa y perdés el trabajo sin
ningún mensaje de error. Y verificá siempre que el JSON parsee antes de abrir: tres segundos de
`node -e "JSON.parse(require('fs').readFileSync(...))"` contra media hora de confusión.

---

## Qué pasa cuando algo falla

Aprendé a leer los síntomas, porque CapCut casi nunca te dice qué pasó:

| Síntoma | Causa casi segura |
|---|---|
| El proyecto no aparece en la lista | JSON inválido, o falta `draft_meta_info.json` |
| Abre pero está vacío | La estructura de `tracks` está mal formada |
| El efecto no se ve | Faltó agregar el id a `extra_material_refs` |
| El efecto se ve en el clip equivocado | Ids duplicados |
| El efecto sale como un cuadro gris o no carga | El recurso no está en la caché local |
| El clip se ve pero suena desincronizado | Velocidad escrita sin recalcular los timeranges |
| CapCut se cierra al abrir el proyecto | Campo obligatorio faltante o tipo de dato equivocado |
| Todo se ve bien pero al exportar falla | Referencia a un archivo de medio que no existe |

Regla de oro para depurar: **cambiá una cosa a la vez.** Si escribiste efectos, animaciones,
keyframes y velocidad de una sola vez y no abre, no vas a saber cuál fue.

---

## Los riesgos reales (leé esto)

1. **Se puede romper en cualquier actualización.** No hay contrato ni API ni compromiso de
   ByteDance. La 8.3.0 funciona así; la 9.0 puede cambiar los campos o cifrar el archivo, como ya
   hizo JianYing desde su v6. **Revalidá cada vez que CapCut se actualice.**
2. **Los recursos pueden desaparecer.** Un efecto de *Tendencias* puede ser retirado. Tu `effect_id`
   sigue guardado, pero si no está en tu caché y CapCut ya no lo sirve, no se descarga nunca más.
   Por eso el donante importa: mantiene los recursos vivos localmente. Respaldá esa caché.
3. **La caché es local.** Los `path` apuntan a **tu** disco con **tu** usuario. En otra máquina no
   existen. CapCut suele redescargar por `effect_id`, pero no cuentes con eso: esto es para tu
   máquina.
4. **Podés corromper proyectos.** Un JSON mal escrito deja el proyecto inutilizable, y CapCut no
   tiene historial de versiones. Sin respaldo, se perdió.
5. **Estás fuera de soporte.** Si se rompe, sos vos y el archivo.

---

## Cuándo vale la pena y cuándo no

**Sí:** cuando producís el **mismo formato muchas veces** con material distinto (50 videos de
producto, cortes semanales de podcast, reels de un catálogo); cuando el montaje sale de datos que ya
tenés (una transcripción, un guion, una lista de tomas); cuando la parte creativa está resuelta y lo
que queda es ejecución repetitiva.

**No:** en piezas únicas — hacerla a mano toma menos que escribir el generador; cuando el montaje
depende de juicio (elegir la mejor toma, sentir el ritmo); cuando hay fecha dura y no podés
permitirte que se rompa.

La jugada correcta casi siempre es **híbrida** (módulo 116): el código arma el esqueleto —cortes,
subtítulos, música, efectos de tu paleta en los puntos obvios— y vos le das los últimos 20 minutos
de criterio humano en CapCut. 80 % del tiempo ahorrado, 100 % del juicio conservado.

---

## Errores comunes

- **Inventar `effect_id`.** No se pueden deducir. Cosechalos de un proyecto donante real.
- **Poner el material en `materials` y olvidar `extra_material_refs`.** El fallo número uno: el
  proyecto abre bien y no se ve nada.
- **Reusar el mismo `id` de material en varios segmentos.** Un GUID nuevo por instancia.
- **Editar el archivo con CapCut abierto.** Lo pisa al guardar y perdés todo, sin aviso.
- **Confundir microsegundos con milisegundos.** `500000` es medio segundo; con `500` no pasa nada
  visible y vas a pensar que la animación no funciona.
- **Medir `time_offset` desde el inicio del proyecto.** Va desde el inicio del **clip**.
- **Escribir velocidad sin recalcular `source_timerange` y `target_timerange`.**
- **Usar `\` en los `path` de Windows.** El archivo real usa `/`.
- **Aplicar una animación de `panel: "text"` a un clip de video** (o al revés). No funciona y no da
  error.
- **Meter transiciones con `is_overlap: true` sin recalcular la línea.** Te corre todo el montaje.
- **No verificar que el JSON parsee antes de abrir CapCut.**
- **Escribir cinco tipos de recurso a la vez la primera vez.** Si falla, no sabés cuál fue.
- **No respaldar la carpeta de caché de los efectos clave.** Si CapCut los retira, se perdieron.
- **Asumir que esto sigue funcionando después de una actualización.** Revalidá siempre.

---

## Checklist

- [ ] Armé un **proyecto donante** con toda mi paleta aplicada y lo guardé aparte.
- [ ] Extraje los bloques JSON a mi propia biblioteca, con nombres legibles y en control de
      versiones.
- [ ] Respaldé la carpeta de caché de los efectos centrales de mi estilo.
- [ ] Verifiqué la versión de CapCut y que `draft_content.json` sea texto plano legible.
- [ ] **CapCut está completamente cerrado** y trabajo sobre una **copia** de la carpeta.
- [ ] Cada material que agregué tiene un GUID único y está referenciado desde
      `extra_material_refs` del segmento correspondiente.
- [ ] Todos los tiempos están en **microsegundos**, y los `time_offset` se miden desde el inicio del
      clip.
- [ ] Si escribí velocidad, recalculé `source_timerange` y `target_timerange`.
- [ ] Los `path` usan `/`.
- [ ] Verifiqué que el JSON parsea antes de abrir CapCut.
- [ ] Probé un tipo de recurso a la vez, no los cinco de golpe.
- [ ] Tengo claro que esto no está soportado y que voy a revalidarlo en cada actualización.
