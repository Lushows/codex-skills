# 137 — IA + design systems: variantes sin perder coherencia

Cuando la marca toca producto digital (web, app, dashboard), la IA puede acelerar el diseño de UI y componentes. Pero la UI tiene una exigencia que la imagen no: **sistema**. Botones, espaciados, tipografía y color deben ser CONSISTENTES y reutilizables, no piezas sueltas bonitas. La IA genera variantes a chorro; el humano cura y mantiene el sistema. Este módulo explica cómo usar IA en UI sin romper la coherencia.

> Las herramientas de IA-a-UI cambian rápido — verifica el estado actual.

---

## Qué puede hacer la IA en UI hoy

| Tarea | Herramientas (ejemplos) | Valor |
|---|---|---|
| **Generar pantallas/maquetas** | v0, Figma (IA), Galileo, Lovable | Arrancar rápido, explorar layouts |
| **Componentes desde prompt** | v0, Cursor, generadores React | Botones, cards, formularios base |
| **Variantes de un componente** | Figma IA, plugins | Estados, tamaños, temas |
| **Texto de UI (microcopy)** | LLMs (Claude/GPT) | Labels, mensajes, placeholders |
| **De diseño a código** | v0, Figma Dev Mode IA | Acelerar handoff |

> Ver 92 sistema de marca (núcleo) y la skill desingweb-lushows para construir UI premium real.

---

## El riesgo central: INCOHERENCIA

La IA genera cada pantalla como una isla. Pides 5 pantallas y obtienes 5 botones distintos, 5 espaciados, 5 azules. Eso NO es un design system, es caos bonito. El sistema requiere:

- **Tokens**: color, espaciado, tipografía, radios, sombras definidos UNA vez.
- **Componentes reutilizables**: un solo botón con sus variantes, no veinte botones.
- **Reglas**: cuándo se usa cada cosa.

La IA no mantiene esto sola. El humano define los tokens y FUERZA a la IA a usarlos.

---

## Cómo usar IA sin romper el sistema

```
1. Define los tokens de marca PRIMERO (color HEX, escala tipográfica,
   espaciado 4/8px, radios) ← humano, ver 92
2. Dale esos tokens a la IA como contexto en cada prompt
3. La IA genera variantes DENTRO de esas reglas
4. Curas: descartas lo que rompe el sistema
5. Consolidas en componentes reutilizables (Figma/código)
```

Prompt de UI con sistema:

```
Diseña una card de producto usando ESTE sistema:
color primario #0E7C5A, fondo #0B1410, texto #E8EFE9,
tipografía sans geométrica, espaciado en múltiplos de 8px,
radio 12px, sombra suave. Estilo: premium, oscuro, calmado.
Variantes: default, hover, agotado.
```

Sin pasarle el sistema, la IA inventa el suyo y rompe la coherencia.

---

## Dónde la IA ayuda de verdad

- **Explorar layouts** al inicio (diverger rápido).
- **Generar muchas variantes** de un componente para elegir estados.
- **Microcopy** consistente (labels, errores, vacíos).
- **Prototipos** para validar con usuarios antes de invertir.
- **Acelerar el código base** que luego un dev refina.

---

## Dónde el humano es insustituible

- **Definir y mantener los tokens** y reglas del sistema.
- **Jerarquía visual y flujo** (qué mira el usuario primero).
- **Accesibilidad** (contraste, tamaños táctiles, foco) — la IA falla seguido aquí.
- **Coherencia entre pantallas** — curar para que todo sea una sola voz.
- **Decisiones de marca** (no toda UI bonita es TU marca).

> La IA acelera el músculo, no reemplaza el cerebro del sistema.

---

## Checklist de IA en design systems

- [ ] Definí tokens de marca ANTES de generar (color, tipo, espaciado, radios).
- [ ] Pasé los tokens a la IA en cada prompt.
- [ ] Curé las variantes: descarté lo que rompe el sistema.
- [ ] Consolidé en componentes reutilizables, no piezas sueltas.
- [ ] Verifiqué accesibilidad (contraste, tamaños) a mano.
- [ ] Todas las pantallas se ven de la misma marca.

---

**Siguiente paso:** lee 138 sobre derechos, ética y autoría de la IA en 2026 — clave antes de entregar trabajo IA a un cliente que paga.
