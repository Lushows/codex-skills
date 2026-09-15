# 254 — Escala, proporción y sistemas

**Escala** es el tamaño relativo de las cosas; **proporción** es la relación entre las partes y el todo. Cuando esas relaciones siguen una lógica repetida, tienes un **sistema de proporción**: el esqueleto matemático que hace que algo se sienta "bien hecho" aunque nadie sepa por qué. Desde el Partenón hasta el iPhone, los objetos que perduran suelen esconder una proporción coherente. Este módulo es teoría —no es el grid de CSS (`51`) ni la escala tipográfica práctica (`48`)— sino el *porqué* de la proporción. Referentes: Le Corbusier (*Le Modulor*), Euclides, Vitruvio, la sección áurea.

## Por qué importa
Un dueño no técnico siente "esto se ve caro" o "esto se ve barato" sin saberlo: muchas veces es la proporción. Los sistemas dan tres cosas: armonía (las partes se relacionan), coherencia (todo nace de la misma regla) y decisión rápida (no eliges tamaños al azar, los deduces).

## Escala: tamaño relativo y su carga
La escala solo existe por comparación. Un círculo no es grande ni pequeño hasta que hay otra cosa al lado.
- **Contraste de escala** = lo enorme junto a lo diminuto. Crea drama, jerarquía brutal, asombro (Vignelli, el cartel monumental).
- **Escala humana** = referencia al cuerpo. Una puerta, una silla, una mano dan sentido de tamaño real (clave en packaging y entornos, ver `85`).
- **Escala como emoción:** lo muy grande = poder, sublime, intimidación; lo muy pequeño = delicadeza, intimidad, preciosismo.

## Proporción: las relaciones que armonizan
La proporción es la *razón* entre dos medidas. Históricas y útiles:

| Sistema | Razón | Carácter / uso |
|---|---|---|
| **Áurea (φ)** | 1 : 1,618 | "Divina proporción"; orgánica, elegante, atemporal. Nautilus, Partenón, Apple. |
| **Raíz de 2 (√2)** | 1 : 1,414 | Base del papel ISO (A4): al partir a la mitad conserva la proporción. Funcional, racional. |
| **Tercios / 1:1,5** | 2 : 3 | Foto 35mm, regla de los tercios (ver `62`). Natural, dinámica. |
| **Cuadrado (1:1)** | 1 : 1 | Estable, neutro, contemporáneo (Instagram). Reposo. |
| **Doble cuadrado** | 1 : 2 | Tensión vertical/horizontal, panorámico, banner. |

La **sección áurea** se construye geométricamente (no hace falta calcular): divide un segmento de modo que la parte menor sea a la mayor como la mayor es al todo. Aparece en la espiral del nautilus, los girasoles (Fibonacci) y la disposición de pétalos — por eso "se siente natural".

## El Modulor de Le Corbusier
Le Corbusier intentó casar la proporción áurea con el cuerpo humano. Su **Modulor** (1948) es una escala de medidas derivadas de un hombre de 1,83 m con el brazo en alto (2,26 m), combinando la sección áurea y la serie de Fibonacci. Su idea: una arquitectura (y un diseño) a escala humana **y** matemáticamente armónica a la vez. Lección para marca: un sistema de tamaños debe ser armónico *y* utilizable por personas, no solo bonito en teoría.

## Sistemas modulares y escalas
Un **sistema modular** define un módulo base y deriva todo de él multiplicando por una razón constante (×1,5, ×φ, ×2). Beneficio: cada tamaño "rima" con los demás. Es el principio detrás de:
- La **escala tipográfica** (12 → 18 → 27 → 40…, ver `48`).
- El **espaciado por baseline** (4 u 8 px como unidad, ver `87` tokens).
- Los **formatos de papel** (serie A).

Una escala con razón **grande** (×2) da contrastes dramáticos y pocos pasos; una razón **pequeña** (×1,2) da gradaciones sutiles y muchos pasos (refinado, editorial).

## ¿Cuándo importa de verdad el sistema?
- **SÍ importa** cuando hay muchas piezas que deben sentirse familia (sistema de marca, editorial, señalética). El sistema garantiza coherencia y velocidad.
- **Menos importa** en una pieza única expresiva, donde el ojo del autor manda y la regla puede romperse.

> Honestidad de oficio: la proporción áurea **no es magia universal** ni explica toda la belleza (muchos clásicos *no* la usan). Es **una** herramienta de armonía fiable, no una ley. Úsala como punto de partida, no como superstición.

## Ejemplos
- **Le Corbusier**, Unité d'Habitation — Modulor construido.
- **Serie A (Walter Porstmann)** — √2 como sistema funcional perfecto.
- **Vignelli** — sistemas de proporción y rejilla como religión del oficio.
- **Apple** — radios, espacios y tamaños derivados de un módulo coherente.

## Ejercicio
1. Mide tres objetos "que se ven bien" (una tarjeta, un libro, tu teléfono). Calcula lado largo ÷ lado corto. ¿Se acercan a 1,5–1,6?
2. Define un módulo (8 mm). Construye una escala ×1,5: 8, 12, 18, 27, 40. Maqueta una mini-pieza usando SOLO esos tamaños. Observa cuánto más coherente se siente.

## Errores típicos
- Elegir tamaños "a ojo" uno por uno → la pieza se siente desafinada.
- Venerar φ como ley y forzarla donde no aporta.
- Razón de escala tan pequeña que los tamaños no se distinguen (no hay jerarquía, ver `253`).
- Olvidar la escala humana en empaque → un frasco se ve "de juguete" o "industrial".

**Siguiente paso:** con escala y proporción dominadas, el siguiente nivel es reducir una forma a su esencia mínima — la abstracción (ver `255`).
