# 52 — Correlación con mercados tradicionales

## Qué es correlación (en simple)

**Correlación** = qué tanto se mueven dos cosas juntas. Va de +1 (siempre juntas), pasando
por 0 (independientes), hasta −1 (siempre opuestas). Ejemplo: si cuando el Nasdaq cae 2%
Bitcoin suele caer también, están correlacionados positivamente.

Dato clave: la correlación **no es fija** — cambia con los meses. Cualquier cifra concreta
("BTC tiene correlación 0.8 con el Nasdaq") hay que **verificarla al día**.

## Los tres compañeros de baile de cripto

| Mercado | Qué es | Relación típica con cripto |
|---|---|---|
| Nasdaq / S&P 500 | Acciones de EE.UU. (Nasdaq = las tecnológicas) | Positiva en épocas de estrés: cripto se comporta como "tecnología con esteroides" |
| DXY (índice dólar) | Fuerza del dólar contra otras monedas | Tiende a ser inversa: dólar fuerte = presión bajista en cripto |
| Oro | El refugio clásico | Ambigua; la tesis "BTC = oro digital" funciona solo a ratos |

## Cuándo se acopla y cuándo se desacopla

- **Se acopla (correlación alta) en pánico y en macro-eventos**: cuando la Fed asusta o hay
  crisis, todo lo riesgoso cae junto — cripto incluido, y con más violencia. En risk-off no
  hay diversificación: las correlaciones "van a 1".
- **Se desacopla en eventos propios de cripto**: un ETF aprobado, un hackeo de exchange, un
  halving — ahí cripto se mueve solo, con las bolsas quietas.
- **Horarios distintos**: las bolsas abren y cierran; cripto opera 24/7. Los fines de semana
  cripto queda "sin ancla" (ver `64`), y los lunes a veces corrige hacia donde fue el Nasdaq.

## Por qué esto importa (y su límite)

Mirar el Nasdaq y el DXY da contexto: si las bolsas están en caída libre, un setup alcista
en BTC nada contra la corriente. Pero cuidado con el humo: la correlación **no predice**,
describe. Saber que "se mueven juntos" no dice cuál se mueve primero ni cuándo.

## Cómo aplica al AGENTE TRADING

- El régimen `risk-on` / `risk-off` que clasifica Haiku (ver `03`) es precisamente la lectura
  de este acoplamiento: en `risk-off` la convicción se limita a ≤4 porque cripto rara vez
  sube solo contra un mercado global asustado.
- El bot solo-LONG se beneficia del acople en una dirección: cuando las bolsas acompañan
  (`risk-on` + `trending-up`), el viento de cola es real.
- Mejora futura razonable: alimentar al clasificador con datos simples de DXY/S&P además de
  las velas de BTC. Mejora NO razonable: intentar "arbitrar" la correlación — eso es liga de
  fondos cuantitativos, no de un bot swing.
