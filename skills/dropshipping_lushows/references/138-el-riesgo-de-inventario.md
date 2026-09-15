# El riesgo de inventario

> Vigencia: septiembre 2026. Para modelar tu exposición invoca `Matematicas_lushows`; para la
> estructura financiera, `economist_lushows`.

El inventario es el único activo del ecommerce que puede valer cero de un día para otro. Y es donde
se muere la mayoría de los negocios que **estaban ganando dinero**. No quiebras por vender poco:
quiebras por tener plata en cajas y no en el banco.

## Las cinco formas de perder con inventario

| Riesgo | Cómo se ve | Frecuencia |
|---|---|---|
| **Obsolescencia** | El producto pasó de moda o salió la versión nueva | Alta en moda/gadgets |
| **Sobrestock** | Compraste 1.000 y vendes 3/día | **La más común** |
| **Producto malo** | Llegó con defectos y nadie inspeccionó | Alta sin QC. Ver `123` |
| **Iliquidez** | El producto vende, pero la plata está en cajas y no puedes pautar | **La más letal** |
| **Merma** | Robo, rotura, humedad, vencimiento | 1-5% |

La cuarta mata negocios sanos. Las otras cuatro matan negocios malos.

## El caso que se repite siempre

```
Mes 1: vendes 200 unidades con plataforma. Margen apretado pero positivo.
       "Si compro el lote, mi margen sube 25 puntos."
Mes 2: compras 1.000 unidades con US$3.000. Te quedan US$600 para pauta.
Mes 3: con US$600 de pauta vendes 90 unidades, no 200.
       Tienes 910 unidades y US$180 en el banco.
Mes 4: subes el precio para "recuperar". Vendes menos.
       Bajas el precio para "mover inventario". Margen cero.
Mes 5: liquidas al costo. Perdiste 5 meses y el capital.
```

El error no fue comprar. Fue comprar **sin dejar caja para pauta**. El inventario no se vende solo.

## La regla del 55/40/5

De tu caja disponible, en fase de crecimiento:

| Destino | % |
|---|---|
| Inventario | **máximo 55%** |
| Pauta y adquisición | **mínimo 40%** |
| Reserva operativa (devoluciones, imprevistos) | 5% |

No es una regla sagrada, pero la proporción importa más que los números exactos: **si el inventario
supera el 60% de tu caja, estás en riesgo de iliquidez aunque el negocio sea rentable.**

## Cómo medir tu exposición

| Indicador | Fórmula | Zona sana | Alarma |
|---|---|---|---|
| Días de inventario | stock / velocidad diaria | 30-60 | 90+ |
| Rotación anual | 365 / días de inventario | 6-12 | menos de 4 |
| Inventario / caja total | — | menos de 55% | más de 70% |
| Inventario muerto (90+ días sin venta) | — | menos de 10% | más de 25% |
| Cobertura de pauta (meses de pauta en banco) | caja libre / gasto mensual de pauta | 1,5-3 | menos de 1 |

El último es el que nadie mira y el que avisa primero. Si tienes menos de un mes de pauta en el banco,
un mal mes te saca del juego.

## Riesgo por tipo de producto

| Tipo | Riesgo de obsolescencia | Cobertura máxima recomendada |
|---|---|---|
| Moda viral / tendencia de TikTok | 🔴 Muy alto | 20-30 días. **O no compres** |
| Estacional (Navidad, regreso a clases) | 🔴 Alto fuera de temporada | Vender el 90% en la ventana |
| Electrónica y gadgets | 🟠 Alto (salen versiones) | 45 días |
| Moda de temporada | 🟠 Alto | 45 días |
| Problema permanente (salud, hogar, mascotas) | 🟢 Bajo | 60-90 días |
| Consumible recurrente | 🟢 Muy bajo | 60-90 días |

**Nunca compres inventario de un producto viral.** Para cuando llega el lote, la tendencia murió. El
viral se ordeña con stock de tercero y se abandona. Ver `61`.

## Las señales tempranas de que vas a tener un problema

| Señal | Gravedad |
|---|---|
| Subiste el presupuesto de pauta para "mover inventario" | 🔴 Espiral |
| Bajaste el precio y el margen quedó en cero | 🔴 |
| Llevas 3 semanas con ventas cayendo y tienes lote en camino | 🔴 |
| Tu días-de-inventario pasó de 45 a 90 en dos meses | 🟠 |
| Tienes más de 3 SKUs con 90 días sin movimiento | 🟠 |
| Tu caja libre no cubre un mes de pauta | 🔴 |

## Qué hacer cuando ya tienes sobrestock

En orden de preferencia:

1. **Bundle.** Empaqueta el producto lento con el que vende. Mueve inventario sin destruir el precio
   de lista. **La mejor opción, siempre.**
2. **Regalo por compra.** "Llévate X gratis con tu pedido." Sube el ticket percibido y limpia stock.
3. **Oferta a la base de clientes existente.** CAC cero. Invoca `ventas_lushows` para el guion.
4. **Descuento agresivo por tiempo limitado.** Daña el precio de referencia; úsalo con fecha de cierre.
5. **Marketplace** (Mercado Libre, Amazon). Menor margen pero tráfico gratis.
6. **Liquidadores mayoristas.** Recuperas 20-40% del costo.
7. **Donación.** Recuperas espacio y, según el país, algún efecto fiscal. Invoca `contador_lushows`.

**Lo que NO hay que hacer:** mantener el precio y esperar. El inventario no mejora con el tiempo; se
deteriora y consume almacenaje.

## La regla que evita el 90% del problema

> **Nunca compres inventario de un producto que no hayas vendido 100 veces con stock de tercero.**

Es la regla del modelo híbrido. Ver `136`. El costo de validar con plataforma (sobreprecio del 40-60%
en 100 unidades) es ridículo comparado con quedarte con 900 unidades muertas.

## El riesgo que sube en Q4 y en el ANC

Dos ventanas donde el riesgo de inventario se dispara:

1. **Q4 (Buen Fin, Black Friday, Navidad).** Todo el mundo compra inventario para la temporada. Si
   llegas tarde, te quedas con producto navideño en enero, que vale una fracción.
2. **Año Nuevo Chino.** Para inventario de Q1-2027 hay que arrancar producción a principios de
   noviembre de 2026; con marítimo (30+ días), pedir a más tardar en noviembre. Quien pide en enero
   recibe en abril. Ver `139`.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Medir el éxito por unidades compradas | El éxito es rotación, no volumen |
| Gastar más del 60% de la caja en inventario | Iliquidez con negocio rentable |
| Comprar inventario de producto viral | La tendencia muere antes de que llegue |
| No medir días de inventario semanalmente | El problema aparece cuando ya es grave |
| Mantener precio esperando que se venda | El inventario se deteriora |
| Repones "porque ya tenías el pedido puesto" | Cancela si las ventas cayeron |
| No asegurar el inventario | Un siniestro termina el negocio |

## Para el proyecto activo (México, diciembre 2026)

Con capital menor a US$500, **el riesgo de inventario correcto es cero**. Dropi MX te lo elimina
completo. Esa es la decisión estratégica más importante del proyecto y ya está tomada bien.

Cuando en enero evalúes el lote chico al mayorista mexicano, la restricción dura es:

```
Máximo a invertir en inventario = caja_disponible × 0,55
Mínimo a reservar para pauta    = caja_disponible × 0,40
Cobertura máxima                = 45 días de venta medida en diciembre
```

Y la regla de diciembre: **si el bundle no llega a 100 ventas, no compres nada.** No hay descuento que
compense comprar inventario de algo que no demostró vender.

## Relacionados
Ver `122`, `135`, `136`, `137`, `139`, `61`, `11`, `06`.
