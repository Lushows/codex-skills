# 451 — Velocidad del movimiento, medida

El recorrido en tanto por ciento no es una velocidad. Un empuje del 12% en un plano de 4 segundos y
el mismo 12% en uno de 12 segundos son **tres veces distintos**, y solo uno de los dos se percibe como
respiración. Este módulo convierte porcentajes en píxeles por segundo, que es la única unidad en la
que el ojo juzga.

`450` reparte los gestos. Aquí se les pone número.

---

## 1. Cuánto se mueve de verdad un empuje

Un elemento situado a una distancia `u` del centro (en tanto por uno del ancho) se desplaza en
pantalla `ancho · u · (z − 1)`. En el borde del cuadro, `u = 0,5`. De ahí sale la cuenta:

> **Recorrido en el borde = 960 · r píxeles** (lienzo 1920), y en la esquina, contando también el
> vertical, `√(960r)² + (540r)²` = **1,10 · 960 r**.

Medido para un lienzo 1920×1080 a 25 fps:

| Recorrido | Borde (px) | Esquina (px) | 4 s: px/s | px/f | 6,73 s: px/s | px/f | 12 s: px/s |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4% | 38 | 44 | 11,0 | 0,44 | 6,5 | 0,26 | 3,7 |
| 8% | 77 | 88 | 22,0 | 0,88 | 13,1 | 0,52 | 7,3 |
| 10% | 96 | 110 | 27,5 | 1,10 | 16,4 | 0,65 | 9,2 |
| **12%** | **115** | **132** | **33,0** | **1,32** | **19,6** | **0,79** | **11,0** |
| 16% | 154 | 176 | 44,1 | 1,76 | 26,2 | 1,05 | 14,7 |
| 22% | 211 | 242 | 60,6 | 2,42 | 36,0 | 1,44 | 20,2 |
| 35% | 336 | 386 | 96,4 | 3,86 | 57,3 | 2,29 | 32,1 |

Léela en horizontal y salta a la vista lo que casi nadie tiene en cuenta: **el 12% en un plano de
12 segundos se mueve a 11 px/s, más lento que el 4% en un plano de 4 segundos.** Un episodio con
planos de duraciones dispares y un recorrido fijo del 12% no tiene un ritmo de movimiento coherente:
tiene planos de ritmos distintos que se parecen en la hoja de cálculo.

---

## 2. La banda legible

Con esa tabla delante, las bandas que funcionan, en píxeles de salida por segundo:

| px/s | Cómo se lee | Uso |
|---|---|---|
| < 8 | no se percibe. El plano parece quieto | inútil |
| 8 – 12 | al límite. Se nota solo comparando extremos | planos largos de descanso |
| **13 – 40** | **respiración. Se siente vivo sin llamar la atención** | el 80% de los planos |
| 40 – 90 | intencionado. El movimiento es el contenido | remates, revelaciones |
| > 120 | tránsito. Deja de leerse la imagen | transiciones, barridos |

**La regla operativa:** si el plano dura más de 8 segundos, deja de pensar en porcentaje y fija la
velocidad. Recorrido = `px/s deseados · duración / 1056` (1056 = 1,10 · 960). Para 22 px/s en un plano
de 11 s: `22 · 11 / 1056 = 0,229`, un 23%. Sí: los planos largos piden **más** recorrido, no menos.

---

## 3. La deriva: de píxeles de fuente a píxeles de pantalla

Cuando desplazas la ventana, los números que escribes en `x` e `y` están en **píxeles de la imagen de
entrada**, no de la salida. La conversión es la ampliación efectiva: `salida / (iw/z)`.

```
fuente 2688, zoom 1,05, salida 1920  ->  1 px de fuente = 0,75 px de pantalla
```

| Paso (px-fuente/fotograma) | px de salida/f | px/s a 25 fps | Se lee como |
|---:|---:|---:|---|
| 0,8 | 0,60 | 15,0 | deriva apenas perceptible |
| 1,4 | 1,05 | 26,2 | deriva cómoda |
| **2,1** | **1,58** | **39,4** | **el tope de lo que no llama la atención** |
| 3,5 | 2,62 | 65,6 | travelling declarado |
| 6,0 | 4,50 | 112,5 | tránsito |

Ese 2,1 es el valor que lleva la deriva diagonal del motor documental, y por eso está justo donde
está: 39 px/s es el borde superior de la banda de respiración.

**El error que produce la conversión olvidada:** cambias la fuente de 2688 a 4320 «para tener más
calidad» y la misma expresión de deriva se vuelve un 38% más lenta, porque cada píxel de fuente ahora
vale menos en pantalla. El plano se apaga y nadie sabe por qué.

---

## 4. Cómo se mide la velocidad de un plano ya renderizado

No hace falta creerse la cuenta. La diferencia media entre fotogramas consecutivos es proporcional al
desplazamiento:

```bash
ffmpeg -hide_banner -i plano.mp4 \
  -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o "YAVG=[0-9.]*"
```

⚠️ **Con `-loglevel error` esto no imprime nada** y parece que ha fallado: `metadata=print`,
`signalstats`, `psnr`, `ssim`, `freezedetect` y `blackdetect` escriben en nivel `info`. Quita el
`-loglevel` o ponlo en `info`.

La serie de valores te dice dos cosas: la **media** es la velocidad, y la **dispersión** es el temblor
(`453`). Un plano sano tiene media estable y coeficiente de variación por debajo del 3%.

---

## 5. Acelerar y frenar

Un recorrido a velocidad constante tiene aceleración infinita en los dos extremos: arranca de 0 a
1,3 px/f en un fotograma. Eso es lo que se lee como «plantilla». La corrección barata, sin salir de
`zoompan`, es sustituir `on/nf` por una curva suave:

```bash
# lineal            : 1+r*(on/nf)
# arranca y frena   : 1+r*(0.5-0.5*cos(PI*on/nf))       <- coseno, la más honrada
# solo frena al final: 1+r*(1-pow(1-on/nf,3))
zoompan=z='1+0.12*(0.5-0.5*cos(3.14159*on/168))':d=1:\
x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25
```
La versión con coseno recorre exactamente lo mismo pero la velocidad de pico es **π/2 = 1,57 veces**
la media: si querías 20 px/s de media, en el centro del plano va a 31. Comprueba que ese pico sigue
dentro de la banda antes de darlo por bueno. La teoría de las curvas está en `84`.

---

## Errores frecuentes

1. **Fijar el recorrido en porcentaje y dejar que la duración decida la velocidad.** Es la causa de
   que un episodio tenga planos que respiran y planos muertos sin ninguna lógica.
2. **Planos largos con poco recorrido.** Por debajo de 8 px/s el movimiento no existe y sigue
   costando render.
3. **Escribir la deriva en píxeles sin convertir a pantalla.** Cambias la resolución de la fuente y
   cambias la velocidad sin tocar la expresión.
4. **Olvidar que una curva de aceleración sube la velocidad de pico** un 57% sobre la media.
5. **Medir con `-loglevel error`** y concluir que el comando no funciona.
6. **Comparar velocidades entre formatos sin normalizar.** 30 px/s en 1920 de ancho no es lo mismo
   que 30 px/s en 1080: en vertical eso es casi el doble de recorrido relativo (`457`).
7. **Usar la misma velocidad para todo el episodio.** La monotonía del movimiento cansa igual que la
   del ritmo de corte.

---

## Relacionado

- `450` — el modelo geométrico y el reparto de gestos del que salen estos números
- `453` — la dispersión de esa misma serie de diferencias: el temblor
- `457` — por qué en vertical los mismos px/s se leen más rápido
- `84` — curvas de animación: la matemática del arranque y el frenado
- `467` — el índice de frenado: una sola cifra para auditar si una animación es lineal
- `458` — lo que cuesta renderizar cada uno de estos planos
- `108` — el instrumental de medida (`signalstats`, `metadata=print`) a fondo
- `canales_lushows/31` y `/38` — curvas de aceleración y ritmo del movimiento a lo largo del episodio
