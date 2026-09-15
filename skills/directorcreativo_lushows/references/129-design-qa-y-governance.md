# 129 — Design QA y governance

Diseñar bien una vez es fácil; mantener todo consistente cuando hay muchas pantallas, muchas manos y muchas actualizaciones es lo difícil. **Design QA** (quality assurance de diseño) es el control de calidad que verifica que lo construido coincida con el sistema y no se degrade con el tiempo. **Governance** es el conjunto de reglas que lo sostiene. Este módulo cierra el bloque: cómo vigilar la consistencia a escala, mucho de ello automatizado, para que el sistema no se pudra (ver 98 checklist de calidad visual para la versión manual/de marca, y 124 para design ops).

## Qué es y por qué
Sin QA, el sistema se erosiona silenciosamente: un dev mete un color a mano, otro cambia un espacio "solo aquí", y a los seis meses tienes otra vez el caos que el sistema vino a resolver. Design QA atrapa esas desviaciones **antes** de que lleguen al producto en vivo.

## Los tres frentes de QA
| Frente | Pregunta que responde | Cómo |
|---|---|---|
| **Visual** | ¿se ve como debe? | comparar antes/después (visual regression) |
| **Consistencia** | ¿usa el sistema? | linting de tokens y componentes |
| **Accesibilidad** | ¿sigue siendo accesible? | chequeos automáticos + manuales (ver 128) |

## Visual regression testing (el guardián automático)
**Visual regression** = el sistema toma una "foto" de cada componente/pantalla y, en cada cambio, la compara con la versión aprobada. Si algo cambió sin querer —el botón se movió 3px, el color mutó— **avisa antes de publicar**.
```
versión aprobada  vs  versión nueva
   [botón]              [botón]      → ✓ igual, pasa
   [tarjeta]            [tarjeta]    → ✗ cambió el padding, ALERTA → revisar
```
Herramientas reales a 2026: **Chromatic** (hecho para Storybook, ver 123), **Percy**, **Playwright** con snapshots. Para Lushows esto es nivel avanzado, pero entender la idea importa: la máquina vigila que nada se rompa solo.

## Linting de tokens (consistencia automática)
**Lint** = una herramienta que revisa reglas automáticamente y marca infracciones. Aplicado al diseño:
- ✗ "este botón usa `#1B5E21` (un hex suelto) en vez del token `color-action`" → error.
- ✗ "este espacio es 15px, no está en la escala (8/16/24)" → error.
- ✗ "contraste 3.9:1, debajo de 4.5:1 AA" → error (ver 128).

Existen plugins de Figma que auditan un archivo y listan dónde se usaron valores fuera del sistema (capas con color/tipo sin token). En código, linters de CSS detectan hex sueltos donde debería haber variables. La meta: **que sea más fácil usar el sistema que saltárselo**.

## Checklist de revisión de diseño (QA manual)
Antes de aprobar una pantalla/componente nuevo:
- [ ] Usa solo componentes y tokens del sistema (cero valores sueltos)
- [ ] Espaciados en la escala definida (8/16/24…), no números random
- [ ] Tipografía de la escala, jerarquía correcta (ver 43)
- [ ] Todos los estados presentes (hover, foco, error, vacío, cargando)
- [ ] Contraste AA verificado (ver 128)
- [ ] Responsivo probado (móvil → desktop, ver 126)
- [ ] Naming de capas/componentes limpio
- [ ] Coincide con la documentación (ver 123)

## Governance: las reglas que lo sostienen
QA atrapa errores; governance evita que ocurran. Lo esencial (detalle en 124):
- **Quién aprueba** qué entra al sistema (un guardián con autoridad).
- **Cómo se contribuye** (flujo: propuesta → revisión → doc → publicación).
- **Cómo se versiona y deprecia** (semver + changelog).
- **Definition of done**: nada está "listo" sin doc, estados, accesibilidad y QA pasado.

## Métricas de consistencia (medir la salud)
No basta con sentir que está bien; mídelo:
- [ ] % de componentes "detached" o valores hardcodeados (mala señal, debe bajar).
- [ ] Cobertura: % de UI hecha con el sistema vs. piezas sueltas.
- [ ] Issues de accesibilidad abiertos.
- [ ] Tiempo desde que se detecta una desviación hasta que se corrige.
Tendencia importa más que el número absoluto: ¿mejora o empeora con el tiempo?

## Dónde encaja en el flujo de trabajo
```
Diseño → QA de diseño → Handoff → Build → QA visual/a11y automático → Publicar
            ↑ linting de tokens         ↑ visual regression
```
El QA no es una etapa al final: hay puntos de control en diseño (linting), en código (regression) y antes de publicar. Cuanto antes se atrapa una desviación, más barato corregirla.

## Errores comunes
- QA solo "a ojo" al final → se escapa lo sutil y lo acumulado.
- Sin linting → los hex sueltos se cuelan y el sistema se diluye.
- Sin visual regression → cambios rompen pantallas que nadie revisó.
- Reglas sin guardián que las haga cumplir → se ignoran.
- Medir nada → no sabes si el sistema mejora o se degrada.

## Para Lushows (no técnico)
Tu QA manual mínimo, sin herramientas caras: antes de dar por buena cualquier pantalla nueva, repasa que (1) los colores sean los de la marca (no inventados), (2) los espacios se sientan parejos con el resto, (3) pase las pruebas de accesibilidad del módulo 128. Si más adelante el producto crece con un equipo, ahí sí invierte en Storybook + Chromatic para que la máquina vigile por ti.

## Mini-checklist
- [ ] Checklist de revisión de diseño antes de aprobar
- [ ] Linting de tokens (no hex/espacios sueltos)
- [ ] Visual regression si hay producto con devs (Chromatic/Percy/Playwright)
- [ ] Chequeos de accesibilidad automáticos + manuales
- [ ] Governance: guardián, flujo de contribución, definition of done
- [ ] Métricas de consistencia con tendencia en el tiempo

**Siguiente paso**: cierras el bloque 12. Con sistema, tokens, doc, ops, responsive, handoff, accesibilidad y QA cubiertos, repasa el núcleo 59 (sistemas de diseño visual), 87 (tokens), 88 (consistencia omnicanal) y 89 (design ops) para conectar lo digital con la marca completa.
