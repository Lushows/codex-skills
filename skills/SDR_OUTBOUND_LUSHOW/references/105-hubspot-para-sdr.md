# 105 — HubSpot para SDR

HubSpot es el CRM (sistema donde vive la verdad de cada contacto, cuenta y trato) más común en pymes y scale-ups, y muchos SDRs trabajan **dentro** de él en vez de sumar herramientas aparte. Este módulo es práctico: **cómo un SDR usa HubSpot para prospectar, correr secuencias, automatizar con workflows, estructurar propiedades y medir su outbound** — sin volverse admin de HubSpot. En el `32` (CRM para outbound) HubSpot es el ejemplo estrella; aquí bajamos al detalle operativo del día a día.

## El principio: el CRM es la fuente de verdad, no una libreta

Todo lo que hace un SDR debe quedar registrado en el CRM: quién es el contacto, a qué cuenta pertenece, en qué etapa está, qué mensajes recibió, qué respondió, qué sigue. Si el dato vive en tu cabeza o en una hoja suelta, **no existe** para el equipo ni para el reporte. HubSpot lo estructura en tres objetos que debes tener claros:

| Objeto | Qué es | Ejemplo |
|---|---|---|
| **Contact** | Una persona | María, gerente de compras |
| **Company** | Una empresa (cuenta) | Restaurante El Fogón |
| **Deal** | Una oportunidad de venta | "El Fogón — Plan anual" |

Un Contact pertenece a una Company; un Deal se asocia a ambos. Separar cuenta de contacto es la base del list-building y del ABM (ver `21`, `22`, `94`).

## Sequences (las cadencias del SDR en HubSpot)

Las **Sequences** de HubSpot son cadencias 1-a-1 semi-automáticas: envían correos desde **tu buzón real** (Gmail/Outlook conectado) y te crean **tareas** para llamadas o LinkedIn (ver `61`). Importante entender qué son y qué NO:

- **Envían desde tu buzón real**, no desde dominios secundarios quemables. Por eso **no sirven para volumen frío alto** — para eso es Instantly/Smartlead (ver `33`, `103`, `104`). HubSpot Sequences son para **volumen moderado y cuentas de más valor** (Tier A/B, ver `16`).
- **Se detienen solas al recibir respuesta** (stop on reply).
- Mezclan **email automático + tareas manuales** (llamar, conectar en LinkedIn) → cadencia multicanal real.
- Tienen **límite diario de inscripciones** por usuario (topes de la plataforma), justamente porque salen de tu buzón personal.

```
Sequence "Restaurantes — outbound tibio":
  Paso 1 (día 0):  Email automático — opener con {{company.name}} (ver 53)
  Paso 2 (día 1):  Tarea — conectar en LinkedIn (manual, ver 57)
  Paso 3 (día 4):  Email automático — caso/valor (ver 54)
  Paso 4 (día 6):  Tarea — llamada (ver 71)
  Paso 5 (día 10): Email automático — break-up (ver 63)
  Delay entre pasos: días hábiles · Stop on reply: ON
```
Cuando el prospecto responde, la conversación de venta —objeciones, agendar, cerrar— **sale del terreno de este módulo** y entra en `ventas_lushows` (ver `64`).

## Workflows (la automatización de fondo)

Los **Workflows** son la automatización basada en reglas del CRM (no confundir con Sequences, que son cadencias 1-a-1). Un SDR se apoya en workflows para que el trabajo aburrido se haga solo:

- **Lead rotation / routing:** cuando entra un lead nuevo, asignarlo al SDR correcto por territorio o round-robin (ver `38`).
- **Lead scoring:** sumar puntos por firmographics + comportamiento y marcar MQL cuando cruza un umbral (ver `38`, `72`).
- **Tareas y alertas:** "si un lead abre 3 correos y visita pricing → crea tarea + Slack al SDR".
- **Data hygiene:** normalizar formatos (país, teléfono), desduplicar, marcar cuentas sin dueño (ver `77`).
- **Reengagement:** mover a nurture los "no ahora" y reengancharlos en X días (ver `76`).

Regla: **Sequences = tú tocando prospectos; Workflows = el sistema moviendo datos y disparando reglas.** Los dos juntos son tu máquina.

## Propiedades (los campos que de verdad usa un SDR)

No inventes 200 campos. Los que importan para outbound:

- **Lifecycle stage:** Subscriber → Lead → MQL → SQL → Opportunity → Customer (ver `72`, `81`). Es la columna vertebral del funnel.
- **Lead status:** New, Attempting, Connected, Open Deal, Unqualified — el estado *dentro* de tu trabajo diario.
- **Contact/Deal owner:** quién es responsable. Sin dueño = nadie lo trabaja.
- **Propiedades de ICP:** tamaño de empresa, industria, tecnología (ver `15`) — para segmentar y puntuar.
- **Disposición de la última actividad:** resultado de la última llamada/correo (ver `77`).
- **Source / original source:** de dónde vino (outbound email, LinkedIn, referido) — para atribuir (ver `80`).

Mantén el set **corto y obligatorio en los momentos clave** (al crear deal, al descalificar). Campos que nadie llena no sirven para reportar.

## Reporting (medir tu outbound dentro de HubSpot)

HubSpot te da los reportes que responden "¿mi outbound funciona?":

- **Funnel por lifecycle stage:** cuántos leads → MQL → SQL → Opportunity, y las tasas de conversión entre etapas (ver `81`, `05`).
- **Actividad del SDR:** correos enviados, llamadas, tareas completadas, reuniones agendadas (ver `80`, `84`).
- **Sequence performance:** reply rate y meetings por secuencia → cuál copy/cadencia gana (ver `65`).
- **Source attribution:** qué canal trae los deals que cierran (ver `82`).

Para que un número deba ser **exacto** (una tasa de conversión, un forecast, comp del SDR) → verifícalo con `Matematicas_lushows`; HubSpot reporta, pero la aritmética fina la confirmas aparte.

## HubSpot solo vs. HubSpot + stack de cold email

- **HubSpot solo:** ideal si tu outbound es **de volumen moderado a cuentas de valor**, desde tu buzón real, y ya vives en HubSpot para todo lo demás. Menos herramientas, todo integrado.
- **HubSpot + Instantly/Smartlead:** cuando necesitas **volumen frío alto** desde dominios secundarios. Ahí Instantly/Smartlead envían el frío y **escriben de vuelta** a HubSpot los que responden vía integración (ver `34`, `103`, `104`). HubSpot sigue siendo la fuente de verdad; el cold-email tool es solo el motor de envío masivo.

## Errores comunes

- **Usar Sequences para spamear frío a volumen** → quemas tu buzón real y tu dominio principal (ver `41`). Volumen frío = herramienta de cold email dedicada.
- **No conectar el sequencer externo al CRM** → estados no fluyen, contactos duplicados (ver `77`).
- **Crear 200 propiedades** que nadie llena → reportes vacíos. Menos campos, obligatorios.
- **No poner owner** a los contactos → leads huérfanos que nadie trabaja.
- **Confiar en el reporte sin auditar la aritmética** de conversiones críticas → `Matematicas_lushows`.

## Siguiente paso

Define tu lifecycle stage + lead status + las 5–6 propiedades de ICP, monta un workflow de scoring/routing (`38`) y una Sequence de 5 pasos para cuentas Tier A/B (`16`, `61`). Si te falta volumen frío, súmale Instantly/Smartlead con write-back a HubSpot (`103`, `104`, `34`). Para el CRM como concepto → `32`; para las métricas del funnel → `80`, `81`.
