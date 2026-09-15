# 162 · Leer un espectrograma

**Qué resuelve:** el medidor de loudness (`86`) dice **cuánto** suena; el espectrograma
dice **qué** suena y **dónde**. Es lo que distingue «el colchón está alto» de «el colchón
está encima de la banda de la voz», que son dos problemas distintos con dos arreglos
distintos.

---

## El comando, y la trampa del muestreo

```bash
ffmpeg -y -v error -i salida/episodio01.mp4 -lavfi \
  "aresample=48000,showspectrumpic=s=1280x480:mode=combined:legend=1:\
scale=log:start=20:stop=16000:color=intensity" salida/_espectro.png
```

⚠️ **Sin `start`/`stop` la imagen no sirve.** El audio del piloto está a **96 kHz**, así
que el espectrograma cubre de 0 a 48 kHz y los 80-4000 Hz donde vive el habla ocupan el
8% del alto: no se puede juzgar nada. Acotado a 20-16000 Hz se vuelve legible. Y eso ya
es un hallazgo: **por encima de 22 kHz no hay absolutamente nada**, así que los 96 kHz
duplican el archivo sin aportar un dato. El episodio se entrega a 48 kHz.

| Parámetro | Para qué |
|---|---|
| `mode=combined` | Las dos pistas superpuestas: es lo que hay que juzgar |
| `mode=separate` | Una encima de otra: sólo para buscar diferencias entre canales |
| `scale=log` | Decibelios. En lineal no se ve nada por debajo de −40 dB |
| `start=20:stop=16000` | La banda útil. Obligatorio si el archivo no está a 48 kHz |
| `s=1280x480` | 16 s por cada 256 px: se distinguen sílabas |
| `color=intensity` | Azul = suelo, rojo = cuerpo, amarillo = fuerte |

Coste real en la máquina de 2009: **23 s** para un episodio de 80 s.

## Qué se lee, banda por banda

| Banda | Qué vive ahí | Qué es un defecto |
|---|---|---|
| 20-80 Hz | Retumbe, el tono grave del colchón | Una línea horizontal continua y brillante: se come cabecera y no se oye en móvil |
| 80-250 Hz | **Fundamental de la voz** | Si la voz no pinta aquí, está filtrada de más y suena flaca |
| 250-2 kHz | **Cuerpo de la voz.** La mayor parte de la energía | Si el colchón pinta igual de fuerte, la voz pierde el frente |
| **2-5 kHz** | **Presencia: consonantes e inteligibilidad** | Si el colchón está más alto aquí que la voz, se entiende peor aunque suene igual de fuerte |
| 5-11 kHz | Aire, sibilantes, brillo de los efectos | Bandas horizontales continuas = ruido del colchón, no voz |
| 11-16 kHz | Casi nada, salvo efectos | Un **corte plano** a los 11 kHz: el material viene de MP3 |

## Lo que dice el piloto

Leído en `episodio01.mp4` (80,28 s) sobre el espectrograma acotado:

1. **Corte plano en ~11 kHz**, y encima un damero disperso hasta 15 kHz: la firma de un
   MP3. La locución se guarda como `locucion.mp3` y su octava alta está recortada. No se
   oye como defecto, pero conviene saberlo antes de culpar al brillo de la mezcla.
2. **Línea continua y brillante entre 20 y 100 Hz durante los 80 segundos**: el tono
   grave del colchón. Cumple su función, pero ocupa cabecera en una banda que el móvil
   ni reproduce.
3. **Columnas verticales de banda completa** en ~10,0 · 15,0 · 20,5 · 55,2 · 70,2 s: los
   destellos con su golpe. Que crucen todo el espectro es correcto —un golpe es un
   transitorio—; uno **sin** columna sería un fogonazo mudo.
4. **Ni un hueco negro.** El colchón llena todas las pausas, que es justo lo que se
   buscaba al arreglar los «clics» (`86`).

## El complemento numérico

La imagen orienta; el número decide. La energía media por banda del episodio terminado:

```bash
for B in "20 80" "80 250" "250 2000" "2000 5000" "5000 11000" "11000 16000"; do
  set -- $B
  echo -n "$1-$2 Hz : "
  ffmpeg -hide_banner -nostats -i salida/episodio01.mp4 \
    -af "aresample=48000,highpass=f=$1:p=2,lowpass=f=$2:p=2,volumedetect" \
    -f null - 2>&1 | grep -E "mean_volume|max_volume" | sed 's/.*] //' | tr '
' ' '
  echo
done
```

```
20-80 Hz       : mean_volume: -29.4 dB  max_volume: -14.0 dB
80-250 Hz      : mean_volume: -21.7 dB  max_volume:  -5.2 dB
250-2000 Hz    : mean_volume: -22.1 dB  max_volume:  -2.5 dB
2000-5000 Hz   : mean_volume: -30.6 dB  max_volume:  -5.4 dB   <-- presencia
5000-11000 Hz  : mean_volume: -28.9 dB  max_volume:  -3.9 dB
11000-16000 Hz : mean_volume: -35.9 dB  max_volume: -11.3 dB
```

- **La presencia (2-5 kHz) está 8,5 dB por debajo del cuerpo (250-2 k):** mezcla cálida y
  algo cerrada, con las consonantes menos apoyadas de lo que podrían.
- **La banda 5-11 kHz está 1,7 dB POR ENCIMA de la presencia.** Eso no lo pone la voz: lo
  pone el colchón, que es ruido y reparte energía hacia arriba. Es la definición de «el
  colchón le pisa la banda de la voz». Se arregla con el paso bajo del ambiente o una
  campana negativa entre 2 y 5 kHz — **no** bajando el colchón entero, que devolvería los
  clics de las pausas.

## Comparar la voz sola con la mezcla

La forma rápida de saber si el colchón estorba: el mismo espectrograma dos veces.

```bash
ffmpeg -y -v error -i audio/locucion.mp3 -lavfi \
  "aresample=48000,showspectrumpic=s=1280x480:legend=1:scale=log:start=20:stop=16000" _voz.png
ffmpeg -y -v error -i salida/episodio01.mp4 -lavfi \
  "aresample=48000,showspectrumpic=s=1280x480:legend=1:scale=log:start=20:stop=16000" _mezcla.png
```

Lo que aparece en `_mezcla.png` y no está en `_voz.png` es el colchón, la música y los
efectos. Si eso nuevo pinta fuerte **entre 2 y 5 kHz**, estorba, por mucho que el LUFS
integrado esté en su sitio.

## Patrones y su causa

| Lo que se ve | Causa | Arreglo |
|---|---|---|
| Línea horizontal fina y constante en 50/60 Hz o sus múltiplos | Zumbido de red en una grabación | `highpass=f=80` o un `anequalizer` estrecho |
| Corte plano y limpio a 11/15/16 kHz | El material es MP3 o AAC | No es arreglable: se acepta o se regraba la fuente |
| Bandas horizontales continuas por encima de 5 kHz | Ruido de fondo, no voz | Paso bajo al colchón, no compresor |
| Columna vertical que llega al tope de la escala | Un golpe recortando | Bajar ese efecto; mirar el pico real (`86`) |
| Tramos negros de banda completa | Silencio absoluto: no hay room tone | Es la causa de los «clics» de pausa |
| Todo blanco arriba y abajo del habla | Loudness demasiado alto o compresor aplastando | LRA (`86`) lo confirma |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Sacar el espectrograma sin acotar la banda | Con 96 kHz, la voz cabe en el 8% del dibujo y no se juzga nada |
| Usar `scale=lin` | Todo lo que esté por debajo de −40 dB desaparece |
| Juzgar la mezcla sin el espectrograma de la voz sola | No se sabe qué parte es voz y qué parte colchón |
| Bajar el colchón entero porque «pisa la voz» | Vuelven los clics en las pausas: el problema era la banda, no el nivel |
| Leer el espectrograma y no medir | Una imagen no es un umbral; los decibelios por banda sí |
| Confiar en el espectrograma para el nivel | Es un mapa, no un medidor: el nivel lo dan `ebur128` y `volumedetect` |

## Relacionado

`86` medir el audio · `85` ducking y espacio · `87` voz a fondo · `80` arquitectura de la
mezcla · `129` medir si la música estorba · `168` reproducir antes de afirmar
