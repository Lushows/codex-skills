# 138 — Dashboards y visualización: qué mirar (y qué no)

> Un dashboard de trading no es para mirar el precio cada 10 minutos — eso es entretenimiento
> que induce a intervenir. Es para responder una pregunta semanal: **¿el sistema sigue sano?**

## Lo que vale la pena mirar (revisión semanal)

| Vista | Pregunta que responde |
|---|---|
| **Curva de equity** | ¿El capital simulado sube, baja o va de lado? ¿La pendiente cambió? |
| **PF rodante** (últimos N trades) | ¿El edge se mantiene o se está degradando? |
| **Drawdown actual y máximo** | ¿Cuánto se ha caído desde el pico? ¿Rompe el criterio (<15%)? |
| **Señales/trades por régimen** | ¿En qué régimen gana y en cuál pierde? (ej: solo gana en trending-up) |
| **Costo de IA acumulado** | ¿Cuánto cuesta correr el cerebro vs el capital que maneja? |
| **Salud técnica** | ¿WebSocket vivo? ¿Errores 24h? ¿Huecos en velas? |

**PF rodante**: el profit factor calculado solo sobre los últimos N trades (ej: 20), no sobre toda
la historia. Detecta degradación reciente que el PF total esconde.

## Lo que NO vale la pena mirar

- El precio en tiempo real (el bot ya lo mira por ti; tú mirándolo solo genera ansiedad).
- El P&L de la posición abierta cada hora — el resultado de UN trade es ruido.
- Rankings de "mejores monedas del día" — invitan a perseguir lo que ya subió.

## Principio de diseño

Cada gráfica debe empujar una **decisión posible**: seguir igual, pausar el bot, revisar una
regla, o escalar. Si una gráfica no cambia ninguna decisión, es decoración.

## Cómo aplica al AGENTE TRADING

- El dashboard actual (SPA con tabs Mercado, Portafolio, Análisis, Performance, Reportes) ya
  cubre: equity (`/api/equity`), métricas (`/api/metrics` con maxDrawdown y sharpe), trades,
  análisis históricos y los meta-análisis semanales que Claude escribe sobre sí mismo.
- **Lo que le falta** (backlog razonable):
  1. **PF rodante** — hoy solo hay PF total (0.89 con 10 trades, muestra aún chica).
  2. **Desglose por régimen** — cruzar resultado de cada trade con el régimen de macroRegime
     al momento de entrar; es la vista que más aprendizaje daría.
  3. **Alerta de huecos en velas** — salud de datos visible, no solo errores de conexión.
- Ritual sugerido para Luis: revisar el dashboard **una vez por semana** junto al meta-análisis,
  no a diario. Con 10 trades, cualquier lectura diaria es leer ruido.
