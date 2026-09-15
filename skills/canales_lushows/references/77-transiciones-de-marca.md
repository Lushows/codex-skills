# 77 · La transición de marca: el tachado rojo

**Qué resuelve:** convertir el gesto de marca de Paper Empires —el tachado rojo `#E3120B`—
en una transición. Una barra de tinta roja cruza el cuadro, **borra** lo que había y
**descubre** lo que viene. Es la única transición del canal que se reconoce como firma.

---

## La regla de uso

> **Una vez por episodio, en la unión donde el protagonista cruza la raya.**

No es una transición de recurso: es un signo. Si aparece dos veces deja de significar
"aquí cambió todo" y pasa a ser un adorno. Y en el segundo en que aparece, **no puede
haber otro rojo en pantalla** ni puede pasar por encima de una cara.

| Parámetro | Valor |
|---|---|
| Color | `#E3120B` = `rgb(227, 18, 11)` |
| Duración | **0,44 s (11 fotogramas)** |
| Grosor de la línea de tinta | 22 px a cada lado del borde (44 px de banda) |
| Recorrido | de `x=−240` a `x=2160` (2400 px) |
| Borde | irregular: `90·sin(Y/37) + 40·sin(Y/11)` — la mano no traza recto |
| Sonido | `tr_whoosh` a −0,14 s + `ob_papel` a −0,06 s (`75`) |

---

## Variante A — barrido de tinta (la completa)

La tinta avanza y detrás de ella ya está la escena siguiente. Se construye cruzando dos
escenas, así que **sí recodifica** ese tramo: la escena A se renderiza con **0,44 s de
cola extra** y la unión pasa a ser un único archivo que sustituye a las dos en
`_escenas.txt` (misma lógica de solape que `79`, para no perder ni un fotograma de la
línea de tiempo).

Con `DURA = 11.60` (duración **nominal** de A), `DURB = 12.00`, `D = 0.44`:

```bash
ffmpeg -hide_banner \
 -i salida/e03_auge_ext.mp4 \
 -i salida/e04_caida.mp4 \
 -filter_complex "
 [0:v]fps=25,setsar=1,format=rgba,tpad=stop_mode=clone:stop_duration=12.00[a];
 [1:v]fps=25,setsar=1,format=rgba,setpts=PTS+11.60/TB,
      geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':
          a='255*lt(X,(T-11.60)/0.44*2400-240+90*sin(Y/37)+40*sin(Y/11))'[b];
 [a][b]overlay=0:0:eof_action=pass,
      geq=r='if(lt(abs(X-((T-11.60)/0.44*2400-240+90*sin(Y/37)+40*sin(Y/11))),22)*between(T,11.60,12.04),227,r(X,Y))':
          g='if(lt(abs(X-((T-11.60)/0.44*2400-240+90*sin(Y/37)+40*sin(Y/11))),22)*between(T,11.60,12.04),18,g(X,Y))':
          b='if(lt(abs(X-((T-11.60)/0.44*2400-240+90*sin(Y/37)+40*sin(Y/11))),22)*between(T,11.60,12.04),11,b(X,Y))',
      format=yuv420p[v]" \
 -map "[v]" -t 23.60 -c:v libx264 -crf 17 -preset medium -y salida/e03_e04_tachado.mp4
```

Qué hace cada pieza:

| Trozo | Para qué |
|---|---|
| `tpad=stop_mode=clone` | Alarga A congelando su último cuadro; queda debajo, tapado por B |
| `setpts=PTS+11.60/TB` | Coloca la escena B en su segundo exacto de la línea de tiempo |
| primer `geq` (`a=...`) | Máscara: B es opaca sólo a la izquierda del borde de tinta |
| segundo `geq` (`r/g/b`) | Pinta la banda roja **encima de las dos**, siguiendo el mismo borde |
| `between(T,11.60,12.04)` | Fuera de la transición no se toca ni un píxel |
| `-t 23.60` | `DURA + DURB`: la duración total no cambia ni un fotograma |

`geq` es lento (recorre píxel a píxel), pero aquí sólo se aplican 11 fotogramas de los
590 del tramo: el coste real son segundos.

## Variante B — el trazo que tacha (la barata)

Un trazo de tinta roja cruza sólo la franja central, como quien tacha una palabra en un
documento, y el corte cae cuando el trazo pasa por el centro. Se monta con la técnica de
`73` (mitad al final de A, mitad al arranque de B), **sin recodificar la unión**:

```
[N:v]scale=2600:-1,format=rgba[tach];
[bg][tach]overlay=x='1920-10273*(t-(DURA-0.22))':y=340:
          enable='gte(t,DURA-0.22)'[v]      # final de A
[bg][tach]overlay=x='1920-10273*(0.22+t)':y=340:enable='lt(t,0.22)'[v]   # inicio de B
```

`marca/tachado.png`: 2600×360 px, trazo de pincel `#E3120B` con los extremos deshilachados
y opacidad 1 (el papel es opaco, también el rojo).

| Variante | Coste | Fuerza | Uso |
|---|---|---|---|
| A · barrido de tinta | Recodifica el tramo | Máxima | El giro del episodio |
| B · trazo que tacha | Ninguno | Media | Tachar un dato, cerrar un capítulo menor |

## El tachado que no es transición

El mismo gesto sirve dentro de una escena, sin cambiar de plano: una cifra en pantalla
que se tacha en rojo mientras la voz da la real. Es el mismo PNG, 0,26 s de recorrido,
sobre el texto. Se distingue porque **el fondo no cambia**: eso lo hace un efecto de
documento (`62`), no una transición.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Usarlo dos o tres veces por episodio | Deja de ser firma y pasa a ser recurso; el giro del relato pierde su marca |
| Rojo distinto de `#E3120B` | La firma no se reconoce entre episodios |
| Tachar por encima de una cara | Se lee como censura o como agresión al retratado |
| Olvidar renderizar A con la cola de 0,44 s | El borde llega al final de A antes de tiempo y el último cuadro se congela |
| No poner `-t` (DURA+DURB) | `tpad` deja cola de más y el episodio se descuadra con la voz |
| Borde recto (sin las dos senoidales) | Parece un wipe de plantilla, no una pincelada |
| Bajarle la opacidad al rojo | La tinta se transparenta: doble exposición, no collage |

## Relacionado

`70` · `71` · `73` · `75` · `78` · `79` · `62`
