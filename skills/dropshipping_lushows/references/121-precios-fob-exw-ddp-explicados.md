# Precios FOB, EXW, DDP explicados

> Vigencia: septiembre 2026. Incoterms 2020 vigentes. Para el tratamiento aduanero y contable invoca
> `contador_lushows`.

Un Incoterm dice **quién paga qué y dónde pasa el riesgo**. Comparar una cotización EXW contra una
DDP sin ajustar es comparar peras con camiones: la diferencia entre ambas puede ser del 40% del
precio.

## Los cinco que vas a usar

| Incoterm | Hasta dónde paga el proveedor | Qué pagas tú | Cuándo usarlo |
|---|---|---|---|
| **EXW** (Ex Works) | Nada. El producto queda en su puerta | Recogida, exportación, flete, seguro, importación, entrega | Con agente que consolida. Ver `116` |
| **FOB** (Free On Board) | Hasta el barco en su puerto, con exportación despachada | Flete marítimo, seguro, importación, entrega | **El estándar para lote marítimo** |
| **CIF** (Cost, Insurance & Freight) | Hasta el puerto de destino, con seguro | Importación, despacho, entrega local | Cómodo pero encarece; el proveedor elige naviera |
| **DAP** (Delivered At Place) | Hasta tu bodega, sin impuestos | Aranceles e impuestos de importación | Aéreo con agente |
| **DDP** (Delivered Duty Paid) | Todo, impuestos incluidos | Nada más | Conveniente. Ojo con el asterisco |

## La escalera de costos: de EXW a tu bodega

Ejemplo, 500 unidades, peso bruto 180 kg, 0,95 m³, marítimo LCL a Buenaventura (Colombia).

| Concepto | Monto (USD) | Acumulado/unidad |
|---|---|---|
| EXW (500 × 2,95) | 1.475 | 2,95 |
| Transporte interno a puerto + exportación | 120 | 3,19 |
| **= FOB Shenzhen** | **1.595** | **3,19** |
| Flete marítimo LCL | 340 | 3,87 |
| Seguro (~0,3% del valor) | 6 | 3,88 |
| **= CIF Buenaventura** | **1.941** | **3,88** |
| Arancel + IVA de importación | según partida. Ver `17` | |
| Agente de aduana + gastos portuarios | 180-400 | |
| Transporte puerto → bodega | 90-200 | |
| **= Landed cost** | | **~4,60-5,40** |

**El precio EXW era 2,95. El costo real es 4,60-5,40.** Modelar el negocio con el precio de la
cotización te da un margen 40-60% más optimista que el real. Para el cálculo exacto de tu caso invoca
`Matematicas_lushows`; para la clasificación arancelaria invoca `contador_lushows`.

## El asterisco del DDP chino

Muchos proveedores y agentes ofrecen "DDP door to door" a precios muy por debajo de lo que costaría
pagar el arancel legal. Eso normalmente significa una de estas cosas:

1. **Subvaloración**: declaran un valor menor al real.
2. **Clasificación arancelaria incorrecta**: declaran una partida con menor tasa.
3. **Fraccionamiento**: parten el envío en paquetes para caer bajo un umbral.
4. **Canal gris**: transportistas que consolidan bajo el nombre de otro importador.

**El riesgo es tuyo.** Si la aduana revisa, quien responde es el importador de registro, no el agente
chino. En México, Colombia o España las consecuencias van de decomiso a sanción y responsabilidad
fiscal. Para el marco legal exacto invoca `contador_lushows`.

**DDP legítimo existe** —hay operadores serios que lo hacen con documentación completa y valor real—
pero se reconoce porque: te dan la declaración de importación a tu nombre, el valor declarado coincide
con tu factura, y el precio del DDP es coherente con el arancel del país. Si el DDP a México sale más
barato que el 33,5% solo del arancel, algo no está bien. Ver `16`, `141`.

## Peso real vs peso volumétrico: la trampa del flete

Las aerolíneas y couriers cobran **el mayor** entre peso real y peso volumétrico.

```
Peso volumétrico (aéreo)   = (largo × ancho × alto en cm) / 6000   → kg
Peso volumétrico (courier) = (largo × ancho × alto en cm) / 5000   → kg
```

Ejemplo: caja de 60 × 40 × 40 cm con 8 kg de producto adentro.
- Volumétrico aéreo: 96.000 / 6.000 = **16 kg**
- Te cobran 16 kg, no 8 kg. **El doble.**

**Consecuencia práctica:** producto liviano y voluminoso (almohadas, organizadores grandes, peluches)
es veneno para el flete aéreo. Producto pequeño y denso (herramientas, electrónica) es ideal.

En marítimo se cobra por el mayor entre peso (tonelada) y volumen (m³), con el factor de 1 m³ = 1.000
kg como regla general para LCL. Verifica con tu agente de carga.

**Siempre pide al proveedor:** peso neto, peso bruto, medidas de caja máster, unidades por caja. Sin
esos cuatro datos no puedes cotizar flete, y sin flete no sabes tu margen. Ver `119`.

## Aéreo vs marítimo: la decisión

| | Aéreo | Marítimo |
|---|---|---|
| Tiempo China→Colombia | 2-4 días puerto a puerto; 3-10 puerta a puerta | 30-45 días FCL / 35-50 LCL a Buenaventura |
| Tiempo China→Chile (Valparaíso) | días | 30-45 días |
| Tiempo China→Perú | días | 30-35 días (Chancay 28-32) |
| Tarifa | ~USD 6-8/kg (hasta 9,10/kg en cargas de 1.000 kg+ a Colombia) | Mucho menor por kg, pero con mínimos |
| Punto de equilibrio aproximado | Cargas chicas y densas | Volumen alto o producto barato por kg |
| Capital inmovilizado | Semanas | **1,5-2 meses.** Esto es lo que duele. Ver `138` |

Regla práctica: **si el flete aéreo supera el 20-25% del valor de la mercancía, evalúa marítimo.** Si
es menos, el aéreo casi siempre gana por el capital que libera.

## Qué Incoterm pedir según tu situación

| Situación | Pide |
|---|---|
| Primer pedido chico, con agente | **EXW** — el agente recoge y consolida |
| Lote de 300-1.000 uds, marítimo | **FOB** — tú controlas la naviera y el costo |
| Aéreo urgente sin agente de carga propio | **DAP** o CIF |
| No tienes RFC/NIT ni quieres importar formalmente | Compra local. **No importes.** Ver `128` |
| Te ofrecen DDP sospechosamente barato | Pide la declaración de importación a tu nombre. Si no la dan, no |

## Cómo comparar cotizaciones con Incoterms distintos

1. Lleva **todas** a la misma base: FOB puerto de salida.
2. Suma flete + seguro con la **misma** cotización de forwarder para todas.
3. Suma arancel e IVA según tu partida arancelaria (no según lo que diga el proveedor).
4. Suma despacho, agente de aduana y transporte interno.
5. Divide por unidades **buenas esperadas** (descuenta la tasa de defecto esperada, 2-5%).

Solo ahí tienes el número con el que se decide.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Comparar EXW contra DDP directo | Diferencia de hasta 40% del precio |
| Modelar el negocio con el FOB | Tu costo real es 40-60% mayor |
| Ignorar el peso volumétrico | Puedes pagar el doble de flete sin saberlo |
| Aceptar DDP barato sin documentación | El riesgo aduanero es tuyo. Ver `141` |
| Elegir marítimo sin contar el capital parado | 45 días de caja inmovilizada. Ver `138` |
| Olvidar el seguro | 0,3% del valor contra perder el 100% del contenedor |

## Para el proyecto activo (México, diciembre 2026)

En diciembre no importas nada: compras local. Los Incoterms importan a partir del lote de 2027, donde
la regla será **FOB + tu propio forwarder + importación formal con RFC y pedimento**. En ese momento
invoca `contador_lushows` para el pedimento y el acreditamiento del IVA.

## Relacionados
Ver `113`, `118`, `134`, `136`, `137`, `138`, `140`, `141`, `13`, `16`, `17`.
