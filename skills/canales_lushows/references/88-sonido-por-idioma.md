# 88 · Sonido por idioma

**Qué resuelve:** el episodio sale en seis idiomas con **una sola mezcla**. Para un canal
normal esto exige seis locutores y seis montajes; aquí la voz se genera, así que la
duración se puede forzar y el resto de la banda no se toca.

---

## El requisito duro de YouTube

Las pistas de audio multi-idioma deben durar **lo mismo que el vídeo**. La plataforma
rechaza cualquiera que se pase de **1 segundo** de diferencia. Todo el método existe
para cumplir ese número.

Margen de trabajo del canal: **0,9 s**, para no jugar en el límite.

## Las seis voces

| Idioma | Voz | `rate` base | Expansión típica vs. español |
|---|---|---|---|
| Español (canal) | `es-MX-JorgeNeural` | `+8%` | — (referencia) |
| Inglés | `en-US-GuyNeural` | `+0%` | −5 a −10% (más corto) |
| Alemán | `de-DE-ConradNeural` | `+2%` | **+15 a +20%** |
| Francés | `fr-FR-HenriNeural` | `+2%` | +8 a +12% |
| Portugués | `pt-BR-AntonioNeural` | `+3%` | +2 a +5% |
| Japonés | `ja-JP-KeitaNeural` | `+0%` | **+15 a +25%** |

El `rate` base compensa que unos idiomas se hablan más rápido que otros de forma
natural. **Alemán y japonés son los que rompen el presupuesto**: si un bloque no cabe,
casi siempre es uno de esos dos.

## El método: generar, medir, ajustar, rellenar

1. Generar cada bloque con el `rate` base del idioma, **en una sola pasada** (`87`).
2. **Medir.** Comparar con el hueco que le toca en el montaje.
3. Corregir con `atempo`, que cambia la velocidad **sin cambiar el tono**.
4. Rellenar con silencio hasta clavar el total.

```python
LIMITE = (0.85, 1.15)      # fuera de aquí se oye

factor = dur(crudo) / objetivo if objetivo > 0 else 1.0
aviso = ""
if factor > LIMITE[1]:
    aviso = f"⚠ {int((factor-1)*100)}% más largo — acortar el TEXTO en este idioma"
    factor = LIMITE[1]
elif factor < LIMITE[0]:
    factor = LIMITE[0]

if abs(factor - 1.0) > 0.005:
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", crudo,
                    "-filter:a", f"atempo={factor:.4f}", "-ar", "24000", "-ac", "1",
                    "-b:a", "160k", "-y", destino], check=True)
else:
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", crudo,
                    "-c", "copy", "-y", destino], check=True)
```

## La ventana de `atempo`

| Factor | Qué se oye |
|---|---|
| 0,85 - 0,95 | Nada; la voz suena un poco más asentada |
| **0,95 - 1,05** | Zona ideal |
| 1,05 - 1,15 | Nada, si la voz no era ya rápida |
| **> 1,15** | Se atropella: las cifras dejan de entenderse |
| **< 0,85** | Arrastra |

> **Pasado el 15%, la solución NO es comprimir más: es reescribir la frase más corta.**
> Es exactamente lo que hace el doblaje profesional de cine. `atempo` arregla desfases
> pequeños, no traducciones que no caben.

Por eso la traducción se pide **con presupuesto**: "esta frase tiene que caber en 4,2
segundos hablados", no "traduce esto".

## 🔴 Los efectos se anclan a la ESCENA, no a la palabra

Dentro de un idioma, un efecto se cuelga de la palabra que lo nombra (`83`). En
multi-idioma eso se rompe: la palabra "millones" cae en el segundo 11,2 en español y en
el 12,8 en alemán, y el efecto se desincroniza en cinco de las seis pistas.

| Elemento | Se ancla a | Motivo |
|---|---|---|
| Colchón, música, ambientes | **Escena** | Son los mismos en las seis pistas |
| Picos dramáticos | **Escena** (o al fotograma de la cifra) | La imagen no se mueve |
| Objetos diegéticos | **Escena** | Lo que suena en pantalla está en pantalla, no en la frase |
| Ducking | La voz de cada pista | Es lo único que sí cambia |

Consecuencia de método: **la banda sin voz se renderiza UNA vez** y se reutiliza.

## Una mezcla, seis pistas

```python
# 1 · la cama (colchón + objetos + picos) se renderiza una sola vez, sin voz
#     → salida/cama.wav

# 2 · por idioma, solo se cambia la voz sobre la MISMA cama
FC = ("[1:a]aformat=channel_layouts=stereo,highpass=f=85,"
      "acompressor=threshold=0.06:ratio=3.2:attack=8:release=180,"
      "volume=1.85,asplit=2[voz][vozsc];"
      "[0:a][vozsc]sidechaincompress=threshold=0.055:ratio=2.8:"
      "attack=60:release=750[camad];"
      "[voz][camad]amix=inputs=2:normalize=0:duration=first,"
      "acompressor=threshold=0.12:ratio=2.4:attack=25:release=420:makeup=1.15,"
      "loudnorm=I=-14:TP=-1.5:LRA=7[out]")

cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error",
       "-i", "salida/cama.wav", "-i", f"salida/voz_{cod}.mp3",
       "-filter_complex", FC, "-map", "[out]",
       "-t", f"{T:.2f}", "-c:a", "aac", "-b:a", "192k",
       "-y", f"salida/pistas/{cod}.m4a"]
```

El `loudnorm` se aplica **por pista**, no una vez: cada idioma tiene su propia densidad
y hay que garantizar los −14 LUFS en las seis.

## La comprobación antes de subir

```python
for cod in IDIOMAS:                       # tolerancia 0,9 s, no 1,0
    dif = dur("salida/episodio01.mp4") - dur(f"salida/pistas/{cod}.m4a")
    print(f"  {cod}  {'OK' if abs(dif) <= 0.9 else 'RECHAZO'}  {dif:+.3f} s")
```

Ninguna pista se sube sin pasar esto **y** la auditoría de `86`.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Anclar efectos a palabras en multi-idioma | Cinco de las seis pistas quedan desincronizadas |
| Rehacer la mezcla por idioma | Seis mezclas distintas que no suenan al mismo canal |
| `atempo` por encima de 1,15 | La voz se atropella y las cifras se pierden |
| Traducir sin presupuesto de duración | Alemán y japonés se salen del hueco siempre |
| Un solo `loudnorm` para las seis | Pistas a niveles distintos; el oyente cambia el volumen |
| Apurar el límite de 1 s | Un redondeo y YouTube rechaza la pista |

## Relacionado

`83` diegético · `85` ducking · `86` medir · `87` voz
