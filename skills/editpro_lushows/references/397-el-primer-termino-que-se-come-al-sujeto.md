# 397 — El primer término que se come al sujeto

**Qué resuelve:** el plano delantero funciona —da profundidad, el cuadro se ve rico— y sin embargo el
espectador no mira lo que la voz está contando. Mira el billete de delante. Este módulo mide el
**peso de atención** de cada plano y fija el margen en el que el primer término aporta sin robar.

`canales 22` ya dice lo esencial de reparto: como mucho un primerísimo vivo a la vez, y sin rótulo
encima. Aquí va el número que decide si ese primerísimo está bien dosificado.

---

## 1. La unidad: peso = área × acutancia

La mirada va a la superficie grande **y** al detalle fino. El producto de las dos aproxima bien a cuál
de los dos elementos gana:

```python
def peso(im, W_lienzo, H_lienzo):
    """peso de atención de un elemento ya escalado y tratado."""
    import numpy as np
    a   = np.asarray(im)[:, :, 3] > 200
    rgb = np.asarray(im.convert("RGB")).astype(np.float32)
    Y   = 0.2126*rgb[:,:,0] + 0.7152*rgb[:,:,1] + 0.0722*rgb[:,:,2]
    gy, gx = np.gradient(Y)
    area = 100.0 * a.sum() / (W_lienzo*H_lienzo)        # % del lienzo
    return area * np.hypot(gx, gy)[a].mean()
```

No es una medida perceptual fina —el color y el movimiento también tiran— pero es **comparativa y
reproducible**, que es todo lo que hace falta para decidir si un plano delantero está pasado.

---

## 2. La tabla medida

Sujeto: `retrato_lustig` a 620 px en 1920 × 1080 → área 24,5 %, ACUT 5,43, **peso 133**.
Primer término: `billetes_falsos`, un grabado de detalle fino, con saturación 1,02 y brillo 1,02.

| Primer término | Ancho | Área % | ACUT | Peso | vs. sujeto |
|---|---|---|---|---|---|
| 125 % sin nada | 775 | 17,0 | **10,36** | 176 | **+32 %** |
| 145 % sin nada | 900 | 22,9 | **9,48** | 217 | **+63 %** |
| 100 % sin nada | 620 | 10,9 | 11,79 | 128 | −4 % |
| 80 % sin nada | 496 | 7,0 | 13,41 | 93 | −30 % |
| **125 % + σ 1,1** | 775 | 16,9 | 7,23 | 122 | **−8 %** |
| 125 % + σ 2,0 | 775 | 16,9 | 5,40 | 92 | −31 % |
| 145 % + σ 1,4 | 900 | 22,9 | 5,97 | 136 | **+3 %** |
| 145 % + σ 2,6 | 900 | 22,9 | 4,39 | 100 | −25 % |

> **El margen bueno del primer término es −35 % a −5 % del peso del sujeto.** Por encima de −5 %
> compite; por encima de 0 % gana. Por debajo de −40 % deja de aportar y se convierte en suciedad.

---

## 3. Por qué se lo come: el primerísimo sin desenfoque

Fíjate en la columna de ACUT. **Un elemento más grande sale más afilado que el sujeto**, no menos: 10,36
contra 5,43. Dos causas que se suman:

1. **El material.** Un grabado de billetes tiene detalle de grabado. A tamaño igual (620 px) ya da ACUT
   11,79 contra 5,43 del retrato: un **factor 2,2** antes de tocar nada.
2. **El tamaño.** Agrandar no ablanda mientras no se pase del nativo; el elemento conserva su filo.

Resultado: un primerísimo "natural" a 125 % pesa un 32 % más que el sujeto de la frase. El espectador
está mirando el adorno. Lo que lo arregla es exactamente lo que `canales 22` prescribe y aquí queda
medido: **el primerísimo lleva algo de desenfoque a propósito** (σ 0,8–1,4). Está más cerca que el
plano de foco, y una cámara de verdad lo desenfocaría.

Y la lectura fina: **σ 1,1 sobre un 125 % lo deja en −8 %; σ 1,4 sobre un 145 % lo deja en +3 %.** El
salto de tamaño exige más sigma del que parece. Si agrandas, desenfoca más.

---

## 4. El caso silencioso: dos elementos del mismo plano

La fila de "100 % sin nada" es la más peligrosa de la tabla. Un elemento **del mismo tamaño que el
sujeto**, en el mismo plano, sin tratamiento, pesa **−4 %**: empata. Ahí no hay un primer término que
se come al sujeto; hay dos sujetos, y el espectador reparte la mirada entre los dos durante los cuatro
segundos que dura la frase.

Cuando en un cuadro dos elementos empatan a peso (±10 %), no hay jerarquía. La solución no es agrandar
el que quieres que gane —eso sube el peso de los dos a la vez y el cuadro se satura— sino **bajar el
otro**: al 80 % sin nada más ya está en −30 %. Es la regla de `204`: para destacar algo, apaga lo demás.

---

## 5. Cuánto puede tapar

El peso dice quién gana la mirada; el solape dice si el sujeto sigue siendo legible.

| Solape sobre el sujeto | Consecuencia |
|---|---|
| 0 % | no hay prueba de profundidad (`396` §3.5) |
| **8 – 25 %** | **el rango bueno: se ve quién está delante y el sujeto sigue entero** |
| 25 – 40 % | tolerable solo si lo tapado es el borde, nunca la cara ni la cifra |
| más del 45 % | el sujeto deja de serlo; sube el primerísimo de plano o quítalo |

**La parte que nunca se tapa** es la que sostiene la frase: la cara de quien se nombra, la cifra que se
dice, la palabra del documento que se cita. Un primerísimo que entra por el borde inferior y tapa un
hombro está bien. El mismo entrando por el centro y cruzando la cara está mal aunque su peso sea −20 %.

---

## 6. El primerísimo se mueve, y eso cuenta doble

El peso medido es de un fotograma quieto. En movimiento, el primer término deriva mucho más rápido que
el resto (`canales 22`: proporción 1 : 2,2 : 3,6) y **el movimiento tira de la mirada más que el
detalle**. Un primerísimo con peso −8 % pero derivando a 40 px/s puede ganarle al sujeto igualmente.

Corrección práctica: si el primerísimo deriva por encima de 30 px/s, cuenta un −10 % adicional en su
presupuesto de peso, es decir, apunta a **−20 % a −15 %** en vez de −8 %. La comprobación sigue siendo
la misma: verlo en movimiento, sin sonido (`368`), y ver adónde va el ojo.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Primerísimo sin desenfoque | Medido: +32 % de peso a 125 %, +63 % a 145 % |
| Agrandar el primerísimo sin subirle el sigma | 145 % con σ 1,4 se queda en +3 %: empata con el sujeto |
| Olvidar que el material ya trae acutancia | Un grabado pesa 2,2× un retrato al mismo tamaño |
| Dos elementos con pesos a ±10 % | No hay jerarquía: la mirada se reparte |
| Agrandar el que quieres que gane | Sube el peso de todo; hay que bajar el otro |
| Tapar la cara o la cifra | El solape correcto es de borde, no de centro |
| Solape por encima del 45 % | El sujeto deja de serlo |
| No descontar la deriva | El movimiento tira más que el detalle: −10 % extra si supera 30 px/s |
| Dos primerísimos vivos a la vez | Tapan el cuadro y no queda dónde mirar (`canales 22`) |

## Relacionado

`390` la profundidad es separación medida · `391` el escalón de tamaño ·
`392` el escalón de desenfoque · `396` el plano que no separa · `398` profundidad en vertical ·
`204` composición en capas (para destacar, apaga lo demás) · `368` ver sin sonido ·
`canales 21` peso visual y jerarquía · `canales 22` profundidad por capas (un primerísimo a la vez)
