# 142 — Gestión de inventario

Tu inventario es **plata congelada**: cada producto en estantería es dinero que ya pagaste y todavía no recuperaste. Bien manejado, libera caja y elimina ventas perdidas; mal manejado, te quiebra aunque vendas. Este módulo te da los pocos números que sí importan.

---

## La idea madre: inventario = caja parada

Cada unidad guardada tiene tres costos ocultos:

1. **Capital inmovilizado** — esa plata podría estar en otra compra, en marketing o en el banco.
2. **Costo de mantener** — bodega, refrigeración, seguro, vencimiento, robo, obsolescencia.
3. **Costo de oportunidad** — lo que dejaste de ganar por no tener la plata libre.

Regla mental: **no quieres ni mucho ni poco**. Mucho = caja muerta y mermas. Poco = quiebres de stock (vendes el cero, el cliente se va a otro lado). El arte es encontrar el punto medio por producto.

> Conecta con flujo de caja (ver 55): el inventario es donde más se esconde la plata de un negocio físico. Y con costos (ver 58): el costo de mantener inventario es un costo real aunque no aparezca en la factura.

---

## Los 5 KPIs que sí debes mirar

| KPI | Qué mide | Fórmula | Señal |
|---|---|---|---|
| **Rotación** | Cuántas veces vendes y repones el inventario en un período | Costo de mercancía vendida (COGS) ÷ Inventario promedio | Más alto = mejor (capital trabaja más) |
| **Días de inventario** | Cuántos días tardas en vender todo lo que tienes | 365 ÷ Rotación anual | Más bajo = mejor |
| **Tasa de quiebres** | % de veces que un cliente pidió y no había | Pedidos no surtidos ÷ Pedidos totales | Bajo, pero >0 es normal |
| **% inventario muerto** | Mercancía sin moverse hace >X meses | Valor inventario sin venta ÷ Inventario total | <5-10% sano |
| **Merma** | Pérdida por vencimiento, daño, robo | Valor perdido ÷ Valor comprado | Depende del rubro |

Rangos orientativos: un supermercado rota muy rápido (días de inventario bajos, una o dos semanas); una joyería rota lento (meses). **No hay número universal** — compáralo contra TU historia y contra tu rubro (cómo conseguir benchmarks reales, ver 21).

---

## Ejemplo numérico de rotación (cifras ilustrativas)

Tienda de hongos funcionales. En el año:

- **COGS** (lo que te costó la mercancía que vendiste): $48.000.000
- **Inventario promedio** (valor de lo que tenías guardado, a costo): $8.000.000

**Rotación = 48.000.000 ÷ 8.000.000 = 6 veces al año.**

**Días de inventario = 365 ÷ 6 ≈ 61 días.** Tardas ~2 meses en vender todo tu stock.

¿Es bueno? Si tu proveedor te entrega en 15 días, 61 días de inventario es exceso: tienes plata parada. Si subes la rotación a 9 veces (≈40 días), liberas inventario:

- Nuevo inventario promedio para sostener el mismo COGS = 48.000.000 ÷ 9 ≈ $5.333.000
- **Caja liberada ≈ 8.000.000 − 5.333.000 = $2.667.000** que ahora puedes usar en otra cosa.

Esa es la magia: **mejorar rotación es como conseguir un préstamo gratis** de tu propia operación.

> Inventario promedio rápido = (Inventario inicial + Inventario final) ÷ 2. Para más precisión, promedia los cierres mensuales.

---

## Costo de mantener inventario (el que nadie suma)

Como % anual del valor del inventario, suele rondar un **rango orientativo del 15% al 30%** entre todos los componentes (bodega + capital + seguro + mermas + obsolescencia). Verifica con TUS cifras reales.

Ejemplo ilustrativo: si mantienes $8.000.000 de inventario y tu costo de mantener es 20% anual, te cuesta **$1.600.000 al año** solo tenerlo ahí. Ese número justifica pelear por menos stock parado.

---

## EOQ básico — ¿cuánto pido cada vez?

EOQ (Cantidad Económica de Pedido) responde: ¿pido mucho de vez en cuando (ahorro en envíos pero acumulo) o poco seguido (menos stock pero más costos de pedir)? Equilibra dos costos:

- **Costo de pedir** (S): cada orden cuesta — transporte, tiempo, mínimos del proveedor.
- **Costo de mantener por unidad/año** (H).

Fórmula: **EOQ = √(2 × D × S ÷ H)** donde D = demanda anual en unidades.

Ejemplo ilustrativo: vendes D = 1.200 frascos/año; pedir cuesta S = $50.000 por orden; mantener un frasco cuesta H = $2.000/año.

EOQ = √(2 × 1.200 × 50.000 ÷ 2.000) = √(60.000.000) ≈ **245 frascos por pedido**, ≈ cada 2,5 meses.

No te cases con el número exacto: EOQ es una **guía de orden de magnitud**, no una ley. Ajústalo por descuentos por volumen, perecibilidad y caja disponible.

---

## Análisis ABC — no todo merece la misma atención

Regla 80/20 aplicada al inventario: pocos productos generan la mayoría de tus ventas.

| Clase | % de productos (aprox.) | % de ventas (aprox.) | Cómo gestionarlos |
|---|---|---|---|
| **A** | ~20% | ~80% | Control estricto, conteo frecuente, nunca quiebre |
| **B** | ~30% | ~15% | Control medio, revisión periódica |
| **C** | ~50% | ~5% | Control liviano, pide en lote, no obsesionarse |

Acción: pon tus mejores procesos y tu mejor seguimiento en los productos **A**. Para los **C**, automatiza y olvídalos.

---

## FIFO — primero en entrar, primero en salir

Vende primero lo que llegó primero. Crítico en perecederos (alimentos, suplementos, cosméticos): evita vencimientos y mermas. Implementación física simple: stock nuevo **atrás**, viejo **adelante**. Marca fechas. En contabilidad, FIFO también afecta cómo valoras el costo (qué método usar para impuestos depende del país — **verifica las reglas vigentes de tu país/ciudad**, ver 63 para lo fiscal).

---

## Punto de reorden y stock de seguridad

- **Punto de reorden** = (demanda diaria × días que tarda el proveedor) + stock de seguridad. Cuando bajas a ese nivel, pides.
- **Stock de seguridad** = colchón para no quebrar si la demanda sube o el proveedor se atrasa.

Ejemplo ilustrativo: vendes 8 frascos/día, el proveedor tarda 10 días, y guardas 20 frascos de colchón. Reorden = (8 × 10) + 20 = **100 frascos**. Al llegar a 100, haces el pedido.

---

## Cómo arrancar mínimo viable (sin software caro)

1. Una hoja de cálculo con: producto, costo, stock actual, ventas del mes, fecha de vencimiento.
2. Calcula rotación y días de inventario una vez al mes.
3. Marca tus productos A, B, C.
4. Define punto de reorden para los A.
5. Cada mes, lista lo que no se movió (inventario muerto) y decide: promoción, combo o liquidación.

Cuando el volumen crezca, pasa a un sistema de inventario/POS (ver 87 para elegir herramientas).

---

## Errores comunes

- **Comprar por descuento, no por demanda.** "Me dieron 30% si llevo 500" = 500 unidades que tardas un año en vender. Calcula el costo de mantener antes.
- **No mirar vencimientos** hasta que ya vencieron. Programa alertas.
- **Tratar todos los productos igual.** Sin ABC desperdicias atención en los C.
- **Confundir tener inventario con tener plata.** Un balance "sano" lleno de mercancía muerta es una trampa de caja (ver 55).
- **Olvidar el costo de mantener** en el precio. Si no lo cubres, vendes a pérdida sin saberlo (ver 58 y 144).
- **Quiebres invisibles.** Si no registras los pedidos que no pudiste surtir, nunca sabes cuánta venta perdiste.

---

## Siguiente paso típico

Calcula HOY tu rotación y días de inventario con las cifras del último año; clasifica tus productos en A/B/C y define punto de reorden solo para los A. Si los días de inventario superan con holgura el tiempo de reposición de tu proveedor, tienes caja atrapada — empieza por liquidar el inventario muerto (ver 55 y 143).
