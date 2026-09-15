# 317 · Perspectiva y escorzo

> Lo mínimo de perspectiva que un ilustrador necesita. No para dibujar edificios: para que
> nada se vea torcido y para que las cosas ocupen espacio de verdad.

---

## 1 · Los tres conceptos que hay que tener

| Concepto | Qué es |
|---|---|
| **Línea de horizonte** | La altura de TUS ojos. No es "el horizonte del paisaje" |
| **Punto de fuga** | Donde convergen las paralelas que se alejan |
| **Plano del cuadro** | La ventana imaginaria por la que miras |

> **Todo depende de dónde están tus ojos.** Cambia la altura del punto de vista y cambia el
> dibujo entero. Decidirlo es la primera decisión, no la última.

---

## 2 · Un punto, dos puntos, tres puntos

- **1 punto:** miras de frente. Solo la profundidad fuga. Corredores, calles de frente
- **2 puntos:** miras una esquina. Los dos lados fugan. El más usado
- **3 puntos:** además miras arriba o abajo. Las verticales también fugan. Rascacielos, picado

Para un espécimen sobre una mesa, casi siempre **es suficiente con entender la línea de
horizonte y las elipses**.

---

## 3 · Las elipses y el horizonte

La regla que más se usa en ilustración de objetos:

- Una elipse **a la altura del horizonte** se ve como una línea
- Cuanto **más lejos** del horizonte, **más abierta** (más circular)
- El vaso visto de arriba: boca muy abierta. Visto a la altura de los ojos: boca casi plana

Aplicado a un hongo: si el sombrero está por debajo de tus ojos, ves su cara superior y la
elipse se abre. Si está por encima, ves las láminas.

---

## 4 · Escorzo *(foreshortening)*

Cuando algo apunta **hacia el espectador**, se acorta.

- Un brazo apuntándote no mide un brazo: mide un puño y un codo
- **El instinto siempre lo dibuja demasiado largo.** Hay que medir (`313`) y confiar en la medida
- Los detalles se **comprimen y se apilan** en el extremo cercano

> Truco: dibuja las **secciones transversales** (`312 §5`). Un cilindro escorzado es una pila
> de elipses cada vez más juntas. Si las elipses están bien, el escorzo está bien.

---

## 5 · Superposición: la señal más fuerte

De todas las señales de profundidad, **la superposición es la más potente** — más que el
tamaño, más que la perspectiva.

Si A tapa a B, A está delante. Sin excepción, y el cerebro lo acepta de inmediato.

> Por eso en una lámina con varios individuos, **hacer que se superpongan** vale más que
> cualquier perspectiva. Y por eso el acento en el solape (`310 §3`) es tan importante:
> es la señal que hace legible la superposición.

---

## 6 · Las otras señales de profundidad

| Señal | Cómo |
|---|---|
| **Superposición** | A tapa a B |
| **Tamaño relativo** | Lo lejano se ve más pequeño |
| **Posición en el cuadro** | Lo más abajo (en un suelo) está más cerca |
| **Detalle** | Lo cercano tiene más textura; lo lejano se simplifica |
| **Contraste** | Lo cercano tiene más contraste; lo lejano se aplana |
| **Borde** | Lo cercano tiene bordes más duros |

> Combinar tres o más señales es lo que da profundidad convincente. Una sola no basta.

---

## 7 · En generativo

- **Orden de dibujo = profundidad.** Se dibuja de atrás hacia adelante y cada cuerpo se rellena
  del color del papel: eso produce superposición real
- **Menos detalle atrás:** multiplicar la densidad de trazos por un factor de profundidad
- **Menos contraste atrás:** bajar la opacidad de los cuerpos traseros
- **Elipses correctas:** el eje menor SIEMPRE paralelo al eje del sólido

```python
orden = sorted(range(n), key=lambda i: -abs(i - (n-1)/2))  # centrales al frente
for i in orden:
    lienzo.fill(silueta(i))        # ocluye lo de atrás
    rayar(..., densidad * profundidad(i))
```

---

## 8 · Errores

- ⛔ Escorzo dibujado demasiado largo
- ⛔ Elipses con el eje menor torcido
- ⛔ Elipse plana lejos del horizonte
- ⛔ Todo el mismo detalle sin importar la distancia
- ⛔ Formas que no se superponen: se leen como recortes pegados en fila
