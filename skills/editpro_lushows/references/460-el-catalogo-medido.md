# 460 — El catálogo medido: qué mide mal cada efecto que delata

**Qué resuelve:** el módulo `56-efectos-que-se-ven-baratos.md` es la lista negra honesta y sigue siendo
la puerta de entrada — ahí está el *porqué* de cada efecto. Este bloque (460–469) es la otra mitad: el
*cuánto*. Por cada efecto, una magnitud que se puede sacar de la imagen con un comando, el umbral por
encima del cual delata, y el sustituto.

El instrumental ya está construido: el **bloque 42 (`420`–`429`)** monta el arnés genérico —`utime`,
PSNR, SSIM, peso codificado, `signalstats`— y `421-medir-lo-que-un-efecto-cambia.md` reparte la
magnitud correcta por familias de efecto. **Este bloque no lo reconstruye: lo aplica a los nueve
efectos concretos que delatan.** Si lo que buscas es "cómo se mide un efecto cualquiera", tu módulo es
`420`; si es "por qué este efecto concreto canta y a partir de qué número", es este.

La diferencia no es académica. "Ese zoom se ve barato" es una opinión y el cliente puede discutirla.
"Ese zoom deja la imagen en el 3% de su nitidez durante 10 fotogramas seguidos" es un número, y contra
un número no se discute: se decide. Ver `08-presentar-y-defender-un-corte.md`.

---

## 1. La frontera con dirección creativa

> `directorcreativo_lushows` **decide** qué es de marca y qué es genérico. Es el dueño del criterio
> estético: la paleta, el degradado, la tendencia, lo que huele a plantilla.
> `editpro` **mide y ejecuta**: cómo se detecta eso en un fotograma ya montado y qué se hace en la
> línea de tiempo.

Cuando la pregunta es "¿este morado es de la marca?", no es tuya: es de `directorcreativo` (sus módulos
`33`, `34`, `37`, `157`, `97`). Cuando la pregunta es "¿cómo demuestro que este fotograma ya montado
está teñido y cuánto?", eso sí es tuyo, y está en `462`.

---

## 2. Las seis magnitudes que delatan

Todo el bloque se apoya en seis mediciones. No hay más, y con estas seis caza casi todo:

| Magnitud | Qué revela | Herramienta | Módulo |
|---|---|---|---|
| **Nitidez por fotograma** (energía de alta frecuencia) | desenfoques, zooms, papilla | laplaciano en numpy | `461`, `469` |
| **Distribución de matiz y canal mínimo** | tinte global, morado de plantilla | HSV + comparación de canales | `462` |
| **Diferencia entre fotogramas (YDIF) y su autocorrelación** | eventos con metrónomo | `signalstats` | `463` |
| **Distribución de tamaños de mancha** | partículas monodispersas | componentes conexas | `464` |
| **Luz añadida por decil de luminancia** | capas aditivas pegadas | resta contra la placa | `465` |
| **Anchura de penumbra frente a la distancia** | sombras falsas | perfil 10→90% | `466` |

Y dos que son de movimiento, no de imagen: el **índice de frenado** de una animación (`467`) y la
**dispersión entre planos** de una corrección de color (`468`).

---

## 3. El banco de pruebas

Todo el bloque se midió sobre material real (fotogramas de archivo del piloto de PAPER EMPIRES) a
**540×960 y 30 fps**, para que cada medición corra en menos de un minuto en un ordenador viejo. Los
comandos de producción van a resolución completa; las cifras de las tablas salen del banco reducido.

```bash
# preparar el banco: dos planos de 1,5 s a partir de dos fotogramas
for f in plano_a plano_b; do
  ffmpeg -y -loglevel error -i $f.jpg -vf scale=540:960 -frames:v 1 s_$f.png
  ffmpeg -y -loglevel error -loop 1 -i s_$f.png -t 1.5 -r 30 \
    -c:v libx264 -crf 14 -pix_fmt yuv420p s_$f.mp4
done
```

CRF 14 no es capricho: si codificas el banco a CRF 23 estás midiendo el codificador, no el efecto. Para
medir, siempre material poco comprimido. Ver `93-compresion-sin-perder-calidad.md`.

---

## 4. La trampa que hace parecer que la medición falló

🔴 **Los filtros de medida de ffmpeg (`psnr`, `ssim`, `signalstats`, `blackdetect`, `freezedetect`)
imprimen en nivel `info`.** Si tienes el reflejo de poner `-loglevel error` —que es lo correcto para
renderizar— **no sale absolutamente nada** y parece que el filtro no funcionó.

Comprobado, mismo archivo, mismo filtro:

```bash
# no imprime NADA — y no hay ningún error
ffmpeg -hide_banner -loglevel error -i clip.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null - 2>&1 | head -5

# 45 líneas, una por fotograma
ffmpeg -hide_banner -loglevel info -i clip.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null - 2>&1 | grep -c YDIF
```

Salida real: `0` líneas en el primero, `45` en el segundo (45 fotogramas = 1,5 s a 30 fps). La regla:
**para renderizar, `-loglevel error`; para medir, `-loglevel info` y `2>&1`.** Ver también
`109-ffmpeg-trampas-y-errores.md`.

---

## 5. El índice del bloque

| Módulo | Efecto | Qué se mide | Umbral que delata | Sustituto |
|---|---|---|---|---|
| `461` | Zoom con desenfoque | nitidez por fotograma | >2 fotogramas bajo el 70% de la base | golpe de 3 f (`53`) |
| `462` | Degradado morado | % de píxeles con verde como canal mínimo | >80% | duotono de marca (`64`) |
| `463` | Glitch decorativo | autocorrelación de YDIF | >0,40 en desfase 2–20 f | 2–3 f irregulares (`57`) |
| `464` | Partícula flotante | razón p90/p10 del área de mancha | <10 | tres estratos (`267`) |
| `465` | Destello pegado | % de píxeles ≥240 en la placa | <0,02% (no hay fuente) | conservar el flare real |
| `466` | Sombra dura falsa | penumbra lejos ÷ penumbra cerca | <2× | contacto + penumbra creciente |
| `467` | Keyframe lineal | % del recorrido en el último 25% del tiempo | >15% | ease out cúbico (`84`) |
| `468` | Filtro global | dispersión de la media entre planos | no baja al aplicarlo | emparejado plano a plano (`62`) |
| `469` | — | cómo rehabilitar cualquiera de los ocho | — | escala · contexto · frecuencia · material |

---

## 6. Cómo se usa esto en un encargo real

No midas todo: mide **lo que el ojo señaló** y mide **la versión que propones, al lado**. Sirve para
decidir entre dos versiones sin discutir de gustos (`369`), para defender el corte en una frase, y para
auditar material heredado o ajeno en diez minutos (`305`). Nunca para lucirse.

---

## Errores frecuentes

1. **Medir con `-loglevel error`.** No sale nada y se concluye que el filtro está roto. Es la trampa
   del punto 4 y cuesta media hora la primera vez.
2. **Medir sobre material ya comprimido para redes.** A CRF 23 la nitidez y el grano ya están tocados:
   mides el codificador.
3. **Medir el efecto sin medir el sustituto.** Un número solo no dice nada; el par sí.
4. **Usar la medición para ganar una discusión estética.** El criterio de marca es de
   `directorcreativo`. Tú aportas la evidencia, no el veredicto.
5. **Aplicar un umbral sin recalibrarlo a tu material.** Salen de un banco concreto; en material muy
   oscuro o muy plano la base cambia y el porcentaje también.
6. **Creer que un efecto que pasa las seis medidas ya es bueno.** Puede pasarlas todas y no responder a
   nada: ese es el cuarto criterio del `56`, y ese no se mide, se justifica.

---

## Relacionado

- `56-efectos-que-se-ven-baratos.md` — la lista negra cualitativa. **Léelo antes que este.**
- `108-ffmpeg-analisis-y-medicion.md` — ffprobe, astats, signalstats, blackdetect: el instrumental.
- `420-un-efecto-es-una-hipotesis.md` · `421-medir-lo-que-un-efecto-cambia.md` — **el arnés genérico.**
- `133-verificacion-automatica.md` — convertir estas medidas en un guardián del pipeline.
- `98-verificacion-del-corte.md` — la rutina de control de calidad del entregable.
- `directorcreativo_lushows/97-tendencias-de-diseno-2026.md` — qué es genérico y por qué (criterio).
- `directorcreativo_lushows/157-gradientes-y-color-generativo.md` — el anti-cliché del degradado.
