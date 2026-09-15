# 197 — Cuándo apagar el sistema

Saber apagar es parte del sistema, no su fracaso. Los criterios de apagado se escriben HOY,
en frío, porque el día que haga falta usarlos habrá dos voces malas susurrando: "dale una
oportunidad más" (esperanza) o "apágalo todo YA" (pánico). Ninguna de las dos decide bien.

## Los 4 gatillos de apagado

| Gatillo | Umbral | Tipo de apagado |
|---|---|---|
| **1. Drawdown** | DD ≥ 15% del pico de equity (el mismo umbral del go-live, `08`) | Inmediato: no abrir posiciones nuevas; cerrar las abiertas en sus stops/targets |
| **2. Degradación del edge** | PF < 1.0 sostenido durante un trimestre completo CON muestra (≥20 trades en el período) — no una mala racha (`17`) | Ordenado: pausa de entradas + diagnóstico antes de decidir pivot o kill |
| **3. Cambio de régimen estructural** | El mercado cambió de forma DURADERA, no cíclica: regulación que bloquea el acceso (geo-bloqueos, prohibiciones), colapso del exchange, o volatilidad crónica fuera del rango donde el sistema fue diseñado (verificar al día) | Ordenado, sin esperar a que las métricas lo confirmen perdiendo plata |
| **4. Costo > beneficio** | (Ganancia esperada mensual) < (costo IA + Render + horas de Luis valoradas honestamente) durante 2+ trimestres | Estratégico: decisión de negocio → `economist_lushows` |

Diferencia clave entre el 1-2 y el 3: los primeros los detectan las MÉTRICAS; el tercero lo
detecta el JUICIO (las métricas llegarían tarde). Por eso la revisión semanal (`15`) incluye
mirar el mundo, no solo el journal.

## El protocolo de apagado ordenado (no se desenchufa y ya)

1. **Congelar entradas** — el bot deja de abrir posiciones (flag en código, no matar el proceso).
2. **Resolver posiciones abiertas** — dejarlas llegar a su stop/target normal (el plan del trade
   se respeta hasta el final) salvo gatillo 3, donde se cierran a mercado.
3. **Snapshot completo** — respaldar traderMemory, analyses, equity curve y configuración. La
   historia es el activo más valioso del proyecto; se apaga el bot, no el aprendizaje.
4. **Autopsia escrita** — qué gatillo disparó, qué dicen los datos, qué se haría distinto.
   Se guarda en esta skill con fecha (`199`).
5. **Retirar el capital** (si es live) a la cuenta de Luis. Plata quieta ≠ plata en riesgo.
6. **Decidir el futuro en frío, semanas después**: pivot (nueva estrategia sobre la misma
   infraestructura), pausa larga, o cierre definitivo.

## Lo que NO es apagar

- **Apagar ≠ perder todo lo construido.** La infraestructura (pipeline, gates, memoria, fase 8)
  y el conocimiento (esta skill) sobreviven a cualquier estrategia muerta. Ya lo dice el `08`:
  el activo sobrevive para otra estrategia.
- **Apagar ≠ vender en pánico.** El apagado es un procedimiento, con pasos, ejecutado con la
  misma disciplina que una entrada.
- **Pausar el kill switch diario (−3% en un día, `191`) NO es este módulo**: eso es un freno
  automático de un día. Este módulo es la decisión estructural.

## Cómo aplica al AGENTE TRADING

- Hoy (paper, DD 1.84%) ningún gatillo está cerca. El momento de acordar estos umbrales es
  exactamente ahora, cuando no duelen.
- El gatillo 2 ya tiene su versión pre-live en el `08`: KILL solo tras 2 pivotes y PF <1.0 con
  50+ trades. Este módulo lo extiende a la vida post-live.
- El gatillo 4 es el más fácil de ignorar porque nada "explota": el sistema puede ser
  técnicamente exitoso y económicamente irrelevante. Revisión honesta trimestral con
  `economist_lushows`; los números del costo total → `Matematicas_lushows`.
