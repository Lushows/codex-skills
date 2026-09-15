# 141 — Sistemas de motion de marca

Una marca seria no anima "a ojo" cada pieza: tiene un **sistema de motion**, igual que tiene paleta de color y tipografías. El sistema convierte el movimiento en un activo reconocible y repetible. Cuando todas tus piezas (reel, web, app, intro de logo) se mueven con el mismo "acento", la gente reconoce la marca antes de leer el nombre. Esto es la evolución del motion branding del núcleo (ver 84) hacia algo gobernable.

## Qué es el "vocabulario de movimiento"

Es el conjunto de gestos característicos de cómo se mueve tu marca. Igual que eliges 2 tipografías y 4 colores, eliges un puñado de comportamientos:
- **Cómo entran las cosas**: ¿aparecen (fade), se deslizan (slide), crecen (scale), rebotan (spring)?
- **Dirección dominante**: ¿de abajo hacia arriba? ¿desde el centro?
- **Carácter de la curva**: ¿suave y serio, o elástico y juguetón?

Elige UN vocabulario y repítelo. Si en un reel el logo rebota y en otro hace zoom dramático, no hay sistema.

## Tokens de motion (los valores de marca)

Igual que defines `color-primario = #1B5E3A`, defines tokens de movimiento reutilizables. Esto conecta con los design tokens (ver 87).

| Token | Ejemplo de valor | Uso |
|---|---|---|
| `duration-fast` | 150 ms | Microinteracciones |
| `duration-base` | 300 ms | Transiciones de estado |
| `duration-slow` | 500 ms | Transiciones de pantalla / entradas grandes |
| `ease-entrada` | `cubic-bezier(0.16, 1, 0.3, 1)` | Todo lo que aparece |
| `ease-salida` | `cubic-bezier(0.7, 0, 0.84, 0)` | Todo lo que desaparece |
| `ease-mover` | `cubic-bezier(0.65, 0, 0.35, 1)` | Movimiento entre puntos |
| `stagger` | 60 ms | Retraso entre elementos de una lista |

**Stagger** (escalonado): cuando una lista de items entra, no aparecen todos a la vez; cada uno entra ~60 ms después del anterior. Crea ritmo y guía el ojo de arriba a abajo. Es una de las firmas de motion más elegantes y baratas de lograr.

## Niveles del sistema

| Nivel | Qué incluye | Quién lo usa |
|---|---|---|
| **Marca** | Logo intro/outro, transiciones de video, vocabulario | Editor de video, motion designer |
| **Producto/UI** | Microinteracciones, transiciones, tokens | Equipo de desarrollo (web/app) |
| **Comunicación** | Plantillas de reel/story animadas | Community manager, dueño |

Los tres deben compartir el mismo "acento". Un menú de la app y un reel de Instagram deben sentirse de la misma marca aunque uno dure 200 ms y otro 30 s.

## Cómo definir el vocabulario (proceso)

1. **Parte de la personalidad** (ver 14): ¿la marca es serena o ágil? Eso fija velocidad y rebote.
2. **Elige el gesto raíz**: el movimiento del isotipo. Todo lo demás deriva de ahí.
3. **Define 2–3 entradas y 2–3 salidas** y prohíbe el resto.
4. **Fija los tokens** (tabla de arriba) con valores concretos.
5. **Documenta con ejemplos en video**, no solo en texto. "Slide-up con ease-out de 300 ms" se entiende mejor viéndolo.

## Guidelines de motion (qué documentar)

- Vocabulario de entrada/salida con ejemplos en video.
- Tabla de tokens (duraciones, curvas, stagger).
- Reglas del logo: cuándo se anima y cuándo está quieto (ver 143).
- Do/don't con clips: "así sí, así no".
- Excepciones: dónde el movimiento se reduce o se apaga (accesibilidad — respetar `prefers-reduced-motion`, que apaga animaciones para usuarios sensibles al movimiento).

## Referentes reales con sistema de motion fuerte
- **Stripe**: microinteracciones suaves, consistentes, casi invisibles pero presentes.
- **Apple**: easing lento y deliberado, sensación de peso y precisión.
- **Duolingo**: vocabulario elástico/juguetón coherente entre app, web y redes.
- **Mailchimp**: movimiento con carácter ilustrado, reconocible.

## Errores comunes
- Definir colores y tipografías pero dejar el motion al azar de cada editor.
- Diez entradas distintas → ningún acento reconocible.
- Tokens solo en texto, sin video → cada quien lo interpreta distinto.
- Ignorar accesibilidad (no respetar reduced-motion).

## Mini-checklist
- [ ] Vocabulario de movimiento definido (un acento, no diez)
- [ ] Tokens de duración y easing fijados con valores
- [ ] Stagger definido para listas
- [ ] Guidelines documentadas con ejemplos en video
- [ ] Coherencia entre marca, UI y comunicación
- [ ] Regla de accesibilidad (reduced-motion) contemplada

**Siguiente paso**: lleva el sistema al producto digital, donde el motion debe ser funcional y casi invisible — las microinteracciones (ver 142). Para implementarlo en web/React, la skill hermana **motion-framer** genera el código de Framer Motion.
