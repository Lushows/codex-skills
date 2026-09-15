# 44 — Market Profile y value areas

El gráfico normal muestra el precio en el tiempo. El **perfil de volumen** (volume profile) gira
la pregunta: ¿en qué PRECIOS se negoció más? Se dibuja como un histograma horizontal pegado al
eje de precios — y revela dónde el mercado pasó tiempo construyendo posiciones y dónde solo pasó
de largo.

## Los conceptos clave

| Término | Qué es | Por qué importa |
|---|---|---|
| **POC** (Point of Control) | El precio con MÁS volumen negociado del período | El nivel de mayor consenso: el mercado lo consideró "justo" |
| **Value Area (VA)** | El rango de precios que concentra ~70% del volumen | La zona de valor aceptado |
| **VAH / VAL** | Bordes superior/inferior de la value area | Fronteras entre "precio aceptado" y "precio en disputa" |
| **HVN** (nodo de alto volumen) | Precio con mucho negocio | Actúa como imán/freno: hay memoria ahí |
| **LVN** (nodo de bajo volumen) | Precio con poco negocio | El precio lo cruza rápido: nadie lo defendió |

(El "Market Profile" original de los 80 usaba tiempo por precio en letras — TPO; el volume
profile moderno usa volumen. La lógica práctica es la misma.)

## La lectura útil

- **Los HVN son soportes/resistencias con evidencia**: no "el precio giró aquí dos veces" (`31`),
  sino "aquí se negociaron miles de BTC — aquí hay posiciones reales que serán defendidas".
  Es la versión medible de la "memoria del mercado".
- **Los LVN son vacíos**: cuando el precio entra en una zona de bajo volumen, tiende a
  atravesarla rápido hasta el siguiente HVN. Explica esos movimientos "en el aire".
- **Aceptación vs rechazo**: precio que sale de la VA y SE SOSTIENE fuera = el mercado acepta
  nuevos precios (tendencia). Precio que sale y regresa de inmediato = rechazo (falsa ruptura,
  vuelta al POC como imán).

## Límites honestos

- El perfil depende del período elegido (¿perfil de la semana? ¿del mes?) — grados de libertad
  que permiten "encontrar" el nivel que uno quiere, como en `41`.
- Hereda los problemas del volumen cripto (`36`): wash trading y volumen repartido entre
  decenas de exchanges. Un perfil de un solo exchange grande es aproximación, no verdad.
- No predice: describe dónde HUBO interés. Que lo vuelva a haber es probabilidad, no promesa.

## Cómo aplica al AGENTE TRADING

- El bot no lo usa hoy, y no es prioridad — pero es la evolución natural de sus
  soportes/resistencias: los S/R actuales se basan en giros del precio; un perfil de volumen
  los validaría con evidencia de participación (giro + HVN = nivel fuerte; giro en LVN = débil).
- Requisito previo: incorporar volumen al pipeline (`36`) — sin volumen por vela no hay perfil.
  Con las velas guardadas + volumen, un perfil aproximado (bucket de precios × suma de volumen)
  son ~20 líneas de JS. Orden correcto del backlog: volumen primero, perfil después, si el
  paper trading justifica la complejidad extra.
