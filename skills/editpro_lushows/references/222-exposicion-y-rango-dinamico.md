# 222 — Exposición y rango dinámico

**Qué resuelve:** decidir **qué tan clara** debe quedar la imagen, sabiendo que esa decisión es de una
sola vía: lo que se quemó no vuelve, y lo que quedó muy oscuro vuelve sucio. En tu material medido, la
luminancia de los planos iba de **70 a 104** (sobre una escala de 0 a 255): unos bloques oscuros, otros
claros, y ninguno decidido a propósito. Este módulo convierte eso en una decisión consciente que se
toma en 10 segundos con el dedo en la pantalla.

---

## 1. Los términos, en tu idioma

> **Exposición:** cuánta luz deja entrar la cámara. Mucha = imagen clara. Poca = imagen oscura. En tu
> celular se controla **tocando la cara en la pantalla y deslizando el dedo arriba/abajo**, y se
> congela con el bloqueo AE/AF (`171`). No hay más controles que esos, y no los necesitas.

> **Paso o "stop":** la unidad con la que se mide la luz. **Un paso = el doble o la mitad de luz.**
> Subir un paso es duplicar el brillo. Es la unidad que usan todos los fotógrafos del mundo y es útil
> porque el ojo funciona así, por duplicaciones, no por sumas.

> **Rango dinámico:** cuántos pasos de diferencia hay entre lo más oscuro y lo más claro que la cámara
> puede grabar **al mismo tiempo**. Un celular de 2026 en video da algo así como 10–12 pasos útiles.
> El ojo humano da bastante más. Por eso lo que a ti te parece bien en el bar, a la cámara le parece
> imposible.

> **Quemado (clipping):** una zona que llegó al blanco puro (valor 255). Ahí **no se grabó nada**: es
> un parche vacío. No hay filtro, IA ni CapCut que devuelva lo que no se grabó.

> **Cortado en negro:** lo mismo por abajo (valor 0). Tampoco hay información.

---

## 2. La asimetría que gobierna todo: arriba es la muerte, abajo es la enfermedad

Esta es **la idea central del módulo** y la razón de la mitad de las reglas de fotografía.

- **Si quemas las altas** (una ventana, un letrero de neón, una camisa blanca al sol): esa zona quedó
  en 255. En el archivo hay un parche de blanco plano. Bajar el brillo después solo produce **un
  parche gris plano**. Es información destruida. Muerte.
- **Si subexpones** (grabas oscuro): la información **sí está**, solo que apretada en la parte baja de
  la escala. Al subirla en CapCut aparece **ruido**: manchas de color verdes y magenta, sobre todo en
  la piel y en las paredes lisas. Es feo, pero es una enfermedad, no una muerte. Y si la subexposición
  es leve, ni se nota.

**De ahí sale la regla de oro:**

> **Ante la duda, un pelo por debajo.**
> Entre quemar la ventana y dejar la cara medio paso oscura, siempre la cara medio paso oscura.

**Pero con un límite, porque el celular no es una cámara de cine:**

Tu celular graba en **8 bits** (256 niveles de brillo) y con compresión fuerte. No tienes margen
infinito para subexponer. Subir dos pasos en CapCut sobre material de celular saca un ruido asqueroso.

> **La regla calibrada para ti: entre −1/3 y −2/3 de paso. Nunca más de −1.**
> Se hace deslizando el dedo hacia abajo un poquito antes de bloquear el AE/AF. Un toque, no un
> arrastre.

---

## 3. Se expone para la piel. Punto.

En un video donde alguien habla, **la cara es el tema**. Todo lo demás se acomoda.

Eso quiere decir: **tocas la cara en la pantalla**, ajustas hasta que la cara se vea bien, bloqueas, y
aceptas lo que le pase al resto. Si la ventana del fondo se quema, se quema. Un fondo quemado detrás de
una cara bien expuesta el espectador lo lee como "está afuera y hay sol". Una cara oscura la lee como
"video mal hecho".

**Dónde debe caer la piel:**

> **IRE:** una escala de 0 a 100 para medir el brillo de una zona de la imagen. 0 = negro, 100 =
> blanco puro. Es la forma estándar de hablar de exposición.

| Tono de piel | Dónde debe caer | En escala 0–255 |
|---|---|---|
| Piel clara | 60–70 IRE | 155–180 |
| Piel media | 50–60 IRE | 130–155 |
| Piel oscura | 35–50 IRE | 90–130 |

**Esto es importante y casi nadie lo dice:** no todas las pieles van al mismo sitio. Exponer una piel
oscura como si fuera clara la **quema y le quita el color**; exponer una piel clara como si fuera
oscura la deja gris. Se expone para **esa** piel, la de la persona que tienes al frente.

**Cómo lo compruebas sin instrumentos:** mira la pantalla al 100% de brillo, tapando el reflejo con la
mano. Preguntas: ¿se le ven los ojos? ¿la mejilla tiene tono, o es un parche blanco sin textura? ¿se
distingue el borde de la nariz? Si sí a las tres, estás bien.

---

## 4. El histograma: la única herramienta objetiva que tienes gratis

> **Histograma:** un gráfico que cuenta cuántos píxeles hay de cada nivel de brillo. A la izquierda los
> oscuros, a la derecha los claros, en el medio los tonos medios. La altura solo dice "cuántos". No es
> una nota; es un mapa.

La cámara nativa no lo muestra. **Blackmagic Camera** (gratis, iOS y Android) sí, y también te da
cebras. Vale los 5 minutos que cuesta instalarla.

Cómo se lee, sin misticismo:

```
Todo amontonado a la IZQUIERDA         -> imagen subexpuesta
Todo amontonado a la DERECHA           -> imagen sobreexpuesta
Un pico PEGADO al borde derecho        -> hay zonas QUEMADAS. Esto es lo que hay que evitar.
Un pico pegado al borde izquierdo      -> hay negros cortados (menos grave, a veces buscado)
Bien repartido con el bulto al centro  -> exposicion sana
```

**Lo que NO significa:** un histograma "bonito y centrado" no quiere decir buena imagen. Una escena de
bar de noche **debe** tener el bulto hacia la izquierda: es de noche. Lo que importa es **dónde cae la
cara**, no dónde cae el promedio.

**Cebras (zebras):** rayas diagonales que la app dibuja encima de las zonas que están por encima de un
umbral. Ponlas en **95%**. Regla: si aparecen cebras sobre la cara, estás quemando la piel, baja. Si
aparecen sobre la ventana o sobre el letrero, generalmente es aceptable.

---

## 5. Cuando la escena no cabe: qué se sacrifica

El caso clásico de tu bar: terraza de día. Cielo y calle a un lado, sombra bajo el techo al otro. La
diferencia puede ser de 8 o 10 pasos. La cámara no lo puede grabar todo.

Tienes cuatro salidas, en orden de calidad:

1. **Cambiar el encuadre para que el problema no esté en cuadro.** Girar 90° y dejar el cielo fuera. Es
   gratis, instantáneo y es la respuesta correcta la mayoría de las veces.
2. **Meter luz en la sombra.** Un cartón blanco devolviéndole luz del cielo a la cara, o la lámpara del
   bar. Sube el lado oscuro y la escena "cabe". (`223`)
3. **Bajar la parte clara.** Cerrar una cortina, mover a la persona bajo el alero.
4. **Elegir y aceptar la pérdida.** Expones para la cara y el cielo se quema en blanco. Es una decisión
   válida y muy usada. Lo que **no** es válido es dejar que el celular decida solo.

**Lo que nunca funciona:** poner la exposición "a la mitad" para salvar los dos extremos. Terminas con
la cara gris **y** el cielo quemado. Elige un bando.

**El HDR no es la solución.** El modo HDR del celular parece resolver esto, pero produce archivos que
llegan lavados o con colores raros a CapCut y a las redes (`171`). Apágalo y resuelve con encuadre y
luz.

---

## 6. Medir de verdad tu propio material

Aquí está la parte que convierte esto en oficio: en vez de discutir si un plano quedó oscuro, lo mides.

**Luminancia promedio del cuadro completo:**

```bash
ffmpeg -hide_banner -i clip.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -frames:v 60 -f null - 2>&1 | grep YAVG | tail -3
```

**Ojo con esto, porque es donde casi todo el mundo se equivoca:** `YAVG` es el promedio de **todo el
cuadro**, fondo incluido. Un plano con la pared oscura y la cara perfecta puede dar YAVG=70, y un plano
con la cara oscura y una ventana quemada puede dar YAVG=104. **El número solo, sin contexto, miente.**

**Por eso hay que medir la zona de la cara.** En vertical 1080×1920 la cara suele caer en el tercio
superior, centrada. Recortas esa zona y mides:

```bash
# Recorta 500x500 centrado horizontalmente, a 550 px del borde superior
# (ajusta el 550 segun donde este la cara en TU encuadre)
ffmpeg -hide_banner -i clip.mp4 \
  -vf "crop=500:500:290:550,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -frames:v 60 -f null - 2>&1 | grep YAVG | tail -3
```

**Cómo interpretar el número de la cara (escala 0–255):**

```
menor a 80    -> demasiado oscura. Al subirla saldra ruido.
90 a 130      -> zona sana para piel media/oscura
130 a 180     -> zona sana para piel clara
mayor a 200   -> se esta quemando. Perdiste textura de piel.
```

**Detectar quemados sin mirar promedios** (cuenta qué proporción del cuadro está por encima de 250):

```bash
ffmpeg -hide_banner -i clip.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YHIGH" \
  -frames:v 60 -f null - 2>&1 | grep YHIGH | tail -3
```

**Auditoría de todo el rodaje de un golpe** — esto es lo que te dice si tienes un problema de
consistencia:

```bash
for f in *.mp4; do
  v=$(ffmpeg -hide_banner -i "$f" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
      -frames:v 30 -f null - 2>&1 | grep -o 'YAVG=[0-9.]*' | tail -1)
  echo "$v   <- $f"
done
```

Si el resultado se parece a tu material medido —**70, 88, 104, 76**— tienes cuatro planos que no se
van a poder cortar seguidos sin que se note el salto. Y esa diferencia (70 → 104) es aproximadamente
**medio paso**, que es exactamente lo que ganas o pierdes con un toque de dedo antes de bloquear.

---

## 7. La consistencia vale más que la perfección

Este es el criterio que hay que interiorizar: **el espectador no compara tu plano con el ideal. Compara
tu plano con el plano de al lado.**

Un video entero medio paso oscuro se ve intencional. Un video que salta de claro a oscuro cada 4
segundos se ve amateur, aunque cada plano por separado esté mejor expuesto que el otro.

**Cómo se consigue consistencia, gratis:**

1. **Decide el nivel una vez, al principio del día.** Un plano de referencia, bien expuesto sobre la
   piel. Ese es el patrón.
2. **En cada plano nuevo**, ajusta hasta que la cara se vea **igual de clara** que en el patrón. No
   igual de clara que el fondo: igual que en el patrón.
3. **No cambies de sitio a mitad de bloque.** Cada cambio de sitio es una exposición nueva y un riesgo
   nuevo (`173`, `175`).
4. **Bloquea siempre.** El automático te cambia la exposición dentro de la toma y eso es lo único que
   de verdad no se arregla.

**Prueba honesta al final del rodaje:** corre el bucle de la sección 6. Si el YAVG de todos los planos
de un mismo sitio está dentro de ±10, quedaste bien. Si hay 30 de diferencia, la edición te va a costar
el doble.

---

## 8. Lo que la exposición le hace a la corrección de color

Para cerrar el circuito con `228`:

- Un plano bien expuesto se corrige en **tres deslizadores y treinta segundos**.
- Un plano subexpuesto un paso se corrige, pero al levantarlo se le va el color de la piel hacia el
  verde o el magenta y hay que perseguirlo.
- Un plano con la cara quemada **no se corrige**. Se bota o se usa muy corto.
- Dos planos con exposiciones distintas hay que emparejarlos uno por uno (`62`), y en un reel de 8
  cortes eso es la tarde entera.

**La frase que resume el módulo:** medio minuto de dedo en la pantalla antes de grabar te ahorra media
hora de deslizadores después, y el resultado es mejor.

---

## Errores comunes

1. **Dejar la exposición en automático.** El brillo cambia solo a mitad de frase y eso es lo único que
   no tiene arreglo. Bloquea AE/AF en cada plano nuevo.
2. **Exponer para el fondo en vez de para la cara.** Toca la cara, no el aire. La cara es el tema.
3. **Quemar la piel por "que se vea clarita".** Una mejilla en 255 es un parche sin textura. Se ve
   plástica y no vuelve.
4. **Subexponer de más "porque en post se sube".** Con 8 bits de celular, más de un paso abajo saca
   ruido de color en la piel. El margen es −1/3 a −2/3, no −2.
5. **Exponer todas las pieles igual.** Una piel oscura expuesta como una clara se quema; una clara
   expuesta como una oscura queda gris. Se expone para la persona que está al frente.
6. **Creer que el histograma tiene que estar centrado.** Una escena de bar de noche debe estar hacia la
   izquierda. Lo que importa es dónde cae la cara.
7. **Poner la exposición "a la mitad" cuando la escena no cabe.** Terminas perdiendo los dos extremos.
   Elige un bando: casi siempre, la cara.
8. **Encender el HDR para salvar el contraste.** Llega lavado a CapCut y a las redes. Se resuelve con
   encuadre y con un cartón, no con HDR.
9. **Cambiar la exposición entre tomas del mismo bloque.** Produce saltos de brillo en cada corte. Un
   bloque = una exposición.
10. **No mirar la toma de prueba en la pantalla al 100% de brillo.** Con el brillo a la mitad y sol
    encima, todo parece oscuro y terminas sobreexponiendo.
11. **No medir nunca.** El bucle de ffmpeg de la sección 6 toma un minuto y te dice si el rodaje va a
    ser montable o no. Córrelo el mismo día, cuando todavía puedes regrabar.
12. **Perseguir el plano perfecto en vez del rodaje consistente.** Vale más que los ocho planos se
    parezcan a que uno sea espectacular.

---

## Checklist

- [ ] **Toqué la cara** en la pantalla y ajusté ahí, no el fondo.
- [ ] La cara está entre **−1/3 y −2/3 de paso** por debajo de lo que el celular proponía. Nunca menos.
- [ ] **AE/AF bloqueado** después de ajustar, en cada plano nuevo.
- [ ] La exposición está pensada para **el tono de piel de esa persona**, no para un ideal.
- [ ] **No hay cebras sobre la piel** (Blackmagic Camera, umbral 95%).
- [ ] Se le **ven los ojos** y la mejilla tiene textura, no un parche blanco.
- [ ] Si la escena no cabía, **elegí un bando** (la cara) y lo asumí, o cambié el encuadre.
- [ ] **HDR apagado.**
- [ ] Todos los planos del mismo sitio están al **mismo nivel** que el plano de referencia del día.
- [ ] Corrí el **bucle de medición** y los YAVG de un mismo sitio están dentro de ±10.
- [ ] Ningún plano tiene **YHIGH alto** en la zona de la cara (nada quemado donde importa).
- [ ] Revisé la toma de prueba en la **pantalla al 100% de brillo**, tapando el reflejo.
