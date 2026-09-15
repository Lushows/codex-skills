# 13 — Operación y monitoreo de producción

## Acceso

- URL: `https://agente-trading-fjpt.onrender.com` — basic auth (credenciales en Render →
  Environment: `DASHBOARD_USER` / `DASHBOARD_PASS`; también en la memoria local del agente).
- Deploy: push a `main` en GitHub → Render auto-despliega. Manual: Render → Manual Deploy.
- Datos persistentes en el disco de Render (`data/`): portfolio, trades, memoria, meta-análisis.
  ⚠️ Recrear el servicio sin migrar el disco = perder el historial de aprendizaje.

## Chequeo rápido (el pulso en 30 segundos)

```bash
curl -s -u "$USER:$PASS" https://agente-trading-fjpt.onrender.com/status
```

Leer: `status:healthy`, `binance_ws.connected:true`, `errors_last_24h:0`,
`claude_api.totalCostUsd` (techo mental: ~$15/mes), `auto_trader.enabled:true`.

## Revisión semanal (el ritual)

1. `/api/meta-analyses` → leer el último reporte: narrativa + patrones + propuestas del propio bot.
2. `/api/metrics` → drawdown y sharpe. `/api/trades` → PF y win rate acumulados.
3. Contrastar contra la tabla de `08-criterios-go-live.md`.
4. **Registrar toda lección nueva en `10-lecciones-aprendidas.md` con fecha.**
5. Si el bot propone un ajuste sensato en su meta-análisis → pasa al backlog `11`, NUNCA se
   aplica caliente el mismo día.

## Cálculo de PF/win rate desde el API (si el dashboard no lo muestra)

```bash
curl -s -u "$USER:$PASS" .../api/trades | node -e "let d='';process.stdin.on('data',c=>d+=c).on('end',()=>{
const a=(JSON.parse(d).trades||JSON.parse(d));const w=a.filter(x=>x.pnl>0),l=a.filter(x=>x.pnl<=0);
const gw=w.reduce((s,x)=>s+x.pnl,0),gl=Math.abs(l.reduce((s,x)=>s+x.pnl,0));
console.log('trades',a.length,'| win rate',(w.length/a.length*100).toFixed(1)+'%','| PF',(gw/gl).toFixed(2),'| neto',(gw-gl).toFixed(2))})"
```

## Señales de alarma (actuar ya)

| Señal | Acción |
|---|---|
| `errors_last_24h` > 10 | Revisar logs en Render; posible WS inestable |
| Costo API se dispara (>$1/día) | Revisar frecuencia del auto-trader / loop de retries |
| Trade que viola protocolo (convicción < threshold) | Parar auto-trader, auditar (ver L3) |
| Drawdown > 8% | Revisión completa de estrategia antes de seguir |
| Servicio dormido/caído | Render → logs; el watcher local no vigila stops mientras está caído |
