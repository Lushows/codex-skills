# 314 · Contorno, contorno cruzado y contorno ciego

> Las tres maneras de dibujar el borde de una cosa, y por qué elegir mal produce siempre el
> mismo resultado: la calcomanía.

---

## 1 · Contorno puro

La línea que separa el objeto del fondo.

- Es **el borde de lo que se ve**, no el borde de lo que se sabe
- Nunca es de grosor constante (ver `310 §3`)
- Nunca está cerrado al 100 % (ver `300 §5`)
- **No es un alambre alrededor del objeto:** es el punto donde la superficie gira y deja de
  verse. Por eso el contorno pertenece al volumen, no al fondo

---

## 2 · Contorno cruzado *(cross-contour)*

Líneas que **recorren la superficie** en vez de rodearla — como si una hormiga caminara sobre
el objeto y dejara rastro.

- Es la manera más directa de explicar volumen **sin usar sombra**
- La dirección de la línea ES la información
- En un cilindro van en anillo; en una esfera, en arcos concéntricos; en un plano, rectas

> **Es la base de la trama que envuelve** (`300 §3.2`). La diferencia es que aquí la línea
> se ve sola, no acumulada.

---

## 3 · Contorno ciego *(blind contour)*

Se dibuja mirando **solo al sujeto**, sin mirar el papel, sin levantar el lápiz.

- El resultado es feo y desproporcionado. No importa
- **Es el ejercicio que enseña a ver**, no a dibujar
- Obliga a seguir el borde real en vez de dibujar el símbolo que uno tiene en la cabeza
- 10 minutos al día cambian el ojo en dos semanas

---

## 4 · El símbolo: el enemigo

Todos tenemos guardado un símbolo de cada cosa: la casa con techo a dos aguas, el ojo con
forma de almendra, la seta con sombrero y puntos.

**Cuando dibujas rápido, sale el símbolo, no lo que ves.**

El contorno ciego y el espacio negativo (`315`) son los dos antídotos, porque los dos
imposibilitan usar el símbolo.

---

## 5 · Borde duro, blando y perdido

Ampliación de `300 §5`, ahora en términos de trazo:

| Borde | Cómo se dibuja | Cuándo |
|---|---|---|
| **Duro** | Línea nítida, ancho pleno | La superficie gira de golpe · hay contraste de material |
| **Blando** | Línea que se afina y se interrumpe | La superficie gira despacio |
| **Perdido** | Sin línea. El objeto y el fondo se tocan sin frontera | Mismo valor a ambos lados · zona de luz |

> **Un dibujo necesita los tres.** Solo duros = calcomanía. Solo blandos = niebla.

---

## 6 · La línea interior

No todo contorno es exterior. Dentro del objeto hay bordes que también se dibujan:

- Donde una parte se superpone a otra → **acento** (`310 §3`)
- Donde cambia el plano
- Donde cambia el material

Estas líneas van **más finas** que el contorno exterior. Si van iguales, el dibujo se aplana.

---

## 7 · Traducirlo a generativo

| Concepto | Implementación |
|---|---|
| Contorno modulado | Pasada de *filo*: trazos cortos alineados al borde, ancho ∝ valor local |
| Contorno cruzado | Arcos perpendiculares al eje, calculados en el espacio del objeto |
| Borde perdido | Opacidad → 0 en la zona de luz. **El contorno se corta solo** |
| Línea interior | Segunda pasada de filo en las intersecciones, más fina |
| Acento de solape | Trazos cortos y oscuros **solo donde dos cuerpos se cruzan** |

---

## 8 · Ejercicio

Dibuja el mismo objeto tres veces: solo contorno puro · solo contorno cruzado · las dos cosas.
La tercera es la que se ve sólida, y entender por qué es la lección.
