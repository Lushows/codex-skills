# Investigar en AliExpress y 1688

Aquí no buscas ideas: buscas **el costo real** y **el proveedor real**. Una idea sin costo
verificado no es un candidato, es un deseo.

Advertencia central para 2026: el precio que ves en AliExpress **no es tu costo**. Tu costo es
"puesto en bodega" e incluye flete, arancel e IVA de importación. En México eso son +33,5% sobre
producto+flete para origen sin TLC desde 1-ene-2026, sin caducidad. Ver `16` y `48`.

## AliExpress: los filtros que importan

| Filtro | Configuración | Por qué |
|---|---|---|
| Ordenar por | **Número de órdenes**, no por relevancia | Órdenes = validación |
| Envío desde | Prueba con almacén local del país si existe | Cambia todo el costeo |
| Rango de precio | Define el máximo según tu múltiplo (`42`) | Evita perder tiempo |
| Calificación del vendedor | ≥ 95% positivo | Umbral mínimo |
| Fecha de la tienda | Tienda con ≥ 2 años | Menos riesgo de desaparición |

## Cómo leer la evolución de ventas

El dato de "X vendidos" es acumulado y no dice cuándo. Lo que sí sirve:

| Indicador | Dónde mirarlo | Lectura |
|---|---|---|
| Fecha de las reseñas más recientes | Pestaña de reseñas, ordenar por reciente | Si las últimas son de hace 4 meses: producto muerto |
| Densidad de reseñas por mes | Contar reseñas de los últimos 30 días | Creciente = despegando |
| Número de vendedores con el mismo SKU | Buscar la foto exacta | Muchos = validado y genérico |
| Aparición de variantes nuevas | El vendedor amplía colores/versiones | Señal de que vende |
| Reseñas con foto del cliente | Calidad real del producto | La foto oficial siempre miente un poco |

**Método de las reseñas con foto:** filtra solo reseñas con imagen y mira 20. Lo que veas ahí es lo
que va a llegarle a tu cliente. Si las fotos reales se ven mal, tu tasa de reembolso va a doler.

## Detectar al proveedor real

En AliExpress casi nadie fabrica: son revendedores de un fabricante en 1688. Detectarlo te puede
bajar el costo 30-50%.

```
1. Toma la foto principal del producto en AliExpress
2. Búsqueda por imagen en 1688.com (la lupa de la barra de búsqueda)
3. Compara precios: el de 1688 suele ser 30-60% menor
4. Mira el MOQ (cantidad mínima) y si el vendedor es 生产厂家 (fabricante) o 贸易商 (comerciante)
5. Verifica los años del vendedor y su tasa de repetición
```

1688 está en chino y no vende al exterior directamente: necesitas un **agente** que compre,
consolide y despache. Con capital menor a USD 500 y primera operación, el agente es prácticamente
obligatorio.

## AliExpress vs 1688 vs agente: cuándo cada uno

| Fuente | Cuándo usarla | Costo relativo | Riesgo |
|---|---|---|---|
| **AliExpress unidad suelta** | Solo para comprar **muestras** | Más caro | Bajo |
| **AliExpress lote** | 10-50 unidades, primera validación | Medio | Medio |
| **1688 vía agente** | 100+ unidades, producto ya validado | Más barato | Medio |
| **Proveedor local ya nacionalizado** | Stock local, reposición rápida | Más caro por unidad, más barato en total | Bajo |

Para el proyecto activo (México, capital <USD 500, prepago, diciembre), la respuesta es la cuarta
fila: **stock local**. Enviar desde China directo al cliente pierde USD 18 por venta y los tiempos
de 25-35 días matan diciembre. AliExpress y 1688 sirven aquí para **conocer el costo de referencia y
negociar con el proveedor mexicano**, no para operar. Ver `128`.

## Las preguntas obligatorias al vendedor (copia y pega)

```
1. ¿Cuál es el precio a 50 / 100 / 300 unidades?
2. ¿Medidas y peso exactos del producto EMPACADO?
3. ¿Medidas del master carton y cuántas unidades trae?
4. ¿Tiene certificación [la que aplique] y puede enviarme el documento?
5. ¿Cuánto tarda la producción si pido 300 unidades?
6. ¿Puede enviar una muestra? ¿Costo?
7. ¿Puede poner mi logo / empaque personalizado? ¿Desde qué cantidad?
8. ¿Tiene stock en [México / Colombia / España] o solo en China?
```

La pregunta 8 es la que más gente olvida y la que más plata vale en 2026: muchos proveedores chinos
ya tienen almacén en México. Eso te elimina el 33,5% de tu ecuación por unidad.

## Banderas rojas del proveedor

| Bandera | Qué significa |
|---|---|
| Responde con traducción automática incoherente y sin datos | Revendedor sin control del producto |
| No da peso ni medidas del empacado | No lo ha enviado nunca en volumen |
| Precio 40% por debajo de todos los demás | Producto distinto al de la foto |
| Fotos robadas de otra marca | Riesgo de propiedad intelectual (`43`) |
| Se niega a mandar muestra | Cierre inmediato de la conversación |
| Presiona con "última oportunidad" | Táctica; el producto no tiene demanda |

## El costeo que debes armar (plantilla)

| Renglón | Cómo se obtiene |
|---|---|
| Precio unitario a tu cantidad | Cotización por escrito |
| Flete internacional por unidad | Peso facturable × tarifa del agente ÷ unidades (`48`) |
| Arancel + IVA de importación | Según país y partida (`13`, `16`, `17`) |
| Manejo / desaduanaje prorrateado | Cotización del agente |
| **= COSTO PUESTO EN BODEGA** | La cifra que usas en el múltiplo (`42`) |

Si haces el múltiplo con el precio de AliExpress solo, lo estás inflando 25-40%. Es el error #1 de
esta parte del proceso.

## La regla de las 3 cotizaciones

Nunca compres con una sola. Tres vendedores distintos del mismo SKU te dan:
1. El rango real de precio (y quién te estaba inflando).
2. Un plan B cuando el producto pegue y el primero se quede sin stock.
3. Poder de negociación real, porque puedes citar el precio del otro.

Es también el criterio 11 del filtro no negociable. Ver `41`.

## Muestras: no es opcional

| Para qué sirve la muestra | Valor |
|---|---|
| Test de caída (`48`) | Evita 12% de rotura en el lote entero |
| Grabar tu propio creativo | Videos originales convierten mejor que los del proveedor |
| Verificar peso y medidas reales | El proveedor a veces redondea a su favor |
| Confirmar calidad percibida | Decide si el ticket de 1.099 MXN es defendible |

Costo típico de una muestra con envío exprés: USD 15-40. Es el mejor dinero que vas a gastar.

## Relacionados
`13` mapa aduanero · `16` arancel México · `41` criterios · `42` múltiplo mínimo ·
`48` peso y fragilidad · `50` método · `53` Amazon · `56` Temu · `128` proveedores en México
