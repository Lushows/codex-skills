# 375 — Entradas y salidas: por qué "Aparición progresiva" le gana a todo

Un catálogo de animaciones de texto tiene 80 opciones. La gramática medida usa **una** de entrada
—Aparición progresiva— y **una** de salida —Flash desactivado—. En 51 proyectos. Este módulo explica por
qué esa disciplina es correcta, cuáles son las pocas alternativas defendibles, y cómo se detecta una
animación barata antes de publicar.

---

## 1. Qué hace una animación de entrada (y qué no)

Una entrada tiene exactamente dos trabajos:

1. **Avisar que hay algo nuevo.** El ojo detecta cambio antes que forma. La entrada es el aviso.
2. **No estorbar la lectura.**

Eso es todo. **La entrada no es contenido.** No cuenta la historia, no vende, no aporta personalidad
—salvo que la marca la tenga como sistema, y ese es otro asunto (`52`)—.

Todo lo que una animación hace de más está robándole tiempo de lectura a una palabra que dura 1,5 s en
pantalla. Si la entrada tarda 0,5 s, te quedaste con 1 s de lectura real. Ese es el costo, y casi nadie
lo calcula.

> **Presupuesto de entrada: 0,20 a 0,35 s.** Por encima de 0,4 s estás gastando más en el aviso que en el
> mensaje.

---

## 2. Por qué "Aparición progresiva" sobrevive a las modas

Es un fundido de opacidad, quizá con un empujoncito de escala. Suena aburrido. Y es la que queda de pie
diez años después. Cinco razones concretas:

**a) No mueve el punto de lectura.** La palabra aparece *donde va a quedarse*. El ojo se posa una vez y
ya. Cualquier entrada con desplazamiento obliga al ojo a perseguir la palabra y luego reenfocar: gasta
80-150 ms de lectura por palabra, y con 10 palabras son 1,5 segundos regalados.

**b) No tiene "sabor de época".** Un deslizamiento con rebote elástico grita 2019. Un typewriter grita
2016. Un glitch RGB grita 2021. El fundido no grita nada porque no tiene forma propia: es la ausencia de
gesto. Lo que no tiene forma no pasa de moda.

**c) Se lleva bien con la cascada.** Seis palabras entrando cada 0,18 s con desplazamiento es un caos de
vectores cruzados. Seis palabras apareciendo es una columna que se construye. La cascada (`372`) **exige**
una entrada sin desplazamiento.

**d) Sobrevive a la compresión.** Instagram y TikTok recomprimen fuerte. Un texto que se desplaza rápido
sobre un fondo con detalle produce artefactos en el borde de las letras. Un fundido no genera movimiento
alto y sale limpio (`93`).

**e) Es compatible con el sándwich.** Ver `377`: cuando el texto va detrás del sujeto, cualquier
desplazamiento delata el recorte, porque la palabra pasa por debajo del borde del recorte y ahí se ven
los defectos de la máscara. El fundido no cruza bordes.

Esa última razón es la más práctica de todas para tu caso: usas sándwich en más de la mitad de tus
proyectos. La entrada tenía que ser un fundido casi por obligación técnica.

---

## 3. Las pocas entradas defendibles

Por orden de seguridad. Todas dentro del presupuesto de 0,35 s:

| Entrada | Cómo es | Cuándo | Riesgo |
|---|---|---|---|
| **Aparición progresiva** | Opacidad 0→100 | Siempre. El 90% de los casos | Ninguno |
| **Aparición + escala 108→100** | Fundido con micro-zoom saliente | Palabra portadora, remate | Bajo |
| **Escala 92→100 con fundido** | Micro-zoom entrante | Palabra que "llega" | Bajo |
| **Revelado por máscara** | La palabra se descubre de izq. a der. | Titular único, 1 vez por video | Medio: solo si es rápido (<0,3 s) |
| **Empuje vertical de 20 px** | Sube a su sitio mientras aparece | Textos secundarios, rótulos | Medio: no en cascada |
| **Máquina de escribir** | Letra por letra | **Solo** si el contenido es un mensaje o un chat | Alto fuera de ese caso |

Nota sobre la última: escribir letra por letra tiene un uso legítimo y uno solo — cuando estás mostrando
algo que *de verdad* se está escribiendo (un WhatsApp, una búsqueda). Ahí no es una animación, es una
representación. Fuera de eso, se lee como plantilla vieja.

---

## 4. Las entradas que se ven baratas (y por qué)

| Animación | Por qué falla |
|---|---|
| Rebote elástico con sobrepaso grande | El sobrepaso >15% es la firma de las plantillas gratis. El ojo lo asocia a "descargado", no a "hecho" |
| Deslizamiento largo (de fuera del cuadro) | Recorre 300+ px; el ojo persigue en vez de leer. Y en cascada se cruzan |
| Giro / rotación 3D | Durante el giro la palabra es ilegible. Regalas medio segundo |
| Parpadeo | Es un error de reproducción disfrazado de efecto |
| Glitch RGB | Fechado en 2021, y en compresión de plataforma se ve sucio |
| Explosión de partículas | Roba toda la atención hacia la animación y ninguna al texto |
| Zoom desde 0% | Deformación extrema, ilegible los primeros 0,15 s |
| Todas las letras entrando por separado desde distintos lados | Máximo ruido, mínima lectura |

**El test infalible:** graba la pantalla, reprodúcelo **al 25% de velocidad** y mírala. Si en la cámara
lenta ves que la palabra está deformada, girada, transparente a medias durante mucho tiempo, o
desplazándose mucho, esa animación te está costando lectura. La animación buena en cámara lenta se ve
casi aburrida. Eso es señal de que está bien.

---

## 5. La salida: donde casi todos fallan

Las salidas se descuidan porque "ya se leyó". Error: la salida define **cómo se siente el corte**.

**Flash desactivado** (desaparición seca, en 1-2 fotogramas) es la salida correcta para la gramática de
palabra suelta, por una razón simple: **una palabra que se desvanece lento compite con lo que viene
después.** Si la siguiente palabra ya entró y la anterior sigue a media opacidad, hay dos textos
compitiendo, uno de ellos medio muerto. Se ve sucio y nadie sabe por qué.

Las tres reglas de la salida:

1. **La salida es más rápida que la entrada. Siempre.** Regla práctica: salida ≤ mitad de la entrada. Si
   la entrada es 0,3 s, la salida es 0,15 s o menos.
2. **La salida cae sobre el corte** cuando se puede. Si el plano cambia y el texto desaparece en el
   mismo fotograma, el cerebro procesa un solo evento y el video se siente limpio.
3. **Toda la cascada sale junta.** Nunca en orden inverso (ver `372`).

### El error de la salida larga
Ponerle "desvanecer" de 0,5 s a la salida es tentador porque "queda suave". Lo que produce en realidad:
media palabra fantasma flotando encima del plano siguiente. En un reel de 20 s eso pasa 10 veces y el
video entero se siente turbio.

---

## 6. Entradas y salidas dentro del presupuesto de la palabra

Una palabra que vive 1,5 s en pantalla, bien repartida:

```
0,00 ─────── 0,28 ────────────────────── 1,40 ── 1,50
   entrada            LECTURA LIMPIA        salida
   (0,28 s)             (1,12 s)           (0,10 s)
```

75% del tiempo es lectura limpia. Ese es el objetivo. Si tu reparto queda en 50/50, la animación se
comió la palabra.

Para palabras de cascada, que viven más (2-3 s), el porcentaje de lectura limpia sube a 85-90%. Perfecto.

---

## 7. En CapCut y en el JSON

En la app: las animaciones de texto están en la pestaña **Animación**, separadas en *Entrada*, *Salida* y
*Bucle*. La barrita de duración debajo del nombre es lo que hay que ajustar, y viene por defecto en
valores demasiado largos —del orden de 0,5-0,8 s—. **Bájala siempre.** El ajuste por defecto de CapCut es
la causa más común de textos que se sienten lentos.

En `draft_content.json`: las animaciones viven en el arreglo de animaciones de material, y el segmento de
texto las referencia por id en su lista de `extra_material_refs`. Cada animación lleva su `type`
(`"in"` / `"out"`), su `duration` en **microsegundos** y un `resource_id`.

```jsonc
{
  "type": "in",
  "name": "Aparición progresiva",
  "duration": 280000,          // 0,28 s en MICROsegundos
  "start": 0,
  "resource_id": "<cópialo de un proyecto donde ya lo aplicaste a mano>"
}
```

**Nunca inventes el `resource_id`.** Aplica el efecto una vez en la app, busca su id en el JSON y reúsalo
para todo (`112`, `119`). Un id inventado abre el proyecto sin animación o directamente lo corrompe.

Chequeo útil al generar por código: **la suma de entrada + salida no puede superar la duración del
segmento.** Si una palabra dura 0,4 s y le pones 0,28 de entrada y 0,3 de salida, CapCut hace algo
impredecible. Valida antes de escribir:

```js
if (dur_in + dur_out > dur_segmento * 0.6) {
  dur_in  = Math.min(dur_in,  dur_segmento * 0.4);
  dur_out = Math.min(dur_out, dur_segmento * 0.2);
}
```

---

## 8. Cuándo sí vale la pena una entrada de autor

Una sola situación: **cuando la entrada es un elemento de marca sostenido en todas las piezas.**

Si cada video de la marca abre con el mismo revelado por máscara diagonal, eso deja de ser una animación
y se vuelve una firma (`52`). Pero entonces se aplica a **un** texto por video —el titular— y todo lo
demás sigue con Aparición progresiva. Nunca a todo.

Una entrada de autor aplicada a todos los textos no es estilo: es un video cansador.

---

## Errores comunes

1. **Dejar la duración por defecto de CapCut** (0,5-0,8 s). Es la causa #1 de texto que se siente lento.
2. **Entradas con desplazamiento largo.** El ojo persigue la palabra en vez de leerla.
3. **Salida más lenta que la entrada.** Deja palabras fantasma sobre el plano siguiente.
4. **Salidas de 0,5 s "para que quede suave".** El video entero se siente turbio.
5. **Sacar la cascada palabra por palabra**, en orden inverso.
6. **Usar más de dos animaciones distintas en la misma pieza.** Cada una añade un dialecto nuevo.
7. **Rebote con sobrepaso mayor al 15%.** Firma inconfundible de plantilla gratuita.
8. **Máquina de escribir fuera de su único caso legítimo** (mostrar algo que se está escribiendo).
9. **Combinar desplazamiento con sándwich.** El texto cruza el borde del recorte y se ve la máscara.
10. **Entrada + salida que suman más que el segmento.** Comportamiento impredecible en CapCut.
11. **Inventar `resource_id`** al generar el proyecto por código.
12. **No revisar en cámara lenta.** Al 25% se ve exactamente cuánta lectura te está costando la animación.
13. **Aplicar la animación de autor a todos los textos** en vez de solo al titular.

---

## Checklist

- [ ] Una sola entrada dominante en toda la pieza (Aparición progresiva por defecto)
- [ ] Una sola salida dominante (Flash desactivado)
- [ ] Duración de entrada entre 0,20 y 0,35 s, ajustada a mano
- [ ] Duración de salida ≤ mitad de la entrada
- [ ] Ninguna entrada mueve la palabra más de 20 px
- [ ] Al menos el 75% del tiempo de cada palabra es lectura limpia
- [ ] La cascada entera sale en el mismo fotograma
- [ ] Las salidas caen sobre el corte cuando se puede
- [ ] Entrada + salida no superan el 60% de la duración del segmento
- [ ] Revisé el video al 25% de velocidad y ninguna palabra se ve deformada o perseguida
- [ ] Si generé por código, los `resource_id` salen de un proyecto real, no inventados
- [ ] Si hay animación de autor, se aplica a un solo texto por pieza
