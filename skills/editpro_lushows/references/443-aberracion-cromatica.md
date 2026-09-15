# 443 — Aberración cromática: radial, no lateral

`editpro/57` ya tiene la separación de canales como **glitch**: un desplazamiento lateral, igual en
todo el cuadro, deliberadamente visible, en un instante concreto. Esto es lo contrario: una
aberración **de lente**, que es cero en el centro, crece con el radio, dura todo el plano y no se ve
—se siente—. Son dos herramientas distintas con el mismo filtro debajo y no hay que confundirlas.

---

## 1. La diferencia, en una línea

| | Glitch (`editpro/57`) | Aberración de lente (aquí) |
|---|---|---|
| Geometría | traslación: `+8 px` en todo el cuadro | **escala**: 0 en el centro, máximo en la esquina |
| Duración | 2–5 fotogramas | el plano entero |
| Intención | que se vea | que **no** se vea |
| Canal | cualquiera, a veces solo uno | R hacia fuera, B hacia dentro (siempre en ese orden) |

Una lente descompone la luz porque el índice de refracción depende de la longitud de onda. El rojo
enfoca ligeramente más lejos del eje que el azul, así que la imagen roja sale **un poco más grande**.
El resultado es que en el centro los tres canales coinciden y en los bordes se abren. Un
desplazamiento uniforme es físicamente imposible y el ojo lo sabe.

---

## 2. La cadena que funciona (verificada con prueba nula)

```bash
ffmpeg -y -i in.mp4 -filter_complex "\
[0:v]split=3[a][b][c];\
[a]lutrgb=g=0:b=0,scale=1928:1085,crop=1920:1080:4:2[R];\
[b]lutrgb=r=0:b=0,scale=1924:1082,crop=1920:1080:2:1[G];\
[c]lutrgb=r=0:g=0[B];\
[R][G]blend=all_mode=addition[RG];\
[RG][B]blend=all_mode=addition,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow -c:a copy out.mp4
```

Cómo se lee: cada rama se queda con **un** canal (los otros dos a cero con `lutrgb`), se escala un
pelo, se recorta al tamaño original **centrado**, y las tres se suman. Como cada una solo tiene un
canal distinto de cero, la suma reconstruye el RGB sin solaparse.

El recorte centrado es lo que hace la aberración radial: escalar 1920 → 1928 y recortar en `x=4`
deja el centro donde estaba y separa todo lo demás en proporción al radio.

**El desplazamiento se calcula, no se adivina:**

```
px de separación R–B en un punto = radio del punto (px) × (escala_R − escala_B)
```

| escala R | separación en la esquina (r = 1101 px) | Lectura |
|---|---|---|
| 1,0010 | 1,1 px | invisible incluso en 4K |
| 1,0021 | 2,3 px | **lo que hace una lente decente** |
| 1,0042 | **4,6 px** | lente barata / vintage; el valor del ejemplo |
| 1,0100 | 11,0 px | ya es efecto, no lente |
| 1,0300 | 33,0 px | glitch: eso es `editpro/57` |

Regla: en 1080p, **por encima de 6 px en la esquina deja de leerse como óptica**.

---

## 3. La trampa: `extractplanes` + `mergeplanes` NO da la vuelta

La ruta que parece más elegante —extraer los tres planos, escalar cada uno y volver a montarlos— está
rota en la práctica. Medido hoy con la cadena de la documentación, sobre un fotograma real:

```bash
# la prueba NULA: si esto no devuelve la imagen idéntica, la cadena está mal
ffmpeg -v error -y -i plano.png -filter_complex \
  "[0:v]format=gbrp,extractplanes=g+b+r[g][b][r];[g][b][r]mergeplanes=0x001020:gbrp,format=rgb24" \
  -frames:v 1 nulo.png
```

| ruta | error medio de la prueba nula | error máximo |
|---|---|---|
| `extractplanes` + `mergeplanes=0x001020:gbrp` | **25,42 niveles** | **169** |
| `lutrgb` + `blend=addition` | **0,0** | **0** |

Con un píxel de control `(200, 120, 40)` la primera ruta devuelve `(40, 200, 120)`: los canales salen
rotados. No es un error de redondeo, es una permutación. Puede depender de la compilación; lo único
seguro es **hacer la prueba nula antes de creerte ninguna cadena por canal**.

> **La prueba nula es el hábito, no el resultado.** Monta la cadena con los tres factores de escala
> a 1,0000 y comprueba que la salida es idéntica a la entrada. Si no lo es, lo que estés midiendo
> después no mide la aberración: mide el error de la cadena.

---

## 4. Qué cuesta

Sobre 5 s de collage 1080p, CRF 12:

| | tiempo | ×ref | bytes | ×ref |
|---|---|---|---|---|
| sin filtro | 22,1 s | 1,00 | 5 979 626 | 1,00 |
| aberración 0,42 % | **25,3 s** | **1,15** | 8 284 346 | **1,39** |

Barata en CPU (+15 %) y cara en bits (+39 %). El motivo del +39 % es que los bordes dejan de ser
bordes limpios: cada contorno pasa a tener una transición de color de 2–4 px que el croma 4:2:0
codifica mal.

Consecuencia: **la aberración y el 4:2:0 se llevan mal**. En el submuestreo de croma, una franja de
color de 2 px ocupa un solo píxel de croma. Por debajo de 2 px de separación la aberración
prácticamente desaparece en el export final. Si la quieres a 1,5 px, no la vas a ver: o subes a 3–4 px
o no la pongas.

---

## 5. Dónde medirla — y dónde no

Medir la aberración promediando el delta de píxeles en una caja no sirve: mides el contenido. El
efecto solo existe donde hay un borde de contraste, así que una caja de cielo da 1,3 y una caja con
un rótulo da 7,4 **con la misma aberración**. Medido:

| zona | radio | franja R−B media | p99 |
|---|---|---|---|
| centro | 0 | 1,31 | 6,0 |
| 1/4 hacia arriba (con rótulo) | 270 | **7,00** | 76,0 |
| borde izquierdo medio | 860 | 2,89 | 21,0 |
| esquina superior derecha | 966 | 7,42 | 58,0 |

El centro sí confirma lo que tiene que confirmar —**1,31 frente a 6,0 de p99: prácticamente nada**—,
y eso es lo único que la medida de píxeles puede decirte. La magnitud en el borde se calcula con la
fórmula del §2; el píxel solo sirve para verificar que el centro está limpio.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Desplazar los canales en lugar de escalarlos | Aberración uniforme: físicamente imposible, se lee como glitch |
| Recortar sin centrar tras el escalado | La imagen se descentra y la aberración deja de ser radial |
| Fiarse de `extractplanes`+`mergeplanes` sin prueba nula | Canales rotados: 25,4 niveles de error medio |
| Aberración por debajo de 2 px en un export 4:2:0 | Se la come el submuestreo de croma; has pagado bits por nada |
| Poner el azul hacia fuera y el rojo hacia dentro | Es al revés; se lee raro sin que nadie sepa por qué |
| Aberración + `unsharp` con croma distinto de 0 | Los halos de color se multiplican |
| Medirla promediando píxeles en una caja | Mides el contenido de la caja, no el efecto |
| Usarla en material que ya viene de una lente barata | Se suma a la que ya trae y sale doble |

---

## Relacionado

`editpro/57` separación de canales como glitch (la versión visible y deliberada) ·
`editpro/445` halación y sangrado · `editpro/444` viñeta medida · `editpro/449` medir si la textura
suma · `editpro/257` look y emulación de película · `editpro/66` nitidez y el croma a 0,0 ·
`canales/68` efectos que se ven baratos
