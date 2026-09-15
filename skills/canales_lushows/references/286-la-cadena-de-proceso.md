# 286 · La cadena de proceso

**Qué resuelve:** qué se le hace a la voz, en qué orden, y **por qué en ese orden**. Hay
dos cadenas y se confunden constantemente: una vive en `voz.py` y fabrica el archivo
`locucion.mp3` que se aprueba en la fase 3; la otra vive en `acabar.py` y monta esa voz
dentro de la mezcla del episodio. Tocar una pensando que es la otra es el fallo típico.

> La teoría genérica del oficio —qué hace un compresor, qué es LUFS, cómo se ecualiza una
> voz— está en `editpro:70`, `editpro:72` y `editpro:73`. Aquí va **la cadena de este
> canal**, con lo que mide cada eslabón sobre el material real.

---

## Cadena 1 · Generación (`voz.py`, fase 3)

```
highpass=f=80,
equalizer=f=240:width_type=q:w=1.0:g=2.5,     ← cuerpo
equalizer=f=3200:width_type=q:w=1.2:g=3.0,    ← presencia
equalizer=f=7000:width_type=q:w=1.5:g=-2.0,   ← sibilancia
acompressor=threshold=0.10:ratio=3.5:attack=6:release=160:makeup=1.6,
aexciter=level_in=1:level_out=1:amount=1.2:drive=6:blend=0.3:freq=7500,
aecho=0.85:0.55:22:0.16,                      ← micro-sala de 22 ms
alimiter=limit=0.95
```

| Eslabón | Por qué **en este canal** |
|---|---|
| `highpass=80` | El TTS trae basura por debajo de 80 Hz que ensucia el grave del colchón |
| `+2,5 dB @ 240 Hz` | La voz sintética es delgada de pecho |
| `+3,0 dB @ 3,2 kHz` | La banda de la inteligibilidad. Sin esto hay que agachar el fondo el doble |
| `−2,0 dB @ 7 kHz` | Sin esto, cada «s» pica |
| `acompressor` | El sidechain de la mezcla (§ `85`) necesita una señal predecible |
| `aexciter` | Armónicos altos: es lo que hace que no suene a robot |
| `aecho 22 ms` | Una sala pequeña. Sin él la voz flota por encima de la mezcla |
| `alimiter 0,95` | Techo antes de entregar |

🔴 **Esta cadena deja la voz muy baja y hay que saberlo:** el crudo está en −19,4 LUFS y
`locucion.mp3` sale en **−27,1 LUFS con pico real −9,5 dBTP**. Son 7,7 LU de caída, y
están medidos: la misma cadena **sin** el `aecho` entrega −20,2 LUFS y −1,52 dBTP, o sea
que **6,6 de esos 7,7 LU los pone el `out_gain=0.55` del eco**. No es un defecto: es la
razón de que en la mezcla
haya un `volume=1.85`. Quien quite el eco sin tocar ese `1.85` se encuentra la voz 5 dB
por encima de donde estaba calibrado todo lo demás.

## Cadena 2 · Mezcla (`acabar.py`, fase 7)

```
[1:a] aformat=channel_layouts=stereo,
      highpass=f=85,
      acompressor=threshold=0.06:ratio=3.2:attack=8:release=180,
      volume=1.85,
      volume='<curva de relieve>':eval=frame,
      asplit=2 [voz][vozsc]

[bed][vozsc] sidechaincompress=threshold=0.055:ratio=2.8:attack=60:release=750 [bedd]

[voz][bedd]  amix=inputs=2:normalize=0:duration=first,
             acompressor=threshold=0.12:ratio=1.8:attack=25:release=420:makeup=1.10,
             loudnorm=I=-14:TP=-1.5:LRA=9 [out]
```

Medido paso a paso sobre `ep01-lustig`:

| Paso | LUFS | dBTP | LRA |
|---|---|---|---|
| 0 · crudo de `edge-tts` | −19,36 | −1,52 | 3,20 |
| 1 · tras la cadena de `voz.py` | **−27,08** | **−9,50** | 2,80 |
| 2 · `+highpass=85` | −27,21 | −12,27 | 2,90 |
| 3 · `+acompressor` | −28,64 | −13,21 | 2,70 |
| 4 · `+volume=1.85` | −23,30 | −7,97 | 2,70 |
| 5 · `+curva de relieve` | −22,70 | −7,16 | **5,10** |
| **Máster del minuto** | **−14,52** | **−1,49** | 3,80 |

El objetivo declarado era −14 LUFS / −1,5 dBTP. Lo entregado: **−14,5 y −1,49**. La
diferencia de 0,5 LU es normal: `loudnorm` en una pasada estima, no mide (§ `86`).

## Por qué ese orden y no otro

| Decisión | Qué pasa si se cambia |
|---|---|
| `highpass` **antes** del compresor | Si va después, el retumbe dispara el compresor y la voz bombea sin motivo. Además baja el pico real 2,8 dB gratis (−9,50 → −12,27) |
| Compresor **antes** de la curva de relieve | Al revés, el compresor se come 1,1 LU del relieve construido: LRA 5,1 → 4,0 (§ `285`) |
| `volume` fijo **antes** de la curva | La curva es relativa (base 1). Si multiplica antes del `1.85` da lo mismo, pero leerlo cuesta más |
| `asplit` **después** de todo el proceso de voz | La llave del sidechain tiene que ser la voz **tal como se va a oír**, con su relieve. Si se saca antes, el colchón no se agacha en los bloques que subiste |
| `sidechaincompress` sobre el colchón, **no** sobre la voz | Es lo que significa ducking: manda la voz (§ `85`) |
| `loudnorm` **el último**, después del pegamento | Si va antes del `acompressor` final, la suma de voz + colchón vuelve a sacar el máster de sitio |

🔴 **La trampa del `asplit`.** Una salida de un filtro en `filter_complex` se consume una
sola vez. La voz se necesita dos veces —para la mezcla y como llave del sidechain— y por
eso hay un `asplit=2`. Sin él, ffmpeg falla con un error sobre etiquetas que no menciona
en ningún momento que el problema sea el reuso (§ `85`).

## Comprobar la cadena sin renderizar el vídeo

```bash
# el stem de voz tal como entra a la mezcla, con su relieve
ffmpeg -i locucion.mp3 -af "aformat=channel_layouts=stereo,highpass=f=85,\
acompressor=threshold=0.06:ratio=3.2:attack=8:release=180,volume=1.85" -y _voz.wav

# y su medida
ffmpeg -nostats -i _voz.wav -af loudnorm=I=-14:TP=-1.5:LRA=9:print_format=json -f null -
```

Toma 3 segundos y responde la única pregunta que importa antes de gastar un render: **¿la
voz entra al nivel para el que está calibrado el colchón?** La referencia del canal es el
stem de voz alrededor de −23 LUFS y el colchón 14 LU por debajo (§ `80`, § `86`).

## Lo que NO se toca

| Tentación | Por qué no |
|---|---|
| Añadir reducción de ruido | No hay ruido: es una señal sintética. Sólo puede quitar armónicos |
| Añadir una puerta de ruido | Los silencios ya son silencio digital. La puerta recorta los finales de palabra |
| Subir el `makeup` del compresor final | Ese eslabón es pegamento, no nivel. El nivel lo pone `loudnorm` |
| Cambiar `loudnorm` a `I=-16` «por YouTube» | YouTube normaliza a la baja, no a la alta: −14 está bien (§ `editpro:73`) |
| Retocar la cadena de `voz.py` con el episodio montado | Cambia el nivel de referencia de toda la mezcla |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Confundir la cadena de `voz.py` con la de `acabar.py` | Se toca el archivo aprobado y se descalibran las dos |
| Quitar el `aecho` sin tocar el `volume=1.85` | La voz sube 5 dB sobre todo lo calibrado |
| Sacar la llave del sidechain antes de la curva de relieve | El colchón no se agacha donde la voz sube |
| Olvidar el `asplit` | Error de ffmpeg sobre etiquetas que no dice cuál es el problema |
| Poner `loudnorm` antes del último compresor | El máster se va de −14 |
| Meter puerta de ruido o reducción de ruido | Se comen los finales de palabra sin quitar nada |
| Dar por bueno el máster sin medirlo | −14,5 se consigue midiendo, no confiando |

## Relacionado

`285` el relieve se construye · `85` ducking y espacio · `86` medir el audio ·
`80` arquitectura de la mezcla · `87` voz a fondo · `editpro:70` cadena de voz
profesional · `editpro:72` ecualización de voz · `editpro:73` compresión y loudness
