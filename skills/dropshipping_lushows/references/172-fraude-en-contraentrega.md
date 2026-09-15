# Fraude en contraentrega

> El COD no tiene contracargos, pero tiene su propia plaga: pedidos que nadie hizo, direcciones que
> no existen, competidores que te hacen quemar flete y clientes que piden lo mismo cinco veces para
> "escoger". Cada uno de esos te cuesta flete de ida **y** de vuelta (`163`).

## Los seis tipos

| Tipo | Cómo se ve | Costo |
|---|---|---|
| **Pedido falso / broma** | Datos inventados, teléfono apagado | Flete doble |
| **Sabotaje de competencia** | Muchos pedidos de golpe, mismo patrón, misma zona | Flete doble × N + inventario bloqueado |
| **Comprador serial que rechaza** | Mismo teléfono con historial de rechazos | Flete doble, repetido |
| **Dirección inexistente** | Calle o número que no existe | Flete doble + tiempo |
| **"No lo recibí"** (prepago) | Estado entregado, cliente lo niega | Producto + contracargo |
| **Robo en reparto** | Entregado a quien no era | Producto + reposición |

## Las señales, antes de despachar

| Señal | Peso |
|---|---|
| Teléfono con formato inválido o repetido en otros pedidos | Alto |
| Nombre obviamente falso o de una sola letra | Alto |
| Dirección sin número, sin referencias, o solo "casa blanca" | Alto |
| Correo desechable | Medio |
| Varios pedidos al mismo teléfono en minutos | **Alto** |
| Varios pedidos a la misma dirección con nombres distintos | Alto |
| Pedido de madrugada con datos incompletos | Medio |
| Cantidad muy por encima del promedio, sin razón | Medio |
| Zona con historial de rechazo alto | Medio (`173`) |
| Teléfono en tu lista negra | **Bloqueo** |

Ninguna señal sola condena. **Dos o más = confirmar sí o sí antes de despachar** (`160`).

## El filtro, por capas

| Capa | Qué hace | Costo |
|---|---|---|
| 1. Validación del formulario | Formato de teléfono, campos obligatorios, referencias | Cero |
| 2. Deduplicación | Mismo teléfono / dirección en las últimas 24 h | Cero |
| 3. Lista negra | Teléfonos con 2+ rechazos previos | Cero |
| 4. **Confirmación previa** | Lo resuelve casi todo (`160`) | Bajo |
| 5. Anticipo del flete | Para casos sospechosos o zona difícil | Baja conversión |
| 6. Revisión manual | Pedidos grandes o raros | Tiempo |

> La capa 4 hace el 80% del trabajo. Un defraudador rara vez contesta el WhatsApp de confirmación y
> casi nunca confirma un monto exacto por escrito.

## La lista negra: cómo se construye

1. Registra cada rechazo con **teléfono, nombre, dirección y motivo**.
2. Un rechazo: se marca, no se bloquea. Puede haber sido una emergencia real.
3. **Dos rechazos**: se exige prepago o anticipo del flete.
4. **Tres**: bloqueo.
5. Revisa la lista cada mes: el cliente que rechazó en marzo puede comprar bien en diciembre.

No es una lista de castigo, es una lista de **riesgo**. Al bloqueado se le ofrece prepago, no se le
cierra la puerta.

## Detectar el sabotaje de competencia

Patrón típico: 10-40 pedidos en pocas horas, misma ciudad, nombres verosímiles pero teléfonos que
no contestan, ticket idéntico, todos en horario de madrugada.

| Paso | Qué haces |
|---|---|
| 1 | **No despaches nada** hasta confirmar uno por uno |
| 2 | Revisa si los teléfonos comparten prefijo o patrón |
| 3 | Revisa el origen del tráfico: ¿vino de tu anuncio o de un enlace directo? |
| 4 | Si confirma cero de N, es sabotaje: cierra todos y guarda evidencia |
| 5 | Ajusta el formulario: campo de referencia obligatorio, límite por IP |

El daño real del sabotaje no es el flete: es que **bloquea tu inventario** en temporada y ensucia
tu píxel con conversiones falsas. Ver `facebook_ads_lushows`.

## Prepago: el otro fraude

En prepago no hay rechazos, hay **contracargos**. Tasa de referencia 0,3-1,5%.

| Defensa | Cómo |
|---|---|
| Prueba de entrega con nombre y fecha | Guardarla siempre (`156`) |
| Dirección de envío = dirección de facturación | Marcar la diferencia como riesgo |
| Descriptor de cobro reconocible en el estado de cuenta | Evita el contracargo por "no reconozco este cargo" |
| Respuesta rápida al cliente antes de que vaya al banco | El 60-70% de los contracargos empieza por no poder contactarte |
| Antifraude de la pasarela activado | Ver `192` |
| Conversación completa guardada | Evidencia |

**El contracargo más común no es fraude: es un cliente que no te pudo contactar.** Poner tu WhatsApp
visible en el inserto (`168`) y en el correo de confirmación previene más contracargos que
cualquier herramienta.

## Lo que no hay que hacer

| Error | Por qué |
|---|---|
| Acusar al cliente sin pruebas | Si te equivocaste, perdiste al cliente y ganaste una reseña |
| Bloquear una zona entera por 3 casos | Ver `173`: se mide, no se intuye |
| Despachar el sospechoso "por si acaso" | Es exactamente el pedido que va a fallar |
| No registrar los rechazos | Sin datos no hay lista negra ni aprendizaje |
| Poner tantos filtros que ahuyentas a los buenos | El filtro debe ser invisible para el cliente honesto |

## Métricas

| Métrica | Referencia | Alerta |
|---|---|---|
| Pedidos bloqueados por filtro | 2-6% | > 10%: filtro demasiado agresivo |
| Rechazos entre los confirmados | 12-25% | > 30%: la confirmación no está funcionando |
| Reincidentes | < 2% | Creciendo: falta lista negra |
| Contracargos (prepago) | 0,3-1,5% | > 1,5%: riesgo con la pasarela |

## Relacionados
`158` contraentrega · `159` tasa de entrega · `160` confirmación WhatsApp · `163` costo de los
rechazos · `173` zonas difíciles · `156` tracking · `192` pasarelas
