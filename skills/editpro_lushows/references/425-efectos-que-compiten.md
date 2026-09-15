# 425 — Efectos que compiten

Una cadena de filtros no es una lista de cosas que pasan. Es una secuencia donde cada eslabón recibe lo
que el anterior dejó. Dos efectos pueden **sumar**, pueden **anularse**, o —el caso caro— pueden pelear
por el mismo recurso y cobrarte los dos aunque solo llegue uno.

Este módulo es cómo se detecta esa pelea con números, y las tres formas que tiene.

---

## 1. Las tres relaciones, medidas

Todo está medido sobre el mismo clip de 4 s a 1080p25, `signalstats` promediado sobre los 100
fotogramas, y el peso a CRF 20 `preset veryfast`.

### a) Ortogonales: cada uno hace lo suyo

| Cadena | `utime` | YAVG | SATAVG | YDIF | MB |
|---|---|---|---|---|---|
| nada | 2,63 | 92,07 | 14,95 | 2,17 | 1,17 |
| `eq=contrast=1.25` | 2,80 | **81,62** | 14,95 | 2,79 | 1,50 |
| `eq=saturation=1.25` | 2,58 | 92,08 | **19,33** | 2,16 | 1,21 |
| `eq=contrast=1.25:saturation=1.25` | 2,94 | **81,62** | **19,33** | 2,80 | 1,53 |

Los dos valores de la cadena combinada son **exactamente** los de cada efecto por separado: 81,62 y
19,33, hasta el último decimal. Contraste y saturación en `eq` no se estorban.

> 🔴 **Esto corrige una creencia extendida.** «Subir el contraste sube la saturación» es cierto
> perceptualmente y cierto en herramientas que trabajan en RGB, pero **no en `eq` de ffmpeg**: `contrast`
> opera sobre el canal Y y deja U y V intactos. SATAVG no se mueve ni una milésima. Si en tu cadena la
> piel se te pone naranja al subir contraste, no es `eq`: es una LUT o una curva en RGB más adelante.

### b) Antagonistas: uno deshace al otro

| Cadena | `utime` | YDIF | MB |
|---|---|---|---|
| nada | 2,63 | **2,17** | 1,17 |
| `noise=alls=6:allf=t+u` | 2,88 | 2,38 | 2,02 |
| `hqdn3d=4:3:6:4` | 4,30 | — | 1,00 |
| `hqdn3d=4:3:6:4,noise=alls=6:allf=t+u` | **4,63** | **1,78** | 1,76 |

Lee la última fila despacio. Pusiste un denoise y luego un grano, pagaste **+2,00 s de CPU** y **+0,59 MB**
sobre el original… y la textura temporal que sale (**YDIF 1,78**) es **menor que la del material sin
tocar** (2,17). El denoise se llevó el grano natural de la fuente; el grano sintético no llegó a
reponerlo. Pagaste dos filtros para quedarte con menos textura de la que tenías gratis.

Es la pelea más frecuente y la más invisible, porque cada eslabón tiene su justificación por separado
(«limpio el ruido de archivo», «le pongo grano de película») y nadie mide el resultado conjunto.

### c) Competidores por bitrate: los dos llegan, pero se encarecen

| Cadena | `utime` | YDIF | MB | suma esperada |
|---|---|---|---|---|
| nada | 2,63 | 2,17 | 1,17 | — |
| `unsharp=5:5:0.8:5:5:0.0` | 7,00 | 3,08 | 2,06 | — |
| `noise=alls=6:allf=t+u` | 2,88 | 2,38 | 2,02 | — |
| `unsharp,noise` | **8,63** | 3,30 | **3,23** | 2,91 |

El YDIF sí es aditivo (0,91 + 0,21 = 1,12 sobre la base; medido, 1,13). El **peso no lo es**: la suma de
los excesos daría 2,91 MB y salen 3,23, un **11% de más**. Los dos efectos añaden alta frecuencia en la
misma banda; el codificador no puede compartir el trabajo y paga dos veces por información
prácticamente idéntica.

Y en la entrega, donde el bitrate tiene techo, eso significa que **ninguno de los dos llega entero**
(`428`).

---

## 2. El arnés: aditividad

La prueba es de tres líneas y es la que hay que correr sobre cualquier par sospechoso:

```bash
#!/usr/bin/env bash
# competir.sh <filtroA> <filtroB> — ¿suman, se anulan o se encarecen?
IN=base.mp4
mide () {
  ffmpeg -hide_banner -loglevel error -y -i $IN -vf "$1,format=yuv420p" \
    -c:v libx264 -crf 20 -preset veryfast -an tmp.mp4
  D=$(ffmpeg -hide_banner -i tmp.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" \
      -f null - 2>&1 | grep -o 'YDIF=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.2f",s/n}')
  M=$(awk -v s="$(stat -c%s tmp.mp4)" 'BEGIN{printf "%.2f",s/1048576}')
  echo "$D $M"
}
read D0 M0 <<< "$(mide null)"
read DA MA <<< "$(mide "$1")"
read DB MB <<< "$(mide "$2")"
read DC MC <<< "$(mide "$1,$2")"
awk -v d0=$D0 -v da=$DA -v db=$DB -v dc=$DC -v m0=$M0 -v ma=$MA -v mb=$MB -v mc=$MC 'BEGIN{
  printf "YDIF   esperado %.2f   medido %.2f   -> %s\n", d0+(da-d0)+(db-d0), dc, \
    (dc < d0 ? "ANTAGONISTAS: peor que sin nada" : (dc < d0+(da-d0)+(db-d0)-0.05 ? "se solapan" : "aditivos"))
  printf "PESO   esperado %.2f   medido %.2f   -> %+.0f%%\n", m0+(ma-m0)+(mb-m0), mc, \
    100*(mc-(m0+(ma-m0)+(mb-m0)))/(m0+(ma-m0)+(mb-m0))
}'
```

Tres lecturas posibles:

| Resultado | Significado | Qué hacer |
|---|---|---|
| medido ≈ esperado | ortogonales | déjalos |
| medido < sin efecto | **antagonistas** | quita uno. Casi siempre el primero |
| peso medido > esperado | compiten por bitrate | baja la dosis de uno, o quita el otro |

---

## 3. Los pares que hay que vigilar

| Par | Relación | Por qué |
|---|---|---|
| `hqdn3d` + `noise` | antagonistas | quitas textura y luego la pagas dos veces |
| `unsharp` + `noise` | competidores | misma banda de frecuencia, doble coste |
| `unsharp` + escalado | depende del orden | ver `426` |
| `vignette` + `eq=brightness` | se pisan en los bordes | la viñeta baja lo que el brillo subió |
| LUT + `eq=saturation` | se solapan | la LUT ya trae saturación dentro |
| `gblur` de fondo + viñeta | competidores de atención | los dos oscurecen la periferia |
| grano + trama/halftone | competidores | dos texturas finas peleando por el mismo bloque |
| destello + fundido | se anulan | el fundido come justo la campana del destello |
| `eq=contrast` + `eq=saturation` | **ortogonales** (medido) | `eq` trabaja en YUV |

---

## 4. La competencia que no es de píxeles: la atención

Hay una segunda capa, y no la mide ffmpeg. Dos efectos que técnicamente no se estorban **sí** compiten si
ocurren al mismo tiempo en el campo visual:

- Un destello y una entrada de texto en el mismo fotograma: el espectador no procesa los dos. Procesa
  uno y el otro se pierde.
- Un movimiento de fondo y un recorte que entra deslizando: se cancelan, y lo que queda es sensación de
  desorden.
- Una viñeta que dirige al centro y un elemento que entra por la esquina: la viñeta está trabajando en
  contra de tu propio montaje.

La regla operativa, que viene de `374` y de `439`: **un evento fuerte a la vez.** Si dos efectos caen en
el mismo fotograma, separa uno 3–5 fotogramas. Es gratis, y la diferencia es enorme.

Para detectarlo sin ojo, sirve la serie de `YAVG` por fotograma cruzada con la lista de eventos del guion
visual: si dos picos caen a menos de 0,15 s uno del otro, hay competencia.

---

## 5. La regla de la casa: un cambio por vez

Toda esta sección se resume en un procedimiento aburrido y muy eficaz:

1. Añade **un** efecto.
2. Mide (`420`).
3. Escribe el número en la ficha.
4. Solo entonces añade el siguiente, y mide **la cadena entera**, no el efecto suelto.

El paso 4 es el que casi nadie hace. Un efecto medido en aislamiento y luego montado dentro de una cadena
de seis puede estar haciendo algo completamente distinto: `426` trata exactamente ese caso.

---

## Errores frecuentes

- **Denoise seguido de grano.** Medido: YDIF 1,78 frente a 2,17 sin tocar nada. Pagas dos filtros para
  tener menos textura.
- **Creer que el contraste sube la saturación en `eq`.** Medido: SATAVG idéntico hasta la milésima.
  Si se te va la piel, el culpable es una LUT o una curva RGB.
- **Sumar `unsharp` y grano «para textura».** Compiten por la misma banda y el peso sale un 11% por
  encima de la suma.
- **Poner una LUT y después `eq=saturation`.** La LUT ya lo trae dentro; mide antes de añadir.
- **Medir cada efecto por separado y no la cadena.** El aporte depende del contexto.
- **Añadir dos efectos en la misma iteración.** Si el resultado cambia, no sabes cuál fue.
- **Un destello y una entrada de texto en el mismo fotograma.** Solo se procesa uno.
- **Viñeta más `gblur` de fondo.** Los dos oscurecen la periferia: elige.
- **Asumir que el peso es aditivo.** Casi nunca lo es, y la diferencia sale del bitrate del resto.
- **No repetir la medición al quitar un eslabón.** Los demás cambian de contexto (`426`).

---

## Checklist

- [ ] Cada efecto entró en la cadena de uno en uno, con su medida.
- [ ] Después de cada añadido medí la **cadena entera**, no solo el efecto nuevo.
- [ ] Corrí la prueba de aditividad sobre los pares sospechosos.
- [ ] Ningún par deja el YDIF por debajo del material sin tocar.
- [ ] El peso de la cadena está cerca de la suma de los pesos; si no, sé por qué.
- [ ] Si hay denoise y grano en la misma cadena, puedo justificar por qué.
- [ ] Si hay LUT, no hay un `eq` detrás haciendo lo mismo.
- [ ] Dos eventos fuertes no caen en el mismo fotograma.
- [ ] La ficha de cada efecto dice con qué otros compite.

---

## Relacionado

- `420`, `421` — el arnés y las magnitudes por familia
- `422` — el coste que se paga aunque el efecto se anule
- `423` — el eslabón que no aporta porque otro ya lo hace
- `426` — orden de aplicación: el mismo par, distinto resultado
- `428` — por qué la competencia por bitrate se decide en la entrega
- `440`, `446` — grano, denoise y ruido que sobrevive
- `66` — la dosis artesanal de nitidez, viñeta y grano
- `65` — LUTs: lo que ya traen dentro
- `374`, `439` — la competencia por la atención y el presupuesto de destellos
