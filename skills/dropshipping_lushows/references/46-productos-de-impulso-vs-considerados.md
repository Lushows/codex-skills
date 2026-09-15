# Productos de impulso vs considerados (el umbral de precio)

## El umbral

Existe un precio por encima del cual el cliente deja de comprar con el pulgar y empieza a
**pensar**: abre otra pestaña, compara, pregunta, lo deja para después. Ese punto no es el mismo en
todos los países ni en todos los métodos de pago.

Cruzar el umbral no está prohibido. Lo que está prohibido es cruzarlo **sin cambiar nada más**:
si subes el precio a zona considerada, tienes que agregar prueba, garantía, financiación o marca.

## Umbral aproximado por país (orientativo, verificar con tus propios datos)

| País | Impulso puro | Zona de fricción | Considerado |
|---|---|---|---|
| Perú | < S/ 90 | S/ 90-180 | > S/ 180 |
| Colombia | < $90.000 COP | $90.000-190.000 | > $190.000 |
| México | < 600 MXN | 600-1.300 MXN | > 1.300 MXN |
| Chile | < $25.000 CLP | $25.000-55.000 | > $55.000 |
| España | < 25 € | 25-55 € | > 55 € |
| EE.UU. | < USD 30 | USD 30-70 | > USD 70 |

Estos rangos son **órdenes de magnitud**, no cifras auditadas: verifica con tu propia curva de CVR
por precio. La regla que sí es sólida: el CVR cae de forma no lineal al cruzar el umbral, no de
forma proporcional.

## Cómo se comporta el CVR alrededor del umbral

| Zona | CVR prepago típico | Qué necesita la página |
|---|---|---|
| Impulso puro | 2,5-4,0% | Foto, precio, botón. Nada más |
| Fricción | 1,5-2,5% | Prueba social, garantía, envío claro |
| Considerado | 0,8-1,8% | Reseñas reales, comparativa, financiación, soporte |

Un producto de zona considerada vendido con página de impulso convierte como si fuera de zona
considerada **sin** los elementos que la sostienen: es decir, mal en ambos lados.

## La trampa del ticket bajo

Bajar el precio para quedar en zona de impulso parece obvio. No lo es: con CPM de 4,50 USD en
México y CVR de 3%, tu CPA es USD 6,82. Si tu ticket es USD 12, el techo de CAC no alcanza.

| Ticket | Múltiplo necesario México (conservador 3,74x) | Costo máximo en bodega |
|---|---|---|
| 399 MXN | 3,74x | 107 MXN — casi imposible con producto útil |
| 699 MXN | 3,74x | 187 MXN — posible |
| 1.099 MXN | 3,74x | 294 MXN — cómodo |
| 1.599 MXN | 3,74x | 428 MXN — zona considerada, exige más página |

Por eso el bundle existe. Ver `218`.

## Cómo subir el ticket sin salirse del impulso (las 5 palancas)

| Palanca | Mecánica | Efecto en CVR |
|---|---|---|
| **Bundle** | 2-3 piezas complementarias a precio "de paquete" | Neutro o positivo si el valor se ve |
| **2x1 / 3x2** | El cliente decide cantidad, no si comprar | Positivo en AOV, neutro en CVR |
| **Meses sin intereses (MSI)** | 1.099 MXN se vuelven "183 al mes × 6" | Muy positivo en México |
| **Envío gratis sobre X** | Empuja a subir el carrito | Positivo en AOV |
| **Upsell post-compra** | No toca el CVR de la primera decisión | Gratis, siempre hacerlo |

El MSI es la palanca más potente en México y es estacional: en Buen Fin (13-17 nov 2026) el
consumidor mexicano **espera** MSI. No tenerlo en esa ventana es regalar conversión. Ver `195`.

## Señales de que tu producto es considerado aunque el precio sea bajo

El precio no es lo único que activa la deliberación:

| Señal | Ejemplo |
|---|---|
| Riesgo percibido de salud o piel | Cosmética, cualquier cosa que toque el cuerpo |
| Requiere compatibilidad | "¿Sirve para mi celular?" |
| Se compra para otro | Regalos: el cliente teme equivocarse |
| Tiene curva de aprendizaje | "¿Y si no sé usarlo?" |
| Alternativa conocida más barata | Ver `43` y `57` |

Cualquiera de estas te obliga a página de considerado aunque cobres 400 MXN.

## Qué cambia en la página según la zona

| Elemento | Impulso | Considerado |
|---|---|---|
| Largo de página | Corta, 1 scroll | Larga, con secciones |
| Reseñas | 3-5 bastan | 20+, con foto |
| Garantía | Mencionada | Explicada y visible |
| FAQ | No necesaria | Obligatoria, 6-10 preguntas |
| Comparativa | No | Sí, contra la alternativa |
| Financiación | No | Sí, destacada |

La construcción visual de esa página: invoca `desingweb-lushows`.

## El error de cambiar de zona sin darse cuenta

Subes el precio de 699 a 1.099 MXN para mejorar el margen. El CVR pasa de 3,0% a 1,7%. Tu CPA sube
de USD 6,82 a USD 12,03 y el margen extra se evapora. Si no mediste antes y después, concluyes "el
producto se quemó" cuando en realidad lo cambiaste de zona.

**Regla:** cada cambio de precio es un test nuevo. Nunca cambias precio y creativo la misma semana.

## Aplicado al proyecto activo (México, dic-2026)

El bundle de ~1.099 MXN cae en la **zona de fricción alta**, casi en considerado. Decisiones que se
derivan de eso, no negociables:

1. Página con prueba social real y garantía visible, no landing de una pantalla.
2. MSI activo desde el 1 de noviembre, obligatorio durante Buen Fin.
3. Motor de compra = dolor, no deseo. Ver `45`.
4. Medir CVR por rango de precio si se prueban dos versiones del bundle.

Con capital menor a USD 500, no hay margen para descubrir en diciembre que el precio estaba en la
zona equivocada: eso se prueba en octubre con presupuesto de validación de USD 50-100.

## Relacionados
`42` múltiplo mínimo · `45` dolor vs deseo · `47` factor wow · `49` estacionalidad ·
`57` Mercado Libre · `195` MSI · `218` bundle · `233` cuántos tiros
