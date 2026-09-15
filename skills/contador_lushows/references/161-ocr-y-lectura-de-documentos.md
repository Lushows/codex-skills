# 161 — OCR y lectura de documentos con IA

La tarea más repetitiva de toda contabilidad es **pasar los datos del papel (o el PDF) al sistema**: número de factura, NIT, fecha, base, IVA, total. Hacerlo a mano es lento y se presta para errores de dedo. La IA hace esto con **OCR** (reconocimiento óptico de caracteres: convierte una imagen en texto) y, encima, con modelos que **entienden** dónde está cada dato. El resultado: la IA propone los campos y el contador valida. Nunca al revés.

Un término clave: **extracción estructurada** es cuando la IA no solo "lee" la imagen, sino que devuelve los datos ordenados en casillas (NIT aquí, total allá), listos para meter al software contable.

## Qué puede leer hoy

| Documento | Qué extrae | Cuidado especial |
|---|---|---|
| Factura electrónica (XML/PDF) | Emisor, NIT, CUFE, base, IVA, INC, total | El XML es la fuente legal, no la imagen |
| Factura física o foto | Mismos campos | La foto borrosa daña la lectura |
| Extracto bancario | Fecha, descripción, valor, saldo | Formatos distintos por banco |
| Recibos y tirillas | Fecha, valor, NIT (si lo tiene) | Suelen no servir como soporte fiscal |
| Documento soporte (compras a no obligados) | Datos del proveedor y valor | Tiene reglas propias en Colombia |

## El paso que NO se puede saltar: validación

La IA puede confundir un 8 con un 0, perder un dígito del NIT o leer mal una fecha. Por eso toda extracción pasa por **validaciones automáticas + ojo humano**:

- **Cuadre aritmético**: base + IVA + INC = total (verificado en código, `Matematicas_lushows`).
- **NIT con dígito de verificación** correcto.
- **CUFE/CUDE** existe y corresponde (en factura electrónica DIAN).
- **Fecha** dentro del periodo y formato válido.
- **Duplicados**: que no se registre dos veces la misma factura.

Si algo no cuadra, va a una **bandeja de excepciones** para revisión humana.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

La IA lee una factura y devuelve: base $100.000, IVA $19.000, total $119.000. La validación recalcula 100.000 + 19.000 = 119.000 ✔. En otra, lee base $100.000, IVA $19.000, total $190.000 ✘ → no cuadra, se manda a revisión: probablemente leyó mal el total. Cifras inventadas; el cuadre siempre se ejecuta en código.

## Errores comunes

- **Aceptar lo que dice la IA sin revalidar el cuadre**: el error entra silencioso a los libros.
- **Usar la imagen en vez del XML** en factura electrónica: el XML es lo que vale ante la DIAN.
- **No detectar duplicados**: se infla el gasto y el IVA descontable.
- **Confiar en fotos malas**: basura entra, basura sale.
- **Guardar solo los datos y botar el soporte**: todo asiento necesita su documento (auditabilidad, módulo 167).

## Conexión con otros módulos

- Una vez extraídos los datos, la IA puede **sugerir el asiento**: módulo **163**.
- El **soporte de cada asiento** y su archivo es regla de oro: módulos **01** y **167**.
- La **factura electrónica DIAN** (CUFE, validación, XML) se trata en el bloque de facturación; el detalle conversacional de captura está en `AVIS_lushows`.
- Todo recálculo de cuadre y dígito de verificación: `Matematicas_lushows`.
- Lo básico de estas herramientas: módulos **84–86**.

## Siguiente paso típico

Toma un lote de 20 facturas reales, pásalas por la herramienta de OCR que uses y **revisa una por una** contra el original. Mide cuántas leyó perfecto y cuántas fallaron: ese porcentaje te dice cuánto puedes confiar y dónde poner el ojo humano.
