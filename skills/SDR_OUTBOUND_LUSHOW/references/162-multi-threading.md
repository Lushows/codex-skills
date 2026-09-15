# 162 — Multi-threading (varios contactos por cuenta, sin quemarla)

**Multi-threading** es contactar a **varias personas de la misma cuenta a la vez** —el usuario que sufre el problema, su jefe que aprueba, el que firma— en vez de apostar todo a un solo contacto (*single-threading*). En ABM no es opcional: es la mecánica que evita el único punto de fallo y construye consenso interno. Pero hacerlo mal —cinco correos idénticos a cinco personas el mismo día— quema la cuenta entera de un golpe. Este módulo es cómo tocar a varios sin spamear ni verte torpe.

## El principio: por qué single-threading pierde deals

En una cuenta grande, apostar a una sola persona falla por probabilidad pura:
- **Se va de la empresa.** Rotación B2B real: un buen % de tus contactos cambia de trabajo cada año. Si era tu único hilo, el deal muere.
- **Dice que no (o no responde) y se acabó.** Sin otro hilo, no hay segunda vía.
- **No tiene poder.** Puede que tu contacto ame tu producto pero no decida ni tenga presupuesto (ver mapa de poder en `165`).

Con multi-threading, si un hilo se cae, los otros siguen. Y más importante: los deals se cierran cuando **varias personas internas quieren avanzar a la vez**. Tú no convences a la empresa desde afuera; enciendes a varios contactos para que empujen desde adentro. Dato de referencia: los deals enterprise que se ganan tienen bastantes más contactos involucrados que los que se pierden. Más hilos = más consenso = más cierre.

## A quiénes tocar por cuenta (los roles del comité)

No contactas "a más gente"; contactas a **roles complementarios** del comité (detalle en `11` y `165`):

| Rol | Qué le importa | Ángulo del mensaje |
|---|---|---|
| **Usuario / doer** | El dolor diario, que su trabajo sea menos infierno | Beneficio operativo concreto |
| **Champion** | Verse bien resolviendo esto, avanzar internamente | Le das munición para vender adentro |
| **Decisor económico** | ROI, riesgo, presupuesto | Números, caso de negocio (`economist_lushows`) |
| **Bloqueador técnico/legal** | Seguridad, integración, cumplimiento | Prueba de que no es un riesgo |
| **Sponsor/ejecutivo** | Iniciativa estratégica, resultado de negocio | Referencia a su iniciativa pública (`164`) |

En Tier A tocas 5–10; en 1:few, 3–6. La regla: al menos **el usuario + el que aprueba + un ejecutivo**.

## Cómo tocar a varios SIN quemar la cuenta

La clave es que cada persona reciba un mensaje **distinto y relevante a su rol**, con ritmo escalonado, y que reconozcas abiertamente que hablas con más gente del equipo (eso genera credibilidad, no incomodidad).

1. **Mensajes diferenciados por rol.** El correo al usuario habla de dolor operativo; el del director, de ROI. Nunca la misma plantilla clonada (ver frameworks en `56`, personalización `164`).
2. **Escalona, no dispares todo el mismo día.** Empieza por 1–2 hilos (usuario + champion); a los pocos días suma al decisor. Si mandas a los 6 el lunes a las 9am, la cuenta huele a máquina.
3. **Nombra a los otros hilos ("naming").** "Estoy hablando también con {nombre/rol} de tu equipo sobre esto." Esto es lo que convierte varios correos sueltos en un movimiento coordinado y le da permiso social a cada quien de responder.
4. **Usa la referencia interna.** Cuando el usuario responde, pídele quién más debería estar: "¿tiene sentido sumar a {rol}?" — y ahora entras a ese contacto *referido desde adentro*, no en frío.
5. **Coordina canales.** Email al director, LinkedIn al usuario, llamada al champion: no satures a una persona por todos lados; reparte (orquestación en `168`).
6. **Un dueño de la cuenta.** Aunque toques a varios, alguien (tú o el AE) lleva el mapa para no cruzar mensajes contradictorios (ver play coordinado `163`).

## Ejemplo: secuencia multi-thread escalonada (una cuenta Tier A)

```
Día 1  → Usuario (jefe de operaciones): email dolor operativo
Día 1  → Champion (coord. de proyecto): LinkedIn, tono par a par
Día 4  → Director (decisor económico): email ROI + caso comparable,
          "hablo también con {usuario} de tu equipo"
Día 6  → Usuario: follow-up + "¿quién más debería ver esto?"
Día 8  → Ejecutivo/sponsor: email corto ligado a su iniciativa pública (164)
Día 10 → Champion: llamada (opener y hook en 53/58; la conversación
          de venta profunda → ventas_lushows)
```

Cada mensaje es 1:1, referencia a ESA cuenta, y cada uno sabe que hay más hilos. No es volumen; es un cerco coordinado.

## Errores comunes (qué NO hacer)

- **La misma plantilla a 6 personas.** Se dan cuenta (a veces se reenvían el correo entre ellos) y matas la cuenta. Diferencia por rol.
- **Disparar todos los hilos el mismo día.** Escalona.
- **Ir directo al CEO ignorando al usuario.** El ejecutivo pregunta a su equipo; si el usuario no te conoce, te hunde. Toca abajo y arriba.
- **No nombrar los otros hilos.** Pierdes el efecto de coordinación; parecen correos aislados.
- **Saturar a una persona por email + LinkedIn + llamada + WhatsApp el mismo día.** Reparte canales entre personas (`168`).

## Frontera y siguiente paso

Detectar **quién tiene poder** dentro del comité (el mapa político) es `165`. La **conversación consultiva, manejar al bloqueador, alinear al comité y cerrar** son oficio de venta enterprise → **`ventas_lushows`**. Tú abres y sostienes los hilos; el AE cierra.

**Siguiente paso:** por cada cuenta Tier A, lista sus 5–8 contactos por rol (usa `165`), escribe un ángulo distinto por rol y arma la secuencia escalonada de arriba. Coordina con marketing y el AE en `163`.
