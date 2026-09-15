# La operación diaria

> Una tienda de un producto con 10-40 pedidos al día se opera en **90 minutos bien puestos**, no en
> 10 horas de mirar el panel. Lo que mata no es el trabajo: es el trabajo desordenado, hecho a
> deshoras, y la costumbre de tocar la campaña cada vez que entras.

## La regla que sostiene todo

**Mirar no es operar.** Cada vez que abres el administrador de anuncios fuera de la ventana
asignada, la probabilidad de que toques algo sube. Y tocar antes de tiempo es la causa #1 de matar
campañas que iban a funcionar. Ver `268` y `297`.

Tres ventanas fijas al día. Fuera de ellas, el teléfono no se abre para la tienda.

## El día, hora por hora

| Hora | Ventana | Duración | Qué haces |
|---|---|---|---|
| 08:00-08:45 | **Mañana: la verdad de ayer** | 45 min | Cierre de ayer, pedidos, mensajes de la noche, decisiones de pauta |
| 13:30-14:00 | **Mediodía: solo operación** | 30 min | Pedidos al proveedor/3PL, mensajes, incidencias. **No se toca la pauta** |
| 20:00-20:15 | **Noche: solo semáforo** | 15 min | Gasto del día, algo roto, mensajes pendientes. Ninguna decisión |

En temporada alta (`294`) se agrega una ventana 17:00-17:20 para stock y corte logístico.

## Ventana 1 — La mañana (45 min)

Orden fijo. No lo cambies, porque el orden evita que las emociones de la pauta contaminen la
operación.

### 1. Caja y pedidos (10 min)
| Reviso | Qué busco | Umbral de alarma |
|---|---|---|
| Pedidos de ayer | Cantidad vs promedio de 7 días | Caída >40% sin causa |
| Pedidos sin pagar / sin confirmar | Que no se queden ahí | >2 con más de 12 h |
| Pedidos sin etiqueta de envío | Todo lo de ayer debe salir hoy | cualquiera con >24 h |
| Saldo de pasarela | Que los depósitos lleguen | depósito atrasado >1 día |
| Pedidos con marca de riesgo | Fraude (`283`) | cualquiera |

### 2. Bandeja de entrada (15 min)
Todo mensaje de más de 12 horas es una urgencia. Ver `277` y `278`. Meta de respuesta: **menos de
2 horas en horario hábil**. No porque sea lindo, sino porque el silencio es la causa #3 de
contracargo (`282`).

### 3. Números de pauta (10 min)
Solo estos, solo de ayer y de los últimos 3 días acumulados. Nada de horas sueltas. Ver `266`.

| Número | De dónde | Qué hace que actúes |
|---|---|---|
| Gasto | Ads | Se pasó del plan |
| Compras (pixel) vs pedidos reales (tienda) | Ambos | Diferencia >15% → revisar CAPI (`200`, `201`) |
| CPA | Ads | Por encima del techo de CAC (`11`) 3 días seguidos |
| ROAS | Ads | Por debajo del de equilibrio (`226`) 3 días seguidos |
| CTR y CPM del creativo nuevo | Ads | CTR <1% con 2.000 impresiones → creativo muerto |

### 4. Decisión del día (5 min)
Una sola. Escrita. Ejemplos válidos: "subo 20% el conjunto A", "mato el creativo 7", "no hago nada".
"No hago nada" es una decisión legítima y es la correcta la mayoría de los días.

### 5. Creativo (5 min)
Anotar qué creativo se produce esta semana. Sin producción no hay negocio (`262`).

## Ventana 2 — Mediodía (30 min)

| Tarea | Detalle |
|---|---|
| Enviar pedidos | Al 3PL, al proveedor o a empaque propio. **Corte diario a hora fija** |
| Actualizar trackings | Los que ya tienen guía, al cliente (`156`, `157`) |
| Incidencias logísticas | Paquetes detenidos >48 h, direcciones malas (`165`, `171`) |
| Mensajes nuevos | Segunda pasada |
| Stock | Unidades restantes vs días de venta a ritmo actual |

**Aquí no se toca la pauta.** Si a las 14:00 el día "va mal", es porque el día no ha terminado.

## Ventana 3 — Noche (15 min)

Solo semáforo, cero decisiones:

- ¿Gastó lo que debía? ¿Se detuvo alguna campaña sola?
- ¿Hay mensajes sin responder? (responder o programar respuesta automática de "mañana a las 8")
- ¿Se cayó la tienda, la pasarela o el dominio?
- ¿Entró algún contracargo o disputa?

Si algo está rojo, se anota. Se resuelve mañana 08:00, salvo tienda caída o pasarela caída, que son
las dos únicas emergencias reales.

## La semana

| Día | Bloque extra | Duración |
|---|---|---|
| Lunes | Cierre de la semana anterior en el tablero (`276`) + decisión de presupuesto | 45 min |
| Martes | Producción de creativos (grabar/editar lote) (`253`, `262`) | 2-3 h |
| Miércoles | Subir creativos nuevos a testeo (`265`) | 30 min |
| Jueves | Inteligencia: biblioteca de anuncios, competidores (`107`, `109`) | 45 min |
| Viernes | Proveedor: reposición, tiempos, pagos (`137`, `140`) | 30 min |
| Domingo | **Nada.** Descanso operativo | — |

## Lo que NO se hace en el día

| Tentación | Por qué no |
|---|---|
| Revisar ventas cada 30 minutos | No cambia el resultado, cambia tus decisiones |
| Apagar un anuncio porque "lleva 4 horas sin vender" | El ruido de un día es enorme; se decide con 3 días o 2× CAC gastado (`268`) |
| Rediseñar la tienda porque hoy vendió poco | El 80% de los problemas de "hoy vendió poco" son de creativo, no de página |
| Contestar mensajes a las 23:00 | Fijas expectativa de atención 24/7 que no vas a sostener |
| Cambiar presupuesto dos veces el mismo día | Reinicia aprendizaje (`269`) |

## Cuando la tienda crece

| Pedidos/día | Cómo cambia el día |
|---|---|
| 0-10 | Las 3 ventanas, tú solo. 90 min |
| 10-40 | Igual, pero la atención empieza a comerse la mañana → automatiza (`279`) |
| 40-100 | Alguien de atención medio tiempo (`288`, `289`). Tú: pauta, creativo, números |
| 100+ | Atención dedicada + 3PL + editor de creativos (`290`). Tú: producto, oferta, dinero |

## Checklist imprimible de la mañana

- [ ] Pedidos de ayer contados y comparados con el promedio de 7 días
- [ ] Ningún pedido de ayer sin etiqueta
- [ ] Bandeja en cero o con respuestas programadas
- [ ] Pedidos marcados como riesgo, revisados
- [ ] Gasto, CPA y ROAS de 3 días anotados en el tablero
- [ ] Diferencia pixel vs tienda menor al 15%
- [ ] Una decisión escrita (puede ser "nada")
- [ ] Creativo de la semana definido

## Relacionados
`276` el tablero del operador · `277` atención que vende · `279` automatizar con IA · `266` métricas
que importan · `268` cuándo matar una campaña · `294` temporada alta · `297` errores que matan
tiendas · `298` el plan de 90 días
