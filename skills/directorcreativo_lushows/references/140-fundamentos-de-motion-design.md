# 140 — Fundamentos de motion design

El motion design es el arte de mover cosas con intención. No es "ponerle animación" a un logo o una pantalla: es decidir cómo nace, viaja y se asienta cada elemento para que comunique personalidad y guíe la atención. La base de todo motion serio son los **12 principios de animación** de Disney (1981), que siguen vigentes porque describen cómo el ojo humano espera que se mueva la materia. Aquí los aplicamos a marca y UI, no a dibujos animados.

Términos clave en simple:
- **Keyframe** (fotograma clave): una posición marcada en el tiempo (ej. "en 0 ms el logo está pequeño, en 400 ms está en su tamaño"). El software calcula los pasos intermedios.
- **Easing** (suavizado): la curva de velocidad entre keyframes. Nada en la vida real arranca o frena de golpe; el easing imita eso.
- **Timing**: cuánto dura un movimiento.
- **Peso**: la sensación de masa. Una pluma y una caja de hierro no se mueven igual.

## Los 12 principios, aplicados a marca y UI

| # | Principio | Qué es | En marca/UI |
|---|---|---|---|
| 1 | Squash & stretch | Deformar al moverse/impactar | Un botón que se comprime 4% al pulsarlo se siente "vivo" |
| 2 | Anticipation | Pequeño retroceso antes de la acción | El logo se encoge un instante antes de expandirse |
| 3 | Staging | Una cosa a la vez, clara | No animes 6 elementos simultáneos; dirige el ojo |
| 4 | Straight ahead / pose to pose | Dibujar al vuelo vs. por poses clave | En UI casi siempre pose-a-pose (keyframes) |
| 5 | Follow-through & overlap | El movimiento no frena seco | Un leve asentamiento al final, partes que llegan desfasadas |
| 6 | Slow in & slow out (easing) | Acelera al salir, frena al llegar | **El más importante.** Lineal = barato |
| 7 | Arcs | Los objetos se mueven en curvas, no líneas rectas | Un icono que entra describiendo un arco se ve natural |
| 8 | Secondary action | Movimiento de apoyo | Una sombra que crece mientras el card sube |
| 9 | Timing | Duración = peso y emoción | Lento = serio/elegante; rápido = joven/ágil |
| 10 | Exaggeration | Empujar un poco más allá de lo literal | Un rebote ligeramente exagerado da carácter |
| 11 | Solid drawing | Volumen/peso creíble | En 3D y sombras, respetar la física (ver 144) |
| 12 | Appeal | Que sea agradable, con personalidad | Lo que separa motion "correcto" de motion memorable |

## Easing: lo no negociable

El movimiento **lineal** (velocidad constante) se ve robótico y barato. Casi todo debe acelerar al salir y frenar al llegar.

| Curva | Cuándo usarla | Bezier aprox. |
|---|---|---|
| ease-out | Entradas (algo aparece) — arranca rápido, frena suave | `cubic-bezier(0.16, 1, 0.3, 1)` |
| ease-in | Salidas (algo desaparece) | `cubic-bezier(0.7, 0, 0.84, 0)` |
| ease-in-out | Movimientos de un punto a otro | `cubic-bezier(0.65, 0, 0.35, 1)` |
| spring (resorte) | Interacciones juguetonas, naturales | rebote físico (Framer Motion lo hace nativo) |

Regla práctica: si dudas, usa **ease-out** para entradas. Es el que mejor se siente.

## Timing: duraciones de referencia

| Tipo de movimiento | Duración | Por qué |
|---|---|---|
| Microinteracción (hover, tap) | 100–200 ms | Debe sentirse instantáneo (ver 142) |
| Transición de estado (abrir menú) | 200–350 ms | Perceptible pero ágil |
| Transición de pantalla | 300–500 ms | Da contexto sin demorar |
| Entrada de elemento al cargar | 300–600 ms | Tiempo de "presentarse" |
| Logo intro | 1–3 s | Más de 3 s aburre (ver 143) |

Principio: **lo grande se mueve más lento, lo pequeño más rápido.** Un panel completo tarda más que un checkbox.

## Peso y personalidad

El mismo recorrido contado distinto cambia la marca:
- **Marca de lujo / institucional**: lento (400–600 ms), easing suave, sin rebotes. Sereno y seguro.
- **Marca joven / tech / consumo**: rápido (150–300 ms), con micro-rebotes (spring). Ágil y divertido.
- **Marca artesanal / orgánica**: arcos amplios, movimiento fluido tipo líquido.

Esto conecta con la personalidad de marca (ver 14): el movimiento debe sentir lo mismo que dice el tono verbal.

## Errores de fundamentos
- Movimiento lineal (sin easing) en cualquier cosa.
- Animar todo a la vez (sin staging) → el ojo no sabe dónde mirar.
- Duraciones largas que estorban (un menú que tarda 800 ms en abrir cansa al 3.er uso).
- Rebotes en una marca seria (rompe la personalidad).
- "Porque puedo": efectos sin función ni significado.

## Mini-checklist
- [ ] Todo movimiento tiene easing (nada lineal)
- [ ] Una acción protagonista a la vez (staging)
- [ ] Lo grande más lento, lo pequeño más rápido
- [ ] Duraciones dentro de rango según tipo
- [ ] El "carácter" del movimiento coincide con la personalidad de marca
- [ ] Entradas con ease-out, salidas con ease-in

**Siguiente paso**: con los fundamentos claros, conviértelos en un sistema repetible y propio de la marca — un vocabulario de movimiento documentado (ver 141 sistemas de motion de marca).
