# 312 · Construcción de la forma

> Cómo se arma un dibujo antes de dibujarlo. Todo lo que se ve sólido en una lámina está
> construido sobre volúmenes simples que después se borran —o se dejan a la vista, ver
> [[310-el-trazo-vivo-gesto-ritmo-acento]] §4.

---

## 1 · Los cinco sólidos

Cualquier cosa del mundo se puede aproximar con estos cinco:

**esfera · cilindro · cono · caja · toro**

- Un tallo es un **cilindro**
- Una clava de Cordyceps es un **cilindro rematado en media esfera**
- Un sombrero de Ganoderma es una **caja aplastada curvada** o media esfera achatada
- Una masa de Hericium es una **esfera lobulada**

> **Por qué importa:** la sombra de un cilindro y la de una caja no se parecen en nada. Si no
> sabes qué sólido es la forma, no puedes sombrearla bien ni por casualidad.

---

## 2 · El eje

Todo volumen tiene un **eje**: la línea recta o curva que lo atraviesa de punta a punta.

- Se dibuja **primero**, antes que el contorno
- Define inclinación y longitud
- Todo lo demás cuelga de él

Un dibujo donde los ejes están mal se ve torcido aunque el contorno sea perfecto.

---

## 3 · Las elipses: el detalle que delata

Un cilindro visto en ángulo tiene **elipses** en los extremos, no círculos ni líneas rectas.

Tres reglas duras:
1. **El eje menor de la elipse es paralelo al eje del cilindro.** Siempre.
2. La elipse **se abre** cuanto más lejos está de la altura de los ojos
3. **Los extremos de la elipse son curvas, nunca puntas.** El error #1 del principiante es
   dibujarlas como un ojo con vértices

---

## 4 · La envolvente

Antes del detalle, se dibuja la **caja o silueta general** que contiene todo el sujeto:

- Fija las proporciones globales
- Evita que el dibujo "crezca" y se salga del papel
- Es lo primero que se traza y lo último que se comprueba

---

## 5 · Secciones transversales *(cross-contour)*

Líneas que **envuelven** el volumen como anillos, perpendiculares al eje.

- Es la herramienta más potente para entender un volumen que no se ve claro
- En el dibujo final pueden quedarse (trama que envuelve, `300 §3.2`) o borrarse
- Si no sabes por dónde iría un anillo alrededor de la forma, **todavía no entiendes la forma**

---

## 6 · La secuencia completa

```
1.  línea de acción        ← intención
2.  envolvente             ← proporción global
3.  ejes de cada volumen   ← estructura
4.  sólidos simples        ← masa
5.  secciones              ← comprensión del volumen
6.  contorno               ← la forma real, encima del andamiaje
7.  valor                  ← luz
8.  detalle y acento       ← lo último, y solo donde importa
```

> **La regla:** nunca se pasa a un paso sin haber resuelto el anterior. El 90 % de los dibujos
> fallidos empezaron por el paso 6.

---

## 7 · Construcción en generativo

Traducción directa de la secuencia:

| Paso | En código |
|---|---|
| Eje | Una polilínea, con curvatura e inclinación aleatorias por individuo |
| Sólido | Una función `perfil(t)` que da el radio a lo largo del eje |
| Sección | Arcos perpendiculares al eje, con el eje menor paralelo al eje del sólido |
| Contorno | Los puntos `eje ± normal·perfil(t)` |
| Valor | La normal del cilindro `(u, −√(1−u²))` contra el vector de luz |

> **Es literalmente el mismo procedimiento que a mano.** Por eso funciona: no se está imitando
> un dibujo, se está dibujando.

---

## 8 · Errores de construcción

- ⛔ Elipses con puntas
- ⛔ Eje menor de la elipse no paralelo al eje del cilindro
- ⛔ Empezar por el contorno
- ⛔ Todos los ejes con la misma inclinación
- ⛔ Sólido equivocado (sombrear un cono como si fuera cilindro)
