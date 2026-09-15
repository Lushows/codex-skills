# 140 — RevOps para outbound

Este es el módulo raíz del Bloque 14. Si `06` te presentó qué es RevOps (Revenue Operations: la función que hace funcionar el motor comercial —datos, herramientas, procesos y métricas), este te da el **sistema completo** que rodea al SDR y del que cuelgan los otros nueve módulos (`141`–`149`). La idea central: un SDR con buen copy pero mal sistema produce una fracción de un SDR con sistema. **El outbound de élite es RevOps con un vendedor encima, no un vendedor con suerte.** Aquí ves las cuatro piezas del sistema y cómo encajan; cada pieza se profundiza en su propio módulo.

## El principio: el pipeline se rompe en las junturas

Ya lo viste en `06` y vale repetirlo porque es la ley del bloque: los leads no se pierden porque el SDR sea malo, se pierden **entre herramientas y entre personas**. El lead que respondió y nadie asignó. El contacto duplicado que recibió dos secuencias. El SQL que el AE nunca trabajó porque el handoff fue un mensaje de WhatsApp perdido. RevOps existe para que el lead **fluya sin fricción y sin manos** de la lista → la secuencia → el CRM → el AE → el reporte. Cada juntura sin aceitar es dinero que se cae.

## Las cuatro piezas del sistema (personas · proceso · datos · herramientas)

RevOps clásico se piensa en cuatro dimensiones. Aplicadas a outbound:

| Pieza | Qué cubre | Módulo a fondo |
|---|---|---|
| **Personas** | Quién hace qué: SDR, AE, AM, ops. Roles, cuotas, SLAs entre equipos | `03`, `74`, `84`, `85` |
| **Proceso** | Las reglas: qué es un SQL, cómo se enruta, cómo es el handoff, la disposición | `72`, `73`, `142`, `77` |
| **Datos** | Que la info de leads/cuentas esté completa, limpia, sincronizada y sin duplicados | `141`, `148`, `139` |
| **Herramientas** | El stack conectado: sourcing → sequencer → CRM → dashboard, hablándose | `146`, `147`, `30` |

La regla de oro entre las cuatro: **el proceso manda, la herramienta obedece.** Nunca compres software para después inventar cómo usarlo. Primero dibuja cómo fluye el lead (proceso), luego elige la herramienta que sirve a ese flujo. El error #1 de RevOps novato es comprar Salesforce y esperar que "organice" un proceso que no existe.

## El sistema en un diagrama

```
        ┌──────────────── RevOps: el que aceita las junturas ─────────────────┐
        │                                                                       │
 DATOS  │  Sourcing ──► Enriquecer ──► Verificar ──► CRM (fuente de verdad)     │
 (141,  │   Apollo/Clay    Clay         NeverBounce    HubSpot/Pipedrive        │
  148)  │      │                                          ▲                     │
        │      ▼                                          │                     │
 HERRAM.│  Sequencer ──(evento: respondió)──► webhook ────┘  (146, 147)         │
 (146)  │   Instantly                                                           │
        │      │                                                                │
PROCESO │      ▼                                                                │
 (142,  │  Scoring+Routing ──► SDR ──(SQL, handoff 73)──► AE ──► AM             │
  143)  │      (38, 142)         │                          │                   │
        │                        └──── loop de feedback (79): qué cierra ───────┘
        │                                                                       │
MÉTRICAS│  Todo lo anterior alimenta ──► Dashboards (144) ──► Forecast (145)     │
 (144)  │                                                                       │
        └───────────────────────────────────────────────────────────────────────┘
```

Léelo así: los **datos** entran limpios y viven en el CRM; las **herramientas** los mueven sin manos; el **proceso** decide a quién y cuándo; las **personas** ejecutan; y todo se **mide** para forecast-ear y corregir. Los diez módulos del bloque son las tuercas de este diagrama.

## Mapa del Bloque 14 (qué módulo resuelve qué)

| # | Módulo | La pregunta que responde |
|---|---|---|
| `141` | Arquitectura de CRM | ¿Qué objetos, campos y estados necesito? |
| `142` | Routing y round-robin | ¿Cómo reparto los leads justo y rápido? |
| `143` | Atribución de outbound | ¿Qué toque generó este deal? |
| `144` | Dashboards y reporting | ¿Qué tableros me dicen dónde se rompe? |
| `145` | Forecasting avanzado | ¿Cómo proyecto con rigor desde el pipeline? |
| `146` | Integración del stack | ¿Cómo evito datos en silos (single source of truth)? |
| `147` | Automatización end-to-end | ¿Cómo va lead → secuencia → CRM → handoff sin manos? |
| `148` | Data pipelines y sync | ¿Cómo mantengo las herramientas sincronizadas? |
| `149` | Costos y ROI del outbound | ¿Cuánto me cuesta un cliente por outbound y rinde el stack? |

## RevOps cuando eres una sola persona

No necesitas un equipo de RevOps para tener RevOps. Si eres solista o agencia chica, **RevOps eres tú ~2 horas a la semana**, distribuidas así:

```
Lunes 30 min   → Higiene: revisar que ningún lead quedó sin estado ni dueño (141, 77)
Miércoles 30 min → Números: mirar el dashboard, ¿qué ratio bajó? (144, 83)
Viernes 30 min  → Junturas: ¿algún flujo se rompió esta semana? arreglar (147)
Cuando toque    → Recalibrar: ¿qué leads sí cerraron? ajustar targeting (79)
```

Saltarte esas dos horas es la razón #1 por la que un solista se estanca: sigue prospectando pero su sistema se pudre por debajo y no se entera hasta que el pipeline se seca.

## Errores comunes (qué NO hacer)

- **Comprar el stack antes de definir el proceso.** La herramienta sirve al flujo, no lo inventa.
- **Tratar el CRM como bodega, no como sistema vivo.** Datos que nadie actualiza mienten, y un forecast sobre mentiras destruye decisiones (ver `141`, `77`).
- **Optimizar el copy e ignorar las junturas.** Un correo 10% mejor no compensa un handoff roto que pierde 30% de los SQL.
- **RevOps como proyecto de una vez.** Es mantenimiento continuo, como aceitar una máquina, no un montaje único.

## Las fronteras

- **Qué motores GTM y si el CAC del negocio cierra** → `economist_lushows` (estrategia). RevOps *ejecuta* el motor, no decide la estrategia de negocio.
- **El cierre y la conversación de venta** en la reunión → `ventas_lushows`.
- **Números exactos** (CAC, ROI, calibración) → `Matematicas_lushows` (ver `149`).
- **La contabilidad de esos costos** (registrar, declarar) → `contador_lushows`.

## Siguiente paso

Dibuja tu diagrama con tus herramientas reales sobre la plantilla de arriba y marca dónde copias y pegas hoy —esas son tus junturas sin aceitar. Luego entra por donde más te duela: si el CRM es un caos → `141`; si los leads se caen entre sillas → `142`; si no sabes qué funciona → `144`; si copias datos a mano → `146`/`147`. Todo el bloque cuelga de este mapa.
