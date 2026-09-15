# 172 — Impuestos del trading en Colombia (conceptos, no cifras)

> ⚠️ Este módulo da el **mapa conceptual**. Cifras, tarifas, topes y formularios cambian cada
> año: **SIEMPRE verificar al día con contador_lushows o directamente con la DIAN.**
> Nada de aquí reemplaza a un contador titulado.

## Las 3 verdades que no cambian

1. **Las ganancias en cripto se declaran.** Que sea digital no la hace invisible: para la DIAN
   la cripto es un activo, y vender con ganancia genera renta.
2. **La cripto que TIENES es patrimonio.** Aunque no vendas nada, el saldo en cripto al cierre
   del año cuenta dentro de tu patrimonio (lo que posees), y eso puede afectar si estás
   obligado a declarar y cuánto.
3. **El momento del impuesto es la VENTA (realización).** Mientras el precio sube y no vendes,
   la ganancia es "de papel". Al vender (o cambiar por otra cripto — ojo, eso también puede
   contar como venta), la ganancia se vuelve real y declarable.

## Trading habitual vs ocasional (por qué importa)

| Concepto | Idea | Tratamiento típico |
|---|---|---|
| **Ocasional** | Compraste, esperaste mucho tiempo, vendiste una vez | Puede tratarse como ganancia ocasional |
| **Habitual** | Operas seguido, es una actividad recurrente | Se parece más a renta ordinaria (tu "negocio") |

La línea entre uno y otro NO es una cifra mágica — depende de frecuencia, intención y cómo lo
sustente el contador. Un bot que hace swing trading recurrente apunta claramente a **habitual**.
La calificación exacta y sus consecuencias: **contador_lushows**.

## Lo que Luis debe guardar desde el día 1 (esto sí es universal)

- **Cada trade**: fecha, activo, cantidad, precio de compra, precio de venta, comisión.
- **Cada depósito/retiro** en pesos: comprobante bancario + registro del exchange.
- **Costo fiscal**: cuánto te costó lo que vendiste (sin esto, la DIAN puede asumir lo peor).
- Exportes periódicos del historial del exchange (si la cuenta se congela, el historial también).

La buena noticia: el AGENTE TRADING **ya registra todo trade con fecha, precio, tamaño y
razón** — el diario del bot es la mitad de la contabilidad hecha.

## Errores caros (anti-humo)

- "No retiré a pesos, así que no debo nada" — cambiar cripto por cripto puede ser hecho gravable.
- "Es poquito, no vale la pena declarar" — el patrimonio omitido descubierto después cuesta
  mucho más que declararlo a tiempo.
- "El exchange no le reporta a Colombia" — asumir eso es apostar tu tranquilidad a un rumor.

## Cómo aplica al AGENTE TRADING

- **Paper trading: cero impuestos** — no hay dinero real, no hay hecho gravable. Etapa perfecta
  para montar la disciplina de registro sin costo.
- Antes del go-live: sesión con **contador_lushows** para definir habitual vs ocasional,
  obligación de declarar según el patrimonio de Luis, y el formato de registro que el contador
  necesitará. Diseñar el reporte del bot para que exporte eso directo.
