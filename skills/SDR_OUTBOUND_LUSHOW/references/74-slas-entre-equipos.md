# 74 — SLAs entre equipos

Un SLA (Service Level Agreement = acuerdo de nivel de servicio) es un compromiso escrito de *quién hace qué, en cuánto tiempo, con qué calidad* entre marketing, el SDR y ventas. Sin SLA, los leads se enfrían esperando, cada equipo culpa al otro, y nadie sabe si el problema es la lista, la velocidad o el cierre. Con SLA, cada frontera del embudo tiene un reloj y un estándar medibles. Este módulo te da los SLA concretos que un equipo de outbound de élite firma, con tiempos defendibles 2026. Se apoya en las definiciones de `72` (MQL/SAL/SQL) y en el handoff de `73`.

## El principio: la velocidad de respuesta decide el resultado

El dato más citado y más real del outbound: **contactar un lead en los primeros 5 minutos vs. 30 minutos multiplica por ~9–20× la probabilidad de conectar y calificar.** Un lead que levantó la mano y espera 24 horas ya se enfrió, ya habló con tu competencia o ya se le olvidó. Por eso el corazón del SLA es *tiempo de respuesta*. El segundo corazón es *calidad*: cada equipo garantiza que lo que entrega cumple el umbral, para que el siguiente no reciba basura (ver `78`).

Un SLA es bidireccional: marketing se compromete a *cantidad y calidad de MQL*, el SDR a *velocidad y aceptación*, ventas a *tomar y trabajar los SQL*. Todos firman.

## Los SLA que importan (tabla maestra)

| Frontera | Compromiso | Tiempo objetivo 2026 |
|---|---|---|
| **Marketing → SDR** | Entregar MQL que cumplan ICP + intención (ver `72`) | Volumen y % de fit acordados/mes |
| **SDR responde MQL** | Primer intento de contacto tras entrar el MQL | **< 5 min** (inbound caliente) · < 1 h aceptable |
| **SDR acepta o devuelve (SAL)** | Revisar y aceptar/rechazar el MQL con motivo | < 24 h |
| **SDR trabaja el lead** | Nº de intentos antes de descartar (ver `77`) | **6–8 toques** en 10–14 días |
| **SDR → AE (handoff)** | Entregar SQL con contexto completo (ver `73`) | Mismo día de calificar |
| **AE toma el SQL** | Aceptar o rechazar el SQL con motivo (ver `79`) | **< 24 h** |
| **AE agenda/atiende** | Reunión realizada tras aceptar | Según disponibilidad, ≤ 5 días |

Los tiempos son plantilla; ajústalos a tu realidad, pero **ponles número**. "Rápido" no es un SLA; "< 5 minutos" sí.

## La cadencia como parte del SLA

Cuánto persigues un lead antes de rendirte también es un acuerdo (evita que un SDR abandone al primer no-contesta y que otro persiga eternamente). Estándar defendible:

```
CADENCIA MÍNIMA antes de marcar "sin respuesta" (ver 77):
  6-8 toques en 10-14 días, multicanal:
  Día 1  email + intento de llamada
  Día 2  llamada + LinkedIn (conectar)
  Día 4  email de seguimiento (nuevo ángulo)
  Día 6  llamada + nota de voz / audio WhatsApp
  Día 9  email "breakup" (cierre suave)
  Día 12 último intento por el canal que más abrió
→ Si nada: NO se descarta, pasa a nurture (ver 76).
```

(La construcción fina de secuencias multicanal está en los módulos de cadencia; aquí solo el compromiso de *cuánto* persistir.)

## Ejemplo de SLA escrito (para pegar y firmar)

```
SLA OUTBOUND — [Empresa], vigente [fecha], revisión mensual

MARKETING se compromete a:
  • Entregar ≥ [N] MQL/mes que cumplan ICP (ver 10) + intención definida (ver 72).
  • Marcar cada MQL con fuente y motivo de calificación.

SDR se compromete a:
  • Primer contacto a MQL inbound en < 5 min (horario laboral).
  • Aceptar o devolver cada MQL en < 24 h, con motivo si lo devuelve.
  • Trabajar cada lead 6-8 toques / 10-14 días antes de nurture.
  • Pasar solo SQL reales (ver 70) con handoff completo (ver 73).

VENTAS (AE) se compromete a:
  • Aceptar o rechazar cada SQL en < 24 h, con motivo (feedback, ver 79).
  • Realizar la reunión en ≤ 5 días hábiles.

MÉTRICAS que revisamos cada mes:
  • Tiempo medio de respuesta a MQL
  • % MQL aceptados (SAL) / devueltos
  • MQL→SQL, SQL→Opportunity (ver 72)
  • % de SQL rechazados por el AE y motivo (ver 78, 79)
```

## Cómo se gobierna: la reunión de sincronía

El SLA vive o muere en una reunión quincenal corta (30 min) marketing + SDR + ventas donde miran los números contra el acuerdo, no opiniones. Si MQL→SQL cae, ¿es lista o mensaje? Si SQL→Opportunity cae, ¿son leads malos (ver `78`) o el AE? La data manda, no el ego. Ahí también fluye el feedback del AE (ver `79`).

## Errores comunes

- **SLA sin números.** "Responder pronto" no se puede medir ni exigir. Pon minutos y horas.
- **SLA de un solo lado.** Si solo el SDR tiene compromisos y el AE no toma los SQL, el sistema falla igual.
- **Firmarlo y no revisarlo.** Un SLA sin reunión de sincronía es papel muerto. Revísalo mensual.
- **Castigar velocidad sacrificando calidad.** Responder en 5 min pero agendar basura no sirve (ver `78`). Velocidad *y* filtro.

## Siguiente paso

Con el SLA firmado, asegúrate de que las definiciones que lo sostienen (`72`) estén claras y el handoff (`73`) las cumpla. Los leads que la cadencia no cerró van a `76`. Alimenta la reunión de sincronía con el loop de feedback de `79` y la higiene de datos de `77`.
