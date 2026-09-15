# 315 · El espacio negativo

> Dibujar el hueco en vez del objeto. Es el truco más viejo y más eficaz para vencer al
> símbolo, y el que más rápido corrige un dibujo torcido.

---

## 1 · Qué es

El **espacio positivo** es el objeto. El **espacio negativo** es todo lo demás: el aire entre
dos tallos, el hueco de un asa, el trozo de fondo que asoma entre dos formas.

La clave: **el cerebro no tiene símbolo guardado para un hueco.** Como no puede recurrir a lo
que "sabe", se ve obligado a mirar de verdad.

---

## 2 · Por qué funciona

| Dibujando el objeto | Dibujando el hueco |
|---|---|
| El cerebro completa con lo que cree saber | No hay nada que creer: solo se puede observar |
| Las proporciones se deforman hacia el símbolo | Las proporciones salen correctas solas |
| Cada parte se dibuja aparte | El conjunto se resuelve al tiempo |

---

## 3 · Cómo se usa

1. Elige el hueco más claro y delimitado que veas
2. Dibújalo como si fuera **un objeto sólido con su propia forma**
3. Repite con los huecos vecinos
4. El objeto aparece solo, entre los huecos

> **Comprobación:** si un espacio negativo del dibujo no coincide en forma con el real, hay un
> error de proporción en las formas que lo rodean. Es el detector más rápido que existe.

---

## 4 · El espacio negativo como composición

No es solo una técnica de dibujo: es una decisión de diseño.

- Los huecos **también se componen**. Un dibujo con todos los huecos del mismo tamaño es aburrido
- Huecos de tamaños muy distintos → ritmo
- El hueco más grande suele ser el que **da respiro** y decide dónde descansa el ojo
- En un grupo de formas, **los huecos entre ellas cuentan la historia** tanto como las formas

> Ver `53-espacio-en-blanco` para el equivalente en diseño gráfico. Es el mismo principio con
> otro nombre.

---

## 5 · La figura-fondo

Cuando el hueco es tan interesante como el objeto, la imagen se vuelve ambigua y el ojo salta
entre las dos lecturas. Eso es **tensión**, y bien usada es lo que hace memorable una imagen.

- Flecha de FedEx, panda del WWF, copa de Rubin
- En ilustración: el aire entre dos tallos puede formar otra silueta

Ver `251-forma-contraforma-y-figura-fondo`.

---

## 6 · En generativo

El espacio negativo se programa **restando**, no dibujando:

- **Relleno de papel por cuerpo** antes de rayarlo: el hueco es lo que queda del fondo
- **Márgenes mínimos** entre elementos: si dos formas se pegan sin hueco, se leen como una
- **Variación de huecos:** si los individuos están equiespaciados, los huecos son todos iguales
  y el conjunto se ve de máquina

```python
# mal: equiespaciado -> todos los huecos iguales
x = W/2 + (i - n/2) * separacion

# bien: la separación varía y los huecos componen
x = W/2 + (i - n/2) * separacion * rnd.uniform(0.72, 1.34)
```

---

## 7 · Ejercicio

Dibuja una silla mirando **solo** los huecos entre las patas y el travesaño. No dibujes ni una
línea de la silla. Al terminar, la silla está ahí. Nadie que lo hace lo olvida.
