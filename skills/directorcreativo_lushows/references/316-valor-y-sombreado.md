# 316 · Valor y sombreado

> El valor es qué tan claro u oscuro es algo. Es **más importante que el color** para que una
> imagen se lea: una foto en blanco y negro sigue funcionando; una con el valor plano y el
> color perfecto, no.

---

## 1 · La escala de valor

Diez pasos del blanco del papel al negro máximo. Un dibujo que solo usa del 3 al 6 se ve
gris y tímido — el error más común.

> **La regla del rango completo:** todo dibujo debe tener **algo del blanco puro del papel** y
> **algo del negro máximo del medio**. Sin esos dos extremos no hay presencia.

---

## 2 · Las seis zonas, otra vez

Repaso de `300 §2` — porque es la estructura de todo sombreado:

**brillo → luz → medio tono → NÚCLEO DE SOMBRA → luz reflejada → sombra proyectada**

Y el recordatorio: **el núcleo de sombra no está en el borde.** Entre él y el borde siempre
hay una franja de luz reflejada. Ese único detalle decide si algo se ve redondo o plano.

---

## 3 · Las cinco maneras de hacer valor

| Técnica | Cómo | Se lee como |
|---|---|---|
| **Trama paralela** | Líneas en una dirección, más juntas = más oscuro | Ordenado, gráfico |
| **Trama cruzada** | Capas en distintos ángulos | Rico, clásico, de grabado |
| **Trama que envuelve** | Las líneas siguen la forma | Volumétrico. **La más potente** |
| **Puntillismo** | Densidad de puntos | Limpio, científico, sin dirección |
| **Frotado / difuminado** | Grafito o carbón extendido | Suave, fotográfico, atmosférico |
| **Garabato** | Trazos sueltos que se cruzan | Gestual, vivo, artístico |

---

## 4 · La sombra proyectada

La que casi nadie dibuja bien:

- **Más oscura y de borde más duro cerca del contacto**, se abre y se aclara al alejarse
- Su forma sigue la del objeto pero **deformada por la superficie** donde cae
- Es lo que **pega el objeto al suelo**. Sin ella todo flota
- Nunca es negra plana: tiene luz rebotada dentro

---

## 5 · La oclusión de contacto

La franja **más oscura de todo el dibujo** está justo donde dos superficies se tocan: la base
del tallo contra el suelo, el punto donde una clava nace de otra.

Es una línea finísima y muy densa. Poner ese acento es lo que hace que las cosas se apoyen
de verdad.

---

## 6 · El borrador como herramienta

En grafito y carbón se dibuja **también quitando**:

- **Goma moldeable** — levanta sin borrar del todo; sirve para sacar luces
- **Goma de nata en punta** — luces nítidas, brillos
- **Trapo** — baja todo un tono de golpe

> Un dibujo trabajado solo aditivamente se ve plano. El ida y vuelta —poner, quitar, volver a
> poner— es lo que da atmósfera.

---

## 7 · Errores de valor

- ⛔ Rango corto: todo entre el 30 % y el 60 % de gris
- ⛔ Lo más oscuro en el borde en vez de en el núcleo
- ⛔ Sin luz reflejada → objeto plano
- ⛔ Sin sombra proyectada → objeto flotando
- ⛔ Sin oclusión de contacto → objeto posado, no apoyado
- ⛔ Sombreado uniforme en toda el área → textura, no volumen

---

## 8 · En generativo

```python
def valor(u):                    # u ∈ [-1,1] a lo ancho de un cilindro
    nx, ny = u, -sqrt(1 - u*u)   # normal aproximada
    d = nx*LUZ[0] + ny*LUZ[1]
    v      = 1 - (d*0.5 + 0.5)              # medio tono base
    nucleo = max(0, 1 - abs(d + 0.20)*1.55) # LA FRANJA, no una línea
    reflejo= max(0, -d - 0.55)*0.55         # rebote en la cara oscura
    return clamp(v + nucleo*0.34 - reflejo)
```

Dos números que deciden todo:
- El **1.55** del núcleo: más alto → la sombra se corta de golpe y el cuerpo se parte en dos
- El **piso** en la aceptación (`0.24 + 0.76*v`): sin él la mitad iluminada queda vacía

Ver `300`, `310` y `301`.
