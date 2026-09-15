# 426 — Orden de aplicación

Los mismos filtros, la misma dosis, el mismo material: cambia solo el orden en que van escritos y sale
otro video, con otro peso y otro tiempo de render. `102` ya lo dice —«se aplican de izquierda a derecha
y cambiar el orden cambia el resultado»— pero lo dice como advertencia. Aquí está medido, con la
diferencia en números y con la regla que sale de ellos.

---

## 1. El principio: cada filtro ve lo que dejó el anterior

Un filtro no opera sobre «el video». Opera sobre el flujo tal y como lo entrega su vecino de la
izquierda. De ahí salen los tres efectos del orden:

1. **El que va después modifica lo que hizo el anterior.** Una viñeta detrás de un grano oscurece el
   grano de las esquinas: el grano sigue ahí, pero atenuado.
2. **El que va después decide si el anterior sobrevive.** Un escalado detrás de una nitidez promedia los
   bordes que la nitidez acababa de crear. El trabajo se hizo y se tiró.
3. **El tamaño en que trabaja cada uno depende de quién va antes.** Un `unsharp` antes de un `scale=960`
   procesa 2,07 megapíxeles por fotograma; después, 0,52. El mismo filtro, cuatro veces el trabajo.

---

## 2. Medido: tres pares, tres lecciones

Clip de 4 s a 1080p25, CRF 20 `preset veryfast`, `signalstats` promediado.

### Par 1 — grano y viñeta

| Orden | `utime` | YDIF | MB |
|---|---|---|---|
| `noise,vignette` | 4,92 | **1,91** | 1,72 |
| `vignette,noise` | 4,52 | **1,98** | 1,96 |

Poner el grano **al final** conserva un 4% más de textura temporal y sube el peso un 14%. Coherente: la
viñeta multiplica la luminancia hacia los bordes y, aplicada después, atenúa el grano justo donde más
se veía. La conclusión para la plantilla: **el grano es el último filtro antes de `format=yuv420p`.**

### Par 2 — contraste y nitidez

| Orden | `utime` | YDIF | MB |
|---|---|---|---|
| `eq=contrast=1.25,unsharp=5:5:0.8` | **8,11** | 3,93 | 2,92 |
| `unsharp=5:5:0.8,eq=contrast=1.25` | **7,14** | 3,92 | 2,89 |

El resultado es **el mismo** (3,93 contra 3,92 está dentro del ruido; 2,92 contra 2,89 MB, un 1%). Lo
que cambia es el coste: casi un segundo por cada 100 fotogramas, un **14% más caro** si el contraste va
primero. Cuando dos filtros dan el mismo resultado en cualquier orden, **el orden lo decide el
cronómetro**.

### Par 3 — nitidez y escalado (el que importa de verdad)

| Orden | `utime` | YDIF | MB |
|---|---|---|---|
| `scale=960:-2,unsharp=5:5:0.8` | **4,77** | **2,05** | 0,38 |
| `unsharp=5:5:0.8,scale=960:-2` | **7,75** | **1,74** | 0,32 |

🔴 **Afilar antes de reducir es peor en las dos monedas a la vez.** Cuesta un **63% más** de CPU —porque
`unsharp` trabaja sobre cuatro veces más píxeles— y entrega **un 15% menos** de estructura, porque el
reescalado promedia justo los bordes que acababas de reforzar. Pagas más por un resultado peor.

Ésta es la inversión de orden más frecuente en las plantillas heredadas, y es la que más render
desperdicia.

---

## 3. La cadena canónica

De los tres pares y del resto del bloque sale un orden que sirve para casi todo. Se lee como una tubería
de cuatro tramos:

```
1. NORMALIZAR   fps → escala → recorte → setsar
2. CORREGIR     denoise → exposicion → balance → contraste → saturacion → LUT
3. AFINAR       nitidez → viñeta → destellos → aberracion
4. TEXTURIZAR   grano → format=yuv420p
```

```bash
-vf "fps=25,\
scale=1920:-2:flags=lanczos,setsar=1,\
hqdn3d=2:1:3:2,\
eq=contrast=1.05:saturation=0.94:gamma=1.16:brightness=0.045,\
unsharp=5:5:0.35:5:5:0.0,\
vignette=PI/5.6,\
noise=alls=6:allf=t+u,\
format=yuv420p"
```

Las razones de cada frontera:

| Frontera | Por qué |
|---|---|
| escalar **antes** de todo | menos píxeles que procesar en todo lo que viene (`102`) |
| denoise **antes** de corregir | corregir ruido lo amplifica |
| LUT **después** del contraste | la LUT espera una entrada estándar, no una ya estirada |
| nitidez **después** de escalar | si no, el escalado se come el trabajo (par 3) |
| viñeta **después** de nitidez | la viñeta oscurece y suaviza el borde: iría en contra |
| grano **al último** | todo lo que vaya detrás lo atenúa o lo promedia (par 1, `428`) |
| `format=yuv420p` **el último de todos** | compatibilidad universal (`102`) |

---

## 4. Las cinco inversiones que rompen cosas

| Inversión | Qué pasa | Medida que lo delata |
|---|---|---|
| nitidez antes de escalar | +63% CPU y −15% estructura | `utime` y `YDIF` |
| grano antes de escalar | el grano desaparece | `YDIF` vuelve al valor base |
| grano antes de la viñeta | grano atenuado en los bordes | `YDIF` −4% |
| corregir antes de denoise | el denoise borra lo que corregiste | SSIM cae más de lo esperado |
| `format=yuv420p` en medio | los filtros de después trabajan a 8 bits submuestreados | banding visible |

Y dos que no son de efecto pero rompen igual, ya cubiertas en `102` y `109`:

- **`fps` después de un `overlay` o un `concat`**: la sincronía se va.
- **`setsar=1` al final en vez de al normalizar**: el clip llega deformado al montaje.

---

## 5. El arnés de permutaciones

Cuando la cadena tiene tres o cuatro eslabones y no está claro el orden, se prueban todas. Con tres son
seis combinaciones; en un clip de 4 s son un par de minutos:

```bash
#!/usr/bin/env bash
# permutar.sh — prueba los ordenes posibles de una cadena de 3
IN=base.mp4
A="eq=contrast=1.05:saturation=0.94:gamma=1.16:brightness=0.045"
B="noise=alls=6:allf=t+u"
C="vignette=PI/5.6"
probar () {
  F="$1"
  U=$(ffmpeg -hide_banner -benchmark -i "$IN" -vf "$F" -f null - 2>&1 \
      | grep -o 'utime=[0-9.]*' | head -1 | cut -d= -f2)
  ffmpeg -hide_banner -loglevel error -y -i "$IN" -vf "$F,format=yuv420p" \
      -c:v libx264 -crf 20 -preset veryfast -an p.mp4
  D=$(ffmpeg -hide_banner -i p.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" \
      -f null - 2>&1 | grep -o 'YDIF=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.2f",s/n}')
  M=$(awk -v s="$(stat -c%s p.mp4)" 'BEGIN{printf "%.2f",s/1048576}')
  printf "u=%-7s YDIF=%-6s %sMB   %s\n" "$U" "$D" "$M" "$(echo "$F" | cut -c1-70)"
}
probar "$A,$B,$C"; probar "$A,$C,$B"; probar "$B,$A,$C"
probar "$B,$C,$A"; probar "$C,$A,$B"; probar "$C,$B,$A"
```

Se ordena la salida por `utime` y se mira la columna de YDIF: **si varias permutaciones dan el mismo
resultado, se elige la más barata.** Si dan resultados distintos, entonces el orden es una decisión de
imagen y hay que mirarlas.

Con cuatro eslabones son 24 permutaciones y ya no se prueban todas: se fijan los tramos de la sección 3
y se permuta solo dentro de un tramo.

---

## 6. El orden dentro de `filter_complex`

En un grafo con varias ramas el orden no es lineal y aparece un tipo nuevo de error: **aplicar el efecto
en la rama equivocada.**

```bash
# MAL: el grano va sobre el fondo, y los recortes encima quedan limpios y "pegados"
[0:v]noise=alls=6:allf=t+u[bg];[bg][1:v]overlay=...[v]

# BIEN: el grano va sobre la composicion entera, al final
[0:v][1:v]overlay=...,noise=alls=6:allf=t+u,format=yuv420p[v]
```

Ésta es la diferencia entre un collage que parece una sola imagen y uno que parece un PowerPoint. La
regla: **lo que unifica va después de componer; lo que caracteriza una capa va dentro de su rama.**

```bash
# Cada recorte lleva LO SUYO dentro de su rama...
[1:v]scale=600:-1,format=rgba,fade=t=in:st=0:d=0.30:alpha=1[e1];
# ...y lo que los hace convivir, sobre el resultado
[bg][e1]overlay=...,eq=...,vignette=PI/5.6,noise=alls=6:allf=t+u,format=yuv420p[out]
```

Es exactamente la estructura del `motor.py` del canal documental: escala, desvanecido y opacidad por
elemento, y el acabado —`eq` + destellos + grano + viñeta— sobre la composición final, en `acabar.py`.
Ver `104` y `105` para la mecánica del grafo.

---

## 7. El orden y el coste: la regla que ahorra render

Junta las dos mitades del módulo en una frase: **lo que reduce el número de píxeles va lo más a la
izquierda posible; lo que añade información va lo más a la derecha posible.**

- Reducen píxeles: `crop`, `scale` hacia abajo, `fps` hacia abajo. **Primeros.**
- No cambian el número de píxeles: `eq`, `hue`, LUT, `vignette`. **En medio, ordenados por criterio de
  imagen.**
- Añaden información que el resto tendría que arrastrar: `unsharp`, `noise`. **Últimos.**

Aplicada al par 3, esa regla sola habría dado con el orden correcto sin medir nada. Aplicada al caso del
canal documental (`422`), habría evitado que el fondo entrara a 4320 px en cada fotograma.

---

## Errores frecuentes

- **Afilar antes de reducir.** Medido: +63% de CPU y −15% de estructura. La peor inversión posible.
- **Poner el grano antes de un escalado o de una viñeta.** Se promedia o se atenúa.
- **Escalar después de corregir.** Gastas todo el color en píxeles que vas a tirar.
- **Corregir antes de limpiar el ruido.** Amplificas lo que ibas a quitar.
- **Meter `format=yuv420p` en medio de la cadena.** Lo que venga después trabaja con menos precisión.
- **Poner la LUT antes del contraste.** La LUT espera una entrada estándar.
- **Aplicar el efecto unificador dentro de una rama del grafo.** El collage se ve como capas pegadas.
- **Cambiar el orden y no volver a medir.** El resultado cambia; el número anterior ya no vale.
- **Probar permutaciones a ojo.** Con tres filtros son seis, y el arnés tarda dos minutos.
- **Suponer que dos órdenes que «se ven igual» cuestan igual.** Medido: 14% de diferencia en el par 2.

---

## Checklist

- [ ] La cadena sigue los cuatro tramos: normalizar, corregir, afinar, texturizar.
- [ ] Todo lo que reduce píxeles está lo más a la izquierda posible.
- [ ] La nitidez va **después** del escalado.
- [ ] El grano es el último filtro antes de `format=yuv420p`.
- [ ] `format=yuv420p` no aparece en medio de la cadena.
- [ ] El denoise va antes de la corrección, no después.
- [ ] En el grafo, lo que unifica va después de componer.
- [ ] Cuando dos órdenes dan el mismo resultado, elegí el más barato en `utime`.
- [ ] Volví a medir la cadena después de reordenarla.
- [ ] El orden elegido está escrito en la plantilla con su motivo.

---

## Relacionado

- `102` — qué hace cada filtro y la plantilla de normalización
- `104`, `105` — `filter_complex` y superposición de capas: el orden en un grafo con ramas
- `420`, `421` — el arnés y las magnitudes
- `422` — el coste, y por qué el tamaño de cuadro manda
- `425` — efectos que compiten: el par que no cambia de resultado pero sí de precio
- `428` — el grano al final, y por qué
- `400`–`403` — orden de capas y el z que se rompe (el orden en la composición, no en los filtros)
- `109` — trampas de ffmpeg
- `66` — la dosis artesanal de nitidez, viñeta y grano
