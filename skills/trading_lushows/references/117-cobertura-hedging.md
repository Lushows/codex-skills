# 117 — Cobertura (hedging)

## Qué es cubrir

**Cubrir** (hedge) = abrir una posición que gana cuando tu posición principal pierde, para
reducir el daño de un movimiento en contra **sin cerrar** la posición principal. Es un seguro
temporal, no una estrategia de ganancia.

Ejemplo simple: tienes 1 ETH en spot y viene un evento de alto riesgo. En vez de vender,
abres un short de 1 ETH en perpetuos. Si ETH cae 10%, el spot pierde ~10% y el short gana
~10%: quedaste plano (delta neutral) durante la tormenta.

## Formas de cubrir una posición spot

| Instrumento | Cómo | Costo principal |
|---|---|---|
| **Short en perpetuo** | Vender perp por el monto a cubrir | Funding (si es negativo, pagas tú) + margen |
| **Short en futuro con vencimiento** | Vender el futuro | La base (ver `115`) + margen |
| **Comprar un put** | Seguro puro: pagas prima, pérdida limitada abajo | La prima (cara si hay miedo, ver `116`) |
| **Cobertura parcial** | Cubrir solo 30-50% de la posición | Proporcional — reduce, no elimina |

## Cubrir vs cerrar: la pregunta honesta

Una cobertura al 100% deja la posición **económicamente igual que cerrada**, pero pagando
fees de dos posiciones, funding y riesgo de margen. Entonces, ¿por qué no simplemente cerrar?

Razones legítimas para cubrir en vez de cerrar:
- **Impuestos**: cerrar realiza la ganancia fiscal; cubrir puede no hacerlo (depende del
  país — en Colombia, verificar con contador, no asumir).
- **Iliquidez de la posición**: no aplica a BTC/ETH spot, que se venden en segundos.
- **Cobertura de cartera grande** que no quieres deshacer y rearmar.
- **Cobertura parcial**: quieres seguir expuesto pero con menos riesgo — bajar de 100 a 50.

Para un trader de swing con posiciones líquidas y chicas, la respuesta casi siempre es:
**cerrar es la cobertura más barata y simple que existe.** La cobertura sofisticada suele
ser complejidad disfrazada de prudencia.

## Los costos que la cobertura esconde

- Fees dobles (abrir y cerrar la pata de cobertura).
- Funding del short si el mercado sigue eufórico.
- **Riesgo de margen**: si el precio sube fuerte, el short cubre… y su margen sangra; mal
  gestionado, te liquidan la cobertura en el peor momento.
- **Riesgo de descoordinación**: quitar la cobertura tarde o temprano es OTRA decisión de
  timing — ahora tienes dos posiciones que administrar en vez de una.

## Cómo aplica al AGENTE TRADING

- El bot **no cubre: cierra o reduce**. Con posiciones spot líquidas de riesgo 1.5%, el stop
  y la salida son la cobertura correcta — simple, barata y ya probada en sus 10 trades.
- Ante eventos de volatilidad programada (ver `113`), la política es reducir exposición,
  no montar coberturas con derivados que el sistema no opera.
- Escenario futuro donde se reevaluaría: capital real grande + posición ganadora de largo
  plazo + evento binario conocido. Ahí, un put comprado (pérdida máxima = prima) sería el
  único hedge candidato — jamás shorts apalancados que agreguen riesgo de liquidación.
