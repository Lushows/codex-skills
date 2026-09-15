# 63 — Ads Manager como instrumento de decisión

El Ads Manager por defecto está configurado para confundirte: columnas que no usas, métricas de vanidad primero. Este módulo lo convierte en un tablero donde decides en 30 segundos. Configúralo UNA vez (20 minutos) y úsalo todos los días. Prerequisito: saber qué métrica informa qué decisión (ver 60). Actualizado jun-2026.

## 1. Columnas custom: tu preset de decisión

Pasos exactos en la UI:
1. Ads Manager → botón **Columnas** (arriba de la tabla) → **Personalizar columnas**.
2. Quita lo que no decide nada (alcance, clics totales, CPC genérico, CTR "todo").
3. Agrega en este orden: **Importe gastado**, **Compras** (o **Conversaciones iniciadas** + tu evento de calificación si es CTWA), **Costo por compra (CPA)**, **ROAS de compras**, **CTR (clics salientes)**, **CPM**, **Frecuencia**, y si usas video: **Reproducciones de 3s**, **ThruPlays**, **% reproducción al 50%**.
4. Abajo a la izquierda: marca **"Guardar como preset"** → nómbralo "DECISIÓN" → fíjalo como vista por defecto.

Resultado: cada fila se lee izquierda→derecha como una frase: "gasté X, compré Y a CPA Z, porque el ad detiene (CTR) y la subasta está a CPM W". Crea un segundo preset "CREATIVO" (gasto, compras, CPA, CTR saliente, 3s plays, % al 50%, frecuencia) para la revisión de ads del 68.

**Nota de atribución 2026:** la ventana por default es **7d-click / 1d-view**. Meta **quitó las ventanas view-through de 7 y 28 días del Ads Insights API el 12-ene-2026**: en la práctica el view-through ya casi no infla tus columnas. Si activaste **atribución incremental**, las columnas reportan MENOS conversiones (solo las causadas) — es lo correcto, no un bug (ver `actualizacion-2026-06`, 16, 65). Fija la ventana de atribución explícitamente en el selector para que todos lean lo mismo.

## 2. Breakdowns (desgloses): dónde están los insights

Botón **Desgloses** → por entrega:
- **Edad/género**: ¿un segmento come presupuesto sin convertir? Accionable en campañas con audiencia manual (puedes excluir); en **Advantage+ Sales** (el nuevo nombre de ASC, ver `actualizacion-2026-06`) lo ves pero NO excluyes → solo informa creativo.
- **Plataforma/ubicación (placement)**: ¿Reels convierte y Audience Network quema plata? Igual: accionable en manual, informativo en Advantage+ placements. Nota 2026: **Instagram Explore se eliminó como placement** y **Threads entró como default** — revisa que Threads no esté comiendo gasto sin convertir antes de excluirlo.
- **Región**: en Colombia, mira ciudades — si Bogotá/Medellín convierten y ciudades sin cobertura de envío gastan, ajusta la geografía (esto SÍ es editable siempre).
- **Día/hora**: patrones de cuándo compra tu gente (cruza con horario de cierre de chat si vendes por WhatsApp).

Cuándo ignorarlos: con poco gasto, cada celda del desglose tiene 2–3 conversiones = ruido. Regla: no actúes sobre un breakdown con menos de ~10 conversiones por celda.

## 3. Comparar rangos de fechas

Selector de fechas (arriba derecha) → "Últimos 7 días" → activa **Comparar** → contrasta contra los 7 anteriores. Cada métrica muestra flecha y % de cambio. Es la forma más rápida de responder "¿estamos mejor o peor?" sin hoja de cálculo. Úsalo siempre en la revisión semanal (ver abajo). Caveat de retención 2026: el histórico de **frecuencia retiene 6 meses** y los **únicos 13 meses** — para series más largas exporta a tu hoja a tiempo (ver 69).

## 4. Filtros y búsquedas guardadas

Botón **Filtros** → ej.: "Entrega = Activa" + "Importe gastado > 0". Guarda con nombre ("ACTIVAS CON GASTO"). Evita revisar 40 ads pausados cada mañana. Otro útil: filtrar por nombre de campaña si usas naming con sistema (ver 66) — p.ej. todas las que contienen "ctwa" o un ángulo creativo.

## 5. Reglas automáticas: red de seguridad, no piloto

Menú ☰ → **Reglas automáticas** → Crear regla. La única que recomiendo de entrada:
- **Pausar ad** SI gasto > 2× tu CPA objetivo Y compras = 0, evaluando últimos 3 días. Ej.: CPA objetivo COP $50.000 → "pausar si gastó >$100.000 con 0 compras".
- Configura **notificación por email** en vez de acción automática mientras aprendes.

Por qué conservadoras: las reglas no ven contexto (atribución que llega tarde, festivo, stock). Útiles como red nocturna; peligrosas como piloto (ver 70-71 para el sistema completo, 69 para qué jamás se automatiza).

## 6. Exportar para reporte

Botón **Informes** → **Exportar datos de la tabla** → CSV/Excel, con tu preset de columnas y el rango del reporte. Esto alimenta tu hoja semanal (ver 64, 69) y el reporte ejecutivo (ver 67). Programa el export el mismo día/hora cada semana para que la serie no tenga huecos.

## La lectura diaria de 5 minutos (en este orden)

1. Vista de campañas, preset DECISIÓN, "Hoy" + "Ayer": ¿gasto corriendo normal? (gasto en $0 o disparado = primero arregla entrega; $0 con campaña "activa" suele ser ad rechazado o saldo, ver 76).
2. CPA/ROAS de ayer vs promedio de la semana: ¿alguna campaña fuera de rango 2×? Si es UN día, anota y espera; no toques nada por un mal día.
3. Filtro ACTIVAS CON GASTO a nivel de ads: ¿algún ad gastó >1–2× CPA sin convertir? Candidato a pausa (criterio completo en 68).
4. Cierra el Ads Manager. En serio. Tocar campañas a diario es la causa #1 de cuentas inestables.

## La revisión semanal profunda (30–45 min, mismo día cada semana)

1. Rango 7 días + Comparar con semana anterior, nivel campaña → ad set → ad.
2. Breakdowns: edad/género, placement, región (solo celdas con ≥10 conversiones).
3. Decisiones de creativo con la matriz del 68 (matar/nuevo hook/iterar cuerpo/escalar).
4. **Triangular contra ventas reales del backend/CRM: MER de la semana (ver 64).** Sin este paso, solo leíste la versión que Meta cuenta de sí misma.
5. Anotar decisiones y razones en tu hoja (ver 69) → alimenta el reporte (ver 67).

## Lectura express por capa (chuleta para no perderte)

| Quiero saber… | Columna(s) | Compárala contra |
|---|---|---|
| ¿La subasta está cara? | CPM, Frecuencia | Tu histórico, no benchmarks ajenos |
| ¿El creativo trabaja? | CTR saliente, 3s plays | 0.5–2%; thumbstop 20–35% (ver 68) |
| ¿Convierte? | CPA, ROAS, Compras | Tu CPA máximo = margen/pedido (ver 64) |
| ¿Voy mejor o peor? | Todas, modo Comparar | Semana anterior |
| ¿El negocio gana? | (no está en Ads Manager) | MER del backend (ver 64) |

## Ejemplo de lectura de 30 segundos

Fila de campaña: gasto $480.000, compras 9, CPA $53.333, ROAS 3.1, CTR saliente 1.4%, CPM $16.000, frecuencia 2.1. Lectura: subasta normal (CPM en rango), creativo sano (CTR 1.4%), convierte a CPA bajo tu máximo de $60.000, frecuencia lejos de fatiga. Decisión: candidata a escalar (ver 72), pero confirma con MER semanal antes de subir presupuesto — el ROAS 3.1 es de plataforma, no del banco (ver 64).

## Errores comunes — blacklist
- Usar las columnas por defecto y decidir con "clics" y "alcance".
- Actuar sobre breakdowns con 3 conversiones por celda.
- Tocar presupuestos/audiencias todos los días "porque ayer estuvo malo" — reinicia el aprendizaje.
- Reglas automáticas agresivas que pausan ganadores por una mañana lenta.
- No guardar el preset y reconstruir columnas cada vez (terminas no mirando nada).
- Mirar solo "Hoy": la atribución llega tarde; los números de hoy SIEMPRE se ven peores de lo que serán.
- Cerrar la semana sin triangular contra el backend: te quedas con la foto que Meta se toma a sí misma.
- Confundir el CTR "todo" (infla con clics a foto/perfil) con el CTR saliente real.
