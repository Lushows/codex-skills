# 20 — Position sizing avanzado

**Position sizing** = decidir cuánto dinero poner en cada trade. Es la palanca que más
determina si una cuenta sobrevive. La entrada perfecta con el tamaño equivocado quiebra;
la entrada mediocre con el tamaño correcto sobrevive y aprende.

## La base: riesgo constante, tamaño variable

La regla madre (módulo 02) fija el **riesgo en USD** y deja que el **notional** (el valor
total de la posición) se acomode:

```
riesgo_usd = capital × riesgo%          → constante ($15 con $1.000 y 1.5%)
notional   = riesgo_usd / distancia_al_stop%   → variable
```

Todo lo "avanzado" de este módulo son formas de decidir esa distancia al stop o de modular
el riesgo% — nunca de romper el techo.

## Sizing por volatilidad

**Volatilidad** = cuánto se mueve el precio en promedio (se mide con ATR u otra métrica;
ver módulo 22). La idea: si el mercado está agitado, el stop debe ir más lejos → la posición
sale más chica automáticamente. Si está calmado, stop más cerca → posición más grande.

| Mercado | Stop (ej.) | Notional con riesgo $15 |
|---|---|---|
| Calmado | 1.0% | $1.500 |
| Normal | 2.0% | $750 |
| Agitado | 4.0% | $375 |

El riesgo en USD es idéntico en los tres casos. Eso es sizing por volatilidad: **la posición
respira con el mercado** sin que el riesgo cambie. Es exactamente lo que hace el bot con su
stop de 1.5× volatilidad.

## Sizing por convicción

Modular el riesgo% según qué tan buena luce la señal (ej. convicción 1-10). Válido SOLO si:
1. La convicción sale de criterios definidos de antemano (no de "me late").
2. Modula **hacia abajo** desde el techo, nunca por encima (convicción 10 = 1.5%, no 3%).

Sin esas dos condiciones, "convicción" es la puerta de entrada del revenge trading disfrazado.

## Fixed fractional vs fixed ratio

- **Fixed fractional** (fracción fija): riesgo = X% del capital ACTUAL. Si el capital baja,
  el riesgo en USD baja solo → freno automático en rachas malas. Es lo que usa el bot.
- **Fixed ratio** (razón fija): el tamaño sube por escalones cada vez que se acumula cierta
  ganancia ("delta"). Diseñado para futuros con contratos enteros; agresivo al inicio.

Para spot cripto con capital chico, fixed fractional gana: simple, anti-ruina, y el freno
en drawdown viene gratis. Fixed ratio solo tiene sentido con historial largo y capital mayor.

## Errores comunes de sizing

1. **Tamaño fijo en USD** ("siempre meto $500"): el riesgo real varía con cada stop — trades
   incomparables y riesgo invisible.
2. **Subir tamaño para recuperar pérdidas** (martingala): la matemática de la ruina en acción.
3. **Ignorar posiciones abiertas**: 2 posiciones de 1.5% en activos correlacionados ≈ una sola
   apuesta de 3% (módulo 25).
4. **Redondear hacia arriba** "porque casi no cambia": los casi-nada se acumulan.
5. **Calcular mentalmente**: los cálculos de sizing se rutean a `Matematicas_lushows` — dinero
   nunca a ojo.

## Cómo aplica al AGENTE TRADING

El bot ya combina las tres capas sanas: fixed fractional (1.5% del capital actual, cap duro),
sizing por volatilidad (stop = 1.5× volatilidad, mín 1%) y convicción como modulador DENTRO
del techo (Kelly fraccional, módulo 21). Con $1.000 eso significa máx $15 de riesgo por trade.
Antes del go-live (22-ago-2026): verificar en código que el notional se recalcula con el
capital actualizado tras cada trade, no con los $1.000 iniciales.
