# 69 — Horarios y ejecución óptima

Este módulo junta las piezas de `61`-`64` en la pregunta operativa: **cuándo y cómo ejecuta
el bot, y qué se puede mejorar en live sin sobre-ingeniería**.

## Cómo ejecuta el bot hoy (paper)

- **Ciclo de análisis cada 2 horas**, 24/7: baja velas 1h de BTC y ETH, Haiku clasifica el
  régimen macro, se evalúa señal, y si hay entrada se simula a precio de mercado con el
  modelo de costos (0.1% comisión + 0.05% slippage por lado).
- El ciclo de 2h es coherente con swing en velas 1h: decisiones sobre velas cerradas, sin
  ansiedad de tick a tick. Un bot que mira el precio cada minuto no es más listo — es más
  impulsivo y paga más peajes (`65`).
- Implicación honesta: entre ciclo y ciclo el bot está "ciego" hasta ~2h. Para las entradas
  es aceptable; para las salidas es exactamente el hueco que las OCO cierran en live (`66`).

## Ejecutar en horas líquidas vs ilíquidas

Resumen operativo de `64` (horas de Colombia, UTC-5):

| Franja | Liquidez | Trato recomendado |
|---|---|---|
| 8 a.m. – 4 p.m. entre semana (sesión EE.UU., solape con Londres en la mañana) | Máxima | Ejecución normal |
| Noche (sesión Asia) | Media | Normal con atención |
| Madrugada profunda (~4-7 a.m.) | Baja | Más colchón en stops; convicción mínima más alta |
| Fin de semana | Baja y traicionera | Exigir más convicción o reducir tamaño; señales valen menos |
| ±2h de FOMC/CPI | Líquida pero violenta | **No abrir posiciones nuevas** (`53`) |

## Mejoras de ejecución para live (por orden: primero lo que protege, luego lo que optimiza)

1. **OCO en el exchange** (`66`) — obligatoria, no negociable. Todo lo demás es opcional.
2. **Registrar la ejecución real**: precio de decisión, precio de llenado, spread del
   momento, hora. Es la materia prima para auditar los 5 bps (`63`) con datos propios.
3. **Factor de franja horaria**: un multiplicador simple (fin de semana / madrugada →
   convicción mínima +1 o tamaño ×0.5). Barato de implementar, ataca el riesgo real.
4. **Calendario macro**: pausar entradas alrededor de FOMC/CPI (fechas públicas, se cargan
   por adelantado).
5. **Entradas limit agresivas** (mejorar unos bps de spread) — solo DESPUÉS de que los datos
   del punto 2 muestren que el ahorro compensa los llenados perdidos. Optimización de último
   orden: el edge del bot vive en el régimen y el riesgo, no en la microejecución.

## El anti-patrón: sobre-optimizar la ejecución

Con capital de laboratorio, la diferencia entre una ejecución "buena" y una "perfecta" son
centavos; la diferencia entre tener stop en el exchange o no tenerlo puede ser la cuenta.
Regla de prioridades: **seguridad de ejecución > medición > optimización**. Un bot que rasca
2 bps con limits sofisticadas pero se cae sin stop una noche de hackeo optimizó lo que no era.

## Cómo aplica al AGENTE TRADING

Hoja de ruta de ejecución de la Fase 8, en una línea: testnet con OCO y reconciliación →
live con tamaño mínimo registrando cada llenado → recién entonces, y con datos propios,
decidir factor horario, calendario macro y entradas maker.
