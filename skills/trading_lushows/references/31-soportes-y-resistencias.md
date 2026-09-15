# 31 — Soportes y resistencias

Un **soporte** es una zona de precio donde históricamente aparecieron compradores y frenaron la
caída. Una **resistencia** es lo contrario: zona donde aparecieron vendedores y frenaron la subida.
Son la "memoria del mercado": niveles donde ya hubo batalla y probablemente la vuelva a haber.

## Por qué se forman

- **Memoria de los participantes**: quien compró en $X y vio subir el precio quiere recomprar ahí.
  Quien quedó atrapado comprando en un techo quiere vender "en tablas" cuando el precio regresa.
- **Órdenes acumuladas**: en niveles redondos y en máximos/mínimos previos se acumulan órdenes de
  compra/venta y stops, lo que crea reacción cuando el precio llega.
- **Cambio de rol**: un soporte roto tiende a actuar como resistencia después (y viceversa),
  porque los atrapados de un lado pasan a ser los vendedores/compradores del otro.

## Cómo trazarlos (sin humo)

1. Alejar el gráfico y marcar los puntos donde el precio **giró varias veces** (mínimo 2 toques;
   3+ es un nivel fuerte).
2. Priorizar los niveles **recientes y visibles**: un máximo de la semana pasada pesa más que uno
   de hace un año.
3. No buscar precisión de centavos: el mercado no respeta líneas exactas.

## Zonas, no líneas

| Enfoque | Problema / ventaja |
|---|---|
| Línea exacta ($67.250,00) | Falsa precisión: el precio la "perfora" 0.3% y parece que falló |
| **Zona** ($67.000–$67.500) | Realista: la batalla ocurre en un área, no en un número |

Regla práctica: el ancho razonable de la zona es del orden de la volatilidad reciente del activo.

## Uso para stops y targets (lo que más importa)

- **Stop de un LONG**: DEBAJO del soporte (no encima, no en el número redondo exacto donde están
  los stops de todos). Si el soporte se pierde de verdad, la tesis murió y hay que salir.
- **Target de un LONG**: DEBAJO de la resistencia siguiente, no en ella. Pedir que el precio
  atraviese la resistencia para cobrar es regalar la ganancia al último tramo, el más difícil.
- La distancia entre entrada, soporte y resistencia define el **R:R real** del trade: si la
  resistencia está más cerca que 2× el riesgo, el setup no cumple el 1:2 y no se toma.

## Cómo aplica al AGENTE TRADING

- El bot ya calcula soportes/resistencias en `technicalAnalysis.js` y los usa como referencia de
  niveles; el stop del sistema (1.5× volatilidad) debería en lo posible quedar del lado correcto
  del soporte más cercano — si el soporte queda DENTRO del stop, mejor.
- Mejora barata: que el prompt de convicción verifique "¿cuánto espacio hay hasta la resistencia?"
  antes de un LONG. Comprar pegado a una resistencia es otra forma del FOMO de `10`.
- Tratarlos como zonas evita que Claude lea "rompió el soporte" por una mecha de 0.2%.
