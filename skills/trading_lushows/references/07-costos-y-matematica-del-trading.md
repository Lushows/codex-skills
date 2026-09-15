# 07 — Costos y matemática del trading (números verificados en código, 6-jul-2026)

> Todos estos números fueron ejecutados y verificados con `Matematicas_lushows` (Node, doble vía).
> Si cambian comisiones o parámetros, recalcular — no reciclar.

## El peaje de cada trade (Binance spot)

- Comisión: 0.1% por lado (0.2% redondo)
- Slippage modelado: 0.05% por lado (0.1% redondo)
- **Total: ~0.30% del notional por trade completo**
- Breakeven exacto: el precio debe moverse **+0.3005%** a favor solo para empatar.

## Win rate mínimo real (R:R 1:2, incluyendo costos)

| Stop | Costo en unidades R | Win rate mínimo |
|---|---|---|
| 1.5% | 0.20 R | **40.0%** |
| 2.0% | 0.15 R | **38.3%** |
| 3.0% | 0.10 R | **36.7%** |

Sin costos el mínimo teórico sería 33.3% — los costos suben la vara 3-7 puntos. Stops muy ceñidos
son doblemente caros: los barre el ruido Y pagan más peaje relativo.

## Profit factor traducido a plata

```
PF = ganancia bruta / pérdida bruta
PF 1.3 con R:R 1:2 ⟺ win rate ≈ 39.4%
```

Con capital $1.000, riesgo 1.5% ($15/trade), 30 trades a PF 1.3:
**12 wins × $30 − 18 losses × $15 = +$90 neto (~9% en 2-3 meses)**.

Lectura honesta (de `economist_lushows`): con capital chico esto es un **laboratorio, no un
sueldo**. El activo valioso es el sistema validado; el capital se escala después de la evidencia.

## Capital mínimo (restricción técnica de Binance)

- minNotional spot ≈ $10 (algunos pares $5). Con riesgo 1.5% y stop 3%: capital mínimo técnico ~$20-50.
- Capital mínimo RAZONABLE para que los datos signifiquen algo y quepan 2 posiciones: **$200-500**.
- Regla de la quiebra: solo dinero cuya pérdida total no cambia tu vida.

## Matemática de la recuperación (por qué el drawdown manda)

| Pérdida | Ganancia necesaria para empatar |
|---|---|
| −10% | +11.1% |
| −25% | +33.3% |
| −50% | +100% |

La asimetría es la razón del techo de riesgo 1.5% y del criterio drawdown <15%.
