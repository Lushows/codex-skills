# Pasarelas de pago en México

> Vigencia: 14-sep-2026. **Comisiones y requisitos cambian: verificar en la web de cada pasarela
> antes de contratar.** Encuadre fiscal: invoca `contador_lushows`.

México es el 8º mercado de ecommerce del mundo: **77,2 millones de compradores digitales, creciendo
19,2% al año, con 17,7% de penetración sobre el retail**. Es un mercado grande, con medios de pago
maduros y con un mecanismo cultural propio que decide compras: los meses sin intereses. `195`.

## Las cuatro opciones reales

| Pasarela | Fuerte en | Débil en |
|---|---|---|
| **Mercado Pago** | Reconocimiento de marca enorme, MSI, saldo MP, efectivo en tiendas, alta rápida | Comisión no es la más baja; panel a veces lento |
| **Stripe MX** | Mejor experiencia técnica, integración impecable con Shopify, MSI disponibles | Requisitos de alta más estrictos; menos reconocido por el comprador final |
| **Conekta** | Mexicana, MSI, **OXXO Pay** y SPEI nativos, buen soporte local | Ecosistema más chico |
| **Openpay** (BBVA) | Respaldo bancario, MSI, buenas tasas negociadas a volumen | Alta más lenta y burocrática |

## Qué debe cubrir tu pasarela en México

| Método | Peso en la decisión | Comentario |
|---|---|---|
| **Tarjeta de crédito con MSI** | **Crítico** | El mecanismo dominante del Buen Fin. `195` |
| Tarjeta de débito | Crítico | Gran parte del país opera con débito |
| **OXXO Pay / efectivo en tienda** | Alto | Para quien no tiene tarjeta o no confía en meterla |
| **SPEI** (transferencia) | Medio-alto | Ticket alto y compradores bancarizados |
| Mercado Pago saldo | Medio | Alto reconocimiento |
| PayPal | Medio | Confianza, pero comisión alta |
| Contraentrega | Bajo en este proyecto | México es menos COD que Colombia. `30` |

**OXXO merece atención aparte.** Un porcentaje relevante de compradores mexicanos prefiere pagar en
efectivo en la tienda de la esquina. Es un pago diferido (el cliente tiene horas para pagar), así
que una parte no se concreta; aun así, suma ventas que de otro modo no existirían. Configura el
recordatorio automático de referencia no pagada.

## Cómo elegir

1. **¿Ofrece MSI y desde qué monto?** Si no los ofrece, descártala para este proyecto.
2. **¿Tiene integración oficial con tu plataforma?** Nada de conectores de terceros. `176`.
3. **¿Qué comisión combinada pagas?** Pasarela + plataforma + IVA sobre la comisión. Ese número va
   al modelo de `06`.
4. **¿Qué pide para el alta?** Persona física con actividad empresarial o moral, RFC, CLABE, y a
   veces comprobante de domicilio y del giro.
5. **¿Cada cuánto liquida?** Con capital bajo USD 500, el plazo de liquidación es tan importante
   como la comisión: si te pagan a 14 días, financias los anuncios con tu bolsillo.
6. **¿Qué antifraude trae?** Un motor de riesgo demasiado agresivo rechaza ventas buenas.

## El costo que se te olvida meter en el modelo

| Concepto | Efecto |
|---|---|
| Comisión base por transacción | El que sí calculas |
| **IVA sobre la comisión** | Sube el costo real |
| **Diferencial de MSI** (~1,5 puntos extra) | Vale la pena: sube conversión de 2,2% a 3,0%. `195` |
| Comisión por reembolso | Algunas no devuelven la comisión original |
| Contracargo | Costo fijo + pérdida del producto |
| Retención por riesgo en tiendas nuevas | Puede congelar tu caja justo en el pico |

Con el modelo verificado del proyecto (ticket USD 60,05, costo USD 29,33, techo de CAC USD 30,73),
cada punto porcentual de comisión son ~USD 0,60 por venta: el 3% de tu utilidad de USD 20,18. No es
trivial, pero **nunca elijas pasarela por 0,3 puntos si la otra te da MSI**.

## La trampa de la retención

Las pasarelas retienen fondos de comercios nuevos con crecimiento repentino. En Buen Fin, con el
gasto multiplicado, una retención de 7-14 días te deja sin caja para pagar los anuncios.

Cómo reducir el riesgo:

1. Da de alta la pasarela **semanas antes**, no la víspera. Empieza el trámite ya.
2. Empieza a facturar bajo y sube gradual, sin saltos de 20x en un día.
3. Ten la documentación en regla desde el principio.
4. Responde reclamos el mismo día: los contracargos son lo que dispara la retención. `188`.
5. **Ten una segunda pasarela dada de alta y probada**, aunque no la uses.

## Alta: qué preparar (México)

| Documento | Nota |
|---|---|
| RFC | Persona física con actividad empresarial o persona moral |
| Constancia de situación fiscal | Vigente |
| CLABE de cuenta a nombre del titular del RFC | Que coincida, o se traba |
| Identificación oficial | INE o pasaporte |
| URL de la tienda **con las legales publicadas** | Las revisan. `207` |
| Descripción del giro | Coherente con lo que vendes |

Muchos rechazos pasan porque la tienda no tiene aviso de privacidad ni política de devoluciones al
momento de la revisión. Publícalas antes de solicitar.

## Configuración para el proyecto (diciembre 2026)

| Decisión | Valor |
|---|---|
| Pasarela principal | Mercado Pago o Conekta (ambas con MSI y OXXO) |
| Pasarela de respaldo | Stripe MX, dada de alta y probada |
| Métodos activos | Crédito con MSI, débito, OXXO Pay, SPEI |
| MSI | Desde 1.000 MXN; el bundle de 1.099 MXN califica **a propósito** |
| Moneda de cobro | MXN. Nunca USD |
| Prueba | Compra real con cada método antes de encender pauta. `190` |

El bundle de 1.099 MXN no está en ese precio por casualidad: cruza el umbral típico de MSI. Esa sola
decisión de precio es la que hace que la utilidad pase de USD 2,63 a USD 20,18. `195`, `42`.

## Relacionados
`195` meses sin intereses · `190` checkout · `193` pasarelas LatAm · `20` playbook México · `205` temporada alta
