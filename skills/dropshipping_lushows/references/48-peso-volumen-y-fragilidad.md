# Peso, volumen y fragilidad (el impuesto silencioso al margen)

## La regla que nadie mira hasta que ya compró

El flete no se cobra por peso real: se cobra por **peso volumétrico**, el que sea mayor.

```
PESO VOLUMÉTRICO (kg) = largo × ancho × alto (cm) ÷ 5000     ← estándar aéreo
PESO FACTURABLE = máximo(peso real, peso volumétrico)
```

Una almohada de 300 g que mide 40×30×20 cm pesa volumétricamente 4,8 kg. Vas a pagar por 4,8 kg.
Ahí mueren los márgenes que se calcularon con la báscula.

## Tabla orientativa de costo aéreo por peso facturable

Rangos de mercado sep-2026 para envíos consolidados China → LatAm. **Verificar con tu agente**: las
tarifas varían por ruta, temporada y volumen.

| Peso facturable | USD/kg orientativo | Costo por unidad | Veredicto |
|---|---|---|---|
| ≤ 100 g | 8-14 | USD 0,80-1,40 | Ideal |
| 100-300 g | 7-12 | USD 0,70-3,60 | Muy bueno |
| 300-500 g | 6-11 | USD 1,80-5,50 | Aceptable |
| 500 g-1 kg | 5-10 | USD 2,50-10,00 | Límite |
| 1-2 kg | 5-9 | USD 5,00-18,00 | Descartar salvo ticket alto |
| > 2 kg | 4-8 | USD 8,00+ | Marítimo o descarte |

En Q4 las tarifas aéreas suben; en la ventana previa a Navidad pueden subir 20-40%. Si tu producto
apenas cuadra a 9 USD/kg en septiembre, no cuadra en noviembre.

## El impacto real sobre el múltiplo

Mismo producto, distinto peso. Ticket 1.099 MXN (≈ USD 58), múltiplo mínimo México conservador 3,74x
→ costo puesto en bodega máximo ≈ USD 15,50.

| Peso facturable | Producto | Flete | Arancel MX 33,5% s/(prod+flete) | Puesto en bodega | ¿Pasa? |
|---|---|---|---|---|---|
| 150 g | USD 6,00 | USD 1,50 | USD 2,51 | USD 10,01 | Sí, con holgura |
| 500 g | USD 6,00 | USD 4,00 | USD 3,35 | USD 13,35 | Sí, justo |
| 1,2 kg | USD 6,00 | USD 9,00 | USD 5,03 | USD 20,03 | **No** |

El producto no cambió. Cambió la caja. Nota además el efecto compuesto: **el arancel se calcula
sobre producto + flete**, así que el peso te castiga dos veces.

Este cálculo es exactamente la razón por la que el proyecto de México usa **stock local**: comprando
en México ya nacionalizado, el flete internacional y el 33,5% no entran en tu ecuación por unidad
(los pagó el importador) y evitas perder ~USD 18 por venta enviando desde China. Ver `16` y `128`.

## Fragilidad: el costo que no aparece en ninguna cotización

| Categoría | Tasa de rotura típica | Costo real por venta |
|---|---|---|
| Plástico sólido, textil, silicona | < 0,5% | Despreciable |
| Electrónica en carcasa | 1-3% | Producto + reenvío |
| Vidrio, cerámica, espejo | 8-20% | Producto + reenvío + reseña mala |
| Pantallas o cristal expuesto | 10-25% | Inviable |

La fórmula del costo oculto:

```
costo_rotura_por_venta = tasa_rotura × (costo_producto + flete_nacional × 2)
```

Con 12% de rotura, producto de USD 6 y flete nacional de USD 6: 0,12 × (6 + 12) = **USD 2,16 por
venta**. Sobre un techo de CAC de USD 19, eso es el 11% de tu capacidad de compra de tráfico,
quemado en cajas rotas.

Y el daño no financiero es peor: cada rotura genera un mensaje de soporte, un reembolso o una
reseña. Con capital menor a USD 500 no tienes colchón para eso.

## El test físico de fragilidad (hazlo tú, no confíes en el proveedor)

1. Pide **una muestra** antes del pedido grande. Siempre. Sin excepción.
2. Déjala caer desde 1 metro **en su empaque de venta**.
3. Aprieta la caja con la mano como lo haría un repartidor.
4. Agita: si suena suelto adentro, va a llegar roto.
5. Si falla cualquiera, exige empaque reforzado y recalcula el peso volumétrico con el empaque nuevo.

Punto 5: el empaque reforzado **sube el peso volumétrico**. Muchas veces la solución a la
fragilidad es la que mata el margen. Si ese es el caso, el producto está descartado.

## Umbrales duros de descarte

| Criterio | Umbral |
|---|---|
| Peso facturable | > 1 kg → descarte por defecto |
| Lado más largo | > 40 cm → problemas de última milla y recargos |
| Rotura en test de caída | Cualquier falla → descarte o reempaque |
| Suma de dimensiones (L+A+A) | > 90 cm → recargo de sobredimensión en muchos couriers |
| Relación peso volumétrico / peso real | > 3x → producto "aire", casi siempre descarte |

## El caso especial: productos que se comprimen

Algunos productos voluminosos se pueden enviar comprimidos al vacío o desarmados, y eso cambia la
ecuación por completo. Textiles, cojines, organizadores plegables. Pregunta siempre al proveedor:
**"¿en qué medidas exactas viene el master carton y cuántas unidades trae?"** Con esas dos cifras
calculas el volumétrico real por unidad, no con la caja individual.

```
volumétrico_por_unidad = (L × A × H del master carton ÷ 5000) ÷ unidades_por_carton
```

## Última milla: el otro flete que se olvida

El flete nacional también depende del peso, y en LatAm los saltos de tarifa son escalonados:

| Rango | Efecto |
|---|---|
| 0-1 kg | Tarifa base |
| 1-2 kg | Salto de 15-30% |
| > 2 kg | Salto adicional y a veces zona extendida |

Quedarse en **990 g en vez de 1,05 kg** puede valer 20% del flete nacional en cada pedido. Vale la
pena pelear ese detalle con el proveedor.

## Checklist antes de cotizar

```
□ Medidas exactas del producto empacado (no del producto desnudo)
□ Peso real con empaque
□ Peso volumétrico calculado (L×A×H÷5000)
□ Medidas y unidades del master carton
□ Muestra recibida y sometida al test de caída
□ Tarifa del agente de carga por ese peso facturable, por escrito
□ Flete nacional del país destino para ese peso
□ Múltiplo recalculado con TODO lo anterior (`42`)
```

## Relacionados
`13` mapa aduanero · `16` arancel México · `41` criterios · `42` múltiplo mínimo ·
`43` qué nunca vender · `50` método de investigación · `128` proveedores en México · `153` paqueterías
