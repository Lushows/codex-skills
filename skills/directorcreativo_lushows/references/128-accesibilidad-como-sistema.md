# 128 — Accesibilidad como sistema

La **accesibilidad** (a menudo abreviada **a11y**) es diseñar para que cualquier persona pueda usar tu producto: quien no ve bien, quien no puede usar mouse, quien navega con lector de pantalla, quien tiene poca luz o una mano ocupada. La gran idea de este módulo: la accesibilidad no es una revisión final que se "agrega" al final —se **embebe en el sistema**, en cada componente, de modo que sea correcta por defecto y nadie tenga que acordarse de ella. Ver 35 contraste y accesibilidad para los fundamentos de color.

## Por qué importa (más allá de lo correcto)
- Es **más gente que te puede comprar/usar** (15-20% de la población tiene alguna discapacidad).
- En muchos países es **ley** (riesgo legal real).
- Lo accesible suele ser **mejor para todos**: buen contraste, foco visible y textos claros ayudan a cualquiera bajo el sol o con prisa.

## El estándar: WCAG 2.2 (y hacia dónde va)
**WCAG** (Web Content Accessibility Guidelines) es la norma mundial. A 2026 la versión vigente es **WCAG 2.2**. Tiene tres niveles: **A** (mínimo), **AA** (el objetivo real de la industria) y **AAA** (exigente). Apunta a **AA**.

Se organiza en cuatro principios (POUR):
| Principio | Significa | Ejemplo |
|---|---|---|
| **Perceptible** | se puede percibir | contraste suficiente, alt en imágenes |
| **Operable** | se puede usar | todo accesible con teclado |
| **Comprensible** | se entiende | errores claros, orden lógico |
| **Robusto** | funciona con tecnologías de apoyo | compatible con lectores de pantalla |

**Hacia 3.0 y APCA**: se está desarrollando WCAG 3.0, con un nuevo método de contraste llamado **APCA** (Advanced Perceptual Contrast Algorithm), que mide el contraste de forma más fiel a cómo el ojo percibe (mejor con texto claro sobre oscuro, mejor en pantallas modernas). A 2026 **AA de WCAG 2.2 sigue siendo el requisito**; APCA es el futuro a vigilar, aún no obligatorio.

## Los números que debes conocer (contraste)
| Caso | Mínimo AA |
|---|---|
| Texto normal vs. fondo | **4.5:1** |
| Texto grande (≥24px o 18.66px bold) | **3:1** |
| Íconos/bordes de UI vs. fondo | **3:1** |

Verifícalo con herramientas reales: el chequeador de contraste de **WebAIM**, los plugins de contraste en Figma, o **APCA** para mirar al futuro. No lo juzgues a ojo: lo que "se ve bien" a veces falla la medición (ver 35).

## Embeber a11y en cada componente (la clave del módulo)
En vez de auditar al final, haz que cada componente del sistema **nazca accesible**:

| Componente | Accesibilidad embebida |
|---|---|
| Botón | foco visible, área táctil ≥44px, contraste AA |
| Input | label SIEMPRE asociado, error con texto (no solo color) |
| Link | distinguible sin depender solo del color |
| Modal | foco atrapado dentro, cierra con Esc, devuelve foco al salir |
| Toast/alerta | anunciado a lectores de pantalla, no solo visual |
| Ícono solo | texto alternativo (no un botón mudo) |

Si el botón del sistema ya cumple, **toda pantalla que lo use cumple**. La accesibilidad se vuelve la opción por defecto, no una tarea extra. Documenta estas reglas en cada componente (ver 123).

## Los tres pilares prácticos
1. **Contraste** (perceptible) — texto y elementos legibles (números de arriba).
2. **Foco** (operable) — el **foco** es el recuadro que indica dónde estás al navegar con teclado (Tab). Debe ser **siempre visible** y seguir un orden lógico. Nunca lo elimines "porque es feo": rediséñalo.
3. **Teclado** (operable) — todo lo que se hace con mouse debe hacerse con teclado (Tab para moverse, Enter/Espacio para activar, Esc para cerrar).

## Errores que dependen solo del color
Un clásico: marcar el error de un campo **solo** en rojo. Quien no distingue rojo/verde no lo nota. Regla: **el color nunca es el único portador de información**. Acompáñalo con ícono, texto o forma:
```
✗ borde rojo, nada más
✓ borde rojo + ícono + "El correo no es válido"
```

## Texto alternativo y semántica
- **Alt text**: describe imágenes con función (un gráfico, un producto). Las decorativas van con alt vacío para que el lector las ignore.
- **Estructura semántica**: títulos en orden (no saltes de H1 a H4), botones que son botones (no imágenes clicables). Esto deja que los lectores de pantalla "entiendan" la página.

## Cómo probar (real, no teórico)
- [ ] Navega TODA la pantalla solo con el teclado (sin tocar el mouse).
- [ ] Pasa un chequeador de contraste a textos y UI.
- [ ] Activa un lector de pantalla y escucha si tiene sentido.
- [ ] Usa herramientas automáticas (axe, Lighthouse) — atrapan ~30-50%; el resto es manual.
- [ ] Sube el zoom al 200%: ¿sigue usable?

## Para Lushows (no técnico)
Tres pruebas que tú mismo puedes hacer en el dashboard de BIO-SETA o en la web: (1) ¿puedo recorrer todo con la tecla **Tab** y ver dónde estoy?, (2) ¿el texto se lee con buen contraste (no gris claro sobre blanco)?, (3) ¿los errores dicen algo escrito, no solo se ponen rojos? Si las tres pasan, vas muy por delante del promedio.

## Mini-checklist
- [ ] Objetivo WCAG 2.2 nivel AA
- [ ] Contraste: 4.5:1 texto, 3:1 grande/UI (medido, no a ojo)
- [ ] Foco siempre visible y en orden lógico
- [ ] Todo operable con teclado (Tab/Enter/Esc)
- [ ] El color nunca es el único indicador
- [ ] Alt text en imágenes con función
- [ ] Accesibilidad documentada por componente
- [ ] Probado con teclado + lector de pantalla, no solo automático

**Siguiente paso**: para sostener accesibilidad y consistencia a escala, hay que automatizar la vigilancia. Pasa a 129 design QA y governance.
