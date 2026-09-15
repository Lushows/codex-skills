# 146 — Integración del stack

Tu stack de outbound son varias herramientas (sourcing, Clay, sequencer, CRM, señales, dashboard). Cada una guarda su propia versión de los datos. La **integración** es lo que las hace hablar para que exista **una sola verdad** —un *single source of truth* (fuente única de verdad: el lugar donde el dato correcto vive, y del que todos los demás leen)— en vez de cinco versiones que se contradicen. `34` te dio las herramientas de pegamento (Zapier/Make/n8n) y los flujos concretos; este módulo es el **principio de arquitectura**: quién es dueño de cada dato, cómo evitar los silos, y por qué sin esto tu operación miente sin que te des cuenta.

## El principio: cada dato tiene UN dueño, todos los demás leen

El caos de datos nace cuando dos herramientas creen ser dueñas del mismo dato y cada una lo edita. ¿El estado del lead vive en el sequencer o en el CRM? ¿El email verificado en Clay o en HubSpot? Si no decides **quién manda sobre cada campo**, terminas con un lead que en Instantly dice "respondió" y en HubSpot dice "en secuencia" —y le sigues escribiendo. La regla de oro (heredada de `32`): **el CRM es el sistema de registro (la verdad de qué pasó); el sequencer es el sistema de acción (contactar).** Cada dato tiene un dueño; el resto son copias de lectura que se sincronizan.

## El mapa de propiedad del dato (data ownership)

Antes de integrar nada, dibuja quién es dueño de qué. Este es el mapa típico:

| Dato | Dueño (fuente de verdad) | Quién lo lee |
|---|---|---|
| Firmographic / empresa | Clay / la herramienta de sourcing → escribe al CRM | CRM, scoring |
| Email verificado + status | Verificador (NeverBounce) → sella en Clay/CRM | sequencer (para no enviar a bounces) |
| Estado del lead (`lead_status`) | **CRM** | dashboard, routing |
| Actividad de envío (enviado/abierto/respondió) | **Sequencer** → se refleja en el CRM | CRM, atribución |
| Score | CRM o Clay (donde se calcula) → CRM | routing |
| Deal / etapa de cierre | **CRM** | forecast, dashboard |

La pregunta que resuelve el 80% de los líos: *"cuando este campo cambie, ¿en qué herramienta cambia primero, y a cuáles debe propagarse?"*. Esa respuesta es tu diseño de integración (el flujo mecánico está en `147`, la sincronía bidireccional en `148`).

## Nativo primero, pegamento después

No todo se integra igual de bien. El orden de preferencia:

```
1. INTEGRACIÓN NATIVA     (Clay→Instantly, HubSpot↔Smartlead, Calendly→CRM)
   → la construyó el fabricante, es la más robusta y barata. ÚSALA SIEMPRE que exista.

2. PEGAMENTO no-code      (Zapier / Make / n8n, ver 34, 107)
   → para conectar lo que no tiene integración nativa.

3. WEBHOOK / API directa  (una herramienta avisa a otra vía URL)
   → cuando necesitas control fino o tiempo real. Requiere algo técnico.

4. CSV a mano             ← el último recurso, y una alarma. Si exportas/importas
                            CSV cada semana, ese es tu silo; automatízalo (147).
```

Error clásico: reconstruir con Zapier algo que **ya es nativo** (Clay ya escribe directo a Instantly y HubSpot; no le pongas un puente encima). Revisa siempre si la integración nativa existe antes de pagar por pegamento.

## Las señales de que tienes silos (y te están costando)

Un **silo** es un dato atrapado en una herramienta que las demás no ven. Síntomas concretos:

- Copias y pegas entre dos herramientas de forma rutinaria (cada copy-paste es un silo con puente humano).
- El mismo lead aparece distinto en dos pantallas (estado, email, dueño).
- El dashboard no cuadra con lo que ves en el sequencer o el CRM.
- Contactas a alguien que ya había respondido o pedido baja (sincronía de estado rota).
- Nadie sabe "de dónde salió este número" en el reporte (fuente de verdad difusa).

Cada uno de estos es dinero: leads perdidos, reputación de dominio dañada (ver `40`), decisiones sobre datos falsos.

## Ejemplo: el stack mínimo integrado y sus puentes

```
Apollo/Maps ──(export)──► CLAY  ──(nativo)──► Instantly (sequencer)
   (sourcing, 25)          │  enriquece+verifica   │
                           │  (31, 28)             │ (evento: respondió/bounce)
                           │(nativo)               ▼
                           └──────────────► HubSpot (CRM = fuente de verdad, 141)
                                              ▲          │
                            Calendly ─(nativo)┘          │(nativo/webhook)
                            (reunión → Deal, 73)         ▼
                                              Looker Studio (dashboard, 144)
                                                 lee del CRM, no duplica
```

Fíjate: **el CRM es el centro**, todo escribe hacia él y el dashboard lee de él. Ni un solo CSV manual en el diagrama. Si aparece uno, ahí está tu silo.

## Buenas prácticas de arquitectura

- **Un dato, un dueño.** Decídelo por campo antes de conectar nada (la tabla de arriba).
- **El CRM al centro.** Todo confluye ahí; los reportes leen de ahí, no de cada herramienta suelta.
- **Nativo > pegamento > CSV.** Y CSV manual recurrente = alarma de silo.
- **Deduplica en la entrada, por dominio/email normalizado, no por texto exacto.** (Lección real de proyectos con dos correos por comercio: el texto exacto no dedup-ea; normaliza mayúsculas/espacios y cruza por dominio. Ver `148`, `139`.)
- **Documenta el mapa.** Un diagrama simple de qué se conecta con qué te salva cuando "un lead desapareció" y hay que rastrear dónde se rompió.

## Errores comunes

- **Dos herramientas dueñas del mismo dato** → versiones que se contradicen y leads mal contactados.
- **Reconstruir integraciones que ya son nativas** → costo y fragilidad inútiles.
- **Dashboard que lee de fuentes distintas al CRM** → números que no cuadran.
- **CSV manual como "integración"** → el silo con más horas-humano y más errores.
- **No documentar el stack** → cuando algo se rompe, nadie sabe por dónde fluía el dato.

## La frontera

Este módulo es el **diseño** (quién manda sobre cada dato, evitar silos). El **mecanismo** de mover el dato sin manos (triggers, webhooks, los flujos paso a paso) → `147`. Mantener las copias **sincronizadas en ambos sentidos** sin que se pisen → `148`. La calidad y governance del dato a escala → `139`. Herramientas de pegamento a fondo (Make/n8n) → `107`.

## Siguiente paso

Dibuja tu stack real con la plantilla del ejemplo y marca (1) quién es dueño de cada dato y (2) dónde copias y pegas hoy. Convierte cada CSV manual en integración nativa o pegamento. Con el mapa listo, monta los flujos → `147`, y asegura la sincronía bidireccional de estados → `148`.
