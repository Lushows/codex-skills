# 127 — Handoff diseño → desarrollo

El **handoff** es el momento en que un diseño pasa a manos de quien lo programa. Es donde más valor se pierde: el diseño se ve perfecto en Figma y el producto final sale "parecido pero no igual" —otro azul, otro espacio, otra tipografía—. Un buen handoff no es "te paso el archivo"; es entregar el diseño de forma que el código pueda replicarlo **exacto** y sin adivinar. Este módulo es cómo reducir esa fricción a cero.

## El problema de las dos verdades
El diseñador piensa en pixeles y capas; el dev piensa en componentes, propiedades y tokens. Si cada uno habla su idioma, el resultado diverge. La solución no es que uno aprenda el del otro, sino tener un **idioma común**: los **tokens** (ver 121). Cuando ambos dicen "color-action" en vez de "ese verde", el handoff casi se resuelve solo.

## Qué necesita un dev para no adivinar
| Necesita | Malo | Bueno |
|---|---|---|
| Color | "el verde" | token `color-action` (#1B5E20) |
| Espacio | "un poco de aire" | `space-md` = 16px |
| Tipografía | "grande y bold" | `text-xl` / 700 / line-height 1.2 |
| Estados | solo el normal | normal, hover, foco, deshabilitado, error, cargando |
| Comportamiento | — | qué pasa al hacer clic, al validar, al cargar |
| Casos límite | el caso feliz | texto largo, lista vacía, error de red |

La mitad de los bugs de interfaz nacen de **estados y casos límite no especificados**. El diseño feliz es fácil; entrega también el vacío, el error y el cargando.

## Dev Mode de Figma (el puente moderno)
A 2026, **Dev Mode** es el canal estándar:
- El dev **inspecciona** medidas, colores y tipos sin abrir el diseño como editor.
- Si conectaste variables a tokens, ve `color-action`, no un hex suelto → habla el idioma del sistema.
- Exporta assets (íconos, imágenes) en el formato correcto (ver 93).
- Marca frames "**ready for dev**" para que sepa qué está listo y qué aún se mueve.
- **Code Connect** (a 2026) puede mostrarle, junto al componente de Figma, el snippet real del componente de código → cierra el círculo diseño↔código.

## De tokens a CSS (la entrega que de verdad sirve)
Lo ideal: el dev no copia valores a mano, los **importa**. Con **Style Dictionary** (ver 121) tus tokens JSON se vuelven variables CSS automáticamente:
```css
:root {
  --color-action: #1B5E20;
  --space-md: 16px;
  --radius-button: 12px;
  --text-xl: 1.8rem;
}
```
Y el dev escribe:
```css
.button { background: var(--color-action); padding: var(--space-md); }
```
Resultado: si mañana cambias el verde en el token, el producto se actualiza sin tocar 40 archivos. **Cero copiar-pegar de hex** = cero deriva.

## La conversación, no solo el archivo
El mejor handoff incluye un **traspaso hablado**, no solo un enlace:
- [ ] Recorrido de 15 min: el diseñador explica intención y prioridades.
- [ ] El dev pregunta los casos límite ahí mismo.
- [ ] Se acuerda qué es "negociable" (si algo es técnicamente caro, ¿hay plan B?).
- [ ] Se define quién revisa el resultado final contra el diseño (ver 129 design QA).

Tirar un archivo por chat y desaparecer es la receta del "no quedó como lo diseñé".

## Checklist de un frame listo para entregar
- [ ] Usa componentes del sistema (no piezas sueltas dibujadas a mano)
- [ ] Todos los colores/espacios/tipos son tokens, no valores random
- [ ] Auto-layout aplicado (el dev ve la estructura flex, ver 122)
- [ ] Todos los estados presentes (hover, foco, error, vacío, cargando)
- [ ] Comportamiento responsivo indicado (qué pasa en móvil, ver 126)
- [ ] Assets exportables marcados y nombrados (ver 87)
- [ ] Notas de accesibilidad (foco, contraste, alt, ver 128)
- [ ] Marcado "ready for dev"

## Reducir fricción a futuro
La mejor entrega es la que casi no necesita explicación porque el sistema ya está alineado:
- Mismos nombres de tokens en Figma y en código.
- Componentes que existen en ambos lados (Code Connect).
- Documentación viva como referencia compartida (ver 123).
Mientras más maduro el design system, más trivial el handoff.

## Errores comunes
- Entregar solo el caso feliz, sin estados ni vacíos.
- Hex y medidas a copiar a mano → derivan al instante.
- Sin conversación: archivo lanzado y silencio.
- No marcar qué está listo vs. en progreso.
- Olvidar accesibilidad → el dev no sabe el orden de foco ni los alt.

## Para Lushows (no técnico)
Cuando contrates a alguien para programar un diseño, exige tres cosas: (1) que reciba los **valores como variables** (no que copie colores a ojo), (2) que le entregues **todos los estados** (qué pasa al error, al cargar), y (3) una **llamada de traspaso**. Con eso evitas el 80% de los "no quedó igual".

## Mini-checklist
- [ ] Tokens compartidos diseño↔código (mismo nombre)
- [ ] Dev Mode con frames "ready for dev"
- [ ] Tokens → CSS automatizado (sin copiar hex)
- [ ] Todos los estados y casos límite entregados
- [ ] Traspaso hablado + dueño de la revisión final
- [ ] Notas de accesibilidad incluidas

**Siguiente paso**: la accesibilidad no es un extra del handoff, es parte del sistema. Pasa a 128 accesibilidad como sistema.
