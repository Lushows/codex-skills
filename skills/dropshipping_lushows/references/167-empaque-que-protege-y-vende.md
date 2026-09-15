# Empaque que protege y vende

> El empaque tiene tres trabajos, en este orden: **que llegue entero, que no te cueste flete de
> más, y que el cliente sienta que compró algo bueno**. El que se salta el primero paga
> devoluciones; el que se salta el segundo paga sobrepeso; el que se salta el tercero no repite
> venta nunca.

> Aquí se define **qué debe lograr** el empaque. El diseño gráfico —cómo se ve, tipografía, color,
> sistema visual— es otro oficio: invoca `directorcreativo_lushows`.

## Los tres trabajos

| Trabajo | Métrica que lo mide | Si falla |
|---|---|---|
| **Proteger** | % de productos dañados en tránsito | Devoluciones, reclamos, seguro que no paga (`166`) |
| **Optimizar** | Peso volumétrico y escalón de tarifa | Flete que se come el margen (`147`) |
| **Vender** | Recompra, reseñas, contenido del cliente | Cliente de una sola vez |

## Proteger: lo mínimo que no se negocia

| Elemento | Cuándo |
|---|---|
| Bolsa de mensajería resistente | Producto no frágil, textil, blando |
| Caja de cartón corrugado | Todo lo rígido o frágil |
| Relleno (burbuja, papel, espuma) | Cualquier hueco: **lo que se mueve se rompe** |
| Bolsa sellada individual | Producto que puede ensuciarse o mojarse |
| Doble cinta en aperturas | Siempre |
| Esquineros | Producto rígido y pesado |
| Sello de garantía | Producto que no debe abrirse antes de entregar |

**Prueba de caída:** deja caer el paquete cerrado desde 1,2 m sobre piso duro, dos veces, y ábrelo.
Si el producto sobrevive, tu empaque sirve. Es literalmente lo que le va a pasar en la banda
transportadora. Hazlo con la primera unidad del lote, no con la número 200.

## Optimizar: el empaque que baja el flete

| Palanca | Efecto |
|---|---|
| Quitar la caja de retail individual del proveedor | Baja 20-40% el volumétrico. Ver `147` |
| Bolsa en vez de caja cuando el producto lo permite | Baja peso y volumen |
| Compactar (textiles al vacío) | Baja mucho el volumen |
| Ajustar la caja al producto, no usar una talla única | Elimina relleno y volumen muerto |
| Vigilar el **escalón de tarifa** de la paquetería | 20 g de más pueden saltar al siguiente escalón |

Antes de cerrar el pedido al proveedor, calcula el volumétrico con el empaque final (`147`). Se
decide en el pedido, no en la bodega.

## Vender: qué debe lograr, sin hablar de diseño

| Objetivo | Cómo se comprueba que se logró |
|---|---|
| Que se sepa de quién es antes de abrir | El cliente identifica la marca sin leer la guía |
| Que abrirlo sea fácil y limpio | No necesita tijeras ni rompe el producto al abrir |
| Que el producto se vea ordenado adentro | Nada suelto ni volcado |
| Que invite a fotografiarlo | El cliente sube la foto sin que se la pidas |
| Que se pueda **reempacar** para devolver | Recuperas producto devuelto (`164`) |
| Que diga cómo contactarte | El cliente con duda te escribe a ti, no a la reseña |

Esto último es logística disfrazada de marketing: un inserto con tu WhatsApp convierte una reseña
de 1 estrella en un mensaje que puedes resolver.

## Marca sí, marca no: el cálculo

| Nivel | Costo | Cuándo |
|---|---|---|
| **Genérico**: caja o bolsa neutra + sticker impreso en casa | Muy bajo | Primer lote, validación, capital < USD 500 |
| **Semi-marca**: cinta impresa + sticker profesional + inserto | Bajo | Producto validado, 100+ pedidos/mes |
| **Marca completa**: caja impresa a medida | Alto, con mínimos de pedido altos | Producto que ya probaste que vende y repite |

Regla: **no imprimas 1.000 cajas de un producto que no has vendido 200 veces.** Es el gasto que más
capital congela en tiendas nuevas. El sticker y la cinta impresa dan el 70% del efecto por el 10%
del costo.

## El empaque como arma contra el rechazo en COD

Un paquete que se ve serio se rechaza menos en la puerta.

| Detalle | Efecto |
|---|---|
| Rótulo impreso, nunca a mano | Se ve profesional y se pierde menos (`165`) |
| Nombre de la tienda visible | El cliente reconoce lo que pidió |
| Paquete limpio, sin reutilizar cajas con logos ajenos | Evita el "esto no es lo que compré" |
| **No** poner afuera lo que contiene, si es atractivo para robo | Menos hurto en reparto |

## Etiquetado obligatorio

Según país y categoría puede exigirse: país de origen, composición, importador, contenido neto,
advertencias, instrucciones en idioma local. Faltarlo puede significar retención en aduana (`151`)
o multa en el mercado.

Verifica el requisito **antes** de pedir el lote: pegarle etiquetas a 500 unidades ya importadas es
un fin de semana entero de trabajo. Para requisitos formales, invoca `contador_lushows`.

## Costeo del empaque

| Componente | Va al costo unitario |
|---|---|
| Caja o bolsa | Sí |
| Relleno | Sí |
| Cinta y sticker | Sí (prorrateado por rollo) |
| Inserto impreso | Sí. Ver `168` |
| Tiempo de empacar | Sí, si pagas a alguien |

Todo esto entra en `152` como `empaque_destino_unit`. Un empaque de USD 0,60 sobre un producto de
USD 4 es un 15% del costo: no es un detalle.

## Errores caros

| Error | Consecuencia |
|---|---|
| Empacar con lo que había | Roturas, reclamos, seguro que no paga |
| Caja enorme con relleno de aire | Pagas volumen que no usas |
| Caja justa sin relleno | Llega abollado |
| Imprimir marca antes de validar | Capital muerto |
| Olvidar el etiquetado legal | Retención o multa |
| No probar la caída | Lo descubres con el cliente |

## Relacionados
`168` inserto y desempaque · `164` devoluciones · `165` paquetes perdidos · `166` seguros ·
`147` peso volumétrico · `152` costo puesto en destino · invoca `directorcreativo_lushows`
