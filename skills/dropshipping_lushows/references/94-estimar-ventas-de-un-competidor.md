# Estimar ventas de un competidor

> Vigencia: 14-sep-2026. Todo lo de aquí produce **rangos**, nunca cifras. Quien te dé un número
> exacto de ventas ajenas está adivinando con confianza.

## Los tres métodos y su error

| Método | Requiere | Error típico | Confianza |
|---|---|---|---|
| **Reseñas** | Que muestre reseñas con fecha | ±3-5× | Media |
| **Numeración de pedidos** | Que el nº de pedido sea secuencial y visible | ±30% si es secuencial real | **Alta** |
| **Inventario / disponibilidad** | Variantes que se agotan | Muy alto | Baja |

Úsalos en ese orden de preferencia, y **cruza al menos dos** antes de escribir una conclusión.

## Método 1 — Por reseñas

Premisa: solo una fracción de compradores deja reseña. En e-commerce de respuesta directa esa tasa
suele estar entre **1% y 5%** (verificar por nicho; la app de reseñas y los recordatorios por correo
la mueven muchísimo).

Procedimiento:

1. Abre la ficha del producto y cuenta el total de reseñas.
2. Anota la fecha de la **más antigua** y la **más reciente**.
3. Calcula los días transcurridos entre ambas.
4. Aplica la banda:

```
ventas_min = reseñas / 0,05     (si el 5% reseña)
ventas_max = reseñas / 0,01     (si el 1% reseña)
```

Ejemplo: 120 reseñas en 90 días → entre **2.400 y 12.000** unidades. Sí, la banda es enorme. Esa es
la verdad del método; por eso hay que cruzarlo.

Trampas:

| Trampa | Cómo la detectas |
|---|---|
| Reseñas importadas de AliExpress | Nombres extranjeros, fotos genéricas, fechas todas iguales, idioma raro |
| Reseñas compradas | Todas 5 estrellas, redacción parecida, en bloque de pocos días |
| Reseñas filtradas | Cero reseñas de 1-2 estrellas en 300 reseñas: imposible |
| Reseñas de OTROS productos | Apps que agrupan reseñas de toda la tienda |

Si detectas importación, el método no sirve: descártalo entero.

## Método 2 — Numeración de pedidos (el mejor)

Muchas tiendas muestran el número de pedido en la página de confirmación o en el correo. Si es
secuencial, mides el caudal directamente.

Procedimiento:

1. Haz una compra real pequeña (o llega hasta donde se genere el número; si tu plataforma solo lo da
   tras pagar, es una compra-espía, ver `92`). **Anota el número y la fecha/hora exacta.**
2. Espera **7 días exactos**.
3. Repite. Anota el segundo número.
4. `pedidos_semana = numero_2 - numero_1`.
5. `ventas_mes ≈ pedidos_semana × 4,33`.

Advertencias reales:

- Shopify empieza en 1001 por defecto; muchas tiendas lo desplazan a propósito para parecer grandes.
- El contador incluye pedidos cancelados y fallidos.
- Algunas plataformas usan numeración aleatoria: si los dos números no guardan relación creciente
  razonable, el método no aplica.
- Cuesta dos compras. Hazlo solo con **el competidor principal**.

Este método es el único que da una cifra defendible. Cuando puedas usarlo, úsalo.

## Método 3 — Por inventario y disponibilidad

Si en `/products.json` (ver `93`) hay `available: false` en variantes concretas, o el tema muestra
"quedan X unidades", puedes seguir la evolución día a día.

| Observación repetida 7 días | Lectura |
|---|---|
| Una variante pasa de disponible a agotada | Está vendiendo esa variante |
| Todas agotadas de golpe | Problema de proveedor, no de demanda (`85`) |
| Nunca cambia nada | Contador falso (app de escasez) o stock enorme |

Los contadores de "quedan 7 unidades" son **casi siempre falsos** (apps de urgencia con número
aleatorio). Verifica recargando en ventana privada: si el número cambia sin lógica, es teatro.

## De ventas a facturación (y por qué no sabes su ganancia)

```
facturacion_estimada = ventas_estimadas × ticket_promedio_observado
```

El ticket lo sacas de `103` y `104` (precio base + probabilidad de bundle/upsell). Pero **facturación
no es ganancia**. Lo que no ves:

| No ves | Por qué importa |
|---|---|
| Costo del producto | Puede ser 20% o 60% del precio |
| Costo de pauta | Suele ser la mayor partida, 25-40% |
| Envío real | Si lo absorbe, cambia todo |
| Devoluciones y contracargos | En COD pueden ser brutales; en prepago mucho menos |
| Impuestos | IVA 16% en México, más aranceles de importación (`16`) |

Un competidor puede facturar el equivalente a USD 80.000/mes y estar perdiendo dinero. Pasa todo el
tiempo. **Nunca uses la facturación estimada de otro como prueba de que el negocio es rentable.** Usa
tus propios números: `06` y `11`.

## Plantilla de conclusión honesta

> "Competidor X, producto Y, México. 214 reseñas con fecha entre 12-may y 09-sep-2026 (120 días).
> Banda por reseñas: **4.300-21.400 unidades** en ese periodo. Numeración de pedidos no verificada.
> Ticket observado 1.099 MXN simple / 1.699 MXN bundle 2x. **Conclusión: el producto mueve volumen
> real en México; magnitud exacta no determinable. Rentabilidad desconocida.**"

Esa conclusión se puede defender delante de cualquiera y sirve para decidir. "Factura 3 millones al
mes" no.

## Relacionados
`92` espiar tiendas · `93` catálogo Shopify · `84` estimar inversión · `103` precios · `104` bundles · `06` la ecuación del negocio
