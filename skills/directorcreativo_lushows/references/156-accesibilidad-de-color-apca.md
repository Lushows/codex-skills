# 156 — Accesibilidad de color: APCA

En el 35 aprendiste la regla clásica de contraste: 4.5:1. Funciona, pero tiene fallas conocidas — a veces rechaza combinaciones que SÍ se leen bien, y aprueba otras que NO. La nueva generación de WCAG (versión 3, aún en borrador a junio 2026) trae un modelo mejor: **APCA**. Este módulo te lo explica simple, para que tomes mejores decisiones de color sin esperar a que sea ley. Es la versión "pro" del 35 contraste y accesibilidad.

## El problema del viejo 4.5:1
La fórmula clásica (WCAG 2) trata todos los colores con la misma vara y NO considera:
- Que el ojo percibe distinto el texto **oscuro sobre claro** vs. **claro sobre oscuro** (importa muchísimo en dark mode, ver 155).
- El **tamaño y grosor** real de la letra (un texto fino necesita más contraste que uno grueso).
- Cómo funciona la luz en pantallas modernas.

Resultado: con WCAG 2 a veces un texto "aprobado" se lee fatal, y un texto "rechazado" se lee perfecto.

## Qué es APCA
**APCA** (Accessible Perceptual Contrast Algorithm) mide el contraste según cómo el OJO HUMANO lo percibe de verdad. En vez de un ratio tipo 4.5:1, da un valor **Lc** (Lightness contrast) de **0 a ~106**, que puede ser positivo o negativo.

| Valor | Significa |
|---|---|
| **Lc ±0–14** | Invisible, no usar para nada |
| **Lc ±15–29** | Solo elementos decorativos/inactivos |
| **Lc ±30–44** | Texto grande/grueso, placeholders |
| **Lc ±45–59** | Texto secundario, subtítulos |
| **Lc ±60–74** | Texto de cuerpo normal — el objetivo |
| **Lc ±75–90+** | Texto fino, cuerpos largos, máxima comodidad |

El **signo** importa: positivo = texto oscuro sobre fondo claro; negativo = texto claro sobre fondo oscuro. APCA distingue los dos casos (WCAG 2 no).

## Cómo se usa (regla práctica para no técnicos)
1. Para **texto de cuerpo** (lo que se lee mucho): apunta a **Lc 75** o más.
2. Para **titulares grandes y gruesos**: **Lc 60** basta.
3. Para **texto secundario o etiquetas**: **Lc 45–60**.
4. Para **bordes, iconos, elementos de UI**: **Lc 30** mínimo.

No calculas a ojo: usa una herramienta (abajo) que te da el Lc de cualquier par de colores.

## APCA vs. WCAG 2: ¿cuál uso hoy?
- **Legalmente / para auditorías formales:** WCAG 2 AA (4.5:1) sigue siendo el estándar exigible en 2026. Cúmplelo SIEMPRE.
- **Para diseñar mejor:** usa APCA como guía de calidad. Si pasa 4.5:1 Y tiene buen Lc, vas perfecto. Si APCA dice que algo se lee mal aunque pase 4.5:1, créele a APCA y mejóralo.
- En la práctica: **cumple WCAG 2 como piso legal, optimiza con APCA como techo de calidad.**

## Herramientas
| Herramienta | Para qué |
|---|---|
| **apcacontrast.com** | Calculadora oficial APCA, da el Lc |
| **Polypane / Contrast** apps | Revisan toda la página |
| **Figma plugins** (Contrast, APCA) | Dentro del diseño |
| **DevTools del navegador** | Ya muestran APCA en versiones recientes |

## Daltonismo avanzado (más allá del 35)
El 8% de los hombres tiene daltonismo. Tipos y qué confunden:
| Tipo | Confunde | Frecuencia |
|---|---|---|
| **Deuteranopía/-anomalía** | Verde ↔ rojo (la más común) | ~5% hombres |
| **Protanopía/-anomalía** | Rojo ↔ verde, y el rojo se ve oscuro | ~2% hombres |
| **Tritanopía** | Azul ↔ amarillo | Rara |
| **Acromatopsia** | Todo (ve en grises) | Muy rara |

Reglas para diseñar inclusivo:
- [ ] Nunca uses SOLO color para informar (refuerza con icono, texto, forma, posición — ver 35).
- [ ] Evita el par rojo/verde como única distinción (semáforos de datos: añade ✓/✗ o texto).
- [ ] Para series de datos, usa paletas seguras: azul + naranja distinguen para casi todos los tipos.
- [ ] Prueba en escala de grises: si se entiende, no dependes del color.
- [ ] Simula daltonismo con herramientas (Sim Daltonism, Stark en Figma) sobre tus pantallas reales.

## Ejemplo trabajado
CTA de marca: texto sobre botón verde `#16A34A`.
- Texto blanco `#FFF`: WCAG 2 da ~2.8:1 → FALLA. APCA da Lc ~52 → solo aceptable para texto grande, no ideal.
- Texto negro `#0A0A0A`: WCAG 2 da ~7.5:1 ✓. APCA da Lc ~78 → excelente para cualquier texto.
- Decisión: **texto oscuro sobre el verde** (coincide con la lección del 35: verdes/amarillos medios piden texto oscuro). Y como el verde "éxito" también marca estado, se acompaña con un icono ✓ para los usuarios daltónicos.

## Siguiente paso
Toma tus 5 combinaciones de color más usadas (texto/fondo, botones, enlaces) y pásalas por apcacontrast.com. Asegúrate de Lc ≥ 75 en cuerpo y ≥ 60 en titulares, manteniendo el piso legal de WCAG 2 AA (35). Simula daltonismo sobre una pantalla real antes de cerrar la paleta (33, 34).
