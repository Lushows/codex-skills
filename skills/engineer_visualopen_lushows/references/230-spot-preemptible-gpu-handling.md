# 230 · GPU Spot / Preemptible (pagar la mitad y sobrevivir a la interrupción)

> Spot es 40-70% más barato que on-demand porque te lo pueden **quitar** en cualquier momento. La
> única forma de aprovecharlo sin perder trabajo: checkpointear seguido y diseñar para reanudar.

## El trato
| | On-demand | Spot / Interruptible |
|---|---|---|
| Precio | full | ~0.23 vs 0.50 $/hr → **40-70% menos** |
| Disponibilidad | garantizada | te la reclaman si entra prioridad mayor |
| Aviso | — | un warning **cuando se puede** (a veces segundos, a veces nada) |
| Uso ideal | online/SLA | batch tolerante a fallo: render, training, encoder |

## Regla de oro
**Asume que el pod muere AHORA mismo, sin aviso.** Todo lo que no esté en almacenamiento persistente al
momento del preempt se pierde. Por eso spot solo sirve para trabajo **idempotente y checkpointeable**,
nunca para el handler online con un cliente esperando (ese va on-demand; ver [[160-disaster-recovery-cascada-fallback]]).

## Patrón de supervivencia
1. **Checkpoint frecuente a volumen persistente** (no a disco efímero del contenedor). Cada N minutos o
   N steps, escribe estado mínimo reanudable. Detalle en [[231-checkpoint-resume-long-jobs]].
2. **Escritura atómica**: escribe a `ckpt.tmp` y `os.rename` → nunca un checkpoint a medias si el preempt
   pega en mitad del write.
3. **Captura la señal de terminación** (SIGTERM en muchos proveedores) → flush de checkpoint en el
   handler antes de morir. Es best-effort: el aviso puede ser cero, por eso (1) es la red real.
4. **Al arrancar, reanuda**: el job nuevo busca el último checkpoint en el volumen y continúa, no empieza
   de cero.
5. **Sube el resultado apenas esté** (a R2/S3): un render terminado pero no subido cuando llega el
   preempt = trabajo perdido.

## Estrategias de orquestación
- **Fallback a on-demand**: si no hay capacidad spot o te preemptean 3 veces seguidas, relanza en
  on-demand. Híbrido = costo bajo con cota de tiempo.
- **Diversificar GPU/región**: pedir spot de varios tipos compatibles sube la probabilidad de conseguir
  y baja la de preempt simultáneo.
- **Cola con reintento idempotente**: el job vuelve a la cola al preempt; el worker que lo tome reanuda
  desde checkpoint. La idempotencia evita doble-cobro/doble-output.

## Capturar el preempt (best-effort)
```python
import signal, sys
def on_term(*_):
    save_checkpoint_atomic(state, volume)   # flush último estado
    sys.exit(0)
signal.signal(signal.SIGTERM, on_term)      # muchos proveedores mandan SIGTERM antes de matar
```
El aviso puede ser de segundos o **inexistente** (preempt duro). Por eso el handler de señal es un
extra, **no** la defensa principal: esa es el checkpoint periódico del paso (1). Nunca dependas de tener
tiempo para guardar al recibir la señal.

## Qué NO poner en spot
- El **endpoint online** con un cliente esperando respuesta: un preempt = request caído. Va on-demand.
- Jobs **no idempotentes** sin checkpoint (efectos secundarios irreversibles a mitad: cobros, envíos).
- Trabajo **más corto que el overhead de relanzar**: el relanzar te cuesta más que correrlo on-demand.

## El cálculo que importa
Spot ahorra dinero pero **alarga el wall-clock** (esperas relanzar tras cada preempt). Si el job es
corto (< intervalo típico de preempt) casi nunca te toca → ahorro casi gratis. Si es largo, el costo del
re-trabajo perdido entre checkpoints debe ser < el ahorro. Checkpoint demasiado raro ⇒ pierdes más de lo
que ahorras; demasiado frecuente ⇒ el I/O te frena. Afina el intervalo al costo de re-hacer ese tramo.

Cruza con [[231-checkpoint-resume-long-jobs]] y [[160-disaster-recovery-cascada-fallback]].
