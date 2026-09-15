# 119 — Portfolio de estrategias

## La idea

Un trader maduro no vive de una sola estrategia: combina varias que ganan en **momentos
distintos**. A eso se le llama portfolio de estrategias, y su magia está en una palabra:
**descorrelación** — que no pierdan todas a la vez.

| Familia | Cuándo gana | Cuándo sufre |
|---|---|---|
| **Trend following** (seguir tendencia) | Tendencias largas y claras | Laterales: entra en cada breakout falso |
| **Mean reversion** (reversión a la media: comprar caídas exageradas dentro del rango) | Mercados laterales | Tendencias fuertes: "compra la caída" que nunca rebota |
| **Momentum entre activos** | Rotaciones sostenidas | Cambios bruscos de líder |
| **Delta neutral** (funding/basis, ver `114`-`115`) | Euforia apalancada | Mercados fríos sin prima |

Trend y reversión son casi opuestas por diseño: el lateral que desangra a una alimenta a
la otra. Esa es la pareja clásica de arranque.

## Por qué suaviza el equity

El **equity curve** (la curva del capital en el tiempo) de una sola estrategia tiene valles
largos: los meses donde su régimen favorito no aparece. Dos estrategias descorrelacionadas
se turnan — cuando una descansa, la otra trabaja — y la curva combinada baja menos y más
corto, **sin necesitar que ninguna mejore**. Matemática de diversificación pura: mismo
retorno esperado, menos sufrimiento en el camino. (Cálculos de correlación y drawdown →
`Matematicas_lushows`.)

La condición es real: si las estrategias pierden juntas (todo LONG cripto cae junto en
risk-off), no hay portfolio — hay la misma apuesta con dos nombres.

## Las advertencias honestas

- **Cada estrategia debe tener edge propio demostrado** (expectancy positiva, ≥30 trades,
  ver `00`). Combinar dos estrategias perdedoras da una perdedora diversificada.
- **Complejidad**: dos estrategias = dos protocolos que auditar, dos memorias que mantener,
  el doble de formas de romperse. Se agrega una estrategia cuando la anterior está probada,
  no antes.
- **Presupuesto de riesgo compartido**: el riesgo total no se duplica porque haya dos
  estrategias; se reparte (p. ej. 1.5% total dividido, no 1.5% cada una) hasta medir la
  correlación real entre ellas.

## Cómo aplica al AGENTE TRADING

- Hoy el bot es **una estrategia**: trend-following LONG spot en 1h. Correcto para esta
  etapa — primero probar el edge de una antes de coleccionar varias.
- La consecuencia visible ya la vive: en `trending-down`, `ranging` y `risk-off` no opera
  y pasa semanas sin aprender (ver `03`). Un portfolio es la solución de fondo a ese
  problema, no un lujo.
- **Ruta de evolución ordenada**: ① SHORT en paper (mismo motor trend, régimen espejo — ya
  en backlog) → ② tercer par (diversificación de activo, ver `126`) → ③ recién después,
  una estrategia de familia distinta (reversión en ranging) como módulo separado con su
  propia memoria y su propio período de paper.
- Regla fija: ninguna estrategia nueva toca capital (ni paper compartido) sin pasar su
  propio ciclo paper → evidencia → escalar.
