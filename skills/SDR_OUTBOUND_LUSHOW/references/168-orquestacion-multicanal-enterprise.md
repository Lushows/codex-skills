# 168 — Orquestación multicanal enterprise (coordinar canales a nivel cuenta)

En volumen coordinas canales a nivel **contacto**: una secuencia email + LinkedIn + llamada para cada persona (ver `61`). En ABM subes un nivel: orquestas canales a nivel **cuenta** —varios contactos, varios canales, marketing y ventas, todo apuntando a la misma empresa en la misma ventana de tiempo—. Este módulo es cómo se dirige esa orquesta sin que suene a ruido: qué canal a quién, en qué orden, sin saturar a nadie y sin que dos personas de tu lado manden mensajes que se contradigan. La orquestación es lo que convierte "varios toques sueltos" en "un cerco coordinado" que la cuenta siente como presencia, no como spam.

## El principio: el ritmo de la cuenta, no del contacto

La unidad de planeación es la **cuenta**. Piensas: "en las próximas 3 semanas, la cuenta X va a recibir —repartido entre sus contactos y canales— ads, un correo del SDR al usuario, una conexión de LinkedIn del AE al decisor, una invitación a webinar, y un post mío en el feed de dos de ellos". Ninguna persona recibe todo; **la cuenta sí percibe presencia sostenida**. La diferencia con el spam es que cada toque es relevante a ESA persona y ESA empresa (research `164`), y están coordinados para no chocar.

## Los canales y a qué rol sirven mejor

| Canal | Fuerte para | Nota |
|---|---|---|
| **Email** | El toque base, el caso de negocio, decisores ocupados | Cuida deliverability, es recurso escaso (`44`) |
| **LinkedIn** | Usuarios/champions, warming, ver y ser visto (`57`) | Menos saturado que el email para muchos roles |
| **Llamada** | Champion/usuario que ya te vio; romper el hielo | Opener/hook `53`,`58`; la venta profunda → `ventas_lushows` |
| **WhatsApp** | LatAm: cercanía, respuesta rápida una vez hay permiso | Infra y cuidado en `47`; no arranques en frío aquí |
| **Ads / retargeting** | El "aire": calentar la cuenta, retargetear a quien interactúa | Skills de ads; públicos por cuenta/lista |
| **Contenido** | Presencia experta en el feed del comité | `167` |
| **Evento** | Excusa premium, contacto humano | `166` |
| **Correo físico / regalo** (para Tier A) | Romper el ruido con algo tangible | Caro; reserva para cuentas soñadas |

## Cómo orquestar sin saturar (las reglas)

1. **Reparte canales entre personas, no los apiles en una.** Al decisor: email + LinkedIn del AE. Al usuario: LinkedIn + llamada del SDR. Nadie recibe los 5 canales; el conjunto sí cubre la cuenta (multi-threading `162`).
2. **Escalona en el tiempo.** No dispares todo el mismo día. El aire (ads/contenido) va primero y sostenido; la tierra (correo/llamada) entra después; el evento en su fecha. Ritmo de semanas, no de horas.
3. **Un dueño de la orquesta por cuenta.** Alguien lleva el mapa (tú o el AE) para que los mensajes no se contradigan ni se dupliquen. Sin director, la orquesta suena a caos (ver `163`).
4. **Deja que las señales disparen el siguiente canal.** Si un contacto abre 2 correos o hace clic en un ad → sube el canal: de email a LinkedIn, o a una llamada. Intent manda el ritmo (`37`, routing `38`).
5. **Respeta límites y deliverability.** Multicanal NO significa más email; significa **menos presión en cada canal** repartiendo. Los límites de envío por buzón (~30–50/día; ver `44`) y la infra multicanal (`48`) siguen mandando.
6. **Todo registrado a nivel cuenta.** Cada toque, en el CRM, colgado de la **cuenta** además del contacto, para que cualquiera del equipo vea el estado completo (arquitectura `141`, higiene `77`).

## Ejemplo: orquestación de 3 semanas sobre una cuenta Tier A

```
CUENTA X — comité: Usuario (Andrea), Decisor (Ricardo), TB (Camilo)

Sem 1  AIRE: ads a la empresa (públicos por cuenta) + 2 posts míos (167)
       en el feed. Sin correos aún.
Sem 1  SDR: LinkedIn a Andrea (comentar → conectar → nota).
Sem 2  SDR: email a Andrea (dolor operativo) + email a Ricardo (ROI),
       ambos nombrando al otro hilo (162). AE conecta con Ricardo.
Sem 2  Señal: Andrea abre 2x + clic en ad → sube a llamada (SDR).
Sem 3  Invitación a webinar (166) al comité. Marketing retargetea
       a quien interactuó. SDR toca a Camilo (TB) antes de la demo (165).
Sem 3  Un hilo agenda → handoff al AE con el mapa (73) → ventas_lushows.
```

Reparte 3 personas × 5 canales en 3 semanas: la cuenta siente presencia constante; **ninguna persona se sintió spameada**.

## Herramientas para orquestar

- **Secuenciadores** (Outreach, Salesloft, Smartlead, Instantly; ver `33`) manejan email + tareas de LinkedIn/llamada por contacto.
- **Plataformas ABM** (6sense, Demandbase, HubSpot ABM) coordinan aire (ads/intent) + tierra a nivel cuenta — potentes pero caras; para equipos pequeños se sustituye con CRM + secuenciador + una hoja de "estado de cuenta" bien llevada.
- **Clay** (`31`) para armar y enriquecer las listas que alimentan todos los canales.
- El pegamento son las **integraciones/automatización** (`34`): que una señal en ads dispare una tarea al SDR, etc.

## Errores comunes (qué NO hacer)

- **Multicanal = más email.** No: es repartir presión entre canales. Apilar todo en email quema deliverability (`44`, `45`).
- **Saturar a una persona por todos lados el mismo día.** Se siente acoso. Reparte por persona y escalona.
- **Sin director de la cuenta:** SDR y AE mandan mensajes que se pisan o contradicen.
- **Ignorar señales:** seguir el guion rígido en vez de subir el canal cuando la cuenta muestra intent (`37`).
- **No registrar a nivel cuenta:** nadie ve el cuadro completo y se repiten toques.

## Frontera y siguiente paso

La orquestación **crea y sostiene** conversaciones; llevarlas a demo, propuesta y **cierre** es venta enterprise → **`ventas_lushows`**. La pauta del "aire" → skills de ads. Cálculos de presión/capacidad exactos → `Matematicas_lushows`.

**Siguiente paso:** por cada cuenta Tier A, dibuja el plan de 3 semanas repartiendo canales entre los contactos del comité (`165`), nombra un dueño de la cuenta y define qué señal dispara subir de canal (`37`/`38`). Ancla la secuencia base de contacto en `61` y la infra multicanal en `48`; mide todo por cuenta en `169`.
