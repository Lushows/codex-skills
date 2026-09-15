# 112 — Rotación de narrativas y sectores

## Qué es

En cripto el capital no se mueve parejo: salta por olas entre "sectores" según la **narrativa**
de moda (la historia que la gente se cuenta sobre qué va a subir). Ejemplos históricos de
narrativas: DeFi, NFTs, layer-2s, IA, memecoins, tokenización de activos reales (RWA).

El patrón clásico de rotación (simplificado):

```
BTC sube → ganancias rotan a ETH → rotan a large caps → rotan a mid/low caps → euforia → todo cae
```

Cuando el dinero llega a lo más especulativo, suele ser señal de ciclo maduro, no de comienzo.

## Por qué es un juego de timing dificilísimo

- **Llegar temprano = estar solo.** Si compras la narrativa antes de que arranque, puedes
  esperar meses sangrando mientras otra cosa sube.
- **Llegar tarde = ser la salida de otros.** Cuando la narrativa ya está en titulares e
  influencers, los que entraron temprano te están vendiendo a ti (exit liquidity, ver `125`).
- **Las narrativas no avisan cuándo mueren.** No hay stop natural: la historia "sigue siendo
  buena" mientras el precio cae 70%.
- **Sobreviven pocas.** De cada ola de tokens de una narrativa, la mayoría nunca recupera
  su máximo. Apostar a la narrativa correcta Y al token correcto Y al momento correcto son
  tres aciertos encadenados.

Quien gana consistentemente con rotación es gente que vive pegada al mercado con información
y velocidad que el retail no tiene. Anti-humo: los hilos de "la próxima narrativa 100x" son
marketing, no análisis.

## Señales de rotación (para leer contexto, no para perseguir)

| Señal | Qué sugiere |
|---|---|
| **Dominancia de BTC** subiendo | Capital refugiándose en BTC; mal clima para alts |
| Dominancia de BTC cayendo con mercado subiendo | Rotación hacia alts ("alt season" posible) |
| ETH/BTC subiendo | Apetito de riesgo dentro de cripto creciendo |
| Volumen migrando a mid/low caps | Ciclo especulativo maduro — precaución |

(Todos son datos públicos; verificar al día, nunca de memoria.)

## Cómo aplica al AGENTE TRADING

- El bot **no rota narrativas**: opera BTC y ETH, los dos activos que sobreviven a todas
  las narrativas. Eso es una decisión de diseño, no una limitación.
- Utilidad real: las señales de rotación sirven como **contexto de régimen**. Dominancia de
  BTC subiendo fuerte suele coincidir con debilidad de ETH — dato relevante para un bot cuyos
  10 trades han sido todos en ETH.
- Si algún día se agrega un tercer par (SOL, ver `126`), será por criterios de liquidez y
  datos — no porque su narrativa esté de moda esa semana.
