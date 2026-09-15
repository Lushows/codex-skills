# 43 — Order flow y libro de órdenes

El **libro de órdenes** (order book) es la lista en vivo de todas las órdenes de compra y venta
pendientes en un exchange. El **order flow** es el estudio de cómo se ejecutan esas órdenes en
tiempo real. Es la lupa de máximo aumento del mercado — y justamente por eso, casi irrelevante
para nuestro swing en 1h. Este módulo existe para entender el concepto y saber por qué NO lo usamos.

## Los conceptos básicos

| Término | Qué es |
|---|---|
| **Bid** | Mejor precio al que alguien quiere COMPRAR ahora |
| **Ask** | Mejor precio al que alguien quiere VENDER ahora |
| **Spread** | Diferencia entre bid y ask (en BTC en exchanges grandes, mínima) |
| **Profundidad** | Cuánto volumen hay apilado en cada nivel del libro |
| **Órdenes limit** | Pasivas: esperan en el libro a que el precio llegue |
| **Órdenes market** | Agresivas: ejecutan ya, contra lo que haya en el libro |

El precio se mueve cuando las órdenes agresivas se comen la profundidad de un lado: más
compradores a mercado que liquidez en el ask → el precio sube al siguiente nivel.

## Absorción e imbalances

- **Absorción**: llegan ventas agresivas grandes y el precio NO cae — alguien con órdenes de
  compra pasivas se las está "comiendo" todas. Suele marcar pisos: un jugador grande acumulando.
- **Imbalance**: desequilibrio marcado entre agresión compradora y vendedora en un nivel.
- **La trampa del libro**: las órdenes pasivas visibles se pueden cancelar en milisegundos.
  Los "muros" gigantes de compra suelen ser teatro (spoofing) — se pintan para asustar y se
  retiran antes de ejecutarse. El libro muestra intenciones declaradas, no compromisos.

## Por qué el swing 1h casi no lo necesita

1. **Escala temporal**: el order flow informa los próximos segundos/minutos. Nuestras decisiones
   viven en horas/días. Para cuando la vela de 1h cierra, mil batallas del libro ya ocurrieron
   y su resumen ES la vela (`30`).
2. **Costo/beneficio**: leer order flow exige datos en tiempo real (streams de nivel 2),
   infraestructura y atención continua. Todo eso para afinar la entrada unos décimos de % en
   trades que buscan movimientos de varios %.
3. **Es el terreno de los profesionales de HFT**: competir en microestructura contra firmas con
   servidores pegados al exchange es elegir la pelea que no podemos ganar. En 1h, en cambio,
   la paciencia compite bien.
4. Lo único que el swing hereda del order flow ya lo tenemos en versión agregada: el volumen
   por vela (`36`) y los niveles donde el precio reaccionó (`31`, `44`).

## Cómo aplica al AGENTE TRADING

- **Fuera del alcance, a propósito.** El bot decide sobre velas 1h cerradas; no consume libro
  ni trades en tiempo real, y agregarlo sería complejidad máxima por edge ~nulo en este marco.
- El concepto útil que sí viaja a nuestro marco: una mecha larga con volumen alto sobre un
  soporte (`30` + `36`) es la huella VISIBLE de una absorción — la versión "para swing" de
  todo este módulo, y Claude puede leerla en los datos que ya recibe.
