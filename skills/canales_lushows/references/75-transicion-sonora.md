# 75 · La transición sonora

**Qué resuelve:** el sonido que cruza el corte. Es el J-cut aplicado al montaje visual:
**el efecto entra antes que la imagen**. Es lo que hace que un corte duro se lea como una
transición trabajada, y es el 70% del efecto con el 5% del trabajo.

---

## Por qué el sonido hace casi todo

El oído es anticipatorio: registra un cambio antes de saber qué lo produjo y prepara al
ojo. Por eso funciona esta asimetría:

| Combinación | Cómo se lee |
|---|---|
| Corte duro **+ efecto adelantado 4 fotogramas** | Transición intencionada y cara |
| Corte duro **sin efecto** | Corte (correcto, pero neutro) |
| Transición visual elaborada **sin efecto** | Fallo de reproducción o efecto de plantilla |
| Efecto **después** del corte | Error de sincronía: se percibe como desfase de audio |

Conclusión práctica: antes de construir un barrido (`71`) o un cruce por elemento (`73`),
probar el corte duro con el efecto adelantado. Muchas veces ya está resuelto.

## El adelanto exacto

| Tipo de sonido | Adelanto respecto al corte | Fotogramas a 25 fps |
|---|---|---|
| `tr_whoosh` (movimiento, barrido, elemento que cruza) | **−0,14 s** | 3,5 |
| `tr_flash` (destello) | **−0,08 s** | 2 |
| `ob_papel` (hoja, página, apilado) | **−0,12 s** | 3 |
| `tr_cierre` (fin de bloque) | **−0,20 s** | 5 |
| `dr_riser` (tensión que desemboca en el corte) | **−1,80 s** | 45 |
| **`dr_golpe` / `dr_impacto`** | **0,00 s — en el fotograma exacto** | 0 |
| Ambiente de la escena siguiente (`amb_*`) | **−0,60 a −1,20 s** | 15 a 30 |

Las dos excepciones a la regla del adelanto son los **impactos** —que tienen que caer
clavados, o el cerebro los lee como error— y los **ambientes**, que entran mucho antes
porque no llaman la atención: sólo preparan el lugar. Ese ambiente adelantado es el J-cut
de verdad: cuando la imagen llega, el espectador ya estaba en el juzgado.

## Cómo se escribe en `acabar.py`

El efecto se coloca con `adelay` (milisegundos) y su ganancia **se mide, no se estima**:

```
# corte en t = 52,00 s  ->  el whoosh arranca en 51,86 s = 51860 ms
[2:a]volume=0.62,adelay=51860:all=1[wh];
[3:a]volume=0.48,adelay=51880:all=1[pap];
[voz][wh][pap]amix=inputs=3:normalize=0:duration=first[mez]
```

`normalize=0` es obligatorio: sin él, `amix` divide el volumen por el número de entradas
y la voz se hunde cada vez que entra un efecto.

Para calcular esos `volume`, primero se mide cada pieza:

```bash
ffmpeg -i sonido/tr_whoosh.wav -af ebur128 -f null - 2>&1 | grep -E "I:"
ffmpeg -i audio/locucion.mp3   -af ebur128 -f null - 2>&1 | grep -E "I:"
```

Objetivo de niveles, con la voz en −14 LUFS integrados:

| Capa | Distancia bajo la voz |
|---|---|
| Efecto de transición (`tr_*`) | **6-8 LU** |
| Impacto dramático (`dr_golpe`) | **4-6 LU** |
| Ambiente (`amb_*`) | **12-15 LU** |

Ya pasó una vez: los WAV venían atenuados de fábrica y al aplicarles 0,3 "a ojo" se
volvieron inaudibles. **Medir siempre.**

## Cruzar los ambientes entre escenas

El ambiente no corta: se cruza. Si la escena A vive en `amb_oficina` y la B en
`amb_encierro`, el cruce dura **0,8-1,2 s** y empieza antes del corte visual:

```
[4:a]atrim=0:34.5,afade=t=out:st=33.6:d=0.9[amb_a];
[5:a]afade=t=in:st=0:d=0.9,adelay=33600:all=1[amb_b];
[amb_a][amb_b]amix=inputs=2:normalize=0[amb]
```

Se hace con `afade` + `adelay`, **no con `acrossfade`**: `acrossfade` acorta la suma de
los dos (`d1+d2−d`) y aquí la línea de tiempo está clavada a la voz (`79`).

## Dónde NO puede caer un efecto

Sobre una palabra. Si el corte cae en mitad de una frase, el efecto tapa una sílaba y
la voz pierde inteligibilidad, que es lo único que no se puede negociar. Dos salidas:

1. **Mover el corte** 3-6 fotogramas hasta la pausa más cercana (mirar `audio/tiempos.json`).
2. Si el corte no se puede mover, bajar el efecto **4 dB** y alargarle el ataque.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Poner el efecto justo en el corte | Se percibe tarde: el oído ya había registrado el cambio de imagen |
| Adelantar un impacto | Suena antes de ver el golpe: error de sincronía evidente |
| `amix` sin `normalize=0` | Cada efecto hunde la voz unos decibelios |
| Ganancias a ojo | O inaudible o tapando la voz; se mide con `ebur128` |
| Efecto de transición sobre una palabra | Se pierde la sílaba; el subtítulo la salva, el oyente no |
| Cortar el ambiente en seco en el corte visual | Delata que son dos vídeos pegados |
| El mismo `tr_whoosh` en las cinco uniones | El oído lo memoriza a la tercera (`78`) |

## Relacionado

`70` · `73` · `74` · `76` · `78` · `80` · `84` · `85` · `89`
