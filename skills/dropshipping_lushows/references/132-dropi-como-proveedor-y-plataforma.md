# Dropi como proveedor y plataforma

> Vigencia: septiembre 2026. Comisiones, transportadoras y plazos cambian; verifica en la plataforma
> de tu país antes de modelar.

Dropi es la plataforma de dropshipping con contraentrega líder de LatAm. Opera en **12 países**:
Colombia, México, Ecuador, Perú, Chile, España, Argentina, Panamá, Paraguay, Venezuela, Guatemala y
Costa Rica. Cada país tiene **catálogo, transportadoras y billetera propios** — no son vasos
comunicantes.

Es la respuesta correcta a la pregunta "quiero arrancar en LatAm sin capital". No es la respuesta a
"quiero el mejor margen".

## Qué es exactamente

| Dropi ES | Dropi NO ES |
|---|---|
| Catálogo de proveedores con stock local | Un proveedor único |
| Integración con transportadoras | Una transportadora |
| Gestor de órdenes y guías | Tu tienda |
| Billetera que recauda el COD y te liquida | Un banco |
| Sistema de novedades y devoluciones | Garantía de entrega |

Los proveedores son terceros que cargan su stock a la plataforma. **La calidad y el stock son del
proveedor, no de Dropi.** Eso cambia cómo debes evaluar cada producto.

## Los números clave

| Concepto | Dato |
|---|---|
| Comisión | **5% sobre el precio de venta** (0% con mentor oficial) |
| Liquidación de billetera | **2-7 días hábiles tras entrega efectiva** |
| Países | 12 |
| Flete México | **MXN 120-200** |
| Flete Colombia | **USD 2,50-3,20** |
| Transportadoras MX | 99minutos (líder urbano), Estafeta, FedEx, Paquetexpress |
| Transportadoras CO | Interrapidísimo, Servientrega, Coordinadora, Envía Colvanes |

**La comisión es sobre el PRECIO DE VENTA, no sobre el costo.** Si vendes a 1.099 MXN, pagas ~55 MXN
de comisión. Súbelo más el precio de venta, sube la comisión. Modélalo.

**El 0% con mentor oficial es real pero verifica las condiciones actuales** antes de contarlo en tu
modelo financiero.

## Manual operativo: del registro a la primera venta

```
 1. Registro en Dropi del país (Dropi MX ≠ Dropi CO: cuentas separadas)
 2. Verificación de identidad y datos fiscales (RFC en MX, NIT en CO)
 3. Configurar la cuenta bancaria de liquidación
 4. Catálogo: filtrar por stock, proveedor, calificación, ciudad de despacho
 5. PEDIR MUESTRA A TU PROPIA CASA de cada producto. Innegociable.
 6. Integrar tu tienda (Shopify/Woo) o cargar órdenes manualmente / por CSV
 7. Definir precio de venta (tú lo fijas, no el proveedor). Publicar y pautar
 8. Llega una orden → la cargas o entra por integración
 9. Confirmas la orden (y en COD, confirma también por WhatsApp)
10. Dropi genera la guía y el proveedor despacha
11. Seguimiento: en tránsito → novedad → entregado / devuelto
12. Cobro COD por la transportadora → billetera → banco en 2-7 días hábiles
```

**El paso 5 es el que separa a los que ganan de los que se queman.** El catálogo tiene fotos de
proveedor; el producto real puede ser otra cosa. Ver `124`.

## La billetera: cómo funciona el flujo de caja

```
Venta COD de 1.099 MXN → cliente paga al repartidor → transportadora entrega la plata a
Dropi → Dropi descuenta costo del producto + flete + 5% comisión → el neto entra a tu
billetera → liquidas a tu banco: 2-7 días hábiles tras entrega efectiva
```

Esto significa que **tu plata vuelve entre 5 y 15 días después de la venta** (tránsito + liquidación).
Mientras tanto ya pagaste la pauta. Ese desfase es el motivo #1 por el que operaciones rentables
quiebran por caja. Ver `138`.

En **prepago** el flujo es distinto y mucho mejor: cobras tú en la web al momento, y pagas a Dropi el
costo + flete. La caja vuelve en 2-3 días (según tu pasarela) en vez de 15. **Por eso el proyecto de
México eligió prepago.** Ver `30`.

## Cómo elegir producto dentro del catálogo

| Filtro | Por qué |
|---|---|
| **Stock alto y estable** | Un quiebre en plena campaña te tumba |
| Proveedor con calificación alta y antigüedad | Ver `120` |
| Ciudad de despacho cerca de tu mercado principal | Menos tránsito, más entrega efectiva |
| **Cuántos otros lo venden** | El producto "más vendido" es el más saturado. Ver `61` |
| Peso y volumen bajos | Flete más barato y menos rotura |
| Margen sobre el PVP objetivo | Después de costo + flete + 5% + CAC |
| Producto que se explica en video de 15 s | Si no, el CAC se dispara |

**La trampa del catálogo:** los productos destacados los ve todo el mundo y los pauta todo el mundo.
El CPM sube y el margen desaparece. El producto correcto suele estar en la página 4, no en la 1.

## Novedades: el concepto que hay que dominar

Una "novedad" es cuando la transportadora no pudo entregar: nadie contesta, dirección errada, cliente
pide reprogramar, rechaza. Cada novedad tiene ventana de resolución.

| Práctica | Impacto |
|---|---|
| Revisar novedades **todos los días** | Recupera 20-40% de las entregas fallidas |
| Llamar/escribir al cliente al ver la novedad | La mejor herramienta de recuperación |
| Confirmar dirección **antes** de despachar | Elimina la mitad de las novedades |
| Dejar la novedad sin gestionar | Se vuelve devolución y pagas flete de ida y vuelta |

**La gestión de novedades es el trabajo operativo más rentable del COD.** No es glamoroso. Es donde
está el dinero.

## Devoluciones: modela el costo desde el día 1

En COD, la devolución te cuesta flete de ida y de vuelta y no ingresas nada. Si tu tasa de entrega es
del 75%, una de cada cuatro ventas es pura pérdida de flete.

```
Costo real de flete por venta ENTREGADA =
    flete_ida + (tasa_devolución / tasa_entrega) × (flete_ida + flete_vuelta)
```

Ejemplo con flete MXN 150, entrega 75%:
`150 + (0,25/0,75) × 300 = 150 + 100 = MXN 250` por venta entregada.

**Tu flete real es 250, no 150.** Quien modela con 150 cree que gana y pierde. Para el cálculo con tus
números invoca `Matematicas_lushows`.

## Dropi vs comprar directo al mayorista

| Criterio | Dropi | Mayorista propio |
|---|---|---|
| Capital inicial | **$0** | Medio-alto |
| Costo de producto | Mayor | **Menor** |
| Comisión | 5% del PVP | 0 |
| Riesgo de inventario | **Ninguno** | Tuyo |
| Control de calidad | Del proveedor | **Tuyo** |
| Empaque y marca | Limitado | **Tuyo** |
| Velocidad de arranque | Hoy | Días-semanas |
| Escalabilidad de margen | Techo bajo | **Alto** |

Regla: **Dropi para validar, mayorista o lote propio para escalar.** Ver `136`.

## Los 10 errores que se cometen con Dropi

| Error | Consecuencia |
|---|---|
| Vender sin haber recibido una muestra | Devoluciones y reseñas malas |
| Elegir el producto más vendido del catálogo | Compites contra 200 personas por el mismo CPM |
| No gestionar novedades a diario | Devoluciones evitables |
| Modelar el flete sin contar la devolución | Crees que ganas y pierdes |
| Olvidar que la comisión es sobre el PVP | Subes precio y sube la comisión |
| No confirmar la orden por WhatsApp en COD | Tasa de entrega 10-20 puntos menor |
| Asumir que el stock del catálogo es real | Se agota; verifica antes de escalar pauta |
| No tener producto B | Un quiebre te deja sin campaña |
| Contar la plata antes de la liquidación | La billetera no es tu cuenta bancaria |
| Creer que Dropi responde por la calidad | El proveedor es un tercero |

## Alternativas

| Plataforma | Nota |
|---|---|
| **Mastershop** | Competidor directo con catálogo y logística propia |
| **Aliddy** | Enfocada en México |
| Mayorista con dropshipping propio | Mejor margen, más gestión. Ver `128`, `129` |

Ver `133` para el panorama completo de plataformas COD de LatAm.

## Para el proyecto activo (México, diciembre 2026)

Dropi MX es la apuesta correcta para arrancar con menos de US$500, **pero en la modalidad de prepago
en tu web**, no COD. Eso te da:

- Cero capital inmovilizado.
- Cero problema de arancel (el stock ya está en México). Ver `16`.
- Caja que vuelve en días, no en semanas.
- Cero devoluciones por "no abrí la puerta".

Checklist de arranque: (1) cuenta Dropi MX verificada con RFC; (2) los 3 componentes del bundle con
**stock alto** y proveedor **B** de respaldo; (3) muestras de los tres a tu casa, US$40-70, ver
`124`; (4) verificar qué permite Dropi de inserto/empaque propio antes de imprimir, ver `125`;
(5) modelar el bundle —costo + flete MXN 120-200 + 5% de 1.099 + CAC— invocando
`Matematicas_lushows`; (6) confirmar el plazo real de liquidación antes de comprometer pauta.

## Relacionados
Ver `128`, `129`, `133`, `134`, `136`, `124`, `125`, `138`, `30`, `16`, `20`, `61`.
