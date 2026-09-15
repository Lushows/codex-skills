# 53 · Luz y viñeta

**Qué resuelve:** dónde poner el punto de luz para que el ojo vaya solo a donde importa,
y cómo oscurecer los bordes sin convertir el plano en un túnel marrón.

---

## El principio: la luz manda antes que el color

El ojo va **primero a la zona más clara del cuadro**. Antes de decidir dónde cae el
recorte, se decide de dónde entra la luz — y esas dos decisiones son la misma.

| Dónde va el elemento principal | Dónde va el punto de luz |
|---|---|
| Izquierda | Cae en la izquierda, un poco más arriba (`at 38% 30%`) |
| Centro | Cenital, desde arriba (`at 50% 0%`) |
| Derecha | `at 62% 34%` |
| Cifra sola en el centro | Luz cenital estrecha, 46-56% de ancho |
| Dos elementos enfrentados | **Dos luces** de distinta temperatura, una por lado |

La luz **no se pone en el centro geométrico por defecto**. Un punto de luz descentrado
(entre 38% y 62% horizontal, 28-44% vertical) da profundidad; centrado da diana.

## La luz base: un radial encima del degradado

```html
<!-- cenital cálida: almacén, dinero, ámbar -->
<div class="l" style="left:50%;top:-6%;transform:translateX(-50%);width:62%;height:48%;
  background:radial-gradient(58% 80% at 50% 0%,rgba(255,232,180,.22),transparent 72%)"></div>

<!-- cenital fría: oficina, acero, institución -->
<div class="l" style="left:50%;top:-6%;transform:translateX(-50%);width:56%;height:44%;
  background:radial-gradient(58% 80% at 50% 0%,rgba(214,240,255,.24),transparent 70%)"></div>

<!-- lateral: ventana a la izquierda -->
<div class="l" style="left:-8%;top:6%;width:52%;height:76%;
  background:radial-gradient(70% 60% at 0% 40%,rgba(226,240,255,.20),transparent 74%)"></div>
```

Sale **fuera del lienzo** (`top:-6%`, `left:-8%`) a propósito: así se ve el haz, no la
bombilla. Un radial con su centro dentro del cuadro se lee como mancha.

## Intensidades

| Alfa de la luz | Lectura |
|---|---|
| .08-.12 | Insinuada. Para escenas de plano técnico, donde no debe haber foco |
| **.16-.24** | **El rango normal.** Se ve el punto de luz, no molesta |
| .26-.34 | Fuerte: revelación, remate, el momento en que se descubre algo |
| más de .40 | Quemado; el grano de la capa 5 desaparece y se ve digital |

**Medido sobre `f_peso` del episodio 01** (mismo fondo, solo cambia el alfa de la luz):

| Luz | Viñeta | `YMAX` | Lectura |
|---|---|---|---|
| .20 | .62 | **82** | Sin blancos. Es el defecto del episodio 01 |
| .34 | .62 | 100 | Ya hay punto de luz |
| .34 | .56 | 104 | — |
| .48 | .56 | **120** | Foco claro, escena con recorrido |

Con la viñeta y el grano encima, **un fondo de este canal no pasa de `YMAX` 120-130**. Por
eso el umbral no es "que haya blanco puro", sino: **`YMAX` por debajo de 90 = escena
apagada.** Las seis del episodio 01 estaban entre 70 y 96 — de ahí el marrón.

## Luz de borde (rim) — separa el recorte del fondo

Cuando el recorte y el fondo tienen tono parecido, el recorte se hunde. Se resuelve con
una banda de luz justo detrás de donde va la figura:

```html
<div class="l" style="left:34%;top:12%;width:30%;height:72%;filter:blur(58px);
  background:linear-gradient(96deg,transparent 0%,rgba(255,245,215,.20) 46%,transparent 78%)"></div>
```

El `blur(58px)` es obligatorio: sin él es una barra, con él es luz.

## Haz de proyector / ventana

```html
<div class="l" style="left:18%;top:-14%;width:36%;height:130%;filter:blur(42px);
  transform:skewX(-14deg);opacity:.16;
  background:linear-gradient(180deg,rgba(255,244,214,.85),transparent 78%)"></div>
```

Dos haces paralelos con 6-10° de diferencia de `skewX` y opacidades distintas (.16 y .09)
dan la sensación de polvo en el aire sin tener que dibujar partículas (`55`).

## La viñeta que no ahoga

```html
<div class="vin" style="background:radial-gradient(76% 70% at 50% 48%,
  transparent 34%,rgba(0,0,0,.62) 100%)"></div>
```

Tres números y cada uno hace algo:

| Parámetro | Qué controla | Rango sano |
|---|---|---|
| `76% 70%` | Tamaño de la zona clara | 72-82% × 66-74% |
| `at 50% 48%` | Centro. **Se mueve con el punto de luz** | 42-58% × 44-52% |
| `transparent 34%` | Dónde empieza a oscurecer | 30-38% |
| `rgba(0,0,0,.62)` | Cuánto oscurece la esquina | **.56-.68** |

**El error del episodio 01 fue pasar de `.68`.** A partir de ahí el degradado del fondo
se come el tercio inferior y las seis escenas convergen al mismo lodo. Si un plano se ve
sucio, lo primero que se baja es la viñeta, no lo que se sube es el brillo.

**La viñeta se descentra con la luz.** Si la luz entra por la izquierda, la viñeta va
`at 44% 48%`: así el lado oscuro es el contrario al foco, que es como se comporta la luz
de verdad. Viñeta centrada + luz lateral = las dos se pelean.

## Comprobar sin opinar

```bash
ffmpeg -hide_banner -i render/f_peso.png -vf "signalstats,metadata=print:file=-" \
  -f null - 2>/dev/null | grep -E "YAVG|YMAX="
```

`metadata=print:file=-` manda la lectura a stdout. **No usar `-v error`**: silencia también
la impresión y la orden devuelve vacío.

| Lectura | Sano | Si se sale |
|---|---|---|
| `YMAX` | 100-130 | < 90: sin punto de luz → subir el alfa de la luz |
| `YAVG` | 34-58 | < 34: ahogado → bajar la viñeta |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Luz centrada por defecto | Diana: composición simétrica y muerta |
| Centro del radial dentro del cuadro | Se ve la mancha, no el haz |
| Viñeta por encima de `.70` | Todo converge al marrón; el episodio pierde recorrido |
| Viñeta centrada con luz lateral | Se anulan; el plano queda plano |
| Haz sin `blur()` | Se lee como una figura geométrica pegada |
| Subir el brillo del degradado en vez de bajar viñeta | Gris lavado, ni oscuro ni claro |

## Relacionado

`50` · `51` · `55` · `58` · `23` empatar recorte y fondo · `67` luz y destellos
