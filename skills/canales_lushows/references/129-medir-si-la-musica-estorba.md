# 129 · Medir si la música estorba

**Qué resuelve:** la discusión de "yo la oigo bien". La única forma de saber si la música
se está comiendo la voz es separar los dos stems, medirlos y comparar. Se hace en un
minuto y da un número, no una opinión.

---

## 🔴 El caso real: el colchón a 24 LU

Los "cortes" del piloto no eran clics de los efectos: eran **las pausas del guion sin nada
debajo**. El colchón medía **24 LU por debajo de la voz** en vez de 12-15. Mientras se
hablaba no se notaba; en cada respiración el nivel se caía al suelo y el oído leía un
salto. Subirlo al rango correcto bajó los saltos de nivel de **18 a 6** sin tocar un efecto.

De ahí la regla: **12-15 LU, nunca 24**. Y el corolario que casi nadie aplica: se mide el
**colchón entero**, no la música sola.

## Los stems se renderizan aparte, con la misma cadena

No vale medir la mezcla terminada: ahí ya están sumados. Cada capa se saca con los mismos
filtros que lleva en la mezcla, menos el maestro — y el **colchón sin ducking**, que es
como está en las pausas, donde vive el problema.

```bash
# stem de VOZ — la cadena de acabar.py sin loudnorm ni amix final
ffmpeg -hide_banner -i locucion.mp3 -af "aformat=channel_layouts=stereo,highpass=f=85,\
acompressor=threshold=0.06:ratio=3.2:attack=8:release=180,volume=1.85" -t 63.45 -y stem_voz.wav
# stem de COLCHÓN — música con su curva (120) + room tone, sin voz y sin ducking
```

La función `medir()` que lee `I`, `LRA` y `TP` de `ebur128` está completa en `86`.

## Lectura real del episodio 01

```
  voz                  I=-23.3 LUFS  LRA=3.0  TP=-8.0
  musica sola          I=-42.8 LUFS  LRA=5.2  TP=-28.9
  colchon (mus+room)   I=-38.9 LUFS  LRA=1.8  TP=-26.4

  voz - musica  = 19.5 LU
  voz - colchon = 15.6 LU   (objetivo 12-15)   ← 0,6 LU fuera de rango

  por bloque:  muerte 16.4 · oficio 15.2 · nombre 16.8 · torre 15.4 · metodo 14.7
```

Diagnóstico: no estorba, **falta**. Arreglo verificado midiendo otra vez — el bloque
entero **+1,6 dB** (base `0.34 → 0.409`, room tone `2.40 → 2.885`):

```
  voz - colchon = 14.0 LU   ✅
  por bloque:  muerte 14.8 · oficio 13.6 · nombre 15.2 · torre 13.8 · metodo 13.1
```

Los cinco bloques dentro de la banda, sin tocar la forma de la curva de intensidad.

## La prueba que casi nadie hace: la banda de la voz

Dos mezclas con la misma distancia total suenan distinto: lo que tapa la voz no es el
nivel general, es la energía **en 300-3500 Hz**, donde viven las consonantes.

```bash
# distancia total, y distancia SOLO en la banda de la voz (1,4 kHz, 3,5 octavas)
for S in stem_voz stem_colchon; do
  ffmpeg -hide_banner -i $S.wav -af "astats=metadata=1:reset=0" \
    -f null - 2>&1 | grep -m1 "RMS level dB"
  ffmpeg -hide_banner -i $S.wav -af "bandpass=f=1400:width_type=o:w=3.5,\
astats=metadata=1:reset=0" -f null - 2>&1 | grep -m1 "RMS level dB"
done
```

Medido en el episodio 01:

| Stem | Total | Banda 300-3500 |
|---|---|---|
| voz | −27,10 dB | −32,32 dB |
| colchón | −39,57 dB | −43,91 dB |
| **distancia** | **12,5 dB** | **11,6 dB** 🔴 |

**El criterio:** si la distancia en la banda de la voz es MENOR que la total, el colchón
está más presente donde vive la voz. Aquí lo está por 0,9 dB: poco, pero mal.

El arreglo no es bajar la música (perdería peso), es abrirle un hueco:

```
equalizer=f=1800:t=q:w=1.1:g=-3      # el hueco para las consonantes
```

Verificado: la banda cae de −43,91 a **−44,85 dB** (distancia 12,5 dB, ya igualada)
mientras el nivel total solo baja **0,37 dB**. La música conserva su peso y deja de competir.

## El espectrograma: para ver lo que el número no dice

```bash
ffmpeg -hide_banner -i stem_colchon.wav \
  -lavfi "showspectrumpic=s=1200x480:mode=combined:legend=1:scale=log:color=intensity" \
  -frames:v 1 -y esp_colchon.png
```

Qué se busca en la imagen:

- **Franja continua y brillante entre 300 Hz y 3,5 kHz** en el colchón: la música metida
  en el sitio de la voz. Ahí debe verse oscuro, y brillante abajo.
- **Columnas verticales** sin golpe previsto que las explique: son clics (`124`).
- **Corte negro vertical** en todas las frecuencias: el colchón se apagó — es lo que el
  espectador oye como "se cortó el vídeo".

## La rutina, antes de publicar

```
1. Renderizar stem de voz y stem de colchón por separado
2. ebur128 a los dos          → voz − colchón entre 12 y 15 LU
3. La misma resta por bloque  → ninguno fuera de 12-16 LU
4. Banda 300-3500 de los dos  → distancia en banda ≥ distancia total
5. Serie S de la mezcla       → recorrido ≤ 8 LU, cero saltos ≥ 6 LU (`86`)
6. Espectrograma del colchón  → sin franja en la banda de voz, sin cortes verticales
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir la mezcla terminada en vez de los stems | Los niveles ya están sumados: no dice nada |
| Colchón a 24 LU | Cada pausa del guion suena a corte — el caso real del piloto |
| Ignorar la banda 300-3500 | La distancia total sale bien y aun así no se entienden las consonantes |

## Relacionado

`86` medir el audio · `120` la curva de intensidad · `85` ducking · `80` arquitectura ·
`162` leer un espectrograma
