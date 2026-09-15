# 156 — Contabilización de criptoactivos

Un **criptoactivo** (Bitcoin, Ethereum, una stablecoin, etc.) es un activo digital que el negocio puede recibir como pago, comprar como inversión o tener en una billetera. La pregunta contable es: **¿cómo lo anoto en los libros y a qué valor?** No es dinero en efectivo (no es moneda de curso legal en Colombia), no es exactamente un inventario y su precio sube y baja todos los días. Aquí explicamos cómo registrarlo y medirlo de forma **auditable**; la parte tributaria (cómo se grava al venderlo) vive en el módulo **107** y debe confirmarse con el contador titulado.

## ¿Qué "es" un criptoactivo en contabilidad?

No existe una cuenta "cripto" estándar; se clasifica según **para qué lo tienes**:

| Si lo tienes para… | Se trata como… |
|---|---|
| Venderlo en el curso normal del negocio (eres exchange/comercio cripto) | Inventario |
| Mantenerlo como inversión / reserva de valor | Activo intangible (criterio NIIF más común) |
| Recibirlo como medio de pago y convertirlo pronto a pesos | Activo de corta duración, se mide a su valor |

La clasificación cambia cómo se mide y dónde aparece en los estados financieros, así que se define **antes** de registrar.

## La volatilidad: el gran problema

El precio del cripto cambia constantemente. Esto obliga a decidir **a qué valor se queda en los libros al cierre**:

| Enfoque | Qué implica |
|---|---|
| Al costo | Lo dejas a lo que te costó; reconoces pérdida si su valor cae por debajo |
| A valor razonable | Lo ajustas al precio de mercado de la fecha de cierre |

Cualquiera que uses, **guarda la evidencia del precio** (captura del mercado, fecha y hora): sin soporte del valor, no es auditable. No inventes precios de cripto.

## Recibir cripto como pago

Cuando un cliente te paga con cripto, registras la **venta al valor en pesos** de ese cripto en el momento del pago, y el criptoactivo entra a tu billetera por ese mismo valor. Si luego lo conviertes a pesos a otro precio, aparece una **ganancia o pérdida** parecida a la diferencia en cambio (módulo **155**).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un cliente te paga una venta de $2.000.000 con cripto (cifras inventadas). Registras:

| Cuenta | Débito | Crédito |
|---|---|---|
| Criptoactivos (billetera) | $2.000.000 | |
| Ingreso por ventas | | $2.000.000 |

Días después conviertes el cripto a pesos y recibes $2.150.000 porque subió:

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $2.150.000 | |
| Criptoactivos | | $2.000.000 |
| Ganancia por valoración cripto | | $150.000 |

Cifras y precios inventados; cualquier valoración o conversión se hace con `Matematicas_lushows` y el precio real con soporte.

## Errores comunes

- **No definir la clasificación** (inventario vs. intangible) antes de registrar.
- **No guardar evidencia del precio** y la fecha: lo vuelve no auditable.
- **Registrarlo como "caja"**: no es efectivo ni moneda de curso legal en Colombia.
- **Olvidar la ganancia/pérdida** al convertir cripto a pesos.
- **Asumir la tributación**: cómo se grava va en el módulo **107** y lo confirma el contador titulado.

## Conexión con otros módulos

- La tributación de los criptoactivos se trata en el módulo **107**.
- La ganancia/pérdida por conversión es prima hermana de la diferencia en cambio (**155**).
- Según la clasificación, conecta con inventarios (**30**) o con intangibles/activos.
- La valoración se reporta en estados financieros (**20**, **21**).
- Toda valoración, conversión y precio → `Matematicas_lushows` con soporte real.

## Siguiente paso típico

Define para qué tienes el cripto (inventario, inversión o medio de pago), fija y documenta el criterio de medición, guarda evidencia del precio en cada fecha y consulta la parte tributaria en el módulo **107** con tu contador titulado.
