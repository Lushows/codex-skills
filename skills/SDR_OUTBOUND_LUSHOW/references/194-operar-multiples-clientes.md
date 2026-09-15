# 194 — Operar múltiples clientes (multi-tenant sin cruzar dominios)

Este módulo es la **disciplina operativa** que sostiene una agencia de outbound con varios clientes a la vez: cómo correr 3, 5 o 15 cuentas sin que una hunda a las otras. Importa porque el error que mata agencias en operación no es vender mal — es **cruzar la infraestructura de envío entre clientes**: un cliente con lista mala genera quejas de spam que envenenan la reputación de dominios que también usas para otros, y de golpe **ninguno** de tus clientes llega a la bandeja. Multi-tenant (atender varios clientes en la misma operación) en outbound significa **una cosa innegociable: infra de envío separada por cliente.** Aquí está cómo se monta y se opera esa separación, más el ritmo de trabajo para no perder el control conforme sumas cuentas.

## El principio: la reputación no se comparte, se aísla

La reputación de envío (qué tan confiable te ven Google/Microsoft) vive a nivel de **dominio e IP** (ver `40`, `46`). Si dos clientes envían desde los mismos dominios, **comparten reputación**: la lista sucia del cliente A, sus quejas de spam y sus bounces contaminan al cliente B, que hizo todo bien. Es como meter la ropa de dos personas en la misma lavadora — si una trae lodo, la otra sale sucia. Por eso la regla es absoluta:

> **Cada cliente tiene sus propios dominios secundarios, sus propios buzones y su propio warmup. Nunca se cruzan.**

Esto no es opcional ni "para cuando crezcas": es desde el cliente #2. Es también lo que justifica que cada cliente pague su costo de infra (ver `190`, `191`): esos dominios y buzones son suyos, dedicados.

## La arquitectura multi-tenant (cómo se separa)

Cada cliente es una "isla" de envío independiente. La estructura por cliente:

```
CLIENTE A                          CLIENTE B
├── dominios: a-io.com, a-hq.com   ├── dominios: b-team.com, b-mail.com
│   (secundarios, nunca su main)   │   (secundarios, nunca su main)
├── buzones: 2–3 por dominio       ├── buzones: 2–3 por dominio
├── warmup propio (2–4 sem)        ├── warmup propio (2–4 sem)
├── lista propia (su ICP)          ├── lista propia (su ICP)
├── secuencias propias             ├── secuencias propias
└── bandeja de respuestas propia   └── bandeja de respuestas propia
        ↓                                  ↓
   ┌─────────────────────────────────────────┐
   │  CAPA COMPARTIDA (la agencia, esto sí)   │
   │  CRM multi-cliente · sending tool ·      │
   │  Clay/Apollo · dashboards · tu equipo    │
   └─────────────────────────────────────────┘
```

Lo que **sí** compartes entre clientes (sin riesgo de reputación): las **herramientas** de sourcing y datos (Apollo, Clay; ver `100`, `31`), el CRM (ver `32`), los sending tools que soportan multi-workspace (Instantly, Smartlead permiten separar cuentas dentro de una suscripción; ver `33`), y tu equipo/procesos. Lo que **nunca** compartes: dominios, buzones, listas, reputación.

## Detalles de la separación (checklist por cliente nuevo)

```
Al dar de alta un cliente nuevo:
[ ] Comprar 2–5 dominios secundarios SUYOS (variantes de su marca)   (ver 41)
[ ] Configurar SPF + DKIM + DMARC en cada dominio                     (ver 42)
[ ] Crear 2–3 buzones por dominio (Google Workspace / M365)          (ver 43)
[ ] Arrancar warmup 2–4 semanas ANTES de enviar en volumen           (ver 43)
[ ] Workspace/cuenta separada en el sending tool                      (ver 33)
[ ] Etiqueta/pipeline separado en el CRM                              (ver 32, 77)
[ ] Lista propia verificada con SU ICP                                (ver 10, 28)
[ ] Bandeja de respuestas separada (o carpeta/etiqueta clara)         (ver 64)
[ ] Monitoreo de reputación por dominio de ese cliente                (ver 46)
```

Si un cliente empieza a generar quejas o bounces, el daño **queda contenido en su isla** — pausas y arreglas ESA cuenta sin tocar las demás. Esa contención es exactamente el punto de la arquitectura.

## El ritmo de operación (no perder el control con volumen)

Operar varios clientes es un problema de **rutina y trazabilidad**, no solo de infra. El día/semana de la agencia:

- **Diario:** revisar respuestas de cada cliente y responder rápido (las respuestas calientes se enfrían; ver `64`), vigilar que ningún dominio esté cayendo en reputación (ver `46`).
- **Semanal:** revisar números por cliente (reply, reuniones; ver `80`, `144`), refrescar listas, rotar copy si algo se agota (ver `65`), y la llamada de revisión con cada cliente (ver `193`).
- **Mensual:** reporte por cliente, decidir qué escalar y qué arreglar (ver `83`), planear altas nuevas.

La herramienta que hace esto sostenible es el **CRM con pipeline separado por cliente** (ver `32`, `77`) más un **dashboard por cliente** (ver `144`). Sin trazabilidad por cliente, a los 5 clientes ya no sabes qué pasa en cada uno y la calidad se cae — que es cuando incumples SLAs (ver `193`) y pierdes cuentas.

## Cuándo puedes sumar otro cliente (la señal)

No sumes clientes más rápido de lo que puedes operarlos **bien**. La señal de que puedes tomar otro: los actuales están dentro de su rango de reuniones prometido (ver `193`), sus dominios están sanos (ver `46`), y tú (o tu equipo) no estás apagando incendios. Si estás corriendo detrás de las respuestas y descuidando bandejas, **primero delega o sistematiza** (ver `85`, `86`, `89`, `198`) — no sumes. Crecer en clientes con la operación desbordada quema dominios e incumple a todos (ver `196`).

## Errores comunes (qué NO hacer)

- Compartir dominios/buzones entre clientes "para ahorrar". El error fatal: un cliente hunde a todos.
- Usar el dominio principal de la agencia (o del cliente) para enviar frío. Lo quemas (ver `97` err 1).
- No separar pipelines en el CRM: mezclas leads de clientes distintos y pierdes trazabilidad (ver `77`).
- Tardar en responder porque tienes muchas bandejas: la respuesta caliente se enfría y pierdes la reunión (ver `64`).
- Sumar clientes más rápido de lo que puedes operarlos: la calidad se cae y empiezas a incumplir SLAs (ver `193`).
- No monitorear reputación por cliente: descubres que un dominio se quemó cuando ya arrastró resultados (ver `46`).

## Siguiente paso

Convierte el checklist de alta en tu proceso estándar: cada cliente nuevo pasa por él, sin excepción. Monta pipelines separados en el CRM (ver `32`) y un dashboard por cliente (ver `144`). Cuando la operación te desborde, la respuesta es sistematizar y delegar (ver `198`, `89`), no bajar la calidad. Para ejemplos de cómo se ve todo esto funcionando por industria, `195`. Para el compilado de lo que NO debes hacer, `196`.
