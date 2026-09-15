# 123 — Documentación viva

Un design system sin documentación es un cajón de herramientas sin etiquetas: nadie sabe cuál usar ni para qué. La **documentación viva** es la capa que explica cada pieza —cómo se ve, cómo se usa, cuándo NO usarla— y que se actualiza junto con el sistema. "Viva" porque si se congela, miente, y un documento que miente es peor que ninguno.

## Qué documentar (y qué no)
Documentar de menos deja huérfano al equipo; documentar de más es trabajo que nadie lee. El punto justo, por componente:

| Sección | Qué incluye |
|---|---|
| Qué es | Una frase: para qué sirve esta pieza |
| Anatomía | Sus partes nombradas (label, icono, contenedor) |
| Estados | Default, hover, foco, deshabilitado, error, cargando |
| Variantes | Tipos y tamaños, con cuándo usar cada uno |
| Do / Don't | Ejemplos visuales de uso correcto e incorrecto |
| Accesibilidad | Contraste, foco de teclado, texto alternativo (ver 128) |
| Código | Cómo llamarlo: `<Button variant="primary">` |

No documentes lo obvio. Documenta las **decisiones** y los **límites**: por qué este botón existe y dónde se rompe.

## Do / Don't: la sección más útil
Los ejemplos de "hazlo así / no así" enseñan más que cualquier párrafo. Reglas:
- Muéstralos en pareja, lado a lado.
- "Don't" siempre con el porqué: *no uses dos botones primarios juntos — compiten por la atención*.
- Casos reales que ya viste fallar, no inventados.

```
✓ DO              ✗ DON'T
[ Guardar ]       [ Guardar ] [ Cancelar ]
[ Cancelar ]      ← dos primarios compiten;
← 1 acción          el secundario debe ser ghost
  principal clara
```

## Herramientas reales (a 2026)
| Herramienta | Para qué | Quién la usa |
|---|---|---|
| **Storybook** | Documenta componentes de **código** vivos e interactivos; cada estado probable | equipos con devs |
| **Zeroheight** | Conecta Figma + texto en un sitio bonito para todo el equipo (no técnicos incluidos) | diseño + negocio |
| **Notion / Google Sites** | Documentación ligera para proyectos chicos | freelancers, marcas pequeñas |
| **Página propia** | Sitio a medida (como hacen Polaris, Material) | empresas con recursos |

**Storybook** es el estándar para componentes reales en código: muestra el botón funcionando, no una captura. **Zeroheight** brilla cuando necesitas que diseñadores Y gente de negocio lean lo mismo, sincronizado con Figma. Para Lushows: empieza en **Notion** o una página simple; sube a Zeroheight cuando el equipo crezca.

## El principio "single source of truth"
La documentación debe ser el **único** lugar al que todos van. Si hay tres versiones (un PDF viejo, un Figma, un chat de WhatsApp), gana el caos. Reglas:
- Un solo enlace canónico, conocido por todos.
- Lo que no está documentado, no existe (no es parte del sistema).
- Si una pieza cambia, la doc cambia en el mismo movimiento.

## Cómo mantenerla VIVA (la parte que casi todos fallan)
La documentación muere por abandono, no por mala redacción. Para evitarlo:
- [ ] **Regla de oro**: ningún componente se considera "terminado" hasta estar documentado.
- [ ] La doc vive **al lado del sistema**, no en otro silo (Storybook lee el código real; Zeroheight lee Figma real).
- [ ] Pon **fecha de última revisión** visible en cada página.
- [ ] Asigna un dueño que revise trimestralmente (ver 124 gobernanza).
- [ ] Borra lo deprecado: marca claramente lo obsoleto, no lo dejes confundir.

## Estructura recomendada de un sitio de doc
```
Inicio              → qué es el sistema, cómo empezar
Fundamentos         → tokens: color, tipografía, espacio, grid (ver 121)
Componentes         → uno por página, con la tabla de arriba
Patrones            → formularios, navegación, tablas
Recursos            → descargas, librería Figma, contacto
Changelog           → qué cambió y cuándo
```
El **changelog** (registro de cambios) es subestimado: que el equipo vea "v2.1 — botón ahora con estado loading" genera confianza y evita sorpresas.

## Tono de la documentación
- Directo y en segunda persona: "Usa el botón primario para la acción principal".
- Sin jerga innecesaria; si usas un término técnico, defínelo una vez.
- Ejemplos antes que teoría.
- Honesto sobre límites: "este componente aún no soporta modo oscuro".

## Errores comunes
- Doc en un PDF que nadie actualiza → mejor un sitio vivo.
- Solo capturas de pantalla → se desactualizan al instante; usa componentes reales.
- Documentar el "qué" pero no el "cuándo" / "cuándo no".
- Sin changelog → el equipo no sabe qué cambió.
- Tres fuentes de verdad compitiendo.

## Para Lushows (no técnico)
Tu documentación mínima viable: una página de Notion con (1) la paleta y tipografías, (2) los 5 componentes clave con su do/don't, (3) un enlace al Figma. Una página, un enlace, siempre actualizada. Con eso ya estás por encima del 90% de las marcas pequeñas.

## Mini-checklist
- [ ] Cada componente con qué es / estados / variantes / do-don't
- [ ] Sección de accesibilidad por componente (ver 128)
- [ ] Un único enlace canónico conocido por todos
- [ ] Doc conectada al sistema real (Storybook/Zeroheight), no capturas sueltas
- [ ] Changelog y fecha de revisión visibles
- [ ] Un dueño responsable de mantenerla

**Siguiente paso**: documentar es parte de un proceso mayor. Pasa a 124 design ops a escala para ver cómo se gobierna, versiona y contribuye al sistema con un equipo.
