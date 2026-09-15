# 53 — Tasas, liquidez y la Fed

## Por qué un banco central en Washington mueve tu gráfico de BTC

La **Reserva Federal (Fed)** es el banco central de EE.UU. Fija la **tasa de interés** de
referencia: el precio del dinero. Como el dólar es la moneda del mundo financiero, su tasa
afecta a todos los activos — cripto incluido.

La cadena lógica, en simple:

| Tasas | Efecto | Consecuencia para cripto |
|---|---|---|
| Altas | Un bono del gobierno paga bien sin riesgo | Menos apetito por activos riesgosos → presión bajista |
| Bajas | El efectivo "no rinde"; sobra dinero barato | El capital busca rendimiento en riesgo → viento a favor |

Cripto está en la punta más lejana de la curva de riesgo: es de lo **primero que se vende**
cuando el dinero se encarece y de lo que **más sube** cuando sobra liquidez.

## Liquidez global: la marea

**Liquidez** = cuánto dinero hay disponible en el sistema buscando dónde invertirse. Depende
de la Fed pero también de otros bancos centrales (Europa, Japón, China). La metáfora útil:
la liquidez es la marea; los activos son los barcos. Con marea alta casi todo flota (bull
market generalizado); con marea baja se ve quién nadaba desnudo.

Estado actual de tasas y ciclo de liquidez: **verificar al día** — cambia cada pocas semanas
y citarlo de memoria es la receta para operar con un mapa viejo.

## FOMC: volatilidad con fecha en el calendario

El **FOMC** es el comité de la Fed que decide las tasas. Se reúne ~8 veces al año en fechas
públicas. Alrededor del anuncio (y de la rueda de prensa que le sigue) pasa algo muy útil de
saber: **volatilidad programada**.

- Minutos antes y después del anuncio: mechas violentas en ambas direcciones, spreads que se
  abren, movimientos que se revierten en minutos.
- No es "manipulación": es el mercado entero reajustando precios ante información nueva.
- Otros eventos del mismo tipo: dato de inflación de EE.UU. (CPI) y de empleo (NFP).

Regla de prudencia clásica: **no abrir posiciones nuevas justo antes de un FOMC/CPI**. No
porque se sepa la dirección (nadie la sabe), sino porque el ruido barre stops sin piedad.

## Cómo aplica al AGENTE TRADING

- El régimen `risk-on`/`risk-off` de Haiku captura indirectamente este macro: tras un FOMC
  duro, el mercado suele virar a `risk-off` y el bot baja convicción — el diseño ya defiende.
- Lo que el bot NO tiene hoy: conciencia del calendario. Analiza cada 2h sin saber si en 30
  minutos hay FOMC. Mejora concreta para Fase 8: **pausar entradas nuevas ±2h alrededor de
  FOMC/CPI** (las fechas son públicas y se pueden cargar por adelantado).
- Los stops por volatilidad (ATR) ayudan, pero en un anuncio la mecha puede superar cualquier
  stop razonable — evitar el evento es más barato que sobrevivirlo.
