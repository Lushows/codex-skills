# 73 · Transición por elemento

**Qué resuelve:** un recorte cruza el cuadro y, al pasar, arrastra el cambio de escena.
Es la transición más versátil del canal: no necesita filtro nuevo, sólo un `overlay` con
la `x` en función de `t`.

---

## El principio: no hace falta tapar el cuadro, hace falta tapar la mirada

Hay dos maneras de esconder un corte con un objeto:

| Variante | Qué hace | Cuándo |
|---|---|---|
| **Cubrir** | El elemento tapa el 100% del cuadro en el fotograma del corte | Cambio de lugar duro; es lo que hace la hoja de papel (`71`) |
| **Arrastrar** | El elemento tapa sólo la zona donde está la atención (30-50% del cuadro) y el corte cae ahí | Casi siempre; más ligero y menos "efecto" |

La segunda funciona por enmascaramiento de atención: el ojo va persiguiendo el objeto,
no vigilando el fondo. Si en el fotograma del corte el objeto está sobre el punto de
interés, el cambio del resto del cuadro **no se percibe**.

## Elementos que sirven en este canal

| Elemento | Recurso | Recorrido | Duración |
|---|---|---|---|
| Maletín / portafolio | `recortes/maletin` | horizontal → | 0,36 s |
| Carpeta de expediente | `fx/expediente` | horizontal ← | 0,36 s |
| Fajo de billetes | `fx/fajo` | horizontal → | 0,32 s |
| Camión / avión de carga | `fx/camiones` | horizontal → | 0,44 s |
| Sello que baja y golpea | `fx/sello_decomiso` | vertical ↓ | 0,28 s |
| Bolígrafo rojo que tacha | `marca/tachado` | horizontal → | 0,44 s (`77`) |

Nunca sirve: un elemento pequeño (menos de 500 px de ancho), uno translúcido, ni uno que
el espectador no pueda identificar de un vistazo.

## Cómo se reparte entre las dos escenas

Igual que en `71`: **mitad en el final de A, mitad en el arranque de B**, así la unión
sigue siendo un corte duro y `concat -c copy` sigue valiendo. La continuidad depende de
una sola cuenta:

```
v   = (1920 + ancho_elemento) / D        # velocidad en px/s, constante
x_A(t) = 1920 - v * (t - (durA - D/2))   # desde t = durA - D/2 hasta el final de A
x_B(t) = 1920 - v * (D/2 + t)            # desde t = 0 hasta t = D/2 de la escena B
```

Con `D = 0,36 s` y un maletín de 900 px: `v = (1920+900)/0,36 = 7833 px/s`. En el
fotograma del corte `x = 510`, o sea el maletín ocupa de 510 a 1410 px: está justo
encima del centro del cuadro, que es donde vive la atención. Al final de su medio
segundo, `x = −900`: fuera del cuadro por la izquierda.

## El código

**Final de la escena A** (`durA` = duración de la escena, `D` = 0,36):

```
[N:v]scale=900:-1,format=rgba,
     rotate=0.05236:c=none:ow=rotw(0.05236):oh=roth(0.05236)[obj];
[bg][obj]overlay=x='1920-7833*(t-(DURA-0.18))':y='430+38*sin(6.0*t)':
         enable='gte(t,DURA-0.18)'[v]
```

**Arranque de la escena B:**

```
[N:v]scale=900:-1,format=rgba,
     rotate=0.05236:c=none:ow=rotw(0.05236):oh=roth(0.05236)[obj];
[bg][obj]overlay=x='1920-7833*(0.18+t)':y='430+38*sin(6.0*t)':
         enable='lt(t,0.18)'[v]
```

El `38*sin(6.0*t)` es lo que separa esto de un PNG deslizándose: un balanceo vertical de
±38 px hace que el objeto **pese**. Sin él se ve como una diapositiva de PowerPoint.

## Aceleración: cuándo sí y cuándo no

| Caso | Curva | Expresión |
|---|---|---|
| El objeto **cruza** y sale del cuadro | **lineal** | `x0 - v*t` |
| El objeto entra y **se queda** (no es transición) | ease-out | `x0+(x1-x0)*(1-pow(1-clip(t/D,0,1),3))` |
| El sello que **baja y golpea** | ease-in + rebote | `y0+(y1-y0)*pow(clip(t/D,0,1),2.4)` y 2 fotogramas de retroceso de 12 px |

Un objeto que cruza y frena en el medio delata que es un efecto. La física de lo que
cruza es constante; la de lo que llega, no.

## El sonido manda

El elemento sin sonido es un recorte moviéndose. Con `tr_whoosh` entrando **0,12 s antes**
de que el objeto asome (`75`), el cerebro lo lee como una masa que pasa. En el sello,
`dr_golpe` cae en el fotograma exacto del impacto, no antes.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| No recalcular `x_B(0)` a partir de `x_A(final)` | El objeto salta cientos de píxeles en el corte y se ve el truco |
| Objeto demasiado pequeño o transparente | No tapa la atención: el corte queda al descubierto |
| Frenar el objeto en el centro | Se lee como transición de plantilla, no como un objeto que pasa |
| Cruzar siempre en la misma dirección | A la tercera vez el episodio se vuelve mecánico (`78`) |
| Objeto que no tiene nada que ver con la historia | Un elemento sin explicar es ruido; si cruza, que sea algo del caso |
| Poner además un `xfade` debajo | Dos transiciones a la vez: se anulan y se nota la recodificación |

## Relacionado

`71` · `74` · `75` · `77` · `78` · `30` · `31`
