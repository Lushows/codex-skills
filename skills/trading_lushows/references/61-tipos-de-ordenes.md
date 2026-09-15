# 61 — Tipos de órdenes

Una **orden** es la instrucción que le das al exchange. Elegir mal el tipo de orden es una
forma silenciosa de perder plata aunque el análisis sea correcto.

## El catálogo

| Orden | Qué hace | Costo/riesgo típico |
|---|---|---|
| **Market** | Compra/vende YA al mejor precio disponible | Ejecución garantizada; precio NO garantizado (pagas spread + slippage) |
| **Limit** | Solo ejecuta a tu precio o mejor | Precio garantizado; ejecución NO garantizada (el mercado puede irse sin ti) |
| **Stop-market** | Cuando el precio toca X, dispara una market | El stop-loss clásico; ejecuta seguro, pero en pánico puede llenar lejos de X |
| **Stop-limit** | Cuando toca X, pone una limit a precio Y | Peligro: en una caída violenta la limit puede NO ejecutar y te quedas sin stop |
| **OCO** | Stop + target atados: si uno ejecuta, el otro se cancela | La pareja completa de salida en una sola orden (ver `66`) |
| **Post-only** | Limit que se cancela si fuera a ejecutar de inmediato | Garantiza pagar comisión de maker (más barata) |
| **IOC** | Ejecuta lo que pueda ya, cancela el resto | Para no dejar órdenes colgadas |
| **FOK** | Todo de inmediato o nada | Para tamaños que no admiten llenado parcial |

Dos términos que salen de aquí: **maker** (tu orden queda esperando en el libro y "hace"
liquidez → comisión menor) y **taker** (tu orden ejecuta contra el libro y "toma" liquidez
→ comisión mayor). Market siempre es taker; limit puede ser maker.

## La trampa del stop-limit

Merece párrafo propio porque suena más "fino" y es más peligroso: si BTC cae con violencia
y atraviesa tu precio límite sin llenarte, **te quedas dentro de la posición sin protección**,
viendo la caída. Para stops de protección, la regla general es **stop-MARKET**: ejecutar
seguro importa más que ejecutar bonito.

## Qué usa y usará el bot

- **Paper (hoy)**: simula entradas tipo market con el modelo de slippage de 5 bps por lado;
  stop y target los vigila el propio bot ("watcher" por software).
- **Fase 8 (live)**:
  - Entrada: **market** en pares BTC/ETH (spread mínimo; la simplicidad vale más que los
    ~bps que ahorraría una limit que además puede no llenarse). Mejorable a limit agresiva
    más adelante (`69`).
  - Salida: **OCO obligatoria** — stop-market + target limit viviendo EN el exchange, no en
    el proceso de Render. Si el servidor se cae, la protección sigue viva (`66`).

## Cómo aplica al AGENTE TRADING

La filosofía de órdenes del bot en una línea: **entradas simples, salidas blindadas**. El
edge del sistema está en el régimen y la gestión de riesgo, no en rascar basis points de
ejecución; pero un stop que no ejecuta puede borrar semanas de trabajo — ahí no se escatima.
