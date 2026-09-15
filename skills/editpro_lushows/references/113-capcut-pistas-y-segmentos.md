# 113 — Pistas y segmentos: el modelo mental de la línea de tiempo

Este es el módulo técnico central del puente. Si entendés bien pistas, segmentos y las dos ventanas de
tiempo, podés escribir cualquier montaje. Si no, vas a estar adivinando siempre.

---

## Pistas: capas apiladas

`tracks` es un **arreglo**. Cada elemento es una pista:

```json
{
  "id": "F1E2D3C4-...",
  "type": "video",
  "attribute": 0,
  "flag": 0,
  "is_default_name": true,
  "name": "",
  "segments": [ ... ]
}
```

| Campo | Qué es |
|---|---|
| `id` | UUID de la pista |
| `type` | `"video"`, `"audio"`, `"text"`, `"filter"`, `"effect"`, `"sticker"` |
| `attribute` | Bandera interna (`0` normal, `1` suele ser silenciada/oculta) |
| `flag` | Bandera interna. Copiala de la plantilla. |
| `segments` | El arreglo de clips que viven en esta pista |

### El orden es el apilado

**La pista en `tracks[0]` se dibuja primero (abajo). Las siguientes se dibujan encima.**

```
tracks[3]  texto        ← se ve arriba de todo
tracks[2]  b-roll
tracks[1]  video principal
tracks[0]  fondo         ← se dibuja primero
```

Si tu texto no aparece, el 90% de las veces es porque su pista está debajo de un video opaco.

Las pistas de audio no compiten por el espacio visual: se **suman**. El orden entre ellas no cambia
nada de lo que se oye.

### Reglas de las pistas

- **Una pista de video, un segmento a la vez.** Dos segmentos de la misma pista **no pueden solaparse
  en el tiempo**. Si necesitás dos cosas al mismo tiempo, van en pistas distintas. Esta regla no es
  negociable: si la rompés, CapCut abre mal o directamente no abre.
- Los **huecos son legales**. Un segmento de 0 a 3 s y el siguiente de 5 a 8 s deja 2 segundos de
  negro. Eso es válido.
- Las pistas de audio **sí se superponen entre sí** (música + voz + efecto suenan juntos), pero dentro
  de una misma pista de audio sigue valiendo la regla: un segmento a la vez.
- El texto va en pistas de `type: "text"`, no en pistas de video.

---

## Segmentos: una aparición en la línea de tiempo

Un segmento es un pedazo de material puesto en una pista, en un momento, durante un rato.

```json
{
  "id": "A1B2C3D4-...",
  "material_id": "E5F6...",
  "target_timerange": { "start": 3000000, "duration": 2500000 },
  "source_timerange": { "start": 12400000, "duration": 2500000 },
  "extra_material_refs": ["...", "..."],
  "speed": 1.0, "volume": 1.0, "visible": true,
  "render_index": 0, "clip": { ... },
  "enable_adjust": true, "reverse": false, "cartoon": false
}
```

| Campo | Qué hace |
|---|---|
| **`material_id`** | Apunta al material principal (el archivo de video, audio o el texto) |
| **`target_timerange`** | **Dónde cae en la línea de tiempo** (start + duration, en µs) |
| **`source_timerange`** | **Qué pedazo del archivo original uso** (start + duration, en µs) |
| **`extra_material_refs`** | IDs de los compañeros: velocidad, fades, animaciones, máscaras |
| `speed` · `volume` · `visible` | Velocidad (1.0 = normal), volumen (1.0 = 100%), si se ve |
| `render_index` | Orden de dibujo dentro del mismo nivel |
| `clip` | Transformación: escala, posición, rotación, opacidad, espejo |

---

## Las dos ventanas de tiempo (esto es lo importante)

Es el concepto que separa a quien entiende el formato de quien lo copia y reza.

```
ARCHIVO ORIGINAL (entrevista.mp4, 3 minutos)
├────────────────────────────────────────────────────────────────┤
0s                    12,4s      14,9s                        180s
                       ├──────────┤
                       source_timerange
                       start: 12400000
                       duration: 2500000
                              │
                              │  este pedazo…
                              ▼
LÍNEA DE TIEMPO DEL PROYECTO
├─────────┬──────────┬────────────────────────────────┤
0s        3s        5,5s                             51,4s
          ├──────────┤
          target_timerange
          start: 3000000
          duration: 2500000
                              …va acá.
```

- **`source_timerange`** responde: *¿de qué parte del archivo original saco esto?*
- **`target_timerange`** responde: *¿en qué momento del video final aparece?*

Ambos son objetos con `start` y `duration`, **en microsegundos**.

### La regla de oro de las duraciones

```
target_timerange.duration = source_timerange.duration / speed
```

A velocidad normal (`speed: 1.0`) las dos duraciones son **idénticas**. A 2x, un pedazo original de 4
segundos ocupa 2 en la línea de tiempo. **Si estas cuentas no cuadran, CapCut hace cosas raras**:
clips que se cortan solos, audio desincronizado, o el proyecto que no abre.

### Las dos reglas de límites

```
source.start + source.duration  ≤  duración real del material     (si no: clip negro o proyecto roto)
duration del proyecto  ≥  max(target.start + target.duration)     (si no: línea de tiempo cortada)
```

Validá siempre la primera contra la duración real que te dio `ffprobe`, no contra lo que creés.

---

## Cómo se arma una secuencia de cortes

Este es el patrón que vas a usar el 80% del tiempo: **cortes al hilo** (uno tras otro, sin huecos) de
pedazos distintos del mismo material. Tres tomas buenas de la entrevista quedan así:

```
segmento 1:  source {start: 12400000, duration: 2500000}   target {start: 0,       duration: 2500000}
segmento 2:  source {start: 45100000, duration: 3600000}   target {start: 2500000, duration: 3600000}
segmento 3:  source {start: 88000000, duration: 2200000}   target {start: 6100000, duration: 2200000}
```

El `target.start` de cada uno es la suma de las duraciones anteriores. La `duration` del proyecto es
`6100000 + 2200000 = 8300000` (8,3 s). **Los tres apuntan al mismo `material_id`**: un material, tres
apariciones.

### El código que lo genera (concepto)

```python
cursor = 0
for toma in tomas:
    seg = copiar_segmento_plantilla()          # nunca inventar el segmento
    seg["id"] = nuevo_uuid()
    seg["material_id"] = id_del_material
    seg["source_timerange"] = {"start": toma.inicio_us, "duration": toma.duracion_us}
    seg["target_timerange"] = {"start": cursor,         "duration": toma.duracion_us}
    pista["segments"].append(seg)
    cursor += toma.duracion_us

draft["duration"] = cursor
```

---

## Microsegundos y fotogramas

Un fotograma dura `1.000.000 / fps` microsegundos. A **25 y 50 fps** el número es entero (40.000 y
20.000). A **24, 30 y 60 fps no lo es** (41.666,67 · 33.333,33 · 16.666,67).

CapCut redondea al fotograma más cercano al mostrar, así que un error de unos pocos miles de
microsegundos es invisible. El problema es **acumularlo**: cincuenta cortes con 300 µs de error cada
uno = 15 ms de deriva, que a esa altura ya se nota contra la música.

**Solución: trabajá en fotogramas (enteros) y convertí a microsegundos una sola vez, al escribir.**

```python
# MAL: cada suma arrastra el redondeo anterior
pos = 0
for d in duraciones_us:
    pos += d

# BIEN: cada posición se deriva del total exacto en fotogramas
acumulado = 0
for d_frames in duraciones_en_frames:
    escribir(round(acumulado * 1_000_000 / fps))
    acumulado += d_frames
```

---

## `clip`: la transformación visual

`clip` es el objeto que dice cómo se ve el segmento en el lienzo:

```json
"clip": {
  "alpha": 1.0,
  "flip": { "horizontal": false, "vertical": false },
  "rotation": 0.0,
  "scale": { "x": 1.0, "y": 1.0 },
  "transform": { "x": 0.0, "y": 0.0 }
}
```

| Campo | Qué hace | Rango típico |
|---|---|---|
| `alpha` | Opacidad | 0.0 (invisible) → 1.0 (opaco) |
| `scale.x` / `scale.y` | Tamaño | 1.0 = tamaño natural, 1.2 = 20% más grande |
| `transform.x` / `transform.y` | Posición | **Coordenadas normalizadas**, 0 = centro |
| `rotation` | Giro en grados | 0 → 360 |
| `flip` | Espejo horizontal / vertical | booleanos |

**El detalle que confunde a todo el mundo: `transform` no está en píxeles.** Va en coordenadas
normalizadas donde el centro del lienzo es `(0, 0)` y los bordes andan por ±1. El signo del eje Y ha
variado entre versiones: movelo a mano en CapCut y mirá qué número quedó (módulo 112).

**Este es el mecanismo del punch-in** (módulo 22): un segundo segmento del mismo material, en una pista
encima, con `scale` en 1.2 y un `transform` que reencuadre. Sin recortar el archivo, sin re-renderizar
nada.

---

## `extra_material_refs`: los compañeros

Un segmento no guarda su velocidad ni sus fades adentro: los referencia por ID.

```json
"extra_material_refs": [
  "AAAA-...",   ← materials.speeds[i].id
  "BBBB-...",   ← materials.sound_channel_mappings[j].id
  "CCCC-...",   ← materials.vocal_separations[k].id
  "DDDD-..."    ← materials.material_animations[l].id
]
```

CapCut agrega compañeros **automáticamente** a cada segmento, aunque no los uses: un `speed` de 1.0, un
mapeo de canales neutro, una separación vocal desactivada. Por eso la plantilla es tan útil: ya los
trae.

- Si duplicás un segmento, **cada copia necesita sus propios compañeros con IDs nuevos.** Compartirlos
  produce bugs raros (cambiás la velocidad de uno y cambian los dos).
- Si borrás un segmento, borrá sus compañeros de `materials`.
- **Si un ID de esta lista no existe en `materials`, el proyecto no abre.** Es la falla número uno.

### `render_index`: no lo toques

Cada segmento tiene un `render_index` que afina el orden de dibujo dentro del mismo nivel, junto con
las banderas globales `free_render_index_mode_on` y `render_index_track_mode_on`. Copiá los valores de
la plantilla y controlá el apilado con el orden de las pistas, que es predecible.

---

## Velocidad, reversa y congelado

| Efecto | Cómo se hace |
|---|---|
| **Cámara lenta / rápida** | `speed` en el segmento **+** un material en `materials.speeds` referenciado. `target.duration = source.duration / speed`. |
| **Reversa** | `"reverse": true`. CapCut genera un archivo reverso; puede tardar al abrir. |
| **Congelado** | Más confiable exportar el fotograma con ffmpeg y meterlo como imagen que pelear con el formato. |

`pyCapCut` no soporta velocidad con curva, solo uniforme. Las curvas se hacen a mano después.

---

## Un ejemplo completo, chiquito

Reel de 8,3 s: tres cortes de entrevista, música de fondo, un texto en el segundo 1.

```
tracks[0]  type "video"
  ├─ seg1  material: entrevista   src 12,400→14,900   tgt 0,000→2,500
  ├─ seg2  material: entrevista   src 45,100→48,700   tgt 2,500→6,100
  └─ seg3  material: entrevista   src 88,000→90,200   tgt 6,100→8,300

tracks[1]  type "text"
  └─ seg1  material: texto_01     tgt 1,000→4,000     clip.transform.y = -0.35

tracks[2]  type "audio"
  └─ seg1  material: musica       src 0,000→8,300     tgt 0,000→8,300
           extra_material_refs → audio_fade (in 300 ms, out 800 ms)

duration = 8300000
```

Ocho segundos de video descritos en veinte líneas. Eso es el puente.

---

## Errores comunes

**Solapar dos segmentos en la misma pista de video.** No es válido. Si necesitás dos cosas al mismo
tiempo, son dos pistas.

**Confundir `source` con `target`.** Es *el* error del formato. Un clip que aparece en el momento
equivocado con el contenido equivocado, casi siempre, es esto.

**No respetar `target.duration = source.duration / speed`.** El clip se corta solo, el audio se
desincroniza, o el proyecto no abre.

**Pedir un `source_timerange` que se sale del archivo.** Negro, o proyecto roto. Validá contra la
duración real de `ffprobe`.

**Olvidar recalcular `duration` global.** Línea de tiempo cortada, o negro al final.

**Acumular error de redondeo sumando duraciones.** A 30 fps el fotograma no es entero. Trabajá en
fotogramas y convertí una sola vez.

**Poner el texto en una pista debajo del video.** No se ve, y perdés media hora buscando por qué.

**Compartir materiales compañeros entre segmentos duplicados.** Cada segmento, sus propios compañeros
con IDs nuevos.

**Dejar referencias huérfanas en `extra_material_refs`.** El proyecto no abre. Validá siempre.

**Pensar `transform` en píxeles.** Son coordenadas normalizadas con el centro en (0,0).

**Toquetear `render_index`.** Controlá el apilado con el orden de pistas y dejá `render_index` como
viene.

**Escribir un solo tiempo de los dos.** Un segmento sin `source_timerange` en un material de video no
sabe qué mostrar.

---

## Checklist

- [ ] Sé qué pista es cuál y confirmé que el orden de `tracks[]` da el apilado que quiero
- [ ] El texto está en una pista `type: "text"` **encima** de las de video
- [ ] Ningún par de segmentos se solapa dentro de la misma pista
- [ ] Cada segmento tiene `material_id` apuntando a un material que existe
- [ ] Cada segmento tiene `source_timerange` **y** `target_timerange`, ambos en microsegundos
- [ ] `target.duration == source.duration / speed` en todos los segmentos
- [ ] Ningún `source.start + source.duration` supera la duración real del archivo
- [ ] Los `target.start` no dejan huecos que no quise, ni solapes
- [ ] Trabajé las posiciones en fotogramas enteros y convertí a µs una sola vez
- [ ] `duration` global = el final del último segmento de todas las pistas
- [ ] Cada segmento duplicado tiene sus propios materiales compañeros con IDs nuevos
- [ ] Ningún ID de `extra_material_refs` está huérfano
- [ ] Los `clip.transform` los pensé en coordenadas normalizadas, no en píxeles
- [ ] No toqué `render_index` ni las banderas globales de renderizado
- [ ] Abrí el proyecto en CapCut y verifiqué que los cortes caen donde los calculé
