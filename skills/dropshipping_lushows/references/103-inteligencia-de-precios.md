# Inteligencia de precios

> Vigencia: 14-sep-2026. Los cálculos de margen y punto de equilibrio exactos se ejecutan con
> `Matematicas_lushows`; la estrategia de precio de negocio con `economist_lushows`. Aquí se MAPEA
> el mercado antes de decidir.

## La regla de orden

**Primero mapeas, después decides.** Poner precio sin haber mapeado el rango del nicho en tu país es
la forma más rápida de descubrir, con dinero real, que estabas 40% arriba o dejando margen en la
mesa.

## Los cinco precios que debes conocer

| Precio | Dónde lo obtienes | Qué te dice |
|---|---|---|
| **P1 — Precio del competidor dropshipper** | Landings (`92`, `93`) | El techo que el mercado ya paga con este tipo de venta |
| **P2 — Precio en marketplace (Mercado Libre, Amazon MX)** | Búsqueda directa | El **precio de referencia** del cliente. El más peligroso |
| **P3 — Precio en tienda física / retail** | Visita o búsqueda | Ancla de "producto de verdad" |
| **P4 — Costo de proveedor local MX** | Cotización | Tu piso |
| **P5 — Costo de importación (producto + flete + arancel + IVA)** | `16`, cotización | Tu piso alternativo |

## El peligro de P2

Si tu producto se encuentra en Mercado Libre México a 249 MXN y tú lo vendes a 1.099 MXN, **el
cliente lo va a encontrar**. Va a aparecer en tus comentarios (`95`: "en Mercado Libre está a la
mitad") y tu conversión se cae.

Salidas posibles, en orden de solidez:

| Salida | Cómo funciona | Dificultad |
|---|---|---|
| **Bundle** que no existe en el marketplace | Vendes un conjunto, no una pieza comparable | Media |
| **Marca y presentación** propia | El empaque y la experiencia justifican | Media-alta |
| **Entrega y garantía** verificables | "48 h desde México, cambio sin preguntas" | Baja, pero replicable |
| Producto **no listado** en marketplaces | Buscas lo que no está | Depende del sourcing |
| Servicio/contenido añadido | Guía, soporte, comunidad | Baja |

La única salida realmente sólida con un bundle de ~1.099 MXN es la **primera combinada con la
tercera**: un conjunto que no se puede comparar pieza a pieza, entregado rápido desde México.

## Procedimiento de mapeo (30 min)

1. Lista 8-10 competidores del nicho en México (`82`, `101`).
2. Para cada uno saca el precio simple y el de bundle desde `/products.json` (`93`).
3. Busca el mismo producto (o el más parecido) en **Mercado Libre MX** y **Amazon MX**. Anota el
   precio más bajo con envío incluido y la reputación del vendedor.
4. Cotiza proveedor local y/o importación.
5. Llena la tabla.

| Fuente | Producto/presentación | Precio MXN | Envío | Precio final | Fecha |
|---|---|---|---|---|---|
| Competidor 1 | 1x | | | | |
| Competidor 1 | bundle 2x | | | | |
| Competidor 2 | … | | | | |
| Mercado Libre | pieza suelta | | | | |
| Amazon MX | | | | | |
| Proveedor local | costo | | | | |

6. Calcula el **rango**: mínimo, mediana y máximo del precio final de los dropshippers.
7. Decide tu posición dentro de ese rango.

## Dónde posicionarte

| Posición | Cuándo tiene sentido | Riesgo |
|---|---|---|
| **Por debajo de la mediana** | Solo si tienes ventaja real de costo | Guerra de precio; con capital bajo la pierdes |
| **En la mediana** | Caso normal si tu oferta es comparable | Ninguna ventaja: compites por creativo |
| **Por encima de la mediana** | Si tu bundle, entrega o garantía son claramente mejores | Necesitas landing y prueba social a la altura |

Con capital menor a USD 500, **no compitas por precio**. No tienes volumen para negociar costo ni
colchón para aguantar una guerra. Compite por oferta (`104`) y por entrega.

## La relación precio ↔ CAC

El precio no se decide solo mirando al competidor: se decide contra tu **techo de CAC** (`11`).

```
margen_bruto_unitario = precio_venta − costo_producto − envio − comisión_pago − impuestos
techo_CAC = margen_bruto_unitario × (1 − margen_objetivo)
```

Si el mapeo dice que el nicho vende a 899 MXN y tu techo de CAC con ese precio es de 180 MXN, pero el
CPM en México (base USD 4,50, Q4 5,40-6,75) y tu conversión te dan un CAC de 320 MXN, **el precio no
te alcanza**: o subes el ticket con bundle, o cambias de producto. Ejecuta el cálculo exacto con
`Matematicas_lushows`, no de cabeza.

## Precio psicológico en México

| Práctica | Nota |
|---|---|
| Terminaciones en 9 (1.099, 899, 1.299) | Estándar; el mercado ya lo lee como precio de oferta |
| Precio tachado (`compare_at_price`) | Casi universal. Si el tachado no es creíble, resta |
| **MSI** | Cambia la percepción: "3 pagos de 366" pesa menos que "1.099" |
| Precio con IVA incluido | En B2C mexicano se comunica el precio final |
| "Envío gratis" | Casi obligatorio; se absorbe en el precio |

Durante el **Buen Fin (13-17 nov 2026)**, los MSI son el argumento dominante. Mapea con `82` (filtro
de fecha nov-2025) cuántos meses ofrecieron tus competidores el año pasado.

## Vigilancia continua

Los precios se mueven, sobre todo en Q4. Registra el precio de tus 5 competidores **cada semana**
durante octubre y noviembre:

| semana | comp1 | comp2 | comp3 | comp4 | comp5 | mediana |
|---|---|---|---|---|---|---|

Cuando la mediana baje dos semanas seguidas, hay guerra de precio empezando. Decisión: o te sales de
la comparación con un bundle distinto, o aceptas menos margen sabiendo cuánto. Nunca lo descubras por
la caída de ventas.

## Relacionados
`93` catálogo del competidor · `104` oferta y bundles · `102` landings · `11` techo de CAC · `06` la ecuación del negocio · `20` playbook México
