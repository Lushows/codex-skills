# Atención al cliente que vende

> En una tienda de un producto, la atención **no es un costo de soporte: es el segundo canal de
> venta**. Entre el 15% y el 30% de las conversaciones previas a la compra terminan en pedido si se
> contestan rápido y bien. El resto de este módulo asume prepago; en COD la atención directamente
> es el cobro (`160`).

## Las tres funciones de la atención

| Función | Cuándo ocurre | Qué está en juego |
|---|---|---|
| **Cerrar** | Antes de comprar | La venta que ya pagaste con pauta |
| **Tranquilizar** | Entre la compra y la entrega | El contracargo (`282`) |
| **Recuperar** | Después de un problema | La reseña y la recompra (`284`, `285`) |

La mayoría de tiendas solo hace la segunda. Ahí pierden.

## La métrica que manda: tiempo de primera respuesta

| Tiempo hasta la 1ª respuesta | Qué pasa con la venta |
|---|---|
| < 5 minutos | Conversión máxima; el cliente sigue con la intención caliente |
| 5-60 minutos | Se mantiene buena parte |
| 1-4 horas | Cae fuerte; muchos ya compraron en otro lado o se les pasó |
| > 24 horas | La conversación está muerta y el riesgo de contracargo empieza |

**Estándar operativo:** primera respuesta < 30 min en horario hábil, < 2 h siempre, < 12 h fuera de
horario con autorespuesta honesta. Ver `279` para sostenerlo sin estar pegado al teléfono.

## Los 5 principios

1. **Responde la pregunta primero, vende después.** Nadie compra a quien esquiva.
2. **Un mensaje, una idea.** Bloques de 5 líneas máximo. Nada de párrafos.
3. **Nunca prometas una fecha que no controlas.** Da rangos y el rango más largo que manejas.
4. **El precio no se defiende, se enmarca.** Ver abajo.
5. **Si la respuesta es "no", dila rápido y con alternativa.** Las evasivas generan contracargos.

## La estructura de toda respuesta

```
1. Reconocer   → "Entiendo, [nombre]."
2. Responder   → el dato concreto, sin rodeos
3. Avanzar     → una pregunta o un siguiente paso claro
```

Tres partes. Siempre. Si te falta la 3, la conversación muere ahí.

## Cerrar antes de la compra

| Lo que escribe el cliente | Lo que está preguntando de verdad | Palanca |
|---|---|---|
| "¿Cuánto cuesta?" (y ya está el precio) | "¿Vale la pena?" | Valor + bundle (`218`) |
| "¿Es original?" | "¿Me van a estafar?" | Garantía + prueba social (`188`, `185`) |
| "¿Cuánto tarda?" | "¿Llega antes de X?" | Rango honesto + fecha de corte (`170`) |
| "¿Tienen tienda física?" | "¿Existen?" | Dirección fiscal, redes, reseñas |
| "Lo pienso" | "No me convenciste" | Preguntar qué duda queda |
| "¿Hay descuento?" | "Quiero sentir que gané" | Bundle o envío, no rebaja seca (`221`) |

> **El guion completo de objeciones, con la mecánica de descubrimiento, reencuadre y cierre, está en
> otra skill: invoca `ventas_lushows`.** Aquí solo va lo específico de ecommerce.

## Cómo enmarcar el precio sin bajarlo

| Técnica | Ejemplo aplicado |
|---|---|
| Unidad de uso | "Son $1.099 una sola vez; si lo usas dos veces por semana, sale a menos de $11 el uso en el primer año" |
| Comparación de gasto | "Es menos de lo que cuesta [alternativa recurrente] en dos meses" |
| Riesgo revertido | "Si no te funciona, tienes 30 días para devolverlo" (`188`) |
| Ascenso, no descuento | "Por $X más te llevas el kit de 2, que es como te lo recomendamos usar" (`218`, `219`) |
| Financiación | En México, MSI en Buen Fin cambia la conversación de precio a mensualidad (`195`) |

Regla dura: **nunca bajes el precio en el chat sin cambiar la oferta.** Bajar el precio sin contra-
partida enseña al mercado a regatear y destruye tu economía unitaria (`223`).

## Canales

| Canal | Fuerza | Debilidad | Cuándo |
|---|---|---|---|
| **WhatsApp** | Cierre, confianza, LatAm | Se sale de control sin sistema | Siempre en LatAm |
| Chat web | Captura al que está en la página | Se pierde si no hay nadie | Con bot (`279`) |
| Instagram/Facebook DM | Vienen del anuncio | Desordenado | Redirigir a WhatsApp |
| Correo | Rastro escrito, útil ante disputa | Lento | Confirmaciones, facturas, posventa |
| Teléfono | Máximo cierre en ticket alto | Caro | COD y reclamos graves |

## El registro: sin esto no hay atención, hay improvisación

Cada conversación deja tres datos mínimos: **número de pedido, motivo, resultado**. Con eso, cada
mes sacas el top 5 de motivos y atacas la causa en la página, no en el chat.

| Motivo frecuente | Causa real | Arreglo estructural |
|---|---|---|
| "¿Dónde está mi pedido?" | No comunicas el envío | Correos automáticos de tracking (`157`) |
| "¿Cuánto tarda?" (antes de comprar) | El plazo no está visible | Ponerlo en la página de producto (`180`) |
| "¿Es original?" | Falta prueba social | Reseñas, video real, garantía (`185`) |
| "Quiero cancelar" | Se arrepintió o se demoró | Acelerar despacho, mejorar expectativa |
| "Llegó dañado" | Empaque | `167` |

**Si un motivo supera el 20% de los mensajes, es un problema de tienda, no de atención.**

## Horario y expectativa

Publica el horario real y cúmplelo. Un horario claro con respuesta rápida dentro de él vale más que
un "24/7" que no cumples. Fuera de horario, autorespuesta que diga la hora exacta de respuesta.

| Zona | Horario recomendado |
|---|---|
| México | L-V 9:00-19:00, S 10:00-14:00 |
| Colombia | L-V 8:00-18:00, S 9:00-13:00 |

En temporada alta (`294`) se amplía y se refuerza: del 20 al 24 de diciembre la atención decide más
ventas que la pauta.

## Lo que nunca se hace

| Nunca | Por qué |
|---|---|
| Discutir con el cliente | Nunca ganas; ganas el contracargo en contra |
| Dejar de responder a alguien molesto | Es el camino directo a la disputa y a la reseña de 1 estrella |
| Prometer "mañana llega" sin guía confirmada | Rompes la confianza y disparas el reembolso |
| Copiar y pegar sin el nombre | Se nota, y se nota mal |
| Pedir que "borre la reseña" a cambio de algo | Riesgo de política de plataforma y de reputación (`284`) |

## Relacionados
`278` plantillas de respuesta · `279` automatizar con IA · `280` cliente molesto ·
`281` devoluciones · `282` contracargos · `284` reseñas · `285` posventa · `160` confirmación de
pedidos · `188` garantía · invoca `ventas_lushows` para el guion de objeciones
