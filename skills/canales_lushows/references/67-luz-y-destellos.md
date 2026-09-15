# 67 · Luz y destellos

**Qué resuelve:** meter luz sin caer en lo barato. Hay exactamente cuatro recursos de
luz en este canal — flash de archivo, foco, halo y proyector — y todos son **sustractivos
o mínimos**. El destello que se añade encima de la imagen es lo que hace que un vídeo se
vea de plantilla (`68`).

---

## La regla: la luz no se añade, se quita

Un foco no se hace poniendo luz en el centro: se hace **oscureciendo todo lo demás**. Es
como funciona la luz de verdad y es lo que separa un plano dirigido de un plano con un
filtro encima. Sólo el flash de archivo es aditivo, y dura menos de un cuarto de segundo.

---

## 1 · Flash de archivo

Simula el fogonazo de una cámara de prensa. Es el único destello legítimo, y sólo cuando
en pantalla hay **algo fotografiable**: un detenido, una rueda de prensa, un retrato.

Dos capas que hacen cosas distintas:

```
# a) el levantón de exposición: brillo real, 3 fotogramas
eq=brightness='if(between(t,3.20,3.32),0.26,0)':eval=frame

# b) el rebote: un PNG blanco que se apaga en 0,22 s
[1:v]format=rgba,fade=t=out:st=3.20:d=0.22:alpha=1[fl];
[bg][fl]overlay=x=0:y=0:enable='between(t,3.20,3.42)'
```

El PNG blanco va al **44-55% de alfa**, nunca al 100%: un blanco pleno corta el vídeo en
dos y el ojo pierde el hilo. `eval=frame` es obligatorio en `eq`, o la expresión se
evalúa una sola vez al arrancar y no pasa nada.

**Duración total 0,12-0,22 s.** Y como mucho **tres flashes** en un episodio de 90 s: el
cuarto ya es un recurso, no un acento.

Si hay flash, hay sonido de flash (`81`). Un fogonazo mudo se lee como error de render.

---

## 2 · Foco (viñeta selectiva)

Un PNG **oscuro con un agujero**, del tamaño del lienzo, encima de todo. No lleva luz:
lleva sombra alrededor.

```html
<div style="position:relative;width:1920px;height:1080px">
  <div style="position:absolute;inset:0;background:radial-gradient(
       34% 46% at 38% 44%, rgba(0,0,0,0) 0%, rgba(0,0,0,.34) 52%,
       rgba(0,0,0,.78) 100%)"></div>
</div>
```

El centro del agujero va **donde está el recorte que sostiene la frase**, y se mueve con
él si el recorte deriva. Un foco fijo mientras el sujeto se desplaza señala al vacío.

Se monta como cualquier elemento, siempre el **último** de la escena, con `dura` larga y
`entrada: fade`. Nunca por encima del texto: un rótulo dentro de la zona oscura pierde
contraste y deja de leerse (`46`).

---

## 3 · Halo detrás del recorte

Un gradiente radial cálido **detrás** de la figura, para despegarla del fondo sin
recortar más ni subir el contraste.

```html
<div style="width:900px;height:900px;background:radial-gradient(50% 50% at 50% 50%,
     rgba(232,197,71,.30) 0%, rgba(232,197,71,.10) 46%, rgba(232,197,71,0) 72%)"></div>
```

En la tabla del guion visual va **antes** que el recorte, con la misma ancla y el mismo
`x`/`y` corregido para quedar centrado, y un ancho 1,6-2,0 veces mayor:

```python
{"r": "halo",       "ancla": "detenido", "offset": -0.22, "dura": 2.6,
 "x": "W*0.02", "y": "H*0.10", "w": 900, "entrada": "fade"},
{"r": "cara_ovalo", "ancla": "detenido", "offset": -0.15, "dura": 2.4,
 "x": "W*0.08", "y": "H*0.24", "w": 480, "entrada": "izq", "rot": -1.4},
```

**Alfa máximo 0,30.** Por encima deja de ser separación y se convierte en resplandor de
plantilla. Y el halo es del color de la escena (`51`), no siempre dorado: un halo dorado
en una escena verde delata que es un adorno pegado.

---

## 4 · Proyector

Para las escenas de sala, archivo o proyección. Un haz trapezoidal con polvo dentro:

```html
<div style="position:relative;width:1920px;height:1080px">
  <div style="position:absolute;left:0;top:0;width:1920px;height:1080px;
       clip-path:polygon(46% 0%, 54% 0%, 88% 100%, 12% 100%);
       background:linear-gradient(180deg, rgba(255,244,214,.20), rgba(255,244,214,.03) 78%,
       rgba(255,244,214,0))"></div>
  <svg style="position:absolute;inset:0;mix-blend-mode:screen;opacity:.20"
       viewBox="0 0 1920 1080" preserveAspectRatio="none">
    <filter id="polvo"><feTurbulence type="fractalNoise" baseFrequency="0.9"
      numOctaves="1" seed="3"/><feColorMatrix type="saturate" values="0"/></filter>
    <rect width="1920" height="1080" filter="url(#polvo)" clip-path="none"/></svg>
</div>
```

El parpadeo se hace con **dos PNG** (haz fuerte y haz débil) alternados, no con una
opacidad animada:

```
[bg][fuerte]overlay=enable='lt(mod(t*7,1),0.5)*between(t,12.0,18.4)'[v1];
[v1][debil] overlay=enable='gte(mod(t*7,1),0.5)*between(t,12.0,18.4)'
```

7 Hz es un parpadeo de proyector creíble. La diferencia entre los dos estados debe ser de
**un 8-12% de alfa**: si se nota el salto, es un estroboscopio.

## Lo que no entra nunca

Lens flare anamórfico, rayos de sol (*god rays*) de plantilla, partículas doradas
flotando, brillo tipo *bloom* sobre todo el cuadro, destellos en las esquinas del texto.
Los sustitutos están en `68`.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Foco hecho con luz añadida en vez de sombra alrededor | Se ve el círculo del gradiente: filtro, no dirección |
| Flash sin `eval=frame` en `eq` | La expresión se evalúa una vez: no pasa nada |
| Flash blanco al 100% | Corta el vídeo en dos y se pierde el hilo |
| Más de tres flashes en 90 s | Deja de ser acento y se vuelve muletilla |
| Flash mudo | Se lee como error de render |
| Halo por encima del recorte | Lo empaña en vez de separarlo |
| Halo por encima de 0,30 de alfa | Resplandor de plantilla |
| Foco fijo con el sujeto en movimiento | Señala al vacío |
| Foco por encima del texto | El rótulo pierde contraste y no se lee |
| Parpadeo de proyector con salto visible | Estroboscopio, no proyector |

## Relacionado

`53` luz y viñeta del fondo · `51` paleta por escena · `68` la lista negra · `81` sintetizar el sonido del flash · `21` peso visual
