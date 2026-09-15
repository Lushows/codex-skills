# 32 — CRM para outbound

El CRM (Customer Relationship Management: el software donde vive tu base de contactos, empresas y negocios) es la **fuente única de verdad** de tu operación. Todo lo demás —el sequencer, Clay, las señales— alimenta o lee del CRM. Sin él, los leads se pierden entre herramientas, el handoff al vendedor es un caos y no puedes medir nada. Este módulo es cómo estructurarlo **para outbound** (no para gestión de cuentas ya cerradas): qué objetos, qué campos, y sobre todo la **higiene** que evita que se pudra. La arquitectura profunda vive en `141`.

## El principio: el CRM es el sistema de registro, el sequencer es el de acción

Regla que evita el 80% de los líos: **el sequencer (Instantly/Smartlead/Outreach) hace la acción de contactar; el CRM guarda la verdad de qué pasó.** El correo se manda desde el sequencer, pero el estado del lead ("respondió", "agendó", "no interesado") vive en el CRM. Si intentas que ambos sean la verdad, tendrás dos versiones que se contradicen. Un lado actúa, el otro recuerda.

## Los tres CRM y cuándo cada uno

| CRM | Para quién | Fuerte en | Débil en | Precio aprox 2026 |
|---|---|---|---|---|
| **HubSpot** | Startups y pymes que crecen | Facilidad, marketing+ventas integrado, tier gratis usable | Se encarece rápido al subir de plan | Free → Starter ~$20/asiento → Pro $$$ |
| **Pipedrive** | Equipos de ventas puros, simples | Pipeline visual, barato, rápido de aprender | Menos automatización/marketing | ~$15–49/asiento |
| **Salesforce** | Empresas grandes / stack enterprise | Personalización infinita, ecosistema | Complejo, caro, necesita admin | $$$ (contrato) |

Para outbound de pyme/agencia en LatAm: **empieza en HubSpot Free o Pipedrive.** Salesforce solo cuando tengas equipo y procesos que lo justifiquen (ver `106` para el stack enterprise).

## Estructura mínima: los 4 objetos

1. **Company / Account (empresa)** — la cuenta. Aquí vive el firmographic (tamaño, industria, ciudad) y el ICP fit (ver `10`, `16`).
2. **Contact (contacto)** — la persona. Cargo, email, teléfono, LinkedIn. Varios contactos cuelgan de una empresa (multi-threading, ver `162`).
3. **Deal / Opportunity (negocio)** — se crea **cuando el lead califica** (se vuelve SQL), no antes. Es lo que el vendedor trabaja para cerrar.
4. **Activity (actividad)** — correos, llamadas, notas, reuniones. El histórico de qué se hizo.

Para outbound, el flujo es: Contacto (frío) → se contacta → responde positivo → **se crea el Deal** → handoff al AE (ver `73`).

## Los campos que outbound necesita (no los de fábrica)

Crea estos campos personalizados desde el día 1:

```
En Company:
  - icp_fit          (A / B / C)         ← tier, ver 16
  - industria_nicho  (texto/lista)       ← tu segmentación real
  - fuente_lista     (Apollo/Clay/Maps)  ← de dónde salió
  - senal_trigger    (job change/funding/hiring/ninguna) ← ver 37

En Contact:
  - lead_status      (nuevo/en secuencia/respondió/calificado/nurture/descartado)
  - canal_entrada    (cold email/LinkedIn/WhatsApp)
  - fecha_ultimo_toque
  - motivo_descarte  (no ICP/no responde/no interesado/timing)
  - email_status     (verificado/catch-all/bounce)  ← ver 28

En Deal:
  - sql_source       (outbound-SDR)       ← atribución, ver 143
  - sdr_owner        (quién lo agendó)
  - fecha_reunion
```

El campo `lead_status` es el más importante: define los **estados limpios** por los que pasa cada lead. Sin él, nadie sabe en qué va cada quien.

## El principio no negociable: higiene de datos

Un CRM sucio miente, y un forecast basado en mentiras destruye decisiones. Reglas de higiene para outbound:

- **Deduplica al entrar.** Antes de importar de Clay/Apollo, cruza por email/dominio para no crear a la misma empresa dos veces. (Este es un dolor real; en proyectos con dos correos por comercio se duplican cuentas — dedup por dominio normalizado, no por texto exacto.)
- **Todo lead tiene estado, siempre.** Nada queda en el limbo. Cada noche, ningún contacto debería estar sin `lead_status`.
- **Nada se borra, se dispone.** Un "no interesado" no se elimina: se marca con `motivo_descarte` y va a nurture (ver `76`). Ese dato entrena tu targeting (ver `79`).
- **Un dueño por lead.** Sin `owner`, nadie hace seguimiento y se cae entre sillas.
- **Sincroniza estados desde el sequencer.** Cuando alguien responde o se da de baja en Instantly/Smartlead, ese estado debe reflejarse en el CRM automáticamente (vía integración, ver `34`, `147`). Un lead que respondió y sigue recibiendo secuencia es un desastre de reputación.

Detalle operativo de estados y disposición → `77`. Governance de datos a escala → `139`.

## Ejemplo: pipeline de deal para SDR

```
[SQL / Reunión agendada] → [Reunión realizada] → [Handoff a AE]
   └ (a partir de aquí el DEAL lo trabaja ventas: descubrimiento,
      propuesta, negociación, cierre → eso es ventas_lushows)
```
Fíjate dónde termina tu responsabilidad: el SDR llena hasta "Handoff a AE". El pipeline de cierre (propuesta → negociación → cerrado ganado/perdido) es del vendedor. Cómo se pasa el testigo con contexto → `73`. El oficio de cerrar ese deal → **`ventas_lushows`**.

## Errores comunes

- **Crear el Deal demasiado pronto** (con cada contacto frío). Infla el pipeline con humo. El Deal nace cuando hay SQL real.
- **No conectar el sequencer al CRM.** Trabajas a ciegas y duplicas contactos entre ambos.
- **Campos infinitos.** 40 campos que nadie llena son peor que 8 que sí. Empieza mínimo.
- **Dejar leads sin estado ni dueño.** Es como no tenerlos.

## Siguiente paso

Elige CRM (HubSpot Free si dudas), crea los 4 objetos y los campos de arriba, y define tus valores de `lead_status`. Conéctalo a tu sequencer (`33`) vía integración (`34`) para que los estados fluyan solos. Para puntuar y enrutar automáticamente lo que entra → `38`. Para el handoff limpio al vendedor → `73`, y el cierre → `ventas_lushows`.
