# 45 — Confluencia de señales (y el peligro de apilar indicadores)

**Confluencia** = varias evidencias INDEPENDIENTES apuntando a lo mismo. Es la idea más
importante de todo el bloque técnico: ninguna señal vale sola (`04`), pero tres capas distintas
de acuerdo construyen un caso. La palabra clave es *independientes* — y ahí está la trampa.

## Las capas del caso (lo que ya hace el sistema)

Un setup de calidad responde tres preguntas DISTINTAS:

| Capa | Pregunta | En el bot |
|---|---|---|
| **Régimen** | ¿El entorno favorece esta operación? | macroRegime (`03`): solo trending-up habilita convicción alta |
| **Técnico/momentum** | ¿El impulso acompaña? | RSI + MACD + SMAs (`04`) |
| **Nivel/ubicación** | ¿La entrada tiene un lugar lógico, con stop cerca? | S/R (`31`), distancia a SMA20 (`33`) |

Régimen bueno + momentum bueno + entrada EXTENDIDA = el trade FOMO de `10` (perdió 3/3).
Las tres capas deben estar; dos de tres no es "casi": es un setup incompleto.

## Scoring de setups (cómo formalizarlo)

En vez de un "sí/no" difuso, un checklist puntuado:

```
+2  régimen trending-up con confianza alta
+1  estructura 1h en HH/HL (32)
+1  entrada en retroceso hacia SMA20/soporte (no persiguiendo)
+1  espacio libre hasta la resistencia ≥ 2× el stop (R:R real)
+1  volumen confirma (cuando exista, 36)
-2  precio a >3% de la SMA20 (la regla de julio)
-1  divergencia RSI/MACD en máximos
```

El valor del score no es el número — es que **obliga a evaluar cada capa por separado** y deja
un registro auditable de por qué se entró (materia prima para el meta-análisis semanal).

## El peligro: apilar indicadores redundantes

- RSI, MACD, estocástico, CCI, Williams %R… **todos derivan del mismo precio**. Cuando "cinco
  indicadores confirman", no hay cinco evidencias: hay UNA evidencia (el precio subió rápido)
  contada cinco veces. Confluencia falsa = confianza inflada sin información nueva.
- Prueba mental rápida: "¿este indicador puede decir algo distinto del que ya tengo?" Si casi
  siempre están de acuerdo, uno de los dos sobra. (Caso Ichimoku, `42`; caso Bollinger, `40`.)
- Independencia real viene de FUENTES distintas: precio (técnico), volumen (`36`, participación),
  timeframe superior (`38`, otro horizonte), macro/régimen (`03`, otro dominio). Máximo un
  indicador de momentum, un mapa de niveles, un filtro de tendencia — y volumen. Más que eso
  es coleccionismo.
- Cada indicador nuevo agrega parámetros, y cada parámetro es una perilla para sobreajustar
  (`47`). El costo del apilamiento no es solo ruido: es una estrategia cada vez más frágil.

## Cómo aplica al AGENTE TRADING

- El diseño actual ya es confluencia bien entendida: régimen (Haiku) → técnico (JS) →
  interpretación y convicción (Sonnet). La mejora no es MÁS indicadores sino más independencia:
  volumen (`36`) y 4h (`38`) agregan fuentes nuevas; otro oscilador no.
- La convicción 1-10 que emite Claude ES el score — hacerle explícito un checklist como el de
  arriba en el prompt la vuelve consistente entre análisis y auditable después.
- Regla de oro para el backlog: **antes de agregar un indicador, nombrar qué información
  independiente aporta**. Si la respuesta es "confirma", no entra.
