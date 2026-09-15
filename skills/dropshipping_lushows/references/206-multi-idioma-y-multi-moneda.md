# Multi-idioma y multi-moneda

> Vigencia: 14-sep-2026. Implementación técnica de rutas y etiquetas: invoca `desingweb-lushows`.
> Obligaciones fiscales por país: invoca `contador_lushows`.

## La regla que ahorra meses

**No abras un segundo idioma hasta que el primero sea rentable.** Multiplicar idiomas multiplica
errores, soporte, devoluciones y costos legales, sin multiplicar ventas. Casi siempre, el operador
que "abre a toda LatAm" termina con seis mercados mediocres en vez de uno bueno.

| Situación | Veredicto |
|---|---|
| México funcionando, quieres Colombia | **Espera.** Es el mismo idioma pero otro modelo de pago y otra logística. `193` |
| España funcionando, quieres Portugal | Idioma nuevo, IVA nuevo, transportadora nueva. Proyecto aparte |
| Brasil | **Portugués no es español con acento.** Todo se rehace. `28` |
| Estados Unidos hispano | Mismo idioma, otro país fiscal y logístico |

## Moneda: la regla no negociable

**Cobra en la moneda local del comprador. Siempre.**

| Práctica | Efecto |
|---|---|
| Tienda mexicana cobrando en MXN | Correcto |
| Tienda mexicana cobrando en USD | Conversión desplomada: se lee como "producto importado, tarda meses" |
| Mostrar en MXN y cobrar en USD | Peor: el cliente ve un cargo distinto en su estado de cuenta y hace contracargo |
| Conversor automático que muestra precios con decimales raros ($1,098.37) | Se ve automático y barato |

Si la plataforma solo te deja cobrar en una moneda, **que sea la del mercado principal**, y no
vendas a los demás hasta poder cobrar en la suya.

## Precios psicológicos por mercado

Un precio convertido matemáticamente se ve mal. Los precios se **fijan**, no se convierten.

| Mercado | Precio bien fijado | Precio convertido (mal) |
|---|---|---|
| México | $1,099 MXN | $1,098.37 MXN |
| Colombia | $189.900 COP | $187.442 COP |
| España | 54,90 € | 54,37 € |
| Chile | $49.990 CLP | $48.712 CLP |

Además, cada mercado tiene su convención de separadores y su símbolo. Un precio escrito a la manera
de otro país es una señal inmediata de tienda extranjera.

## Idioma: qué se traduce de verdad

Traducir no es pasar el texto por un traductor. Si abres un idioma, se rehace:

| Elemento | ¿Se traduce o se reescribe? |
|---|---|
| Promesa del encabezado | **Se reescribe.** El dolor se dice distinto en cada cultura. `181` |
| Texto de producto | **Se reescribe** desde los dolores locales. `183` |
| Reseñas | Se traducen, pero con nombres y ciudades del mercado. `185` |
| FAQ | Se reescribe: las dudas son otras (plazos, pagos, aduana). `187` |
| Páginas legales | **Se rehacen** según la ley del país. `207` |
| Correos transaccionales | Se reescriben |
| Video | Subtítulos nuevos como mínimo; locución nueva idealmente. `186` |
| Atención al cliente | Persona que hable el idioma |

Si no puedes hacer las ocho, no abras el idioma.

## Variantes del español: sí importan

El español mexicano, el colombiano y el de España no son intercambiables en copy de venta.

| Concepto | México | Colombia | España |
|---|---|---|---|
| Tratamiento | Tú | Tú / usted según nicho | Tú |
| Envío | "Te llega en 2 a 4 días hábiles" | "Te llega en 2 a 5 días hábiles" | "Recíbelo en 24-48 h" |
| Pago diferido | "Meses sin intereses" | "Cuotas" | "A plazos" / "Pago aplazado" |
| Descuento | "Descuento", "precio de Buen Fin" | "Descuento", "promoción" | "Rebaja", "oferta" |
| Dinero | Pesos, $ | Pesos, $ | Euros, € |
| "Genial" | "Está padrísimo" | "Está bacano" | "Está genial" |

Usa el registro local con moderación: el modismo forzado suena peor que el neutro. La regla segura
es **neutro en lo formal y local en lo cotidiano** (envíos, pagos, unidades).

## Lo técnico que no puedes ignorar

| Requisito | Por qué |
|---|---|
| URL distinta por idioma (`/es`, `/pt`) o dominio propio | Sin eso, el buscador y las plataformas se confunden |
| Etiquetas `hreflang` | Evita que se sirva el idioma equivocado |
| Detección por país con opción de cambiar | La detección automática sin opción de salir es una trampa |
| Que el cambio de idioma no pierda el carrito | Error clásico |
| Moneda coherente entre página, carrito y pasarela | `190` |

## El costo real de abrir un mercado

| Concepto | Nota |
|---|---|
| Reescribir todo el copy | Días de trabajo o pago a un redactor nativo |
| Páginas legales del país | `207`, y encuadre fiscal con `contador_lushows` |
| Pasarela local | Alta, documentos, tiempo. `192`, `193`, `194` |
| Logística local | Transportadora, plazos, tarifas |
| Soporte en el idioma | Persona o bot entrenado |
| **IOSS si es la UE** | €20-300/mes + alta €99-400. `194` |
| Impuestos y facturación locales | Variable |

Con capital menor a USD 500, abrir un segundo mercado es matemáticamente imposible sin sacrificar el
primero. `11`.

## Cuándo sí abrir el segundo mercado

Las cuatro condiciones, todas:

1. El primer mercado es **rentable** con margen medido, no con ROAS estimado.
2. Hay caja para el inventario y los anuncios del nuevo mercado **sin tocar** los del primero.
3. Tienes resuelta la logística local (no vas a enviar desde el país 1 al país 2).
4. Tienes quién escriba y atienda en ese idioma.

Si falla una, no lo abras.

## Para el proyecto de diciembre 2026

**Un idioma: español mexicano. Una moneda: MXN. Un país: México.**

Nada de conversor de monedas, nada de traducción automática, nada de "también vendo a Colombia".
Toda la energía en un mercado de 77,2 millones de compradores digitales creciendo 19,2% al año.
Ese mercado no se queda chico. `20`, `192`.

## Relacionados
`192` pasarelas México · `193` pasarelas LatAm · `194` pasarelas Europa · `207` la tienda legal · `10` cómo se elige un país
