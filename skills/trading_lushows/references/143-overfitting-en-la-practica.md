# 143 — Overfitting en la práctica (complementa el módulo 47)

> **Overfitting**: ajustar una estrategia tan bien al pasado que memoriza su ruido en vez de
> aprender su patrón. El resultado: backtest glorioso, vivo desastroso. El módulo 47 da la
> teoría; este da los síntomas concretos y las reglas de taller.

## Síntomas concretos (si ves esto, es overfitting hasta que se demuestre lo contrario)

| Síntoma | Ejemplo |
|---|---|
| **Parámetros mágicos** | "RSI 27.5 gana; RSI 27 y 28 pierden" — un edge real no vive en un decimal |
| **PF altísimo in-sample** | PF 3, 4, 5+ en el período de ajuste. Los sistemas reales sostenibles viven mucho más abajo |
| **Muchas condiciones apiladas** | "Comprar si RSI<30 Y MACD cruza Y es martes Y volumen>X" — cada filtro añadido recorta trades y memoriza casos |
| **Curva de equity perfecta** | Sin drawdowns visibles = se optimizó hasta borrar las pérdidas del pasado (solo del pasado) |
| **Muere fuera de la muestra** | Brillante en 2024, mediocre en 2025 → aprendió 2024, no el mercado |

**In-sample**: los datos usados para diseñar/ajustar. **Out-of-sample**: datos que la estrategia
nunca vio. Solo el segundo dice la verdad.

## Las reglas de taller

1. **Pocos parámetros.** Cada parámetro ajustable es un grado de libertad para memorizar ruido.
   Objetivo: que la estrategia quepa en 3-5 números. Si necesita 10, es un disfraz del pasado.
2. **Mesetas, no picos.** Un parámetro robusto funciona en un rango (RSI 25-35 todos rentables,
   con matices). Si solo funciona un valor exacto, es un pico de ruido: descartarlo.
3. **Out-of-sample obligatorio.** Separar los datos ANTES de empezar: diseñar con una parte,
   validar con la otra, y la parte de validación se toca **una sola vez**. Si iteras contra el
   out-of-sample, lo convertiste en in-sample.
4. **Contar los intentos.** Si probaste 50 variantes y una dio PF 2, esperabas encontrarla por
   puro azar. Más intentos = más exigencia al ganador (y walk-forward, módulo 144).
5. **Preferir la explicación económica.** "Compra debilidad en tendencia alcista porque hay
   compradores estructurales" sobrevive; "el cruce de la SMA 47 con la 183" no tiene por qué.

## Cómo aplica al AGENTE TRADING

- Ventaja estructural nuestra: el sistema tiene **pocos parámetros duros** (riesgo 1.5%, umbral de
  convicción 8, cooldowns) y una capa de juicio (Claude) que no se "optimiza" por barrido. Mantener
  esa sobriedad: la tentación tras el backtest será añadir filtros — resistirla.
- Al backtestear con las velas de `candlesStore`: separar out-of-sample desde el día uno (ej: el
  último tramo de la historia queda sellado) y probar **mesetas** de parámetros, no valores únicos.
- El PF actual (0.89 con 10 trades) ni valida ni condena nada — pero cualquier "arreglo" que
  suba el PF pasado retocando reglas contra esos 10 trades sería overfitting de bolsillo: 10
  trades es anécdota, no muestra.
