# 144 — Costeo y precios avanzado

Para saber cuánto te cuesta DE VERDAD cada producto y cada cliente — no el costo "a ojo" que esconde
productos que pierden plata. Cuando lo aplicas, casi siempre descubres que el 20% de tus líneas
financia las pérdidas del otro 80%, y que estás regalando trabajo. Aquí ves cómo costear bien y
poner precio sobre verdad, no sobre ilusión.

## Por qué el costeo "a ojo" te engaña

La mayoría costea así: "el producto me cuesta lo que pago por los materiales, le sumo un poco y listo".
Eso es **costo directo** solamente. Ignora todo el costo de operar el negocio (arriendo, sueldos
administrativos, electricidad, software, tu tiempo) — el **costo indirecto** u **overhead**.

- **Costo directo**: lo que se mueve con cada unidad. Materia prima, insumos, comisión de venta, el
  empaque, la hora del operario que toca ese producto. Si haces una unidad más, este costo sube.
- **Costo indirecto (overhead)**: existe aunque no vendas nada hoy. Arriendo, contador, internet,
  el dueño, el ERP, el seguro. No "pertenece" a un solo producto — hay que **repartirlo**.

El problema: si repartes mal el overhead, un producto que parece rentable en realidad pierde plata,
y otro que castigas por "caro" es tu mina de oro. Vendes más del que pierde → quiebras más rápido.

## Las 4 formas de repartir overhead (de peor a mejor)

| Método | Cómo reparte el overhead | Cuándo sirve | Riesgo |
|---|---|---|---|
| **Sin repartir** | No lo cuenta | Nunca (es el error a ojo) | Crees que ganas y pierdes |
| **% sobre ventas** | A cada producto según cuánto factura | Negocio muy simple, 1-2 líneas | Castiga lo caro, premia lo barato |
| **Por mano de obra/horas** | Según horas de trabajo que consume | Servicios, talleres | Ignora otros recursos (máquinas, setups) |
| **ABC (por actividad)** | Según las **actividades** que cada producto realmente usa | Mezcla de productos/clientes muy distintos | Más trabajo de montar |

ABC = *Activity-Based Costing*, costeo basado en actividades. La idea en una frase: **los productos no
consumen costos, consumen actividades; y las actividades consumen recursos.** Repartes el overhead
según cuánto de cada actividad usa cada producto, no según cuánto factura.

## Cómo montar un ABC en 5 pasos (versión PYME, sin software caro)

1. **Lista las actividades** que generan costo indirecto. Ej.: recibir pedidos, preparar/setup,
   producir, empacar, despachar, atender postventa, facturar.
2. **Mete el overhead total del mes en esas actividades** (cuánto cuesta cada actividad al mes).
3. **Elige el "driver" (medidor) de cada actividad** — qué la dispara. Ej.: nº de pedidos, nº de
   setups, horas-máquina, nº de despachos, nº de llamadas de soporte.
4. **Calcula costo por unidad de driver** = costo de la actividad ÷ total de drivers del mes.
5. **Asigna a cada producto/cliente** según cuántos drivers consume.

> Regla práctica: no necesitas 30 actividades. 5-7 actividades bien elegidas capturan el 90% de la
> distorsión. Lo perfecto aquí es enemigo de lo útil.

## Ejemplo numérico (cifras ILUSTRATIVAS, no datos de mercado)

Tienda que vende dos cosas: **Cápsulas** (producto estrella, alto volumen) y **Combos personalizados**
(pocos, pero cada uno lleva armado, instrucciones y soporte). Overhead total del mes: **$12.000.000**.

Mismo overhead, dos métodos:

**A) Método viejo — repartir por % de ventas**

| | Cápsulas | Combos | Total |
|---|---|---|---|
| Ventas del mes | $40.000.000 | $10.000.000 | $50.000.000 |
| Unidades | 2.000 | 100 | |
| Overhead repartido (80%/20% según ventas) | $9.600.000 | $2.400.000 | $12.000.000 |
| Overhead por unidad | $4.800 | $24.000 | |
| Costo directo/unidad | $9.000 | $35.000 | |
| **Costo total/unidad** | **$13.800** | **$59.000** | |
| Precio de venta/unidad | $20.000 | $100.000 | |
| **Margen/unidad** | **+$6.200** | **+$41.000** | |

Conclusión falsa: "los Combos son un negoción, hay que vender más Combos".

**B) Método ABC — repartir por actividades**

Repartimos los $12.000.000 en 3 actividades y elegimos drivers:

| Actividad | Costo/mes | Driver | Total drivers | Costo por driver |
|---|---|---|---|---|
| Procesar pedidos | $3.000.000 | nº de pedidos | 600 pedidos | $5.000/pedido |
| Armar/setup | $5.000.000 | nº de setups | 250 setups | $20.000/setup |
| Soporte postventa | $4.000.000 | nº de consultas | 400 consultas | $10.000/consulta |

Consumo real (los Combos son intensivos en armado y soporte; las Cápsulas casi no):

| | Cápsulas | Combos |
|---|---|---|
| Pedidos | 500 | 100 |
| Setups | 50 | 200 |
| Consultas | 100 | 300 |
| Overhead asignado | 500×5.000 + 50×20.000 + 100×10.000 = **$4.500.000** | 100×5.000 + 200×20.000 + 300×10.000 = **$7.500.000** |
| Overhead por unidad (÷2.000 / ÷100) | $2.250 | **$75.000** |
| Costo directo/unidad | $9.000 | $35.000 |
| **Costo real/unidad** | **$11.250** | **$110.000** |
| Precio de venta/unidad | $20.000 | $100.000 |
| **Margen real/unidad** | **+$8.750** | **−$10.000** |

Verdad revelada: **cada Combo pierde $10.000.** Vendías 100 al mes → **−$1.000.000/mes regalado.**
Y las Cápsulas ganan más de lo que creías. El método viejo te empujaba justo al producto que te hundía.
(Para qué hacer con la línea que pierde, ver 92.)

## Costo por CLIENTE, no solo por producto

El mismo razonamiento aplica a clientes. Dos clientes te compran lo mismo, pero uno:
pide 8 veces al mes en pedidos chicos, pelea cada factura, exige despacho urgente y llama a soporte.
Ese cliente consume muchas más "actividades" → su costo de servir es altísimo aunque facture igual.

- Calcula **costo de servir** por cliente con los mismos drivers (pedidos, devoluciones, soporte, urgencias).
- Resultado típico: un puñado de clientes consume rentabilidad del resto. Opciones: subirles precio,
  ponerles mínimo de pedido, cobrar el extra (urgencia, personalización) o dejarlos ir educadamente.

## Del costo real al PRECIO (no es lo mismo)

El costo te dice el **piso**: por debajo, pierdes. El precio lo manda el **valor para el cliente** y el
mercado, no tu costo (ver 57 para fijación de precio por valor, y 53 para punto de equilibrio).

- Costo real → es tu **línea roja**. Nunca vendas por debajo salvo decisión estratégica consciente.
- Margen de contribución (precio − costo directo) → cuánto deja cada venta para pagar overhead (ver 53 y 58).
- Si un producto da margen real negativo: o subes precio, o le bajas el costo de actividad (menos
  setups, pedidos más grandes, automatizar soporte), o lo cortas. No lo dejes "porque da imagen" sin
  ponerle número a esa imagen.

## Errores comunes

- **Repartir overhead por ventas o por igual** → esconde justo los productos/clientes que pierden.
- **Costear una sola vez y nunca actualizar** → tus costos cambian; revisa cada 3-6 meses.
- **Confundir "vende mucho" con "deja mucho".** Volumen no es rentabilidad. Mide margen real.
- **Olvidar tu propio tiempo** como costo. Si te pagas $0, cualquier negocio "parece" rentable.
- **Querer un ABC perfecto** con 40 actividades. Empieza con 5-7 y mejora.
- **Dar costos/precios sin contexto de país:** impuestos, tarifas y costos laborales cambian todo.
  Pregunta país/ciudad primero y verifica cifras vigentes (cómo conseguir datos reales, ver 21).

## Siguiente paso típico

Toma tus 2-3 productos (o clientes) más distintos, lista 5 actividades de overhead, asígnales un driver
y calcula el costo real de cada uno este mes. Si alguno da margen negativo, decide ya: subir precio,
bajar su costo de actividad o cortarlo (ver 57, 53, 92).
