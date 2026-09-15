# 292 — Stems y organización de la mezcla

Un **stem** es una pista que contiene todo lo de una función, y nada más. La voz completa del video en
un archivo. La música completa en otro. Los efectos en otro. El ambiente en otro.

No es un capricho de estudio grande. Es la diferencia entre "cámbiame la música" costando 40 segundos o
costando dos horas.

---

## Los cuatro stems

Para video social, comercial y corporativo, cuatro stems resuelven el 99% de los casos:

| Stem | Qué contiene | Nombre de archivo |
|---|---|---|
| **VOZ** | locución, entrevistas, testimonios, TTS | `01_VOZ.wav` |
| **MUSICA** | música de fondo, stingers musicales | `02_MUSICA.wav` |
| **FX** | efectos puntuales: whoosh, impactos, clics, riser | `03_FX.wav` |
| **AMB** | room tone, ambiente de local, calle, naturaleza | `04_AMB.wav` |

El número al principio no es decorativo: hace que el `ls` y el glob `*.wav` los devuelvan siempre en el
mismo orden, y ese orden es el orden de la jerarquía (`291`). Cuando escribes el `filter_complex`, las
entradas caen en el orden correcto sin que tengas que pensarlo.

Si la pieza es más compleja, se abren sub-stems, no stems nuevos:

```
01_VOZ_principal.wav
01_VOZ_secundaria.wav      ← el otro entrevistado
03_FX_transiciones.wav
03_FX_interfaz.wav          ← los clics de la demo de pantalla
```

Se agrupan por prefijo, no por invención. Regla: **si dos cosas se van a mover juntas siempre, son el
mismo stem.**

---

## La regla que hace que todo funcione: todos empiezan en cero

**Todos los stems duran exactamente lo mismo y arrancan en el mismo instante que el video.** Si la
música entra en el segundo 4, el stem `02_MUSICA.wav` tiene 4 segundos de silencio al principio.

Esto suena a desperdicio de disco y es la decisión más importante del módulo. Con stems alineados desde
cero:

- Los juntas con `amix` sin un solo `adelay`. Cero riesgo de desfase.
- Puedes intercambiar cualquiera por otra versión sin recalcular tiempos.
- Puedes medir cada uno con `astats` y comparar peras con peras.
- Si el video cambia de duración, ves inmediatamente cuál stem quedó corto.

```bash
# generar un stem con silencio adelante y relleno atrás hasta la duración exacta del video
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 video.mp4)

ffmpeg -i musica_recortada.wav -af "
  adelay=4000|4000,
  apad
" -t "$DUR" -c:a pcm_s24le 02_MUSICA.wav
```

`adelay=4000|4000` mete los 4 segundos de silencio al principio (milisegundos, un valor por canal).
`apad` agrega silencio infinito al final y `-t "$DUR"` lo corta en la duración exacta del video. Sin
`apad`, `-t` no puede alargar nada: solo recorta.

Verifica siempre que quedaron iguales:

```bash
for f in 0*.wav; do
  printf "%-28s %s\n" "$f" "$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")"
done
```

Si un archivo sale con 27.98 y otro con 28.00, alguno se va a cortar antes. Igualarlos ahora te ahorra
un render de 20 minutos que sale mal al final.

---

## El formato de los stems

| Parámetro | Valor | Por qué |
|---|---|---|
| Formato | **WAV** (`pcm_s24le`) | sin pérdida; MP3 entre pasos acumula daño |
| Frecuencia | **48.000 Hz** | es el estándar de video; 44.100 obliga a remuestrear |
| Bits | **24** | 144 dB de rango: nunca vas a saturar un stem |
| Canales | **estéreo** en música y ambiente, **mono** en voz | ver abajo |

**La voz va en mono.** Una voz es una sola fuente, en el centro. Grabarla o guardarla en "estéreo" no
agrega nada: duplica el archivo y abre la puerta a problemas de fase (`299`). Se convierte al final,
cuando se mezcla.

```bash
# forzar mono a 48 kHz, 24 bits
ffmpeg -i voz_cruda.wav -ac 1 -ar 48000 -c:a pcm_s24le 01_VOZ.wav
```

**Nunca guardes un stem normalizado a −14 LUFS.** El stem se guarda al nivel de mezcla, con el pico bien
lejos del techo (−6 dB de pico está perfecto). La sonoridad se ajusta una sola vez, sobre la mezcla
final (`293`).

---

## La estructura de carpetas

```
proyecto-reel-restaurante/
├── 00_BRUTO/                  ← lo que llegó, intocable
│   ├── video/
│   └── audio/
├── 01_TRATADO/                ← cada elemento después del bloque 7
│   ├── voz_tomas_limpias/
│   ├── musica_recortada.wav
│   └── fx_originales/
├── 02_STEMS/                  ← los cuatro archivos alineados desde 0
│   ├── 01_VOZ.wav
│   ├── 02_MUSICA.wav
│   ├── 03_FX.wav
│   └── 04_AMB.wav
├── 03_MEZCLA/
│   ├── mezcla_v03.wav         ← sin normalizar
│   └── mezcla_v03_-14LUFS.wav ← entregable
├── mezclar.sh                 ← el script que reconstruye todo
└── mapa_de_mando.txt          ← el plan de 291
```

`00_BRUTO/` no se toca nunca. Si algo salió mal, siempre puedes volver ahí. Convención completa en `135`.

---

## El script de mezcla: lo que convierte esto en método

Con stems alineados, la mezcla completa cabe en un script corto que puedes correr cuantas veces quieras.
**Este archivo es el proyecto**, más que cualquier archivo de audio.

```bash
#!/usr/bin/env bash
# mezclar.sh — reconstruye la mezcla desde los stems
set -euo pipefail

S=02_STEMS
OUT=03_MEZCLA
mkdir -p "$OUT"

# --- niveles (ver mapa_de_mando.txt y modulo 291) ---
VOL_VOZ=0
VOL_MUS=-20
VOL_FX=-9
VOL_AMB=-38

ffmpeg -y \
  -i "$S/01_VOZ.wav" \
  -i "$S/02_MUSICA.wav" \
  -i "$S/03_FX.wav" \
  -i "$S/04_AMB.wav" \
  -filter_complex "
    [0:a] volume=${VOL_VOZ}dB [voz];
    [1:a] volume=${VOL_MUS}dB, equalizer=f=3000:t=q:w=1.2:g=-4 [mus];
    [2:a] volume=${VOL_FX}dB [fx];
    [3:a] volume=${VOL_AMB}dB, lowpass=f=7000 [amb];
    [mus][voz] sidechaincompress=
        threshold=0.05:ratio=8:attack=15:release=350 [musd];
    [voz][musd][fx][amb] amix=inputs=4:duration=longest:normalize=0 [mix]
  " \
  -map "[mix]" -c:a pcm_s24le "$OUT/mezcla.wav"

echo "Mezcla lista. Medición:"
ffmpeg -i "$OUT/mezcla.wav" -af astats=metadata=1 -f null - 2>&1 \
  | grep -E "RMS level dB|Peak level dB|Number of clipped" | head -6
```

Lo que ganas: cambiar la música del video es reemplazar `02_MUSICA.wav` y correr `./mezclar.sh`. Cuarenta
segundos. Sin stems, es rehacer la sesión.

---

## Por qué los stems te salvan de verdad: los cinco casos reales

**1. "Cámbiame la música."** Reemplazas un archivo. El resto queda idéntico, incluido el ducking, que se
recalcula solo contra la voz.

**2. "Hazme la versión sin voz para poner subtítulos."** Quitas `01_VOZ` del `amix` — pero ojo, hay que
apagar también el `sidechaincompress`, porque sin voz el ducking no tiene contra qué reaccionar.

```bash
# versión sin voz: música al frente (-6 dB), sin ducking
ffmpeg -y -i 02_STEMS/02_MUSICA.wav -i 02_STEMS/03_FX.wav -i 02_STEMS/04_AMB.wav \
  -filter_complex "[0:a]volume=-6dB[m];[1:a]volume=-9dB[f];[2:a]volume=-34dB[a];
                   [m][f][a]amix=inputs=3:duration=longest:normalize=0[mix]" \
  -map "[mix]" -c:a pcm_s24le 03_MEZCLA/mezcla_sin_voz.wav
```

**3. "La versión en otro idioma."** Cambias `01_VOZ.wav` por la locución doblada (`79`) y corres el
script. La música, los efectos y el ambiente se mantienen exactos.

**4. "Instagram lo bajó, súbelo."** No re-mezclas: renormalizas la mezcla (`293`).

**5. "El cliente dice que la música tapa la voz."** Cambias `VOL_MUS=-20` a `-24` en una línea del script
y vuelves a correr. Sin tocar nada más.

Sin stems, los cinco casos son "rehacer la mezcla".

---

## Consolidar tomas en un stem sin dejar huecos

El stem de voz casi nunca es una grabación seguida: son doce tomas buenas de veinte. Consolidar bien es
la mitad del trabajo.

```bash
# armar el stem de voz colocando cada toma en su instante exacto
ffmpeg -y \
  -i toma_03.wav -i toma_07.wav -i toma_12.wav \
  -filter_complex "
    [0:a] adelay=1800|1800  [a0];
    [1:a] adelay=9400|9400  [a1];
    [2:a] adelay=17250|17250 [a2];
    [a0][a1][a2] amix=inputs=3:duration=longest:normalize=0, apad [voz]
  " \
  -map "[voz]" -t 28 -c:a pcm_s24le 02_STEMS/01_VOZ.wav
```

Fíjate: `amix` aquí no está mezclando voces simultáneas, está **pegando tomas en el tiempo**. Como cada
una tiene silencio digital antes y después, no se suman entre ellas. Es más seguro que `concat` porque
los tiempos son absolutos: si mueves una toma, las demás no se corren.

**Y ese silencio digital entre tomas es exactamente el problema que resuelve `296`.** Un stem de voz
consolidado tiene huecos de silencio absoluto (piso −∞) entre frases grabadas con piso a −46,5 dB. El
oído oye el salto. Por eso el stem `04_AMB.wav` no es opcional.

---

## Nombrar y versionar

```
mezcla_v01.wav      ← primera pasada
mezcla_v02.wav      ← música más abajo, cliente pidió
mezcla_v03.wav      ← con el efecto del logo
mezcla_v03_FINAL.wav        ← NO
mezcla_v03_FINAL_ok.wav     ← NO
mezcla_v03_FINAL_ok2.wav    ← NO, por favor
```

Números, no adjetivos. La versión que se entrega se copia con el nombre del entregable:

```
GastroLatam_reel_costos_9x16_v03_-14LUFS.wav
```

Y en un archivo de texto al lado, dos líneas de qué cambió en cada versión. En tres semanas no te vas a
acordar de por qué la v02 existe.

---

## Cuándo NO vale la pena hacer stems

Sé honesto: los stems tienen un costo de organización. No siempre se justifica.

- **Video de un solo elemento** (una locución sobre un plano, sin música). No hay nada que separar.
- **Pieza desechable** que se publica hoy y no se vuelve a tocar (una historia de 24 horas).
- **Cuando el material entero dura menos de 10 segundos** y la mezcla es un `amix` de dos entradas.

Todo lo demás — cualquier cosa que un cliente pueda pedir cambiar, cualquier cosa que vaya a tener una
segunda versión, cualquier cosa que dure más de 20 segundos — va con stems.

---

## Errores comunes

1. **Stems de distinta duración.** El más corto se acaba antes y el ducking se desengancha. Iguala con
   `apad` + `-t`.
2. **Stems que no empiezan en cero.** Te obliga a recalcular `adelay` cada vez que cambias algo. Silencio
   al principio, siempre.
3. **Guardar stems en MP3.** Cada paso agrega pérdida y el `sidechaincompress` reacciona raro a los
   artefactos. WAV 24 bits.
4. **Mezclar frecuencias de muestreo.** Un stem a 44.100 y otro a 48.000 hace que ffmpeg remuestree
   silenciosamente y a veces desfasa. Todo a 48 kHz.
5. **Normalizar cada stem a −14 LUFS.** Cuatro stems a −14 dan una mezcla a −8 y saturada. Los stems van
   al nivel de mezcla, sin normalizar.
6. **Guardar la voz en estéreo.** Duplica el archivo y abre problemas de fase. Voz en mono.
7. **No guardar el script de mezcla.** Si la mezcla vive solo en un comando que escribiste en la terminal,
   la perdiste.
8. **Meter la música y los efectos en el mismo stem.** Es exactamente el cambio que más piden los
   clientes. Sepáralos.
9. **`amix` sin `normalize=0`.** Sale todo 12 dB abajo.
10. **Versionar con adjetivos.** `FINAL_ok2` no es una versión, es una confesión.
11. **Borrar `00_BRUTO/` para ahorrar disco.** El día que necesites volver, no hay vuelta.
12. **Olvidar el stem de ambiente porque "no se oye".** Es el que pega los planos (`296`). Que no se note
   es el punto.

---

## Checklist

- [ ] Existen los **cuatro stems** (VOZ, MUSICA, FX, AMB), numerados por orden de jerarquía.
- [ ] Todos los stems **empiezan en 0** y tienen **la misma duración** que el video (verificado con
      `ffprobe`).
- [ ] Todos son **WAV 48 kHz / 24 bits**; la voz en **mono**.
- [ ] **Ningún stem está normalizado**; el nivel de sonoridad se aplica al final (`293`).
- [ ] Existe `mezclar.sh` y **reconstruye la mezcla completa** desde los stems.
- [ ] Los niveles de la mezcla están en **variables** al principio del script, no repartidos en el filtro.
- [ ] `amix` lleva **`normalize=0`**.
- [ ] La carpeta `00_BRUTO/` está **intacta**.
- [ ] Existe `mapa_de_mando.txt` con el plan de jerarquía (`291`).
- [ ] Las versiones se numeran (**v01, v02, v03**), no se adjetivan.
- [ ] Se probó reemplazar un stem y volver a correr el script: **funciona sin tocar nada más**.
- [ ] El stem de **ambiente existe**, aunque no se note.
