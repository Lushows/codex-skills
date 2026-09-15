# 37 · Movimiento de cámara simulado

**Qué resuelve:** no hay cámara. Hay una imagen grande y una ventana que se pasea por
ella. Bien hecho, el espectador ve un travelling; mal hecho, ve una foto arrastrándose.
La diferencia está en tres cosas: margen suficiente, velocidad dentro de banda y una
curva que arranque y pare como para un brazo humano.

---

## El margen: la cuenta que hay que hacer antes

`zoompan` recorta una ventana de `iw/zoom` × `ih/zoom` y la escala a 1920x1080. El
desplazamiento disponible es:

```
x_max = iw · (1 - 1/z)
```

**A `z = 1,0` el margen es CERO.** Un travelling exige zoom base. Con fuente de 4320 px:

| Zoom base | Margen en `x` | Recorrido del cuadro |
|---|---|---|
| 1,08 | 320 px | 7,4% |
| 1,12 | 463 px | 12,0% |
| 1,18 | 659 px | 18,0% |
| 1,25 | 864 px | 25,0% |

El recorrido del cuadro es `x_recorrido · z / iw`. Por eso una panorámica larga no se
hace subiendo el zoom (pierdes resolución): se hace con **una fuente más ancha**, 7680 u
8640 px, y el zoom se queda en 1,10.

## Velocidad

| px/s en salida | Lectura |
|---|---|
| menos de 25 | Se percibe como estático |
| **40 - 90** | Travelling normal. La banda de trabajo |
| 90 - 140 | Urgencia, persecución |
| 150 - 400 | Barrido (3-6 fotogramas). Es un corte, no un movimiento |

Ejemplo: recorrido del 12% sobre 1920 px = 230 px en 4 s = **58 px/s**. Correcto.

**Duración mínima de un gesto de cámara: 2,5 s.** Por debajo no da tiempo a leerse como
cámara; se lee como que la imagen se corrió.

---

## Travelling lateral

Arranca y para dentro del plano, así que lleva `smoothstep` (`31`), no `easeOut`:

```bash
[0:v]scale=4320:-2,
     zoompan=z='1.18':d=1:
             x='(iw-iw/zoom)*(0.20+0.60*(clip((on/25)/4.0,0,1)*clip((on/25)/4.0,0,1)*(3-2*clip((on/25)/4.0,0,1))))':
             y='(ih-ih/zoom)*0.55':s=1920x1080:fps=25
```

Recorre del 20% al 80% del margen: **nunca de 0 a 1**. Llegar al borde exacto de la
imagen se ve, y además deja el plano sin sitio si hay que corregir el encuadre.

## Panorámica

Igual que el travelling pero sobre una lámina construida a propósito, mucho más ancha
que 16:9, y **sin zoom**: el zoom durante una panorámica delata que no hay cámara.

Aquí no se usa `zoompan` sino `crop` + `scale`: la ventana es de tamaño constante, así
que no hay reescalado por fotograma ni truncado a entero, y `crop` acepta `t` directo.

```bash
# lámina de 8640x2430: la ventana de 3456x1944 recorre casi toda la imagen en 6 s
[0:v]scale=8640:-2,
     crop=w=3456:h=1944:
          x='(in_w-3456)*(0.10+0.80*(clip(t/6.0,0,1)*clip(t/6.0,0,1)*(3-2*clip(t/6.0,0,1))))':
          y='(in_h-1944)/2',
     scale=1920:1080,fps=25
```

La ventana debe ser 16:9 sobre la fuente ampliada (3456x1944 = 1920x1080 × 1,8).

## Grúa

Vertical + zoom a la vez. Es el único gesto donde se permite mover dos ejes: la grúa
real hace exactamente eso.

```bash
zoompan=z='1.06+0.10*(1-pow(1-clip((on/25)/4.5,0,1),3))':d=1:
        x='(iw-iw/zoom)*0.50':
        y='(ih-ih/zoom)*(0.78-0.48*(1-pow(1-clip((on/25)/4.5,0,1),3)))':
        s=1920x1080:fps=25
```

Sube desde el 78% de altura hasta el 30% mientras se acerca un 10%. Se usa una vez o dos
por episodio: es un gesto grande y gastado pierde todo.

## Vértigo (dolly zoom)

No se puede hacer sobre una imagen plana — hace falta 3D. Pero con **dos capas** (`33`)
sale el efecto de verdad: el fondo se acerca mientras la figura se aleja a la misma tasa,
así que la figura conserva su tamaño y el fondo cambia detrás.

```bash
[0:v]scale=4320:-2,
     zoompan=z='1+0.14*clip((on/25)/3.5,0,1)':d=1:
             x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25[bg];
[1:v]format=rgba,
     scale=w='iw*(1.14-0.14*clip(t/3.5,0,1))':h=-1:eval=frame[fg];
[bg][fg]overlay=x='(W-w)/2':y='(H-h)/2+70'
```

Se reserva para un momento por episodio, y ese momento es siempre el mismo: cuando la
historia da la vuelta.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Travelling con `z=1.0` | Margen cero: `x` no puede moverse y el plano sale quieto |
| Recorrer el margen de 0 a 1 | Se ve el borde de la imagen y no queda aire para corregir |
| Panorámica con zoom simultáneo | Delata que no hay cámara |
| Velocidad por debajo de 25 px/s | El espectador no percibe el gesto |
| Gesto de cámara de 1,5 s | Se lee como que la imagen se corrió, no como travelling |
| `easeOut` en un travelling | Arranca de golpe; un brazo humano acelera |
| Subir el zoom para ganar recorrido | Se pierde resolución. Lo que se amplía es la fuente |
| Dos gestos de cámara en el mismo plano | Cámara indecisa. La grúa es la excepción |

## Relacionado

`30` catálogo de movimientos · `31` curvas de aceleración · `33` parallax real ·
`34` movimiento que narra · `38` ritmo del movimiento
