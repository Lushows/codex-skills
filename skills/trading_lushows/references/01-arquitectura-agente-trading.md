# 01 — Arquitectura del AGENTE TRADING (fuente de verdad)

> Actualizar este módulo cuando cambie la arquitectura. Última actualización: **6-jul-2026 (v1.4)**.
>
> v1.3: filtro anti-extensión (>3% sobre SMA20 → HOLD), maxPositionsPerPair=1, source/conviction/analysisId en posiciones.
> v1.4: **ciclo de aprendizaje completo** — posiciones guardan régimen+extensión de ENTRADA; lección
> atribuida al análisis que abrió el trade; bloque CALIBRACION REAL (stats JS por régimen/convicción/par)
> inyectado al prompt de convicción; memoria FIFO 400 con selección balanceada; endpoints
> `GET /api/lessons` y `GET /api/calibration`.

## Qué es

Bot de **paper trading** de cripto (BTCUSDT, ETHUSDT) con IA, propiedad de Luis (Lushows).
Capital simulado $1.000 USD. Swing trading. Corre 24/7 en Render.

- **Carpeta local:** `c:\Users\user\Desktop\AGENTE TRADING`
- **Producción:** https://agente-trading-fjpt.onrender.com (basic auth; credenciales en variables
  de Render `DASHBOARD_USER`/`DASHBOARD_PASS` — NO están en el repo)
- **Deploy:** auto-deploy desde GitHub `main` (Render Starter, disco persistente en `data/`)
- **Región Render:** US — ⚠️ Binance geo-bloquea TRADING desde IPs de USA; los datos llegan por el
  mirror `data-api.binance.vision` (solo lectura). Para Fase 8 live: mover a Frankfurt.

## Stack (v1.2, jul-2026)

| Pieza | Tecnología |
|---|---|
| Runtime | Node.js 20+, ESM, sin framework de tests (node --test, 145 tests) |
| Datos | WebSocket Binance público (velas 1h) + REST mirror |
| IA fast (régimen) | `claude-haiku-4-5-20251001` (sin thinking) |
| IA deep (convicción, meta-análisis) | `claude-sonnet-5` + adaptive thinking (max_tokens 4096–6000) |
| SDK | `@anthropic-ai/sdk` ^0.110 |
| Server | Express 5 + Socket.IO, dashboard SPA single-file |
| Persistencia | JSON en `data/` (en Render: disco persistente) |

## Mapa de código

```
config/tradingConfig.js       ← lee .env (modelos, riesgo, pares, AUTO_EXECUTE_THRESHOLD)
src/binance/                  ← client REST + websocket + parser
src/paperTrading/             ← broker (simulador: comisión 0.1%, slippage 5bps), portfolio, watcher, pnl
src/skills/                   ← macroRegime (Haiku), druckenmiller (Sonnet), positionSizing (JS puro),
                                 traderMemory, technicalAnalysis (RSI/MACD/SMA), tradingPsychology,
                                 wisdomLibrary (6 traders)
src/strategy/                 ← claudeAnalyzer (wrapper SDK + costos), engine (orquestador),
                                 autoTrader, metaAnalyzer (semanal), equityTracker, retryWithBackoff
src/persistence/              ← *Store.js atómicos (candles, portfolio, traderMemory, analyses,
                                 metaAnalyses FIFO 52 semanas, equity, alerts)
src/server.js                 ← Express + Socket.IO + API + basic auth
dashboard/                    ← SPA (tabs: Mercado, Portafolio, Análisis, Performance, Reportes)
```

## Pipeline de un análisis (engine.js)

```
1. tradingPsychology (gate JS: si BLOCK, corta sin gastar tokens)
2. macroRegime (Haiku) → risk-on|risk-off|trending-up|trending-down|ranging
3. traderMemory → lecciones de setups similares filtradas por régimen
4. technicalAnalysis (JS) → RSI/MACD/SMA + resumen de velas
5. druckenmiller (Sonnet) → conviction 1-10 + BUY|HOLD + reasoning (JSON)
6. positionSizing (JS puro, Kelly fraccional cap 1.5% riesgo) → notional, stop, target
```

- Auto-trader corre **cada 2h** por par; ejecuta solo si `conviction >= AUTO_EXECUTE_THRESHOLD` (8).
- Stops/targets los vigila `watcher.js` **localmente** (⚠️ en live deben vivir en el exchange, OCO).
- **Solo LONG** — no existe SHORT todavía (backlog `11`).

## Endpoints útiles (con basic auth)

```
GET /status                 ← salud completa: uptime, ws, costo Claude, auto-trader, errores 24h
GET /api/portfolio          ← balance, posiciones abiertas y cerradas
GET /api/trades             ← trades cerrados
GET /api/metrics            ← maxDrawdown, sharpeRatio
GET /api/equity             ← curva de equity
GET /api/meta-analyses      ← reportes semanales que Claude escribe sobre sí mismo
GET /api/analyses           ← historial de análisis
GET /api/trades/export      ← CSV
POST /api/auto-trader/start|stop
POST /api/meta-analysis/run ← forzar meta-análisis manual
```

## Reglas de protección vigentes (config)

| Regla | Valor |
|---|---|
| Riesgo máx por trade | 1.5% del capital inicial |
| Posiciones simultáneas máx | 2 |
| Convicción mínima auto-ejecución | 8/10 (`AUTO_EXECUTE_THRESHOLD`) |
| Cooldown tras 3 pérdidas seguidas | 4h (tradingPsychology) |
| Bloqueo overtrading | >5 trades/24h |
