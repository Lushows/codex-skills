# 167 — Directo y streaming

**Qué resuelve:** dos cosas que van juntas. Primera: cómo se prepara un directo para que no sea un
desastre técnico ni un ladrillo de dos horas. Segunda — y donde está el trabajo real del editor — cómo se
saca contenido publicable de la grabación de un directo, que es el material más difícil que existe: mal
encuadrado, mal iluminado, mal audio y sin estructura.

> **La regla del formato:** un directo se emite una vez y se ve para siempre en pedazos. El 90% de las
> vistas de un directo llegan **después**, en los cortos. Si grabas el directo pensando solo en quien está
> viendo en vivo, botas el 90% del valor.

---

## PARTE 1 — PREPARAR EL DIRECTO

## 1. La estructura que hace un directo mirable

Un directo sin estructura dura dos horas y no se puede cortar. Uno con estructura dura lo mismo y produce
15 cortos.

```
0:00 – 0:05   Sala de espera / pantalla de "empezamos en 5 min" con música
0:05 – 0:10   Entrada. Saludo. Qué se va a hacer hoy (la agenda visible en pantalla)
0:10 – 0:15   Repaso de lo anterior / contexto para quien llega tarde
0:15 – …      BLOQUES. Cada uno con su rótulo y su cierre.
…             Preguntas
final         Cierre con lo que viene la próxima
```

### La técnica del bloque cerrado

Cada 8–12 minutos cierras un bloque explícitamente: "Listo, eso era el tema del costeo. Ahora vamos a…".

Eso hace tres cosas:
1. Le da a quien llega tarde un punto de entrada
2. Marca el corte para el editor (**cada bloque es un corto potencial**)
3. Evita el efecto "esto no va para ningún lado"

**El truco del reinicio:** cada 10 minutos vuelves a decir quién eres y qué se está haciendo. En directo
la gente entra y sale constantemente; sin reinicios, el 70% de la audiencia nunca supo de qué se trataba.

---

## 2. Lo técnico que hay que dejar amarrado antes

### Bitrate y resolución

| Plataforma | Resolución | Bitrate video | Audio |
|---|---|---|---|
| YouTube Live 1080p60 | 1920x1080 | 6.000–9.000 kbps | 128–192 kbps |
| YouTube Live 1080p30 | 1920x1080 | 4.500–6.000 kbps | 128 kbps |
| Instagram Live | 1080x1920 | 3.500 kbps | 128 kbps |
| TikTok Live | 1080x1920 | 3.500–5.000 kbps | 128 kbps |
| Facebook Live | 1920x1080 | 4.000 kbps | 128 kbps |

**Regla de subida:** tu velocidad de subida real tiene que ser **el doble** del bitrate. Si emites a 6.000
kbps necesitas 12 Mbps de subida estables. Mide la subida, no la bajada, y mídela a la hora del directo.

### Configuración de codificación que no falla

```
Codificador:      x264 (CPU) o NVENC (GPU NVIDIA) — NVENC si tienes tarjeta
Preset:           veryfast (x264) / quality (NVENC)
Keyframe:         2 segundos  ← obligatorio, todas las plataformas lo exigen
Perfil:           high
Control de tasa:  CBR (tasa constante)
```

**El keyframe a 2 s no es opcional.** Con keyframes cada 10 s el video se ve a bloques y las plataformas
lo rechazan o lo degradan.

### La grabación local: lo más importante de todo

**Graba siempre en local, aparte del stream.** La grabación de la plataforma viene comprimida, con caídas
y con el bitrate del stream. La local viene limpia.

```
Stream:      6.000 kbps, con caídas → sirve para el vivo
Local:       CQP 18 / CRF 18, sin caídas → sirve para editar
```

En OBS: Configuración → Salida → Grabación, con calidad "Indistinguible" y contenedor **mkv** (si se cae
la luz, el mkv sobrevive; el mp4 se corrompe entero). Después se remuxea sin recodificar:

```bash
ffmpeg -i directo.mkv -c copy directo.mp4
```

### Audio del directo

- **Graba pistas separadas** si hay más de una fuente (voz, música, invitado remoto). En OBS: Salida →
  Grabación → "Pistas de audio" 1,2,3.
- Deja el máster con **techo a -3 dBFS**, no a 0. En vivo no hay segunda oportunidad para arreglar un
  clipeo.
- Monitorea con audífonos. Siempre. Un directo de una hora con el micrófono en el canal equivocado pasa
  más de lo que crees.

---

## 3. Cosas de rodaje que multiplican el material aprovechable

Estas cinco decisiones son las que separan un directo del que sí se puede sacar contenido:

1. **Encuadre con aire arriba y a los lados.** Si emites en 16:9 y encuadras justo, no puedes reencuadrar
   a vertical después. Deja al sujeto centrado con margen.
2. **Luz constante.** El directo suele durar hasta que anochece; si la luz es natural, a los 40 minutos
   estás en penumbra y los cortos del final no sirven.
3. **Repite las preguntas del chat en voz alta** antes de responder. Sin eso, la respuesta es inservible
   como corto.
4. **Di los datos completos.** "Como decía", "eso que mencionamos" — inservible. "El costo de un plato se
   calcula sumando insumo, merma y porción" — corto publicable.
5. **Marca los momentos en vivo.** Cada vez que digas algo que sirve, di una palabra clave (o toca una
   tecla que ponga un marcador). En OBS hay marcadores de capítulo; también sirve anotar el minuto en un
   papel.

---

## PARTE 2 — SACAR CONTENIDO DE LA GRABACIÓN

## 4. Diagnóstico del archivo

Antes de nada, mira qué te llegó:

```bash
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=codec_name,width,height,r_frame_rate,channels -of default=nw=1 directo.mkv
```

Y busca los tramos rotos (caídas de conexión que en la grabación local no deberían existir, pero en la
descargada de la plataforma sí):

```bash
# Fotogramas negros o congelados
ffmpeg -i directo.mkv -vf "blackdetect=d=1:pic_th=0.98" -f null - 2> negros.txt
ffmpeg -i directo.mkv -vf "freezedetect=n=-60dB:d=2" -f null - 2> congelados.txt
```

---

## 5. Encontrar los momentos sin ver dos horas

Tres herramientas, en este orden:

### a) La transcripción con timecodes

Es la principal. Se genera, se lee en diagonal, y se marca. → `124-transcripcion-y-timecodes-con-ia.md`.

Buscas patrones de lenguaje que casi siempre marcan un buen corto:

```
"lo que pasa es que…"        → explicación
"el error más grande es…"    → afirmación fuerte
"a mí me pasó que…"          → historia
"nadie te dice que…"         → contraintuitivo
"la gente cree que… pero"    → mito vs realidad
"¿me preguntan si…"          → pregunta del chat respondida
```

### b) La curva de audio

Los picos de volumen marcan risas, énfasis y discusión:

```bash
ffmpeg -i directo.mkv -filter_complex \
 "aformat=channel_layouts=mono,showwavespic=s=7680x400:colors=cyan" -frames:v 1 onda_directo.png
```

Una imagen de 7680 px para 2 horas: cada píxel es ~1 segundo. Los cerros son tus candidatos.

### c) El chat

Si lo guardaste, los momentos con más mensajes por minuto son los de más energía. Es el único formato
donde el público te marca los picos gratis.

---

## 6. Extraer los tramos

Con la lista de timecodes, extraes en dos tiempos: primero copia rápida con margen, después corte fino.

```bash
# Extracción con margen (5 s antes, 5 s después), sin recodificar
ffmpeg -ss 00:47:12 -to 00:48:40 -i directo.mkv -c copy tramos/12_costeo.mp4
```

⚠️ Con `-c copy` el corte se pega al keyframe: puede desviarse hasta 2 s. Por eso el margen. El corte
exacto se hace después, recodificando:

```bash
ffmpeg -ss 00:00:04.80 -to 00:01:03.20 -i tramos/12_costeo.mp4 \
  -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k cortos/12_costeo_fino.mp4
```

---

## 7. Arreglar lo que el directo trae mal

El material de directo llega con cuatro defectos típicos. Todos tienen arreglo parcial:

### Audio con eco de sala y nivel irregular

```bash
ffmpeg -i corto.mp4 -af "\
highpass=f=90,\
afftdn=nr=14:nf=-26,\
equalizer=f=250:t=q:w=1.6:g=-3,\
equalizer=f=3400:t=q:w=1.2:g=3,\
acompressor=threshold=-20dB:ratio=4:attack=5:release=200:makeup=4,\
loudnorm=I=-14:TP=-1.5:LRA=7" \
-c:v copy corto_audio_ok.mp4
```

El `-3 dB en 250 Hz` es lo que quita la mayor parte de la sensación de "cuarto vacío".

### Imagen oscura y con ruido (luz que se fue)

```bash
ffmpeg -i corto.mp4 -vf "hqdn3d=3:2:4:4,curves=all='0/0.02 0.2/0.28 0.6/0.68 1/1',\
eq=saturation=1.08:contrast=1.06,unsharp=5:5:0.6" -c:a copy corto_color_ok.mp4
```

Levantar sombras sube el ruido; por eso el `hqdn3d` va **antes** de la curva, no después.

### Balance de blancos que cambió a mitad de directo

Se corrige por tramos, no de una. Cada tramo con su ajuste → `62-emparejar-planos.md`.

### Encuadre malo (la persona en una esquina)

```bash
# Reencuadre a vertical tomando la zona donde de verdad está la persona
ffmpeg -i corto.mp4 -vf "crop=608:1080:820:0,scale=1080:1920,unsharp=5:5:0.4" \
  -c:a copy corto_vertical.mp4
```

Si el sujeto se mueve mucho, se corta el tramo en 2–3 partes y cada una con su `x`.

---

## 8. Convertir un tramo de directo en un corto que funcione

El material de directo tiene un problema estructural: **empieza en el medio de una conversación**. Nunca
lo publiques tal cual.

### Lo que hay que agregar siempre

| Elemento | Por qué |
|---|---|
| **Contexto en texto**, 2 s al inicio | "Alguien preguntó cuánto cuesta un plato" |
| **Recorte del arranque** hasta la primera palabra fuerte | El directo arranca lento siempre |
| **Subtítulos quemados** | Obligatorio; el audio de directo es peor |
| **Punch-ins** cada 5–8 s | El encuadre de directo es fijo y muerto |
| **Cierre fabricado** | El directo no cierra ideas; hay que cortarlo donde cierre |

### La reconstrucción del gancho

Casi siempre la mejor frase del tramo está en el segundo 40, no en el 0. Se saca y se pone de arranque:

```bash
# La frase fuerte (40,2 s → 43,1 s) va primero, después el resto desde el segundo 0
ffmpeg -ss 40.2 -to 43.1 -i tramo.mp4 -c:v libx264 -crf 18 -c:a aac gancho.mp4
ffmpeg -ss 0 -to 40.2 -i tramo.mp4 -c:v libx264 -crf 18 -c:a aac cuerpo.mp4
printf "file 'gancho.mp4'\nfile 'cuerpo.mp4'\n" > l.txt
ffmpeg -f concat -safe 0 -i l.txt -c copy corto_reordenado.mp4
```

⚠️ Cuidado con el sentido: si la frase fuerte respondía a algo, reordenarla puede cambiar lo que dijiste.
Ver `197-etica-del-montaje.md`.

---

## 9. Publicar la grabación completa

Si vas a dejar el directo completo publicado:

1. **Corta la sala de espera y el arranque muerto.** Nadie ve 5 minutos de pantalla estática.
2. **Corta las caídas técnicas.**
3. **Ponle capítulos.** Un directo de 2 h sin capítulos es un archivo, no un video.
4. **Cambia la miniatura.** La que genera la plataforma es siempre la peor. → `94-miniatura-y-portada.md`
5. **Cambia el título.** "Directo 14 de agosto" no lo busca nadie.
6. **Normaliza el audio.** El directo suele venir bajo.

```bash
# Recorte de arranque + normalización + faststart, en un paso
ffmpeg -ss 00:06:12 -i directo.mkv -af "loudnorm=I=-14:TP=-1.5:LRA=9" \
  -c:v libx264 -crf 20 -preset fast -pix_fmt yuv420p -c:a aac -b:a 192k \
  -movflags +faststart directo_publicable.mp4
```

---

## 10. El sistema por episodio

Un directo semanal produce, si hay sistema:

```
1  grabación completa publicada (con capítulos y miniatura nueva)
6–12  cortos verticales
1  resumen de 3–5 min con lo mejor
2–4  citas en imagen fija (texto sobre fotograma) para feed
1  audio para podcast, si el contenido lo permite
```

**Eso se decide antes de emitir, no después.** Si sabes que vas a sacar 10 cortos, estructuras el directo
en 10 bloques con inicio y final claros. El editor que trabaja así hace en 3 horas lo que otro hace en 12.

---

## Errores comunes

1. **No grabar en local.** Editar sobre la grabación descargada de la plataforma es trabajar con material
   degradado y con caídas.
2. **Grabar en mp4 en vez de mkv.** Si se corta la luz o se cae OBS, el mp4 queda ilegible.
3. **Keyframe distinto de 2 s.** Video a bloques y degradado por la plataforma.
4. **Bitrate mayor a la mitad de tu subida real.** Caídas cada pocos minutos.
5. **Encuadrar justo, sin aire.** Imposibilita el reencuadre vertical de los cortos.
6. **No repetir las preguntas del chat.** Cada respuesta queda inservible como pieza suelta.
7. **Directo sin bloques.** Dos horas continuas de las que no se puede cortar nada limpio.
8. **No hacer reinicios de contexto** cada 10 minutos. La mayoría de la audiencia entró después.
9. **Publicar el tramo de directo tal cual.** Empieza en el medio, arranca lento, no tiene gancho.
10. **No quitar el arranque muerto** de la grabación completa.
11. **Dejar la miniatura y el título automáticos.** Es un video que nadie va a encontrar.
12. **Levantar sombras antes de reducir ruido.** Amplificas la basura.
13. **Corte con `-c copy` sin margen.** El keyframe te come el principio de la frase.
14. **Audio de directo publicado sin procesar.** El eco de sala se arregla con 3 dB en 250 Hz y cuesta
    treinta segundos.

---

## Checklist

### Antes de emitir
- [ ] Velocidad de subida real medida a la hora del directo; bitrate ≤ la mitad
- [ ] Keyframe configurado a 2 s
- [ ] Grabación local activa, en mkv, calidad alta e independiente del bitrate del stream
- [ ] Pistas de audio separadas si hay varias fuentes
- [ ] Techo de audio a -3 dBFS; monitoreo con audífonos
- [ ] Encuadre con aire arriba y a los lados para permitir reencuadre vertical
- [ ] Luz constante que aguante toda la duración
- [ ] Estructura en bloques de 8–12 min, cada uno con cierre explícito
- [ ] Plan de cuántos cortos se van a sacar, decidido antes

### Después
- [ ] Grabación local remuxeada a mp4 y verificada (duración, audio, sin congelados)
- [ ] Transcripción con timecodes generada
- [ ] Momentos marcados cruzando transcripción + curva de audio + chat
- [ ] Tramos extraídos con margen y después cortados fino recodificando
- [ ] Audio de cada corto procesado (eco, nivel, presencia) a -14 LUFS
- [ ] Imagen corregida: ruido antes de levantar sombras
- [ ] Cada corto tiene gancho reconstruido, contexto en texto, subtítulos quemados y punch-ins
- [ ] Ningún corto necesita el directo para entenderse
- [ ] Grabación completa: arranque muerto cortado, capítulos, miniatura y título nuevos
- [ ] Pasó `98-verificacion-del-corte.md`
