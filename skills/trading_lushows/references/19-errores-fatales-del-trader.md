# 19 — Los 10 errores fatales del trader

Estos errores no hacen perder trades: hacen perder CUENTAS. La mayoría de traders minoristas no
quiebra por falta de aciertos sino por cometer 2-3 de esta lista. El AGENTE TRADING existe, en
buena parte, para hacer estos errores estructuralmente imposibles.

## La tabla: error → por qué mata → qué regla del bot lo previene

| # | Error fatal | Por qué mata la cuenta | Regla del bot que lo previene |
|---|---|---|---|
| 1 | **Operar sin stop** | Una sola posición "que ya va a rebotar" puede llevarse 30-100% del capital | Stop obligatorio en cada trade: 1.5× volatilidad, calculado ANTES de entrar |
| 2 | **Promediar a la baja** (comprar más cuando pierdes "para bajar el promedio") | Convierte una pérdida chica en una apuesta gigante contra el mercado | El sizing se calcula UNA vez al entrar; no existe código para agrandar perdedoras |
| 3 | **Apalancarse** (operar con dinero prestado del exchange) | Multiplica pérdidas y permite perder MÁS que el capital | Spot puro, sin apalancamiento, hoy y en fase live inicial |
| 4 | **Mover la portería** (correr el stop "un poquito más" cuando el precio se acerca) | El stop deja de existir en la práctica = error #1 disfrazado | El watcher ejecuta el stop original; nadie "opina" en medio del trade |
| 5 | **Revenge trading** (operar más fuerte tras perder, para "recuperar") | Las peores decisiones se toman en el peor estado emocional | Cooldown de 4h tras 3 pérdidas seguidas (gate de psicología) |
| 6 | **Overtrading** (operar por aburrimiento o adicción a la acción) | Los costos (~0.30% redondo) se comen el edge; más trades ≠ más plata | Máx 5 trades/día + convicción ≥8 (la mayoría de ciclos no operan) |
| 7 | **FOMO** (entrar tarde porque "se va sin mí") | Comprar extendido = comprar donde los ganadores venden | Lección real del bot: 0/3 sobre $1.788 → filtro anti-extensión (pivote candidato) |
| 8 | **Arriesgar mucho por trade** (5-10% "porque estoy seguro") | 10 pérdidas de 10% = −65%; matemática de la ruina (ver `02`) | Techo duro 1.5% que la convicción NUNCA rompe |
| 9 | **Cambiar de sistema cada semana** | Nunca acumula muestra; siempre está en el día 1 | Umbrales pre-registrados (22-ago) + un cambio a la vez (ver `195`) |
| 10 | **No registrar nada** | Sin journal no hay aprendizaje, solo repetición de errores | traderMemory + analyses registran el 100% automáticamente |

**Términos:** *FOMO* = "fear of missing out", miedo a quedarse por fuera. *Apalancamiento* =
operar con más dinero del que tienes, prestado por el exchange.

## La verdad incómoda

Un humano disciplinado también puede evitar estos 10 errores... hasta el día que no. La ventaja
real de un bot no es que analice mejor que un humano — es que **no tiene un mal día**. El código
cumple la regla la vez 1.000 igual que la vez 1. Por eso las reglas viven en código (gates,
techos, cooldowns) y no en "buenas intenciones" ni en el prompt.

## El matiz honesto

El bot previene los errores del TRADER, pero introduce errores de INGENIERÍA: el trade con
convicción 0 fue un bug, no una emoción. La disciplina del sistema es tan buena como su código —
por eso existen la fase testnet, el kill switch y el mes híbrido antes del live (ver `08` y `191`).

## Cómo aplica al AGENTE TRADING

- Usa esta tabla como auditoría trimestral: recorrer los 10 y verificar que la regla preventiva
  sigue VIVA en el código (no solo en la documentación).
- Para la fase live se agregan rieles contra errores nuevos: límite de pérdida diaria 3%,
  OCO en el exchange, kill switch — ver `02` y `191`.
- Decisión de cuánto capital exponer → `economist_lushows`; verificación numérica → `Matematicas_lushows`.
