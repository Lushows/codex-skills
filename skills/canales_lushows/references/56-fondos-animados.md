# 56 · Fondos animados

**Qué resuelve:** el `zoompan` mueve el fondo entero como una lámina rígida. Un fondo vivo
tiene **capas que se mueven a velocidades distintas** — y eso es lo que hace que se lea
como un espacio y no como una foto que se acerca.

---

## La regla de oro

> **El fondo se mueve por debajo del umbral de atención.** Si el espectador nota que el
> fondo se mueve, el fondo está robando la escena.

Todo lo que se mueva en el fondo va **más lento que el elemento más lento del collage** y
en dirección distinta a la del `zoompan`. Si el fondo empuja hacia dentro y una capa
deriva a la izquierda, el ojo lee profundidad. Si todo empuja igual, lee zoom barato.

| Capa | Velocidad en pantalla | Ejemplo |
|---|---|---|
| Fondo base (`zoompan`) | 8-16% del cuadro en toda la escena | La lámina completa |
| Capa media | 20-40 px en 6 s | Textura, rejilla, suelo |
| Capa cercana | 60-120 px en 6 s | Humo, niebla, primer plano borroso |
| Punto de luz | 10-20 px en 6 s | Deriva del haz |

**Máximo dos capas en movimiento** además del `zoompan`. Con tres, el fondo hierve.

---

## Método 1 · Capas separadas (el que se usa por defecto)

El fondo se renderiza en **dos o tres PNG**: la base opaca y las capas con alfa. Después
`motor.py` las mueve por separado. Sale barato, es infinitamente suave y no multiplica el
número de archivos.

En `fondos.py`, la misma escena se exporta en partes:

```python
F["f_planta"]      = f'<div class="esc" style="background:...">{textura}{capas(".62")}</div>'
F["f_planta_humo"] = f'<div class="esc" style="background:transparent">{humo}</div>'
```

Para las capas con alfa hay que añadir al comando de Chrome:

```
--default-background-color=00000000
```

Sin eso, la capa sale con fondo blanco y no sirve como sobreimpresión.

Y en el render de la escena:

```bash
ffmpeg -y \
  -loop 1 -framerate 25 -t 6.4 -i render/f_planta.png \
  -loop 1 -framerate 25 -t 6.4 -i render/f_planta_humo.png \
  -filter_complex "\
[0:v]scale=4320:-2,zoompan=z='1+0.00048*on':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':\
s=1920x1080:fps=25,format=rgba[bg];\
[1:v]scale=4320:-2,format=rgba,colorchannelmixer=aa=0.34[hu];\
[bg][hu]overlay=x='-1200-t*26':y='-600+t*7':shortest=1[out]" \
  -map "[out]" -c:v libx264 -crf 16 -pix_fmt yuv420p render/_planta.mp4
```

La capa de humo es más grande que el cuadro a propósito: entra desplazada
(`x=-1200-t*26`) y se arrastra 166 px en los 6,4 s. Eso son **26 px/s**: se percibe como
aire en movimiento, no como un objeto que cruza.

| Expresión | Movimiento |
|---|---|
| `x='-1200-t*26'` | Deriva lateral constante |
| `y='-600+t*7'` | Ascenso lento (humo que sube) |
| `x='-1200+120*sin(t*0.35)'` | Vaivén: para niebla y tela |
| `x='-1200-t*26':y='-600-t*3'` | Diagonal suave, la más natural |

---

## Método 2 · Ciclo de fotogramas (para humo y parpadeo)

Cuando el movimiento no es un desplazamiento sino una **deformación** —humo que se
retuerce, una luz que parpadea— hay que renderizar varios fotogramas del mismo HTML.

Chrome congela la animación en el instante que se le pida con `animation-delay` negativo y
`animation-play-state:paused`:

```css
.humo{animation:retorcer 8s linear infinite;animation-play-state:paused;
      animation-delay:{{DELAY}}}
@keyframes retorcer{
  from{transform:translate(0,0) scale(1)}
  to  {transform:translate(-90px,-60px) scale(1.12)}}
```

```python
CICLO, N = 8.0, 16                       # 8 s de ciclo en 16 fotogramas
for i in range(N):
    delay = -(CICLO * i / N)
    html = plantilla.replace("{{DELAY}}", f"{delay:.3f}s")
    io.open(tmp, "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--no-sandbox", f"--user-data-dir={PERFIL}", "--no-first-run",
                    "--default-background-color=00000000",
                    "--virtual-time-budget=2200", "--force-device-scale-factor=2.25",
                    "--window-size=1920,1080",
                    f"--screenshot=render/f_humo_{i:02d}.png",
                    "file:///" + tmp.replace("\\", "/")], capture_output=True, timeout=150)
```

El ciclo se monta una vez y luego se repite tantas veces como haga falta:

```bash
ffmpeg -y -framerate 12 -i render/f_humo_%02d.png -c:v ffv1 render/_ciclo_humo.mkv
ffmpeg -y -stream_loop -1 -i render/_ciclo_humo.mkv -t 6.4 -c:v ffv1 render/_humo64.mkv
```

**16 fotogramas a 12 fps** = 1,33 s de ciclo, que al repetirse no se nota si la animación
es un bucle cerrado (el fotograma 16 debe empatar con el 1: por eso `linear infinite` y no
`ease`). Renderizar 100 fotogramas a 4320 px es tirar veinte minutos: no hace falta.

---

## Parpadeo de luz sin fotogramas

Para una luz que respira basta con animar el alfa de la capa en ffmpeg:

```
[1:v]format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':\
a='alpha(X,Y)*(0.78+0.22*sin(2*PI*T*0.6))'[luz]
```

`geq` es lento: usarlo solo en capas pequeñas (menos de 1000 px de lado), nunca sobre el
fondo entero.

## Cuándo NO animar el fondo

| Caso | Por qué |
|---|---|
| Escena con 3-4 elementos vivos | Ya hay movimiento de sobra; el fondo debe estar quieto |
| La cifra clave en pantalla | Nada compite con el dato |
| Escenas de menos de 3 s | No da tiempo a percibirlo; solo añade peso de render |
| Fondo de datos (`54`) | Una rejilla que se mueve marea |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Capa que se mueve a más de 150 px/s | Se lee como objeto, roba la escena |
| Tres o más capas móviles | El fondo hierve y cansa |
| Movimiento en la misma dirección que el `zoompan` | Se anulan: parece un zoom sucio |
| Ciclo que no cierra | Salto visible cada vez que repite |
| Olvidar `--default-background-color=00000000` | La capa sale con fondo blanco |
| Animar el fondo en la escena del dato | El espectador pierde la cifra |

## Relacionado

`50` · `55` · `30` catálogo de movimientos · `33` parallax real · `37` cámara simulada
