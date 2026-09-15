# 166 — Testing de sistemas de trading: los 145 tests del bot

## Por qué los tests importan más aquí que en una web

En una web, un bug muestra una página fea. En un bot de trading, un bug **pierde plata en
silencio a las 3am**. Y hay un agravante: el bot opera solo, sin un humano mirando cada acción.
Los tests son la única supervisión permanente.

## Qué es un test (en simple)

Un test es código que ejecuta tu código con datos conocidos y verifica que el resultado sea el
esperado. El bot usa `node --test` (el runner incluido en Node 20 — sin instalar nada) y hoy
corren **145 tests** en segundos, gratis, antes de cada cambio.

## Las capas de testing del bot

| Capa | Qué prueba | Ejemplo real |
|---|---|---|
| **Unit por módulo** | Cada pieza aislada | `positionSizing`: con capital X, riesgo 1.5% y stop Y, el notional debe ser exactamente Z |
| **Mocks de Claude** | La lógica alrededor de la IA, sin llamar a la IA | Se inyecta un cliente falso que devuelve `{conviction: 9, action: "BUY"}` y se verifica que el engine reaccione bien; también respuestas malformadas |
| **Escenarios de negocio del broker** | Historias completas del simulador | "Abrir posición, precio cae al stop → el watcher cierra, cobra comisión 0.1% y slippage, el PnL cuadra" |
| **Reglas de protección** | Que los frenos frenen | Cooldown tras 3 pérdidas, bloqueo >5 trades/24h, máximo 2 posiciones |

Los **mocks** son posibles gracias a la inyección de dependencias (módulo 160): como el engine
recibe el cliente de Claude como parámetro, el test le pasa uno falso. Beneficio doble: los tests
no gastan tokens y no dependen de que la API esté arriba.

## Qué debe probarse SIEMPRE en un sistema de trading

- **La aritmética del dinero** (sizing, comisiones, PnL): un off-by-one aquí es pérdida directa.
- **Los bordes:** capital casi cero, stop igual al precio de entrada, respuesta de Claude sin el
  campo esperado, JSON corrupto al leer.
- **Que los límites bloqueen:** es más grave que un freno no frene a que un motor no arranque.

## Lo que falta (honesto)

| Hueco | Riesgo | Plan |
|---|---|---|
| **E2E** (end-to-end: el sistema completo corriendo junto, WS real + engine + broker) | Los módulos funcionan solos pero podrían no encajar en producción | Parcialmente cubierto por 44 días de paper trading — que ES un test E2E continuo |
| **Testnet de Binance** | Nada ha probado aún el camino de órdenes REALES (firmas, OCO, errores del exchange) | Fase 8: testnet obligatorio antes del go-live 22-ago-2026 |
| **Tests de caos** | ¿Qué pasa si el disco se llena, si Claude tarda 5 min? | Deseable, no bloqueante |

Verdad incómoda: **145 tests verdes no prueban que la estrategia gane plata.** Prueban que el
sistema hace lo que se diseñó. Que el diseño gane es pregunta del track record (paper y luego
live chico), no de los tests.

## Cómo aplica al AGENTE TRADING

La regla del proyecto: ningún cambio entra a `main` sin que los 145 pasen (y todo cambio de
lógica trae tests nuevos). Antes del go-live, la lista de arriba manda: correr el flujo completo
de órdenes contra el **testnet** de Binance desde Frankfurt, incluyendo OCO y los códigos de
error del exchange. Es la última red antes del dinero real.
