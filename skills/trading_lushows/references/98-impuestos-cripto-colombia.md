# 98 — Impuestos cripto en Colombia (panorama, no asesoría)

> Este módulo da el MAPA general para que nada tome por sorpresa. Cifras exactas (UVT, tarifas,
> topes de declaración del año fiscal) cambian: **verificar con `contador_lushows` al día** y,
> cuando haya plata real de por medio, con un contador titulado.

## Lo primero: en paper NO aplica nada

Mientras el bot opera con dinero simulado no hay ingreso, no hay activo, no hay nada que
declarar. Este módulo se vuelve relevante el día del primer peso real.

## El mapa general (Colombia)

| Concepto | La idea en simple |
|---|---|
| Cripto es un activo | Para la DIAN, las criptomonedas son un activo intangible con valor patrimonial. Tenerlas cuenta en tu patrimonio; venderlas con utilidad genera ingreso gravable |
| Renta vs ganancia ocasional | El tratamiento depende, entre otras cosas, de cuánto tiempo se poseyó el activo. Un bot de swing que compra y vende en días opera en horizontes cortos — la utilidad de ese tipo de actividad tiende al terreno de renta ordinaria, no de ganancia ocasional. La clasificación exacta la define el contador con la norma vigente |
| Obligación de declarar | Declarar renta depende de topes (ingresos, patrimonio, consumos, movimientos bancarios) medidos en UVT que cambian cada año. Mover plata entre bancos y exchanges suma a esos topes aunque no haya utilidad |
| Exógena / reportes | Los exchanges y las plataformas de pago reportan información a la DIAN. Asumir siempre que la DIAN puede ver los movimientos: se declara porque toca y porque conviene |
| Costo fiscal | La utilidad gravable es venta menos costo de adquisición (y fees). Sin registros buenos, no puedes demostrar el costo → terminas tributando sobre más de lo que ganaste |

## Lo que el bot ya hace bien para esto (sin buscarlo)

El log estructurado de cada orden (fecha, par, cantidad, precio, fees) ES la contabilidad
primaria que un contador va a pedir. Reglas desde el día 1 live:

1. No borrar jamás el historial de trades; exportarlo periódicamente fuera de Render.
2. Guardar los extractos/reportes que Binance genere.
3. Registrar la tasa de cambio USD→COP relevante de los retiros (la declaración es en pesos).

## Errores comunes que evitar

- "Como es cripto, no se declara" → falso y caro: sanciones e intereses superan lo ahorrado.
- "Solo declaro cuando paso a pesos" → la obligación puede nacer antes; el patrimonio en
  cripto también se reporta. Lo define el contador, no la intuición.
- Mezclar la plata del bot con la personal en las mismas cuentas → hace la trazabilidad un
  infierno. Cuenta/bolsillo separado para el capital del bot.

## Cómo aplica al AGENTE TRADING

- Módulo 09 ya lo dice: cuando lleguen las primeras ganancias reales → invocar
  `contador_lushows` (y ese skill rutea números exactos a `Matematicas_lushows`).
- Con capital inicial de $200-500, las utilidades del primer año difícilmente mueven la aguja
  tributaria — pero los REGISTROS se llevan perfectos desde el trade #1, porque reconstruirlos
  después es lo verdaderamente costoso.
- Al escalar capital y hacer retiros (módulo 96), la conversación con el contador pasa de
  "por si acaso" a obligatoria anual.
