# 35 · Animar una foto fija

**Qué resuelve:** el canal se hace con material que no se mueve. Una foto puesta tal cual
durante 3 segundos no es "un plano tranquilo": son **75 fotogramas idénticos**, y eso el
espectador lo lee como que el video se congeló.

---

## Por qué se lee como avería

A 25 fps, tres segundos de imagen quieta son 75 fotogramas byte a byte iguales. Pasan
tres cosas, en este orden:

1. **A los 0,6-0,8 s** el ojo terminó de leer la imagen y busca el siguiente cambio
2. **A los 1,5 s** el espectador comprueba si el video avanza: mira la barra o toca la
   pantalla. Ahí ya lo perdiste
3. **Si el plano anterior se movía**, no se lee como pausa: se lee como fallo técnico

Agravante del formato: en móvil, con autoplay y sin sonido en la primera pasada, la
imagen quieta es indistinguible de un video que no cargó.

**El suelo, sin excepciones: ningún plano por debajo de 6% de recorrido, y ningún tramo
de más de 2 s sin un evento.**

---

## Forma 1 · Cámara sobre el plano

Es el suelo, no la solución. Un `zoompan` con el 8-12% de recorrido y una curva
(`31`) ya saca la lámina del estado de foto:

```bash
[0:v]scale=4320:-2,
     zoompan=z='1+0.10*(1-pow(1-clip((on/25)/3.0,0,1),3))':d=1:
             x='(iw-iw/zoom)*0.55':y='(ih-ih/zoom)*0.42':
             s=1920x1080:fps=25
```

Resuelve el problema técnico —ya no hay fotogramas idénticos— pero no el narrativo:
sigue siendo una lámina creciendo. Nunca basta por sí sola.

## Forma 2 · Separar en capas

La buena. Se recorta la figura (rembg + limpieza de alfa) y se montan dos o tres capas a
velocidades distintas — implementación en `33`. Además de profundidad, permite que
**entren elementos entre las capas**: un rótulo por detrás de la figura y por delante
del fondo. Ahí el plano deja de ser una foto y pasa a ser un espacio. Coste: 4-8 minutos
por plano con el recorte incluido; se reserva para los planos que sostienen el episodio.

## Forma 3 · Cambio de estado dentro del plano

Que algo **cambie**, no solo que se desplace. Es lo que sube la densidad de eventos
(`10`) sin añadir cortes:

- **Elementos que entran y salen encima** — dos o tres datos, un rótulo, un sello. Es la
  vía principal: cada entrada es un evento
- **Grano temporal** — imprescindible. El grano quemado en el PNG es peor que nada: se ve
  como un escaneo sucio y congelado. El grano tiene que moverse:

  ```
  noise=alls=7:allf=t+u
  ```

  `t` lo hace temporal (cambia cada fotograma), `u` lo hace uniforme. Valores 5-9; por
  encima de 12 ensucia los negros

- **Luz que respira** — una rampa mínima de brillo, imperceptible como efecto pero que
  cambia todos los píxeles:

  ```
  eq=brightness='0.018*sin(2*PI*t/6)':contrast=1.02:eval=frame
  ```

- **Viñeta que se cierra** — acompaña al empuje y cierra el cuadro:

  ```
  vignette=a='PI/5+0.02*sin(2*PI*t/5)':eval=frame
  ```

- **Cambio de estado del contenido** — la cifra que pasa de un valor a otro, el mapa que
  se dibuja, la barra que crece (`36`). El más potente de todos

**Orden en la cadena:** movimiento → color/luz → composición de elementos → grano →
viñeta. El grano y la viñeta van al final para que afecten a todas las capas por igual.

---

## El plano completo

```bash
ffmpeg -loop 1 -t 3.6 -i lamina.png -loop 1 -t 3.6 -i dato.png -filter_complex "
[0:v]scale=4320:-2,
     zoompan=z='1+0.10*(1-pow(1-clip((on/25)/3.6,0,1),3))':d=1:
             x='(iw-iw/zoom)*0.55':y='(ih-ih/zoom)*0.42':s=1920x1080:fps=25,
     eq=brightness='0.018*sin(2*PI*t/6)':contrast=1.02:eval=frame[bg];
[1:v]format=rgba,fade=t=in:st=1.10:d=0.24:alpha=1,
     fade=t=out:st=3.10:d=0.20:alpha=1[el];
[bg][el]overlay=x='1240-80*pow(1-clip((t-1.10)/0.30,0,1),3)':y='300',
        noise=alls=7:allf=t+u,
        vignette=a='PI/5',format=yuv420p[v]
" -map "[v]" -r 25 -y plano.mp4
```

## Auditoría: detectar los congelados

`mpdecimate` descarta fotogramas duplicados. Si el conteo baja, hay imagen quieta:

```bash
# fotogramas reales
ffprobe -v error -count_frames -select_streams v:0 \
        -show_entries stream=nb_read_frames -of csv=p=0 plano.mp4

# fotogramas que sobreviven al descarte de duplicados
ffmpeg -i plano.mp4 -vf mpdecimate -f null - 2>&1 | grep -o "frame=[ ]*[0-9]*" | tail -1
```

Diferencia por debajo del **2%**: correcto. Por encima del 10%: hay tramos congelados y
hay que localizarlos con la grilla de fotogramas.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Foto quieta "porque el momento pide calma" | 75 fotogramas idénticos; se lee como avería, no como calma |
| Grano quemado en el PNG | Escaneo sucio y congelado: peor que sin grano |
| Solo `zoompan`, sin capas ni elementos | Deja de estar congelado pero sigue siendo una lámina |
| Grano por capa en vez de al final | Las capas se despegan visualmente |
| Rampa de luz demasiado grande | Se ve el efecto; el límite es 0,02 de brillo |
| Recorrido por debajo del 6% | Técnicamente se mueve, perceptualmente no |

## Relacionado

`10` densidad de eventos · `11` el hueco prohibido · `30` catálogo de movimientos ·
`33` parallax real · `36` contadores y cifras animadas
