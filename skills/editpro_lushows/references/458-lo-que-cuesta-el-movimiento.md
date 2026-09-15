# 458 — Lo que cuesta el movimiento

Un montaje de imágenes fijas no se renderiza: se **recompone**, fotograma a fotograma, desde los
archivos originales. Y ahí está el coste que nadie calcula: ffmpeg **reescala cada imagen en cada
fotograma**, aunque el resultado sea idéntico las 168 veces. Este módulo tiene los números medidos y
la decisión que los cambia.

---

## 1. El caso: un `scale` que no hacía nada y costaba un tercio del plano

La cadena era la receta clásica de `102` y `83`: preescalar la entrada 4× antes de `zoompan` para
evitar el temblor (`453`).

```bash
[0:v]scale=4320:-2,zoompan=z='1+0.00059524*on':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':\
s=1920x1080:fps=25,format=rgba
```

El fondo **ya venía a 4320×2430**. Ese `scale=4320:-2` no cambiaba un solo píxel y aun así ffmpeg lo
ejecutaba 168 veces. Medido sobre una escena de 6,73 s, midiendo solo el grafo de filtros (`-f null -`,
sin codificar):

| Cadena | Tiempo | |
|---|---:|---|
| entrada 4320, `scale=4320:-2` por fotograma | **61,79 s** | |
| PNG preescalado a 2688 una sola vez, sin `scale` en la cadena | **40,54 s** | **−34%** |

El preescalado se paga una vez: 3,96 s con PIL, y el archivo queda en caché para todos los renders
siguientes. A partir del segundo render, gratis.

La medición original del motor sobre esa misma escena da 33,5 s → 22,6 s, un −33%. Los valores
absolutos dependen de la máquina; **la razón se reproduce**.

### ¿Y la calidad?

```bash
ffmpeg -hide_banner -i antiguo.mp4 -i nuevo.mp4 -lavfi psnr -f null -
ffmpeg -hide_banner -i antiguo.mp4 -i nuevo.mp4 -lavfi ssim -f null -
```

| Métrica | Valor |
|---|---:|
| PSNR (media) | **43,69 dB** |
| PSNR Y | 42,02 dB |
| SSIM (todos los canales) | **0,969** |
| SSIM Y | 0,955 |

Por encima de 40 dB de PSNR la diferencia no es visible a tamaño real. **Un tercio menos de render por
nada.**

⚠️ `psnr` y `ssim` imprimen en nivel `info`: con `-loglevel error` no sale ni una línea.

---

## 2. Las capas: el coste marginal que se dispara

Escena de 6,73 s a 1920×1080, solo grafo de filtros, tres tandas seguidas de la misma máquina:

| Composición | Capas sin preescalar | Capas preescaladas |
|---|---|---|
| fondo solo | 33,0 / 66,5 / 74,7 s | — |
| fondo + 3 capas | 87,6 / 98,7 / 51,3 s | 51,9 / 73,9 / 33,5 s |
| fondo + 8 capas | 116,2 / 128,5 / 94,1 s | 52,1 / 92,0 / 70,9 s |

**Honestidad sobre la máquina:** el mismo comando varía entre 33 y 75 segundos entre tandas. Los
valores absolutos no valen nada; lo que se repite en las tres tandas es la comparación **dentro** de
cada una, y el coste marginal de una capa **sin preescalar**: entre 5,7 y 8,6 segundos por capa
añadida, creciendo linealmente. Preescaladas, el ahorro total va del **25% al 55%**.

El origen es el mismo que en el fondo: un recorte de archivo de 1447 px mostrado a 340 se reduce 168
veces al mismo tamaño. Reducirlo una vez y guardarlo convierte el trabajo por fotograma en trivial.

---

## 3. La regla del preescalado

> **Reduce cada PNG una sola vez a 1,4× el tamaño al que se va a ver, y cachéalo.**

- **1,4×, no 1,0×.** Hace falta margen para la rotación, la deriva y cualquier `scale` fino posterior.
  Reducir exactamente al tamaño final hace que el elemento se vea blando en cuanto gira dos grados.
- **Solo si de verdad sobra tamaño.** Si el original ya está cerca del objetivo, preescalarlo es una
  pérdida neta: pon un umbral (`original > objetivo · 1,15`).
- **La caché se nombra con un hash de la ruta completa, nunca con el nombre del archivo.** Hay
  `ficha_policial.png` en dos carpetas distintas, y cachear por nombre hace que el segundo reutilice
  el PNG del primero: **imagen equivocada en pantalla y ni un solo error**.
- **Ante cualquier fallo, devuelve el original.** Un preescalado es una optimización; nunca puede ser
  el motivo de que una escena no se renderice.

### Lo que NO cuadra: bajar en dos pasos

Se dice que reducir 4320 → 2688 → 1920 «suaviza mejor» que hacerlo de golpe. **Medido, no.** Sobre un
patrón de zonas (el peor caso de aliasing), comparando contra una reducción de referencia:

| Variante | PSNR vs referencia | Energía espuria en zonas planas |
|---|---:|---:|
| `lanczos`, 1 paso | **56,27 dB** | **1,43** |
| `lanczos`, 2 pasos | 40,98 dB | 6,89 |
| `bicubic`, 1 paso | 34,60 dB | 1,09 |
| `bicubic`, 2 pasos | 31,25 dB | 14,74 |
| `area`, 1 paso | 25,11 dB | 32,15 |

Dos pasos con `bicubic` sí sale **más blando** —y de ahí viene la impresión de que «suaviza mejor»—,
pero blando no es mejor: mete cuatro veces más energía espuria en las zonas que deberían ser planas.
**Un solo paso con `flags=lanczos`.** Lo que ahorra tiempo es preescalar **una vez y guardarlo**, no
partir la reducción en dos.

---

## 4. Cómo se estructura un render que escala

- **Una escena, un comando de ffmpeg.** Un episodio largo son más comandos, no un `filter_complex`
  más grande: los grafos enormes son lo que revienta.
- **Se concatena al final con `-c copy`.** Coste prácticamente cero.
- **Intermedios con `-crf 12 -preset ultrafast`.** La calidad se guarda para el máster; en los
  intermedios lo que se quiere es velocidad y no perder nada visible.
- **Si una escena falla, se aborta el episodio.** Concatenar las demás deja todo lo que viene después
  desincronizado de la voz, y eso no avisa: se descubre viendo el vídeo entero.
- **Orden de magnitud:** con el fondo preescalado, 6,73 s de escena costaban 40 s de filtros en esta
  máquina. Un episodio de 63,45 s con sus elementos y su codificación está en torno a los **10
  minutos**, y esa cifra escala linealmente con la duración.

---

## Errores frecuentes

1. **Dejar un `scale` que no cambia nada.** Cuesta lo mismo que uno que sí, 168 veces por escena.
2. **Preescalar dentro del grafo en vez de una vez en disco.** `scale` dentro de la cadena se ejecuta
   por fotograma, siempre.
3. **Preescalar exactamente al tamaño en pantalla.** Sin el margen de 1,4× el elemento se ablanda en
   cuanto rota o deriva.
4. **Cachear por nombre de archivo.** Dos recursos con el mismo basename y en pantalla sale el que no
   es, sin ningún error.
5. **Partir la reducción en dos pasos creyendo que mejora.** Medido: pierde 15 dB y mete aliasing.
6. **Usar `area` o `bilinear` para reducir.** El peor resultado de la tabla, con diferencia.
7. **Sacar conclusiones de una sola medición** en una máquina que varía el doble entre tandas. Mide
   tres veces y compara dentro de cada tanda.
8. **Medir con `-loglevel error`** y creer que `psnr`, `ssim` o `metadata=print` no funcionan.
9. **Un solo `filter_complex` para todo el episodio.** Escena por escena y `concat -c copy`.
10. **Concatenar con escenas que fallaron.** Todo lo posterior queda desincronizado de la voz.

---

## Relacionado

- `453` — cuánto preescalado hace falta de verdad para que no tiemble: el otro extremo de esta cuenta
- `452` — el coste de las capas, y por qué el paralaje sale barato si están preescaladas
- `450` y `451` — las decisiones de gesto y velocidad que se están pagando aquí
- `102` — `scale`, `flags=lanczos` y el orden correcto de la cadena de filtros
- `422` — **el marco general del coste**: aquel mide lo que cuesta CUALQUIER
  efecto en render y en atención; aquí solo se aplica al movimiento sobre fijo.
  El instrumento y el protocolo de decisión viven allí, no se repiten aquí
- `108` — `psnr`, `ssim` y el resto del instrumental de medida
- `132` y `134` — render reproducible y procesado por lotes
- `canales_lushows/248` — pre-escalado y caché dentro de un motor real, con el fallo de la caché por nombre
