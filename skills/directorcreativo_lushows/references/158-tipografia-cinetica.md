# 158 — Tipografía cinética

**Tipografía cinética** (kinetic typography) es texto que se MUEVE: aparece, crece, cambia de peso, se desliza, baila al ritmo de una voz. La ves en intros de Netflix, videos de Apple, presentaciones de Awwwards, reels y motion de marca. Bien hecha, multiplica el impacto de una palabra; mal hecha, marea y nadie lee. Este módulo te enseña a moverla con criterio. Conecta con el 150 fuentes variables (que la hacen posible) y el 04 principios del diseño (jerarquía, ritmo).

## La regla que todo lo gobierna: LEGIBILIDAD primero
El movimiento NUNCA debe impedir leer. Si el espectador no alcanza a leer la palabra, el efecto falló, por bonito que sea. Antes de cualquier animación pregúntate: ¿se LEE cómodo? Si no, frena, agranda o simplifica.

## Para qué sirve (el propósito, no el adorno)
| Propósito | Ejemplo |
|---|---|
| **Énfasis** | Una palabra clave que crece o cambia de color |
| **Jerarquía en el tiempo** | El título entra primero, luego el subtítulo (guías la mirada) |
| **Emoción/tono** | Letras suaves y lentas (calma) vs. rápidas y duras (energía) — ver 14 personalidad |
| **Ritmo con audio** | Texto que pulsa con la música o sincroniza con la voz |
| **Transición** | Texto que lleva de una escena a otra |

## El ritmo (lo que separa al pro)
El movimiento tiene música: tiempos, pausas, aceleraciones. Conceptos clave:
- **Easing (curva de aceleración):** nada en la vida se mueve a velocidad constante. Usa `ease-out` para entradas (rápido y frena) y `ease-in` para salidas. El `linear` se siente robótico.
- **Stagger (escalonado):** las palabras o letras no entran todas juntas, sino una tras otra con un pequeño retardo. Da elegancia y ritmo.
- **Pausa:** el texto debe QUEDARSE quieto el tiempo suficiente para leerse antes de salir. Regla: ~0.3s por palabra de lectura, mínimo.
- **Anticipación y reposo:** un micro-movimiento antes (anticipa) y un asentamiento al final (settle) hacen que se sienta vivo, no mecánico.

```css
/* entrada escalonada de palabras */
.word {
  opacity: 0;
  transform: translateY(0.4em);
  animation: rise .6s cubic-bezier(.2,.8,.2,1) forwards;
}
.word:nth-child(1){ animation-delay: 0s; }
.word:nth-child(2){ animation-delay: .08s; }   /* stagger */
.word:nth-child(3){ animation-delay: .16s; }
@keyframes rise { to { opacity:1; transform:none; } }
```

## El superpoder: animar fuentes variables
Con una fuente variable (ver 150) puedes animar el PESO o el ancho de la letra suavemente — algo imposible con fuentes normales. Es la tipografía cinética más fina y moderna.
```css
.titulo { transition: font-variation-settings .5s ease; }
.titulo:hover { font-variation-settings: "wght" 800, "wdth" 110; }
```
De Light a Black de forma fluida al pasar el mouse, o un texto que "respira" cambiando de peso. Se ve carísimo y casi nadie lo hace.

## Técnicas y herramientas
| Dónde | Con qué |
|---|---|
| **Web** | CSS animations/transitions, GSAP, Framer Motion (React) |
| **Video / motion** | After Effects (+ plugins como Type-O-Matic), Cavalry |
| **Diseño/prototipo** | Figma (Smart Animate), Rive (interactivo) |

## Errores frecuentes
- [ ] Mover TODO: si todo se mueve, nada destaca. Anima 1–2 cosas.
- [ ] Demasiado rápido: no da tiempo a leer.
- [ ] Rebotes y efectos excesivos (bounce exagerado) → infantil/barato.
- [ ] Sin pausa de lectura: el texto sale antes de leerse.
- [ ] Easing lineal: se siente de máquina.
- [ ] Ignorar `prefers-reduced-motion`: hay personas a quienes el movimiento marea o enferma. RESPÉTALO:
```css
@media (prefers-reduced-motion: reduce) {
  .word { animation: none; opacity: 1; transform: none; }
}
```

## Casos para estudiar (reales)
- **Intros de Apple** (keynotes): texto que entra con stagger sutil y easing perfecto, siempre legible.
- **Awwwards "Sites of the Day":** hero text que revela palabra por palabra al hacer scroll.
- **Saul Bass / títulos de cine** (histórico): la raíz del kinetic type, vale estudiarlos (ver 03 maestros).
- **Reels/TikTok con subtítulos animados:** ritmo sincronizado con la voz palabra a palabra.

## Ejemplo trabajado
Hero de una marca de eventos. Titular "HACEMOS QUE PASE". Animación: las 3 palabras entran con stagger de 0.1s, cada una sube 0.4em con `cubic-bezier(.2,.8,.2,1)` (rápido y asienta). La palabra "PASE" además anima su peso de 400 a 800 (fuente variable) en 0.5s, quedando más fuerte: refuerza el mensaje. Queda quieto 2s para leerse. Respeta `prefers-reduced-motion`. Resultado: 1.2s de animación que se siente premium y la palabra clave golpea — sin marear ni impedir la lectura.

## Siguiente paso
Elige UNA pieza (un hero, una intro, un reel) y anima solo el texto más importante con: stagger, buen easing y una pausa de lectura. Si usas fuente variable, prueba animar el peso (150). Añade siempre el bloque `prefers-reduced-motion`. Para que el ritmo case con la marca, revisa 14 personalidad y tono.
