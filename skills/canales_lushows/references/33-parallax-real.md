# 33 · Parallax real

**Qué resuelve:** una foto de archivo con `zoompan` sigue siendo una foto plana que crece.
El parallax la convierte en un espacio: la figura y el fondo se mueven a velocidades
distintas y el cerebro deduce profundidad. Es el gesto que más eleva un plano de retrato
y el que más barato sale, porque el recorte de silueta ya está hecho.

---

## El principio

Al desplazarse una cámara, lo cercano recorre más ángulo que lo lejano. Se imita dando a
cada capa una velocidad propia:

| Capa | Velocidad relativa | Contenido |
|---|---|---|
| Fondo | 1,0× | La lámina construida por código, la ciudad, el edificio |
| Medio | 1,4-1,6× | Objetos, documentos, elementos de contexto |
| Figura | **1,6-2,4×** | El recorte de silueta del protagonista |

**Umbrales:** por debajo de **1,4×** no se percibe (has gastado render para nada). Por
encima de **3×** se lee como error de composición: la figura patina sobre el fondo.

Presupuesto: el fondo se queda en la banda baja del recorrido (**8%**) para que la figura,
al doble, siga dentro de lo razonable (**16%**).

---

## El agujero detrás de la figura

Si separas la figura del fondo, queda un hueco con la silueta recortada. En cuanto las
dos capas se desplazan una respecto a la otra, ese hueco asoma por los bordes.

Tres soluciones, por orden de coste:

1. **No mover tanto** — con un desplazamiento relativo por debajo de **25 px** el hueco
   no llega a asomar en un recorte de tamaño medio. Es el 80% de los casos
2. **Fondo ampliado y desenfocado** — se escala el fondo un 6% y se le aplica
   `gblur=sigma=0.9`. El desenfoque tapa el borde del hueco y además **es lo correcto
   ópticamente**: el fondo de un retrato está desenfocado
3. **Relleno real** — clonar el fondo sobre el hueco en el PNG antes de montar. Solo
   cuando el desplazamiento tiene que ser grande porque el plano dura mucho

---

## Implementación completa

Dos capas, 4,5 segundos, fondo al 8% y figura al 17%:

```bash
ffmpeg \
  -loop 1 -t 4.5 -i capa_fondo.png \
  -loop 1 -t 4.5 -i capa_figura.png \
  -filter_complex "
[0:v]scale=4320:-2,
     zoompan=z='1+0.0007*on':d=1:
             x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':
             s=1920x1080:fps=25,
     gblur=sigma=0.9[bg];

[1:v]format=rgba,
     scale=w='iw*(1+0.038*t)':h=-1:eval=frame:flags=bicubic[fg];

[bg][fg]overlay=x='(W-w)/2+120':y='(H-h)/2+90':format=auto,
        noise=alls=6:allf=t+u,
        format=yuv420p[v]
" -map "[v]" -r 25 -y plano.mp4
```

Qué hace cada pieza:

- **`zoompan` solo en el fondo.** La capa con alfa NO va por `zoompan`: el camino seguro
  para RGBA es `scale=eval=frame` + `overlay`
- **`scale=w='iw*(1+0.038*t)'`** — 3,8% por segundo × 4,5 s = 17% de crecimiento
- **`h=-1`** mantiene la proporción; `flags=bicubic` evita el aliasing del escalado por
  fotograma
- **`overlay` con `(W-w)/2`** — `overlay` reevalúa `w` cada fotograma, así que la figura
  crece desde su centro y no se desplaza sola
- **`noise` DESPUÉS del `overlay`** — el grano tiene que ser común a las dos capas. Si se
  aplica por separado, el collage se separa: son dos texturas distintas y se ve

## Parallax lateral (sin zoom)

Cuando el gesto es un travelling y no un empuje, las capas se desplazan en `x`:

```bash
[0:v]scale=4320:-2,
     zoompan=z='1.16':d=1:
             x='(iw-iw/zoom)*(0.34+0.16*clip((on/25)/4.5,0,1))':
             y='(ih-ih/zoom)*0.50':s=1920x1080:fps=25[bg];
[1:v]format=rgba[fg];
[bg][fg]overlay=x='860-46*clip(t/4.5,0,1)':y='210'
```

El fondo recorre 0,16 del margen; la figura recorre 46 px en dirección **contraria**.
Contrario, no igual: es lo que separa las capas de verdad. Relación efectiva ≈ 2,1×.

## Los remates que lo hacen creíble

| Remate | Valor | Por qué |
|---|---|---|
| Desenfoque del fondo | `gblur=sigma=0.6` a `1.2` | La profundidad de campo real |
| Grano común | `noise=alls=5` a `8`, `allf=t+u` | Une las dos capas en una sola imagen |
| Sombra bajo la figura | 8-14 px de desplazamiento, 40% de opacidad | Sin sombra, la figura flota |
| Contraste de la figura | +4% sobre el fondo | Lo cercano es más contrastado |
| Viñeta | `vignette=a=PI/5` | Cierra el cuadro y disimula el borde del hueco |

## Cuándo NO usarlo

- Cuando el recorte tiene alfa sucia: al moverlo sobre el fondo, el halo se hace visible.
  Auditar el recorte **sobre gris**, nunca sobre negro
- Cuando la figura y el fondo no empatan (luz, ángulo, grano). El parallax no arregla un
  collage mal casado: lo delata
- En planos de menos de 2 s: no da tiempo a percibir la separación

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `zoompan` sobre el PNG con alfa | Camino frágil con RGBA; la transparencia se pierde |
| Grano aplicado por capa | Dos texturas distintas: el collage se despega |
| Relación por debajo de 1,4× | Render gastado, efecto invisible |
| Relación por encima de 3× | La figura patina sobre el fondo |
| Figura y fondo en la misma dirección y velocidad parecida | Se lee como un zoom mal hecho |
| Sin desenfoque de fondo | El hueco de la silueta asoma por los bordes |

## Relacionado

`22` profundidad por capas · `23` empatar recorte y fondo · `30` catálogo de movimientos ·
`35` animar una foto fija · `37` cámara simulada
