# 16 — Atribución 2026

Atribución = a quién le damos el crédito de una venta. Suena contable, pero define TODAS tus decisiones: si crees el número equivocado, escalas lo que no funciona. Lee este módulo cuando los números de Ads Manager no cuadren con tus ventas reales (spoiler: nunca cuadran exacto) o antes de decidir apagar/escalar algo grande.

## Cómo atribuye Meta por defecto

Ventana default: **7d-click / 1d-view**. Significa: Meta se anota la conversión si la persona **clickeó** tu anuncio en los últimos 7 días, **o** simplemente lo **VIO** (sin clic) en las últimas 24 horas.

- **View-through** (la parte "1d-view") es la polémica: alguien scrolleó, tu anuncio pasó por su pantalla, y compró ese día por cualquier otra razón (te buscó en Google, le llegó tu correo, ya venía decidido) → Meta se anota la venta. En cuentas con retargeting pesado o marca conocida, el view-through puede inflar resultados 15-40% (rango orientativo; varía muchísimo por cuenta).
- Además existen las **modeled conversions**: desde iOS 14.5 (2021), Meta no ve todo (usuarios de iPhone que rechazaron tracking) y **estima estadísticamente** conversiones que cree que ocurrieron. Parte de tu columna de resultados es modelo, no observación. Mitigación: CAPI con buen EMQ (calidad de matcheo de datos, ver 22-23) le da más señal real, y por tanto menos modelado y más verdad.

> ⏱️ **Cambio 2026 (ver `actualizacion-2026-06`):** el **12-ene-2026 Meta quitó las ventanas view-through (7d y 28d) del Ads Insights API**; el view-through largo ya casi no existe en el reporte de API, solo quedan ventanas por **CLIC** (la UI conserva el 1d-view default). También **recortó la retención** de datos (insights a nivel único ~13 meses; algunos breakdowns de frecuencia ~6 meses) — exporta tu histórico tú mismo si quieres comparar año contra año. Efecto: tus números de retargeting/WhatsApp que vivían del view-through bajaron; no empeoró la campaña, dejó de contarse humo. Estándar de hoy: **7d-click / 1d-view**.

## Atribución incremental (el estándar nuevo, 2026)

Meta consolidó **Atribución incremental** en Ads Manager: en vez de last-touch, usa ML contrafactual (entrenado con Conversion Lift) para contar solo las conversiones que el anuncio **causó de verdad**, no las que igual iban a pasar. **Reporta MENOS conversiones que el default — y eso es lo bueno**: es la verdad sin el view-through inflado. En 2026 además **alimenta las pujas de valor** (Minimum ROAS / Value Rules, ver 15): el algoritmo puede optimizar hacia conversiones incrementales, no solo atribuidas.

- **Úsala si** tienes volumen (≥100 conversiones/semana): los números serán más bajos pero más honestos.
- **No la uses para reportar** junto a otra cuenta sin avisar: como cuenta menos, parecerá que "rinde peor" cuando en realidad es más real. Documenta qué ventana usas en cada reporte (ver 60).
- En cuentas chicas no tendrá señal suficiente; quédate en 7d-click/1d-view y triangula con backend.

Es el puente entre la atribución de plataforma y la incrementalidad real medida con experimentos (ver 65).

## Ver cuánto es real: comparar ventanas

En Ads Manager: Columnas → **Comparar configuraciones de atribución**. Activa 1d-click, 7d-click y 7d-click/1d-view en paralelo. Lectura:

| Lo que ves | Interpretación |
|---|---|
| 1d-click ≈ 7d-click/1d-view | Tus conversiones son inmediatas y de clic: número bastante confiable |
| 7d-click ≫ 1d-click | Tu cliente piensa varios días antes de comprar (normal en ticket alto) |
| 7d-click/1d-view ≫ 7d-click | Mucho view-through: desconfía, sobre todo en retargeting (ver 24) |

Regla práctica: el **1d-click es tu piso conservador**, el default es tu techo optimista, la **atribución incremental es tu mejor estimado de verdad**. La realidad de caja vive entre el piso y el backend.

## Plataforma > realidad: cómo triangular

Meta reporta con SU ventana y SU modelo; Google reporta lo suyo (ver google_ads_lushows); TikTok lo suyo (ver tiktok_ads_lushows); suma todos los "atribuidos" y te dan más ventas de las que existieron. Por eso:

1. **Backend primero**: tus pedidos reales (Shopify, tu sistema, el cuaderno, `data/orders.json` del bot) son la única verdad absoluta.
2. **MER** (Marketing Efficiency Ratio = ingresos totales ÷ gasto publicitario total): la métrica de sanidad global. Si Ads Manager dice ROAS 4 pero tu MER es 1.3, alguien miente (detalle en 64).
3. **Test de coherencia mensual**: ventas que Meta se atribuye vs ventas totales del negocio. Si Meta "se atribuye" el 130% de tus ventas, ya sabes cuánto descontar mentalmente.

### Mini-ejemplo de triangulación (COP)

| Fuente | Ventas atribuidas mes | Lectura |
|---|---|---|
| Ads Manager (7d-click/1d-view) | $40.000.000 | techo optimista |
| Ads Manager (1d-click) | $26.000.000 | piso conservador |
| Atribución incremental | $30.000.000 | mejor estimado |
| Backend (pedidos reales totales) | $48.000.000 | verdad de caja |
| Gasto del mes | $12.000.000 | — |

MER = 48M ÷ 12M = **4.0** → el negocio crece sano aunque Meta "solo se anote" 30-40M. Decides escalar con el MER y el backend, no con la columna bonita.

## CTWA y leads: atribución más limpia

Buena noticia para Colombia: en **Click-to-WhatsApp** y lead ads la atribución es casi binaria — la conversación/lead existe y vino del anuncio, punto. No hay view-through fantasma en el conteo de conversaciones. Lo que queda en tus manos es el tramo final: qué % de chats se vuelve venta (tasa de cierre — mídela por semana y por anuncio; guiones en ventas_lushows). Ahí no hay modelo de Meta que te engañe, solo tu propio Excel sin llenar.

## Regla práctica de decisión

- **Decisiones de negocio** (¿sigo invirtiendo? ¿subo presupuesto global?): con tendencias del **backend + MER**.
- **Decisiones comparativas** (¿qué campaña/creativo es mejor?): con **Ads Manager**, porque el sesgo de atribución aplica parejo a todos tus anuncios — los números absolutos mienten, pero el ranking ENTRE campañas/creativos suele ser direccional y útil.
- Para comparar fino prospecting vs retargeting, pon ambos en 1d-click o 7d-click (sin view) y reduces el sesgo más gordo.

## Errores comunes — blacklist

- Tomar el ROAS de Ads Manager como verdad contable y "celebrar" mientras la cuenta bancaria no crece.
- Comparar el ROAS de retargeting (inflado por view-through sobre gente que YA te conocía) contra prospecting y concluir que "retargeting es lo único que funciona" (ver 24).
- Apagar una campaña por las ventas de AYER: con ventana 7d-click, las conversiones de hoy se siguen "acomodando" a días anteriores; espera 3-7 días para juzgar un período.
- Sumar conversiones de Meta + Google + TikTok + email y reportar el total: contaste la misma venta varias veces.
- Cambiar la ventana de atribución del ad set buscando "ver más resultados": cambia el reporte Y la optimización; hazlo solo con intención.
- No exportar tu histórico antes de que la retención recortada 2026 lo borre: luego no podrás comparar año contra año.
- No medir tasa de cierre de WhatsApp y evaluar campañas CTWA solo por costo por conversación: conversaciones baratas de curiosos quiebran igual.
