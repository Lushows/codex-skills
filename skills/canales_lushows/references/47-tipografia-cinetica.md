# 47 · Tipografía cinética

**Qué resuelve:** el texto entra con `fade` y se queda quieto. Eso no es un error de
gusto: un texto que aparece sin gesto se lee como una capa pegada en posproducción, y
además desperdicia el único elemento del cuadro que puede reaccionar a la voz. Aquí
están los tres movimientos del canal y su implementación exacta.

Sólo tres. Un cuarto tipo de movimiento por episodio ya es inconsistencia.

---

## 1 · Golpe con sobre-impulso

Para la cifra de impacto, el nombre del protagonista y el remate. Es el gesto que
convierte un dato en revelación (`44`).

| Fase | Escala | Tiempo | Fotogramas a 25 fps |
|---|---|---|---|
| entrada | 0,74 → **1,06** | 0-0,18 s | 0-4 |
| asentamiento | 1,06 → 1,00 | 0,18-0,32 s | 4-8 |
| salida | fundido, sin escala | 0,35 s | — |

El sobre-impulso a **1,06** es todo: sin él es un *fade-in* con escala.

### La trampa de `zoompan`

`zoompan` **no baja de `z=1`**: cualquier valor menor se recorta a 1. No se puede
animar una reducción directamente. La salida es **pre-escalar el PNG al 74% del tamaño
final** y dejar que `zoompan` lo lleve hasta `z=1,35` (= 100%), pasando por 1,43
(= 106%).

```
escala_base = tamaño_final / 1.35
z_reposo    = 1.35        z_pico = 1.43        z_inicio = 1.00
```

Comprobado, con el PNG del texto centrado en un lienzo transparente de 1920×1080:

```python
FPS, DE, DA = 25, 0.18, 0.14              # entrada y asentamiento
a, b = int(DE * FPS), int((DE + DA) * FPS)  # 4 y 8
z = (f"if(lt(on,{a}),1.00+0.43*(on/{a}),"
     f"if(lt(on,{b}),1.43-0.08*((on-{a})/({b}-{a})),1.35))")

fc = ("[0:v]format=rgba[bg];"
      "[1:v]scale=1200:-1,format=rgba,"                     # 1200 = final(1620) / 1.35
      "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x00000000,"
      f"zoompan=z='{z}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
      "s=1920x1080:fps=25[t];"
      "[bg][t]overlay=0:0[out]")
```

- `d=1` + `fps=25` → un fotograma de salida por cada uno de entrada; sin esto `zoompan`
  genera 25 por imagen y el vídeo se congela.
- `on` es el índice del fotograma de salida, no el tiempo — la misma variable que usa
  `expr_fondo()` en `motor.py`.
- El `pad` a lienzo completo permite escalar sin que el texto se desplace. Para anclar
  el gesto en otra parte del cuadro se descentra el `pad`, no el `x`/`y` de `zoompan`.

Medido sobre el render: el ancho del texto va 534 → 753 px (pico) → 721 px (reposo),
que es exactamente 0,74 → 1,06 → 1,00.

---

## 2 · Cascada

Para fichas, listas y bloques de varias líneas. Cada línea repite el gesto de la
anterior con retardo, y el ojo baja con ellas.

| Parámetro | Valor |
|---|---|
| Retardo entre líneas | **0,07 s** (rápido, 5-8 líneas) · **0,11 s** (pausado, 2-4) |
| Gesto por línea | fundido + 22 px de deriva vertical hacia arriba, en 0,26 s |
| Salida | **todas a la vez**, no en cascada |

Entrar escalonado se lee como construcción; salir escalonado, como que algo se rompe.

Cada línea es un PNG y se declara con su propio offset en la tabla de eventos:

```python
BASE, PASO = -0.18, 0.07
for i, r in enumerate(["fch_nombre", "fch_alias", "fch_expediente", "fch_distrito"]):
    ESC["elementos"].append({
        "r": r, "ancla": "guzman", "offset": BASE + i * PASO,
        "dura": 3.4 - i * PASO, "x": "168", "y": str(420 + i * 74),
        "w": 620, "entrada": "abajo", "dur_entrada": 0.26, "fade_out": 0.30})
```

Nótese `"dura": 3.4 - i*PASO`: todas terminan en el mismo instante.

---

## 3 · Revelado por máscara

Para citas, titulares largos y cualquier texto que deba leerse como impreso que aparece
bajo una lupa.

### ⚠️ `crop` NO sirve para esto

`crop` evalúa `w` y `h` **una sola vez, al configurar el filtro**, cuando `t` todavía no
existe — sólo `x` e `y` se recalculan por fotograma, y `crop` no acepta `eval=frame`.
Comprobado en ffmpeg 8.1:

```
crop=w='iw*min(1,max(0,(t-1.0)/1.4))':h=ih:x=0:y=0
  → Error when evaluating the expression 'iw*min(1,max(0,(t-1.0)/1.4))'
```

Falla al arrancar, no a medias. **Cualquier receta de revelado basada en un `crop` que
crece con el tiempo está rota** — incluido el «Método 1» del módulo `41`.

### Lo que sí funciona: máscara sobre el canal alfa

Se extrae el alfa del PNG, se recorta con `geq` —que sí expone `T` (tiempo), `X`, `Y`,
`W` y `H`— y se vuelve a pegar con `alphamerge`:

```bash
# revelado de izquierda a derecha, arranque rapido y frenada (ease-out cubica)
ffmpeg -i fondo.mp4 -loop 1 -framerate 25 -t 6 -i titular.png -filter_complex "
[1:v]format=rgba,split[a][b];
[a]alphaextract,
   geq=lum='if(lt(X,W*(1-pow(1-clip((T-1.80)/0.55,0,1),3))),p(X,Y),0)'[m];
[b][m]alphamerge[txt];
[0:v][txt]overlay=x=160:y=760
" -y salida.mp4
```

- `1-pow(1-p,3)` es la curva **ease-out cúbica**: recorre el 70% del ancho en el primer
  tercio del tiempo y frena al final. Un revelado lineal se ve barato exactamente igual
  que un travelling lineal (`31`).
- `clip((T-t0)/D,0,1)` acota el progreso: antes de `t0` no se ve nada, después de
  `t0+D` queda completo.
- **`geq` va píxel a píxel en software.** Se aplica al PNG del texto **a su tamaño**,
  antes de cualquier `pad` o `scale` al lienzo. Sobre 1920×1080 el render se dispara.
- **`W` es el ancho del PNG, no el de las letras.** Un titular de 430 px de tinta dentro
  de un lienzo de 900 px termina de revelarse al 48% del recorrido y el resto del gesto
  no se ve. El PNG se recorta a la tinta antes de animarlo.

Variantes, cambiando sólo la condición de `geq` (con `p` = la expresión de progreso):

| Variante | `lum=` |
|---|---|
| De abajo hacia arriba | `if(gt(Y,H*(1-p)),p(X,Y),0)` |
| Desde el centro | `if(lt(abs(X-W/2),W/2*p),p(X,Y),0)` |
| Diagonal | `if(lt(X+Y*0.4,(W+H*0.4)*p),p(X,Y),0)` |
| **Borde suave de 60 px** | `p(X,Y)*clip((W*p-X)/60,0,1)` |

El borde suave es el que mejor se lee: un corte duro se ve como una persiana; 60 px de
degradado se ven como tinta que llega.

**Lo que NO se hace:** rotación 3D, rebote elástico de varias oscilaciones, trayectorias
curvas, desenfoque de movimiento, un gesto distinto por palabra, y movimiento durante la
permanencia. El gesto es de **entrada**; después, deriva mínima y quieto.

---

## Sincronía

El gesto empieza **antes** que la palabra, y cuánto antes depende del gesto:

| Gesto | Adelanto |
|---|---|
| Golpe | **0,15 s** — el pico de escala cae sobre la sílaba tónica |
| Cascada | **0,18 s** — la primera línea; las demás van detrás por diseño |
| Revelado | **0,25 s** — hay que empezar a leer antes de que la voz lo diga |

El sonido va en el fotograma del **pico**, no en el del arranque: `ob_impacto` para el
golpe, `ob_teletipo` recortado para el revelado, nada para la cascada salvo la primera
línea (`89`).

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `zoompan` con `z` menor que 1 | Se recorta a 1: no hay entrada, el texto aparece de golpe |
| `zoompan` sin `d=1` y sin `fps` | 25 fotogramas por imagen: el vídeo se congela |
| Escalar sin `pad` al lienzo | El texto se desplaza mientras crece |
| `crop` con `w` dependiente de `t` | Falla al configurar el filtro: el render muere |
| `geq` aplicado sobre el lienzo de 1920×1080 | El render se vuelve inviable; va sobre el PNG |
| Curva lineal en el revelado | Se ve barato, igual que un travelling lineal |
| Salida en cascada | Se lee como que algo falla |
| Gesto que sigue vivo durante toda la permanencia | Cansa y estorba la lectura |
| Sonido en el arranque del gesto | Suena adelantado: va en el pico |

## Relacionado

`41` máquina de escribir · `44` la cifra en pantalla · `31` curvas de aceleración ·
`32` entradas y salidas · `39` sincronizar gesto y palabra · `89` biblioteca de sonido
