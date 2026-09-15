# 165 — Cadena de suministro avanzada

Cómo asegurar que lo que vendes llegue a tiempo, al menor costo posible y sin que un solo proveedor te deje en cero. Esto deja de importar cuando vendes 5 unidades al mes; empieza a definir tu rentabilidad cuando vendes en serio.

## Para qué sirve
Tu cadena de suministro es todo el camino: materia prima → proveedor → tu bodega → cliente. Optimizarla significa pelear tres frentes al mismo tiempo: **costo** (que no se coma tu margen, ver 142), **velocidad** (lead time corto) y **riesgo** (que no se rompa). Casi nunca puedes maximizar los tres; este módulo te da el método para elegir bien.

## Conceptos clave (sin tecnicismos)
- **Lead time**: tiempo desde que pides hasta que recibes. Si pides a China y tarda 60 días, tu lead time es 60 días (no los 3 días que tarda el barco en cargar).
- **Stock de seguridad**: inventario extra que guardas "por si acaso" se atrasa el proveedor o sube la demanda.
- **Just-in-time (JIT)**: pedir lo justo para llegar justo a tiempo, casi sin inventario. Barato en almacenamiento, frágil ante imprevistos.
- **Punto de reorden**: el nivel de inventario en el que debes volver a pedir para no quedarte sin stock antes de que llegue lo nuevo.
- **MOQ** (cantidad mínima de pedido): lo mínimo que un proveedor te vende por orden.

## Marco 1 — Múltiples proveedores (no dependas de uno solo)
La regla de oro: **ningún proveedor crítico debería superar ~60-70% de tu volumen** de ese insumo. Estrategias:

| Estrategia | Qué es | Cuándo usarla |
|---|---|---|
| Single-source | 1 proveedor | Solo si es insustituible y confiable. Riesgo alto. |
| Dual-source | 1 principal (70%) + 1 respaldo (30%) | Recomendado por defecto. |
| Multi-source | 3+ proveedores rotando | Volumen alto, insumo commodity. |
| Proveedor local + importado | Local caro/rápido + importado barato/lento | Cubre ambos escenarios. |

Tener un segundo proveedor activo (aunque le compres poco) mantiene la relación viva y te da poder de negociación (ver 85). Un respaldo "en teoría" que nunca te ha despachado, NO es un respaldo.

## Marco 2 — JIT vs Stock de seguridad
No es uno u otro; es **cuánto colchón** según el riesgo:

- **Más stock de seguridad cuando**: lead time largo o variable, proveedor poco confiable, demanda impredecible, costo de quedarte sin producto es alto (pierdes la venta y al cliente).
- **Más JIT (menos stock) cuando**: producto perecedero o que se vuelve obsoleto, dinero escaso (el inventario es plata congelada, ver 143), lead time corto y confiable.

Fórmula práctica del **punto de reorden**:
> Punto de reorden = (demanda diaria × lead time en días) + stock de seguridad

## Ejemplo numérico (cifras ilustrativas)
Vendes un suplemento. Datos de ejemplo:
- Demanda: 20 frascos/día.
- Lead time del proveedor: 30 días.
- Stock de seguridad que decides mantener: 200 frascos (10 días de colchón).

**Punto de reorden** = (20 × 30) + 200 = **800 frascos**. Cuando tu inventario baje a 800, pides de nuevo.

Ahora el costo de ese colchón:
- 200 frascos × costo unitario de 15 (ejemplo) = **3.000 inmovilizados** todo el tiempo.
- Si ese dinero te cuesta ~3%/mes (financiamiento o costo de oportunidad, ver 143) = **90/mes** solo por tener el colchón.

Compáralo con el costo de un quiebre de stock:
- Si te quedas sin producto 5 días: 20 frascos/día × 5 × margen de 25 (ejemplo) = **2.500 de venta perdida**, más clientes que se van a la competencia.

Conclusión del ejemplo: pagar 90/mes de colchón para evitar perder 2.500 por quiebre **vale la pena**. Pero si tu margen fuera mínimo y el producto se venciera, la cuenta cambiaría. Corre TU cuenta con tus números.

## Marco 3 — Costos logísticos ocultos
El precio del proveedor NO es tu costo real. Costo verdadero por unidad =

> Precio + flete + aranceles/impuestos de importación + seguro + costo de almacenamiento + merma/daños + costo del dinero inmovilizado

**Aranceles, IVA de importación y trámites aduaneros dependen 100% del país y del tipo de producto.** No asumas porcentajes: pregunta país/ciudad y verifica el arancel vigente con la autoridad aduanera local o un agente de aduanas antes de calcular (ver 21 para conseguir el dato real).

Checklist de costos a sumar siempre:
- [ ] Flete internacional y nacional (última milla incluida).
- [ ] Aranceles + IVA/impuesto de importación (verificar por país).
- [ ] Seguro de mercancía.
- [ ] Bodegaje (alquiler, o costo de tu propio espacio).
- [ ] Merma: % que se daña, vence o se pierde.
- [ ] Costo financiero del inventario parado.

## KPIs de cadena de suministro
1. **Lead time promedio y su variabilidad** (no solo el promedio: un proveedor que tarda "30 días ±2" es mejor que uno de "20 días ±15").
2. **Fill rate / nivel de servicio**: % de pedidos que cumples completos y a tiempo.
3. **Rotación de inventario**: cuántas veces vendes y repones tu stock al año (más alto = menos plata congelada, ver 143).
4. **Tasa de quiebre de stock (stockouts)**: % de veces que te quedaste sin producto.
5. **Costo logístico como % de ventas**: para ver si la logística se está comiendo el margen (ver 142).

## Cómo arrancar (mínimo viable)
1. Lista tus 3-5 insumos críticos (los que, si faltan, paras de vender).
2. Para cada uno: ¿cuántos proveedores tengo realmente activos? Si es 1, busca un segundo HOY.
3. Mide tu lead time real de los últimos pedidos (no el prometido).
4. Calcula tu punto de reorden con la fórmula de arriba.
5. Pon una alerta simple (hoja de cálculo) cuando el inventario baje al punto de reorden.

No necesitas un software caro al inicio. Una hoja de Excel/Sheets con columnas: insumo, proveedor, lead time, stock actual, punto de reorden, ya te resuelve el 80%.

## Trampas que matan la cadena de suministro
- **Depender de un solo proveedor** porque "siempre ha cumplido". El día que falle, paras tú.
- **Confundir precio barato con costo bajo**: un proveedor 10% más barato pero con lead time del doble y más merma puede salir más caro.
- **Stock de seguridad a ojo**: ni mucho (plata congelada) ni poco (quiebres). Calcúlalo.
- **Ignorar la variabilidad**: optimizar para el escenario promedio y reventar el día atípico.
- **No tener el dato aduanero real** antes de importar y descubrir el arancel ya con la mercancía en el puerto.
- **Comprar por MOQ** más de lo que rotas, solo por el descuento por volumen (ver 142).

## Errores comunes
- Negociar solo precio y no plazos de pago ni lead time (ver 85).
- No documentar quién es el plan B; el respaldo vive en tu cabeza, no en un contrato.
- Medir el promedio de lead time pero nunca su desviación.
- Crecer en ventas sin escalar la cadena: vendes el doble pero tu proveedor no puede entregar el doble.

## Siguiente paso típico
Haz hoy la lista de tus insumos críticos y marca cuáles tienen un solo proveedor: ese es tu riesgo número uno. Consigue un segundo proveedor activo para el más crítico y calcula su punto de reorden con tus números reales (ver 85 para negociar, 143 para el costo del inventario, 142 para el impacto en margen).
