# DDP, DDU y quién paga el arancel

> Tres letras deciden si tu cliente recibe una caja o recibe una **llamada pidiéndole plata**. DDU
> significa que el courier le cobra el arancel a tu cliente en la puerta. Ahí no pierdes un envío:
> pierdes la venta, la reseña, el reembolso y la reputación de la tienda.

## Los incoterms que te importan (los otros no)

| Sigla | Nombre | Hasta dónde llega tu responsabilidad | Quién paga impuestos |
|---|---|---|---|
| **EXW** | Ex Works | La puerta de la fábrica | Tú, todo |
| **FOB** | Free on Board | Cargado en el barco/avión en origen | Tú, desde ahí |
| **CIF** | Cost, Insurance & Freight | Puerto de destino, con seguro | Tú (aduana en destino) |
| **DDU / DAP** | Delivered Duty Unpaid | Puerta del cliente, **sin impuestos pagados** | **EL CLIENTE**, en la puerta |
| **DDP** | Delivered Duty Paid | Puerta, **todo pagado** | Tú, ya incluido |

## Por qué DDU te destruye

Escena real: tu cliente en Ciudad de México compró un bundle de 1.099 MXN. El repartidor llega y
le dice que debe pagar 380 MXN de impuestos antes de recibir la caja.

| Lo que pasa | Consecuencia |
|---|---|
| El cliente rechaza | Pierdes producto + flete de ida + flete de vuelta (si vuelve) |
| El cliente paga de mala gana | Reseña de 1 estrella, contracargo probable |
| El cliente pide reembolso | Pagas el reembolso y ya perdiste el producto |
| El cliente reclama públicamente | Comentarios en tus anuncios → sube el CPA |
| Meta ve reportes negativos | Riesgo de restricción de cuenta |

El costo de un DDU mal manejado **no es el arancel**: es el CAC entero más el producto más la
reputación. Nunca vale la pena "ahorrar" mandando DDU.

## La regla

> **Si vendes a consumidor final, siempre DDP. Sin excepciones.**
> DDU solo tiene sentido entre empresas, cuando tu contraparte tiene agente aduanal y lo sabe.

## Cómo se ve DDP en cada estructura

| Estructura | Quién despacha | Cómo cobras el impuesto |
|---|---|---|
| **Stock local** (recomendado) | Tú, una vez, al importar el lote | Ya está dentro del costo del producto. El cliente nunca ve un impuesto |
| Línea dedicada DDP China→cliente | El agente, en lote | Va incluido en el USD/kg que pagas |
| Courier DDP | El courier | Te lo factura a ti después |
| Marketplace con bodega local | El marketplace | Incluido |
| **China directo DDU** | Nadie hasta que llega | **El cliente. No hagas esto** |

## El mapa 2026: cuánto es "el arancel" que alguien tiene que pagar

Datos con fecha; verificar antes de cotizar porque este es el terreno que más se mueve.

| Mercado | Umbral libre | Carga sobre origen sin acuerdo | Vigencia |
|---|---|---|---|
| **EE.UU.** | **De minimis ELIMINADO** | Origen chino **~54%**; ~30% si entra por courier | 2026 |
| **Unión Europea** | Sin exención práctica | **€3 por línea** desde **1-jul-2026** + tasa propuesta desde **1-nov-2026** | 2026 |
| **México** | — | **33,5%** para países sin TLC desde **1-ene-2026**, **sin fecha de caducidad** | vigente |
| **Colombia** | **US$200 FOB** | Origen sin TLC: **IVA 19% + ~10% courier** | vigente |
| **Reino Unido** | **£135** | — | al menos hasta **31-dic-2026** |
| **Chile** | **US$41** | — | vigente |
| **Perú** | **US$200** | — | vigente |

Detalle por país en `13`-`19`. Para clasificación arancelaria exacta, valoración y si te conviene
importación formal, **invoca `contador_lushows`**.

## Consecuencia estratégica

El fin del de minimis y el 33,5% de México matan el modelo "China directo al cliente" en los dos
mercados más grandes de la región. Por eso la respuesta de 2026 es **stock local**: importas una vez,
pagas una vez, controlas el costo, entregas en días.

| Modelo | Con las reglas de 2026 |
|---|---|
| China → cliente, DDU | Muerto. El cliente paga en la puerta |
| China → cliente, DDP courier | Sobrevive solo con márgenes muy altos |
| China → tu bodega local → cliente | **El que funciona** |
| Proveedor local → cliente | El más simple, menor margen, cero riesgo aduanero |

## Qué escribir en tu web

Con stock local y DDP, escribe literalmente:

> **Precio final. Sin costos de aduana ni cargos sorpresa al recibir.**

Es una ventaja competitiva real contra los que mandan desde China y todavía no lo dicen. Úsala en
la página de producto y en el checkout, donde más duele la duda.

Con DDU no puedes escribir nada tranquilizador: tendrías que poner "podrías tener que pagar
impuestos al recibir", que es exactamente lo que hunde la conversión.

## Checklist antes de contratar un envío

1. ¿El incoterm está **escrito** en la cotización? Si dice solo "flete", pregunta.
2. ¿DDP incluye **arancel e IVA**, o solo arancel? Son cosas distintas.
3. ¿Qué pasa si la aduana reclasifica y el impuesto sube? ¿Quién asume la diferencia?
4. ¿El agente emite documento que soporte el gasto en tu contabilidad?
5. Si es courier: ¿la cuenta de impuestos está a tu nombre (importador de registro) o al del
   cliente? Si es al del cliente, **es DDU disfrazado**.
6. ¿Tu página dice en algún lado quién paga los impuestos? Si no dice nada, el cliente asume que tú.

## Errores caros

| Error | Costo |
|---|---|
| Cotizar precio de venta sin el arancel adentro | Vendes con margen negativo y lo descubres tarde |
| Asumir que "DDP" del proveedor chino cubre todo | Muchos "DDP" cubren arancel pero no IVA. Pregunta |
| Cambiar de DDP a DDU para bajar el flete | Ver la escena del principio |
| No recalcular cuando cambia la regla | México cambió el 1-ene-2026 y hay tiendas que siguen con la vieja hoja |

## Relacionados
`150` valor declarado · `151` despacho de aduana · `152` costo puesto en destino · `13` mapa
aduanero 2026 · `16` México 33,5% · `17` Colombia · `14` fin del de minimis · `157` comunicar la
entrega
