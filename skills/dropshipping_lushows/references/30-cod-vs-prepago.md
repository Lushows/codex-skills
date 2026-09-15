# COD vs prepago: la decisión estructural

> No es una preferencia de cobro. Es **la decisión que define qué producto puedes vender, con qué
> proveedor, con cuánto capital y a qué velocidad creces**. Se toma antes que el producto.

## Las dos máquinas

| | **COD (pago contra entrega)** | **Prepago (paga en la web)** |
|---|---|---|
| Qué vendes | Impulso, precio bajo-medio, categorías de "quiero verlo" | Cualquier cosa, incluido ticket alto |
| Quién compra | Sin tarjeta, sin confianza en internet, LatAm popular, Asia | Bancarizado, urbano, comprador habitual |
| Riesgo | **Tuyo** hasta que el cliente abre la puerta | **Del cliente** desde el clic |
| Qué financias | El inventario y el flete de ida **y de vuelta** | Nada |

## Tabla comparativa completa

| Variable | COD sin confirmación | COD confirmado | COD urbano confirmado | Prepago |
|---|---|---|---|---|
| **Conversión en la página** | **6-9%** | 6-9% | 6-9% | **2-4%** |
| **Tasa de cobro / entrega** | **45-60%** | 65-78% | **70-85%** | **95-98%** |
| Conversión efectiva (venta cobrada) | 3,2-4,7% | 4,2-6,3% | 4,5-7,0% | 1,9-3,9% |
| **Días hasta tener la plata** | 10-18 | 10-15 | **~12** | **~3** |
| Vueltas de caja / 75 días | ~5 | ~6 | **6,2** | **25** |
| Capital para operar | **Alto** | Alto | Alto | **Bajo** |
| Costo de un pedido fallido | flete ida + vuelta + confirmación | idem | idem | producto + flete perdidos, rara vez |
| Compatible con proveedor a 15 días | **No** (ver `31`) | No | No | **Sí, con matices** |
| Fraude / pedidos falsos | Alto | Medio | Medio-bajo | Casi nulo (hay contracargos) |
| Contracargos | No existen | No existen | No existen | **Sí: 0,3-1,5%** |
| Curva de aprendizaje del píxel | Sucia (optimiza por pedidos que no se cobran) | Sucia | Media | **Limpia (optimiza por compra real)** |
| Dónde funciona mejor | CO, PE, EC, MX interior, PH, IN | idem | CDMX/GDL/MTY, Bogotá, Lima | MX urbano, ES, CL, US, UK, PL |

> Las tasas de entrega son las verificadas: sin confirmación 45-60%, con confirmación previa 65-78%,
> urbano con confirmación por WhatsApp o voz IA 70-85%, y CDMX/GDL/MTY con 99minutos ~78%.

## El error de leer solo la conversión

El COD convierte **dos a tres veces más** en la página. Eso es real y por eso todo el mundo lo
recomienda. Pero la conversión no es lo que te pagan.

```
Prepago:  CVR 3,0%  ×  cobro 97%  =  2,91% de visitantes que te dejan plata
COD:      CVR 6,5%  ×  cobro 52%  =  3,38% de visitantes que te dejan plata
```

Parece que gana el COD. Ahora mete el costo de los que **no** pagaron: cada pedido no entregado te
cuesta flete de ida, flete de retorno y la llamada de confirmación. En México ese costo hunde el
COD sin confirmación por debajo del prepago, y en el modelo verificado del proyecto la utilidad
queda así:

| Configuración México | Ticket USD | Entrega | Utilidad/venta | Caja |
|---|---|---|---|---|
| Prepago bundle 1.099 + MSI | 60,05 | 97% | **20,18** | 3 días |
| COD 1.099 confirmado | 60,05 | 78% | 19,87 | 12 días |
| COD 699 confirmado | 38,20 | 78% | 4,11 | 12 días |
| Prepago 699 | 38,20 | 97% | 2,63 | 3 días |

**La utilidad por venta es casi empate en ticket alto. La caja no.** Prepago devuelve el dinero en
3 días (25 vueltas de temporada) y el COD en 12 (6,2 vueltas). Con capital chico eso no es un
matiz, es el negocio entero. Ver `32`.

## Qué te obliga a elegir COD

1. Tu mercado **no está bancarizado** y el prepago te deja fuera del 60% de la demanda.
2. Tu producto se vende por impulso en un rango de precio donde nadie saca la tarjeta.
3. Estás en un país donde la pasarela no te acepta como extranjero.
4. La plataforma que te da el stock (Dropi y similares) **solo opera COD**. Ver `132`.

## Qué te obliga a elegir prepago

1. **Tu proveedor está lejos.** Si el cliente espera más de una semana, el COD se cae. Ver `31`.
2. Capital menor a US$1.000: no puedes financiar 12 días de flotante multiplicado por cada pedido.
3. Ticket alto: nadie manda a un mensajero con MXN 1.099 en efectivo sin fricción.
4. Quieres que el píxel aprenda con datos limpios. El algoritmo optimiza por lo que le reportas;
   si le reportas pedidos que nunca se cobraron, te trae más gente que no paga.
5. Quieres vender con **meses sin intereses** — imposible en efectivo, y en México el MSI sube la
   conversión ~36%. Ver `195`.

## El híbrido: lo que hacen los que ganan

**Ofrece ambos, empuja el prepago con incentivo.**

| Palanca | Efecto típico | Costo |
|---|---|---|
| Descuento 5-10% por pagar en línea | Migra 20-40% de los COD | El descuento |
| Envío gratis solo en prepago | Migra 15-30% | El flete |
| Regalo extra visible solo al pagar en línea | Migra 10-25% | Costo del regalo |
| COD con recargo explícito ("manejo de efectivo") | Migra 15-35% | Fricción, cuidado |

Cada punto que migras de COD a prepago te devuelve caja nueve días antes. En una temporada de 55
días eso es literalmente más inventario girando.

## Reglas duras

| Situación | Regla |
|---|---|
| Proveedor a >7 días del cliente | **Prepago o nada.** Ver `31` |
| Capital < US$500 | **Prepago.** El COD te deja sin caja en la semana 2 |
| COD sin confirmación previa | **Prohibido.** 45-60% de entrega no es un negocio, es una donación |
| COD en zona rural | Solo con margen por encima del 60% |
| Black Friday / Buen Fin con COD | Cuidado: el pico de pedidos te congela toda la caja justo cuando necesitas reinvertir |

## Cómo decide el proyecto activo

Tienda en México para diciembre 2026, capital menor a US$500, **stock local, nunca China directo**:

```
COD  →  descartado. No por la utilidad (es parecida), sino por la caja:
        6,2 vueltas contra 25. Con US$500 la velocidad ES el capital.
Prepago cerrando en página web, bundle ~1.099 MXN, MSI activos en Buen Fin.
Techo de CAC 30,73 · CAC esperado 10,54 · holgura 2,92x · ROAS de equilibrio 1,95.
```

## Los números que debes medir desde el día uno

| Métrica | Dónde se rompe | Qué hacer |
|---|---|---|
| Tasa de entrega COD | < 65% | Confirmar antes de despachar o cerrar zonas |
| % de pedidos prepago sobre el total | < 30% en híbrido | Subir el incentivo |
| Días de flotante reales | > 15 | Renegociar con la transportadora o cambiar de modelo |
| Contracargos (prepago) | > 1,5% | Revisa la promesa del anuncio: estás vendiendo humo |

Cómo se cobra y se concilia cada modelo: `192` (pasarelas), `160` (confirmación).
La mecánica de la campaña que lleva tráfico a cada modelo: **invoca `facebook_ads_lushows`**.

## Relacionados
`31` por qué COD y China son incompatibles · `32` velocidad de rotación de caja · `20` playbook
México · `132` Dropi · `159` tasas de entrega · `160` confirmación de pedidos · `192` pasarelas ·
`195` meses sin intereses
