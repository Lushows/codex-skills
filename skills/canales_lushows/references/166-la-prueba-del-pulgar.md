# 166 · La prueba del pulgar

**Qué resuelve:** el episodio se juzga en un monitor de 1920 px y se ve en un móvil de
siete centímetros. Esta prueba enseña **qué sobrevive a ese tamaño**, que es casi
siempre mucho menos de lo que uno cree.

---

## El tamaño equivalente: 400 px

Un vídeo 16:9 a pantalla completa en el feed de un móvil de 6,1" ocupa unos **7 cm de
ancho**, mirado desde unos 30 cm. En un monitor de 24" (53 cm de ancho, 1920 px) a 60 cm
de distancia, el mismo ángulo visual son **≈ 370-420 px de ancho**.

**Es decir: reducir el fotograma a 400 px y mirarlo desde donde uno trabaja es una
simulación honesta del móvil.** No hace falta un teléfono ni pasarse el archivo.

```bash
# un fotograma a tamaño de movil
ffmpeg -y -v error -ss 26.75 -i salida/ep01-lustig-min1.mp4 \
  -vf "scale=400:-1" -frames:v 1 _pulgar.png

# el episodio entero a tamano de movil, para verlo del tiron
ffmpeg -y -v error -i salida/ep01-lustig-min1.mp4 -vf "scale=400:-1" \
  -c:v libx264 -crf 20 -c:a copy salida/_pulgar.mp4
```

**La grilla ya es la prueba del pulgar.** `160` genera las casillas a `scale=440:-1`.
Mirar `_grid.png` **al 100%, sin ampliar**, es exactamente mirar 36 móviles a la vez. Por
eso el paso 1 de la revisión de la grilla —«sin ampliar, de un vistazo»— no es pereza:
es el único momento en que se ve el episodio como lo verá la mayoría.

## Qué sobrevive y qué no

A 400 px, el fotograma mide 400×225. Todo se divide por **4,8**.

| En el lienzo de 1920 | En el móvil | Veredicto |
|---|---|---|
| Rótulo con letra de 34 px en pantalla | 7 px | **Desaparece.** Es una mancha gris |
| Rótulo de 60 px | 12,5 px | Se intuye que hay texto; no se lee |
| Titular de 90 px | 19 px | Se lee si es corto, en negrita y con contraste |
| Cifra de 150 px | 31 px | Se lee siempre. Es el formato de la cifra protagonista |
| Recorte de 440 px de ancho | 92 px | Se ve la silueta, no el contenido |
| Recorte de 900 px | 188 px | Se reconoce el objeto |
| Diferencia de luminancia de 16 | 16 | **No cambia**: el contraste no se escala (`163`) |
| Movimiento de fondo del 8% | 8% | No cambia, pero se percibe menos |

Dos consecuencias prácticas:

- **La información obligatoria vive en dos tamaños: 90 px y 150 px.** Nombre del
  protagonista, cifras que sostienen el episodio y las marcas de columna. Todo lo demás
  es decoración a efectos de móvil, y decorar está bien siempre que no sea el soporte
  de un dato (`165`).
- **El contraste importa el doble en móvil.** Al reducir, los detalles se promedian: un
  elemento con `dL` de 10 sobre su fondo, que en 1920 al menos se adivina, en 400 px se
  funde del todo. El umbral de `163` no se relaja para móvil: se endurece.

## Las tres cosas que se miran

1. **¿Se distingue una forma protagonista en cada casilla?** Si una casilla es una papilla
   de manchas del mismo tamaño, el plano no tiene jerarquía (`21`). En móvil eso es un
   plano perdido.
2. **¿Hay algo escrito que se lea?** Recorrer las 36 casillas contando cuántas tienen
   texto legible a 440 px. Si son menos de un tercio, el episodio depende de la voz.
3. **¿La primera casilla funciona sola?** Es el gancho, y es lo que decide el barrido. A
   440 px tiene que verse **una cosa**, clara, distinta del fondo. Un gancho con cuatro
   elementos equilibrados no gana a esa escala: gana el que tiene uno grande.

## La miniatura no es esto

La miniatura del vídeo (`99`) se diseña aparte, con sus propias reglas, y se juzga a
**320×180**, que es todavía más pequeño. La prueba del pulgar juzga **el episodio**, no
la portada. Confundirlas lleva a montar el episodio entero como si fueran 36 miniaturas,
y eso produce un vídeo agotador.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Mirar el fotograma reducido ampliándolo en el visor | El visor interpola y devuelve nitidez que el móvil no tiene |
| Reducir a 720p y llamarlo "prueba de móvil" | 1280 px no es 400: no se pierde nada y la prueba no dice nada |
| Corregir un rótulo ilegible haciéndolo más largo | Lo que falta es cuerpo de letra, no palabras (`164`) |
| Dar por bueno un plano porque en el monitor grande se lee | El monitor grande lo ve una persona: quien montó el episodio |
| Meter cuatro elementos del mismo tamaño en el gancho | A 440 px no hay protagonista y el espectador sigue barriendo |
| Subir el tamaño de TODO para que se lea en móvil | Se acaba con cuatro titulares encima y cero jerarquía |

## Relacionado

`160` la grilla de fotogramas · `163` contraste elemento-fondo · `164` legibilidad por
altura · `165` la prueba del mudo · `21` peso visual y jerarquía · `49` zona segura y
tamaños · `99` título, miniatura y descripción
