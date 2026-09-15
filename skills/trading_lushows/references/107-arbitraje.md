# 107 — Arbitraje: el juego donde el retail llega tarde

**Arbitraje** = ganar de una diferencia de precio del MISMO activo en dos lugares o formas:
comprar donde está barato y vender donde está caro, al mismo tiempo. En teoría es ganancia sin
riesgo direccional (no apuestas a que suba o baje). En la práctica, es una carrera de
velocidad e infraestructura — y hay que saber contra quién se corre.

## Los 3 tipos clásicos en cripto

| Tipo | Cómo funciona | El truco escondido |
|---|---|---|
| **Entre exchanges** | BTC cotiza distinto en el exchange A y el B: comprar en A, vender en B | Mover fondos entre exchanges tarda minutos; el spread vive segundos. Necesitas capital YA depositado en ambos lados, y aun así compites por velocidad |
| **Triangular** | Dentro de un mismo exchange: BTC→ETH→USDT→BTC termina con más de lo que empezó | Las inconsistencias son minúsculas y duran milisegundos; las comisiones de 3 operaciones suelen comerse la diferencia |
| **De funding** | En futuros perpetuos, los LONGs y SHORTs se pagan entre sí una tasa periódica (*funding*). Estrategia: comprar spot + vender el futuro = neutral al precio, cobrando el funding | Es el más accesible, pero no es "sin riesgo": el funding cambia de signo, hay riesgo de liquidación en la pata corta y riesgo del exchange mismo |

**Spread** = la diferencia de precio que se intenta capturar. **Perpetuo** = futuro sin fecha
de vencimiento, el derivado más operado en cripto.

## Por qué el retail llega tarde (la parte honesta)

El arbitraje es un juego de suma casi-cero donde gana el más rápido. Los competidores son
firmas con:

- **Velocidad**: servidores en el mismo edificio que el exchange, código en lenguajes de baja
  latencia, acceso de mercado privilegiado. Ellos ven y ejecutan en milisegundos; una llamada
  API normal desde Colombia tarda cientos.
- **Capital pre-posicionado** en decenas de exchanges, para no mover fondos nunca.
- **Comisiones negociadas** de alto volumen: un spread que a ellos les deja margen, a la tarifa
  retail es pérdida.

Consecuencia: para cuando una oportunidad de arbitraje es visible a ojo humano (o a un bot
casero), ya fue tomada — o queda porque tiene un riesgo escondido (un exchange congelando
retiros, un activo con el mismo nombre que no es el mismo). **El arbitraje "fácil" que
sobrevive es la carnada; el difícil exige infraestructura de firma.** Las cifras de spreads y
fundings cambian a diario: cualquier número concreto, verificar al día.

El caso menos desigual es el funding (no exige velocidad extrema, sino gestión), pero exige
operar derivados con margen, monitoreo continuo de la pata corta y aceptar riesgo de
contraparte del exchange — otra disciplina completa, no un extra de fin de semana.

## Honestidad: no es nuestro juego

- Nuestro edge buscado es **direccional y paciente**: swing en 1h, análisis c/2h, convicción
  con IA. El arbitraje es **neutral y de milisegundos**: infraestructura, latencia, capital
  distribuido. No comparten casi nada — ni código, ni riesgos, ni métricas.
- Un ciclo de análisis cada 2 horas está, literalmente, millones de veces por fuera de la
  ventana de tiempo del arbitraje entre exchanges o triangular.
- El funding arbitrage exigiría SHORT en derivados, margen y vigilancia de liquidación — el
  bot es solo-LONG spot por diseño (ver `109` para lo que implicaría abrir esa puerta).
- Decisión de método, no de capacidad: aunque se pudiera construir, sería OTRO sistema
  compitiendo por otro premio contra otros jugadores. El AGENTE TRADING compite donde el
  retail sí puede tener ventaja: paciencia, disciplina y proceso — no velocidad.
