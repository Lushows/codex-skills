# Pasarelas de pago en Colombia y LatAm

> Vigencia: 14-sep-2026. **Comisiones y requisitos cambian: verificar antes de contratar.**
> Encuadre tributario colombiano: invoca `contador_lushows`.

## Colombia

El dato que manda: **~70% del ecommerce de producto físico se paga contraentrega**. Eso significa
que la pasarela no es la protagonista, pero no puede faltar: el 30% prepago es el que te da caja
inmediata y margen sin fletes fallidos.

### Las cuatro

| Pasarela | Fuerte en | Débil en |
|---|---|---|
| **Wompi** (Bancolombia) | Alta rápida y simple, Nequi nativo, buena experiencia móvil, respaldo bancario | Menos funciones avanzadas |
| **Mercado Pago** | Reconocimiento, saldo MP, cuotas | Comisión y soporte variables |
| **PayU** | Cobertura regional, muchos métodos, madura | Panel pesado, alta más burocrática |
| **ePayco** | Local, flexible, buen soporte en español | Marca menos reconocida por el comprador |

### Métodos que tu checkout colombiano debe tener

| Método | Peso |
|---|---|
| **PSE** (débito desde cuenta bancaria) | **Crítico.** Es el prepago colombiano por excelencia |
| **Nequi** | Alto y creciendo, sobre todo en menores de 40 |
| Tarjeta de crédito con cuotas | Alto |
| Tarjeta de débito | Alto |
| Daviplata | Medio |
| Efectivo en corresponsal (Efecty, Baloto) | Medio |
| **Contraentrega** | El dominante. Va por formulario, no por pasarela. `191` |

### La estrategia colombiana que funciona

1. Formulario COD como opción principal. `191`.
2. Botón secundario de prepago con descuento real (5-10%): `Paga ahora con PSE o Nequi y ahorra`.
3. El descuento se paga solo: evitas el flete fallido y la comisión de recaudo, y cobras hoy.

Con capital corto, el prepago colombiano es el que mantiene viva la operación mientras el COD se
liquida.

## Chile

| Dato | Valor |
|---|---|
| Pasarelas | Transbank (Webpay) como estándar de facto, Flow, Mercado Pago, Khipu |
| Método dominante | **Webpay** con tarjeta de crédito y débito |
| Cuotas | Sí, importantes culturalmente |
| COD | Marginal. Chile es mercado prepago |
| Nota | Sin Webpay, el checkout chileno se siente extranjero |

## Perú

| Dato | Valor |
|---|---|
| Pasarelas | Niubiz, Culqi, Izipay, Mercado Pago |
| Métodos | Tarjeta, **Yape** y **Plin** (billeteras móviles, adopción masiva), PagoEfectivo |
| COD | Relevante, especialmente fuera de Lima |
| Nota | Yape y Plin son el equivalente de Nequi: si no los tienes, pierdes al comprador joven |

## Argentina

| Dato | Valor |
|---|---|
| Pasarelas | Mercado Pago domina con enorme ventaja |
| Métodos | Tarjeta **en cuotas** (el mecanismo cultural, como los MSI mexicanos), transferencia, saldo MP |
| COD | Bajo |
| Nota | Inflación y controles cambiarios: modela con cuidado. Invoca `economist_lushows` |

## Brasil

| Dato | Valor |
|---|---|
| Pasarelas | Mercado Pago, PagSeguro, Stripe BR, Pagar.me |
| Métodos | **PIX** (instantáneo, costo casi nulo) + **parcelamento** en tarjeta |
| COD | Marginal |
| Nota | PIX elimina la fricción del checkout y da caja inmediata. Es la mejor combinación de la región |

Detalle de mercado en `28`.

## Ecuador

| Dato | Valor |
|---|---|
| Pasarelas | Datafast, Payphone, Kushki, PayPal |
| Métodos | Tarjeta con **diferidos** (cuotas), transferencia |
| COD | Alto |
| Nota | Economía dolarizada: simplifica el modelo. `25` |

## La tabla de decisión rápida

| País | Prepago imprescindible | Mecanismo de cuotas | ¿COD? |
|---|---|---|---|
| Colombia | **PSE + Nequi** | Cuotas de tarjeta | **Dominante** |
| México | Tarjeta + OXXO | **MSI** `195` | Menor |
| Chile | **Webpay** | Cuotas | Marginal |
| Perú | **Yape / Plin** + tarjeta | Cuotas | Relevante |
| Argentina | Mercado Pago | **Cuotas** | Bajo |
| Brasil | **PIX** | **Parcelamento** | Marginal |
| Ecuador | Tarjeta | **Diferidos** | Alto |

## Las cinco reglas para toda LatAm

1. **Cobra en moneda local.** Cobrar en dólares hunde la conversión en toda la región.
2. **Ten el método local de billetera.** Nequi, Yape, Plin, PIX: sin eso pierdes al comprador joven.
3. **Ten cuotas.** Toda LatAm compra a plazos. Es cultural, no financiero.
4. **Revisa el plazo de liquidación** antes que la comisión: con capital corto, la caja manda.
5. **Da de alta una pasarela de respaldo.** Las retenciones y bloqueos pasan en el peor momento.

## El error que se repite

Montar una tienda para Colombia con solo tarjeta internacional y PayPal. Resultado: la mayoría del
tráfico no puede pagar aunque quiera, la conversión se desploma, y el operador concluye que "el
producto no sirve". El producto sirve; el checkout no.

Antes de encender pauta, pregúntale a tres personas del país: **¿cómo pagarías esto?** Y ofrece
exactamente eso.

## Relacionados
`191` formulario COD · `192` pasarelas México · `194` pasarelas Europa · `21` playbook Colombia · `30` COD vs prepago
