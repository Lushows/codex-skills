# 142 — Microinteracciones y UI motion

Una **microinteracción** es la pequeña respuesta animada que da una interfaz cuando haces algo: el botón que se hunde al pulsarlo, el corazón que late al dar "me gusta", el switch que se desliza, el campo que tiembla cuando escribes mal la contraseña. Son diminutas (100–300 ms) pero definen si una app se siente viva y de calidad o muerta y barata. Aquí el motion es función pura: confirma, orienta y tranquiliza. Nada de adorno.

## Anatomía de una microinteracción (Dan Saffer)

| Parte | Qué es | Ejemplo |
|---|---|---|
| **Disparador (trigger)** | Lo que la inicia | Click, hover, scroll, carga de datos |
| **Reglas** | Qué pasa | Al pulsar, el botón se comprime y cambia de color |
| **Feedback** | Lo que ves/sientes | La compresión + un check que aparece |
| **Bucle/modo** | Qué pasa si se repite o queda en espera | Spinner que gira mientras carga |

## Las 4 funciones del UI motion

1. **Feedback**: "te escuché". El botón reacciona al tap → el usuario sabe que registró.
2. **Estado**: muestra que algo cambió (toggle on/off, item agregado al carrito).
3. **Orientación espacial**: de dónde viene y a dónde va algo. Un panel que entra desde la derecha enseña dónde "vive" y cómo cerrarlo.
4. **Continuidad**: conecta dos pantallas para que el cambio no sea un salto brusco (transición compartida).

Si una animación no cumple ninguna de las 4 → probablemente sobra.

## Duraciones (en UI, corto es rey)

| Interacción | Duración | Nota |
|---|---|---|
| Hover / tap feedback | 100–150 ms | Casi instantáneo |
| Toggle / switch | 150–250 ms | Se ve el recorrido sin demora |
| Abrir menú / dropdown | 200–300 ms | Con ease-out |
| Transición de pantalla | 300–500 ms | Con dirección coherente |
| Aparición de toast/notificación | 200 ms entrada, 150 ms salida | Salida más rápida que entrada |

Regla de oro: en UI, **si dudas entre rápido y lento, elige rápido.** Una animación que estorba al tercer uso es peor que ninguna.

## Estados que SIEMPRE deben tener motion

- **Loading**: skeleton (esqueleto gris pulsante) o spinner. Nunca pantalla congelada.
- **Éxito**: check animado, confeti sutil en momentos clave (no en cada acción).
- **Error**: shake (temblor) o color rojo que aparece — orienta sin texto.
- **Vacío**: ilustración con micro-movimiento que invita a la primera acción.

## Función sobre adorno: el filtro

Antes de animar algo en UI, pregunta:
- ¿Confirma una acción? (feedback)
- ¿Explica un cambio? (estado)
- ¿Orienta en el espacio? (¿de dónde vino?)
- ¿Suaviza una transición brusca?

Si la respuesta a las cuatro es "no", no animes. El motion decorativo en UI **ralentiza la tarea** y molesta a quien usa la app 50 veces al día.

## Accesibilidad (obligatorio)

Algunas personas sienten mareo/náusea con movimiento. El sistema operativo expone `prefers-reduced-motion`. Tu UI debe **reducir o apagar** animaciones cuando esté activo (reemplazar slides por fades simples, quitar parallax y rebotes). No es opcional en producto serio.

## Referentes reales
- **Stripe / Linear**: microinteracciones casi invisibles, rapidísimas, premium.
- **iOS**: transiciones compartidas (un icono que se "abre" en pantalla completa).
- **Things / Notion**: feedback de tap sutil que da sensación de calidad.

## Puente a web (motion-framer)

Para implementar esto en web/app real:
- **CSS transitions**: para hover, toggles simples (lo más ligero).
- **Framer Motion** (React): para microinteracciones complejas, springs, gestos, transiciones de layout. La skill hermana **motion-framer** genera este código directamente.
- **Web Animations API**: control fino sin librería.

Mapa rápido: hover/tap simple → CSS; animación con física/gesto/layout → Framer Motion (ver 149 herramientas).

## Errores comunes
- Animaciones largas (>400 ms) en acciones frecuentes.
- Confeti/celebración en cada click (pierde el "momento").
- Ningún feedback al pulsar (la app se siente rota aunque funcione).
- Transiciones sin dirección coherente (entra por la derecha, sale por arriba).
- Ignorar `prefers-reduced-motion`.

## Mini-checklist
- [ ] Cada animación cumple una de las 4 funciones
- [ ] Duraciones cortas (100–300 ms para microinteracciones)
- [ ] Estados de loading, éxito y error con motion
- [ ] Feedback en cada acción tocable
- [ ] Direcciones de transición coherentes
- [ ] `prefers-reduced-motion` respetado

**Siguiente paso**: el activo de motion más visible de la marca es su logo en movimiento — cómo animar la intro, el loader y el reveal sin caer en lo genérico (ver 143 logo animation y brand reveal).
