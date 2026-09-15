# 301 — Leer una curva de retención: el método completo

> Verificado a **agosto de 2026**. Instagram añadió este año el **gráfico de retención por reel** y la
> **tasa de salto** (el % que se va en los primeros 3 segundos, que reemplazó a la vieja "tasa de
> visualización"). TikTok lleva años dando la curva segundo a segundo. YouTube da la más detallada de
> todas. Es decir: **hoy las tres plataformas que te importan te dan la curva.** Ya no hay excusa.
> `140` te presentó cuatro formas de curva. Aquí está el método completo de lectura y, sobre todo, cómo
> **localizar el segundo culpable** con precisión de fotograma.

## Qué es exactamente lo que estás mirando

```
100 ┤█                        ← el 100 % es "todos los que abrieron el video"
 60 ┤ ███████████
 20 ┤           ██████████████
    └────┬────┬────┬────┬────┬───
         3    6    9   12   15  segundos
```

- **Eje vertical:** qué porcentaje de la gente que empezó el video sigue viendo en ese momento.
- **Eje horizontal:** el tiempo del video.
- **Siempre baja.** Instagram lo dice explícitamente: siempre vas a ver una pendiente hacia abajo. Lo que
  distingue un buen video de uno malo es **qué tan plana** es esa pendiente, no que no baje.

Dos advertencias: **el 100 % del eje no son todas las personas a las que se les mostró** — es solo quien
empezó a reproducir (los que pasaron de largo están en la tasa de salto y en el alcance). Y **la curva
puede pasar del 100 %** en algunos paneles cuando hay repeticiones: si te pasa, celebra.

---

## Paso 1 — Antes de interpretar, consigue la duración exacta

Todo el método depende de traducir **porcentaje del video → segundo real**. Y para eso necesitas la
duración de verdad, no la que crees.

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 reel_chorizo.mp4
# 14.867000
```

Un reel que "dura 15 segundos" dura 14,867. Parece una tontería, pero cuando la curva te dice "cae al
40 % del video", la diferencia entre calcular sobre 15 o sobre 14,867 son 0,05 s — nada. Pero cuando el
panel te da porcentajes gruesos (Meta Ads te da 25/50/75/100 %), esa base sí mueve el cálculo.

**La fórmula que vas a usar todo el tiempo:**

```
segundo culpable  =  (porcentaje del eje X donde cae)  ×  duración exacta
```

Ejemplo: la curva cae en el 45 % de un video de 14,867 s → 0,45 × 14,867 = **6,69 s**.

---

## Paso 2 — Clasifica la forma

Hay ocho formas que se repiten. Aprenderte estas ocho es el 90 % del trabajo.

### Forma A — Acantilado inicial

```
100 ┤█
 50 ┤ ██
  0 ┤   ████████████████
    └──┬──┬──┬──┬──┬──┬──
       2  4  6  8 10 12
```

Cae en picado los primeros 2–3 segundos y luego se aplana.

**Significado:** el gancho no enganchó, **pero el video sí es bueno**. Los pocos que se quedaron se
quedaron hasta el final (por eso se aplana). Este es el diagnóstico más fácil de arreglar y el que más
plata deja: mismo material, arranque nuevo.

**Señal de confirmación:** tasa de salto alta + porcentaje de finalización decente *entre los que
sobrevivieron*.

### Forma B — Tobogán constante

```
100 ┤███
 50 ┤   ██████
  0 ┤         ██████
    └──┬──┬──┬──┬──┬──
```

Baja parejo, sin escalones, hasta el final.

**Significado:** no hay un error puntual. **El video es más largo de lo que su contenido aguanta.** Cada
segundo pierde gente porque cada segundo no está justificando su existencia.

**Arreglo:** recorta un 30 %. No busques el momento malo — no hay uno, hay demasiado video.

### Forma C — Meseta y derrumbe

```
100 ┤██████
 50 ┤      ███████
  0 ┤             ████
    └──┬──┬──┬──┬──┬──
       2  4  6  8 10
```

Se sostiene y de golpe cae en un punto exacto.

**Significado:** hay un momento aburrido, confuso o publicitario **localizable**. Este es el caso donde el
método de este módulo brilla: puedes ir al fotograma exacto.

### Forma D — Escalera

```
100 ┤████
 60 ┤    ███  █████
 30 ┤            ███  █████
    └──┬──┬──┬──┬──┬──┬──
```

Varios derrumbes pequeños, con mesetas entre ellos.

**Significado:** el video tiene varias "puertas de salida". Normalmente coincide con el final de cada
idea: la gente entiende un bloque, siente que ya vio lo que venía a ver, y se va. Te falta **encadenar**
— cada bloque debería abrir el siguiente en vez de cerrarse (ver `31` sobre bucles y `06` sobre atención).

### Forma E — Joroba de repetición

```
100 ┤███
 50 ┤   ██████████    ██
  0 ┤             ████
    └──┬──┬──┬──┬──┬──┬──
                     ↑ sube
```

Sube en algún punto (casi siempre al final).

**Significado:** gente rebobinando o repitiendo. **Es la señal más fuerte que existe.** Puede ser por dos
razones opuestas:
- **Buena:** el contenido es denso y quieren volver a ver (un precio, una cara, un truco).
- **Mala:** algo no se entendió y tuvieron que volver.

**Cómo distinguirlas:** mira el pico. Si es al final del video → bucle, es buena. Si es en la mitad y va
justo después de un texto rápido o un dato → no se entendió, es mala. Y si hay comentarios de "¿qué
dijo?", es mala confirmada.

### Forma F — Muerte en el CTA

```
100 ┤████████████
 40 ┤            ██████
    └──┬──┬──┬──┬──┬──┬──
                  ↑ aquí dijiste "escríbenos"
```

Retención buenísima hasta que empieza el cierre.

**Significado:** el video funciona, el cierre delata la venta. La gente aguanta contenido, no aguanta
comercial. **Arreglo:** el CTA no puede ser un bloque aparte pegado al final — tiene que salir *dentro* de
la acción, o el video tiene que terminar antes y el CTA vivir en el texto en pantalla durante todo el
video.

### Forma G — Plana desde el principio

```
100 ┤███████████████████
    └──┬──┬──┬──┬──┬──┬──
```

Casi no baja.

**Significado:** o el video es cortísimo (menos de 6 s, y entonces no hay mérito), o tienes algo
excepcional. Verifica primero la duración antes de emocionarte.

### Forma H — Sierra

```
100 ┤█ █ █ █ █ █
    └──┬──┬──┬──┬──
```

Sube y baja constantemente en tramos cortos. **Significado:** casi siempre es **muestra pequeña**. Con
300 reproducciones, cada persona que se va mueve la curva un punto entero. Es ruido, no patrón. Ver `308`.

---

## Paso 3 — Localizar el segundo culpable con precisión

Esto es lo que casi nadie hace y es la parte que convierte "la curva cae por ahí" en "corta el segundo
6,7".

### 3.1 Lee el porcentaje del eje X, no el segundo del panel

Los paneles de móvil son pequeños y engañan. Calcula tú, y verifica contra la duración exacta.

### 3.2 Extrae el fotograma exacto

```bash
# El fotograma justo ANTES de la caída
ffmpeg -ss 6.2 -i reel_chorizo.mp4 -frames:v 1 antes.png

# El fotograma justo DESPUÉS
ffmpeg -ss 7.4 -i reel_chorizo.mp4 -frames:v 1 despues.png
```

Míralos lado a lado. En el 80 % de los casos, la respuesta salta a la vista: es el mismo plano en los dos.
**La gente se fue porque nada cambió.**

### 3.3 Saca el pedazo culpable en video

```bash
# Los 3 segundos alrededor de la caída, para verlos en bucle
ffmpeg -ss 5.5 -t 3 -i reel_chorizo.mp4 -c copy culpable.mp4
```

Ver ese pedazo solo, en bucle, sin el resto del video alrededor, es brutalmente revelador: sin el contexto
que tú tienes en la cabeza, se nota lo aburrido que es.

### 3.4 Cuenta los cortes en esa ventana

El estándar de ritmo en 2026 es **un cambio visual cada 1,5–2 segundos**. No es un corte cada 2 s
necesariamente: un punch-in, un texto que entra o un movimiento fuerte también cuentan como cambio visual.

```bash
# Detección aproximada de cortes
ffmpeg -i reel_chorizo.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep showinfo
```

Si en la ventana del derrumbe llevas 3 segundos sin ningún cambio visual, **ya sabes por qué se fueron**.
No hace falta más análisis.

### 3.5 Lee la transcripción de esa ventana

```bash
ffmpeg -ss 5.5 -t 3 -i reel_chorizo.mp4 -vn -ar 16000 -ac 1 culpable.wav
```

Y transcribe (ver `124`). Lee la frase en voz alta, sola. Las tres frases asesinas: **"bueno, entonces…"**
(relleno), **"como les venía diciendo…"** (repetición) y **"y no solo eso, sino que además…"** (segunda
idea encadenada donde el video debía terminar).

---

## Paso 4 — Cruza la curva con tu línea de tiempo

Este es el hábito profesional. Cuando montas, tienes una estructura mental: gancho, desarrollo, giro,
remate. Dibújala debajo de la curva.

```
CURVA      100 ┤████████
            50 ┤        ████████
             0 ┤                ███
                └──┬────┬────┬────┬────┬───
                   2    4    6    8   10  s

TU MONTAJE     [gancho][ contexto ][ producto ][ cta ]
                                  ↑
                          la caída empieza EXACTAMENTE
                          donde empieza "producto"
```

Cuando la caída coincide con el borde de un bloque de tu montaje, no es casualidad: **ese bloque no se
ganó su lugar**. Cuando la caída cae en la mitad de un bloque, el problema es de ritmo dentro del bloque,
no de estructura.

Es la diferencia entre "sobra una sección" y "esta sección está mal cortada". Son arreglos distintos.

---

## Paso 5 — Comparar curvas entre videos (bien hecho)

Comparar dos curvas de videos de distinta duración **superpuestas en segundos** es un error. Un video de
10 s y uno de 40 s no se comparan en el eje del tiempo.

**Normaliza a porcentaje del video:**

| Punto del video | Video A (12 s) | Video B (35 s) |
|---|---|---|
| 25 % | 71 % | 52 % |
| 50 % | 62 % | 38 % |
| 75 % | 55 % | 29 % |
| 100 % | 48 % | 22 % |

Ahora sí son comparables: A retiene mejor en toda la curva. Pero ojo con la trampa inversa: si el objetivo
era **exposición de marca**, B expone 35 × 0,22 = 7,7 s y A expone 12 × 0,48 = 5,8 s. Depende de qué
estabas midiendo (ver `300`).

**La comparación más útil de todas:** la misma curva del **mismo video en dos plataformas**. Si en TikTok
retiene 60 % y en Instagram 35 %, el video no es el problema — es el público o el momento. Y si retiene
mal en las dos, el video sí es el problema.

---

## Paso 6 — Cuándo la curva no significa nada

| Condición | Umbral mínimo |
|---|---|
| Reproducciones | **1.000** — por debajo, la curva es ruido con forma |
| Antigüedad | **72 horas** — antes, el reparto todavía se está estabilizando |
| Duración | **más de 6 s** — más corto, todo retiene bien y no aprendes |
| Pauta encima | Mezcla público frío con orgánico. Lee las dos curvas aparte |

---

## Las diferencias entre plataformas que te van a confundir

| Plataforma | Qué tiene | Trampa |
|---|---|---|
| **Instagram** (2026) | Gráfico de retención + tasa de salto | La tasa de salto mide los primeros **3 s**; la curva empieza después de eso. No son el mismo 100 % |
| **TikTok** | Curva segundo a segundo + "vieron el video completo" | La más honesta. Ojo con los videos que se reparten en oleadas: la curva promedia oleadas distintas |
| **YouTube** | Retención de audiencia, la más detallada | Incluye "retención relativa" comparada con videos parecidos. Muy útil y muy ignorada |
| **Meta Ads** | Solo 25/50/75/100 % | No es una curva, son cuatro puntos. Suficiente para clasificar la forma, no para localizar el segundo |

Con Meta Ads, la forma se deduce así:

```
3 s → 25 %  cae mucho   = acantilado inicial (Forma A)
25 % → 50 % cae mucho   = derrumbe en el primer tercio (Forma C)
caída pareja en los 4   = tobogán (Forma B)
75 % → 100 % cae mucho  = muerte en el CTA (Forma F)
```

---

## Errores comunes

- **Mirar el número resumen y no la curva.** El resumen dice que algo está mal; la curva dice dónde.
- **Alarmarse porque la curva baja.** Siempre baja. Lo que importa es la pendiente y los escalones.
- **Leer el segundo directamente del panel de móvil.** Calcula: porcentaje × duración exacta.
- **No sacar la duración con `ffprobe`.** Un video "de 15 s" casi nunca dura 15,000.
- **Comparar curvas de videos de distinta duración en el eje de segundos.** Normaliza a porcentaje.
- **Confundir la joroba de repetición buena con la mala.** Al final = bucle. En la mitad = confusión.
- **Interpretar una curva con 300 reproducciones.** Forma H = ruido, no patrón.
- **Ver el pedazo culpable dentro del video completo.** Sácalo aparte y míralo en bucle.
- **Arreglar el medio cuando la forma es un acantilado inicial.** El cuerpo está bien; es el arranque.
- **Recortar puntualmente cuando la forma es un tobogán.** Ahí no sobra un pedazo, sobra video entero.
- **Mezclar la curva del orgánico con la del video en pauta.** Son públicos distintos, léelas aparte.

---

## Checklist

- [ ] Saqué la **duración exacta** con `ffprobe`.
- [ ] El video tiene **más de 1.000 reproducciones** y **más de 72 horas**.
- [ ] Clasifiqué la curva en una de las **ocho formas** (A–H) y la escribí.
- [ ] Traduje el punto de caída a **segundo real** = porcentaje × duración.
- [ ] Extraje el **fotograma de antes y de después** de la caída y los comparé.
- [ ] Saqué el **pedazo culpable** a un archivo aparte, lo vi en bucle, conté los **cambios visuales**
      (¿pasé de 2 s sin cambio?) y leí su **transcripción** buscando relleno.
- [ ] Dibujé **mi estructura de montaje debajo de la curva** y vi si la caída coincide con un borde.
- [ ] Si comparo con otro video, **normalicé a porcentaje**, no a segundos.
- [ ] Si el video está en dos plataformas, comparé **las dos curvas** antes de culpar al video.
- [ ] Terminé con **una frase**: "la caída está en el segundo X y es por Y".
