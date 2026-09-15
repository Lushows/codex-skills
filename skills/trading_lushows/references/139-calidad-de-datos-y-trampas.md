# 139 — Calidad de datos: gaps, timestamps y otras trampas

> Regla de oro: **basura entra, basura sale**. Un backtest sobre datos con huecos o duplicados
> produce conclusiones falsas con total confianza. Validar datos es aburrido y es lo primero.

## Las trampas clásicas

### 1. Gaps (huecos en las velas)
Falta la vela de las 14:00 porque el WebSocket estuvo caído. Consecuencias:
- Los indicadores (RSI, medias móviles) se calculan mal sin avisar.
- Un backtest "salta" el hueco como si el precio hubiera teletransportado.

Detección: verificar que entre vela y vela haya exactamente el intervalo esperado (1h = 3.600.000 ms).

### 2. Timestamps ambiguos
- ¿La marca de tiempo es de **apertura** o de **cierre** de la vela? Binance usa apertura.
  Confundirlo desplaza todo 1 hora → look-ahead bias accidental (módulo 142).
- ¿Zona horaria? Todo debe estar en **UTC** y en milisegundos epoch. Mezclar hora local de
  Colombia con UTC produce huecos y duplicados fantasma.

### 3. Duplicados y velas mutantes
La vela "en curso" cambia hasta que cierra. Si guardas la misma vela dos veces (una a medio
formar, otra cerrada) tienes duplicados con valores distintos. Regla: **persistir solo velas
cerradas**, y si llega de nuevo la misma marca de tiempo, sobrescribir, no acumular.

### 4. Datos de exchanges caídos o ilíquidos
Durante mantenimientos o pánicos, algunos exchanges imprimen precios absurdos (mechas falsas) o
dejan de imprimir. Contra esto: chequeos de cordura (¿el high es mayor que el low? ¿el cierre está
dentro del rango? ¿el salto vs la vela anterior es físicamente creíble?).

## Checklist mínimo antes de cualquier backtest

- [ ] Sin gaps (o gaps documentados y excluidos)
- [ ] Sin duplicados de timestamp
- [ ] Todo en UTC, misma unidad (ms)
- [ ] OHLC coherente en cada vela (high ≥ open/close ≥ low, volumen ≥ 0)
- [ ] Solo velas cerradas

## Cómo aplica al AGENTE TRADING

- El bot **ya valida velas antes de persistir** en `candlesStore` (estructura y cierre) — esa
  disciplina es la que hace que el dataset JSON sirva para el backtesting del backlog.
- Antes de correr el primer backtest: escribir un **script de auditoría** del JSON de velas
  (gaps, duplicados, coherencia OHLC) y correrlo SIEMPRE antes de cada backtest. Es una tarde de
  trabajo que evita semanas de conclusiones falsas.
- Los huecos por caídas del WS en Render deben rellenarse vía el mirror REST — verificar que el
  relleno realmente ocurre revisando continuidad, no confiando en que "debería".
