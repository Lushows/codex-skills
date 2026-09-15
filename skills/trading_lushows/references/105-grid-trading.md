# 105 — Grid trading: por qué parece dinero gratis (y no lo es)

**Grid trading** = poner una "grilla" de órdenes escalonadas: comprar cada vez que el precio
baja un escalón y vender cada vez que sube uno. Ejemplo: entre $60.000 y $70.000, una orden
cada $1.000. El precio sube y baja, la grilla compra abajo y vende arriba una y otra vez, y
cada vaivén deja una ganancia chiquita. Los exchanges lo ofrecen como bot de un clic.

## Por qué seduce

- **Parece que monetiza el ruido**: el precio siempre oscila, y cada oscilación "paga".
- **Gana seguido**: montones de operaciones ganadoras pequeñas. El historial se ve verde.
- **No pide predicción**: no hay que saber si sube o baja, solo que se mueva dentro del rango.
- Cero decisiones: se configura y "trabaja solo".

Todo eso es cierto... mientras el precio se quede dentro del rango.

## La letra pequeña: la tendencia contra la grilla

El perfil de resultados de un grid es el clásico "recoger monedas delante de una aplanadora":
muchas ganancias chicas y una pérdida grande esperando su turno.

| Escenario | Qué le pasa al grid |
|---|---|
| Precio lateral dentro del rango | Gana poquitos, seguido — el escenario de folleto |
| Precio rompe hacia ABAJO | La grilla compró en cada escalón de la caída: quedas cargado del activo con pérdida grande y sin plan de salida |
| Precio rompe hacia ARRIBA | La grilla vendió todo en la subida: te bajaste del movimiento que sí pagaba |

El problema de fondo: **el grid es una apuesta implícita a que el rango se mantiene**, pero se
vende como si no apostara nada. Y cripto es precisamente un mercado de tendencias violentas que
rompen rangos sin avisar. Peor: comprar cada escalón hacia abajo es promediar a la baja
sistematizado — la práctica que este método prohíbe explícitamente (ver `106`).

El grid no elimina el riesgo; **lo esconde en la cola**: semanas de ganancias visibles, y la
pérdida concentrada el día que el rango se rompe. Un historial de grid con 95% de trades
ganadores puede tener expectancy negativa — por eso se mira profit factor y expectancy, nunca
el win rate solo.

## ¿Quién puede usarlo con sentido?

Quien pueda definir el rango con criterio, dimensionar la pérdida del peor caso (ruptura hasta
el fondo de la grilla) como un riesgo aceptado de una sola posición, y tenga un plan de corte
si el rango se rompe. Es decir: exige exactamente el trabajo de análisis y gestión de riesgo
que el folleto promete evitar.

## Por qué NO para nuestro bot

- **Contradice el riesgo definido por trade**: el AGENTE TRADING arriesga 1.5% con stop conocido
  ANTES de entrar. El grid acumula exposición creciente sin stop natural — su "peor caso" es
  la grilla entera comprada en una caída.
- **Contradice la filosofía de edge**: el bot opera cuando hay razón estadística (convicción ≥8);
  el grid opera porque el precio se movió, sin pregunta previa. Es actividad, no edge.
- **Es promediar abajo con otro nombre**, y esa práctica está prohibida en el protocolo.
- **El régimen ya nos dice cuándo no operar**: en lateral, la decisión sana del bot es quedarse
  quieto — no montar una grilla para "aprovechar" el lateral apostando a que dura.
- Si algún día se explorara (no está en el plan), sería como sistema separado, backtesteado con
  costos y con corte duro de ruptura de rango — nunca parchado sobre el bot actual.
