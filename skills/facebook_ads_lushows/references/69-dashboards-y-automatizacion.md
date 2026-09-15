# 69 — Dashboards y automatización: salir del Ads Manager para VER el negocio

El Ads Manager te muestra lo que pasa DENTRO de Meta; el negocio vive afuera (ventas reales, margen, WhatsApp, banco). Este módulo te da los tres niveles de tablero según tu tamaño, las alertas que valen la pena y la línea roja de lo que jamás se automatiza. Léelo cuando sientas que "miras muchos números y decides poco", o cuando un cliente pida "un dashboard". Actualizado jun-2026.

Principio rector: **anti-dashboard**. 40 gráficas que nadie lee pierden contra 5 números que deciden. Un dashboard se mide por las decisiones que provoca, no por lo bonito que se ve (ver 67: los números core son los mismos del reporte). Antes de construir nada, pregunta: "¿qué decisión cambia este gráfico?". Si no cambia ninguna, no lo pongas.

Nota de retención 2026 que hace urgente la hoja: Meta recortó el histórico del API (frecuencia **6 meses**, únicos **13 meses**, view-through fuera desde 12-ene-2026; ver `actualizacion-2026-06`). Si no exportas a TU hoja a tiempo, pierdes la serie larga para siempre. Tu dashboard es ahora también tu archivo histórico.

## Nivel 1 — Hoja de cálculo semanal manual (pyme: 15 min/semana)

Suficiente hasta varios millones COP/mes de inversión. Google Sheets, una fila por semana, llenada el mismo día (datos del export de Ads Manager ver 63 + backend/CRM ver 64):

| Columna | Fuente |
|---|---|
| Semana (fecha) | — |
| Gasto Meta (COP) | Ads Manager |
| Gasto total pago (todos los canales) | Suma manual (Meta+Google+TikTok) |
| Conversaciones iniciadas | Ads Manager / WhatsApp |
| Pedidos reales | Backend / CRM de chat (ver 53) |
| Ventas reales (COP) | Backend / banco |
| MER (ventas ÷ gasto total) | fórmula |
| Clientes nuevos / nCAC | CRM |
| Factor inflación (plataforma ÷ real) | fórmula (ver 64) |
| Notas y decisión | tú |

La columna más valiosa es **Notas** ("subimos 40% presupuesto", "se agotó stock del combo", "festivo", "Meta desaprobó el ganador 2 días"): en 3 meses explica cada pico y valle. Con formato condicional (MER en rojo si <breakeven, ver 64) ya tienes "dashboard". Añade una mini-gráfica sparkline de MER por semana y tienes la tendencia que importa más que cualquier semana suelta.

## Nivel 2 — Looker Studio gratis (cuando reportas a un cliente)

Looker Studio (lookerstudio.google.com, gratis) hace gráficas de tendencia automáticas y siempre actualizadas:
- **Datos de Meta**: no hay conector oficial gratuito → usa un conector de terceros (categoría "Facebook Ads" en la galería; los decentes cuestan ~USD 10–30/mes) **o** la vía gratis: tu Google Sheet del nivel 1 como fuente (export semanal y listo). Para una pyme, la vía Sheet es suficiente y no agrega costo.
- Qué armar: UNA página — gráfica de tendencia (gasto vs ventas reales por semana), tarjetas grandes con MER/CPA/nCAC del periodo, y tabla de campañas. Nada más.
- Valor real: el cliente "ve" la tendencia sin pedirte nada y la llamada mensual arranca en la decisión, no en los datos (ver 67).

## Nivel 3 — Herramientas pagas (e-com grande)

Tipo Supermetrics (mueve datos de Meta a Sheets/Looker automático) o un dashboard e-com con atribución propia (conecta Shopify+Meta+Google). Cuándo se justifican: inversión de decenas de millones COP/mes, múltiples canales pagos, o cuando las horas que ahorras valen más que los USD 100–300/mes que cuestan. Antes de eso, son un dashboard caro para los mismos 5 números que ya tenías en la hoja. **Caveat 2026:** su "atribución propia" también es opinión, no verdad — y con view-through fuera del API de Meta, varias de estas herramientas recalibraron sus modelos; valídalos contra tu backend igual que a Meta (ver 64, 65).

## Reglas automáticas de Meta (resumen operativo de 70-71)

Red de seguridad, NO piloto automático:
- Pausar ad si gasto > 2× CPA objetivo con 0 compras (últimos 3 días) — la red nocturna clásica.
- Notificar (no actuar) si el gasto diario se sale ±50% de lo esperado.
- Subir presupuesto solo con regla MUY conservadora y supervisada (nunca dejar que escale sola sin ojos, ver abajo).
- Configúralas conservadoras y en modo notificación primero; las reglas no ven contexto (atribución que llega tarde, festivos, stock) — detalles y plantillas en 70-71.

## Alertas que valen la pena (pocas y accionables)

| Alerta | Umbral sugerido | Por qué |
|---|---|---|
| Gasto diario anómalo | ±50% del plan | Saldo rechazado, ad desaprobado o gasto desbocado |
| CPA fuera de rango sostenido | >1.5× objetivo durante 3 días seguidos | Un día malo es ruido; tres son tendencia (ver 61) |
| Frequency alta en BOFU | >4/semana en retargeting | Quemando la misma gente (ver 39, 65) |
| Entrega en cero | gasto $0 con campaña "activa" | Rechazo de ad, saldo, o cuenta en revisión (ver 76) |
| MER semanal bajo breakeven | < tu breakeven ROAS (ver 64) | Estás pautando a pérdida — revisa YA |

Todo lo demás se mira en la cadencia normal (diaria de 5 min y semanal, ver 63), no por alerta. Más de ~5 alertas activas = fatiga de alertas = no miras ninguna.

## Lo que NUNCA se automatiza

La decisión de **escalar o matar** sin ojos humanos. Los datos deciden, pero tú interpretas el contexto que ningún número trae: temporada (¿es quincena? ¿Q4?), stock (¿puedo cumplir si escalo?), competencia (¿alguien reventó el CPM?), creativo (¿tengo variantes listas si fatigo al ganador? ver 68), atribución (¿el CPA "malo" de hoy es real o llega tarde?). Una regla que escala sola un ad puede duplicar pedidos de un producto sin inventario; una que mata sola puede ejecutar a tu mejor ad por una mañana lenta de atribución. **Automatiza la VIGILANCIA; reserva el GATILLO.**

## La rutina completa que conecta todo (cómo encaja el bloque medición)

1. **Diario 5 min** (ver 63): entrega normal + ningún ad sangrando. Cierra el Ads Manager.
2. **Semanal 30–45 min**: creative analytics (ver 68) + breakdowns + **triangular MER contra backend** (ver 64) + llenar la hoja (este módulo) → genera el reporte (ver 67).
3. **Mensual**: tendencia 3 meses + learnings acumulados + tests de incrementalidad (ver 65) → PDF ejecutivo (ver 67).
4. **Trimestral**: re-leer `actualizacion-2026-06` y verificar qué cambió en Meta (precios, atribución, features).
La hoja del nivel 1 es el hilo que cose toda esta rutina: sin ella, cada semana arranca de cero.

## Errores comunes — blacklist
- Armar el dashboard de 40 gráficas antes de tener la hoja de 10 columnas funcionando.
- Dashboard solo con datos de Meta: sin ventas reales del backend solo automatizaste la versión inflada (ver 64).
- Pagar herramienta de USD 200/mes gastando COP 2M/mes en ads.
- Reglas automáticas agresivas como "piloto": escalan sin stock y matan ganadores.
- Alertas para todo → fatiga de alertas → no miras ninguna.
- Llenar la hoja "cuando haya tiempo": la serie con huecos no sirve para tendencias ni para el reporte (ver 67), y en 2026 lo que no exportaste a tiempo el API ya no te lo devuelve.
- Confiar en la "atribución propia" de una herramienta paga como verdad absoluta: valídala contra el banco igual que a Meta (ver 65).
