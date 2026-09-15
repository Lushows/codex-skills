# Confirmación por voz con IA

> WhatsApp confirma al que contesta mensajes. La llamada confirma al que no. Juntas empujan la tasa
> de entrega urbana al **70-85%**. La voz con IA sirve para lo que un humano hace mal: llamar a las
> 9:03, a las 13:40 y a las 19:15 del mismo día sin cansarse y sin cambiar de tono.

## Voz vs texto: cada uno a lo suyo

| | WhatsApp (`160`) | Llamada de voz |
|---|---|---|
| Costo por contacto | Muy bajo | Bajo con IA, alto con humano |
| Tasa de respuesta | 50-70% | 30-55% (contestan la llamada) |
| Velocidad de resolución | Minutos u horas | Segundos |
| Deja prueba escrita | **Sí** | Solo si grabas |
| Sirve para quien no usa WhatsApp | No | **Sí** |
| Maneja objeción compleja | Regular | Mejor |
| Se siente invasivo | Poco | Más |

**La secuencia que funciona:** WhatsApp primero (barato, deja rastro), llamada solo para los que
no respondieron en 3-4 horas. Llamar primero a todos es caro y molesta.

## Qué puede y qué no puede hacer la voz IA hoy

| Puede | No puede bien |
|---|---|
| Presentarse, decir producto, monto y dirección | Negociar precio |
| Preguntar sí/no y capturar la respuesta | Convencer a un indeciso duro |
| Corregir una dirección dictada | Entender audio con ruido de calle fuerte |
| Reprogramar el día de entrega | Manejar un cliente enojado |
| Reintentar a distintas horas | Improvisar fuera del guion |
| Escalar a humano | Sustituir a un buen vendedor |

Regla: la IA **clasifica y confirma**; el humano cierra lo difícil. Si la llamada se sale del
guion, escala. Ver `ventas_lushows` para el cierre.

## El guion de voz (30-45 segundos)

> "Hola, ¿hablo con {Nombre}? … Te llamo de {Tienda} por el pedido de {Producto} que hiciste
> {hoy/ayer}. Es para confirmarte el envío.
>
> El monto a pagar al recibir es de {monto}, y lo enviamos a {calle y número}. ¿Es correcto?
>
> Perfecto. ¿Te lo despachamos hoy para que llegue {rango de fechas}?
>
> Listo, {Nombre}. Te llega entre {fecha} y {fecha}. Te mandamos el número de guía por WhatsApp.
> Ten el teléfono a la mano ese día. Gracias."

Reglas del guion hablado:

1. Frases cortas. La gente cuelga con los párrafos.
2. El monto y la dirección **siempre**, textualmente.
3. Una pregunta a la vez, esperando respuesta.
4. Cerrar con la fecha y la acción del cliente ("ten el teléfono a la mano").
5. Nunca más de 60 segundos en el caso feliz.

## Cadencia de llamadas

| Intento | Cuándo | Si no contesta |
|---|---|---|
| 1 | 3-4 h después del pedido, si no respondió WhatsApp | Deja mensaje de voz corto + WhatsApp |
| 2 | Mismo día, franja distinta (mañana↔tarde) | WhatsApp con "te llamé" |
| 3 | Día siguiente en la mañana | **Cierra el pedido, no despachas** |

Tres intentos, dos días, y se acabó. Insistir más no sube la entrega: sube los reportes.

## Costo y punto de equilibrio

Los precios de las plataformas de voz IA cambian rápido: **verificar antes de contratar**. Lo que no
cambia es la aritmética de cuándo vale la pena.

```
Vale la pena si:   costo_por_llamada  <  margen_por_entregado × (puntos ganados / 100)
```

Ejemplo con los números del script de `159` (margen por entregado ~USD 4,89 al 78%): si llamar
agrega 6 puntos de entrega sobre 100 pedidos, ganas ~6 entregas más. El presupuesto disponible para
llamar a esos 100 pedidos es ese diferencial de margen. Corre tu propio caso con `159` antes de
firmar nada, y para la aritmética fina invoca `Matematicas_lushows`.

## Requisitos legales y de sentido común

| Punto | Qué hacer |
|---|---|
| Identificarse | La llamada dice el nombre de la tienda en la primera frase |
| Decir que es un asistente automatizado | Cada vez más exigido; además evita la sensación de engaño |
| Grabación | Si grabas, avísalo. Verificar la norma del país |
| Horario | Nunca antes de las 8:00 ni después de las 20:00 |
| No insistir | Si dice que no, se registra y no se vuelve a llamar |
| Datos personales | Tratamiento y conservación según la ley local. Verificar |

En Colombia y México hay normativa de protección de datos y de habeas data aplicable; verifica
con un profesional antes de escalar el volumen.

## Los errores que arruinan el canal

| Error | Consecuencia |
|---|---|
| Voz robótica sin naturalidad | Cuelgan en 5 segundos |
| Llamar antes de que el cliente reciba la confirmación escrita | "¿Quién es usted?" |
| Llamar desde un número distinto al de WhatsApp | Desconfianza |
| No capturar el resultado de la llamada | No puedes medir ni reintentar bien |
| Usarla para vender más en vez de confirmar | Molesta y baja la confirmación |
| Llamar a los que ya confirmaron por WhatsApp | Desperdicio puro |

## Métricas del canal

| Métrica | Referencia |
|---|---|
| Tasa de contacto (contestan) | 30-55% |
| Confirmación sobre contactados | 55-75% |
| Duración promedio | < 60 s |
| Escalados a humano | 10-20% |
| **Entrega de confirmados por voz** | Comparar contra confirmados por texto |

Lo último es la prueba real: si los confirmados por voz entregan igual o mejor que los de texto, el
canal funciona. Si entregan peor, tu IA está confirmando gente que en realidad dijo "mmm, bueno".

## Relacionados
`160` confirmación por WhatsApp · `162` reusar un bot propio · `159` tasa de entrega · `158`
contraentrega · `163` costo de los rechazos · invoca `ventas_lushows` y `Matematicas_lushows`
