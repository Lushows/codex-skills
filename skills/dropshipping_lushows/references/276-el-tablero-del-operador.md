# El tablero del operador

> El panel de Shopify y el de Meta te mienten por omisión: uno no sabe lo que gastaste, el otro no
> sabe lo que cobraste. El tablero es **una hoja de cálculo tuya** donde los dos números viven
> juntos. Sin eso operas a ciegas aunque tengas 14 gráficas abiertas.

## Los tres niveles

| Nivel | Cuándo | Para qué sirve | Cuántos números |
|---|---|---|---|
| **Diario** | Cada mañana, 5 min | Detectar que algo se rompió | 7 |
| **Semanal** | Lunes, 30 min | Decidir presupuesto, matar o escalar | 12 |
| **Mensual** | Día 1-3, 60 min | Saber si el negocio existe | 10 |

No mezclar niveles. Mirar el margen neto mensual todos los días te vuelve loco; mirar el CPA solo
una vez al mes te quiebra.

## Nivel 1 — Diario (7 números)

| # | Número | Fuente | Regla de alarma |
|---|---|---|---|
| 1 | Gasto de ads | Ads | > plan diario +20% |
| 2 | Pedidos reales | Tienda | < 60% del promedio de 7 días |
| 3 | Ingreso bruto | Tienda | — (se lee con 2) |
| 4 | **CPA real** = gasto ÷ pedidos reales | Tú | > techo de CAC (`11`) 3 días seguidos |
| 5 | **ROAS real** = ingreso ÷ gasto | Tú | < ROAS de equilibrio (`226`) 3 días seguidos |
| 6 | Ticket promedio | Tienda | Caída >10% sin promo activa |
| 7 | Mensajes sin responder | Bandeja | > 0 al cerrar la mañana |

> El CPA "real" usa **pedidos de la tienda**, no compras del píxel. Si difieren más del 15%, tienes
> un problema de medición y todas tus decisiones están sesgadas. Ver `200`, `201`.

Formato de anotación (una fila por día, literal):

```
FECHA | GASTO | PEDIDOS | INGRESO | CPA | ROAS | TICKET | MSJ
14/09 | 1.450 |    9    | 9.891   | 161 | 6,82 |  1.099 |  0
```

Moneda local, siempre la misma. Sin decimales de más.

## Nivel 2 — Semanal (12 números)

Se calcula el lunes sobre lunes-domingo cerrado. Nunca sobre "últimos 7 días" corriendo, porque no
puedes comparar semanas.

| Bloque | Número | Qué decide |
|---|---|---|
| **Dinero** | Ingreso de la semana | — |
| | Gasto de ads | — |
| | Costo de producto vendido | — |
| | Costo de envío | — |
| | **Margen de contribución** (`227`) | Si el producto vive |
| **Adquisición** | CPA de la semana | Escalar o cortar (`269`, `268`) |
| | ROAS de la semana | idem |
| | CPM promedio | Si la subida es de mercado o tuya (`270`) |
| **Página** | Sesiones | Si el problema es tráfico o conversión |
| | Tasa de conversión (`203`) | Diagnóstico de página (`204`) |
| **Operación** | % de pedidos entregados (`159`) | Crítico en COD |
| | Tiempo medio de respuesta | Salud de la atención |

### La tabla semanal de decisión

| Situación | Qué significa | Acción |
|---|---|---|
| CPA bajo techo + margen positivo | Producto vivo | Subir 20-30% (`269`) |
| CPA sube, CPM sube, CTR igual | Es el mercado (Q4) | Aguantar si el margen resiste (`270`) |
| CPA sube, CTR baja | Fatiga creativa | Creativos nuevos (`264`) |
| CPA igual, conversión baja | Página o precio | Revisar `204`, `216` |
| Pedidos ok, entregas bajan | Logística | `159`, `163` |
| Margen negativo 2 semanas seguidas | Producto muerto | Cerrarlo (`296`) |

## Nivel 3 — Mensual (10 números)

| Número | Cómo | Para qué |
|---|---|---|
| Ingreso neto (después de devoluciones y no entregados) | Tienda − ajustes | La verdad |
| Costo de mercancía total | Facturas | — |
| Gasto de publicidad total | Ads | — |
| Costos fijos (apps, dominio, pasarela, 3PL, gente) | Bancos | `229` |
| **Utilidad neta** | Resta | Si el negocio existe |
| **Margen neto %** | Utilidad ÷ ingreso | Salud estructural |
| Clientes nuevos | Tienda | — |
| % recompra | Tienda | `230`, `285` |
| **LTV a 90 días** | Ingreso por cliente acumulado | Cuánto puedes pagar por cliente |
| Caja disponible y días de cobertura | Banco | La métrica que decide si sobrevives (`234`) |

> **Margen neto de referencia** en dropshipping con stock local y prepago: sano 15-25%, apretado
> 8-15%, insostenible <8%. Verificar contra tus propios costos, no contra estos rangos.

## La trampa de los números de Meta

| Lo que dice Meta | Lo que realmente pasa | Qué hacer |
|---|---|---|
| "Compras: 14" | Vendiste 9 | Usa la tienda como fuente de verdad |
| "ROAS 4,2" | Con ventana de atribución de 7 días clic + 1 vista | Compara solo contra ti mismo |
| "Valor de conversión $X" | No descuenta devoluciones ni no entregados | Ajusta en el mensual |
| "CPA por conjunto" | Reparte crédito entre conjuntos | Decide a nivel campaña cuando el volumen es bajo |

El número que manda: **gasto total del día ÷ pedidos reales del día**. Ese no miente.

## El tablero mínimo en una hoja

Tres pestañas, nada más:

| Pestaña | Filas | Columnas |
|---|---|---|
| `DIARIO` | 1 por día | las 7 de arriba |
| `SEMANAL` | 1 por semana | las 12 de arriba |
| `MENSUAL` | 1 por mes | las 10 de arriba |

Si quieres el modelo de economía unitaria que alimenta los techos (CAC máximo, ROAS de equilibrio),
está en `228` y `233`. Para que los cálculos salgan exactos y auditados, **invoca
`Matematicas_lushows`**.

## Errores de tablero

| Error | Consecuencia |
|---|---|
| Medir solo ROAS | Ignoras el margen; puedes tener ROAS 3 y perder plata |
| No registrar costos de envío por pedido | Descubres el hueco en el cierre mensual |
| Usar el ingreso bruto como "lo que gané" | Confundes caja con utilidad y reinviertes lo que no tienes |
| Cambiar de fuente entre semanas | Series incomparables |
| No anotar los días de promoción | Luego no entiendes los picos |

## Checklist del lunes

- [ ] Las 7 filas diarias de la semana están completas
- [ ] Margen de contribución de la semana calculado
- [ ] CPA y ROAS comparados con las 2 semanas anteriores
- [ ] Decisión de presupuesto escrita para la semana
- [ ] Un creativo ganador identificado para iterar (`263`)
- [ ] Un creativo muerto apagado

## Relacionados
`275` la operación diaria · `266` métricas que importan · `223` economía unitaria · `226` ROAS de
equilibrio · `228` modelo financiero · `234` flujo de caja · `239` el tablero de números ·
`296` cerrar un producto · `298` el plan de 90 días
