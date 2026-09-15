# 38 — Análisis multi-timeframe

Un **timeframe** es el tamaño de la vela: 1h = cada vela resume una hora. Mirar el mismo activo
en varios timeframes es como hacer zoom en un mapa: el 1h muestra la calle, el 4h el barrio,
el diario la ciudad. El error clásico es operar la calle ignorando que el barrio va en contra.

## El principio: el marco mayor manda

- **El 4h manda sobre el 1h**: una tendencia bajista en 4h convierte los "rebotes alcistas"
  del 1h en trampas — retrocesos dentro de una caída mayor.
- La razón es mecánica, no mística: cada vela de 4h contiene 4 velas de 1h. La estructura mayor
  ES la suma de las menores; pelear contra ella es pelear contra más capital y más inercia.
- Regla de dedo común: el marco de **decisión** (¿opero LONG o nada?) debe ser 3-6× mayor que
  el marco de **ejecución** (¿dónde exactamente entro?). Para ejecución en 1h → decisión en 4h.

## Alineación de timeframes

| 4h dice | 1h dice | Lectura |
|---|---|---|
| Alcista (HH/HL) | Alcista | Alineados: el mejor escenario para LONG |
| Alcista | Retrocediendo | El escenario DORADO del swing: comprar el retroceso del 1h dentro de la tendencia del 4h |
| Alcista | Bajista rompiendo estructura | Precaución: puede ser el inicio del giro mayor |
| Bajista | Alcista | Rebote contra-tendencia: el terreno donde mueren los LONGs |

El segundo caso merece énfasis: cuando el 1h "se ve mal" pero el 4h sigue alcista, ese sesgo
pesimista de corto plazo suele ser exactamente el HL (`32`) que se quería comprar.

## Errores típicos

- **Buscar hasta encontrar**: revisar 1h, 4h, diario, semanal… hasta que ALGUNO valide el trade
  que ya se quería hacer. Los marcos se definen ANTES, y son dos (máximo tres).
- **Parálisis**: con 5 timeframes siempre hay uno en contra. Dos marcos bastan.
- **Cambiar de marco a mitad del trade**: entrar por el 1h y, cuando va perdiendo, "convertirlo
  en trade de diario" para no cerrar. El stop se decide al entrar y en el marco de entrada.

## Cómo lo implementaríamos en el bot

Está en el backlog (`11`) y no requiere datos nuevos:

1. **Sin API extra**: agrupar las velas 1h que ya se guardan en bloques de 4 → velas 4h
   sintéticas (open = open de la 1ª, close = close de la 4ª, high/low = extremos, volumen = suma).
2. Calcular sobre ellas lo mínimo: SMA20 del 4h y estructura (¿HH/HL o LH/LL?).
3. Pasarlo al prompt como **filtro, no como señal**: `tendencia4h: alcista | bajista | lateral`.
   - 4h no alcista → convicción máxima limitada (como ya hace el régimen en `03`).
   - 4h alcista + retroceso en 1h hacia SMA20 → el setup de mayor calidad del sistema.

## Cómo aplica al AGENTE TRADING

- Es probablemente la mejora de mayor valor/costo del backlog junto al volumen (`36`): cero
  costo de datos, cálculo trivial en JS, y ataca directo el error FOMO de `10` — las entradas
  extendidas en 1h se ven claramente tardías cuando se mira la vela de 4h que las contiene.
- Encaja con la filosofía del sistema: el régimen macro (`03`) ya es un "timeframe superior"
  conceptual; el 4h le pone estructura de precio concreta a esa capa.
