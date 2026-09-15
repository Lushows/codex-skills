# 97 — Multi-exchange (cuándo sí, y por qué HOY no)

> Operar en más de un exchange suena a diversificación inteligente. Para un bot de una persona
> con $200-500, es complejidad que multiplica los puntos de fallo sin multiplicar el edge.

## Las razones legítimas para un segundo exchange (algún día)

| Razón | Qué significa |
|---|---|
| Riesgo de plataforma | Si Binance congela cuentas, sufre un hackeo o restringe tu país, no quieres el 100% ahí. Es el riesgo real más serio (los exchanges HAN quebrado: el caso FTX en 2022 es la cicatriz de la industria) |
| Mejores fees | Otro exchange puede cobrar menos por operar; con volumen alto, importa |
| Mejor liquidez en un par | Para pares exóticos. BTC/ETH tienen liquidez profunda en cualquier exchange grande |
| Redundancia operativa | Si la API de uno se cae, el otro sigue |

## Lo que cuesta de verdad (la letra pequeña)

Cada exchange adicional duplica o complica:

- **Código**: otro cliente firmado (cada API firma distinto), otros formatos de error, otros
  filtros de órdenes, otro tipo de OCO (o su ausencia). No es "cambiar una URL".
- **Reconciliación**: el módulo 93 ahora tiene DOS fuentes de verdad externas. Los huérfanos
  se buscan en dos lados.
- **Seguridad**: dos juegos de keys, dos whitelists, dos superficies de ataque (módulo 92).
- **Capital fragmentado**: $400 partidos en dos exchanges = posiciones más chicas, fees mínimos
  que pesan más, y saldo muerto en el lado que no está operando.
- **Testing**: dos testnets (si el otro tiene), dos matrices de fallos, doble mantenimiento
  cuando cualquiera de los dos cambia su API.

Regla honesta: el segundo exchange NO agrega edge (la estrategia es la misma); solo agrega
resiliencia. Y la resiliencia tiene sentido cuando hay algo grande que proteger.

## ¿Cuándo tendría sentido para nosotros?

Todas estas a la vez, no una:

1. Capital escalado a niveles donde el riesgo de plataforma duele de verdad (miles, no cientos).
2. Sistema live estable ≥6 meses sin incidentes — la operación con UN exchange ya es aburrida.
3. Una razón concreta (fees medidos que ahorrarían $X/mes, o señal regulatoria sobre Binance
   en la región) — no "por si acaso" genérico.

Mientras tanto, la protección contra el riesgo de plataforma es más simple: **retiros
periódicos** (módulo 96). Sacar ganancias del exchange regularmente protege más que tener
dos exchanges llenos.

## Cómo aplica al AGENTE TRADING

- Decisión actual: **un solo exchange (Binance), spot, BTC/ETH**. Nada multi-exchange en
  Fase 8 ni en el primer año live salvo cambio de circunstancias.
- El geo-tema ya nos enseñó que cada exchange trae sorpresas regulatorias (Binance bloquea
  trading desde IPs de EE.UU. → mudanza a Render Frankfurt, módulo 09). Multiplicar exchanges
  multiplica ese tipo de sorpresas.
- Si algún día se evalúa, se abre como proyecto propio con su testnet y sus 2 semanas de
  prueba — mismo estándar que la Fase 8 original.
