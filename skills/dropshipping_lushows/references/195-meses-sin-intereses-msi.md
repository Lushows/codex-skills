# Meses sin intereses (MSI)

> Vigencia: 14-sep-2026. Módulo clave para México. **Comisiones y umbrales varían por pasarela y por
> banco: verificar antes de configurar.** Encuadre fiscal: invoca `contador_lushows`.

Los MSI no son una promoción: son **el mecanismo de compra dominante** del comercio mexicano, y
especialmente del Buen Fin. Un mexicano que ve "12 meses sin intereses" no está calculando
financiación: está viendo el precio real que va a sentir cada mes. El número que compara no es 1.099
pesos; es 91,58.

## El efecto verificado

| Métrica | Sin MSI | Con MSI | Cambio |
|---|---|---|---|
| Conversión | 2,2% | **3,0%** | **+36%** |
| Comisión de pasarela | Base | Base + ~1,5 puntos | Costo |
| **CAC** | USD 14,38 | **USD 10,54** | **−27%** |

El CAC cae porque el mismo gasto en anuncios produce más ventas. Ese es el mecanismo completo: los
MSI no bajan tu costo por clic, bajan tu costo por **venta**.

## La cuenta que decide

Modelo verificado del proyecto (bundle 1.099 MXN, México, prepago, diciembre 2026):

| Concepto | Valor (USD) |
|---|---|
| Ticket | 60,05 |
| Costo (producto + envío + comisiones) | 29,33 |
| **Techo de CAC** | **30,73** |
| CAC real con MSI | 10,54 |
| **Utilidad por venta** | **20,18** |
| Holgura sobre el techo de CAC | **2,92x** |
| ROAS de equilibrio | **1,95** |

Comparación con el mismo producto sin bundle:

| Escenario | Ticket | Utilidad por venta |
|---|---|---|
| Bundle 1.099 MXN + MSI | USD 60,05 | **USD 20,18** |
| Producto suelto 699 MXN | ~USD 38 | **USD 2,63** |

**7,7 veces más utilidad.** Los MSI y el bundle son la misma decisión: el bundle sube el ticket por
encima del umbral de MSI, y los MSI hacen que ese ticket más alto no asuste.

## Por qué el bundle está en 1.099 y no en 999

Porque los MSI suelen activarse desde un monto mínimo (típicamente alrededor de 1.000 MXN, **verifica
el de tu pasarela y banco**). Un bundle de 999 MXN queda justo debajo y pierde el beneficio; uno de
1.099 lo cruza con holgura. Esa diferencia de 100 pesos vale +36% de conversión.

## Cuánto cuestan de verdad

El diferencial de MSI (~1,5 puntos de comisión adicional) es el precio de entrada. La cuenta sobre
100 sesiones de tráfico:

| Escenario | Conversión | Ventas | Ingreso bruto | Comisión extra MSI | Resultado relativo |
|---|---|---|---|---|---|
| Sin MSI | 2,2% | 2,2 | ~USD 132 | 0 | Base |
| **Con MSI** | 3,0% | 3,0 | ~USD 180 | ~USD 2,70 | **+USD 45 aprox.** |

El diferencial se paga **muchas veces**. Los MSI no se discuten por costo: se discuten por si tu
pasarela los ofrece o no.

> Los importes se derivan del modelo verificado; **recalcula con tus propias comisiones**. Para la
> aritmética exacta, invoca `Matematicas_lushows`.

## Quién paga los intereses

Nadie los paga en forma de intereses: tú pagas una **comisión de diferimiento** más alta a la
pasarela, y el banco financia al cliente. Dos modalidades:

| Modalidad | Quién absorbe | Cuándo usarla |
|---|---|---|
| **Comercio absorbe** (el estándar) | Tú, vía comisión mayor | Siempre en B2C de consumo. Es lo que el cliente espera |
| Cliente paga el diferimiento | El cliente ve un precio mayor al elegir meses | Destruye el efecto. No la uses |

## Cómo se activan

1. Elige una pasarela que los ofrezca: Mercado Pago, Conekta, Stripe MX, Openpay. `192`.
2. En su panel, activa **promociones / diferido a meses**.
3. Define los plazos: 3, 6, 9, 12 meses. Empieza con 3, 6 y 12.
4. Define el **monto mínimo**. Ponlo justo debajo de tu bundle.
5. Define qué bancos participan (la pasarela suele manejar la lista).
6. Verifica que el plugin de tu plataforma muestre los MSI **en el producto**, no solo al pagar.
7. **Haz una compra real a 12 meses con tarjeta de crédito propia** y comprueba el estado de cuenta.

El paso 6 es el que casi todos se saltan, y es el que mueve la conversión: si el cliente descubre
los MSI hasta el último paso, ya decidió no comprar.

## Cómo se comunican en la página (textos listos para copiar)

| Ubicación | Texto |
|---|---|
| Barra de anuncio | `Hasta 12 meses sin intereses en compras desde $1,000` |
| **Junto al precio** | `$1,099 MXN` · `o 12 pagos de $91.58 sin intereses` |
| Bajo el botón | `Paga a 3, 6, 9 o 12 meses sin intereses con tu tarjeta de crédito.` |
| Tira de confianza | `Hasta 12 MSI` |
| En la FAQ | Ver `187`, la respuesta completa |
| En el checkout | `Elige tus meses sin intereses en el siguiente paso.` |
| En Buen Fin | `12 MSI disponibles hasta el 17 de noviembre` |

**La línea más importante de todas es la del pago mensual junto al precio.** Convierte 1.099 en
91,58. Es la misma cifra que el cliente usa para decidir.

### El ejemplo completo del bloque de precio

> **$1,099** ~~$1,499~~ MXN
> **o 12 pagos de $91.58 sin intereses**
> Envío gratis · Llega en 2 a 4 días hábiles
> **[ LO QUIERO — $1,099 ]**
> Garantía de 30 días · Hasta 12 MSI con tarjeta de crédito

(El precio tachado solo si es real. `189`.)

## Buen Fin: 13-17 de noviembre de 2026

Es el evento donde los MSI dejan de ser una ventaja y pasan a ser el requisito de entrada. Toda la
competencia los tendrá.

| Acción | Cuándo |
|---|---|
| Alta de la pasarela con MSI | **Ya.** Puede tardar días o semanas. `192` |
| Prueba de compra real a MSI | Al menos 3 semanas antes |
| Comunicación de MSI en toda la página | 1 semana antes |
| Subir plazos a 12 e incluso 18 si tu pasarela lo permite | 13-17 nov |
| Volver a la configuración normal | 18 nov |

Detalle de la operación de temporada en `205`.

## Errores comunes

| Error | Costo |
|---|---|
| Activar MSI y no mostrarlos en la página de producto | Pagas la comisión extra sin ganar conversión |
| Poner el mínimo de MSI por encima de tu ticket | Los MSI existen pero nadie califica |
| Calcular la mensualidad mal | Reclamos y desconfianza. Deja que la plataforma la calcule |
| Prometer MSI con tarjeta de débito | Los MSI son de **crédito**. Dilo explícitamente |
| No probar con tarjeta real | Descubrir en Buen Fin que no funcionan |
| Modelar el margen sin el diferencial de comisión | Margen fantasma |

## Relacionados
`192` pasarelas México · `190` checkout · `187` FAQ · `205` temporada alta · `42` múltiplo de margen
