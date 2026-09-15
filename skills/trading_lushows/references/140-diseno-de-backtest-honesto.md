# 140 — Diseño de un backtest honesto

> **Backtest**: simular una estrategia sobre datos históricos para ver cómo le habría ido.
> El 90% de los backtests que se ven en internet son mentira — no por mala fe, sino por errores
> de diseño. Este módulo es la receta para no mentirnos a nosotros mismos.

## Los 5 mandamientos

### 1. Reglas exactas, escritas ANTES de mirar los datos
La estrategia debe estar definida al 100% antes de correr nada: qué dispara la entrada, dónde va
el stop, dónde el target, cuánto se arriesga. Si mientras miras resultados "ajustas un poquito",
ya no estás backtesteando: estás ajustando la curva al pasado (overfitting, módulo 143).

### 2. Hipótesis primero
Escribir: "creo que X funciona porque Y, y espero ver Z". El backtest **confirma o refuta** una
hipótesis; no es una excavadora para encontrar lo que sea que haya funcionado.

### 3. Costos y slippage SIEMPRE incluidos
Comisión por lado + slippage por lado en cada trade simulado. Un backtest sin costos infla
sistemáticamente los resultados — y las estrategias de muchos trades son las más infladas.
Extra de honestidad: en velas de rango extremo (cascadas, módulo 136), asumir slippage mayor.

### 4. Datos suficientes y limpios
- Pasar el checklist del módulo 139 antes de nada.
- Cubrir **más de un régimen**: un backtest solo en mercado alcista "valida" cualquier cosa que
  compre. Idealmente incluir tendencia, rango y caída.
- Regla práctica: mínimo decenas de trades simulados; con menos de ~30, la estadística es humo.

### 5. Sin información del futuro
Cada decisión simulada solo puede usar datos disponibles **hasta ese momento** (módulo 142).
El clásico: decidir con el cierre de la vela en curso, que en la vida real aún no existía.

## Qué reportar (no solo "ganó X%")

| Métrica | Por qué |
|---|---|
| PF, win rate, trades totales | El edge y si la muestra alcanza |
| Max drawdown | El peor trago — decide si es vivible |
| Resultado por régimen/sub-período | Dónde gana y dónde pierde (módulo 146) |
| Sensibilidad a costos | ¿Sobrevive con costos ×1.5? |

## Cómo aplica al AGENTE TRADING

- El plan del backlog: backtestear con las **velas 1h guardadas en `candlesStore`** (dataset
  propio, ya validado al persistir).
- Reto particular nuestro: la señal viva la genera **Claude**, que no es determinista ni barato de
  re-ejecutar sobre miles de velas. Camino sensato: backtestear primero las **partes mecánicas**
  (reglas técnicas de technicalAnalysis, stops/targets de positionSizing, filtro de régimen) y
  tratar la capa de Claude aparte (validada con paper + A/B, módulos 147-148).
- Costos a usar en el simulador: los mismos que ya modela el broker paper — 0.1% comisión +
  0.05% slippage por lado (~0.30% redondo, módulo 07).
- Hipótesis antes de correr. Escribirla en el repo. Sin excepciones.
