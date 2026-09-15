# 88 — Métricas y tablero

Sirve para que sepas, en una sola mirada, si tu negocio va bien o mal — y qué hacer hoy. Un tablero
no es para presumir gráficos: es para tomar decisiones rápido con pocos números que sí importan.

## La regla de oro: pocas métricas, bien elegidas

Si mides todo, no decides nada. La trampa más común es ahogarse en datos bonitos pero inútiles.
Por eso separamos dos tipos de métricas:

- **Métrica de vanidad**: sube siempre y te hace sentir bien, pero no cambia tu decisión.
  Ejemplos: seguidores, "me gusta", visitas totales, número de descargas acumuladas.
- **Métrica accionable**: si se mueve, tú cambias algo concreto. Ejemplos: tasa de conversión,
  costo de adquirir un cliente (CAC, ver 52), ingreso recurrente, recompra.

> Test rápido: "Si esta métrica sube/baja 20%, ¿haría algo distinto mañana?" Si la respuesta es NO,
> probablemente es vanidad. Mídela si quieres, pero no la pongas en el tablero principal.

## La métrica norte (North Star)

Es **el número que mejor representa el valor que entregas a tus clientes**. Una sola, para todo el
equipo. Todo lo demás la alimenta.

| Tipo de negocio | Métrica norte (ejemplo orientativo) |
|---|---|
| E-commerce / tienda | Pedidos pagados por semana |
| Suscripción / SaaS | Ingreso recurrente mensual (MRR) |
| Marketplace | Transacciones completadas por mes |
| App de contenido | Usuarios activos que vuelven cada semana |
| Servicio / agencia | Proyectos entregados y cobrados por mes |

Cómo elegir la tuya: pregúntate "¿qué número, si sube de forma sana, significa que mi negocio crece
de verdad?" Evita que sea solo ingreso bruto si eso te empuja a vender a pérdida (ver 53, punto de
equilibrio, y 52, CAC/LTV). La métrica norte debe reflejar valor real, no solo dinero entrando hoy.

## KPIs por etapa (el embudo)

Un negocio convierte desconocidos en clientes que recompran. Mide UNA cosa clave en cada paso:

| Etapa | Pregunta que responde | KPI típico |
|---|---|---|
| Atracción | ¿Cuánta gente nueva llega? | Visitas/leads nuevos por semana |
| Conversión | ¿Cuántos compran? | % de visitas que compran (tasa de conversión) |
| Ingreso | ¿Cuánto deja cada venta? | Ticket promedio y margen por venta |
| Retención | ¿Vuelven? | % de clientes que recompran / cancelan |
| Referencia | ¿Te recomiendan? | % que llega por recomendación |

"KPI" (Key Performance Indicator) = indicador clave de desempeño: el número que vigilas en esa etapa.
La gracia es ver dónde se rompe el embudo. Si llega mucha gente pero casi nadie compra, el problema
NO es atraer más, es convertir mejor — y gastar en más tráfico sería tirar plata.

## Ejemplo numérico de embudo (cifras ilustrativas, inventadas)

Tienda online en un mes. **Estos números son solo un ejemplo para que veas el razonamiento:**

| Etapa | Número | Conversión a la siguiente |
|---|---|---|
| Visitas al sitio | 4.000 | — |
| Agregan al carrito | 400 | 10% |
| Compran | 80 | 20% del carrito |
| Recompran (mes siguiente) | 16 | 20% de los que compraron |

- Tasa de conversión total: 80 / 4.000 = **2%**.
- Si subieras el carrito→compra de 20% a 30% (mejorando checkout/pago), pasarías de 80 a 120 ventas
  **sin gastar un peso más en tráfico**. Ese es el poder de mirar el embudo.

Lección: la métrica que más palanca te da no siempre es la de arriba. Busca el **cuello de botella**.

## Tablero simple (qué poner y cómo)

Un buen tablero cabe en una pantalla y se lee en 30 segundos. Para empezar basta una hoja de cálculo
(Google Sheets) con una fila por semana o mes.

Estructura recomendada (5 a 8 números máximo):

1. **Métrica norte** (la principal, arriba y grande).
2. **2-3 KPIs del embudo** donde hoy duele más (ej. conversión, recompra).
3. **1-2 de salud financiera**: margen y caja disponible / runway (ver 58 sobre costos y presupuesto).
4. **CAC y, si aplica, LTV** (ver 52) — cuánto cuesta y cuánto vale un cliente.

Para cada número guarda: **valor actual, valor anterior, meta, y flecha** (↑ bueno / ↓ malo).
Sin meta, un número no dice nada: $5M de ventas puede ser excelente o un desastre según el objetivo.

## Ejemplo de tablero básico (cifras ilustrativas, inventadas)

Negocio de suscripción, vista mensual. **Ejemplo, no datos reales:**

| Métrica | Mes pasado | Este mes | Meta | Estado |
|---|---|---|---|---|
| MRR (métrica norte) | $8.0M | $9.2M | $10M | ↑ cerca |
| Clientes nuevos | 40 | 52 | 50 | ↑ ok |
| Cancelación mensual (churn) | 6% | 8% | <5% | ↓ alerta |
| Conversión prueba→pago | 18% | 17% | 25% | → flojo |
| CAC | $180k | $210k | <$200k | ↓ alerta |
| Caja / meses de runway | 7 | 6 | >6 | → vigilar |

Lectura en 30 segundos: el ingreso sube, pero el **churn empeoró y el CAC se pasó de meta**. La acción
no es "vender más", es "averiguar por qué se van los clientes" antes de seguir gastando en adquirir.
Un tablero bueno te dice qué pregunta hacer, no solo qué pasó.

## Cada cuánto mirarlo

- **Diario** (1 min): solo señales de vida — ventas/pedidos del día, caja. Para detectar caídas bruscas.
- **Semanal** (15 min): el embudo y la métrica norte. Aquí decides ajustes tácticos.
- **Mensual** (1 h): salud financiera completa, CAC/LTV, tendencias, metas (ver 90).

No revises todo todos los días: genera ansiedad y ruido. El ruido diario engaña; la tendencia manda.

## Errores comunes

- **Coleccionar métricas de vanidad** y sentir que vas bien mientras la caja baja.
- **Sin meta ni comparación**: un número solo no es bueno ni malo. Siempre pon meta y dato anterior.
- **Promedios que esconden la verdad**: el ticket "promedio" puede ocultar que 3 clientes grandes
  sostienen todo. Mira también la mediana o segmenta.
- **Tablero demasiado grande**: 30 indicadores = ninguno se mira. Menos es más.
- **Medir y no actuar**: una métrica que nunca cambia una decisión es trabajo perdido.
- **Reaccionar al ruido diario**: cambiar de estrategia por un mal día. Mira la tendencia de semanas.
- **Olvidar el margen**: vender más con margen negativo es quebrar más rápido (ver 58).

## Cómo conseguir los datos reales

Tamaños de mercado o benchmarks de tu sector/país son orientativos — consíguelos con el método del
módulo 21, no los inventes. Pero tus propios números (ventas, conversión, churn) salen de tu pasarela
de pago, tu CRM o tu hoja de cálculo: empieza a registrarlos HOY aunque sea a mano. Un mes de datos
propios vale más que cualquier benchmark externo.

## Siguiente paso típico

Define tu métrica norte en una frase, elige los 5-6 KPIs que sí cambian decisiones y arma una hoja
de cálculo con valor actual, meta y dato anterior. Conéctala con tu punto de equilibrio (ver 53), tu
CAC/LTV (ver 52) y tu caja/presupuesto (ver 58), y agéndate 15 minutos cada lunes para revisarla.
