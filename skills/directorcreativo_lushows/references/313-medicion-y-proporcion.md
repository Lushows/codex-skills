# 313 · Medición y proporción

> Cómo se acierta el tamaño. No es talento: es un procedimiento, y se puede aprender en una
> tarde. Es también lo que separa un dibujo que "no sé qué tiene raro" de uno que convence.

---

## 1 · La unidad de medida

Se elige **una** medida del sujeto y todo lo demás se expresa en ella.

- En figura humana: la cabeza (una figura mide ~7,5 cabezas)
- En un hongo: el ancho del sombrero, o la altura del pie
- **Siempre la misma unidad en todo el dibujo.** Cambiar de unidad a mitad es la causa #1 de
  proporciones rotas

---

## 2 · El visado *(sighting)*

El gesto clásico del brazo estirado con el lápiz:

1. Brazo **completamente estirado** — si se dobla, la escala cambia y la medida miente
2. Un solo ojo cerrado
3. El lápiz **perpendicular a la línea de visión**
4. Se marca con el pulgar el largo de la unidad
5. Se cuenta cuántas unidades caben en lo demás

> **Mide relaciones, no centímetros.** No importa cuánto mide de verdad: importa que el
> sombrero sea 2,4 veces el pie.

---

## 3 · Verticales y horizontales de referencia

Se sostiene el lápiz **a plomo** (vertical puro) o nivelado (horizontal puro) y se observa
qué cae en línea con qué.

- "La punta de esta clava cae justo encima del arranque de aquella"
- "El borde del sombrero está a la misma altura que el tercer anillo"

Estas relaciones **son el esqueleto invisible** de un dibujo bien puesto. Sin ellas, cada parte
está bien y el conjunto está mal.

---

## 4 · Los ángulos

Los ángulos se miden **contra la vertical o la horizontal**, nunca "a ojo":

1. Se pone el lápiz sobre el borde real que se quiere dibujar
2. Se mantiene ese ángulo y se baja al papel
3. Se traza

Suena tonto y es lo que más corrige un dibujo torcido.

---

## 5 · Triangulación

Para ubicar un punto difícil: se relaciona con **dos puntos ya dibujados y correctos**.

"Esta punta está a una unidad a la derecha de aquella y media unidad más arriba."
Dos referencias fijan un punto sin ambigüedad.

---

## 6 · Comprobaciones que siempre encuentran el error

| Comprobación | Cómo |
|---|---|
| **Voltear el dibujo** | Del revés se ven los errores de proporción al instante |
| **Mirarlo en un espejo** | Lo mismo: rompe la costumbre del ojo |
| **Entrecerrar los ojos** | Elimina el detalle y deja las masas |
| **Alejarse tres metros** | La distancia revela lo que la cercanía esconde |
| **Fotografiarlo** | Reduce y aplana: los errores saltan |

> **La regla:** si algo se ve raro y no sabes qué, **es proporción**. Casi nunca es detalle.

---

## 7 · Proporciones que valen la pena saber de memoria

- **Figura humana:** 7,5 cabezas · codo a la cintura · muñeca a la entrepierna · rodilla a media pierna
- **Cabeza:** los ojos a la MITAD de la altura, no arriba. Es el error más universal
- **Mano:** el largo de la palma ≈ el largo de la cara
- **Sección áurea 1:1,618** — útil como comprobación, no como fórmula

---

## 8 · Proporción en generativo

El error equivalente al "todo mide igual": generar todos los individuos con el mismo tamaño.

```python
# mal: todos iguales
alto = 300

# bien: una unidad + variación con jerarquía
UNIDAD = 300
alto = UNIDAD * (0.78 + 0.44 * centralidad) * rnd.uniform(0.86, 1.14)
```

**Dos reglas:**
1. Debe existir **una unidad** de la que todo se derive
2. La variación debe tener **jerarquía** (el del centro más alto), no ser puro ruido

Ver [[312-construccion-de-la-forma]].
