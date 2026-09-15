# 84 — Keyframes y curvas

**Qué resuelve:** por qué tu texto que entra, tu logo que aparece y tu personaje que sube **se ven
baratos** aunque los colores y la tipografía estén bien. La respuesta casi siempre es una sola: el
movimiento es **lineal**. Este módulo explica qué es una curva de animación, por qué el ojo humano
odia el movimiento uniforme, y cómo se hacen curvas de verdad en ffmpeg con expresiones.

---

## 1. Qué es un keyframe y qué es una curva

> **Keyframe (fotograma clave):** un punto donde tú decides el valor de algo. "En el segundo 3 el logo
> está fuera de cuadro; en el segundo 3,5 está en su sitio." Esos son dos keyframes.

> **Interpolación:** cómo se rellenan los fotogramas de en medio. Entre el 3 y el 3,5 hay 12 fotogramas
> y alguien tiene que decidir dónde está el logo en cada uno.

> **Curva de animación (easing):** la regla de ese relleno. Si es una línea recta, el logo avanza la
> misma distancia en cada fotograma: **movimiento lineal**. Si es una curva, avanza distinto: arranca
> lento y frena, o arranca rápido y se demora en llegar.

**La curva es la personalidad del movimiento.** Dos animaciones con los mismos keyframes y distinta
curva se sienten como dos marcas diferentes.

---

## 2. Por qué el movimiento lineal se ve barato

Nada en el mundo físico se mueve a velocidad constante desde el reposo. Una puerta que se abre acelera y
frena. Tu mano al alcanzar un vaso arranca lenta, acelera y desacelera al llegar. Un carro no pasa de
0 a 60 instantáneamente y luego se detiene en seco.

Cuando algo en pantalla se mueve **linealmente**, el cerebro registra: *esto no obedece a la física.*
No lo piensa con palabras — lo siente. Y lo que siente es "artificial", "de plantilla", "hecho por
alguien que no sabe".

| | Lineal | Con curva |
|---|---|---|
| Cómo arranca | de golpe, a velocidad plena | desde cero, acelerando |
| Cómo llega | se detiene en seco | frenando |
| Cómo se lee | mecánico, PowerPoint 2003 | físico, intencional, caro |
| Costo de arreglarlo | — | una línea de expresión |

> **La regla más rentable de todo el bloque 8:** cambiar tus movimientos lineales por movimientos con
> frenado sube la percepción de calidad más que cualquier efecto que puedas comprar. Cuesta cinco
> minutos.

---

## 3. Las curvas que de verdad usas (y para qué sirve cada una)

Con cuatro te alcanza para el 95% del trabajo de marca:

| Curva | Cómo se siente | Para qué |
|---|---|---|
| **Ease out** (frena al llegar) | decidido, seguro, limpio | **la que más usas.** Todo lo que ENTRA |
| **Ease in** (acelera al irse) | se va, desaparece | todo lo que SALE |
| **Ease in-out** (arranca y frena) | elegante, suave, premium | movimientos largos, empujes de cámara |
| **Ease out back** (se pasa y vuelve) | vivo, juguetón, con energía | logos, personajes, texto de impacto |

La quinta que existe pero se usa mal: el **rebote** (bounce). Da infantil. Úsalo solo si la marca es
explícitamente juguetona, y con un solo rebote, nunca tres.

### La regla de oro de la dirección

- **Lo que entra:** ease **out**. Llega y frena. Se siente que llegó a su lugar.
- **Lo que sale:** ease **in**. Acelera y se va. Se siente que se fue con decisión.

Al revés se siente mal y nadie sabe explicar por qué: algo que entra acelerando parece que se le
escapó de las manos a alguien.

---

## 4. Cómo se hace una curva en ffmpeg

ffmpeg no tiene "keyframes" como un editor visual. Tiene algo mejor y peor a la vez: **expresiones
matemáticas** que se evalúan en cada fotograma. Peor porque hay que escribirlas; mejor porque puedes
hacer cualquier curva que se te ocurra.

### El patrón base

Todo se construye igual, en dos pasos:

1. **Calcular el progreso** `p`: un número que va de 0 a 1 durante la animación.
2. **Aplicarle la curva** y usar el resultado para interpolar entre el valor inicial y el final.

```
p  = clip((t - inicio) / duracion, 0, 1)
e  = <formula de la curva aplicada a p>
valor = A + (B - A) * e
```

En expresiones de ffmpeg se guarda `p` en una variable con `st(0, ...)` y se lee con `ld(0)`. El
separador `;` evalúa varias cosas y devuelve la última.

### Las fórmulas, listas para copiar

Con `P` = `ld(0)` (el progreso ya calculado y recortado entre 0 y 1):

| Curva | Fórmula |
|---|---|
| Lineal (la que NO quieres) | `P` |
| Ease out cúbico | `1-pow(1-P,3)` |
| Ease out fuerte (quinto) | `1-pow(1-P,5)` |
| Ease in cúbico | `pow(P,3)` |
| Ease in-out cúbico | `if(lt(P,0.5), 4*pow(P,3), 1-pow(-2*P+2,3)/2)` |
| Ease out back (sobre-impulso) | `1+2.70158*pow(P-1,3)+1.70158*pow(P-1,2)` |
| Suave simple (coseno) | `(1-cos(PI*P))/2` |

La del coseno es la más corta de escribir y da un in-out decente. Si tienes prisa, esa.

---

## 5. Ejemplos reales

### Logo que sube y frena (ease out cúbico)

Entra en el segundo 1,0, tarda 0,5 s, va desde fuera de cuadro hasta 200 px del borde inferior.

```bash
ffmpeg -i base.mp4 -i logo.png \
  -filter_complex "[1:v]scale=-1:180,format=rgba[lg];\
[0:v][lg]overlay=x=(W-w)/2:\
y='st(0,clip((t-1.0)/0.5,0,1)); H - (H-(H-h-200))*(1-pow(1-ld(0),3))'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Compáralo con la versión lineal (cambia `1-pow(1-ld(0),3)` por `ld(0)`) y exporta las dos. La diferencia
es brutal y es una sola línea.

### Personaje con sobre-impulso (ease out back)

Sube, se pasa un poco de su posición, y vuelve. Esto es lo que hace que un motion se sienta "vivo".

```bash
ffmpeg -i base.mp4 -i pj.png \
  -filter_complex "[1:v]scale=-1:620,format=rgba[pj];\
[0:v][pj]overlay=x=W-w-56:\
y='st(0,clip((t-3.0)/0.45,0,1)); \
st(1, 1+2.70158*pow(ld(0)-1,3)+1.70158*pow(ld(0)-1,2)); \
H - (H-(H-h-470))*ld(1)':enable='gte(t,3.0)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

`st(1, ...)` guarda la curva ya calculada en el registro 1 para no repetir la fórmula. El sobre-impulso
del `back` estándar es de ~10%. Para marcas serias, bájalo cambiando `2.70158` por `1.6` y `1.70158`
por `0.9`: queda un guiño en vez de un salto.

### Entrada desde el lado con salida (curva en cada extremo)

```bash
-filter_complex "[1:v]scale=-1:180,format=rgba[lg];\
[0:v][lg]overlay=y=H-h-200:\
x='if(lt(t,4.2), \
   st(0,clip((t-1.0)/0.5,0,1)); -w + ((W-w)/2+w)*(1-pow(1-ld(0),3)), \
   st(0,clip((t-4.2)/0.35,0,1)); (W-w)/2 + (W-(W-w)/2)*pow(ld(0),3))'"
```

Entra con ease **out** (frena), sale con ease **in** (acelera). La salida dura 0,35 s, menos que la
entrada de 0,5 s: **lo que sale siempre sale más rápido de lo que entró.**

### Opacidad con curva: usa `fade`, no expresiones

Para transparencia no hace falta pelear con expresiones. El filtro `fade` con `alpha=1` ya trae una
curva razonable:

```bash
[1:v]format=rgba,fade=t=in:st=1.0:d=0.35:alpha=1,fade=t=out:st=4.2:d=0.25:alpha=1[lg]
```

### Escala animada

El filtro `scale` acepta expresiones si le pones `eval=frame`:

```bash
[1:v]format=rgba,scale=w='iw*(0.85+0.15*(1-pow(1-clip(t/0.4,0,1),3)))':h=-2:eval=frame[lg]
```

Entra creciendo del 85% al 100% con frenado. **Ojo:** cambiar el tamaño en cada fotograma es pesado y
algunas compilaciones se quejan. Si te da guerra, prerrenderiza el elemento como video con alfa (`81`)
y superpónlo ya animado.

---

## 6. Los tiempos: cuánto debe durar cada cosa

Las duraciones importan tanto como las curvas. Números que funcionan en video social:

| Movimiento | Duración | Por qué |
|---|---|---|
| Entrada de texto (golpe) | 0,12 – 0,22 s | tiene que sentirse instantáneo pero no seco |
| Entrada de logo o gráfico | 0,35 – 0,55 s | es un elemento con peso |
| Entrada de personaje | 0,40 – 0,60 s | tiene cuerpo, tarda |
| Salida de cualquier cosa | **60–70% de su entrada** | irse siempre es más rápido |
| Empuje de cámara / parallax | 2 – 5 s | tiene que ser imperceptible (`83`) |
| Anticipación (retroceso previo) | 0,08 – 0,14 s | más de eso ya se ve como error |

**El error de tiempos más común:** entradas de 1 segundo. Se sienten eternas. En video vertical, casi
nada debería tardar más de medio segundo en llegar.

---

## 7. Anticipación: el detalle que separa el motion bueno del profesional

> **Anticipación:** antes de moverse hacia adelante, el elemento hace un movimiento pequeño **hacia
> atrás**. Como el pitcher que echa el brazo atrás antes de lanzar.

Es uno de los 12 principios de Disney (ver `85`) y sirve para dos cosas: hace que el movimiento se sienta
físico, y **avisa al ojo** dónde va a pasar algo antes de que pase, así el espectador no se lo pierde.

```bash
-filter_complex "[1:v]scale=-1:180,format=rgba[lg];\
[0:v][lg]overlay=x=(W-w)/2:\
y='st(0,clip((t-1.0)/0.12,0,1)); st(1,clip((t-1.12)/0.42,0,1)); \
if(lt(t,1.12), \
   (H-h-200) + 26*(1-cos(PI*ld(0)))/2, \
   (H-h-200) + 26 - (26+ (H-(H-h-200)))*0 - 26*(1-pow(1-ld(1),3)))'"
```

En cristiano: durante 0,12 s el logo baja 26 píxeles (se agacha), y después sube a su sitio con frenado.
Se ve como si tomara impulso.

Para elementos pequeños, 20–30 px de anticipación. Para elementos grandes, 40–60 px. Si te pasas, parece
que el elemento se cayó.

---

## 8. Arcos: nada se mueve en línea recta

Otro principio de Disney que cambia mucho: **las cosas vivas se mueven en arco**, no en línea recta. Un
elemento que entra desde abajo perfectamente vertical se ve mecánico. Si además se desplaza un poco de
lado mientras sube, se ve natural.

```bash
overlay=\
x='(W-w)/2 + 40*sin(PI*clip((t-1.0)/0.5,0,1))':\
y='st(0,clip((t-1.0)/0.5,0,1)); H-(H-(H-h-200))*(1-pow(1-ld(0),3))'
```

El `40*sin(PI*p)` hace que la X se desvíe 40 px hacia un lado a la mitad del recorrido y vuelva al
centro al final. El resultado es una **curva**, no una recta. Es invisible conscientemente y se siente
inmediatamente.

---

## 9. Verificar una curva sin verla correr

Como no puedes reproducir el video, saca la tira de fotogramas de la animación y **mira el espaciado**:

```bash
ffmpeg -ss 0.9 -i salida.mp4 -t 0.8 -vf "fps=25,scale=200:-1,tile=10x2" -frames:v 1 curva.png
```

Lo que buscas en la tira:

- **Lineal:** el elemento avanza la misma distancia entre cada cuadrito. Espaciado uniforme = mal.
- **Ease out:** los primeros saltos son grandes y los últimos, pequeñísimos. Los últimos 3–4 cuadritos
  se ven casi iguales. **Eso es lo correcto.**
- **Ease out back:** en algún cuadrito el elemento está **más allá** de su posición final y luego vuelve.
- **Anticipación:** los primeros 2–3 cuadritos van en dirección contraria.

Si la tira te muestra espaciado uniforme, tu curva no se aplicó: casi siempre por un paréntesis mal
cerrado en la expresión (ffmpeg no siempre falla, a veces evalúa raro y sigue).

---

## Errores comunes

1. **Movimiento lineal.** El error madre. Todo lo demás de este módulo existe para arreglar esto.
2. **Aplicar la misma curva a la entrada y a la salida.** Entra con ease out, sale con ease in. Al revés
   se siente como si el elemento se le hubiera escapado a alguien.
3. **Salidas tan largas como las entradas.** La salida va al 60–70% del tiempo de la entrada. Siempre.
4. **Entradas de 1 segundo.** En vertical se sienten eternas. Medio segundo es el techo para casi todo.
5. **Sobre-impulso en todo.** El `back` es sabroso y por eso se abusa. Uno o dos elementos por video, no
   todos.
6. **Rebote de tres saltos.** Infantil. Un rebote, si acaso, y solo si la marca lo pide.
7. **Anticipación exagerada.** 26 px se lee como impulso; 120 px se lee como que se cayó.
8. **Movimiento perfectamente vertical u horizontal.** Nada vivo se mueve en línea recta. Métele arco.
9. **Olvidar `clip(...,0,1)` en el progreso.** Sin recortar, la fórmula sigue calculando después del
   final y el elemento se va de cuadro o hace cosas raras.
10. **Paréntesis mal cerrado en la expresión.** ffmpeg a veces no falla, solo evalúa mal. Si el
    movimiento no se ve como esperabas, revisa paréntesis antes que cualquier otra cosa.
11. **Confiar en que se aplicó sin verificar.** Saca la tira de fotogramas y mira el espaciado. Toma
    diez segundos.
12. **Animar la escala con `scale` sin `eval=frame`.** Se evalúa una sola vez al inicio y no pasa nada.

---

## Checklist

Antes de dar por buena una animación:

- [ ] **Ningún movimiento es lineal.** Todos tienen curva.
- [ ] Lo que entra usa **ease out**; lo que sale usa **ease in**.
- [ ] La salida dura **60–70%** de lo que dura la entrada.
- [ ] Las duraciones respetan la tabla: texto 0,12–0,22 s / logo 0,35–0,55 s / personaje 0,40–0,60 s.
- [ ] El progreso está recortado con `clip(...,0,1)`.
- [ ] Los elementos importantes tienen **anticipación** (0,08–0,14 s, 20–60 px según tamaño).
- [ ] Los recorridos largos van en **arco**, no en línea recta.
- [ ] El sobre-impulso está en **uno o dos elementos**, no en todos.
- [ ] Saqué la **tira de fotogramas** y el espaciado confirma la curva (últimos cuadritos casi iguales).
- [ ] Revisé paréntesis en cada expresión larga.
- [ ] Si animé escala, usé `eval=frame` o prerrendericé el elemento con alfa.
