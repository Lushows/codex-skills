# 09 — Fase 8: transición a real (plan técnico)

> Construir en julio-agosto 2026, en paralelo al paper. Nada de esto toca dinero hasta que
> `08-criterios-go-live.md` esté en verde.

## Bloqueadores conocidos (resolver en orden)

1. **Geo-bloqueo Binance**: el servicio corre en Render US; Binance rechaza TRADING desde IPs de
   EE.UU. (el mirror `data-api.binance.vision` es solo datos). Solución: recrear el servicio en
   **Render Frankfurt (región EU)** con el mismo repo + disco. Verificar latencia WS aceptable.
2. **No existe modo live en el código**: `broker.js` es 100% simulador. Falta la rama real.
3. **Stops locales**: `watcher.js` vigila stops en memoria. En live los stops DEBEN vivir en el
   exchange (órdenes **OCO**: stop-loss + take-profit atados), porque si Render cae, el stop queda.

## Arquitectura del modo live (Strategy Pattern, ya previsto en el spec)

```
config: MODE=paper | live          ← mismo código, distinta ejecución
broker.placeOrder()
  ├─ MODE=paper → simulateOrder()  (lo actual, intacto)
  └─ MODE=live  → executeRealOrder()
        ├─ POST /api/v3/order (MARKET o LIMIT, firmado HMAC-SHA256)
        ├─ POST /api/v3/order/oco (stop + target en el exchange)
        └─ reconciliación: el estado real del exchange manda sobre el JSON local
```

Componentes nuevos: `src/binance/signedClient.js` (HMAC, timestamp, recvWindow),
`src/liveTrading/liveBroker.js`, `src/liveTrading/reconciler.js` (sincroniza posiciones
exchange↔local al arrancar), ampliar `/status` con estado de la cuenta real.

## Testnet primero (el puente gratis)

- `testnet.binance.vision` — API real de Binance con dinero falso. Misma firma, mismos endpoints.
- Config: `BINANCE_REST_URL=https://testnet.binance.vision` + API keys del testnet.
- Meta: **≥2 semanas en testnet sin incidentes** (órdenes ejecutadas, OCO respetados, reconexión
  correcta, reconciliación al reiniciar) antes de tocar la cuenta real.

## Seguridad de la cuenta (no negociable)

- Cuenta Binance de Luis con KYC completo.
- API keys: permisos SOLO "Enable Spot Trading" — **jamás withdrawal**.
- Whitelist de IP (la IP fija del servicio Render EU).
- Keys en variables de entorno de Render, nunca en el repo ni en el dashboard.

## Rieles de operación live

| Riel | Regla |
|---|---|
| Kill switch | Botón en dashboard + endpoint; cierra posiciones y apaga auto-trader |
| Límite pérdida diaria | −3% del capital en un día → kill switch automático |
| Modo híbrido (mes 1) | Bot propone → notifica (WhatsApp/dashboard) → Luis confirma |
| Alertas | Cada orden real ejecutada notifica de inmediato |
| Auditoría | Log estructurado de cada orden con request/response del exchange |

## Impuestos (cuando haya ganancias reales)

Las utilidades de cripto en Colombia se declaran (renta/ganancia ocasional según el caso).
Cuando lleguen las primeras ganancias reales → invocar `contador_lushows`. En paper: no aplica.
