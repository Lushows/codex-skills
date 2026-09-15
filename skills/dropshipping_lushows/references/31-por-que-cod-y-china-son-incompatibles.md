# Por qué COD y China son incompatibles

> El hallazgo central de esta skill. Si te llevas una sola idea, que sea esta:
> **pago contra entrega + proveedor a 15 días = negocio muerto**, aunque cada pieza por separado
> funcione.

## La frase en una línea

Cuando el cliente paga al recibir, **puede arrepentirse sin costo**. Y le das entre 15 y 25 días
para hacerlo.

## La mecánica psicológica

El día que compra, el cliente está en el pico de deseo: acaba de ver tu video, el problema que le
mostraste le duele, el precio le pareció justo. Ese pico **no dura**.

| Día | Estado mental del cliente COD | Probabilidad de recibir |
|---|---|---|
| 0 | Pico de deseo. Ordena | — |
| 1-3 | Todavía lo recuerda y lo espera | Alta |
| 4-7 | Se enfría. Empieza a dudar del precio | Media-alta |
| 8-14 | "¿Yo pedí eso?". Ya compró otra cosa, o vio uno más barato | Media-baja |
| 15-25 | Olvido, desconfianza ("me estafaron"), o simplemente no está en casa | **Baja** |

En prepago la duda no importa: **ya pagaste**. El cliente que se arrepiente devuelve, y devolver
cuesta trabajo, así que la mayoría se queda con el producto. En COD arrepentirse cuesta cero: solo
hay que no abrir la puerta.

> El pedido COD no es una venta. Es **una opción de compra gratis** que le regalaste al cliente,
> con vencimiento el día que llegue el mensajero.

## Los números

| Escenario | Días de tránsito | Rechazo típico | Entrega |
|---|---|---|---|
| Stock local urbano, confirmado | 1-3 | ~15-22% | **78-85%** |
| Stock local nacional, confirmado | 3-6 | 22-35% | 65-78% |
| Stock local sin confirmar | 3-6 | 40-55% | 45-60% |
| **China → LatAm, COD** | **15-25** | **~50%** | **~50%** |

El salto es el que importa: el rechazo pasa de **~28% a ~50%** cuando el tránsito se estira a dos
o tres semanas. Cada punto de rechazo se paga dos veces — flete de ida y flete de retorno — y el
producto puede volver inservible o no volver.

## Por qué destruye el margen, con aritmética

Costo real por venta **cobrada** cuando la mitad no se cobra:

```
Por cada 100 pedidos:
  50 se entregan y pagan
  50 se rechazan  →  pagas flete de ida ×50, flete de retorno ×50 y la confirmación ×100

Costo de los fallidos repartido entre los buenos:
  desperdicio = (1 − 0,50) / 0,50 = 1,00
  → cada venta buena carga el costo completo de una venta fallida
```

Aplicado al modelo mexicano verificado, con arancel del 33,5% a origen sin TLC encima:

| Configuración | Ticket USD | Entrega | Costo total | Utilidad por venta |
|---|---|---|---|---|
| Prepago bundle 1.099 + MSI, stock local | 60,05 | 97% | 29,33 | **+20,18** |
| COD 1.099 confirmado, stock local | 60,05 | 78% | 33,63 | +19,87 |
| **COD desde China directo** | 38,20 | **50%** | 46,86 | **−18,11** |

**Menos dieciocho dólares por venta.** No es un margen bajo: es una máquina de quemar plata que se
acelera cuando escalas la pauta.

## El triple golpe

No es un solo problema, son tres que se multiplican:

| Golpe | Qué pasa |
|---|---|
| **1. Tiempo** | 15-25 días borran el impulso que pagaste con publicidad |
| **2. Sin fricción para arrepentirse** | No abrir la puerta es gratis; devolver un prepago no lo es |
| **3. Aduana** | Con el de minimis de EE.UU. eliminado y el decreto mexicano del 33,5%, la mercancía llega más cara o se detiene. Ver `13`, `14`, `16` |

Y hay un cuarto silencioso: **el píxel aprende basura**. Si le reportas 100 compras y solo 50 son
reales, el algoritmo te trae más gente parecida a los 50 que no pagan. El costo del error se
compone semana a semana. **Invoca `facebook_ads_lushows`** para la mecánica del evento de compra.

## Las combinaciones que sí funcionan

| Proveedor | Cobro | ¿Funciona? | Por qué |
|---|---|---|---|
| China lejos | COD | **Nunca** | Este módulo completo |
| China lejos | **Prepago** | Sí, con condiciones | Ya cobraste; el riesgo es reputacional y de contracargo, no de caja. Exige promesa de entrega honesta en la página |
| **Stock local** | COD | Sí, con confirmación | 1-3 días urbano → 78-85% de entrega |
| **Stock local** | **Prepago** | **Lo mejor** | 97% de cobro y caja en 3 días. Es la configuración del proyecto |

## Si ya estás en la combinación mala: el orden de los arreglos

1. **Apaga el COD hoy.** Pasa a prepago aunque la conversión caiga a la mitad. Dejas de perder por
   pedido.
2. **Consigue stock local** aunque sea de un mayorista con menos margen. Margen menor cobrado supera
   margen mayor no cobrado.
3. **Confirma antes de despachar** todo lo que quede en COD. Sube la entrega 15-25 puntos. Ver `160`.
4. **Sube el ticket.** El flete fallido se diluye mejor sobre un pedido de 1.099 que sobre uno de
   399. Ver `218`.
5. **Cierra las zonas malas.** Si una región entrega por debajo del 55%, no la anuncies.

## Señales de que ya estás en el problema

| Señal | Diagnóstico |
|---|---|
| El panel de anuncios reporta buen ROAS pero el banco no crece | Estás midiendo pedidos, no cobros |
| "Tasa de entrega" que nadie mide en la empresa | Ya perdiste el control |
| Clientes que escriben "¿ya viene?" al día 10 | Vas camino al rechazo |
| Devoluciones que llegan sin abrir | Puro arrepentimiento por demora |
| El proveedor te da tracking que no actualiza en 6 días | El cliente lo ve también |

## La excepción que confirma la regla

COD **sí** funciona con tránsito largo en un solo caso: producto insustituible, sin alternativa
local, y comprador que ya te conoce (segunda compra). Es tan estrecho que en la práctica no es un
plan de adquisición, es una cola de clientes fieles.

## Qué hace el proyecto activo

Tienda de México, diciembre 2026: **prepago cerrando en página web y stock local, nunca China
directo**. No es prudencia excesiva — es que la alternativa está cuantificada en −US$18,11 por
venta. Ver `20`, `16`.

## Relacionados
`30` COD vs prepago · `32` velocidad de rotación de caja · `13` mapa aduanero · `16` arancel de
México · `20` playbook México · `128` proveedores locales · `160` confirmación de pedidos ·
`218` bundle y ticket
