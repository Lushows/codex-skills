# El agente de sourcing

> Vigencia: septiembre 2026. Los rangos de fee son de mercado; verifica en negociación real.

El agente de sourcing es **la figura que separa el dropshipping de juguete del negocio real**. Es una
persona o empresa en China que compra por ti, inspecciona, consolida, empaca y despacha. Es tu
departamento de compras y calidad, tercerizado, por 5-10%.

Sin agente estás comprando al por menor y llamándolo mayoreo.

## Qué hace un agente (la lista completa)

| Función | Detalle |
|---|---|
| **Encontrar la fuente** | Le mandas link de AliExpress, te devuelve el de 1688/fábrica con precio |
| **Negociar precio** | En chino, con contexto cultural, sabiendo cuánto margen hay. Ver `118` |
| **Comprar** | Paga en Alipay/RMB. Resuelve el problema de acceso a 1688. Ver `112` |
| **Recibir e inspeccionar** | Abre las cajas, cuenta, fotografía, prueba función. Ver `123` |
| **Rechazar y reponer** | Devuelve al proveedor lo defectuoso **antes** de que salga de China |
| **Almacenar** | Guarda tu stock días o semanas sin cobrar (o barato) |
| **Consolidar** | Junta compras de 4 proveedores en un solo envío. Ahorra 40-60% de flete |
| **Empacar** | Pone tu inserto, bolsa con logo, etiqueta. Ver `125` |
| **Despachar** | Elige línea (aéreo/marítimo/express) y gestiona la guía |
| **Gestionar reclamos** | Persigue al proveedor cuando algo sale mal |
| **Fulfillment unitario** | Muchos agentes despachan pedido por pedido con tu marca |

Lo que **no** hace: no es tu 3PL de destino, no despacha aduana en tu país, no responde por
tu decisión de producto.

## Cuánto cobra

| Modelo | Rango típico | Cuándo se usa |
|---|---|---|
| **% sobre el valor de la mercancía** | 3-10% (típico 5%) | El más común |
| Fee fijo por pedido | US$0,50-2,00 por unidad despachada | Fulfillment unitario |
| Fee fijo mensual + costo | US$200-800/mes | Volumen alto y estable |
| "Sin fee, gano del proveedor" | 0% aparente | **Bandera roja.** Ver abajo |

**El agente que dice "no te cobro nada" está cobrando comisión del proveedor.** Eso significa que su
incentivo es que compres caro, no barato. Es el conflicto de interés más común del sector. Prefiere
pagar 5% transparente.

## La cuenta que justifica al agente

Producto de US$7,80 en AliExpress, US$2,45 en 1688.

| Concepto | Sin agente | Con agente (5%) |
|---|---|---|
| Producto (300 uds) | 2.340 | 735 |
| Fee del agente | — | 37 |
| Flete individual / consolidado | incluido | 285 |
| Inspección | 0 | incluida |
| **Total** | **2.340** | **1.057** |
| Costo por unidad | 7,80 | **3,52** |

Ahorro: **US$1.283 en un pedido de 300 unidades.** El fee de US$37 es ruido.

El agente empieza a tener sentido a partir de aproximadamente **US$1.000-1.500 de compra mensual**.
Por debajo de eso, el tiempo de coordinar no se paga y las plataformas son más prácticas. Ver `115`.

## Tipos de agente

| Tipo | Perfil | Pros | Contras |
|---|---|---|---|
| **Individual / freelance** | Persona en Yiwu o Shenzhen, WeChat | Barato, flexible, atención directa | Se satura, vacaciones, riesgo de una sola persona |
| **Agencia pequeña** (5-20 personas) | Oficina + bodega propia | Balance. **El punto dulce** | Precio algo mayor |
| **Agencia grande / "dropshipping agent"** | Estructura tipo CJ con marca | Procesos, dashboard, API | Menos negociación, te tratan como número |
| **Oficina de compras occidental en China** | Gestión en tu idioma, QC formal | Mejor para producto regulado | Fee 8-15% |

Para dropshipping de 100-1.000 unidades/mes, la **agencia pequeña** es casi siempre la mejor
relación precio/servicio.

## Cómo se trabaja con un agente, en la práctica

```
Canal: WeChat (no email). Hora china: UTC+8 → adelantado 13-14 h respecto a México.
Ritmo: le escribes en la noche de México, respondes en la mañana.

Ciclo por pedido:
 1. Mandas lista: link + variante + cantidad
 2. Agente devuelve "quotation sheet" (Excel) en 24-48 h
 3. Apruebas por escrito, con captura de la fila aprobada
 4. Pagas (Wise/transferencia). Ver 140
 5. Agente compra. 3-7 días para recibir en su bodega
 6. Fotos/video de inspección. Tú apruebas o rechazas. Ver 123
 7. Cotiza flete: aéreo vs marítimo, con peso real y volumétrico
 8. Despacha. Te da número de guía o BL
```

**Todo por escrito, todo en el mismo hilo.** Cuando algo falla, el hilo de WeChat es tu único
contrato real. Ver `144`.

## Lo que debes exigir desde el día uno

1. **Quotation sheet en Excel** con columnas: link, foto, variante, precio unitario CNY, precio USD,
   MOQ, peso unitario, medidas de caja, unidades por caja.
2. **Fotos de inspección** de cada SKU, no solo del bulto.
3. **Peso real y volumétrico** antes de cotizar flete. Ver `121`.
4. **Desglose del fee**: qué incluye y qué no.
5. **Política de defectuosos**: quién asume y en cuánto tiempo.
6. **Tu stock identificado** en su bodega (etiqueta con tu nombre), no revuelto.

## Banderas rojas (resumen; detalle en `117`)

| Señal | Qué significa |
|---|---|
| "No cobro comisión" | Cobra del proveedor. Conflicto de interés |
| No manda fotos de inspección | No inspecciona |
| Precio que no coincide con el de 1688 que tú ves | Se está quedando con la diferencia además del fee |
| Insiste en pagos a cuenta personal de un tercero | Ver `140`, `141` |
| Solo habla de "productos ganadores" y te vende catálogo | Es revendedor, no agente |
| No tiene bodega física verificable (video en vivo) | Es un intermediario de otro agente |

## Errores frecuentes

| Error | Realidad |
|---|---|
| Buscar agente antes de tener producto validado | El agente optimiza costo, no encuentra el negocio |
| Trabajar con uno solo desde el inicio | Ten 2. El segundo te da precio de referencia. Ver `117` |
| Pagar todo por adelantado sin inspección | Es exactamente lo que el agente debe evitarte |
| Asumir que habla inglés perfecto | Escribe frases cortas, sin modismos, y confirma con números |
| Pedirle que "elija el mejor proveedor" sin criterio | Elegirá el que le da más comisión o el más fácil |

## Para el proyecto activo (México, diciembre 2026)

**No necesitas agente en diciembre.** Con capital menor a US$500 y cero ventas validadas, el agente
es una solución a un problema que aún no tienes. Valida con Dropi MX o mayorista mexicano.

Empieza a buscar agente cuando: (a) tengas 100+ ventas del mismo bundle, (b) el costo de mercadería
sea tu mayor línea de gasto, (c) tengas US$1.500+ para un lote. Realista: febrero-marzo de 2027,
después del Año Nuevo Chino. Ver `139`, `136`.

## Relacionados
Ver `110`, `112`, `117`, `118`, `119`, `120`, `123`, `125`, `136`, `140`, `141`, `144`.
