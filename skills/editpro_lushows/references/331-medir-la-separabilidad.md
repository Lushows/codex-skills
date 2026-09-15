# 331 — Medir la separabilidad con ffmpeg antes de decidir

**Qué resuelve:** convertir "esta toma se ve mejor" en un número que se puede ordenar. Cuatro medidas,
cuatro comandos, dos minutos para 16 tomas. Todo verificado en ffmpeg 8.1.2 sobre el material real de
Bendita Pola.

---

## 1. El paso previo: un fotograma por toma

No midas el video entero. Es lento y no hace falta. Saca **un fotograma representativo** de cada toma —
al 30% de su duración, que casi siempre ya tiene a la persona en cuadro — y escálalo a 540 px de ancho.
Todo lo demás se mide sobre ese PNG.

```bash
# Un fotograma al 30% de la duración, a 540 px de ancho
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 toma.mp4)
t=$(awk -v x="$d" 'BEGIN{printf "%.2f", x*0.3}')
ffmpeg -v error -ss "$t" -i toma.mp4 -frames:v 1 -vf "scale=540:-1" -y frames/toma.png
```

`-ss` **antes** de `-i` hace la búsqueda por keyframe: es instantánea aunque el archivo pese 200 MB.

Escalar a 540 no falsea nada de lo que vas a medir (medias de color, densidad de bordes) y multiplica la
velocidad por cuatro.

---

## 2. Medida 1 — Color y exposición: `signalstats`

Es el instrumento base. Da las medias de luminancia y de los dos canales de color en un solo paso.

```bash
ffprobe -v error -f lavfi "movie=toma.png,signalstats" \
  -show_entries "frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG,lavfi.signalstats.YLOW,lavfi.signalstats.YHIGH" \
  -of default=noprint_wrappers=1:nokey=1
```

Qué mira cada número:

| Etiqueta | Qué es | Lectura |
|---|---|---|
| `YAVG` | brillo medio (0–255) | por debajo de 40 la toma está oscura de verdad |
| `YLOW` / `YHIGH` | percentiles bajo y alto | `YHIGH` cerca de 255 = hay zonas quemadas |
| `UAVG` | media del canal azul-diferencia | **piel sana siempre por debajo de 128** |
| `VAVG` | media del canal rojo-diferencia | piel entre 145 y 160 aprox. |
| `SATAVG` | saturación media | por encima de 45 hay una luz de color dominando todo |

> ### ⚠️ Trampa verificada: ffprobe ignora el orden que pediste
> `ffprobe` imprime las etiquetas en el orden en que el filtro las creó, **no** en el orden en que las
> pediste. Con `signalstats` el orden real es siempre:
> **`YLOW`, `YAVG`, `YHIGH`, `UAVG`, `VAVG`, `SATAVG`.**
> Si usas `-of default=nw=1:nokey=1` y asumes tu orden, todas tus conclusiones quedan corridas. Para
> depurar, quita `nokey=1` y lee los nombres.

---

## 3. Medida 2 — Enredo del fondo: `edgedetect`

`edgedetect` pinta los bordes de blanco y todo lo demás de negro. Si después de eso mides `YAVG`, tienes
**la densidad de bordes**: qué tan enredado está el cuadro.

```bash
ffprobe -v error -f lavfi "movie=toma.png,edgedetect=low=0.1:high=0.35,signalstats" \
  -show_entries "frame_tags=lavfi.signalstats.YAVG" -of default=nw=1:nk=1
```

**Cómo se convierte a porcentaje:** el resultado va de 0 a 255. Divide entre 2,55 y tienes el porcentaje
de píxeles que son borde.

| Densidad de bordes | Qué significa |
|---|---|
| menos de 2% | fondo limpio, pared lisa, primer plano |
| 2–4% | normal, recorte tranquilo |
| 4–6% | fondo cargado; mira si el enredo está **pegado al sujeto** |
| más de 6% | rejas, plantas, sillas, gente. Recorte con pelea |

`low` y `high` van de 0 a 1 y son los umbrales del detector Canny. Usa siempre los mismos valores en todas
las tomas o los números no se pueden comparar entre sí. `low=0.1:high=0.35` funciona bien con material de
celular.

---

## 4. Medida 3 — Foco: `blurdetect`

```bash
ffprobe -v error -f lavfi "movie=toma.png,blurdetect" \
  -show_entries "frame_tags=lavfi.blur" -of default=nw=1:nk=1
```

Devuelve `lavfi.blur`. **Más alto = más borroso.** Es un número relativo: sirve para comparar tomas del
mismo rodaje, no para decir "5,2 es malo" en abstracto.

Ojo con la trampa: una toma con fondo desenfocado a propósito (un primer plano de la botella) da un valor
alto sin estar mal enfocada. Por eso el foco se mide **recortando la zona del sujeto**, nunca en el cuadro
completo. Ver `332`.

---

## 5. Medida 4 — La que decide: medir por zonas con `crop`

Las tres medidas anteriores son promedios de todo el cuadro. Los promedios mienten (`332`). La medida
que de verdad decide es la misma, pero **aplicada a una región**.

```bash
# crop=ancho:alto:x:y   — sobre el PNG de 540 px de ancho
ffprobe -v error -f lavfi "movie=toma.png,crop=80:90:230:380,signalstats" \
  -show_entries "frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG" \
  -of default=nw=1:nk=1
```

Las tres regiones que hay que medir siempre:

1. **La cara** — un recuadro pequeño sobre la mejilla y la frente. Dice si hay piel o hay neón.
2. **El fondo justo detrás del sujeto** — una franja pegada al contorno.
3. **La banda alrededor del sujeto** — para la densidad de bordes que realmente estorba.

**La resta entre 1 y 2 es la separabilidad de verdad:**

| Diferencia `YAVG` cara vs. fondo | Pronóstico del recorte |
|---|---|
| más de 60 | limpio, casi automático |
| 30 a 60 | funciona con retoque de borde |
| menos de 30 | el algoritmo va a dudar; espera halos y agujeros |
| menos de 15 | no lo intentes: cambia de toma (`336`) |

---

## 6. El caso real: las 16 tomas medidas

Material `videos/entrada`, 16 archivos, fotograma al 30%, 540 px. Números reales.

| # | Toma | YAVG | UAVG | VAVG | SAT | Bordes | Blur |
|---|---|---|---|---|---|---|---|
| 1 | 122837 escaleras | 72,3 | **128,0** | 138,0 | 13,4 | 4,24% | 5,25 |
| 2 | 123726 pasillo | 77,9 | 148,5 | 143,6 | 35,3 | 3,82% | 4,23 |
| 3 | 123910 pasillo vacío | 82,4 | 149,3 | 141,8 | 34,5 | 3,95% | 4,39 |
| 4 | 124427 mano/botella | 104,0 | 121,7 | 139,2 | 17,3 | **1,55%** | 6,95 |
| 5 | 125739 barra | 74,4 | 146,6 | 160,0 | 45,7 | 4,00% | 4,85 |
| 6 | 135553 terraza | 101,1 | **117,8** | 139,1 | 17,0 | 6,70% | 4,84 |
| 7 | 135656 terraza | 101,7 | **117,4** | 139,6 | 17,6 | 6,30% | 4,87 |
| 8 | 142916 salón | 81,3 | **163,6** | 167,9 | 57,5 | 5,42% | 4,42 |
| 9 | 143116 salón | 75,1 | **162,5** | 167,2 | 56,2 | 4,99% | 4,46 |
| 10 | 143641 cuerpo entero | 84,5 | **163,6** | 169,0 | 57,7 | 4,83% | 4,92 |
| 11 | 155416 barra | 71,7 | 140,8 | 166,8 | 49,0 | 3,14% | 4,57 |
| 12 | 155807 barra | 71,6 | 143,2 | 170,5 | 52,6 | 3,00% | 4,51 |
| 13 | 160137 barra | 70,8 | 142,0 | 170,7 | 52,2 | 3,00% | 4,43 |
| 14 | 160651 barra | 74,5 | 142,4 | 169,1 | 51,2 | 3,12% | 4,49 |
| 15 | 161405 brazos arriba | 77,2 | 142,9 | 160,9 | 45,2 | 3,11% | 4,62 |
| 16 | 161648 barra vacía | 73,0 | 149,9 | 158,8 | 46,0 | 2,59% | 5,54 |

Lo que la tabla dice sin que nadie tenga que opinar:

- **Las tomas 8, 9 y 10 tienen U entre 162 y 164.** Ahí no puede haber piel correcta: es una persona
  bañada en neón morado. Ninguna corrección de color las salva (`259`).
- **Las tomas 6 y 7 son las únicas con U por debajo de 118 y saturación por debajo de 18.** Son las de la
  terraza, con luz de día. Son las tomas buenas del rodaje, y estaban en la mitad de la lista.
- **La toma 1 da U = 128,0**, justo bajo el umbral, y aun así es la peor de todas. Por qué, en `332`.
- **La toma 4 tiene la menor densidad de bordes (1,55%)** porque es un primer plano de una mano: perfecta
  como inserto, inútil como sujeto recortable.
- Las tomas 3 y 16 no tienen a nadie: son **placas limpias** que habilitan matte por diferencia (`261`).

---

## 7. Medirlo todo de una pasada

Extrae primero un PNG por toma con el comando de la sección 1, déjalos en `frames/`, y corre esto **desde
dentro de esa carpeta** (rutas relativas: ver sección 8).

```bash
#!/usr/bin/env bash
# medir-tomas.sh — corre desde la carpeta frames/
printf "%-22s %6s %6s %6s %6s %7s %6s\n" toma YAVG UAVG VAVG SAT bordes blur
for p in *.png; do
  # OJO: el orden que devuelve signalstats es YLOW YAVG YHIGH UAVG VAVG SATAVG
  read -r ylow yavg yhigh uavg vavg sat < <(ffprobe -v error -f lavfi "movie=$p,signalstats" \
    -show_entries "frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG,lavfi.signalstats.YLOW,lavfi.signalstats.YHIGH" \
    -of default=nw=1:nk=1 | tr '\n' ' ')
  e=$(ffprobe -v error -f lavfi "movie=$p,edgedetect=low=0.1:high=0.35,signalstats" \
    -show_entries "frame_tags=lavfi.signalstats.YAVG" -of default=nw=1:nk=1)
  bl=$(ffprobe -v error -f lavfi "movie=$p,blurdetect" \
    -show_entries "frame_tags=lavfi.blur" -of default=nw=1:nk=1)
  pct=$(awk -v y="$e" 'BEGIN{printf "%.2f%%", y/2.55}')
  printf "%-22s %6.1f %6.1f %6.1f %6.1f %7s %6.2f\n" "${p%.png}" "$yavg" "$uavg" "$vavg" "$sat" "$pct" "$bl"
done
```

Guárdalo, córrelo una vez por rodaje, y la discusión de "cuál toma usamos" pasa de veinte minutos de
opiniones a una tabla ordenada.

---

## 8. Tres trampas de Windows verificadas hoy

Estas tres cuestan una hora si nadie las avisa.

**a) El `movie=` con ruta absoluta y letra de unidad.** Los dos puntos de `C:` son el separador de
opciones del filtro. Hay que escaparlos **dos veces**:

```powershell
# Funciona en PowerShell (comillas simples, DOS barras invertidas)
ffprobe -v error -f lavfi 'movie=C\\:/ruta/al/frame.png,signalstats' `
  -show_entries "frame_tags=lavfi.signalstats.YAVG" -of default=nw=1:nk=1
```

En Git Bash eso **no** funciona: MSYS reescribe la ruta y la convierte en basura (`C;C:\Program Files\Git\...`).
La solución robusta y portable: **entra a la carpeta y usa rutas relativas** en `movie=`. Verificado.

**b) `-pattern_type glob` no existe en las compilaciones de Windows.**

```
Pattern type 'glob' was selected but globbing is not supported by this libavformat build
```

Para tratar un montón de PNG como secuencia, cópialos con nombre numerado (`f00.png`, `f01.png`…) y usa
`-i "f%02d.png"`.

**c) `drawtext` sin fontconfig.** `Fontconfig error: Cannot load default config file` significa que hay
que pasar la fuente a mano: `drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':...`. Sin eso, cualquier
comando que numere las casillas de una hoja de contactos falla.

Más trampas del mismo tipo en `109`.

---

## Errores comunes

1. **Medir el video entero en vez de un fotograma.** Tarda cien veces más y dice lo mismo.
2. **Asumir que ffprobe respeta el orden de `-show_entries`.** No lo hace. `signalstats` siempre devuelve
   `YLOW YAVG YHIGH UAVG VAVG SATAVG`.
3. **Comparar densidades de bordes con umbrales distintos de `edgedetect`.** Los números dejan de ser
   comparables. Fija `low` y `high` y no los toques.
4. **Sacar el fotograma en el segundo 0.** Casi siempre es la mano tapando el lente o el sitio vacío.
5. **Medir solo el cuadro completo.** Es el error del que trata `332` entero.
6. **Leer `blurdetect` como valor absoluto.** Solo sirve comparando tomas del mismo rodaje.
7. **Medir después de aplicar un filtro de color.** Se mide el material como salió de la cámara; si no,
   estás midiendo tu propia corrección.
8. **Medir un PNG guardado con perfil de color raro.** Guarda los fotogramas con `-vf scale` a secas y
   sin conversiones intermedias.
9. **Escalar cada toma a un tamaño distinto.** La densidad de bordes cambia con la escala. Mismo ancho
   para todas.
10. **Confiar en la tabla y no mirar las imágenes.** La tabla ordena candidatas; el ojo decide (`332`).
11. **Pelear con `movie=` y rutas absolutas en Windows.** Entra a la carpeta y usa rutas relativas.
12. **Usar `-pattern_type glob` en Windows.** No existe; renumera los archivos.
13. **No guardar la tabla.** En dos semanas nadie recuerda por qué se eligió esa toma.

---

## Checklist

- [ ] Saqué **un fotograma por toma**, al mismo porcentaje y al mismo ancho.
- [ ] Medí `signalstats` en las **finalistas**, con el orden de etiquetas correcto.
- [ ] Convertí la densidad de bordes a **porcentaje** (dividir entre 2,55).
- [ ] Usé los **mismos umbrales** de `edgedetect` en todas.
- [ ] Medí `blurdetect` **en la zona del sujeto**, no en el cuadro completo.
- [ ] Medí la **cara** y el **fondo pegado al sujeto** por separado, con `crop`.
- [ ] Calculé la **diferencia de YAVG** entre cara y fondo.
- [ ] Verifiqué que la cara dé **U por debajo de 128**.
- [ ] Marqué las tomas con **U por encima de 150**: ahí no hay piel que salvar.
- [ ] Identifiqué si hay **placa limpia** entre las tomas.
- [ ] Miré las imágenes además de la tabla.
- [ ] Guardé la tabla junto al material (`317`).
