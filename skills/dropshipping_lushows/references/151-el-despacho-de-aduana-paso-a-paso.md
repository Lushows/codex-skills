# El despacho de aduana paso a paso

> La aduana no es un muro: es un procedimiento con pasos, documentos y relojes. Lo que la vuelve
> cara es llegar sin papeles y descubrirlo cuando la carga ya está en piso cobrando almacenaje.
> **Añade 3-10 días a cualquier tránsito** y planifica con ese número, no con el optimista.

## El flujo, de principio a fin

| # | Paso | Quién lo hace | Reloj |
|---|---|---|---|
| 1 | Llegada y manifiesto de carga | Transportista | 0-1 día |
| 2 | Desconsolidación | Agente en destino | 1-3 días |
| 3 | Transmisión de la declaración | Agente aduanal | horas |
| 4 | Liquidación de impuestos | Sistema aduanero | horas |
| 5 | Pago de impuestos | Tú o el agente | inmediato si hay fondos |
| 6 | **Selectividad** (canal) | Sistema | minutos |
| 7 | Revisión, si aplica | Aduana | 1-7 días |
| 8 | Levante / liberación | Aduana | horas-1 día |
| 9 | Retiro y transporte a tu bodega | Transporte local | 1-3 días |

## Los canales de selectividad

Casi todos los países usan el mismo semáforo, con nombres distintos.

| Canal | Qué pasa | Frecuencia típica | Días extra |
|---|---|---|---|
| **Verde** (automático) | Libera sin revisión | la mayoría | 0 |
| **Naranja / documental** | Revisan papeles | frecuente en importador nuevo | 1-3 |
| **Rojo / físico** | Abren y verifican la mercancía | minoría, pero no rara | 2-7 |

> El importador nuevo o esporádico cae más en naranja y rojo. Tu **primer** embarque es el que más
> riesgo tiene. Planifica con holgura precisamente ahí, no en el tercero.

## Los documentos, sin excepción

| Documento | Qué debe decir | Error que lo tumba |
|---|---|---|
| **Factura comercial** | Vendedor, comprador, descripción real, cantidad, unitario, total, incoterm, moneda | Descripción vaga tipo "gift", "sample", "accessories" |
| **Packing list** | Bultos, contenido, peso bruto y neto, medidas | Pesos que no coinciden con la guía |
| **Guía aérea (AWB) o BL** | Consignatario correcto | Consignatario mal escrito → no puedes retirar |
| **Certificado de origen** | Solo si vas a usar un TLC | Formato vencido o mal emitido |
| Registros / permisos | Según producto: sanitario, telecom, etiquetado | El más común de olvidar |
| Documento de identificación fiscal | RFC (MX), NIT/RUT (CO), etc. | Datos que no coinciden |

## Los productos que se complican

| Categoría | Requisito frecuente | Riesgo |
|---|---|---|
| Cosmética, suplementos, alimentos | Registro sanitario | Decomiso. Ver `07` |
| Electrónicos con radio (Bluetooth, Wi-Fi) | Homologación telecom | Retención |
| Juguetes infantiles | Norma de seguridad, etiquetado | Retención |
| Textiles y calzado | Etiquetado de composición y país de origen | Multa |
| Cualquier cosa con logo de marca | Prueba de licencia | **Decomiso y proceso** |
| Baterías de litio | Documentación de mercancía peligrosa | Rechazo del vuelo |

Regla práctica para quien arranca con menos de USD 500: **evita las seis categorías de arriba en tu
primer lote.** No porque sean imposibles, sino porque un decomiso te borra el capital entero.

## Los costos del despacho (aparte de los impuestos)

| Concepto | Cómo se cobra | Nota |
|---|---|---|
| Honorarios de agente aduanal | Por declaración o % del valor | Verificar; suele haber mínimo |
| Manejo en terminal / THC | Por bulto o por peso | — |
| Desconsolidación | Por guía hija | — |
| **Almacenaje** | **Por día** | El que te arruina si te demoras |
| Inspección física | Costo del movimiento de carga | Solo si cae rojo |
| Transporte a tu bodega | Por viaje | — |

El almacenaje es el castigo por la desorganización. Empieza a correr aunque la demora sea culpa del
agente. Ten los fondos para pagar impuestos **antes** de que llegue la carga, no después.

## Procedimiento para que salga bien

1. **Dos semanas antes de que embarque**: pide al proveedor el borrador de factura comercial y
   packing list. Revísalos tú.
2. Verifica que la descripción del producto sea **real y específica**: "organizador de cocina de
   plástico PP, 24 piezas", no "kitchen set".
3. Confirma con tu agente la **subpartida arancelaria** y el impuesto estimado. Escríbelo.
4. Calcula el costo puesto en destino con `152` y confirma que el margen aguanta.
5. Verifica si el producto necesita permiso. Si lo necesita y no lo tienes, **cambia de producto**.
6. Ten el dinero de impuestos separado desde antes del embarque.
7. Al embarcar, guarda la guía madre y pide seguimiento cada 48 h.
8. Cuando llegue, pregunta el canal el mismo día. Si es rojo, avisa a tu equipo y **corre el
   calendario de campaña**, no lo dejes igual.
9. Guarda todo el expediente (`150`).

## Régimen simplificado vs importación formal

| | Simplificado / courier | Formal |
|---|---|---|
| Quién declara | El courier o la línea | Agente aduanal a tu nombre |
| Límite de valor | Sí, por país (ver `13`) | Sin límite práctico |
| Velocidad | Más rápido | 3-10 días |
| Costo por unidad | Alto | Bajo en volumen |
| Puedes deducir el gasto | Depende, verificar | Sí, con declaración |
| Cuándo | Primer lote, pruebas | Cuando el volumen lo justifique |

El salto a formal es una decisión contable y tributaria, no logística. **Invoca
`contador_lushows`** cuando estés cerca de darlo.

## Señales de que tu agente te está fallando

- No te dice el canal de selectividad.
- No te pasa la liquidación desglosada.
- Te avisa del almacenaje cuando ya lleva 5 días corriendo.
- "Está en proceso" tres días seguidos sin número de trámite.
- Te pide pagos por fuera de la liquidación oficial.

## Relacionados
`149` DDP y DDU · `150` valor declarado · `152` costo puesto en destino · `148` líneas dedicadas ·
`13` mapa aduanero 2026 · `146` tiempos de tránsito · invoca `contador_lushows`
