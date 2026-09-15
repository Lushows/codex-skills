# Declarar valor: la línea legal

> Subdeclarar el valor de una importación no es "un truco de importador". Es **fraude aduanero**:
> un delito, con nombre propio en la ley de tu país. En 2026 hay control documental cruzado y te
> pueden pedir consistencia entre la factura comercial, el valor declarado y **lo que efectivamente
> pagaste**. Este módulo existe para que sepas dónde está la raya y no la pises por ignorancia.

## Qué es el valor en aduana

El valor sobre el que se liquidan impuestos no es "lo que tú digas". Es el **valor de transacción**:
el precio realmente pagado o por pagar por la mercancía, con ajustes según el método del país.
En general incluye:

| Sí entra | Normalmente no entra (verificar por país) |
|---|---|
| Precio del producto | Impuestos internos del destino |
| Comisiones de venta | Transporte interno después del despacho |
| Empaques y embalajes | Intereses de financiación declarados aparte |
| Regalías y licencias vinculadas | — |
| Flete y seguro hasta destino, según base CIF/FOB del país | — |

Colombia usa referencia **FOB** para el umbral de US$200; otros países liquidan sobre CIF. Esa
diferencia cambia el número final. Para determinar la base correcta y la subpartida arancelaria,
**invoca `contador_lushows`**.

## Lo que sí es legal

| Práctica | Legal | Por qué |
|---|---|---|
| Negociar un precio real más bajo con el proveedor | ✅ | El valor bajo **es real** |
| Facturar flete y seguro por separado cuando el país liquida sobre FOB | ✅ | Es la base correcta |
| Clasificar en la subpartida correcta aunque pague menos | ✅ | Clasificar bien no es evadir |
| Usar un acuerdo comercial con certificado de origen válido | ✅ | Es el beneficio previsto en la norma |
| Importar bajo régimen simplificado dentro de sus límites | ✅ | Es el régimen |
| Dividir una compra grande en varios pedidos **reales**, en fechas distintas y por necesidad real | ⚠️ | Legal como decisión de compra; **ilegal si es fraccionamiento artificial para evadir el umbral** |

## Lo que no es legal

| Práctica | Nombre real | Riesgo |
|---|---|---|
| Pedir factura por USD 40 cuando pagaste USD 400 | Subfacturación / fraude aduanero | Multa, decomiso, responsabilidad penal |
| Declarar "regalo" / "muestra sin valor" una mercancía comercial | Falsedad en documento | Decomiso, sanción |
| Declarar una mercancía por otra para bajar el arancel | Contrabando técnico | Decomiso, sanción, cierre |
| Partir un mismo pedido en 5 guías el mismo día al mismo destinatario | Fraccionamiento | La aduana suma y sanciona |
| Aceptar el "DDP mágico" de un agente que evade por ti | Sigues siendo responsable | Tuya la mercancía, tuya la sanción |

> El agente que te ofrece "no te preocupes, nosotros lo pasamos" no asume la sanción. El importador
> responde. Si eres tú, pierdes tú.

## Por qué en 2026 ya no funciona lo que "funcionaba antes"

1. **Control documental cruzado.** Piden factura comercial, contrato, comprobante de pago y, cada
   vez más, el precio publicado en tu tienda. Si vendes a 1.099 MXN y declaraste USD 2 de costo,
   la incoherencia salta sola.
2. **Bases de datos de precios de referencia.** La aduana tiene rangos por subpartida y origen; si
   declaras muy por debajo del rango, se activa duda razonable.
3. **Trazabilidad del pago.** La transferencia internacional deja rastro; el valor pagado no
   coincide con el declarado.
4. **Fin del de minimis en EE.UU. y umbral €3 en la UE**: el volumen que antes pasaba sin mirar
   ahora sí se mira.
5. **Plataformas que reportan.** Marketplaces y pasarelas informan ventas. El cruce es cuestión de
   tiempo.

## La "duda razonable": qué pasa cuando no te creen

| Paso | Qué ocurre | Tiempo |
|---|---|---|
| 1. Aduana cuestiona el valor | Te piden soportes | inmediato |
| 2. Aportas factura, contrato y pago | Si son consistentes, se libera | 2-10 días |
| 3. No son consistentes | Reliquidan con valor de referencia | + días |
| 4. Hay indicios de fraude | Multa, decomiso, proceso | semanas o meses |
| Mientras tanto | **Almacenaje corriendo por día** | costo diario, verificar |

En dropshipping, una carga retenida 20 días en temporada alta te cuesta la temporada completa.
El "ahorro" del 20% de impuestos nunca compensa eso.

## El expediente que te salva

Guarda por cada importación, mínimo 5 años (verificar el plazo de tu país con `contador_lushows`):

1. Factura comercial con: vendedor, comprador, descripción real, cantidad, precio unitario, total,
   incoterm, moneda.
2. Packing list con bultos, pesos y medidas.
3. **Comprobante de pago** al proveedor por el mismo monto de la factura.
4. Documento de transporte (guía aérea o BL).
5. Declaración de importación y liquidación de impuestos.
6. Correspondencia con el proveedor donde se negoció el precio.
7. Fotos de la mercancía y del marcado de cajas (`148`).

Regla simple: **factura = lo que pagaste = lo que declaraste.** Tres números iguales. Si alguien
propone que sean distintos, te está proponiendo un delito.

## El cálculo honesto que vuelve todo innecesario

Casi siempre, el impulso de subdeclarar viene de un margen mal calculado desde el principio. Si el
producto solo funciona evadiendo, **no es un producto ganador, es un producto malo**. Ver `42`:
si el múltiplo no aguanta con el impuesto pagado, cambia de producto, no de declaración.

| Producto | Costo China | Impuesto pagado | Costo real | Precio | ¿Sirve? |
|---|---|---|---|---|---|
| A | USD 3 | USD 1,0 | 4,0 | 25 | Sí |
| B | USD 12 | USD 4,0 | 16,0 | 28 | No, y no lo arregla evadir |

## Relacionados
`149` DDP y DDU · `151` despacho de aduana · `152` costo puesto en destino · `13` mapa aduanero ·
`42` múltiplo mínimo de margen · `07` ética y legalidad · invoca `contador_lushows`
