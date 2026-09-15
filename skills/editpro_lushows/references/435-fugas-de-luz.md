# 435 — Fugas de luz

> Una fuga de luz es luz que **no debería estar ahí**: entra por una rendija del cuerpo de la cámara,
> por el borde del chasis, por el lateral del objetivo. Por eso siempre viene **de un borde**, siempre
> tiene **una dirección**, y siempre es **cálida**. Una mancha de luz en el centro del cuadro no es una
> fuga: es una calcomanía.

`267`, §5.3, tiene la receta rápida — un óvalo cálido en una esquina con `screen` y opacidad animada —
con su aviso de "verifícalo, la expresión de opacidad no funciona en todas las versiones". Aquí está
verificada, corregida, y sobre todo **medida**, que es lo que cambia cómo se dosifica.

---

## 1. Las tres reglas físicas

| Regla | Por qué | Qué pasa si se rompe |
|---|---|---|
| **Entra por un borde** | la luz se cuela por una junta del cuerpo | mancha central = capa pegada |
| **Tiene dirección** | viene de un lado y se apaga hacia dentro | resplandor simétrico = filtro de aplicación |
| **Es cálida** | la película se vela en naranja-rojo | fuga azul = error de color, no de cámara |

Y la cuarta, que es de montaje y no de física: **una fuga ocupa un instante, no un plano.** Entra en
0,2 s, vive 0,3 s y se va en 0,3 s. Una fuga permanente es un grado mal hecho.

---

## 2. La construcción correcta: el PNG una vez, el movimiento con `fade`

La fuga no se genera por fotograma. Se genera **una vez** como PNG con alfa y se anima con `fade`, que
cuesta cero:

```bash
# 1) la rampa, una sola vez
ffmpeg -y -f lavfi -i "color=c=0xFF7A3C:s=1080x1920" \
  -vf "format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='210*exp(-pow(X/240\,2))'" \
  -frames:v 1 fuga.png

# 2) se monta y se anima
ffmpeg -y -i plano.mp4 -loop 1 -framerate 25 -t 4 -i fuga.png -filter_complex "\
[1:v]format=rgba,fade=t=in:st=1.60:d=0.20:alpha=1,fade=t=out:st=1.95:d=0.30:alpha=1[f];\
[0:v][f]overlay=0:0[o]" -map "[o]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p fuga.mp4
```

**Dos fallos mudos que hay que conocer, los dos verificados:**

> 🔴 **`format=rgba` va ANTES de `geq`, no después.** Si lo pones detrás, `geq` no tiene plano alfa donde
> escribir, la expresión `a=` se descarta **sin un solo aviso**, y el PNG sale RGBA pero **opaco**.
> Comprobado con `alphaextract`: con `format=rgba` detrás, el alfa mide `YMIN=255 YAVG=255 YMAX=255`
> — plano y opaco. Con `format=rgba` delante: `YMIN=0 YAVG=42,5 YMAX=210`, que es la rampa. El resultado
> del primero es un rectángulo naranja que tapa el vídeo.
>
> La comprobación, que cabe en una línea:
> ```bash
> ffmpeg -i fuga.png -vf "format=rgba,alphaextract,signalstats,metadata=print" -f null -
> ```

> 🔴 **Un PNG entra como UN fotograma.** Sin `-loop 1 -framerate 25 -t N`, el `fade` no tiene sobre qué
> correr y la fuga no aparece ni se anima. En la primera prueba de este módulo, esa omisión dio un Δ de
> luminancia de **+0,02 niveles**: el efecto sencillamente no ocurrió (`432`).

---

## 3. La medición que hace la diferencia: la banda, no el cuadro

Una fuga es **local**. Medirla sobre el fotograma entero da un número que no sirve para dosificar.
Medido sobre el render anterior, con la fuga entrando por la izquierda:

| Zona medida | Base Y | Pico Y | Δ |
|---|---|---|---|
| **Cuadro completo** | 68,06 | 81,67 | **+13,61** |
| **Banda izquierda (25 % del ancho)** | 66,45 | 116,18 | **+49,73** |
| Banda derecha (25 % del ancho) | 53,35 | 53,37 | +0,02 |

**La media del cuadro subestima la fuga 3,7 veces.** Si dosificas con el +13,6 vas a poner el triple de
lo que crees. Y la banda de la derecha confirma lo que se espera de una fuga bien hecha: no toca el lado
contrario.

El arnés es un `crop` delante del `signalstats`:

```bash
ffmpeg -hide_banner -i fuga.mp4 \
  -vf "crop=iw/4:ih:0:0,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -
```

**Dosis de trabajo, en la banda afectada: Δ de +25 a +50.** Por debajo de +20 no se lee como fuga; por
encima de +70 tapa la imagen y se convierte en un flash de color.

---

## 4. Para qué sirven de verdad

Tres trabajos, y ninguno es decorar:

1. **Tapar una costura.** Es el uso bueno. Un corte que no empata, un recorte con un borde feo, un salto
   de color entre dos planos: la fuga pasa por encima en el fotograma exacto y el ojo se va con ella.
   Es el mismo oficio que las partículas de `267`, §1, función 3.
2. **Marcar el paso del tiempo.** Entre dos bloques, una fuga hace de "más tarde" sin cartel.
3. **Dar textura a material demasiado limpio.** Metraje generado o gráficos planos: una fuga muy suave
   les devuelve la sensación de que pasaron por una cámara.

**Dónde no:** producto sobre fondo blanco, comida (`340`), cualquier plano donde haya texto en el borde
por el que entra la fuga, y piezas de marca donde el color de la fuga pelea con el de la identidad
(`224`).

---

## 5. Variantes que valen la pena

- **Fuga por el borde superior**, cambiando `X` por `Y` en la expresión de alfa. Se lee distinto: la
  lateral es "se abrió el chasis", la superior es "entró sol".
- **Fuga con desplazamiento.** En vez de sólo aparecer, que entre moviéndose:
  `overlay=x='-200+260*t':y=0`. Cuesta lo mismo y se ve mucho mejor.
- **Fuga sobre el corte.** Si cae exactamente en un corte, tapa el empalme y es la versión elegante del
  flash de `53`. Ahí sí puede llevar sonido; como recurso suelto en medio de un plano, no lo necesita —
  y en eso se diferencia del destello, que **siempre** lo lleva (`433`).
- **Fuga grabada.** La mejor y la más barata: apunta el móvil a una lámpara y pasa el dedo o un CD por
  delante del objetivo. Sale sobre negro y se monta en `screen` (`267`, §4.1).

---

## Errores frecuentes

- **`format=rgba` después de `geq`.** El alfa sale opaco sin avisar y la fuga tapa el vídeo.
- **Meter el PNG sin `-loop 1 -framerate N -t N`.** El `fade` no corre y el efecto no ocurre (+0,02).
- **Dosificar con la media del cuadro.** Subestima la fuga 3,7 veces; se mide la banda con `crop`.
- **Fuga en el centro.** No es una fuga, es una mancha. Entra por un borde.
- **Fuga fría.** El velado de la película es naranja-rojo. El azul se lee como error de balance.
- **Fuga permanente.** Un plano entero con fuga es un grado mal hecho. Entra, vive y se va en menos de
  un segundo.
- **Renderizar la rampa con `geq` fotograma a fotograma.** Minutos por plano. Una vez, como PNG.
- **Fuga sobre texto en el borde.** Se come la legibilidad justo donde hace falta (`376`).
- **Ponerle sonido de flash.** No es un destello; una fuga muda es correcta.

---

## Relacionado

- `267` — la receta original de fuga y viñeta de color, y el catálogo de elementos de luz.
- `434` — bloom y halación: luz que sangra desde dentro de la imagen, no desde el borde.
- `430`, `433` — el destello: evento breve, con sonido obligatorio. Una fuga no es eso.
- `432` — el arnés de medición, aquí con `crop` delante.
- `53` — la fuga puesta sobre un corte es pariente del flash de transición.
- `224` — luz de color y neón: elegir el color de la fuga cuando hay marca de por medio.
- `57`, `66` — glitch y textura, viñeta y grano: los vecinos de este efecto.
