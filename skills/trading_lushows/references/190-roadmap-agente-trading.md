# 190 — Roadmap del AGENTE TRADING

El mapa completo del proyecto: de dónde viene, dónde está y a dónde va. Regla general del
roadmap: **nunca se salta una etapa** (ver `00`) y cada avance se paga con evidencia, no con
entusiasmo.

## Lo construido (fases 0-7 + versiones)

| Fase | Qué se construyó | Estado |
|---|---|---|
| 0-2 | Base: Node.js en Render, datos de mercado BTC/ETH (velas 1h), paper trading con $1.000 simulados | ✅ Hecho |
| 3-4 | Cerebro: pipeline cada 2h — régimen (Haiku 4.5), técnico JS (RSI/MACD/SMA), convicción Druckenmiller (Sonnet 5, JSON 1-10) | ✅ Hecho |
| 5-6 | Riesgo y disciplina: Kelly fraccional techo 1.5%, R:R 1:2, stop 1.5× volatilidad, gates de psicología (límites diarios, cooldown), costos realistas (0.30% redondo) | ✅ Hecho |
| 7 | Memoria y aprendizaje: traderMemory, registro de analyses, meta-análisis | ✅ Hecho |
| v1.1 | Mejoras post-lecciones (auto-ejecución con convicción ≥8, refinamientos de pipeline) | ✅ Hecho |
| v1.2 | Sonnet 5 como motor de convicción + precios Haiku actualizados | ✅ Hecho (⚠️ verificar commit/deploy al día) |

**Desempeño real al 6-jul-2026**: 10 trades (todos ETH, solo LONG), PF 0.89, drawdown 1.84%,
44 días de uptime sin caídas, costo IA ~$5/mes. Infraestructura verde; edge aún no demostrado.

## La fase actual: acumular muestra (jul → 22-ago-2026)

No es una fase de construir: es de **dejar correr y observar**. Tareas de Luis: revisión semanal
del journal (`15`), investigar el bug del trade con convicción 0, y decidir si el filtro
anti-extensión entra como pivote formal (`195`). Prohibido: tocar dos cosas a la vez.

## El hito: evaluación 22-ago-2026

Contrato pre-registrado (detalle en `08`): PF >1.3, DD <15%, ≥30 trades, ≥3 meses de paper.
Tres veredictos posibles: **GO** (fase 8 completa + live chico), **PIVOT** (un cambio grande,
4-6 semanas más de paper), **KILL** (solo tras 2 pivotes fallidos con 50+ trades).

## Fase 8: puente a dinero real (si hay GO)

Resumen (detalle ejecutable en `191`): testnet de Binance, órdenes OCO en el exchange, migrar a
Render Frankfurt (Binance geo-bloquea trading desde IPs de EE.UU.), kill switch, límite de
pérdida diaria 3%, y primer mes **híbrido** (el bot propone, Luis confirma cada trade).
Capital inicial real: $200-500.

## Post-live: el horizonte (solo con evidencia)

En orden, cada uno con su módulo y su propia vara de evidencia:

1. **Escalar capital** — tras 3 meses live rentable, escalado geométrico prudente (`192`).
2. **SHORT** — duplica los regímenes operables; exige broker/watcher/prompts nuevos (`194`).
3. **Multi-par / multi-estrategia** — SOL y más, sin romper la atribución (`193`).
4. **Mejora continua de prompts** — A/B con método, siempre medido en paper primero (`195`).

## Cómo aplica al AGENTE TRADING

- Este módulo es el índice narrativo del proyecto: si algo de aquí cambia (fecha, veredicto,
  fase), actualizarlo el mismo día con fecha (protocolo en `199`).
- La tentación permanente será adelantar fases ("ya casi, metámosle plata"). La respuesta vive
  en `08` y `17`: la evidencia manda, no el calendario ni las ganas.
- Decisiones de capital y de "¿vale la pena seguir?" → `economist_lushows`.
