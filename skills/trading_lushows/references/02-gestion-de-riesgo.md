# 02 — Gestión de riesgo

La gestión de riesgo no es un accesorio del sistema: ES el sistema. El edge decide si ganas;
el riesgo decide si sobrevives para cobrarlo.

## Riesgo por trade (la regla madre)

```
riesgo_usd = capital × riesgo% (1.5% en AGENTE TRADING)
notional  = riesgo_usd / distancia_al_stop%
```

Ejemplo con $1.000 y stop a 2%: riesgo $15 → notional $750. El notional varía con el stop;
**el riesgo en USD es constante**. Eso hace comparables todos los trades (unidades de "R").

## Por qué 1.5% y no más

- 10 pérdidas seguidas con 1.5% = −14% del capital → se sobrevive y se sigue operando.
- 10 pérdidas seguidas con 10% = −65% → para recuperar hay que ganar +186%. Matemática de la ruina.
- La recuperación es asimétrica: −50% exige +100% solo para empatar. Verificable en `Matematicas_lushows`.

## Kelly fraccional (lo que usa positionSizing.js)

Kelly puro dice cuánto apostar para maximizar crecimiento, pero asume que conoces tus
probabilidades exactas (nadie las conoce). Por eso se usa **fracción de Kelly** con techo duro:
nunca más del 1.5% de riesgo, escale lo que escale la convicción. La convicción (1-10) modula
DENTRO del techo, jamás lo rompe.

## Drawdown: el número que mata cuentas

- **Drawdown** = caída desde el pico de equity. Se mide en % del pico.
- Umbral del proyecto: **máx 15%** (criterio go-live). En paper vamos en ~1.8% — muy sano.
- Regla de comportamiento: tras drawdown >8%, REDUCIR tamaño a la mitad hasta recuperar el pico.
  Nunca "recuperar" subiendo el riesgo — así se muere.

## Reglas anti-ruina del sistema (vigentes en código)

1. Máx 2 posiciones simultáneas (evita concentración temporal).
2. Máx 5 trades/día (evita overtrading, tradingPsychology bloquea).
3. Cooldown 4h tras 3 pérdidas seguidas (evita revenge trading).
4. Riesgo total expuesto ≤ 6% (spec; verificar en código antes de live).

## Para la fase live (añadir a las reglas)

- **Límite de pérdida diaria** (ej. 3% → kill switch automático, apagarse solo).
- **Stops en el exchange (OCO)**, no solo en el watcher local — si el servidor cae, el stop vive.
- **API keys sin permiso de retiro** + whitelist de IP.
- Empezar con capital que no duela ($200–500) — regla de la quiebra de `economist_lushows`.
