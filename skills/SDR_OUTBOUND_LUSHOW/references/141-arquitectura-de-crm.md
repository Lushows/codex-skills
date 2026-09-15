# 141 — Arquitectura de CRM

`32` te dio la versión práctica: qué CRM elegir y los campos mínimos para arrancar. Este módulo es la **arquitectura profunda**: cómo se relacionan los objetos entre sí, qué campos merecen existir (y cuáles solo estorban), y sobre todo cómo modelar los **estados** por los que viaja un lead para que el CRM nunca mienta. Un CRM bien arquitecturado es invisible: el lead fluye, todo tiene su lugar, y cualquiera abre el registro y entiende en 5 segundos en qué va. Uno mal arquitecturado es un pantano donde los leads se pudren y el forecast es ficción.

## El principio: el CRM modela la realidad, no la decora

Cada objeto y cada campo debe corresponder a algo real de tu proceso comercial. Si no vas a usar un dato para **decidir, filtrar o medir**, no lo captures —cada campo vacío o basura ensucia el sistema. La pregunta antes de crear cualquier campo: *"¿qué decisión o reporte depende de esto?"*. Si no hay respuesta, no va.

## Los objetos y cómo se relacionan

Cuatro objetos, con cardinalidad (cuántos de uno cuelgan de otro) que importa entender:

```
ACCOUNT (empresa)  1 ──── N  CONTACT (persona)
   │                            │
   │ 1                          │ N
   │                            │
   N                            │
DEAL (negocio) ◄────────────────┘   (un deal se ata a una empresa
   │                                  y a uno o varios contactos)
   │ 1
   │
   N
ACTIVITY (correo/llamada/nota/reunión)
```

- **Account (empresa)** es el ancla. El firmographic (tamaño, industria, ciudad), el ICP fit y el tier (`16`) viven aquí, no en el contacto. Regla: **lo que es cierto de la empresa entera va en Account** (levantó ronda, es del nicho X), lo que es cierto de la persona va en Contact.
- **Contact (persona)** — varios cuelgan de una Account (multi-threading: contactas a 3 personas de la misma empresa, ver `162`). Cargo, email, teléfono, LinkedIn, canal de entrada.
- **Deal (negocio)** — nace **cuando hay SQL**, no antes (regla de oro de `32`). Se ata a la Account y al/los Contact(s) involucrados. Es lo que el AE trabaja para cerrar.
- **Activity (actividad)** — el histórico. Cada toque (correo, llamada, WhatsApp, reunión) cuelga del Contact y/o el Deal. Es la materia prima de la atribución (`143`).

## Los campos: los que sirven y los que estorban

Divide los campos en tres familias y no mezcles:

```
FIRMOGRÁFICOS (en Account) — quién es la empresa
  industria_nicho · empleados · ciudad_pais · icp_tier (A/B/C, ver 16)
  fuente_lista (Apollo/Clay/Maps) · dominio (clave de dedup, ver 148)

DE PERSONA (en Contact) — quién es y cómo entró
  cargo · seniority (decisor/influenciador/usuario, ver 11) · email
  email_status (verificado/catch-all/bounce, ver 28) · canal_entrada
  linkedin_url · fecha_ultimo_toque

DE PROCESO (en Contact y Deal) — en qué va
  lead_status (el más importante, ver abajo)
  score (0–100, ver 38) · owner (dueño, nunca vacío)
  motivo_descarte · senal_trigger (ver 37) · sql_source (atribución, ver 143)
```

Regla de sanidad: **si un campo lleva 3 meses vacío en el 80% de los registros, o lo empiezas a llenar o lo borras.** Campos zombis son deuda.

## El corazón: la máquina de estados de `lead_status`

El campo que hace o rompe tu CRM. Un lead siempre está en **exactamente un estado**, y los estados forman una máquina con transiciones válidas. Sin esto, nadie sabe en qué va nada.

```
        ┌──────────────────────────────────────────────────────┐
        ▼                                                        │
   [nuevo] ──► [en_secuencia] ──► [respondió] ──► [calificado/SQL] ──► [handoff_AE]
        │            │                  │                                    │
        │            ▼                  ▼                                    ▼
        └──────► [descartado]      [nurture] ◄──────────────────────  (no ahora, 76)
                (motivo_descarte     │
                 obligatorio)        └──► (revive a en_secuencia en 60–90 días)
```

Reglas de la máquina:
- **Todo lead nace en `nuevo` y nunca queda sin estado.** Cada noche, cero registros en limbo.
- **`descartado` exige `motivo_descarte`** (no ICP / no responde / no interesado / timing / competidor). Nada se descarta "porque sí" —ese motivo entrena tu targeting (ver `79`).
- **Nada se borra, se dispone.** Un "no interesado" va a `nurture`, no a la papelera (ver `76`, `77`).
- **`respondió` y `en_secuencia` son excluyentes.** Un lead que respondió y sigue recibiendo secuencia es un desastre de reputación —la sincronía sequencer↔CRM (ver `148`) lo evita.
- **`calificado/SQL` es la línea donde nace el Deal** y empieza el handoff (`73`).

## Ejemplo: registro de un lead sano

```
ACCOUNT: "Restaurante La Brasa"
  industria_nicho: gastronomía  ·  empleados: 45  ·  ciudad: Medellín
  icp_tier: A  ·  dominio: labrasa.co  ·  fuente_lista: Clay+Maps
  senal_trigger: abrió 2da sede (hiring)

  CONTACT: "Ana Gómez"
    cargo: Gerente  ·  seniority: decisor  ·  email: ana@labrasa.co
    email_status: verificado  ·  canal_entrada: cold email
    lead_status: calificado/SQL  ·  score: 78  ·  owner: SDR_Luis
    fecha_ultimo_toque: 2026-07-01

    DEAL: "La Brasa — Calculadora Gastro"  (nace aquí, no antes)
      etapa: Reunión agendada  ·  sql_source: outbound-SDR (143)
      owner: AE_Marta  ·  fecha_reunion: 2026-07-04
```

Cualquiera abre esto y en 5 segundos sabe: quién es, por qué es tier A, en qué va y quién lo tiene.

## Errores comunes

- **Meter firmographics en el Contact** en vez de la Account → los duplicas y desincronizas por cada persona.
- **Crear el Deal con cada contacto frío** → pipeline inflado de humo. El Deal nace con SQL.
- **Estados ambiguos o solapados** (¿"contactado" y "en secuencia" son lo mismo?). Cada estado, una realidad clara.
- **40 campos de fábrica que nadie llena.** Empieza con los de arriba; añade solo lo que uses para decidir o medir.
- **Dejar leads sin `owner`.** Sin dueño, nadie hace seguimiento y se cae entre sillas (lo resuelve el routing, `142`).

## Siguiente paso

Crea los 4 objetos, define tu máquina de `lead_status` (dibújala antes de tocar el CRM) y captura solo los campos de las tres familias. La higiene diaria que mantiene esto vivo → `77`. Repartir el `owner` de forma justa y automática → `142`. Sincronizar los estados desde el sequencer para que no se pudran → `148`. La atribución que sale de las Activities → `143`. Números de calibración exactos → `Matematicas_lushows`.
