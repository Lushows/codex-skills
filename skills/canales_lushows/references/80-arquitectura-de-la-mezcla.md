# 80 · Arquitectura de la mezcla

**Qué resuelve:** dónde va cada sonido y a qué nivel, para que el episodio suene a
producción y no a voz pegada sobre un archivo. Sin esta estructura, subir volúmenes a
ojo produce exactamente lo contrario de lo que se busca.

---

## Las cuatro capas

Toda la banda sonora del canal cabe en cuatro capas. No hay una quinta.

| # | Capa | Qué es | Continuidad | Nivel relativo a la voz |
|---|---|---|---|---|
| 1 | **Voz** | La locución. Manda siempre | Continua | **0 LU** (referencia) |
| 2 | **Colchón** | Room tone + drones graves + latido | **Nunca se apaga** | **−12 a −15 LU** |
| 3 | **Objetos** | Lo que suena en pantalla (`83`) | Puntual | −8 a −14 LU en su pico |
| 4 | **Picos** | Riser, impacto, revelación (`84`) | 3-6 por episodio | −3 a −6 LU en su cresta |

Los niveles son **relativos**, no absolutos. El `loudnorm` final sube o baja todo el
conjunto; lo que decide si la mezcla suena bien es la DISTANCIA entre capas.

Anclas medidas en `episodio01` (`86`): el stem de voz procesado da **−24,8 LUFS** y cada
pieza de colchón se calibra a **−41,0 LUFS**. Con 3-4 sonando a la vez, la suma queda en
−36/−35 LUFS — unos **11-12 LU bajo la voz en las pausas**, y **15-16 LU mientras habla**
porque el ducking la agacha (`85`). Ese vaivén ES el rango de la tabla.

## El hallazgo que ordenó todo: el colchón estaba 24 LU abajo

Los "cortes" que se oían en el piloto **no eran clics de los efectos**. Eran las pausas
del guion sin nada debajo. El colchón medía **24 LU por debajo de la voz** en vez de
12-15: durante la locución no se notaba, pero en cada respiración el nivel se caía al
suelo y el oído leía un salto.

Al subir el colchón al rango correcto, los saltos de nivel pasaron de **18 a 6** en el
mismo episodio, sin tocar ni un efecto. Es el arreglo de audio más rentable que tiene
este canal. (Cómo se cuentan bien esos saltos: `86` — sobre el corto plazo, no sobre el
momentáneo.)

> **Regla:** el colchón existe para que el silencio nunca sea silencio digital.
> Si al quitar la voz queda vacío, la mezcla está mal.

## El orden de la cadena (no es negociable)

```
1. VOZ        aformat → highpass 85 → acompressor → volume → asplit
2. PIEZAS     aformat → volume (calibrada, § 89) → atrim → asetpts
                      → afade in/out → adelay
3. SUMA       amix normalize=0 → [bed]
4. DUCKING    [bed][copia-de-voz] sidechaincompress → [bedd]   (§ 85)
5. MAESTRO    [voz][bedd] amix → acompressor → loudnorm
```

Cada paso depende del anterior. El error clásico es meter el `loudnorm` antes del
ducking: el compresor de sidechain trabaja entonces sobre un material ya nivelado y
deja de agacharse cuando hace falta.

## El esqueleto real

```python
filtros = [
    # 1 · VOZ — asplit porque una salida de filtro NO se puede usar dos veces
    "[1:a]aformat=channel_layouts=stereo,highpass=f=85,"
    "acompressor=threshold=0.06:ratio=3.2:attack=8:release=180,"
    "volume=1.85,asplit=2[voz][vozsc]",
]
etiquetas = []
for n, (arch, ini, dur, gan, bucle) in enumerate(PISTAS, start=2):
    # 2 · cada pieza, con rampa de entrada y salida — nunca un interruptor
    filtros.append(
        f"[{n}:a]aformat=channel_layouts=stereo,volume={gan},"
        f"atrim=0:{dur:.2f},asetpts=PTS-STARTPTS,"
        f"afade=t=in:st=0:d=0.25,afade=t=out:st={max(0.1, dur-0.4):.2f}:d=0.4,"
        f"adelay={int(ini*1000)}|{int(ini*1000)}[s{n}]")
    etiquetas.append(f"[s{n}]")

# 3 · SUMA — normalize=0 o cada efecto nuevo baja todo lo demás
filtros.append("".join(etiquetas) +
    f"amix=inputs={len(etiquetas)}:normalize=0:duration=longest,"
    "aformat=channel_layouts=stereo[bed]")

# 4 · DUCKING
filtros.append("[bed][vozsc]sidechaincompress=threshold=0.055:ratio=2.8:"
               "attack=60:release=750[bedd]")

# 5 · MAESTRO
filtros.append("[voz][bedd]amix=inputs=2:normalize=0:duration=first,"
               "acompressor=threshold=0.12:ratio=2.4:attack=25:release=420:makeup=1.15,"
               "loudnorm=I=-14:TP=-1.5:LRA=7[out]")
```

## `normalize=0` — la trampa de `amix`

Por defecto `amix` divide la salida entre el número de entradas. Con 5 pistas cada una
suena al 20%; al añadir la sexta, **todo lo que ya estaba baja otro escalón**. El
síntoma es "cuantos más efectos meto, más flojo suena todo".

```
amix=inputs=7:normalize=0:duration=first
```

Con `normalize=0` la suma es aritmética y el nivel de cada pieza lo decide su `volume`
calibrado (`89`). El limitador de cola (`alimiter`, y después el `loudnorm`) se encarga
del techo.

## El destino: −14 LUFS / −1,5 dBFS

```
loudnorm=I=-14:TP=-1.5:LRA=7
```

- **I=-14 LUFS** integrados: es lo que normaliza YouTube. Entregar más alto solo
  consigue que la plataforma lo baje y se pierda el margen dinámico.
- **TP=-1,5 dBFS** de pico real: deja aire para el codificador AAC, que puede
  sobrepasar el pico de la muestra al reconstruir la onda.
- **LRA=7 LU** de recorrido: suficiente para que el impacto pese, poco para que nadie
  tenga que tocar el volumen del móvil.

Verificación obligatoria antes de publicar: `86`.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Colchón 20-24 LU bajo la voz | Las pausas suenan a corte; saltos de nivel en cada respiración |
| `amix` sin `normalize=0` | Cada efecto añadido apaga toda la mezcla |
| `loudnorm` antes del ducking | El sidechain trabaja sobre material ya nivelado y no reacciona |
| Reutilizar `[voz]` en el sidechain | ffmpeg falla: una salida se consume una sola vez → hace falta `asplit` |
| Poner ganancias a ojo | 44 saltos audibles en el piloto; hay que MEDIR cada pieza (`89`) |
| Objetos por encima de la voz | El espectador oye la contadora y pierde la frase |
| Colchón que se apaga entre escenas | El vacío se lee como fallo técnico, no como intención |

## Relacionado

`84` picos · `85` ducking · `86` medir · `87` voz · `89` biblioteca
