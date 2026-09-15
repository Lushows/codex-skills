# 136 — Liquidaciones: por qué existen las velas violentas

> Si alguna vez viste BTC caer 5% en 15 minutos "sin noticia", casi seguro fue una cascada de
> liquidaciones. Entenderlas no te hace predecirlas, pero te deja diseñar defensas.

## Qué es una liquidación

Cuando alguien opera con apalancamiento (dinero prestado) y el precio va en su contra más allá de
cierto punto, el exchange **cierra su posición a la fuerza** para cobrarse. Esa venta (o compra)
forzada es una orden de mercado que empuja el precio aún más en la misma dirección.

## La cascada

```
Precio cae un poco → liquidan a los longs más apalancados (venta forzada)
→ esa venta baja más el precio → liquidan al siguiente nivel de longs
→ más venta forzada → ... → vela roja gigante en minutos
```

Lo mismo al revés con shorts = subida violenta. Por eso el mercado cripto "exagera" los
movimientos: hay mucho apalancamiento minorista concentrado en niveles predecibles.

## Mapas de liquidez / liquidaciones

Herramientas que estiman en qué precios se acumulan las liquidaciones pendientes (porque la gente
pone apalancamiento similar en niveles similares). Dos verdades incómodas:

1. Son **estimaciones**, no datos reales — nadie ve las posiciones de todos.
2. Esos clusters actúan como **imanes**: al mercado le "conviene" visitar zonas con mucha
   liquidez. Es una explicación plausible de por qué el precio barre un nivel y rebota; no es
   una bola de cristal.

## La defensa (esto es lo importante)

No puedes predecir la cascada. Puedes diseñar para sobrevivirla:

| Defensa | Cómo funciona |
|---|---|
| **Sin apalancamiento** | No puedes ser liquidado. Punto. |
| **Sizing por volatilidad** | Posiciones más chicas cuando el mercado está más loco |
| **Stops con aire** | Stops muy ceñidos son barridos por mechas de cascada que luego revierten |
| **Pocas posiciones** | Una cascada golpea todo a la vez; menos posiciones = menos daño simultáneo |

## Cómo aplica al AGENTE TRADING

- El bot no usa apalancamiento: **no puede ser liquidado**. Su riesgo con las cascadas es que las
  mechas violentas ejecuten sus stops en el peor precio.
- Las defensas ya existen: riesgo máx 1.5% por trade, máximo 2 posiciones, y stops calculados
  por `positionSizing` — la mejora pendiente es ligar la distancia del stop a la volatilidad
  reciente (ej: ATR) para darles aire en mercados locos.
- En el backtest con nuestras velas 1h: las velas de cascada aparecen como rangos enormes en una
  vela. Asumir que el stop se ejecuta **al precio del stop** en esas velas es mentirse — modelar
  slippage extra en velas de rango extremo (ver módulo 140).
