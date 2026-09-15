# 71 — FOMO a fondo

**FOMO** (Fear Of Missing Out): el miedo a quedarse por fuera de un movimiento que "todos" están
aprovechando. Es el sesgo que más plata le saca al trader retail de cripto, porque cripto produce
subidas verticales y pantallas verdes diseñadas (sin querer) para dispararlo.

## Anatomía del FOMO

1. **Disparador**: el precio sube fuerte y rápido; lo ves en el gráfico, en Twitter, en el grupo.
2. **Narrativa instantánea**: el cerebro fabrica una razón ("esta vez es distinto", "va a $200k").
3. **Urgencia falsa**: sientes que si no entras YA, pierdes la oportunidad de tu vida.
4. **Entrada tardía**: compras después de que el movimiento ya ocurrió, cerca del pico local.
5. **Resaca**: el precio retrocede a su media, tu posición queda roja, y ahora el miedo es al revés.

## Por qué entrar tarde es estadísticamente caro

Cuando el precio está **extendido** (muy por encima de su media móvil, RSI alto), la matemática
juega en contra:

| Factor | Efecto |
|---|---|
| Reversión a la media | Los precios extendidos tienden a retroceder hacia su promedio antes de continuar (si continúan) |
| Stop lejano | Para darle "aire" al trade, el stop queda lejos → riesgo por unidad más grande → posición más pequeña o pérdida mayor |
| Asimetría rota | El grueso del movimiento ya pasó; te queda poco upside y todo el retroceso de downside |
| Vendedores esperando | Quienes compraron abajo tienen ganancias enormes listas para tomar — tú eres su liquidez de salida |

No significa que "nunca sube más". Significa que, en promedio y con muchos trades, comprar
extendido pierde contra comprar en retrocesos. El edge está en la repetición, no en el caso épico.

## El caso real del bot (jul-2026)

Tras una racha de 4 wins, el AGENTE TRADING entró **3 veces en precio extendido y perdió las 3
(0/3)**. El bot no "sintió" nada: su prompt de convicción simplemente no penalizaba la extensión,
así que un momentum fuerte le parecía un setup fuerte. Mismo comportamiento que un humano con
FOMO, producido por una regla ausente. Lo detectó el propio meta-análisis semanal (módulo 84).

## Filtros anti-FOMO (para humanos y para bots)

- **Distancia a la media**: si el precio está a más de X% de su SMA, no hay entrada; se espera retroceso.
- **RSI techo**: no comprar con RSI en zona de sobrecompra (p. ej. >70) sin señal adicional.
- **Regla de las velas**: ¿cuántas velas verdes seguidas lleva? Después de N seguidas, la entrada se degrada.
- **Pregunta de control**: "¿este trade lo tomaría si el precio llevara 3 días plano?" Si la única razón es la subida reciente, es FOMO.
- **Precio límite, no market**: obligarse a entrar solo en retroceso convierte el FOMO en paciencia.

## Cómo aplica al AGENTE TRADING

- La lección 0/3 vive en `traderMemory` y se inyecta al prompt de convicción cuando el setup se parece.
- El fix estructural es de reglas, no de regaño: penalizar extensión explícitamente en el prompt de Druckenmiller y/o un filtro JS previo (distancia a SMA / RSI) que degrade la convicción antes de llegar a Sonnet.
- Para Luis: si el bot no entró en una subida épica, eso NO es un error del bot — es el filtro haciendo su trabajo. El costo de perderse un cohete es menor que el costo acumulado de comprar picos.
