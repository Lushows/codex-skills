# El punto de equilibrio por producto

## De qué equilibrio hablamos

Aquí se calcula el punto de equilibrio **del producto**: cuántos pedidos cobrados necesitas para
que ese producto pague lo que te costó lanzarlo y operarlo. El punto de equilibrio **de la empresa**
(arriendo, sueldos, herramientas, tu vida) es otra cosa: para eso invoca `economist_lushows`.

## Las tres preguntas

| Pregunta | Fórmula |
|---|---|
| ¿Gano dinero con un pedido más? | utilidad por pedido > 0 |
| ¿Cuántos pedidos para recuperar el test? | inversión de test ÷ utilidad por pedido |
| ¿Cuántos para recuperar el stock comprado? | costo del lote ÷ utilidad por pedido |

## 1. Equilibrio por pedido (el básico)

```
utilidad por pedido = ticket − costos por pedido cobrado − CAC
```

Si es negativo, no hay equilibrio posible: cada venta adicional te aleja. Apaga (`231`).

| Escenario MX | Utilidad/pedido | Veredicto |
|---|---|---|
| Suelto 699 | USD 2,63 | positivo pero frágil (holgura 1,21x) |
| Bundle 1.099 | USD 20,18 | sano (holgura 2,92x) |

## 2. Equilibrio del test

```
pedidos para recuperar el test = inversión del test ÷ utilidad por pedido
```

| Inversión de test | Utilidad/pedido 2,63 | Utilidad/pedido 20,18 |
|---|---|---|
| USD 100 | 38 pedidos | 5 pedidos |
| USD 200 | 76 pedidos | 10 pedidos |
| USD 300 | 114 pedidos | 15 pedidos |

Esta tabla explica por qué el ticket flaco no solo gana menos: **tarda muchísimo más en devolverte
el capital de validación**, y con capital menor a USD 500 eso te saca del juego.

## 3. Equilibrio del lote de stock

Con stock local compras por adelantado. Ese capital está muerto hasta que se venda.

```
pedidos para recuperar el lote = (unidades × costo puesto en bodega) ÷ utilidad por pedido
```

Ejemplo: 100 unidades × USD 20 = USD 2.000 de lote.

| Utilidad/pedido | Pedidos para recuperar | % del lote que debes vender |
|---|---|---|
| 20,18 | 100 | 100% |
| 10,00 | 200 | **200% — imposible, el lote son 100** |

Cuando el número de pedidos necesarios supera las unidades del lote, **el lote no se paga solo**:
dependes de una segunda compra a mejor costo o de subir el ticket. Señal de alarma.

## 4. Punto de equilibrio en unidades vendidas con costos fijos del producto

Si ese producto tiene costos fijos propios (fotos, video, muestras, diseño de empaque):

```
unidades de equilibrio = costos fijos del producto ÷ margen de contribución por unidad
```

| Costo fijo | Margen de contribución | Unidades |
|---|---|---|
| USD 250 (creativos + muestras) | 20,18 | 13 |
| USD 250 | 2,63 | 96 |

Ver `227` para calcular el margen de contribución correctamente.

## 5. ROAS de equilibrio (el mismo punto, en lenguaje de pauta)

```
ROAS DE EQUILIBRIO = TICKET ÷ TECHO DE CAC
```

| Escenario MX | ROAS de equilibrio |
|---|---|
| Suelto | 2,50 |
| Bundle | **1,95** |

Por debajo de ese ROAS, pierdes. Ver `226` a fondo.

## Punto de equilibrio y tasa de cobro

En COD el equilibrio se calcula sobre pedidos **cobrados**, no generados. Con 62% de cobro necesitas
generar 161 pedidos para cobrar 100.

```
pedidos generados necesarios = pedidos cobrados necesarios ÷ tasa de cobro
```

Y cada pedido generado que no se cobra sigue costando flete. Ver `229`.

## Tabla de decisión

| Situación | Acción |
|---|---|
| Utilidad por pedido ≤ 0 | apagar hoy (`231`) |
| Equilibrio del test > 40 pedidos | el ticket es muy flaco: bundle (`218`) |
| Lote no se paga con el lote | no repongas hasta subir ticket o bajar costo |
| Equilibrio alcanzado en < 2 semanas | producto validado, escalar (`234`) |
| ROAS real < ROAS de equilibrio 3 días seguidos | pausar y revisar creativo/oferta |

## Horizonte temporal: el equilibrio tiene fecha

Un producto que llega al equilibrio en 6 semanas puede estar muerto antes (ciclo de vida, `62`).
Un producto de temporada tiene un equilibrio con **fecha límite**: si el 20 de diciembre no
recuperaste el lote, el 26 ese lote vale la mitad.

Para el proyecto México dic-2026:

```
Ventana de venta útil: ~1 nov a ~20 dic (Buen Fin 13-17 nov incluido)
El lote debe estar pagado antes del 15 de diciembre.
Lo que quede después es inventario de enero, no utilidad de diciembre.
```

## Ejecución

El cálculo completo (techo, CAC, holgura, ROAS de equilibrio, punto de equilibrio y utilidad) está
implementado en `228`. Para verificar la aritmética de un caso concreto, invoca
`Matematicas_lushows`.

## Relacionados
`11` · `62` · `218` · `223` · `224` · `226` · `227` · `228` · `229` · `231` · `232` · `234` · `238`
