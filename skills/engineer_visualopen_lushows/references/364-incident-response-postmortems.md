# 364 · Respuesta a incidentes y postmortems (recuperar rápido, aprender sin culpar)

> Un incidente no es un examen moral: es un fallo del **sistema**, no de la persona que tocó el botón.
> El objetivo doble: restaurar el servicio lo antes posible **y** salir más fuerte, no buscar a quién despedir.

## Severidades: clasifica para no sobre/sub-reaccionar
Define niveles ANTES del incidente, así nadie improvisa la gravedad a las 3am.

| Sev | Significado | Ejemplo (stack visual) | Respuesta |
|---|---|---|---|
| **SEV1** | Caída total / pérdida de datos / cobro erróneo | Endpoint GPU caído, todos los videos fallan | Todos a bordo, war-room, comms cada 30 min |
| **SEV2** | Degradación grave, parcial | Latencia 5×, 20% de jobs OOM | On-call + 1 experto, mitigar ya |
| **SEV3** | Impacto menor / workaround existe | Fallback a API premium activo, más caro pero funciona | Horario laboral, ticket |

## Roles durante el incidente (no todos hacen todo)
- **Incident Commander (IC)**: coordina, decide, NO mete las manos en el teclado. Es el único que declara sev y resolución.
- **Operaciones**: ejecuta la mitigación (rollback, kill-switch, escalar workers).
- **Comms**: actualiza stakeholders/status page. Libera al IC de explicar mientras se arregla.
Un solo IC evita el caos de "5 personas tocando producción a la vez sin saberlo".

## Mitigar primero, entender después
La tentación del ingeniero es **encontrar la causa raíz** antes de actuar. ERROR. Primero **detén el sangrado**:
rollback al último deploy bueno, activa el kill-switch de la feature, sube el % de fallback. La causa raíz se
investiga **después**, con el servicio ya estable. Un rollback de 2 min vence a un fix "correcto" de 40 min.

## Comunicación: di lo que sabes, cuándo y a quién
Plantilla de actualización: **qué impacto** (qué no funciona, a quién), **desde cuándo**, **qué estamos haciendo**,
**próxima actualización en X min**. Cadencia fija (cada 30 min en SEV1) aunque sea "seguimos investigando" —
el silencio genera más ansiedad que las malas noticias. Una status page honesta vale más que prometer plazos que incumples.

## Postmortem blameless: el sistema falló, no Juan
Tras todo SEV1/SEV2, postmortem escrito en ≤ 48h. **Blameless**: el lenguaje describe acciones y contexto, no
intenciones ni culpa. "El deploy no tenía gate de canary" no "Juan desplegó mal". Si la gente teme el castigo,
oculta información → no aprendes → el incidente se repite. La psicología de seguridad es lo que hace útil al postmortem.

### Estructura del documento
1. **Resumen**: 3 líneas, qué pasó e impacto (jobs fallidos, minutos caído, $).
2. **Timeline**: con timestamps — detección → diagnóstico → mitigación → resolución.
3. **Impacto**: cuantificado (usuarios, dinero, SLO/error-budget quemado).
4. **Causa raíz**: usa los "5 por qués", llega al fallo **sistémico** (por qué fue posible, no solo qué pasó).
5. **Qué salió bien / mal / tuvimos suerte**: honestidad total.
6. **Action items**: con dueño y fecha. **Sin esto el postmortem es teatro.**

## Action items: el postmortem que no cambia nada es ritual vacío
Cada item: **accionable, asignado, con fecha, rastreado** en el backlog como cualquier otro trabajo. Mide el
MTTR (mean time to recover) — si no baja con el tiempo, tus postmortems no están funcionando. Distingue items que
**previenen** la recurrencia de los que solo **detectan** más rápido; prioriza prevención.

## Errores que muerden
- Saltarse el postmortem porque "ya lo arreglamos" → garantizas la repetición.
- Postmortem con culpables nombrados → la próxima vez nadie reporta el near-miss.
- Action items sin dueño → mueren en el documento; nadie los hace.
- No declarar IC → decisiones contradictorias y producción tocada por varios a la vez.
- Confundir causa raíz con "el trigger": el deploy fue el trigger; la **ausencia de canary** fue la causa.

Cruza con [[363-monitoring-alerting-oncall]].
