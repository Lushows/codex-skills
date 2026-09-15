# 123 — Altcoins de riesgo (mid y low caps)

## Qué son

**Mid caps** y **low caps** son criptomonedas de capitalización media y baja: todo lo que está por
debajo de las 10-15 primeras del ranking. Miles de tokens. Aquí es donde viven las historias de
"hice 10x en un mes" — y las de "perdí el 95% y nadie me lo contó".

## Los tres problemas estructurales

### 1. Manipulación

Con poca capitalización, un solo actor grande (una **ballena**) puede mover el precio a voluntad:

- **Pump & dump**: inflan el precio coordinadamente, venden arriba, el precio colapsa. El que
  compró "porque estaba subiendo" es el que paga la fiesta.
- **Wash trading**: el mismo actor se compra y se vende a sí mismo para fingir volumen. El
  "volumen alto" de muchas low caps es teatro (módulo 127).
- **Spoofing**: órdenes grandes falsas en el libro para asustar o atraer, que se cancelan antes
  de ejecutarse.

Un bot técnico lee velas. Si las velas están fabricadas, el bot analiza una mentira.

### 2. Iliquidez

En una low cap, salir de una posición mediana puede mover el precio en tu contra varios puntos
porcentuales. El stop loss deja de ser una protección confiable: la orden se ejecuta, pero a un
precio mucho peor del que pediste (**slippage** severo). En una caída fuerte puede no haber
compradores a ningún precio razonable.

### 3. −90% es un resultado normal, no una anomalía

En cada ciclo bajista de cripto, la mayoría de las altcoins pequeñas pierden 80-95% desde máximos
y muchas nunca se recuperan (el patrón se repite ciclo tras ciclo; los casos concretos, verificar
al día). En BTC/ETH un −80% ha sido históricamente el fondo del ciclo; en una low cap puede ser
apenas la mitad de la caída, o el final del proyecto.

## "Pero el retorno potencial es enorme"

Cierto, y es exactamente el argumento de la lotería (módulo 125 desarrolla la matemática). Un
sistema sistemático de swing no vive de encontrar el billete ganador: vive de una ventaja
estadística pequeña repetida muchas veces sobre activos donde el análisis técnico significa algo.
La manipulación y la iliquidez destruyen las dos cosas que el sistema necesita: velas honestas y
salidas ejecutables.

## Cómo aplica al AGENTE TRADING

- El bot NO opera mid/low caps. No es una limitación temporal a superar: es una decisión de
  diseño alineada con el pilar 1 (supervivencia, módulo 00).
- El universo del bot es BTC, ETH y, si pasa el checklist del módulo 126, una tercera large cap
  (SOL candidato). Nada por debajo de ese piso de liquidez.
- Si alguna vez se considera bajar de escalón, la carga de la prueba es del activo nuevo:
  backtest propio, costos reales medidos, y respuesta honesta a "¿qué gana el sistema aquí que
  no gana en ETH?". Casi siempre la respuesta es: nada, con más riesgo.
