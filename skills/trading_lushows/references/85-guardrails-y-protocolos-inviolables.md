# 85 — Guardrails y protocolos inviolables

Un **guardrail** es una barrera de seguridad que impide que el sistema haga algo prohibido —
aunque una parte del sistema (la IA, un bug, un dato corrupto) lo intente. En un bot de trading
los guardrails no son paranoia: son la diferencia entre "un bug feo" y "un bug que quema la
cuenta".

## El principio rector: el sistema hace IMPOSIBLE lo prohibido

Hay dos formas de "prohibir" algo:

| Enfoque | Ejemplo | Problema |
|---|---|---|
| **Pedirlo** (débil) | El prompt dice "nunca arriesgues más de 1.5%" | La IA puede ignorarlo, alucinar, o devolver un formato raro |
| **Imposibilitarlo** (fuerte) | El código de sizing NUNCA calcula más de 1.5%, diga lo que diga la IA | No depende de que nadie "se porte bien" |

Regla de la casa: **las instrucciones al modelo son deseos; el código es ley.** Todo límite que
importe (riesgo por trade, solo LONG, convicción mínima, máximo de posiciones) debe existir
como verificación en código, no solo como frase en el prompt.

## Defensa en profundidad: validar en CADA capa

La misma regla se verifica en todas las capas que atraviesa una decisión, porque cualquier capa
puede fallar:

```
1. PROMPT pide     → "responde convicción 1-10, solo LONG, formato JSON"
2. JS verifica     → parsea la respuesta; si convicción no es número 1-10, si la
                     dirección no es LONG, si falta un campo → RECHAZA el trade
3. Sizing recalcula→ el tamaño sale de la fórmula de riesgo 1.5%, nunca del texto de la IA
4. Broker rechaza  → la capa de ejecución valida de nuevo (fondos, límites) antes de enviar
```

Parece redundante. ES redundante — a propósito. La probabilidad de que fallen las 4 capas a la
vez es muchísimo menor que la de que falle una. Y cada capa que rechaza algo deja un log que
dice exactamente dónde se rompió el protocolo.

## Caso real: el bug de convicción-0

En el AGENTE TRADING, trades disparados por rutas distintas (automático vs manual) llegaban a
registrarse con convicción 0 — un valor imposible según el protocolo (la escala es 1-10, y
ejecutar exige ≥8). El sistema estaba operando con un dato que violaba sus propias reglas y
nadie lo veía porque "el número existía".

La solución tuvo dos partes, y las dos son lecciones generales:
1. **Etiquetar el origen**: cada trade lleva `source: auto | manual`. Un dato sin procedencia
   no se puede auditar; con etiqueta, la ruta que produce basura se encuentra en minutos.
2. **Rechazar lo imposible**: convicción fuera de 1-10 no se guarda "para revisar después" —
   se bloquea. Un valor imposible que entra a la base de datos envenena todas las estadísticas
   que se calculen sobre ella (calibración, PF por convicción, etc. — ver `89`).

Moraleja: los guardrails no solo evitan catástrofes; **mantienen los datos limpios**, y sin
datos limpios no hay aprendizaje.

## Propiedades de un buen protocolo inviolable

- **Falla cerrado**: ante duda, ambigüedad o error → NO operar. Perderse un trade cuesta poco;
  un trade fantasma cuesta caro.
- **Ruidoso al fallar**: cada rechazo se loguea y (si es grave) alerta (ver `86`). Un guardrail
  silencioso que rechaza todo es un bot apagado que nadie nota.
- **Sin excepciones manuales "por esta vez"**: el día que el humano puentea el guardrail porque
  "está seguro", el protocolo dejó de existir.
- **Probado**: se le lanzan entradas inválidas a propósito (convicción 11, dirección SHORT,
  JSON roto) y se verifica que rechaza. Un guardrail no probado es decoración.

## Cómo aplica al AGENTE TRADING

- Ya implementado: validación en capas prompt→JS→sizing, umbral convicción ≥8 verificado en
  código, solo-LONG estructural, riesgo 1.5% calculado en JS (nunca por la IA), etiqueta
  `source` tras el bug de convicción-0.
- Antes del go-live (22-ago-2026): agregar la capa broker real (la API del exchange como última
  validación), un kill-switch (apagar operaciones nuevas sin apagar el monitoreo) y límite de
  pérdida diaria/semanal que bloquee entradas nuevas al tocarse.
- Test periódico: inyectar respuestas malformadas de la IA en un entorno de prueba y confirmar
  que las 4 capas rechazan. Si algún día una entrada inválida pasa, eso es incidente grave
  aunque el trade hubiera sido ganador.
