# 08 — Criterios go-live (el contrato paper→live)

> Umbrales definidos ANTES de ver resultados (spec 21-may-2026). **No se negocian, no se mueve
> la portería.** Método de `economist_lushows` módulo 36 (go/no-go).

## La tabla de decisión (fecha de evaluación: 22-ago-2026)

| # | Criterio | Umbral GO | Estado 6-jul-2026 |
|---|---|---|---|
| 1 | Tiempo en paper continuo | ≥ 3 meses (desde 22-may) | ⏳ ~6.5 semanas — cumple 22-ago |
| 2 | Profit factor | > 1.3 | 🔴 **0.89** (necesita mejorar) |
| 3 | Drawdown máximo | < 15% | 🟢 **1.84%** (excelente) |
| 4 | Trades cerrados (muestra) | ≥ 30 | 🔴 **10** (ritmo insuficiente) |
| 5 | Costo API mensual | ≤ $15 | 🟢 ~$5.2/mes ($7.70 en 44 días) |
| 6 | Uptime / robustez | >24h sin caídas | 🟢 44 días seguidos, 0 errores/24h |

**Veredicto parcial: la INFRAESTRUCTURA está lista (3/3 verdes); la ESTRATEGIA no todavía
(PF bajo, muestra corta).** Eso es normal a mitad de período — pero prohibido ignorarlo el 22-ago.

## Los 3 veredictos posibles el 22-ago

- **GO**: 4 criterios de desempeño en verde → Fase 8 live con $200-500, primer mes híbrido.
- **PIVOT**: infraestructura sana pero PF < 1.3 → se cambia UNA variable grande de estrategia
  (ej. filtro anti-extensión, SHORT, threshold), se corren 4-6 semanas más de paper, se re-evalúa.
  NO es fracaso: es el sistema aprendiendo barato.
- **KILL**: solo si tras 2 pivotes el edge no aparece (PF persistente <1.0 con 50+ trades).
  El activo (infraestructura + skill) sobrevive para otra estrategia.

## Condiciones adicionales para el GO (aunque la tabla esté verde)

1. Fase 8 técnica construida y probada ≥2 semanas en **testnet** sin incidentes (`09`).
2. Rieles de seguridad activos: OCO en exchange, kill switch, límite pérdida diaria, alertas.
3. Primer mes live en modo **híbrido**: el bot propone, Luis confirma. Auto-ejecución real solo
   después de 1 mes híbrido limpio.
4. Capital inicial $200-500 (regla de la quiebra). Escalar solo tras 3 meses live rentable.

## Anti-trampas

- Si el 22-ago faltan trades para la muestra, NO se baja el umbral: se extiende el plazo.
- Ganar mucho en paper la última semana no adelanta la fecha. Una semana buena no es evidencia.
- Si Luis siente urgencia de "ya meter plata", releer `05` y `07`: el costo de esperar 6 semanas
  es ~$0; el costo de entrar sin edge es el capital.

## REVISIÓN 6-jul-2026: modo estudio acelerado (decisión del dueño)

Luis activó el modo estudio: 3 pares (BTC/ETH/SOL), análisis cada 1h, threshold 7, hasta 3
posiciones. Efecto esperado: ritmo de trades ×4-6 (de ~1.5/semana a ~6-10/semana).

**Lo que cambia:** la fecha. Con muestra acelerada, los 30 trades con las reglas v1.3+
llegarían a **fin de julio / principios de agosto** — la evaluación se hace cuando n≥30, no
por calendario.
**Lo que NO cambia:** los umbrales de evidencia (PF > 1.3, DD < 15%, ≥30 trades) y todas las
condiciones técnicas (testnet ≥2 semanas, rieles, híbrido primero). La portería de CALIDAD
no se movió — solo llega más rápido el partido.
**Trade-off asumido y documentado:** menos diversidad de regímenes en la muestra (6 semanas
aceleradas ven menos "climas" de mercado que 3 meses lentos). Mitigación: el primer mes live
es híbrido y con $200-500, que es en sí mismo otra capa de validación.
**Bonus de calibración:** con threshold 7, la calibración v1.4 medirá por separado si los 8
superan a los 7 — dato imposible de obtener antes.
