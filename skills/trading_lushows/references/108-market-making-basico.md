# 108 — Market making básico: el spread como negocio

El **market maker** ("creador de mercado") no apuesta a que el precio suba o baje: pone a la
vez una orden de compra un poco por debajo del precio y una de venta un poco por arriba, y gana
la diferencia — el **spread** — cada vez que alguien le compra y alguien le vende. Es el
negocio de la tienda de barrio: comprar al por mayor, vender al detal, ganar el margen muchas
veces al día. Los exchanges los necesitan (dan la **liquidez** con la que todos operamos) y
suelen premiarlos con comisiones menores o incluso *rebates* (comisión negativa).

## Por qué parece un gran negocio

- Gana el spread decenas o cientos de veces al día, sin predecir nada.
- Mientras el mercado está tranquilo, es un goteo constante de ganancias chicas.
- Las comisiones juegan a favor (órdenes *maker*, las que esperan en el libro, pagan menos).

## El riesgo que no se ve en el folleto: el inventario

Cada vez que te compran, quedas con menos activo; cada vez que te venden, con más. Esa
acumulación es el **riesgo de inventario**, y es donde el negocio se rompe:

| Situación | Qué le pasa al market maker |
|---|---|
| Mercado lateral, flujo parejo | Compra y vende balanceado: cobra el spread feliz |
| El precio empieza a CAER | Todos le venden, nadie le compra: acumula inventario que vale cada vez menos |
| Noticia / movimiento brusco | Los informados le compran/venden ANTES de que ajuste sus precios: pierde contra cada uno |

Lo segundo tiene nombre: **selección adversa** — el flujo que llega en los momentos violentos
es justo el flujo que sabe algo que tú no. El market maker gana centavos con el flujo
desinformado y pierde pesos contra el informado; el negocio solo cierra si ajusta sus
cotizaciones más rápido de lo que el mercado se mueve. Estructuralmente es primo del grid
(ver `105`): muchas ganancias chicas, y el riesgo concentrado en el movimiento brusco.

## La infraestructura que exige (y que no tenemos)

- **Velocidad real**: recotizar en milisegundos ante cada cambio del libro de órdenes.
  Quien cotiza lento es el almuerzo de quien cotiza rápido. Un ciclo cada 2h ni siquiera es
  el mismo deporte.
- **Presencia continua**: 24/7 en el libro. Cada desconexión (ver `87`) es quedar con
  inventario huérfano en pleno movimiento.
- **Gestión de inventario automatizada**: sesgar precios para descargar lo acumulado, coberturas
  en derivados, límites duros de exposición.
- **Volumen y comisiones de mayorista**: el spread neto de comisiones retail suele ser
  demasiado fino para vivir de él.
- Capital dedicado a "estar en el libro" en vez de a posiciones con tesis.

Es una empresa de tecnología financiera operando 24/7, no una estrategia que se agrega a un bot.

## Honestidad: no es nuestro juego

- El AGENTE TRADING toma liquidez con tesis direccional y riesgo definido (1.5%, R:R 1:2); el
  market maker provee liquidez sin tesis y su riesgo es el inventario. Filosofías opuestas.
- No tenemos ni necesitamos: latencia de milisegundos, presencia 24/7 en el libro, cobertura en
  derivados (solo-LONG spot), ni comisiones de mayorista.
- Valor real de entender el market making para nosotros: saber que **el spread y el slippage
  que pagamos en cada trade son el sueldo de estos jugadores** — por eso los backtests honestos
  los descuentan siempre (ver `46`), y por eso las órdenes en momentos violentos ejecutan peor
  (el maker se protege ampliando el spread justo cuando más quieres entrar).
