# 54 — Del clic al cierre

Lee este módulo cuando tus campañas **traen clics pero no ventas** y sospechas que el problema no está en Google sino en lo que pasa **después** del clic: el lead llega y nadie lo atiende a tiempo, se pierde el rastro de qué anuncio lo trajo, o el equipo "cierra como puede" sin proceso. Google capta la intención; el dinero se gana — o se pierde — en el **handoff**: el momento en que el clic se vuelve conversación. Aquí montamos ese puente. El oficio de cerrar la conversación es ventas_lushows (esp. 82 WhatsApp); este módulo es la **plomería** que lleva al cliente hasta esa puerta sin perderlo en el camino.

## El embudo real no termina en el clic

La mayoría mide hasta el clic y se felicita. El embudo real es más largo, y cada salto pierde gente:

```
Impresión → Clic → Llega al destino → Inicia conversación → Responde a tu mensaje
→ Lead calificado → Propuesta → CIERRE (plata)
```

Google solo te muestra hasta "inicia conversación" (si está bien medido). Del cierre para atrás, **eres tú** quien tiene que devolverle el dato a Google con OCI (ver 53) para que optimice por lo que importa. Si mides solo clics, estás contando pasos, no ventas (ver 60 métricas, 64 ROAS-real). Una cuenta puede tener CTR envidiable y CPC barato y aun así **no facturar un peso** si el handoff se cae.

## Velocidad de contacto: la variable que más cierra

Si te quedas con una sola idea de este módulo, que sea esta: **la velocidad con que contactas al lead decide el cierre más que casi cualquier otra cosa.** Un lead contactado en los primeros 5 minutos cierra muchísimo más que el mismo lead contactado una hora después — la intención se enfría rápido, y el cliente ya le escribió a tu competencia mientras esperaba.

| Tiempo hasta el primer contacto | Qué pasa |
|---|---|
| < 5 min | Máxima probabilidad de cierre — el cliente sigue caliente |
| 5–30 min | Aún bueno, empieza a enfriarse |
| 30 min – 1 h | Cae fuerte; ya comparó con otros |
| > 1 h / al otro día | Casi muerto; "ya resolví, gracias" |

Por eso el handoff debe ser **automático e instantáneo**: lead form → webhook → WhatsApp del bot que responde en segundos (ver 52, y en este proyecto el bot ya contesta al instante y avisa al operador con `operatorNotifier` cuando hay intención de compra). Una llamada que no se contesta o un WhatsApp que responde "mañana" tira a la basura el clic que pagaste. La automatización no es lujo: es lo que hace rentable la pauta.

## Etiquetas, tiempos y captura del gclid

Para que el handoff no pierda información, tres cosas viajan con cada lead:

1. **El gclid** (ver 53): el hilo que conecta el clic con la venta. Se captura en la landing/formulario y se pega al lead. Sin esto no hay OCI, y sin OCI Google no aprende a traer compradores.
2. **La fuente/etiqueta:** de qué campaña, grupo y keyword vino. Sirve para saber **qué traer más** y qué cortar. Una **plantilla de seguimiento** (parámetros `utm_` en la URL: `utm_source=google&utm_campaign=...&utm_term=...`) deja que tu CRM/hoja sepa el origen sin adivinar.
3. **El timestamp:** cuándo entró, para medir tu velocidad de respuesta real y respetar la ventana de atribución (ver 16 atribución).

Flujo limpio:

```
Anuncio (?gclid + utm) → Landing puente (captura gclid+utm en campos ocultos)
→ WhatsApp/llamada con el lead etiquetado → CRM/customerMemory guarda gclid+utm+hora
→ Equipo cierra → marca "vendió" + valor → OCI sube a Google (ver 53)
```

Con esto cierras el círculo: Google trae al prospecto, tú lo atiendes en segundos, registras de dónde vino, cierras, y le devuelves la verdad a la máquina para que traiga más como ese.

## Define qué cuenta como conversión — y dónde

No todo clic ni todo "hola" es una conversión que valga optimizar. Decide la jerarquía:

| Evento | ¿Conversión para optimizar? | Cómo medirla |
|---|---|---|
| Clic al anuncio | No (es el costo) | Métrica nativa |
| Inicia chat / llama | Conversión "blanda" (señal temprana) | Conv. de WhatsApp / call tracking (ver 51) |
| Lead calificado | Conversión media | OCI con valor de etapa (ver 53) |
| Venta cerrada | **Conversión que manda** | OCI con valor real (ver 53, 96) |

Arranca optimizando por la **señal blanda** (hay volumen para que Smart Bidding aprenda — un negocio nuevo no tiene suficientes ventas para alimentar el algoritmo), y a medida que acumulas ventas, **mueve la optimización hacia la conversión que paga** vía OCI. Ese es el camino de una cuenta que madura (ver 15 pujas, 58). Regla de dedo: Smart Bidding necesita ~15-30 conversiones/mes del evento que optimizas para aprender bien; si la "venta" no llega a ese piso aún, optimiza por "inició chat" y migra cuando tengas datos.

El cierre en sí —qué decir, cómo manejar "está caro", cómo no perseguir ni rogar— no es Google: es ventas_lushows 82 (WhatsApp). Google entrega el prospecto caliente en la puerta; cruzarla es oficio de venta.

## Diagnóstico: ¿dónde se cae tu embudo?

Cuando "no vende", el problema vive en uno de tres tramos. Diagnostícalo con números antes de tocar la campaña:

| Síntoma | Dónde está el problema | Qué arreglar |
|---|---|---|
| Pocas impresiones / clics | Google: puja baja, keywords flojas, geo mal | Pujas, keywords, geo (ver 15, 20, 26) |
| Muchos clics, pocos chats/llamadas | Destino: landing lenta o que no engancha | Landing/oferta (desingweb-lushows) |
| Muchos chats, pocas ventas | Handoff o cierre: lento o sin proceso | Velocidad + venta (este módulo, ventas 82) |
| Vende pero la cuenta dice "0 conversiones" | Medición rota: gclid/OCI no montado | OCI (ver 53) |

El último es el más común y el más caro: la cuenta **sí** vende pero Google no lo sabe, así que optimiza mal y tú crees que "Google no sirve". Casi siempre es que falta capturar el gclid o subir la venta. Revisa la medición ANTES de culpar al tráfico.

## Errores comunes — blacklist

1. **Medir hasta el clic y declarar victoria.** El clic es el costo, no el resultado. Mide hasta la venta y devuélvela a Google con OCI (ver 53, 60).
2. **Contestar lento.** Bajo 5 minutos cierra; en una hora está muerto. Automatiza el handoff a WhatsApp instantáneo o quemas lo que pagaste.
3. **Perder el gclid en el camino.** Sin gclid no hay OCI y Google no aprende. Captúralo en la landing puente y pégalo al lead (ver desingweb-lushows).
4. **Handoff manual y desordenado.** "Copio el número y luego le escribo" se cae el día que hay volumen. Webhook → bot/CRM automático.
5. **No etiquetar la fuente.** Si no sabes qué campaña trajo al que cerró, escalas a ciegas. Usa `utm_` + plantilla de seguimiento.
6. **Optimizar por "inició chat" para siempre.** Es buena señal temprana, pero si nunca subes la venta real, te llenas de "holas" que no compran. Migra a la conversión que paga cuando tengas volumen (ver 53, 64).
7. **Culpar a Google por un cierre flojo.** Si el tráfico es bueno y no cierra, el problema es el handoff o la venta, no la keyword. Arregla el proceso (ventas_lushows 82) antes de subir presupuesto.
