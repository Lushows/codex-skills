# Envío gratis y cómo pagarlo

## No existe el envío gratis

El flete lo paga alguien. Las únicas tres opciones son:

| Opción | Quién paga | Efecto en CVR | Efecto en techo de CAC |
|---|---|---|---|
| Envío cobrado aparte | el cliente | baja (fricción en checkout) | neutro |
| Envío "gratis" con precio ajustado | el cliente, sin verlo | alta | neutro si ajustaste bien |
| Envío gratis sin ajustar precio | **tú** | alta | se hunde |

La tercera es la que quiebra tiendas. El flete en México son ~USD 8,74 por pedido: si lo absorbes
sin subir el precio, el techo de CAC cae de USD 30,73 a USD 21,99 y la holgura de 2,92x a 2,09x.

## El costo de sorprender al cliente con el flete

El flete revelado en el último paso es la causa #1 de carrito abandonado en LatAm. El cliente hizo
la cuenta con un número y le cambiaste el número. La conversión cae; el CAC sube proporcionalmente.

```
Si la CVR cae de 3,0% a 2,4% (−20%), el CAC sube 25%:
CAC 10,54 → 13,18  ·  holgura 2,92x → 2,33x
```

Eso cuesta más que el flete mismo.

## Las 4 estructuras que funcionan

### 1. Envío incluido en el precio (recomendada para ticket ≥ USD 50)

```
Precio mostrado: 1.099 MXN — envío incluido
Adentro:         1.099 = producto + flete + margen
```

Ventajas: cero fricción, un solo número, se comunica como beneficio.
Requisito: el ticket debe aguantar el flete. Con USD 60,05 de ticket, USD 8,74 son el 14,6%. Con
USD 38,20 son el 22,9% — ahí ya duele.

### 2. Umbral de envío gratis (la que sube el ticket)

```
"Envío gratis desde 899 MXN"
```

| Efecto | Detalle |
|---|---|
| Sube el ticket promedio | el cliente agrega para alcanzar el umbral |
| Preserva margen en pedidos pequeños | ahí sí cobras flete |
| Empuja hacia el bundle | el umbral se fija justo debajo del bundle |

**Regla del umbral:** fíjalo entre 1,2x y 1,5x tu ticket promedio actual, y justo por debajo del
precio del bundle que quieres vender. Si tu bundle es 1.099, el umbral en 899-999 hace que la
opción suelta de 699 se sienta incompleta.

### 3. Envío cobrado explícito y barato

```
Producto 699 + envío 99 = 798
```

Funciona en tickets bajos y en mercados acostumbrados (Mercado Libre educó al mercado mexicano en
ambas direcciones). Hay que mostrarlo **desde la página de producto**, no en el checkout.

### 4. Envío gratis condicionado a prepago (útil donde conviven COD y prepago)

```
"Paga con tarjeta: envío gratis. Contraentrega: +79 de gestión."
```

Empuja al prepago, que devuelve el dinero en ~3 días contra ~12 del COD (`234`) y no carga el costo
de los fallidos. Ver `30`.

## Cómo saber si tu precio aguanta el envío incluido

```
flete como % del ticket = flete ÷ ticket
```

| % del ticket | Veredicto |
|---|---|
| < 10% | envío incluido sin pensarlo |
| 10-18% | envío incluido, pero verifica holgura (`228`) |
| 18-25% | necesitas subir ticket (bundle) o cobrar envío |
| > 25% | el producto probablemente no sirve para este modelo (`41`) |

México bundle: 8,74 ÷ 60,05 = **14,6%** → envío incluido, correcto.
México suelto: 8,74 ÷ 38,20 = **22,9%** → aquí el flete es el problema.

## El envío gratis también hay que pagarlo en los fallidos

En contraentrega, el pedido fallido cuesta flete de ida **y** de vuelta. Con tasa de cobro del 78%:

```
desperdicio = (1 − 0,78) ÷ 0,78 = 0,282
costo de fallidos por venta buena = 0,282 × (8,74 × 2) = USD 4,93
```

Con 52% de cobro, el desperdicio es 0,923 y el costo sube a **USD 16,14 por venta buena**. Eso solo
en flete. Ver `229` y `30`.

En prepago reembolsado pierdes producto + flete, no flete doble:

```
costo de fallidos por venta buena = desperdicio × (costo puesto en bodega + flete)
```

## Velocidad de entrega: el otro lado del flete

| Modelo | Tiempo típico | Efecto |
|---|---|---|
| Envío directo desde China | 12-30 días | CVR baja, reembolsos altos, reseñas malas |
| Stock local (bodega en el país) | 2-5 días | CVR alta, reembolsos bajos |

El stock local cuesta capital inmovilizado, pero mueve el denominador entero de la ecuación de
valor (`211`) y baja los fallidos. En temporada de diciembre, **entregar tarde es no entregar**:
un pedido de regalo que llega el 27 es un reembolso. Ver `145` y `238`.

## Comunicación en la página

| Dónde | Qué debe decir |
|---|---|
| Arriba, junto al precio | "Envío incluido" o "Envío gratis desde X" |
| Bajo el botón de compra | plazo real de entrega en días |
| Barra superior | "Entrega en 2-4 días · Envío incluido" |
| Checkout | el mismo número que prometiste arriba, sin sorpresas |

Prometer un plazo que no cumples no es marketing: es la fábrica de reembolsos y disputas.

## Aplicación México dic-2026

Envío incluido en el bundle de 1.099 MXN (14,6% del ticket), umbral de envío gratis en 899 MXN para
empujar hacia el bundle, y plazo real de 2-4 días con stock local. Fecha límite de compra para
entrega antes del 24 de diciembre publicada en la página desde el 1 de diciembre.

## Relacionados
`30` · `41` · `145` · `211` · `216` · `218` · `220` · `221` · `228` · `229` · `234` · `238`
