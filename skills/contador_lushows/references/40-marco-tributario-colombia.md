# 40 — Marco tributario de Colombia: quién declara qué

Antes de liquidar un solo peso de impuestos hay que entender el **mapa**: en Colombia los impuestos no los cobra una sola entidad. Hay impuestos **nacionales** (los administra la DIAN — la Dirección de Impuestos y Aduanas Nacionales) e impuestos **territoriales** (los cobran los departamentos y, sobre todo, los municipios). Saber cuál es cuál evita que un negocio pague de más, deje de pagar lo que debe, o presente una declaración en la entidad equivocada.

Este módulo es el "índice" del bloque de impuestos. No liquida nada: te ubica. La liquidación de cada tributo vive en los módulos siguientes (41 a 49).

> **Regla de oro del bloque:** las tarifas, la UVT y los topes **cambian todos los años** (la UVT cada enero, las tarifas con cada reforma tributaria). Aquí explicamos el CONCEPTO y la MECÁNICA. Cuando necesites un valor exacto, **verifica la tarifa/UVT vigente del año en la DIAN** y manda el cálculo a `Matematicas_lushows` para que se haga con `decimal`, nunca de cabeza.

## Términos que debes conocer
- **UVT (Unidad de Valor Tributario):** una "unidad de medida" en pesos que la DIAN actualiza cada año. Muchos topes y sanciones se expresan en UVT en vez de en pesos, para que se ajusten solos con la inflación. *Verifica el valor de la UVT del año en la DIAN.*
- **Sujeto pasivo:** quién debe pagar el impuesto (la persona o empresa).
- **Hecho generador:** el evento que hace nacer el impuesto (vender, tener una propiedad, obtener renta).
- **Base gravable:** la cifra sobre la cual se aplica la tarifa.
- **Tarifa:** el porcentaje (o valor) que se aplica a la base.

## Impuestos nacionales (los administra la DIAN)
| Impuesto | Sobre qué recae | Quién lo declara | Módulo |
|---|---|---|---|
| Impuesto de renta | La utilidad / renta del año | Personas naturales y jurídicas | 42 |
| IVA (Impuesto al Valor Agregado) | El consumo de bienes y servicios gravados | Responsables de IVA | 41 |
| Retención en la fuente | Recaudo anticipado de otros impuestos | Agentes retenedores | 43 |
| Impuesto al consumo (INC) | Ciertos bienes/servicios (p. ej. restaurantes) | Responsables del INC | 41 (relación) |

## Impuestos territoriales (los cobran municipios/departamentos)
| Impuesto | Sobre qué recae | Quién lo cobra | Módulo |
|---|---|---|---|
| ICA (Industria y Comercio) | Ingresos por actividad económica en el municipio | El municipio | 44 |
| Avisos y tableros | Complementario al ICA (publicidad visible) | El municipio | 44 |
| Predial | Propiedad de inmuebles | El municipio | 44 (relación) |
| Vehículos | Propiedad de vehículos | El departamento | 44 (relación) |

## Cómo saber qué le aplica a tu negocio
1. **¿Vende bienes o servicios gravados con IVA?** → es probable que sea **responsable de IVA** (antes "régimen común"). Ver 41.
2. **¿Le hacen pagos a proveedores/empleados?** → puede ser **agente de retención**. Ver 43.
3. **¿Genera utilidades?** → declara **renta** (jurídica casi siempre; natural según topes). Ver 42.
4. **¿Tiene actividad económica en un municipio?** → paga **ICA** en ese municipio. Ver 44.
5. **¿Está obligado a facturar?** → factura electrónica DIAN. Ver 45.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Sabores del Valle SAS", restaurante en Cali:
- Renta → declara ante la DIAN (es persona jurídica).
- IVA → si vende productos gravados; **ojo:** los restaurantes suelen estar en **impuesto al consumo**, no IVA (verifica el régimen aplicable a su actividad).
- Retención en la fuente → si le paga a un proveedor por encima de la base, debe retener.
- ICA → paga en el municipio de Cali sobre sus ingresos.
- Factura electrónica → obligatoria.

Cada uno tiene **su propio formulario, su periodicidad y su plazo**. No se mezclan.

## Errores comunes
- Creer que "la DIAN cobra todo": el **ICA es municipal**, no se declara en la DIAN.
- Confundir **IVA** con **impuesto al consumo** (son distintos; restaurantes suelen ir a consumo).
- Asumir tarifas o UVT "de memoria": **siempre cambian**, siempre se verifican.
- Pensar que si el negocio es pequeño "no aplica nada": casi siempre aplica ICA y facturación.

## Conexión con otros módulos
- **41 (IVA)**, **42 (Renta)**, **43 (Retención)**, **44 (ICA)** — el detalle de cada tributo de la tabla.
- **45 (Facturación electrónica)** — la base documental de casi todos los impuestos.
- **46 (Calendario)** y **47 (Presentación)** — el cuándo y el cómo.
- **Matematicas_lushows** — toda liquidación de valores.
- **economist_lushows** — la planeación tributaria estratégica (qué régimen conviene) se decide allá; aquí registramos y reportamos.

## Siguiente paso típico
Identificar cuáles de estos impuestos le aplican al negocio concreto y abrir el módulo de cada uno. El primero suele ser **41 (IVA)** o **42 (Renta)**.
