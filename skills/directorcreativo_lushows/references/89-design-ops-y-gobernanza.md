# 89 — Design ops y gobernanza

Una marca no es un proyecto que se entrega y termina: es un activo vivo que hay que mantener años. Design ops y gobernanza son el "cómo se mantiene": quién decide, dónde viven los archivos, quién puede tocar la marca, cómo se capacita al equipo y cómo evoluciona sin romperse. Sin esto, hasta la mejor identidad se degrada en meses.

## El problema del día después
El estudio entrega la marca, cobra, se va. Seis meses después: el proveedor usó otro color, el nuevo empleado hizo un flyer en otra fuente, alguien encontró el logo viejo en una carpeta. Nadie fue malo — simplemente no había gobernanza. La marca se erosiona por mil decisiones pequeñas sin dueño.

## Las cuatro preguntas de gobernanza
1. **¿Quién aprueba?** — antes de que una pieza salga al mundo, ¿quién dice sí?
2. **¿Dónde está todo?** — ¿dónde vive la fuente de verdad de los assets?
3. **¿Quién puede tocar la marca?** — ¿quién diseña, quién solo usa plantillas?
4. **¿Cómo cambia?** — ¿cómo evoluciona sin que cada quien improvise?

Responde estas cuatro y tienes gobernanza.

## 1. Quién aprueba (el guardián de marca)
Define un **brand guardian**: una persona (en negocio chico, el dueño) que da el visto bueno final a piezas importantes antes de publicar/imprimir. No para frenar todo — para evitar que salga lo que rompe la marca.

Niveles de aprobación según riesgo:
| Pieza | Aprobación |
|---|---|
| Post de plantilla existente | El community publica directo |
| Pieza nueva (flyer, valla, empaque) | Pasa por el guardián |
| Cambio de logo/color/fundamento | Solo el dueño + diseñador |

## 2. Dónde vive todo (biblioteca central)
Una **única fuente de verdad** (single source of truth): la carpeta/sistema donde están los assets correctos y actualizados (ver 87). Reglas:
- Un solo lugar oficial (Drive/Dropbox/Notion/Figma compartido).
- Las versiones viejas se archivan en una subcarpeta "_ARCHIVO", no en la principal.
- Todos los proveedores reciben los archivos de AHÍ, no de un correo viejo.
- Si hay web/app, los design tokens viven versionados (ver 87).

Si el logo correcto solo lo tiene el diseñador en su compu, no hay gobernanza: hay un punto único de falla.

## 3. Quién puede tocar la marca (roles)
| Rol | Puede |
|---|---|
| Dueño / guardián | Aprobar, decidir cambios de fondo |
| Diseñador | Crear piezas nuevas dentro del sistema |
| Community / equipo | Usar plantillas, no inventar |
| Proveedores externos | Producir con los archivos oficiales, sin "mejorar" |

La frase clave para proveedores: "usa exactamente estos archivos; no recrees ni ajustes el logo". El imprentero "creativo" es el mayor enemigo de la consistencia.

## 4. Cómo evoluciona la marca (evolución controlada)
Las marcas deben evolucionar — pero con criterio, no por capricho:
- **Refresh** (ajuste): afinar color, tipografía, aplicaciones. Frecuente, sano.
- **Rediseño** (cambio mayor): nuevo logo/concepto. Raro, justificado por estrategia.
- **Regla**: cambia por una razón de negocio (nuevo público, nuevo posicionamiento), no porque "ya aburre". Coca-Cola lleva un siglo casi igual; cambiar tu logo cada año destruye el reconocimiento que tanto cuesta construir (ver 88).

Cuando cambies: actualiza el manual, la biblioteca, retira versiones viejas de TODOS los puntos, comunica al equipo y proveedores.

## Capacitar al equipo (lo que casi nadie hace)
Un manual que nadie leyó no sirve. Design ops incluye enseñar:
- Sesión corta al equipo: "así es nuestra marca, esto sí, esto no".
- La mini-guía de 1 página a la mano (ver 80).
- Mostrar dónde están las plantillas y cómo usarlas.
- Un canal para preguntar "¿esto está bien?" antes de que salga mal.

Para Lushows: con un equipo chico, basta una conversación + la mini-guía + la carpeta compartida. La gobernanza no tiene que ser burocracia; tiene que ser claridad.

## Design ops a escala (cuando la marca crece)
En organizaciones grandes, design ops se vuelve disciplina formal:
- **Design system vivo** documentado (Figma + tokens + componentes).
- Versionado del sistema (como software: v1.2, changelog).
- Equipo dedicado a mantener el sistema.
Referentes: **Material Design (Google)**, **Polaris (Shopify)**, **Spectrum (Adobe)** — sistemas con gobernanza, versionado y equipo que los cuida. No es el caso de un negocio chico, pero muestra hacia dónde escala la lógica.

## Métricas de salud de marca (opcional, útil)
- ¿Cuántas piezas salieron sin pasar por el guardián? (menos = mejor control)
- ¿Aparecen versiones viejas? (señal de fuga)
- ¿El equipo encuentra los assets solo? (biblioteca sana)
- Auditoría de consistencia periódica (ver 88).

## Errores comunes
- Entregar la marca y no definir quién la cuida.
- El único archivo bueno vive en la compu de una persona.
- Proveedores recreando el logo "a ojo".
- Cambiar la marca por aburrimiento, no por estrategia.
- Manual hecho pero nunca comunicado al equipo.

## Mini-checklist
- [ ] Definido quién aprueba (guardián de marca)
- [ ] Niveles de aprobación según riesgo de la pieza
- [ ] Biblioteca central única, versiones viejas archivadas
- [ ] Roles claros (quién crea / quién usa plantillas / proveedores)
- [ ] Política de evolución (refresh vs. rediseño, por estrategia)
- [ ] Equipo capacitado + mini-guía a la mano
- [ ] Auditoría de consistencia periódica agendada (ver 88)

**Siguiente paso**: cierra el sistema de identidad. Con manual (80), aplicaciones (81–86), assets (87), consistencia (88) y gobernanza (89), la marca está lista para vivir y mantenerse. Revisa el bloque de estrategia/concepto para asegurar que todo este sistema sigue sirviendo a la idea central de la marca.
