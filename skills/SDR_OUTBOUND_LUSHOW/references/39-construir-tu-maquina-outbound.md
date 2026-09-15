# 39 — Construir tu máquina de outbound

Este módulo junta todo el Bloque 3 en un solo mapa: cómo se conectan las herramientas, los datos y las acciones en **un sistema de punta a punta** que llena tu pipeline sin que un humano copie y pegue entre pantallas. "Máquina" es literal: una entrada (una lista/una señal), un flujo de transformaciones automáticas, y una salida (una reunión agendada en el calendario del vendedor). Aquí ves el diagrama completo y cómo armarlo por capas. La versión ampliada del sistema entero vive en `147` (automatización end-to-end) y `198` (el mapa de 0 a máquina).

## El principio: outbound es una tubería, no una bandeja

El error mental del principiante es ver el outbound como "mandar correos". La mentalidad correcta es **una tubería (pipeline) de datos**: los prospectos entran crudos por un extremo, pasan por estaciones que los enriquecen, filtran, contactan y califican, y salen como reuniones por el otro. Cada estación es una herramienta del Bloque 3. El valor está en que **el prospecto avanza solo** de estación en estación; el humano solo interviene donde su juicio manda (elegir el ICP, aprobar el mensaje, tener la conversación de venta).

Si dibujas tu operación y ves manos humanas moviendo datos entre cajas, ahí está tu cuello de botella. La máquina bien hecha tiene manos humanas solo en las **puntas** (estrategia y conversación), no en el medio (plomería).

## El diagrama de la máquina (flujo de punta a punta)

```
┌─────────────────────────────────────────────────────────────────┐
│  0. ESTRATEGIA (humano)                                          │
│     ICP definido + señal elegida + oferta clara                  │
│     (ver 10, 37 · el negocio/CAC → economist_lushows)            │
└───────────────┬─────────────────────────────────────────────────┘
                ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. FUENTE / SOURCING                                            │
│     Apollo · Sales Navigator · Google Maps · señales (37)        │
│     → cuentas + contactos crudos                    (ver 21,25,26)│
└───────────────┬─────────────────────────────────────────────────┘
                ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. ENRICHMENT + CALIFICACIÓN  ← el cerebro (Clay)               │
│     waterfall email (130) · verificar (28) · research IA (35)    │
│     · lead score fit+intent (38) · filtrar por Tier A/B          │
│                                                     (ver 29,31)   │
└───────────────┬─────────────────────────────────────────────────┘
                ▼  (write-back automático, ver 34)
┌───────────────┴───────────────┐         ┌─────────────────────────┐
│  3. CRM (fuente de verdad)     │◄───────►│  6. SEÑALES / INTENT    │
│     contactos, estados, deals  │  sync   │     RB2B · G2 · Bombora │
│     (ver 32, 141)              │         │     realimentan la      │
└───────────────┬───────────────┘         │     fuente (ver 36,37)  │
                ▼                          └─────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│  4. SENDING / CADENCIA                                           │
│     Smartlead/Instantly (33) sobre infra de deliverability:      │
│     dominios 2ºs (41) · SPF/DKIM/DMARC (42) · warmup (43) ·      │
│     límites (44) · copy y secuencia (Bloque 5 y 6)               │
│     stop-on-reply ON                                             │
└───────────────┬─────────────────────────────────────────────────┘
                ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. RESPUESTA → HANDOFF                                          │
│     IA clasifica respuesta (35,64) → interesado avisa al humano  │
│     (Slack/WhatsApp, ver 34) → SDR califica y agenda (71) →      │
│     Deal + contexto al AE (73)                                   │
└───────────────┬─────────────────────────────────────────────────┘
                ▼
        🤝 CONVERSACIÓN DE VENTA Y CIERRE  →  ventas_lushows
           (descubrimiento, objeciones, negociación, cierre)
                ▼
        📊 MEDICIÓN cierra el loop  →  cada etapa reporta ratios (80,81)
           lo que cierra recalibra el ICP y el score (79)
```

Fíjate en tres cosas: (a) el **humano solo toca las puntas** (estrategia arriba, venta abajo); (b) las flechas del medio son **automáticas** (integraciones, `34`); (c) es un **loop** —la medición y lo que cierra vuelven a afinar la estrategia y el score—.

## Cómo construirla, por capas (no todo de una)

No montes las 6 estaciones el día 1. Construye en este orden y prueba cada capa antes de la siguiente:

1. **Capa datos (semana 1):** fuente + Clay enrichment + verificación → una lista limpia de 200 cuentas Tier A/B. Sin esto, nada más importa (la lista es media venta, ver `20`).
2. **Capa envío (semana 1–2):** dominios secundarios + buzones + warmup **corriendo desde ya** (el warmup tarda ~2–3 semanas, arráncalo el día 1 aunque no envíes todavía, ver `43`).
3. **Capa CRM (semana 2):** conecta la lista al CRM con estados y dedup (ver `32`).
4. **Capa cadencia (semana 3, cuando el warmup esté listo):** copy + secuencia + stop-on-reply (Bloques 5 y 6).
5. **Capa handoff + automatización (semana 3–4):** respuesta → aviso → calificación → Deal (ver `34`, `73`).
6. **Capa señales (mes 2+):** cuando la base funcione, añade intent/señales para subir el timing (ver `36`, `37`).
7. **Capa medición (siempre):** desde el correo #1, mide reply, positive reply y reuniones (ver `80`).

## Ejemplo: la máquina de un solista en LatAm (servicios B2B)

```
Estrategia → ICP escrito, señal = "empresa contratando" (37)
Sourcing   → Apollo + Google Maps
Cerebro    → Clay: email waterfall + verify + Claygent opener + score (38)
CRM        → HubSpot Free, dedup por dominio
Envío      → Instantly, 3 dominios / 6 buzones, warmup, ~150/día
Handoff    → respuesta positiva → webhook → WhatsApp al dueño → agenda
Cierre     → el dueño conversa y cierra (con el oficio de ventas_lushows)
Medición   → hoja simple: enviados → respuestas → reuniones → clientes
```
Todo esto cabe en ~$250/mes (ver el stack de `30`) y lo opera una persona porque el medio está automatizado.

## Errores comunes

- **Construir todo antes de probar algo.** Monta la capa datos + un envío pequeño y valida que agendas UNA reunión antes de sobre-construir.
- **Olvidar arrancar el warmup temprano.** Tarda semanas; si lo dejas para el final, tu máquina espera parada.
- **Manos humanas en el medio.** Si copias/pegas entre Clay y el sequencer, automatiza esa costura (`34`).
- **No cerrar el loop de medición.** Sin saber qué cierra, la máquina no aprende (ver `79`, `83`).
- **Sobre-optimizar la máquina y descuidar la conversación.** La máquina agenda; si el vendedor no cierra, el problema no es la máquina → `ventas_lushows`.

## Siguiente paso

Dibuja TU diagrama con las herramientas que ya tienes y marca dónde hay manos humanas en el medio: esas son tus automatizaciones pendientes (`34`). Construye por capas en el orden de arriba, arrancando el warmup hoy. Para el sistema automatizado a fondo → `147`; el mapa de 0 a máquina completa → `198`. La frontera se mantiene: **esta máquina llena el pipeline; `ventas_lushows` lo cierra.**
