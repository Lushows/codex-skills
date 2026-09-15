# 72 — SQL, MQL, SAL

Estas tres siglas son el idioma común entre marketing, el SDR y ventas. Si cada equipo entiende algo distinto por "lead calificado", vas a pelear todo el mes por leads basura y reuniones fantasma. Definirlas por escrito —y acordar quién es dueño de cada etapa— es lo que convierte tu embudo en una máquina medible en vez de un teléfono roto. Este módulo fija las definiciones estándar 2026 y el acuerdo de traspaso entre etapas. Es la base sobre la que se montan el SLA (ver `74`) y la calificación (ver `70`).

## El principio: un lead cambia de "dueño" al calificar, no al aparecer

Un lead viaja por etapas y en cada frontera alguien lo acepta o lo devuelve. Sin definiciones, marketing dice "te pasé 100 leads" y ventas dice "eran basura": ambos tienen razón porque nunca acordaron qué era un lead bueno. La solución no es discutir, es **definir el umbral por escrito y medir contra él**. La regla de oro: *un lead solo avanza si el equipo que lo recibe puede aceptarlo con criterios claros y devolver el que no cumple.*

## Las definiciones (estándar, adáptalas a tu negocio)

| Sigla | Nombre | Qué es | Dueño |
|---|---|---|---|
| **Lead** | Contacto | Cualquiera que entró a tu base (descargó algo, dejó correo, lo prospectaste) | Marketing / SDR |
| **MQL** | Marketing Qualified Lead | Mostró interés suficiente por señales de marketing (abrió, descargó, pidió demo, encaja el ICP) — *vale la pena que un humano lo toque* | Marketing |
| **SAL** | Sales Accepted Lead | El SDR (o ventas) **revisó el MQL y lo ACEPTÓ** para trabajarlo — pasó el filtro de fit básico | SDR |
| **SQL** | Sales Qualified Lead | El SDR habló con él, **confirmó dolor + fit + autoridad + timing** (ver `70`) → listo para el AE | SDR → AE |
| **Opportunity** | Oportunidad | El AE aceptó el SQL y abrió un trato en el CRM | AE |

La diferencia crítica que casi nadie tiene clara: **SAL es "acepto trabajarlo", SQL es "confirmé que califica".** MQL lo declara marketing; SAL y SQL los declara el SDR. Ese doble filtro (aceptar → calificar) es lo que evita que marketing infle números y que ventas reciba basura.

## El outbound: ¿de dónde entra tu lead?

En outbound puro (tú prospectas en frío, ver `20`) el lead no viene de marketing: **lo generas tú**. Entonces tu embudo se ve así:

```
Lista (ICP, ver 10) → Prospecto contactado → Respondió → SQL (calificado por ti) → Opportunity (AE)
```

Aquí no hay MQL clásico, pero el concepto de umbral es igual: no le pasas al AE nada que no sea SQL. Si tu empresa mezcla inbound (marketing) y outbound (tú), entonces sí manejas MQL (inbound) + tus SQL outbound, y ambos entran al mismo criterio de aceptación.

## El acuerdo escrito (plantilla para pegar en Notion/Sheet)

```
DEFINICIONES — [Empresa], vigente [fecha]

MQL = encaja ICP (sector X, tamaño Y, país Z) + hizo ≥1 acción de intención
      (demo request / descarga de fondo-de-embudo / respondió campaña).
      → Dueño: Marketing. SLA de traspaso: ver 74.

SAL = el SDR revisó el MQL en < 24h y lo aceptó (fit básico correcto)
      o lo devolvió con motivo (fuera de ICP / dato malo / duplicado).

SQL = el SDR confirmó por conversación (ver 71):
      ✅ Dolor real   ✅ Fit ICP   ✅ Autoridad/acceso   ✅ Timing
      → se agenda reunión con AE.

Opportunity = el AE asistió a la reunión y confirmó que vale abrir trato.
      El AE puede RECHAZAR un SQL con motivo (ver 79 loop de feedback).

Tasa objetivo: MQL→SQL ≥ 20% · SQL→Opportunity ≥ 70%.
```

Ese "el AE puede rechazar un SQL con motivo" es sagrado: sin derecho a devolver, no hay calidad (ver `78`, `79`).

## Ejemplo real (LatAm)

Software para restaurantes, dos fuentes:

- **Inbound:** el dueño de una cafetería descarga tu guía "Cómo calcular el costo de tu plato" → **MQL**. El SDR lo revisa: es una cafetería de 1 local en Medellín, encaja → **SAL**. Lo llama, tiene el dolor y quiere resolver este mes → **SQL** → agenda con AE.
- **Outbound:** prospectas en frío a un grupo de 4 restaurantes (ver `21`). Responden. Calificas en la llamada corta (ver `71`): dolor + fit + timing → **SQL** directo → AE.

Ambos terminan como SQL medibles, con el mismo estándar.

## Errores comunes

- **No tener las definiciones por escrito.** Discutes calidad todo el mes sin data. Escríbelas.
- **Marketing declara SQL.** Marketing declara MQL; calificar es del SDR. Si marketing "califica", nadie confía en el número.
- **Sin derecho a devolver.** Si el SDR no puede rechazar un MQL malo ni el AE un SQL malo, la calidad se pudre (ver `78`).
- **Medir volumen y no conversión entre etapas.** El número que importa es MQL→SQL→Opportunity, no "cuántos leads".

## Siguiente paso

Con las definiciones cerradas, formaliza los tiempos y responsabilidades en el SLA (ver `74`). El criterio de qué hace a un SQL lo detallas en `70`. Mantén los estados limpios en el CRM con `77`, y cierra el círculo de calidad con `78` y `79`.
