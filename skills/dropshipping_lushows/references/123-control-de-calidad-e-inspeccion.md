# Control de calidad e inspección

> Vigencia: septiembre 2026. AQL según ISO 2859-1 / ANSI-ASQ Z1.4. Verifica tarifas con la firma.

La inspección es el único momento en que puedes rechazar mercancía **antes de pagarla y antes de que
cruce un océano**. Quien se la salta descubre el problema cuando ya tiene 500 unidades malas en su
bodega y cero palanca.

## Los cuatro tipos de inspección

| Tipo | Cuándo | Qué detecta | Costo típico |
|---|---|---|---|
| **Muestra pre-producción (PPS)** | Antes de producir el lote | Que entendieron la especificación | Costo de muestra + courier |
| **DUPRO** (durante producción, ~30% hecho) | A mitad | Errores sistemáticos a tiempo de corregir | US$150-350/día |
| **PSI / Final Random Inspection** | Producción 100% terminada, 80% empacada | Defectos, cantidad, empaque, marcado | **US$150-350/día** |
| **Supervisión de carga (LS)** | Al cargar el contenedor | Que suba lo correcto y bien estibado | US$150-350/día |

**La mínima viable es PPS + PSI.** El PPS evita producir mal; el PSI evita embarcar mal.

## Qué es AQL y cómo se usa sin saber estadística

AQL (Acceptable Quality Limit) define **cuántas unidades se revisan** de un lote y **cuántos defectos
se aceptan** antes de rechazarlo todo. Es el lenguaje estándar; decirlo te posiciona como comprador
serio inmediatamente.

Los defectos se clasifican en tres:

| Categoría | Definición | AQL típico consumo |
|---|---|---|
| **Crítico** | Peligroso para el usuario o ilegal | 0 |
| **Mayor** | El cliente lo devolvería | 2,5 |
| **Menor** | Defecto cosmético que no impide el uso | 4,0 |

Tamaño de muestra según nivel de inspección general II (aproximado, ISO 2859-1):

| Tamaño del lote | Unidades a revisar | Aceptar/Rechazar (Mayor 2,5) |
|---|---|---|
| 151-280 | 32 | 2 / 3 |
| 281-500 | 50 | 3 / 4 |
| 501-1.200 | 80 | 5 / 6 |
| 1.201-3.200 | 125 | 7 / 8 |

Lectura: en un lote de 500 unidades se revisan 50; si aparecen 3 defectos mayores se acepta, con 4 se
rechaza el lote completo. Verifica la tabla exacta con tu inspector antes de firmar.

**Cómo se escribe en la PI:** "Inspection: ISO 2859-1, General Level II, AQL Critical 0 / Major 2.5 /
Minor 4.0. Balance payable against approved inspection report."

## Quién inspecciona

| Opción | Costo | Cuándo |
|---|---|---|
| **Tu agente** | Incluido en su fee | Lotes chicos, producto simple. Ver `116` |
| **Firma de inspección de tercero** (SGS, Bureau Veritas, TÜV, QIMA y similares) | US$150-350 por hombre-día | Lotes de US$3.000+, producto técnico |
| Freelance inspector local | US$80-200/día | Intermedio. Verifica referencias |
| El propio proveedor | "Gratis" | **No es inspección.** Es un informe de sí mismo |
| Tú al recibir en destino | Gratis | Demasiado tarde. Ya pagaste y ya importaste |

**Regla de costo:** si el lote vale más de US$2.500, una inspección de tercero de US$250 es el 10% y
paga sola. Si vale US$600, que la haga el agente.

## El checklist de inspección (dáselo escrito al inspector)

1. **Cantidad**: conteo real vs orden, por variante y color.
2. **Especificación**: material, medidas con calibrador, peso, color contra referencia física o
   Pantone.
3. **Función**: si enciende, si cierra, si soporta peso. Define la prueba y el número de unidades a
   probar.
4. **Acabado**: rebabas, costuras, rayones, pintura.
5. **Empaque**: caja individual correcta, manual incluido, sellado, inserto tuyo presente.
6. **Marcado**: código de barras legible y correcto, etiqueta de país de origen, advertencias
   legales, shipping marks en la caja máster.
7. **Caja máster**: unidades por caja, peso bruto real, medidas reales (esto es tu flete).
8. **Prueba de caída (drop test)** de la caja máster si el producto es frágil.
9. **Fotos**: mínimo 30, incluyendo defectos encontrados.
10. **Veredicto**: PASS / FAIL / PASS WITH CONDITIONS, firmado.

El punto 7 es el que más plata te ahorra y el que más se olvida: si la caja máster pesa 22 kg y no 18,
tu costo de flete sube 22% y lo descubres con la factura. Ver `121`.

## El procedimiento completo

```
1. Escribe la especificación en la PI. Sin esto no hay nada que inspeccionar. Ver 113
2. PPS: muestra de pre-producción. Apruebas por escrito y guardas una unidad sellada
   como "golden sample". Ver 124
3. Producción.
4. Avisas la inspección con 3-5 días. El proveedor debe tener 100% producido y 80% empacado.
5. Inspección. Reporte en 24-48 h.
6. Si PASS → pagas el saldo, embarcan.
   Si FAIL → el proveedor retrabaja o repone a su costo, y se re-inspecciona
   (la re-inspección la paga él: escríbelo en la PI).
7. Supervisión de carga si es contenedor completo.
```

**Nunca pagues el saldo antes del reporte.** Es la única palanca real que tienes.

## La golden sample

Guarda una unidad de la muestra aprobada, sellada, con fecha y firma. Es el patrón contra el que se
compara toda producción futura. Sin golden sample, "el color está distinto" es opinión; con golden
sample es un hecho verificable. Manda una copia al proveedor y quédate con una.

## Qué hacer cuando la inspección falla

1. **No pagues el saldo.** Punto de partida de toda negociación.
2. Pide el reporte completo con fotos y clasificación de defectos.
3. Decide entre: retrabajo (el proveedor arregla), reposición (produce de nuevo lo malo), descuento
   (aceptas con nota de crédito) o cancelación con devolución del depósito.
4. **El retrabajo suele ser la mejor opción** si el defecto es cosmético y el tiempo aprieta.
5. Documenta todo por escrito. Usa la plantilla de reclamo de `119`.
6. Si estás en Trade Assurance, abre la disputa **antes** de confirmar recepción. Ver `113`.

## Control de calidad sin importar: el 3PL y Dropi

Cuando compras local (Dropi MX, mayorista mexicano) no hay inspección de fábrica, pero sigue habiendo
control de calidad. Qué hacer:

1. **Pide el producto a tu propia casa** antes de venderlo. Siempre. Sin excepción.
2. Revisa una unidad de cada lote nuevo que entre a tu 3PL.
3. Monitorea la **tasa de devolución y de queja por producto**. Si sube de un mes a otro, el
   proveedor cambió algo. Ver `144`.
4. Si trabajas con 3PL, pide **inspección de entrada** (recepción con conteo y fotos). Ver `134`.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Inspeccionar sin especificación escrita | No hay contra qué comparar. La inspección no sirve |
| Pagar el saldo y luego inspeccionar | Perdiste toda la palanca |
| Aceptar el "reporte de calidad" del proveedor | Es marketing |
| No revisar peso y medidas de la caja máster | Te enteras del sobrecosto de flete con la factura |
| No guardar golden sample | Todo reclamo futuro se vuelve subjetivo |
| Avisar la inspección con 1 día | El proveedor no la tendrá lista y pierdes el viaje |
| Rechazar el lote entero por defectos menores | A veces el descuento y vender es mejor negocio. Calcula |

## Para el proyecto activo (México, diciembre 2026)

Con stock local, tu control de calidad son tres cosas: **(1) comprar una muestra de cada componente
del bundle a tu casa antes de lanzar, (2) fotografiar y pesar cada componente, (3) medir la tasa de
devolución por SKU desde la primera semana.**

Si el bundle de ~1.099 MXN se arma con tres productos, el riesgo se multiplica por tres: basta que
uno llegue mal para que la devolución sea del bundle completo. Pide muestra de los tres.

## Relacionados
Ver `113`, `116`, `119`, `120`, `121`, `124`, `134`, `144`.
