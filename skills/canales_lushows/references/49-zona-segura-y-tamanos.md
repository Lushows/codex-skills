# 49 · Zona segura y tamaños

**Qué resuelve:** el texto se compone en un monitor de 27 pulgadas y se ve en un móvil
de 6, con la interfaz de la plataforma encima. Lo que ahí se decidió como "elegante y
discreto" llega al espectador como una línea gris ilegible detrás del botón de
seguir. Aquí están los márgenes y los mínimos, en píxeles.

---

## El mínimo se mide en altura de mayúscula

El `font-size` no dice cuán grande se ve un texto: cada familia usa una parte distinta
del cuerpo. Medido con las fuentes de esta máquina:

| Familia | Caja de mayúscula | `font-size` para 44 px de caja |
|---|---|---|
| Arial / Arial Black | 0,716 em | 61 px |
| Georgia | 0,693 em | 63 px |
| Times New Roman | 0,663 em | 66 px |
| Consolas | 0,638 em | 69 px |
| Courier New | 0,571 em | 77 px |

Un titular de 60 px en Courier New tiene la misma presencia que uno de 48 px en Arial.
**Los mínimos de abajo son de caja de mayúscula, no de `font-size`.**

### Mínimos (lienzo 1920×1080)

| Tipo de texto | Caja mín. | `font-size` aprox. (Consolas / Arial) |
|---|---|---|
| Titular / destacado | 76 px | 119 / 106 |
| Cifra de impacto | 90 px | 141 / 126 |
| Subtítulo de transcripción | 44 px | 69 / 61 |
| Rótulo de objeto | 32 px | 50 / 45 |
| Atribución, fuente, pie | **24 px** | 38 / 34 |

**24 px de caja es el suelo absoluto del canal.** Por debajo, en un móvil, deja de ser
texto y pasa a ser textura. Si un dato no cabe a 24 px, el dato sobra o el bloque está
mal compuesto — nunca se resuelve reduciendo el cuerpo.

En **9:16 (1080×1920)** todo sube un escalón: el vídeo se ve a un brazo de distancia
pero compitiendo con notificaciones y con el pulgar encima. Suelo: **34 px de caja**;
transcripción: **56 px**.

---

## Zona segura 16:9 — 1920×1080

```
      ┌──────────────────────────────────────────┐
   96 │  ┌────────────────────────────────────┐  │ 96
      │  │                                    │  │
      │  │        TEXTO SEGURO                │  │
      │  │        1728 × 888                  │  │
      │  │                                    │  │
      │  └────────────────────────────────────┘  │
  150 │      ← franja de reproductor y título     │
      └──────────────────────────────────────────┘
```

| Margen | Píxeles | Motivo |
|---|---|---|
| Izquierda / derecha / superior | **96** (5%) | Recorte en televisores y vistas previas |
| Inferior | **150** | Barra de progreso, tiempo y controles del reproductor |
| Inferior derecha | **300 × 150** | Reloj, calidad, pantalla completa |
| Superior derecha | **340 × 130** | Tarjetas de sugerencia y menú |

El texto que quiera vivir en el último tercio inferior sube a `y ≤ 930`.

**Además, el recuadro de 16:9 se recorta a 1:1 y a 9:16 en algunas superficies.** Lo
que sobrevive a los tres es la columna central de **608 px de ancho** (`x` de 656 a
1264). Ahí van el remate y la cifra final, y sólo ahí.

---

## Zona segura 9:16 — 1080×1920

Las interfaces cambian sin avisar, así que estos son **márgenes de trabajo
conservadores**: la unión de lo que tapan TikTok, Reels y Shorts. La única autoridad es
el propio teléfono (ver la verificación abajo).

| Margen | Píxeles | Qué hay ahí |
|---|---|---|
| Superior | **200** | Barra de estado, pestañas, buscador |
| Inferior | **520** | Nombre de cuenta, descripción, audio, barra de progreso |
| Derecha | **200** | Columna de iconos: perfil, me gusta, comentar, compartir |
| Izquierda | **60** | Sólo respiración |

**Zona útil resultante: 820 × 1200** — menos de la mitad del cuadro. Componer el
vertical sin esta reserva es por qué la mitad de los cortes verticales son inservibles.
Y su centro no es el del cuadro: el centro óptico está en `x = 470`, `y = 800`.

---

## Verificación

```bash
# 1 · plantilla de zona segura, para superponer al montar
ffmpeg -f lavfi -i "color=c=black@0:s=1080x1920,format=rgba" -vf "
drawbox=x=60:y=200:w=820:h=1200:color=0x00FF00@0.9:t=4,
drawbox=x=880:y=200:w=200:h=1720:color=0xFF0000@0.35:t=fill,
drawbox=x=0:y=1400:w=1080:h=520:color=0xFF0000@0.35:t=fill" \
  -frames:v 1 -y zona_9x16.png

# 2 · la prueba del pulgar: el fotograma al tamaño real de un móvil en la mano
ffmpeg -i salida/piloto.mp4 -vf "fps=1/3,scale=-1:420,tile=8x3" -frames:v 1 prueba.png
```

**La prueba del pulgar:** si en `prueba.png` —donde cada cuadro mide unos 420 px de
alto, aproximadamente lo que ocupa un móvil visto a un brazo— no se lee un texto, ese
texto no existe. No se discute: se agranda o se quita.

Y una vez por episodio, **verlo en el teléfono de verdad**, subido como no listado. Es
el único sitio donde aparece la interfaz real de la plataforma encima del vídeo.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Fijar mínimos por `font-size` | Courier a 60 px se lee como Arial a 48 px |
| Texto pegado al borde inferior en 16:9 | Lo tapa la barra de progreso del reproductor |
| Marca de agua o firma en la esquina inferior derecha | Choca con los controles del reproductor |
| Componer el vertical usando el cuadro entero | La columna de iconos se come el lado derecho |
| Centrar en el 9:16 por el centro geométrico | Queda bajo y descentrado respecto de la zona útil |
| Bajar el cuerpo para que quepa el texto | Se pierde el dato; hay que acortar el texto |
| Validar sólo en el monitor grande | Ahí todo se lee, incluso lo que no se lee |
| Reencuadrar el 9:16 recortando el 16:9 ya montado | El texto queda fuera o partido |

## Relacionado

`42` tipografía del canal · `44` la cifra en pantalla · `45` subtítulos y destacados ·
`46` texto sobre collage · `28` respiración del cuadro · `99` título, miniatura y descripción
