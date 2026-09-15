# Evaluar a un proveedor

> Vigencia: septiembre 2026. Método de evaluación; aplica a China, México, Colombia o España.

Evaluar un proveedor no es "ver si tiene buenas reseñas". Es responder cuatro preguntas: **¿existe?
¿fabrica o revende? ¿aguanta mi volumen? ¿qué pasa cuando algo sale mal?**

## Las cuatro capas de verificación

| Capa | Qué verificas | Costo | Cuándo |
|---|---|---|---|
| 1. Existencia | Que la empresa sea real y esté vigente | Gratis | Siempre |
| 2. Naturaleza | Fábrica vs trading company | Gratis | Siempre |
| 3. Capacidad | Que aguante tu volumen y calidad | US$30-150 (muestras) | Antes del lote |
| 4. Comportamiento | Cómo responde bajo presión | Un pedido chico | Antes de escalar |

Casi todo el mundo hace la 1 y salta a comprar. El desastre vive en la 3 y la 4.

## Capa 1 — ¿Existe?

1. Pide la **licencia comercial (营业执照)** en foto. Debe traer: nombre legal en chino, número de
   registro unificado (18 dígitos), capital registrado, fecha de constitución, alcance de operación.
2. Contrasta el **nombre legal** con el de la cuenta bancaria a la que te piden pagar. **Si no
   coinciden, para.** Ver `141`.
3. Busca el nombre legal en el registro público chino (National Enterprise Credit Information
   Publicity System). Un agente te lo verifica en minutos.
4. Antigüedad: **menos de 2 años = riesgo alto** para un primer pedido grande.
5. Capital registrado bajo (ej. ¥100.000) no descalifica, pero indica estructura pequeña.

Para proveedores locales: verifica RFC (México), NIT/RUES (Colombia), CIF (España). Para el análisis
tributario y de formalidad invoca `contador_lushows`.

## Capa 2 — ¿Fábrica o comercial?

| Prueba | Fábrica real | Trading company |
|---|---|---|
| Alcance de la licencia (经营范围) | Incluye 生产/制造 (producción) | Solo 销售/贸易 (venta) |
| Video en vivo de la línea, hoy, sin aviso | Lo manda en 10 minutos | "Mañana", "el jefe no está" |
| Catálogo | Una categoría profunda | Muchas categorías inconexas |
| Ubicación | Coincide con el clúster. Ver `110` | No coincide |
| Pregunta técnica específica (gramaje, tonelaje de la inyectora, número de líneas) | Responde con números | Responde con generalidades |
| Precio de molde | Sabe cuánto cuesta y por qué | "Te averiguo" |
| Fotos del producto | Propias, con su piso de fábrica | De catálogo, iguales a otras 30 tiendas |

**No siempre quieres fábrica.** Una buena trading company te consigue MOQ menor, gestiona varios
proveedores y te resuelve el 80% de los problemas. Lo que no puedes es **pagar precio de fábrica y
recibir servicio de intermediario sin saberlo.**

## Capa 3 — ¿Aguanta?

1. **Muestras de 3 proveedores** con la misma especificación. Ver `124`.
2. Evalúalas contra una **lista escrita antes de recibirlas**: material, peso real, medidas con
   calibrador, acabado, funcionamiento, empaque, olor.
3. Pesa y mide **tú mismo**. El 30% de las fichas técnicas mienten en peso, y el peso es flete.
4. Pregunta **capacidad mensual del SKU**. Si tu pedido es más del 30% de su capacidad mensual, vas a
   sufrir en temporada alta.
5. Pregunta **quiénes son sus otros clientes** por región. Si ya exporta a LatAm, sabe de documentos.
6. Pide **certificaciones** si tu producto las requiere. Ver `143`.

## Capa 4 — ¿Cómo se comporta?

Solo se ve con un pedido real chico. Qué observar:

| Comportamiento | Lectura |
|---|---|
| Avisa de un retraso **antes** de la fecha | 🟢 Excelente. Es el mejor predictor de todo |
| Avisa el día de la fecha | 🟡 Normal |
| No avisa y tú preguntas | 🔴 Va a pasar siempre |
| Manda fotos de producción sin que las pidas | 🟢 Proactivo |
| Acepta el error y repone rápido | 🟢 Socio |
| Discute cada defecto, pide "pruebas" infinitas | 🔴 Cambia de proveedor |
| Sube el precio después de confirmar la PI | 🔴 Crítico |
| El peso facturado supera el cotizado en >10% | 🟠 Verifica: puede ser error o puede ser sistema |

## Matriz de puntuación (úsala, no la improvises)

| Criterio | Peso | 1-5 |
|---|---|---|
| Verificación legal completa | 15% | |
| Fábrica vs comercial (según lo que necesitas) | 10% | |
| Calidad de la muestra vs especificación | **25%** | |
| Precio competitivo (vs 8 cotizaciones) | 15% | |
| Lead time y cumplimiento | 10% | |
| Velocidad y claridad de comunicación | 10% | |
| Capacidad de personalizar | 5% | |
| Certificaciones y documentación | 10% | |

Corte: **menos de 3,5 sobre 5 ponderado = no**. Y la muestra pesa 25% por una razón: es el único
dato que no es una promesa.

## Las 8 preguntas que revelan más

1. ¿Cuál es su capacidad mensual de **este** SKU?
2. ¿Cuál es su tasa de defectos interna y cómo la miden?
3. ¿Qué hacen con las unidades que no pasan el control?
4. ¿Cuánto tarda una reposición si rechazo 10% del lote?
5. ¿A qué países exportan más y desde hace cuánto?
6. ¿Qué pasa si el tipo de cambio o la materia prima suben durante la producción?
7. ¿Aceptan inspección de tercero antes del saldo?
8. ¿Cuál es el nombre legal de la cuenta bancaria receptora?

La 7 y la 8 son eliminatorias. Quien dice no a la inspección tiene algo que esconder; quien pide pago
a una cuenta de nombre distinto es riesgo de fraude. Ver `123`, `141`.

## Señales de que debes irte, aunque el precio sea bueno

| Señal | Gravedad |
|---|---|
| Nombre de cuenta bancaria distinto al legal | 🔴 |
| Se niega a inspección de tercero | 🔴 |
| Vende producto con marca registrada de otro | 🔴 Ver `142` |
| Presiona con "el precio sube mañana" | 🟠 |
| Cambia la especificación después de la PI | 🟠 |
| No manda muestra "porque es igual a la foto" | 🟠 |
| Responde solo por audio y nunca por escrito | 🟡 |
| El precio está 40% bajo el resto del mercado | 🟠 Algo se recortó |

## Errores frecuentes

| Error | Realidad |
|---|---|
| Confiar en el sello "Verified Supplier" | Verifica instalaciones, no tu producto. Ver `113` |
| Evaluar por precio primero | El precio se negocia; la capacidad no |
| Una sola muestra | Sin comparación no tienes criterio |
| No pesar la muestra | El peso es flete y el flete es margen. Ver `121` |
| Saltarse la capa 4 | Todo proveedor se ve bien hasta el primer problema |

## Para el proyecto activo (México, diciembre 2026)

Aplica las cuatro capas al **mayorista mexicano**: verifica RFC, pide factura (sin factura no hay
deducción ni respaldo), compra una muestra, y haz un pedido chico antes de comprometer inventario.
Con Dropi MX la capa 1-2 la absorbe la plataforma, pero la 3 y la 4 siguen siendo tuyas: **pide un
producto a tu propia casa antes de venderlo.** Ver `128`, `132`, `144`.

## Relacionados
Ver `110`, `113`, `117`, `118`, `123`, `124`, `141`, `142`, `143`, `144`.
