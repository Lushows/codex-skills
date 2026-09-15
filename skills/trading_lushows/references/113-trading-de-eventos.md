# 113 — Trading de eventos (halving, ETFs, listings, upgrades)

## Qué es un evento programado

Cripto tiene fechas conocidas de antemano que concentran atención y volatilidad:

| Evento | Qué es | Ejemplo histórico |
|---|---|---|
| **Halving** | Cada ~4 años se reduce a la mitad la emisión nueva de BTC | Halvings de 2016, 2020, 2024 |
| **Aprobación de ETF** | Un fondo regulado que permite a inversionistas tradicionales comprar exposición | ETFs spot de BTC (2024) |
| **Listing** | Un exchange grande lista un token nuevo | Cualquier "listado en Binance" |
| **Upgrade de red** | Cambio técnico mayor de una blockchain | The Merge de Ethereum (2022) |
| **Decisiones macro** | Tasas de interés (Fed), datos de inflación | Cada reunión del FOMC |

## "Compra el rumor, vende la noticia"

El patrón más repetido del trading de eventos: el precio sube **antes** del evento (todos
anticipan) y cae **cuando ocurre** (los anticipadores toman ganancia y ya no queda quién
compre). The Merge de ETH es el ejemplo de libro: meses de subida previa, caída tras el evento.

¿Por qué? Porque el mercado descuenta el futuro: cuando el evento llega, ya estaba en el
precio. La noticia buena confirmada no trae compradores nuevos — libera vendedores.

**Pero no es ley.** A veces la noticia supera lo esperado y el precio sigue (los ETFs de BTC
sorprendieron con flujos enormes). Ahí está la trampa: el patrón existe, pero apostarle en
cada evento es cara-o-sello con fees.

## Volatilidad programada

Lo único casi garantizado de un evento es la **volatilidad**: movimientos grandes en ambas
direcciones, mechas violentas, stops barridos en segundos, spreads que se abren. La dirección
es incierta; la turbulencia no.

## Cómo debe atravesarlos el bot: reducir exposición, no predecirlos

Regla de oro: **el bot no apuesta a eventos, los sobrevive.**

- **Antes de un evento mayor conocido** (halving, decisión de ETF, FOMC, upgrade grande):
  la jugada correcta es reducir exposición — no abrir posiciones nuevas horas antes, y
  considerar achicar o cerrar las abiertas. Perderse un movimiento es un costo; que una mecha
  barra el stop y luego el precio vaya a donde el análisis decía, es tilt garantizado.
- **Después del evento**: esperar a que el polvo se asiente (varias velas de 1h) y dejar que
  macroRegime reclasifique. El régimen post-evento puede ser opuesto al previo.
- **Nunca** subir la convicción "porque viene una noticia buena". Si la noticia es conocida,
  ya está en el precio; si no es conocida, el bot no la conoce tampoco.
- Los eventos van al análisis como **contexto de riesgo** (volatilidad esperada), jamás como
  señal direccional.

Predicción honesta: nadie sabe la dirección post-evento. Gestión honesta: nadie necesita
saberla si no está sobreexpuesto.
