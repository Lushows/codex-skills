# 194 — Implementación de SHORT

**SHORT** = ganar cuando el precio BAJA: vendes primero (algo prestado o un derivado) y recompras
más barato. Hoy el bot solo opera LONG (comprar barato, vender caro), lo que significa que en
mercado bajista o lateral-bajista está condenado a mirar. Agregar SHORT **duplica los regímenes
operables** — es la expansión con mejor razón de existir del roadmap.

## Por qué duplica los regímenes

| Régimen del mercado | Bot solo-LONG | Bot LONG+SHORT |
|---|---|---|
| Tendencia alcista | ✅ Opera | ✅ Opera (LONG) |
| Tendencia bajista | ❌ Espera (a veces meses) | ✅ Opera (SHORT) |
| Lateral | ⚠️ Pocas señales | ⚠️ Pocas señales (SHORT no arregla el lateral) |

Beneficio extra: más regímenes operables = más trades = la muestra de 30+ se llena más rápido.

## Qué hay que construir (no es "un if invertido")

1. **Broker/instrumento**: en spot no puedes vender lo que no tienes. Opciones: margin de Binance
   o futuros perpetuos (verificar al día disponibilidad y requisitos para la cuenta de Luis).
   Ambas implican una forma de apalancamiento — usarlo en 1x efectivo, jamás para amplificar.
2. **Watcher espejo**: en SHORT todo se invierte — el stop va ARRIBA del precio de entrada, el
   target ABAJO. El watcher y el cálculo de R:R necesitan la rama invertida, con tests propios.
3. **Sizing**: la fórmula de Kelly/1.5% es la misma, pero la distancia al stop se mide hacia
   arriba. Cuidado con un detalle sucio: en futuros hay *funding* (pago periódico entre longs y
   shorts) que es un costo extra que el modelo de 0.30% no incluye — modelarlo, verificar al día.
4. **Prompts**: régimen (Haiku) y convicción (Sonnet) hoy piensan en clave LONG. Hay que
   reescribirlos para evaluar setups bajistas SIN sesgo — y pasar por `195` (A/B en paper) porque
   es un cambio grande de prompt.
5. **Memoria**: traderMemory arranca de CERO para SHORT. Los patrones aprendidos en LONG
   (ej. $1.788/$1.760) no aplican al lado corto.

## Los riesgos específicos del SHORT (más peligroso que LONG)

- **Pérdida teóricamente ilimitada**: en LONG lo peor es −100% (el precio llega a 0); en SHORT
  el precio puede subir 200%, 500%... El stop pasa de importante a VITAL — solo OCO en el
  exchange, jamás únicamente en el watcher.
- **Short squeeze**: cuando muchos están en corto y el precio sube, los cortos cierran comprando,
  lo que empuja el precio MÁS arriba en cascada. En cripto los squeezes son violentos y saltan
  stops (el precio "brinca" el nivel: slippage grande en el peor momento).
- **Sesgo estructural**: cripto ha pasado más tiempo subiendo que bajando en su historia; los
  rallies bajistas en contra son brutales. El SHORT exige convicción ≥8 con más razón que el LONG.

## Cómo aplica al AGENTE TRADING

- Orden correcto: SHORT es candidato a **PIVOT** del 22-ago (si PF <1.3, es una de las variables
  grandes permitidas) o mejora post-live — NUNCA se agrega mientras otra variable está en prueba
  (un cambio a la vez, `193`, `195`).
- Todo el ciclo completo aplica de nuevo: paper con SHORT ≥30 trades y PF >1.3 propios (atribución
  separada LONG/SHORT) antes de que un SHORT toque dinero real.
- Nota de MEMORY del proyecto: "SHORT paper" ya está en la lista de próximos — este módulo es su
  especificación de partida.
- Elección de instrumento (margin vs perpetuos, costos de funding) → números a `Matematicas_lushows`,
  decisión de riesgo de negocio → `economist_lushows`.
