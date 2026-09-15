# 150 — Diseñar la organización de outbound

Antes de contratar al primer SDR ya estás tomando decisiones de organización: a quién reporta, si vende con un AE (Account Executive — el vendedor que cierra) o él mismo cierra, si tu equipo se organiza por producto o por territorio. Diseñar mal la organización se paga en fricción diaria: leads que se caen entre roles, SDRs sin dueño, AEs que se quejan de la calidad. Este módulo es el plano: cómo estructurar el área de outbound desde cero, qué ratios usar, y cuándo pasar de solista a equipo. Es el marco donde encajan reclutar (`151`), compensar (`154`) y las cuotas (`155`).

## El principio: la estructura sigue al modelo de venta

No hay una organización "correcta"; hay la que encaja con tu ciclo de venta y tu ticket. La pregunta de fondo: **¿cuánto trabajo hay entre el primer toque y el cierre?**

- **Ticket bajo / ciclo corto** (venta transaccional, PYME) → un mismo rol puede prospectar y cerrar (SDR full-cycle). Menos handoffs, menos fricción.
- **Ticket alto / ciclo largo** (venta compleja, comité de compra, ver `11`) → separas roles: el SDR agenda, el AE cierra. Especializar sube la producción de cada uno.

La separación SDR↔AE (ver `03`) es la decisión estructural #1. Se justifica cuando el AE gana más cerrando que prospectando: si el AE cierra deals de $10.000 y un SDR le llena la agenda, sale carísimo que el AE prospecte. Si tus deals son de $200, no vale separar.

## Modelos de organización

| Modelo | Cómo es | Cuándo usarlo |
|---|---|---|
| **Solista full-cycle** | Una persona (o el founder) prospecta, agenda y cierra | Arranque, validar el playbook antes de contratar (ver `89`) |
| **SDR + AE (asignación fija)** | Cada SDR "alimenta" a 1–3 AEs fijos | El estándar B2B; construye relación y confianza SDR↔AE (ver `73`) |
| **SDR + AE (round-robin)** | Los SQL caen a un pool de AEs por turno | Equipos grandes; más justo, menos relación |
| **Pods (célula)** | Mini-equipo: 1 líder + 2–3 SDRs + 2–3 AEs + a veces 1 CS | Escala; cada pod es una unidad medible y replicable |

El **pod** es la unidad de escalamiento más limpia: cuando un pod funciona y da sus números, clonas el modelo en vez de agrandar un equipo gigante e inmanejable. Coaching y QA se organizan mejor por pod (ver `156`, `157`).

## Los ratios que definen el diseño

Estos números guían cuánta gente necesitas de cada rol. Son órdenes de magnitud (los cálculos exactos según tu embudo → `Matematicas_lushows`, y tu embudo real → `81`):

```
Ratio SDR : AE
  Ciclo corto / self-serve   ~1 SDR : 1 AE  (o full-cycle)
  Ciclo medio B2B            ~1 SDR : 1–2 AE
  Ciclo largo enterprise     ~2–3 SDR : 1 AE  (mucho trabajo de prospección por deal)

Ratio Líder : SDR (span of control)
  Un líder de SDRs coachea bien a  ~5–8 SDRs.
  Más de 8 → el coaching (156) se diluye → contrata otro líder o arma otro pod.
```

**Regla:** el cuello de botella define a quién contratas. Si tus AEs tienen agenda vacía → te faltan SDRs. Si tus SDRs agendan reuniones que nadie atiende → te faltan AEs. Mira el embudo (`81`) para saber cuál es.

## Líneas de reporte: ¿a quién reporta el SDR?

| Opción | Ventaja | Riesgo |
|---|---|---|
| **SDR reporta a un líder de SDRs** (equipo propio) | Coaching especializado, cultura de outbound, carrera clara | Silo con ventas si no hay SLA (ver `74`) |
| **SDR reporta al AE que alimenta** | Alineación total con quien cierra | El AE no siempre sabe (ni quiere) coachear prospección |
| **SDR reporta a Marketing** | Bueno si el SDR trabaja leads inbound (ver `02`) | Desconexión con la meta de revenue |

Lo más común y sano al escalar: **equipo de SDRs con su propio líder**, alineado con ventas por un SLA escrito (ver `74`) y un loop de feedback (ver `79`). Esto le da al SDR un jefe que sí entiende su oficio y un camino de carrera (ver `156`). Todo esto vive bajo RevOps / go-to-market (ver `06`).

## Inbound SDR vs. Outbound SDR: no los mezcles

Son trabajos distintos y conviene **separarlos** apenas tengas volumen:
- **Outbound SDR (a veces llamado BDR):** genera desde cero, escribe cold email, construye listas. Trabajo de cazador.
- **Inbound SDR:** califica leads que ya levantaron la mano (formularios, demos). Trabajo de velocidad de respuesta.

Un mismo SDR haciendo ambos hace mal los dos: cuando entra un lead inbound "caliente" abandona el outbound (que es más duro), y el pipeline outbound se seca. Si por tamaño no puedes separarlos, al menos **bloquea horas** para outbound protegido (ver `67`).

## Ejemplo: organización de un equipo que arranca

```
Etapa 0 (validar):     El founder full-cycle prueba el playbook.  0 contrataciones.
Etapa 1 (primer SDR):  1 SDR outbound → alimenta al founder/1 AE.  Ratio 1:1.
Etapa 2 (primer pod):  Líder + 3 SDRs + 2 AEs.  Se escribe SLA (74) y comp (154).
Etapa 3 (escalar):     Se clona el pod cuando el primero da números repetibles.
                       Se separan inbound SDR / outbound SDR si hay volumen inbound.
```

## Errores comunes

- **Separar SDR/AE con ticket bajo.** Agregas un handoff (y fricción) sin ganar nada.
- **Contratar SDRs antes de validar el playbook.** Sin proceso probado no sabes qué escalar (ver `89`).
- **Un líder con 12 SDRs.** El coaching se evapora; nadie mejora (ver `156`).
- **Mezclar inbound y outbound en la misma persona sin proteger el outbound.** El pipeline frío se seca.
- **SDRs sin línea de reporte clara.** Nadie los coachea, nadie los defiende, rotan (ver `159`).
- **Organización sin SLA entre SDR y AE.** Guerra fría por la calidad de los SQL (ver `74`, `78`).

## Siguiente paso

Define tu modelo (empieza solista → primer SDR → primer pod) según tu ticket y ciclo. Fija el ratio SDR:AE desde tu embudo (`81`) y no pongas más de ~6–8 SDRs por líder. Escribe el SLA SDR↔AE (`74`) antes de que aparezca la fricción. Con la estructura clara, el siguiente paso es llenarla → reclutar a escala (`151`). Para los costos de nómina de esa estructura → `contador_lushows`; para si el equipo cabe en tus unit economics → `economist_lushows`.
