# 03 — El modelo SDR / BDR / AE / AM / RevOps

Antes de armar tu máquina de outbound necesitas saber quién hace qué en un equipo comercial moderno. Estos roles no son títulos vanidosos: son una **división del trabajo** que existe porque nadie hace bien las cuatro cosas a la vez (prospectar, calificar, cerrar y retener). Entender el modelo te dice dónde vive el outbound (SDR/BDR), dónde termina tu trabajo (el handoff al AE) y por qué esta skill NO cierra ventas.

## El principio: especializar aumenta el output

La idea viene de Aaron Ross en Salesforce (*Predictable Revenue*): cuando un solo vendedor hacía todo —prospectar, cerrar y cuidar cuentas— era mediocre en todo, porque prospectar y cerrar exigen mentalidades opuestas (volumen frío vs. profundidad de relación). Al **separar los roles**, cada uno se vuelve experto en su parte y el sistema produce más. El outbound predecible nació de esa separación.

## Los cinco roles

| Rol | Nombre completo | Qué hace | Cómo se mide |
|---|---|---|---|
| **SDR** | Sales Development Representative | Outbound: prospecta en frío, agenda reuniones para el AE | Reuniones calificadas agendadas (SQLs) |
| **BDR** | Business Development Representative | Casi lo mismo; suele enfocarse en outbound puro / cuentas nuevas | Reuniones/oportunidades outbound |
| **AE** | Account Executive | El vendedor: toma la reunión, hace discovery, negocia y **cierra** | Revenue cerrado (quota) |
| **AM** | Account Manager | Cuida al cliente ya cerrado: renueva, hace upsell/cross-sell | Retención, expansión, NRR |
| **RevOps** | Revenue Operations | El sistema: CRM, datos, procesos, métricas que sostienen a todos | Eficiencia del motor (ver `06`, `140`) |

## SDR vs BDR: ¿cuál es la diferencia?

En la práctica casi son sinónimos y muchas empresas usan un solo término. La distinción más común:

- **SDR** — suele trabajar los leads **inbound** (los que llegaron por marketing/ads) además de outbound. Recibe la mano levantada y la califica.
- **BDR** — suele ser **outbound puro**: sale a buscar cuentas nuevas que nunca han oído de la empresa, en frío.

Para efectos de esta skill (que es la **máquina de outbound**), trabajamos el rol **outbound sin importar el nombre**: SDR o BDR, el trabajo es conseguir y agendar reuniones frías. Contratación y comp de este rol en `84`, `85`, `150`–`159`.

## El flujo de una oportunidad entre roles

```
MARKETING / ADS ──(lead inbound)──┐
                                   ├──► SDR/BDR ──(SQL: reunión calificada)──► AE ──(cliente cerrado)──► AM
OUTBOUND (esta skill) ─────────────┘         │                                  │
                                             └── califica y protege             └── discovery, negocia, cierra
                                                 el tiempo del AE                    → oficio de ventas_lushows
```

El **handoff SDR→AE** es el momento más delicado del sistema: si el SDR pasa un lead que no encaja, le hace perder el tiempo al AE y erosiona la confianza entre ambos. Por eso el SDR **califica duro** (ver `70`, `78`) y entrega contexto completo (ver `73`, `74`).

## Dónde termina el trabajo del SDR (la frontera con ventas)

El SDR **agenda la reunión y la entrega calificada**. Todo lo que pasa *dentro* de esa reunión de venta —el discovery profundo, rebatir objeciones difíciles, la negociación, el cierre, la postventa— es **oficio del AE = `ventas_lushows`**. Esta skill construye la máquina que llena la agenda del vendedor; no vende por él.

Un caso de frontera típico: el SDR hace una llamada en frío, da el opener y el hook (ver `58`), consigue interés... y ahí, si la conversación se vuelve una venta real, se agenda con el AE o se rutea el *cómo convencer* a `ventas_lushows`. El SDR abre; el AE cierra.

## El caso del solista (sin equipo)

Muchos usuarios (Lushows incluido) empiezan **solos**: son el SDR *y* el AE *y* el AM al mismo tiempo. Está bien — pero el truco es **separar los sombreros por bloques de tiempo**, no mezclarlos:

- **Bloque de SDR** (mañana): prospectar, mandar cadencias, agendar. Mentalidad de volumen (ver `67`).
- **Bloque de AE** (tarde): tomar las reuniones agendadas y cerrar (con `ventas_lushows`).
- **Bloque de AM** (semanal): cuidar a los clientes que ya cerraste.

Cuándo dejar de ser solista y contratar tu primer SDR está en `89`. La regla corta: cuando el bloque de SDR te está robando tiempo de cerrar, contrata al SDR primero (para que tú, mejor cerrador, te quedes de AE).

## Errores comunes (qué NO hacer)

- **Que el SDR intente cerrar.** Descuida el volumen de prospección y suele cerrar peor que un AE. Cada rol en lo suyo.
- **Que el AE prospecte su propio pipeline.** El AE es caro y su tiempo rinde más cerrando; hacerlo prospectar es desperdiciar tu mejor recurso (por eso existe el SDR).
- **No tener RevOps ni siquiera básico.** Sin CRM ordenado ni métricas, nadie sabe qué funciona (ver `06`).
- **Handoff sin contexto.** Pasar "aquí está la reunión" sin el porqué, el dolor y la calificación quema al AE (ver `73`).

## Siguiente paso

Ubica en qué rol estás hoy (solista o equipo). Si eres solista, aplica el time-blocking por sombreros de arriba. Si vas a armar equipo, ve a `88` (estructura y ratios SDR:AE) y `84` (comp). Para entender el sistema completo que rodea estos roles, lee `06` (RevOps y go-to-market).
