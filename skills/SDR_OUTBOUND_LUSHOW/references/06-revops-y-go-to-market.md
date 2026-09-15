# 06 — RevOps y go-to-market

El SDR no trabaja en el vacío: es una pieza dentro de un motor comercial más grande. Este módulo explica el **go-to-market (GTM — la estrategia de cómo una empresa lleva su producto al mercado y consigue clientes)** y **RevOps (Revenue Operations — el equipo/función que hace funcionar ese motor: datos, herramientas, procesos y métricas)**, para que entiendas dónde encaja tu outbound y por qué sin "la fontanería" invisible de RevOps ninguna máquina de outbound escala.

## El principio: el pipeline se rompe en las junturas, no en las personas

Un SDR brillante con un CRM caótico produce poco: los leads se pierden, nadie sabe qué mensaje funcionó, los datos están sucios y el handoff al AE se cae. El outbound de élite no es solo "buenos correos": es un **sistema conectado** donde el lead fluye sin fricción de la lista → la secuencia → el CRM → el AE → el reporte. RevOps es quien construye y aceita ese sistema. **La mayoría de los outbounds que "no funcionan" fallan en las junturas, no en el talento.**

## Qué es go-to-market (GTM)

El GTM es **cómo tu empresa consigue y sirve clientes**: qué vendes, a quién, por qué canal, a qué precio y con qué proceso. El outbound es **una de las jugadas** dentro del GTM. Los grandes motores GTM combinan varios:

| Motor GTM | Cómo consigue clientes | Skill |
|---|---|---|
| **Outbound / sales-led** | SDRs contactan cuentas en frío | **esta skill** |
| **Inbound / marketing-led** | Contenido + SEO atraen | parcial `02` |
| **Paid / demand-gen** | Anuncios generan/capturan demanda | `facebook_ads`, `google_ads`, `tiktok_ads` |
| **Product-led (PLG)** | El producto se prueba gratis y se vende solo | fuera de alcance |
| **Partner/channel** | Aliados revenden o refieren | fuera de alcance |

La decisión de **qué mezcla de motores** conviene a un negocio (y si el CAC de cada uno cierra) es estrategia de negocio → `economist_lushows`. Esta skill **ejecuta** el motor outbound una vez decidido.

## Qué hace RevOps (y por qué lo necesitas aunque seas solista)

RevOps es la función que mantiene el motor comercial funcionando. Sus cuatro áreas:

1. **Datos** — que la info de leads/cuentas esté completa, limpia y actualizada (ver `28`, `139`). Datos sucios = outbound que rebota y se va a spam.
2. **Herramientas (tech stack)** — que las herramientas estén conectadas y sincronizadas: la de sourcing → el sequencer → el CRM → el dashboard (ver `30`, `146`, `148`). Sin integración, copias y pegas a mano y todo se desincroniza.
3. **Procesos** — reglas claras: qué es un SQL, cómo se enruta un lead, cómo es el handoff, qué SLA hay entre equipos (ver `72`, `73`, `74`, `142`).
4. **Métricas y reporting** — los dashboards que dicen qué funciona y dónde se rompe el embudo (ver `80`, `144`).

Aunque seas una sola persona, **RevOps básico eres tú media hora a la semana**: mantener el CRM limpio, conectar tus dos o tres herramientas, y mirar tus números. Saltártelo es la razón #1 por la que los solistas se estancan.

## Dónde vive el SDR en el motor

```
                    ┌─────────────── RevOps (datos · stack · proceso · métricas) ───────────────┐
                    │                          (la fontanería que sostiene todo)                 │
MARKETING/ADS ──┐   │                                                                             │
                ├───┼──► SDR/BDR ──(SQL)──► AE ──(cierre)──► AM ──(retención/expansión)           │
OUTBOUND ───────┘   │      ▲                   │                                                  │
(esta skill)        │      └── loop de feedback: qué targeting sí cierra (ver 79) ────────────────┘
```

El SDR es el **motor de arranque** del pipeline outbound, pero está enchufado a RevOps por todos lados: saca datos del stack, registra todo en el CRM, y su output alimenta las métricas. El **loop de feedback** (ver `79`) es clave: lo que el AE sí cierra le dice al SDR a quién targetear mejor. Sin RevOps midiendo eso, el SDR nunca afina su lista.

## El stack mínimo de un motor outbound

No necesitas el stack enterprise para arrancar. El mínimo viable:

```
Sourcing de datos   → Apollo o Clay (ver 25, 31)
Sequencer / envío   → Instantly o Smartlead (ver 33)
CRM                 → HubSpot free o Pipedrive (ver 32)
Verificación        → NeverBounce o ZeroBounce (ver 28)
Dashboard           → el reporte del propio CRM al inicio (ver 144)
```

Todo conectado (idealmente con la integración nativa o vía Make/n8n; ver `34`, `107`) para que un lead fluya de la lista al CRM sin copiar y pegar. El stack a fondo está en Bloque 3 (`30`–`39`) y Bloque 10 (`100`–`109`).

## Errores comunes (qué NO hacer)

- **Comprar herramientas antes de definir el proceso.** El stack sirve al proceso, no al revés. Primero decide cómo fluye el lead, luego elige la herramienta (ver `01`, diagnóstico primero).
- **CRM como cementerio.** Un CRM donde nadie registra ni actualiza es peor que no tenerlo: da datos falsos. Higiene de CRM en `77`.
- **No medir el loop AE→SDR.** Si el SDR no sabe qué leads sí cerraron, sigue trayendo el tipo equivocado. Ese feedback es RevOps puro (ver `79`).
- **Stack desconectado.** Cinco herramientas que no se hablan = trabajo manual, datos desincronizados y errores. Integra (ver `146`).

## Las fronteras

- **¿Qué motor GTM y si el CAC cierra?** → `economist_lushows` (estrategia de negocio).
- **El cierre y la conversación de venta** dentro de la reunión → `ventas_lushows`.
- **RevOps a fondo** (arquitectura de CRM, routing, atribución, forecasting avanzado) → Bloque 14 (`140`–`149`).
- **Números exactos** (CAC por outbound, ROI del stack) → `Matematicas_lushows` y `149`.

## Siguiente paso

Dibuja tu motor: ¿qué motores GTM usas hoy y dónde encaja el outbound? Luego arma tu stack mínimo (sourcing + sequencer + CRM + verificación) y conéctalo. Si ya tienes el stack, ve a `144` para montar el dashboard que te dice dónde se rompe el embudo. La estrategia de qué motores priorizar → `economist_lushows`.
