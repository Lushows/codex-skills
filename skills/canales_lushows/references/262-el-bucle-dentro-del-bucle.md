# 262 · El bucle dentro del bucle

**Qué resuelve:** en un vídeo corto hay un bucle: se abre al principio y se cierra al
final. En doce minutos con un solo bucle no se llega: entre el minuto 3 y el 9 no
pasa nada que el espectador esté esperando. Con seis bucles sueltos tampoco: se
olvidan, se cruzan y se quedan sin pagar. Este módulo es la **contabilidad** de los
bucles de un episodio largo.

La mecánica de abrir y cerrar una pregunta está en editpro `31`. Aquí lo que importa
es otra cosa: **cuántos caben abiertos a la vez y en qué orden se cierran**.

---

## Tres niveles, y sólo tres

| Nivel | Duración | Cuántos | Función |
|---|---|---|---|
| **Maestro** | Todo el episodio | **1** | Es la pregunta del título. Se cierra en el penúltimo tramo |
| **De acto** | 2–4 minutos | 2–3 | Sostiene el bloque. Se cierra dentro del mismo acto |
| **De tramo** | 40–90 s | uno por tramo | Micro-promesa que empuja al minuto siguiente (`261`) |

El de tramo **no se anota como bucle**: es reenganche, vive y muere en noventa
segundos. Se contabilizan sólo el maestro y los de acto. En `ep01` eso son **seis
apuntes en toda la tabla**, no veinte.

## La regla de la pila

Los bucles se comportan como una pila: **el último que se abre es el primero que se
cierra**, y el maestro se cierra siempre el último.

```
A  maestro ─────────────────────────────────────────────────┐
   B ────┐                                                  │
         C ────────┐                                        │
                   D ──┐                                    │
                   ▼   ▼        E ──┐                       │
  min 1  2  3  4  5  6  7  8  9  10 11 12
                                   ▲                        ▼
                                  cierra E            cierra A · F
```

**Nunca más de tres abiertos a la vez.** Con cuatro, el espectador deja de llevar la
cuenta y ninguno produce tensión: produce confusión, que se parece al aburrimiento en
la curva de retención pero no se arregla acelerando.

Y la cuenta que de verdad importa: **un bucle sin minuto de cierre escrito en la tabla
no se abre.** Si al llenar la columna «cierra» queda un hueco, la frase que lo abría
se borra del guion. No se deja «ya veremos dónde lo pago».

## La tabla de bucles de `ep01`

Seis apuntes. Es el documento que se revisa cada vez que se cierra un tramo:

| ID | Pregunta que abre | Abre | Cierra | Nivel |
|---|---|---|---|---|
| **A** | ¿Queda algo de la torre cuando se mira el papel? | 1 (0:41) | **11** | maestro |
| B | ¿De dónde sale la leyenda, si el papel no dice nada? | 2 | 3 | acto |
| C | ¿Cómo se pasa de un camarote a un monumento? | 3 | 5 | acto |
| D | ¿Por qué el comprador no denunció? | 5 | 6 | acto |
| E | Si no hay papel de la torre, ¿de qué sí lo hay? | 7 | 8 | acto |
| **F** | ¿Qué más decía esa casilla? | 1 (implícito) | **12** | maestro diferido |

**F es el dato guardado** (`266`) y es un caso especial: se abre **sin que el
espectador sepa que se ha abierto**. En el minuto 1 la voz dice «aprendiz de
vendedor» y ahí no hay pregunta; la pregunta nace en el minuto 8, cuando aparece la
palabra *falsificador* en otro sitio, y el espectador vuelve solo a la casilla. Un
bucle que se abre hacia atrás es el más potente que hay y el más frágil: se rompe
entero si el dato se filtra antes (`266`, la auditoría).

## El cierre parcial

El minuto 6 cierra D y, de paso, **cierra la leyenda entera**: la historia que se
cuenta ha llegado a su punto más alto y no puede crecer más. Pero A sigue abierto,
porque A no preguntaba si la historia era buena, sino si tenía papel.

Ese medio cierre es lo que hace que la bisagra II→III no se sienta como un corte
arbitrario: algo **acaba de terminarse** y por eso se puede empezar otra cosa. Un acto
que termina sin cerrar nada se lee como abandono del tema.

## El recordatorio

Un bucle que lleva **más de seis minutos abierto** hay que recordarlo o el pago no se
cobra: el espectador ya no se acuerda de la pregunta y la respuesta le llega como un
dato más.

El recordatorio son **una frase y un motivo visual**, no un resumen:

- Frase: «de la torre, todavía, ni una línea». Ocho palabras, en el minuto 9 o 10.
- Visual: vuelve `balanza_*` o `m_cuenta` un instante. El motivo es el recibo del
  bucle y por eso está declarado como motivo y exento del antirrepetición (`254`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cuatro o más bucles abiertos a la vez | El espectador deja de llevar la cuenta; se lee como desorden |
| Abrir un bucle sin saber en qué minuto se paga | Queda huérfano y el final sabe a incompleto sin que nadie sepa por qué |
| Cerrar el maestro en el minuto 8 | Los cuatro últimos minutos ya no los espera nadie |
| Cerrar en desorden (el maestro antes que uno de acto) | El de acto que queda vivo después del final parece un error de montaje |
| Confundir reenganche con bucle | Se anotan veinte bucles, la tabla deja de servir y nadie la revisa |
| Bucle maestro abierto seis minutos sin recordatorio | Se paga en el 11 y el espectador ya no recuerda la pregunta |
| Contestar el bucle a medias y seguir | Peor que no cerrarlo: enseña que las promesas del canal no se pagan |

## Relacionado

`260` el arco de doce minutos · `261` reenganchar cada noventa segundos · `263`
capítulos y bisagras · `266` el dato que se guarda · `267` el remate diferido ·
`254` motivos: lo que vuelve a propósito · `93` estructura de episodio ·
editpro `31` bucle abierto (la mecánica del corte en formato corto)
