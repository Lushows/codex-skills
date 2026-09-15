# 88 — La estructura del equipo de ventas

Cómo organizas a la gente que consigue clientes determina cuánto puedes escalar sin que se rompa la calidad ni la moral. Este módulo cubre la anatomía del equipo de ventas moderno: la división SDR ↔ AE, los ratios sanos (cuántos SDRs por AE), la organización en **pods** (equipos pequeños y autónomos), y la distinción entre SDR de **inbound** y de **outbound**. Es el mapa que necesitas cuando pasas de una persona a varias (el *cuándo* está en `89`; aquí está el *cómo se organiza*).

## El principio: especializar por etapa del embudo

La idea que revolucionó las ventas B2B (Aaron Ross, *Predictable Revenue*) es **no pedirle a una persona que haga todo el embudo**. Prospectar, calificar, cerrar y retener son habilidades distintas; el que es bueno prospectando rara vez es el mejor cerrando. Dividir el trabajo por etapa sube la productividad de cada rol y hace el sistema medible y escalable.

Los cuatro roles del embudo moderno:

| Rol | Qué hace | Etapa del embudo (`81`) |
|---|---|---|
| **SDR / BDR** | Consigue y agenda reuniones calificadas (outbound + inbound) | 1–6 (hasta SQL) |
| **AE** (Account Executive) | Toma las reuniones, hace demo, negocia, **cierra** | 6–8 (SQL → cliente) |
| **AM / CS** (Account Manager / Customer Success) | Retiene, hace crecer y renueva la cuenta | Post-venta |
| **Líder / Sales Manager** | Coachea, gestiona números y proceso | Todo |

**La frontera es nítida y hay que respetarla:** el SDR agenda y califica; el AE cierra. El SDR que se pone a cerrar descuida el volumen y pasa leads mal calificados; el AE que prospecta deja de cerrar. Todo el *arte de cerrar* que hace el AE vive en `ventas_lushows` — esta skill es la máquina que le llena la agenda.

## SDR de inbound vs. SDR de outbound

No son el mismo trabajo, y mezclarlos en una sola persona baja el rendimiento de ambos:

| | **SDR de outbound** | **SDR de inbound** |
|---|---|---|
| Origen del lead | Frío, tú lo iniciaste (foco de esta skill) | Caliente, ellos levantaron la mano (llenaron un form, pidieron demo) |
| Habilidad clave | Escribir, investigar, construir listas, cadencias, deliverability | Velocidad de respuesta, calificar rápido, no dejar enfriar |
| Métrica de presión | Reply rate, positivas, SQL de frío | **Speed-to-lead** (responder en minutos), tasa de calificación |
| Volumen | Muchos toques, respuesta lenta | Menos volumen, urgencia alta |

**Regla:** si tienes ambos flujos, sepáralos apenas puedas. El inbound "muere" si el outbound-SDR lo atiende horas después (el lead caliente se enfría en minutos). Al arrancar, una persona hace ambos; al crecer, se especializa. Nota: el inbound vive en la frontera con marketing/ads — de dónde vienen esos leads calientes es trabajo de las skills de pauta (`facebook_ads_lushows`, `google_ads_lushows`, `tiktok_ads_lushows`); esta skill se enfoca en el **outbound frío**.

## El ratio SDR : AE (la métrica de balance)

El ratio sano es **~2:1 a 3:1** (dos o tres SDRs alimentando a un AE). La lógica: un SDR maduro produce ~15–30 SQL/mes (ver `84`), y un AE puede trabajar bien ~20–40 oportunidades activas/mes sin descuidar el cierre. Si desbalanceas:

- **Demasiados SDRs por AE** (ej. 5:1): el AE se ahoga, no da abasto, las oportunidades se enfrían en su bandeja y los SQL se desperdician. Estás pagando por reuniones que nadie trabaja.
- **Muy pocos SDRs por AE** (ej. 1:2): los AE se quedan sin pipeline y terminan prospectando ellos mismos (mal uso de un rol caro que debería estar cerrando).

```
Regla de dimensionamiento:
  SQL que necesita 1 AE/mes ÷ SQL que produce 1 SDR/mes = # de SDRs por AE
  Ej.:  30 SQL que trabaja el AE ÷ 12 SQL/SDR ≈ 2.5 → redondea a 2–3 SDRs por AE
```
**Para dimensionar con tus números exactos → `Matematicas_lushows`.** El ratio real depende de tu ciclo de venta, ticket y capacidad del AE — ajústalo con datos, no con la regla de dedo.

## Pods: la unidad que escala sin caos

Un **pod** (célula) es un equipo pequeño y autónomo que contiene el embudo completo: típicamente **1 líder + 2–3 SDRs + 1 AE** (+ a veces 1 CS). En vez de tener un mar de 20 SDRs y 8 AEs mezclados, agrupas en pods de ~4–5 personas.

Ventajas del pod:
- **Rendición de cuentas clara:** el pod es dueño de su número; el SDR sabe exactamente a qué AE alimenta y el AE le da feedback directo sobre los SQL (cierra el loop de QA, ver `78`, `87`).
- **Coaching más íntimo:** el líder de pod conoce a cada uno (1:1 reales, ver `87`), imposible con 20 reportes directos.
- **Escala por replicación:** cuando un pod funciona, lo **clonas** en vez de agrandar uno gigante. Cada pod es una máquina probada.
- **Sana competencia y cultura:** los pods pequeños crean identidad y motivación sin la política de un equipo enorme.

```
De 5 personas a 40, sin caos:
  1 pod   →  1 líder + 3 SDR + 1 AE           (equipo temprano)
  3 pods  →  se replica la fórmula que funciona
  8 pods  →  + un líder de líderes, misma célula base
La célula no cambia; se multiplica.
```

## Especialización dentro del SDR (al escalar mucho)

En equipos grandes, hasta el rol de SDR se sub-especializa:
- **List-builder / researcher:** construye y enriquece listas (`20`, `29`) para que los SDRs solo ejecuten y respondan. Sube muchísimo la productividad del SDR "de contacto".
- **SDR de contacto:** corre cadencias y maneja respuestas.
- A veces un rol de **ops/RevOps** que cuida el stack, la deliverability y los datos (ver `30`, `40`) para todo el equipo.

No sub-especialices demasiado temprano: con 1–3 SDRs, cada uno hace todo. La especialización se justifica cuando el volumen la paga.

## Errores comunes

- **Pedirle a una persona todo el embudo al escalar.** Prospectar + cerrar + retener en un rol tope el crecimiento y quema gente.
- **Ratio SDR:AE desbalanceado.** AE ahogado (SQL desperdiciados) o AE sin pipeline (prospectando en vez de cerrar).
- **Mezclar inbound y outbound en la misma persona sin querer.** El inbound caliente se enfría; sepáralos.
- **Un equipo gigante en vez de pods.** Pierdes accountability y coaching. Replica células pequeñas.
- **Sobre-especializar temprano.** Con 2 SDRs no necesitas un list-builder dedicado.

## Siguiente paso

Define tu estructura objetivo: empieza con un pod (tú/líder + 1–2 SDRs + tú o un AE cerrando). Fija el ratio SDR:AE desde tus números (`Matematicas_lushows`) y sepára inbound/outbound apenas el volumen lo pida. El *cuándo* y *cómo* llegar ahí desde solista → `89`; el motor que mantiene la calidad dentro del pod → `87` (coaching/QA); el arte de cerrar que hace el AE → `ventas_lushows`.
