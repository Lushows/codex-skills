# 94 — ABM (Account-Based Marketing) — introducción

**ABM (Account-Based Marketing)** es outbound al revés: en vez de contactar a miles de contactos sueltos y ver quién responde, eliges **pocas cuentas grandes específicas** y orquestas un ataque coordinado (marketing + SDR + vendedor) sobre cada una, tratando **la cuenta entera como el mercado**. Importa porque cuando persigues empresas grandes —donde un solo contrato vale mucho y la decisión la toma un **comité de compra** de varias personas— el outbound de volumen fracasa: no le vendes a "un lead", le vendes a una organización. Este módulo es la **introducción**: qué es, cuándo usarlo y en qué se diferencia del outbound normal. El desarrollo profundo (selección de cuentas, multi-threading, orquestación, medición) vive en el **Bloque 16 (`160`–`169`)**; aquí te doy el mapa para saber cuándo ir para allá.

## El principio: pocas cuentas, muchos contactos por cuenta, todo coordinado

El outbound clásico piensa en **contactos**: mil personas, un mensaje, X% responde (ver `05`). ABM piensa en **cuentas**: 30 empresas objetivo, y por cada una, varios contactos tocados a la vez con un mensaje hecho a la medida de ESA empresa. La lógica cambia en tres ejes:

| Eje | Outbound de volumen | ABM |
|---|---|---|
| **Unidad** | El contacto (lead) | La cuenta (empresa entera) |
| **Cantidad** | Cientos/miles de cuentas | 20–100 cuentas (tier 1) |
| **Contactos por cuenta** | 1, tal vez 2 | 4–10 (multi-threading, ver `162`) |
| **Mensaje** | 1:many, personalización ligera | 1:1 profundo, investigación por cuenta (ver `164`) |
| **Quién ejecuta** | El SDR solo | SDR + AE + marketing coordinados (ver `163`) |
| **Métrica de éxito** | Reuniones, leads | Engagement de la cuenta, no leads sueltos (ver `169`) |

**Por qué funciona:** en una empresa grande, una sola persona rara vez decide. Si contactas solo al gerente y él se va o dice que no, perdiste la cuenta. Con **multi-threading** (varios contactos a la vez: el usuario que sufre el problema, el jefe que aprueba, el que firma) construyes consenso interno y no dependes de un único punto de fallo (ver `165`, comité de compra `11`).

## Cuándo usar ABM (y cuándo NO)

Usa ABM cuando:
- El **ticket es alto** y justifica investigar cada cuenta a mano (contratos grandes; la economía la valida `economist_lushows`).
- Hay **pocas cuentas que valen la pena** — tu mercado real son 50–300 empresas, no 50.000.
- La decisión involucra un **comité** (enterprise, sector regulado; ver `165`, `175`).
- El ciclo de venta es largo y consultivo.

NO uses ABM cuando:
- Vendes a pymes con decisor único y ciclo corto → eso es outbound de volumen (ver `93`).
- Tu ticket es bajo: el costo de la personalización profunda no se paga.
- Necesitas volumen de reuniones rápido con muchas cuentas pequeñas.

Regla simple: **muchas cuentas pequeñas y baratas = volumen; pocas cuentas grandes y caras = ABM.** Muchos negocios corren las dos máquinas en paralelo, con SDRs distintos (ver `88`).

## Cómo se ve en la práctica (vistazo)

1. **Selección de cuentas** — el ICP de *cuenta*, no de contacto: qué 30–100 empresas encajan de verdad (tiering A/B/C; ver `161`, `16`).
2. **Mapa del comité** — por cada cuenta, quiénes son los 4–8 contactos clave (decisor, champion, usuario, bloqueador; ver `11`, `165`).
3. **Investigación por cuenta** — señales, prioridades, iniciativas públicas de ESA empresa (ver `164`, `37`).
4. **Play coordinado** — marketing calienta con contenido/ads a la cuenta, el SDR toca a varios contactos, el AE entra en las conversaciones serias (ver `163`, `168`).
5. **Medir por cuenta** — cuánto engagement generó la cuenta completa, no cuántos correos mandaste (ver `169`).

## Ejemplo de mensaje ABM (1:1, referencia la iniciativa de la cuenta)

```
Asunto: {iniciativa pública de la empresa} + {área del contacto}

Hola {nombre}, leí que {empresa} anunció {iniciativa real —
expansión, nueva línea, meta pública}. Suele implicar que
{consecuencia concreta para el área de esta persona}.

Trabajamos con {empresa comparable del sector} justo en ese
momento y {resultado}. Estoy contactando también a {otro rol}
de tu equipo porque esto los toca a ambos.

¿Vale una llamada de 20 min con {nombre del AE} y contigo?
```

La conversación consultiva, navegar el comité y **cerrar** el trato grande son oficio de venta enterprise → `ventas_lushows`. ABM te pone dentro de la cuenta; ahí se cierra.

## Errores comunes (qué NO hacer)

- Llamar "ABM" a mandar la misma plantilla a más gente. ABM es pocas cuentas + coordinación + 1:1 real, no volumen disfrazado.
- Single-threading: contactar a una sola persona de una cuenta grande. Un solo punto de fallo (ver `162`).
- ABM sin alineación con el vendedor/marketing: el SDR solo no hace ABM, es un esfuerzo de equipo (ver `163`).
- Aplicar ABM a pymes de ticket bajo: el costo no se paga.

## Siguiente paso

Decide si tu caso es volumen o ABM con la regla de arriba. Si es ABM, entra al **Bloque 16**: empieza por `160` (fundamentos) y `161` (seleccionar cuentas). Para el comité de compra ver `11` y `165`; para multi-threading `162`. Si es pyme de ciclo corto, vuelve a `93`. El cierre del deal grande → `ventas_lushows`.
