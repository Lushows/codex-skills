# 121 — ETH a fondo (como activo de trading)

## Qué es ETH para un trader

Ethereum es el segundo activo de cripto por tamaño y liquidez, pero no es "un BTC más
chico": es un activo con **motores propios**. BTC es oro digital pasivo; ETH es la
plataforma donde corre casi todo lo demás (DeFi, NFTs, stablecoins, tokenización), y su
precio refleja tanto el clima cripto general como la salud de ese ecosistema.

## La propiedad clave: beta más alta que BTC

**Beta** = cuánto se mueve un activo cuando se mueve su referencia. Si BTC sube 2% y ETH
suele subir 3% ese mismo día, ETH tiene beta ~1.5 contra BTC. El número exacto cambia por
época (verificar al día), pero la regla histórica es estable:

```
ETH tiende a moverse MÁS que BTC — en las dos direcciones.
Sube más en los rallies, cae más en los sustos.
```

No es magia ni mérito: es un activo algo menos líquido y más sensible al apetito de riesgo.
La beta alta no es "mejor" ni "peor" — es más octanaje: más oportunidad y más golpe por
unidad de exposición.

## Catalizadores propios (los que BTC no tiene)

| Catalizador | Ejemplo |
|---|---|
| **Upgrades de la red** | The Merge (2022, cambio a proof-of-stake), reducciones de costos de layer-2 |
| **Actividad DeFi** | Más uso → más fees quemados → presión sobre la oferta del token |
| **Staking** | ETH bloqueado generando rendimiento: afecta oferta circulante |
| **ETFs y regulación propia** | Sus aprobaciones y dramas regulatorios, separados de los de BTC |
| **El par ETH/BTC** | Su fuerza relativa contra BTC: termómetro de apetito de riesgo interno del mercado (ver `112`) |

Consecuencia práctica: ETH puede tener tendencia propia mientras BTC lateraliza — un
calendario de eventos propio que vigilar (ver `113`) y una razón para analizarlo como
activo, no como sombra de BTC.

## Por qué los 10 trades del bot fueron todos en ETH

No es sesgo del bot ni casualidad pura: es la beta trabajando. Más volatilidad significa
que ETH cruza los umbrales técnicos (rupturas, pullbacks, momentum) **más veces por mes**
que BTC en el mismo período. Más setups → más veces que el análisis llega a convicción ≥8.

Lectura honesta de ese dato:
- **Esperable**: el par de mayor octanaje genera más señales en un sistema de momentum.
- **Vigilable**: 10/10 en un solo activo significa que toda la memoria del bot (traderMemory)
  es memoria de ETH. Las lecciones aprendidas podrían no transferirse limpias a BTC o a un
  tercer par — el meta-análisis debe marcar esa concentración, no celebrarla.

## Cómo aplica al AGENTE TRADING

- ETH es, en la práctica, **el activo principal del bot** hoy. Su beta alta encaja con un
  sistema exigente (convicción ≥8): el filtro es duro, ETH es el que más veces lo pasa.
- La beta corta ambos lados: el riesgo por trade (1.5%) ya lo contiene vía sizing, pero las
  mechas de ETH castigan stops apretados más que en BTC — dato para el análisis de stops.
- Todo trade de ETH exige mirar BTC primero (ver `120`): LONG de ETH contra BTC débil es
  la versión cripto de remar contra corriente.
