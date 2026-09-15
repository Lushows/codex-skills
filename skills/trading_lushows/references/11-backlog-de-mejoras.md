# 11 — Backlog de mejoras (priorizado — actualizar cada sesión)

## 🔴 Antes del 22-ago (afectan la evaluación go-live)

1. ✅ ~~Investigar bug L3~~ (6-jul): el auto-trader SÍ tenía el gate correcto; el trade
   "convicción 0" era una orden sin etiqueta de origen. Fix: `source: 'auto'|'manual'` +
   `conviction` + `analysisId` en cada posición — ahora todo trade es auditable.
2. ✅ ~~Filtro anti-extensión (L1)~~ (6-jul): implementado en `engine.js` — si el precio está
   >3% sobre la SMA20, BUY se convierte en HOLD con convicción ≤4 (cap en CÓDIGO, no en prompt).
   **Medir su efecto en el PF durante julio.**
3. ✅ ~~Anti-clustering (L2)~~ (6-jul): `maxPositionsPerPair: 1` en el broker — imposible
   duplicar posición en el mismo par.
4. **Vigilar el ritmo de trades tras los filtros**: los filtros nuevos reducirán señales;
   si la proyección cae bajo ~25 trades al 22-ago, considerar tercer par (SOL) — no bajar threshold.

## 🟠 Fase 8 técnica (julio-agosto, en paralelo)

4. ✅ ~~Cliente Binance firmado (HMAC) + liveBroker + OCO + reconciliación~~ (v2.1, 14-jul — falta encender en testnet) + `liveBroker` + OCO + reconciliación — ver `09`.
5. Servicio Render en **Frankfurt** (geo-bloqueo US) — probar primero con un servicio gemelo.
6. **Testnet** end-to-end ≥2 semanas.
7. Kill switch + límite de pérdida diaria + notificaciones de órdenes (WhatsApp webhook ya
   previsto en spec, no construido).

## 🟡 Estrategia (después de medir el efecto de lo rojo)

8. ✅ ~~SHORT en paper~~ (v2.0, 14-jul) — duplica regímenes operables (hoy solo trending-up/risk-on). Cambio
   grande: broker, watcher, sizing, prompts. Hacerlo DESPUÉS del filtro anti-extensión para no
   mezclar dos cambios y no poder atribuir el resultado.
9. Tercer par (SOLUSDT) — más señales sin tocar la estrategia.
10. Multi-timeframe (4h filtra al 1h) + ATR formal + volumen.
11. A/B de prompts de convicción (infra de abTest existe en GASTROWHATS como referencia).

## 🟢 Nice-to-have

12. Backtesting histórico con las velas guardadas (validar cambios de prompt sin esperar semanas).
13. Dashboard: panel de "lecciones" que lea los meta-análisis y muestre las reglas derivadas.
14. Exportar métricas a la skill automáticamente (endpoint → módulo 10).

## Hecho

- ✅ v1.2 (6-jul-2026): Sonnet 5 + adaptive thinking, SDK 0.110, precios corregidos, README real.

## De la auditoría v1.6 (6-jul) — pendientes priorizados

- ✅ ~~Dashboard ciego al modo nuevo~~ (v1.7, 6-jul): cards hardcodeadas BTC/ETH (SOL invisible), no muestra
  source/convicción/régimen en posiciones, ni consume /api/lessons ni /api/calibration.
  → Tab "Aprendizaje" + cards dinámicas desde config.pairs. (Sesión dedicada de UI.)
- ✅ ~~Contrafactuales~~ (v1.7, 6-jul): los ~60 HOLDs/semana y los bloqueos del filtro anti-extensión nunca
  se evalúan (¿el filtro salva plata o mata ganadores?). Job horario sin IA que mire qué hizo
  el precio 24h después y guarde saved|missed.
- ✅ ~~Meta-análisis → decisión~~ (v2.1, 14-jul): las recommendations semanales se archivan y nadie las lee.
  Inyectar la última al prompt de convicción (acotada) o flujo propuesta→aprobación de Luis.
- 🟡 rrRatio siempre =2 por construcción (input constante disfrazado de señal; branches de PTJ
  muertos) → derivar target de resistencia real o quitar el input.
- 🟡 Guard de staleness de currentPrices (si el precio tiene >X min, no operar).
- 🟡 JSON parse de Claude: extracción greedy sin retry (1 retry barato ante fallo).
- ✅ ~~timingSafeEqual + cache countErrors~~ (v2.1, 14-jul) + cachear countErrorsLast24h (bloquea event loop c/30s).
- 🟡 Redondeo de stops a 2 decimales rompe pares sub-$1 (si algún día se agregan).
- 🟡 configVersion en posiciones (calibración ya usa ventana de 60, esto la refina).

## 🔬 De la investigación de mercado (21-jul) — plan de estudio "el mejor cerebro"
Investigación con fuentes reales (López de Prado, Dalio, Renaissance, LiveTradeBench). Artifact
publicado. Todo es simulación offline (cero riesgo); la portería de go-live NO se mueve.

**FASE 1 — base de medición (desbloquea todo):**
1. 🧠 **Journal estructurado**: R obtenido, razón de salida, MAE/MFE (parcial ya), feature-vector
   del estado, flag "respetó el plan". Bajo esfuerzo, prerequisito de todo. → módulo 15.
2. 🧠 **Backtester walk-forward sobre velas guardadas** (EL acelerador): aprender de meses en
   segundos, de ~24 a cientos de decisiones. Con purga/embargo (López de Prado). → módulos 46,140,144.
3. 🧠 **LLM vs regla simple (baseline)**: ¿el LLM aporta edge o narra? Medir expectancy en R +
   Deflated Sharpe. La pregunta central. LiveTradeBench: capacidad del LLM NO correlaciona con
   Sharpe real → el LLM es JUEZ dentro de guardrails, no oráculo de precio.

**FASE 2 — mejor conocimiento (arregla la raíz del bug del short):**
4. **Multi-timeframe** (no operar contra tendencia 4h/1D) — arregla EL bug. Bajo esfuerzo. → módulo 38.
5. **Régimen por volatilidad + CUSUM** (no-rezagado) reemplaza el death-cross SMA50/200. → módulos 03,37.
6. **Funding rate + open interest** (API gratis Binance/Coinalyze): el gap cripto más grande;
   cuándo el rally está apalancado. → módulos 114,135.

**FASE 3 — mejor memoria e intuición:**
7. **Memoria por similitud** (feature-vector + coseno, JS puro): recupera setups parecidos, no
   por keywords. → módulo 83.
8. **Calibrar convicción** contra resultados (¿un 9 gana más que un 5?) — meta-labeling por reglas.
9. **Salidas dinámicas (trailing ATR/Chandelier)** vs R:R fijo 1:2 (deja correr ganadoras). → módulo 24.
10. **2º edge (mean-reversion)** descorrelacionado → mini-ensemble (Dalio Holy Grail). → módulo 119.
11. **Guardarraíl anti-overfitting** del meta-análisis (significancia antes de proponer cambio).

**NO perseguir (humo/infra que no tenemos):** order flow/VPIN (HFT), estrategias "91% win rate"
retail (overfitting), on-chain como gatillo de timing, ML pesado (marginal sobre versiones a mano).
Veredicto RSI/MACD: casi ruido en aislamiento (11M tests) — solo contexto secundario, nunca gatillo.

## 🔴 De la revisión de estado (14-sep-2026) — lo único que importa ahora

El direccional está CERRADO (S8) y el carry es el único edge. Todo el backlog de estrategia
direccional (items 4, 8-11 arriba) queda ARCHIVADO: no se trabaja sobre un edge que no existe.

1. **Leer el bot EU** (5 min, desbloquea todo): entrar a `agente-trading-eu.onrender.com` con el
   usuario/clave del panel y sacar PF, trades cerrados, drawdown de ~7 semanas con
   REGIME_DISCIPLINE + POSITIONING_INTEL encendidos. Sin este dato no hay decisión posible.
2. **Decidir el bot EU: seguir o apagar.** Si el paper con las mejoras nuevas sigue con PF <1.0,
   apagar el servicio ($7/mes que no compran información nueva) y quedarse solo con el carry.
3. **Cerrar LTC del carry demo** (el portero lo pausó, la posición sigue viva 53 días después) y
   resolver el `pending` fantasma de AVAXUSDT en el store.
4. **Portero que CIERRA, no solo pausa**: hoy marca no-elegible y deja la posición abierta.
   Es el hueco operativo más claro del carry.
5. **Citar siempre APR OBSERVADO, no esperado** (S9: el esperado sobreestima 1.3-7×). Cambiar el
   readout del monitor/dashboard para que el número grande sea el observado.
6. **Item 2 del GO-LIVE GATE sigue en ⚠️**: la pata SPOT nunca se abrió en demo → la neutralidad
   delta no está validada end-to-end. Antes de un peso real: abrir el par completo (spot + perp)
   y medir el tracking de las dos patas.
7. **Automatizar el monitor** (cron/Render job): 53 días sin una lectura es la prueba de que un
   monitoreo manual no se hace.
