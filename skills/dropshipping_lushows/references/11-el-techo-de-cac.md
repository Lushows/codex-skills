# El techo de CAC (el número que gobierna el negocio)

## Definición

```
TECHO DE CAC = TICKET − TODOS LOS COSTOS POR PEDIDO COBRADO
```

Es **lo máximo que puedes pagar por conseguir una venta** antes de empezar a perder dinero.

Todo el negocio se reduce a una competencia entre dos números:

```
  TECHO DE CAC   (lo controlas tú)
        vs
  CAC REAL       (lo controla la subasta publicitaria)
```

## Por qué es más importante que el ROAS

El ROAS es un número sin contexto. Un ROAS de 2,0 puede ser excelente o ruinoso:

| Negocio | Ticket | Techo de CAC | ROAS de equilibrio | ¿ROAS 2,0 sirve? |
|---|---|---|---|---|
| Margen alto | $60 | $30 | 2,00 | Estás en el límite exacto |
| Margen bajo | $38 | $10 | 3,80 | Estás perdiendo plata |
| Margen muy alto | $90 | $60 | 1,50 | Estás ganando bien |

El techo de CAC te dice **tu** número. El ROAS solo te dice el de la industria.

## Cómo se calcula, renglón por renglón

```
  TICKET (lo que paga el cliente, con envío si lo cobras)
− costo del producto
− flete internacional prorrateado por unidad
− arancel e impuestos de importación
− flete de última milla al cliente
− comisión de pasarela o de plataforma COD
− costo de confirmación (bot, call center) si aplica
− COSTO DE LOS PEDIDOS FALLIDOS repartido entre los cobrados
                                   ↑ el renglón que todos olvidan
= TECHO DE CAC
```

### El renglón que hunde operaciones

Los pedidos que no se cobran **igual costaron dinero**. En contraentrega pagaste el flete de ida y el
de regreso. En prepago reembolsado perdiste el producto y el envío.

La forma correcta de modelarlo:

```
desperdicio = (1 − tasa de cobro) ÷ tasa de cobro

costo_fallidos_COD     = desperdicio × (flete × 2 + costo de confirmación)
costo_fallidos_prepago = desperdicio × (costo del producto + flete)
```

Con tasa de cobro del 78%, el desperdicio es 0,282: **por cada venta buena pagas el 28% de un
fallido**. Con 52% de entrega, el desperdicio es 0,923 — casi un fallido entero por cada venta buena.
Ahí es donde muere el contraentrega sin confirmación. Ver `163`.

## La holgura: el número que dice si puedes escalar

```
HOLGURA = TECHO DE CAC ÷ CAC REAL
```

| Holgura | Lectura | Qué hacer |
|---|---|---|
| < 1,0 | Pierdes en cada venta | Parar. Subir ticket o cambiar producto |
| 1,0 - 1,3 | Trabajas gratis | Arreglar oferta antes de gastar más |
| 1,3 - 2,0 | Negocio real, frágil ante el CPM de temporada | Escalar con cuidado |
| 2,0 - 3,0 | Sano. Aguanta el Black Friday | Escalar |
| > 3,0 | Excelente. Probablemente estás subinvirtiendo | Subir presupuesto agresivo |

**La holgura es lo que se come la temporada alta.** Si el CPM sube 60% en Black Friday, tu CAC sube
proporcionalmente y tu holgura de 2,0 se convierte en 1,25. Por eso se entra a temporada con holgura
de sobra, no justa.

## Cómo subir el techo (esto es lo que rinde)

Ordenado por impacto real, de mayor a menor:

1. **Subir el ticket con bundle.** El flete, la comisión y el CAC no cambian. Es la palanca más
   grande que existe. Ver `218`, `220`.
2. **Subir la tasa de cobro.** Pasar de 52% a 78% de entrega reduce el desperdicio de 0,92 a 0,28.
   Ver `159`, `160`.
3. **Añadir order bump y upsell.** Ingreso incremental con costo marginal casi nulo. Ver `219`.
4. **Bajar el flete.** Negociar volumen, cambiar transportadora, reducir peso del empaque.
5. **Bajar el costo del producto.** Negociar con el proveedor. Es lo último porque es lo que menos
   mueve la aguja y lo que más tiempo toma.

Nota el orden: **lo que todos hacen primero (pelear el precio del proveedor) es lo último de la
lista.**

## Cómo bajar el CAC real

No lo controlas del todo, pero sí influyes:
- Mejor creativo → mejor CTR → menos CPM efectivo por clic. Ver `248`.
- Mejor página → mejor CVR → menos clics por venta. Ver `204`.
- Mejor señal al algoritmo (CAPI, eventos limpios) → mejor optimización. Ver `200`.
- Salir de la semana de mayor competencia → CPM más barato. Ver `274`.

## El modelo ejecutable

No calcules esto a mano. Está en `228` como script y en `12` como comparador de países.

## Relacionados
`06` la ecuación del negocio · `12` comparador de países · `220` el ticket como palanca · `224` calcular el CAC real · `226` ROAS de equilibrio · `228` modelo financiero · `163` el costo oculto de los rechazos
