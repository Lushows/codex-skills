# 71 · Transiciones de collage

**Qué resuelve:** las tres transiciones que pertenecen al idioma del canal —barrido de
hoja, pase de página y apilado de recortes— y cómo se construyen en un pipeline que
renderiza cada escena por separado.

---

## El principio: la transición la hace un objeto, no un filtro

En un collage nada se desvanece: **algo pasa por delante**. El fundido cruzado es un
recurso de vídeo; una hoja que barre el cuadro es un recurso de papel. Las tres
transiciones de esta familia son **objetos que se mueven**, y eso trae una ventaja
técnica enorme:

> **Se construyen DENTRO del render de cada escena, mitad en el final de A y mitad en el
> principio de B. La unión sigue siendo un corte duro, y `concat -c copy` sigue valiendo.**

Nada que recodificar, nada que descuadre la voz. Es la diferencia con `xfade` (`79`).

---

## 1. Barrido con hoja de papel

Una hoja grande cruza el cuadro de derecha a izquierda. El corte cae en el fotograma en
que lo cubre del todo, así que el ojo no puede verlo. Parámetros fijos (25 fps, 1920×1080):

| Parámetro | Valor | Por qué |
|---|---|---|
| Hoja | `fx/hoja_barrido.png`, 3200×1600 px, papel `#E6DCC4`, borde rasgado | Tiene que sobrar por los cuatro lados |
| Duración total | **0,40 s (10 fotogramas)** | Menos se lee como parpadeo; más se hace lento |
| Reparto | 0,20 s al final de A · 0,20 s al arranque de B | El corte cae en el medio |
| Velocidad | 12.800 px/s (1920 → −3200) | Cubre el cuadro entre t=0,15 y t=0,25 |
| Giro | −4° | Recto parece un panel; más de 6° descubre esquinas |
| Sonido | `ob_papel` adelantado 0,12 s (`75`) | Sin sonido es un rectángulo, no papel |

**En el final de la escena A** (con `durA` la duración de la escena):

```
[N:v]scale=3200:-1,format=rgba,rotate=-0.06981:c=none:ow=rotw(-0.06981):oh=roth(-0.06981)[hoja];
[bg][hoja]overlay=x='1920-12800*(t-(DURA-0.20))':y=-260:
          enable='gte(t,DURA-0.20)'[v]
```

**En el arranque de la escena B** (la hoja entra ya cubriendo y sale por la izquierda):

```
[N:v]scale=3200:-1,format=rgba,rotate=-0.06981:c=none:ow=rotw(-0.06981):oh=roth(-0.06981)[hoja];
[bg][hoja]overlay=x='-640-12800*t':y=-260:enable='lt(t,0.20)'[v]
```

El `-640` es la posición exacta en que quedó la hoja al terminar A (`1920 − 12800·0,20`):
si se cambia la velocidad hay que recalcularlo o la hoja salta en el corte.

⚠️ `rotate` agranda el lienzo (`ow=rotw(...)`) y `x` se corre unos píxeles: con giros de
hasta 6° es imperceptible; si hace falta más, se rota el PNG de origen.

---

## 2. Pase de página

Una página gira sobre su lomo izquierdo y descubre la escena siguiente. No se puede
hacer con filtros de ffmpeg sin que parezca un "cubo 3D" de plantilla: **se pre-renderiza
con Chrome**, que es la herramienta que ya usa el proyecto para todo lo demás.

`paso_pagina.py` genera 12 PNG (0,48 s a 25 fps) con `perspective` + `rotateY` y una
sombra que crece con el giro:

```python
for i in range(12):
    ang = -i * 100 / 11                       # 0° → -100°
    som = 0.10 + 0.55 * (i / 11)              # se oscurece al girar
    html = f"""<!doctype html><meta charset='utf-8'><style>
    html,body{{width:1920px;height:1080px;background:transparent;overflow:hidden}}
    .esc{{perspective:2600px;width:1920px;height:1080px}}
    .pag{{width:1920px;height:1080px;transform-origin:left center;
      transform:rotateY({ang:.2f}deg);box-shadow:0 0 90px rgba(0,0,0,.55);
      background:linear-gradient(100deg,#E6DCC4,#CFC3A4);
      filter:brightness({1-som:.2f})}}
    </style><div class='esc'><div class='pag'></div></div>"""
    # escribir TODOS los HTML primero y capturar después, a fx/pag_%02d.png
```

Y se compone como cualquier otra entrada, esta vez como secuencia de imágenes:

```
ffmpeg -i escena_A.mp4 -framerate 25 -i fx/pag_%02d.png \
  -filter_complex "[0:v][1:v]overlay=0:0:enable='gte(t,DURA-0.24)':shortest=0" \
  -c:v libx264 -crf 17 -pix_fmt yuv420p -y escena_A_pag.mp4
```

Reparto: **6 fotogramas al final de A** (la página cubre y empieza a girar) y **6 al
arranque de B** (termina de girar y sale). Sonido: `ob_papel` + un toque de `tr_whoosh`
a −6 dB.

**Cuándo se usa:** salto de tiempo largo ("catorce años después"). Una por episodio.

---

## 3. Apilado de recortes

Cuatro o cinco recortes caen sobre el cuadro, uno cada 2-3 fotogramas, hasta taparlo. Ahí
va el corte. En B salen despedidos hacia fuera.

| Fotograma (relativo al corte) | Qué pasa |
|---|---|
| −15 a −13 | Cae el recorte 1 (grande, arriba-izquierda) |
| −12 a −10 | Cae el 2 (cubre el centro) |
| −9 a −7 | Cae el 3 |
| −6 a −2 | Caen 4 y 5, el cuadro queda **cubierto al 100%** |
| **0** | **corte** |
| +1 a +8 | Los cinco salen a la vez, cada uno en una dirección |

Cada recorte entra con `ease-out` de 0,12 s y su ángulo propio entre −7° y +7°. Sonido:
cinco `ob_papel` solapados, uno cada 2 fotogramas, bajando 1,5 dB cada vez.

**Cuándo se usa:** cambio de capítulo con acumulación de pruebas. Es ruidosa: una vez
por episodio, nunca dos.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Hoja más pequeña que el cuadro | Se ve el corte por una esquina: el efecto se delata |
| Opacidad menor que 1 en la hoja | Se transparenta la escena de abajo: doble exposición, no collage |
| No recalcular la `x` de arranque en B | La hoja salta varios cientos de píxeles en el corte |
| Usar el barrido en dos uniones seguidas | El espectador aprende el truco y deja de ver la historia (`78`) |
| Girar la hoja 20° "para que quede dinámica" | Las esquinas dejan de cubrir y asoma la escena de debajo |

## Relacionado

`70` · `73` · `75` · `77` · `78` · `25`
