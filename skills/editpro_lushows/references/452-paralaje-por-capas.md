# 452 — Paralaje por capas

Un empuje sobre una foto sigue siendo una foto plana que crece: todo el cuadro se mueve a la vez y en
la misma proporción, que es justo lo que **nunca** hace una escena real. El paralaje rompe esa
uniformidad dando a cada plano su propia velocidad, y el cerebro deduce profundidad sin que nadie se
lo diga.

`83 §4` da la receta de partir la ilustración en capas. Este módulo es el **reparto de velocidades
medido**: cuánto diferencial hace falta, en qué unidad se mide, y qué cuesta.

---

## 1. La magnitud que importa es el diferencial, no la razón

Casi todo lo escrito sobre paralaje habla de razones («el frente se mueve 5 veces lo que el fondo»).
La razón sola no basta: 5× sobre un fondo que se mueve 2 px es un diferencial de 8 px, y no se
percibe nada. Lo que el ojo lee es la **diferencia absoluta de recorrido entre capas**, y se mide en
píxeles de pantalla por segundo, igual que en `451`.

Recorridos de un plano de 4 s (lienzo 1920×1080), con la razón clásica frente = 5× fondo:

| Fondo (px) | Medio ×2,5 | Frente ×5 | Diferencial frente−fondo | px/s | Cómo se lee |
|---:|---:|---:|---:|---:|---|
| 6 | 15 | 30 | 24 | 6 | plano. No hay profundidad |
| 12 | 30 | 60 | 48 | 12 | se intuye, al límite |
| **22** | **55** | **120** | **98** | **24,5** | **profundidad clara y natural** |
| 40 | 100 | 200 | 160 | 40 | escenario de teatro, algo teatral |
| 70 | 175 | 350 | 280 | 70 | las capas se despegan: parece un error |

> **La banda de trabajo es un diferencial de 20 a 45 px/s.** Por debajo de 12 px/s no hay señal de
> profundidad; por encima de 60 px/s el frente se despega del fondo y se lee como capa mal pegada,
> no como volumen.

Y la razón sigue importando **dentro** de esa banda: con frente menos de 3× el fondo el cerebro lo
interpreta como una sola imagen mal registrada —temblor, no profundidad—; por encima de 8× el frente
va por su cuenta. **3× a 6×** es el rango sano, con 5× como valor por defecto.

---

## 2. El comando, verificado

```bash
ffmpeg -hide_banner -y \
  -loop 1 -framerate 25 -t 4 -i fondo_2688.png \
  -loop 1 -framerate 25 -t 4 -i medio.png \
  -loop 1 -framerate 25 -t 4 -i frente.png \
  -filter_complex "\
[0:v]zoompan=z='1+0.00075*on':d=1:x='iw/2-(iw/zoom/2)-(on-50)*0.6':y='ih/2-(ih/zoom/2)':\
s=1920x1080:fps=25,format=rgba[bg];\
[1:v]scale=680:-1,format=rgba[md];\
[2:v]scale=840:-1,format=rgba[fr];\
[bg][md]overlay=x='520-13.75*t':y='240'[c1];\
[c1][fr]overlay=x='860-30*t':y='380',format=yuv420p[out]" \
  -map "[out]" -frames:v 100 -c:v libx264 -crf 18 -preset veryfast paralaje.mp4
```

Tres detalles que deciden si funciona:

- **El fondo se mueve con `zoompan` y las capas con `overlay`.** No es capricho: `zoompan` desplaza
  *dentro* de una imagen mayor que el lienzo; `overlay` desplaza un elemento *sobre* el lienzo. Mezclar
  los dos papeles es la forma más rápida de que una capa se salga (`456`).
- **`format=rgba` en cada capa antes de superponerla.** Sin él la transparencia se pierde y aparece un
  rectángulo opaco.
- **Los coeficientes están en px de pantalla por segundo**, porque `overlay` trabaja en coordenadas
  del lienzo. En `zoompan` estarían en px de fuente y habría que convertir (`451 §3`). Esa diferencia
  de unidades es la causa de la mitad de los paralajes descompensados.

---

## 3. Qué cuesta: medido

Escena de 6,73 s a 1920×1080, 25 fps, midiendo solo el grafo de filtros (`-f null -`), sobre la misma
máquina y en tandas seguidas:

| Composición | Capas sin preescalar | Capas preescaladas | Ahorro |
|---|---:|---:|---:|
| fondo + 3 capas | 87,6 s / 98,7 s / 51,3 s | 51,9 s / 73,9 s / 33,5 s | 25–41% |
| fondo + 8 capas | 116,2 s / 128,5 s / 94,1 s | 52,1 s / 92,0 s / 70,9 s | 25–55% |

Los tres números de cada celda son tres tandas distintas: **la máquina varía casi el doble entre
tandas, así que los valores absolutos no significan nada y las razones dentro de una misma tanda,
sí.** Lo que se repite en las tres es el coste marginal de una capa **sin preescalar**: entre 5,7 y
8,6 segundos por capa, y crece linealmente. Preescalada, ese coste marginal cae a una fracción.

La razón está en `458`: ffmpeg reescala el PNG **en cada fotograma**. Un recorte de archivo de 1447 px
mostrado a 340 se reduce 168 veces idénticamente. Reducirlo una vez a 1,4× su tamaño en pantalla, y
guardarlo, convierte ese trabajo en trivial.

**La consecuencia de diseño:** el paralaje de 3 capas es barato si las capas están preescaladas y caro
si no. La decisión «¿tres capas o una?» no se toma por coste de render; se toma por si la imagen tiene
de verdad un frente separable.

---

## 4. Cuándo NO hay paralaje que hacer

- **Cuando no hay frente.** Un paisaje, una multitud, una textura: no hay nada a qué darle velocidad
  propia. Ahí el gesto es un empuje o una deriva (`450`).
- **Cuando el recorte de silueta es malo.** Un borde con halo o con restos de fondo se delata en
  cuanto la capa se mueve: quieto se perdona, en movimiento no. Ver `81`.
- **Cuando el «fondo» no existe** porque el sujeto ocupaba todo el cuadro. Rellenar el hueco a mano o
  con IA cuesta más que el plano entero, y se nota.
- **Cuando el plano dura menos de 1,5 s.** No hay tiempo para que el diferencial acumule píxeles
  suficientes: a 24 px/s en 1,2 s son 29 px, por debajo del umbral.

---

## Errores frecuentes

1. **Perseguir la razón y olvidar el diferencial.** 5× sobre un fondo casi quieto no es profundidad.
2. **Frente a menos de 3× el fondo.** Se lee como imagen mal registrada, no como volumen.
3. **Frente a más de 8× el fondo.** La capa se despega y parece pegada encima.
4. **Mover todas las capas en la misma dirección y con la misma curva.** Aunque las velocidades sean
   distintas, el ojo detecta el patrón. Dale al frente algo de vertical, o una curva distinta.
5. **Mezclar unidades:** coeficientes de `zoompan` (píxeles de fuente) con los de `overlay` (píxeles de
   lienzo) en el mismo plano.
6. **Olvidar `format=rgba`** en alguna capa y descubrir el rectángulo negro al ver el render.
7. **No preescalar los PNG de las capas.** Es el coste dominante de la escena, y es evitable.
8. **Mover cinco capas.** Dos o tres. Con cinco, el ojo no encuentra dónde pararse.
9. **Hacer paralaje con un recorte de silueta sucio.** El movimiento revela todos los defectos del
   borde.

---

## Relacionado

- `450` — el gesto del que cuelga el paralaje: qué hace el fondo mientras las capas se mueven
- `451` — la unidad común (px/s) y las bandas de legibilidad de las que sale el diferencial
- `456` — dónde pierde la capa su margen y empieza a salirse del lienzo
- `458` — por qué preescalar las capas es la decisión que más render ahorra
- `83 §4` — cómo conseguir y preparar las capas (pedirlas, generarlas o recortarlas)
- `81` — recortes sin fondo: el borde que el movimiento delata
- `105` — `overlay` a fondo: coordenadas, `enable`, orden de capas
- `402` — el z dinámico: cuando una capa tiene que pasar por delante y luego por detrás
- `422` — cómo se mide el coste de un filtro en `utime`, que es la unidad honrada
- `canales_lushows/33` — el paralaje dentro de la gramática del canal documental
