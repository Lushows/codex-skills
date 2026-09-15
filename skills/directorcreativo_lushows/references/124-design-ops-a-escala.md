# 124 — Design ops a escala

Un design system no es un proyecto que termina: es un producto que vive, crece y se cuida. **Design ops** (operaciones de diseño) es la disciplina de gestionar ese sistema y al equipo que lo usa: quién decide qué entra, cómo se contribuye, cómo se versiona, cómo se mantiene sano a medida que más gente lo toca. Sin ops, hasta el mejor sistema se pudre en seis meses (ver 89 para la versión de marca/gobernanza general).

## El problema que resuelve
Al inicio el sistema lo hace una persona y todo va bien. Pero al crecer: dos diseñadores crean dos botones distintos, un dev "parchea" un componente solo para su pantalla, nadie sabe qué versión es la buena. Design ops pone reglas para que **muchas manos** no destruyan la coherencia.

## Modelos de gobernanza (quién manda)
| Modelo | Cómo funciona | Cuándo |
|---|---|---|
| **Centralizado** | Un equipo dueño decide y construye todo | sistema chico, equipo pequeño |
| **Federado** | Varios contribuyen, un grupo aprueba | empresas medianas/grandes |
| **Híbrido** | Núcleo central + aportes con revisión | el más común a 2026 |

Para Lushows / proyectos chicos: **centralizado de facto** —tú (o un diseñador de confianza) eres el guardián—. No necesitas comité; necesitas una persona que diga sí o no con criterio.

## El flujo de contribución (cómo se agregan cosas)
La pregunta clave: "necesito un componente nuevo, ¿qué hago?". Define un camino claro:
```
1. Propuesta   → ¿existe ya algo parecido? ¿es reutilizable o caso único?
2. Revisión    → el guardián valida: encaja con tokens, naming, accesibilidad
3. Construcción→ se hace bien (estados, variants, doc)
4. Documentación→ no entra sin doc (ver 123)
5. Publicación → se libera en la library y se anuncia en el changelog
```
Regla de oro: **antes de crear, busca**. El 80% de las veces ya existe algo que sirve o se adapta. Crear de más infla el sistema y lo vuelve inmanejable.

## Versionado (semver, en simple)
Los sistemas serios versionan como software, con **semver** (versión semántica) `MAYOR.MENOR.PARCHE`:

| Cambio | Sube | Ejemplo |
|---|---|---|
| **Parche** (3.4.→1) | arreglo sin romper nada | corregir color de un borde |
| **Menor** (3.→5.0) | algo nuevo, compatible | nuevo tamaño de botón |
| **Mayor** (→4.0.0) | cambio que ROMPE lo existente | renombrar un token usado en todos lados |

Por qué importa: si renombras `color-primary` sin avisar (cambio mayor), rompes a todos los que lo usan. El versionado + changelog (ver 123) avisa y da tiempo de adaptarse. Para una marca chica basta con "v1, v2" y notas de qué cambió; no necesitas la maquinaria completa, pero sí el hábito de avisar.

## Deprecación (cómo retirar algo sin romper todo)
Nunca borres de golpe. El ciclo sano:
1. **Marca como deprecado** (obsoleto) en la doc, con el reemplazo recomendado.
2. Da un **periodo de gracia** para migrar.
3. Recién entonces **elimina**.
"Deprecado pero documentado" evita el caos de que algo desaparezca de un día para otro.

## El equipo (roles, aunque seas pocos)
Aun en equipos chicos conviene saber quién cubre cada sombrero:
- **Guardián / owner** — decide qué entra, cuida la coherencia.
- **Contribuyentes** — diseñadores/devs que proponen y construyen.
- **Consumidores** — quienes usan el sistema para hacer producto.
- **Champions** — defensores que evangelizan su uso en cada equipo.

En Lushows estos roles pueden ser una o dos personas; lo importante es que el rol de **guardián** exista y tenga autoridad para decir "no".

## Métricas de salud (¿el sistema sirve?)
No es solo construir, es medir adopción:
- [ ] % de pantallas que usan componentes del sistema (vs. piezas sueltas).
- [ ] Cuántos componentes "detached" o duplicados aparecen (mala señal).
- [ ] Tiempo de armar una pantalla nueva (debería bajar con el tiempo).
- [ ] Cuántas dudas/peticiones llegan (mucho = falta doc; nada = nadie lo usa).

Un sistema que nadie adopta es dinero tirado. Si el equipo lo esquiva, el problema casi siempre es: difícil de usar, mal documentado o sin un dueño que lo empuje.

## Referentes reales
- **Spotify** y **Atlassian** popularizaron el modelo federado.
- **Material Design** y **Carbon** muestran versionado y deprecación públicos ejemplares.
- Mira sus changelogs: verás versiones, deprecaciones y rutas de migración reales.

## Errores comunes
- Construir y olvidar: nadie lo mantiene → muere.
- Cero proceso de contribución → cada quien crea su versión.
- Borrar componentes sin deprecar → rompes productos en vivo.
- No medir adopción → no sabes si sirve.
- Guardián sin autoridad → las reglas se ignoran.

## Para Lushows (no técnico)
Tu design ops mínimo: (1) tú eres el guardián, (2) regla "antes de crear, busca si ya existe", (3) una nota de "qué cambió" cada vez que tocas el sistema, (4) nunca borres sin avisar. Eso es el 90% del valor sin burocracia.

## Mini-checklist
- [ ] Un guardián con autoridad definido
- [ ] Flujo claro para proponer/agregar componentes
- [ ] Versionado + changelog (aunque sea simple)
- [ ] Proceso de deprecación (marcar → gracia → eliminar)
- [ ] Métrica básica de adopción
- [ ] "Antes de crear, busca" como cultura

**Siguiente paso**: una de las pruebas de fuego de un sistema es vestir varias marcas. Pasa a 125 multi-brand y white-label.
