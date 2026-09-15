# 233 · FSDP2 / DeepSpeed para entrenar difusión y video grande

> Entrenar (o full-finetune) un DiT de video no es servirlo: el optimizer state y las activaciones,
> no solo los pesos, tienen que caber. FSDP2/ZeRO shardean eso. Más a fondo que [[13-multi-gpu-distribuido]].

## Qué consume VRAM al entrenar (y por qué no cabe)
Para un modelo de `P` params en bf16 con Adam: pesos `2P` + grad `2P` + estados optim `~12P` (master fp32
+ m + v) = **~16P bytes** antes de una sola activación. Un DiT de 14B → ~224GB solo de estado. Las
**activaciones** de atención sobre secuencias de video largas (miles de tokens × frames) son el segundo
monstruo y escalan con batch×seq. Por eso DDP (que replica todo) no aplica: hay que **shardear**.

## FSDP2 vs DeepSpeed ZeRO (mapa de decisión)
| | Shardea | Cuándo |
|---|---|---|
| **DDP** | nada (replica) | el modelo + optim + activaciones CABEN en 1 GPU. Más rápido si cabe. |
| **FSDP2 `full_shard`** | params+grad+optim entre todos los ranks (≈ZeRO-3) | no cabe; nativo PyTorch, API por capa `fully_shard(block)` |
| **FSDP2 `HSDP`** (hybrid) | shard intra-nodo, replica inter-nodo | el BW inter-nodo es el cuello; reduce comm cruzando nodos |
| **DeepSpeed ZeRO-1/2/3** | optim / +grad / +params | ecosistema HF/Accelerate, offload CPU/NVMe maduro |
| **ZeRO-Infinity** | + offload a NVMe | entrenas modelos >> VRAM total pagando latencia de disco |

Regla práctica: si ya vives en PyTorch puro y quieres control por capa → **FSDP2**. Si usas `accelerate`
y quieres offload CPU/NVMe llave en mano → **DeepSpeed**. No mezcles ambos sobre el mismo modelo.

## Las palancas que de verdad bajan VRAM
1. **Activation/gradient checkpointing**: recomputa activaciones en el backward en vez de guardarlas.
   Cambia ~30% de cómputo por un recorte enorme de memoria de activaciones — casi obligatorio en video.
2. **`reshard_after_forward=True`** (FSDP2): re-shardea tras el forward; baja el pico de memoria de params.
   En 8×H100 deja params+grad combinados en ~35GB/GPU [no verificado: depende del modelo].
3. **CPU/NVMe offload**: `CPUOffload(offload_params=True)` (FSDP) o ZeRO offload. Velocidad por VRAM.
   Útil para que "quepa" en GPUs chicas; mata throughput si el bus PCIe es el cuello.
4. **Shardear los encoders congelados** (text encoder T5, VAE): ZeRO-3 sobre módulos frozen libera 20GB+
   sin tocar el step. No necesitan grad → puro ahorro de footprint.

## Mixed precision: el gotcha que cuelga el entrenamiento
- **bf16** es el default sano en Ampere+: mismo rango que fp32 → normalmente **sin loss scaling** (a
  diferencia de fp16, que sí necesita `GradScaler`).
- **Master weights fp32**: mantén una copia fp32 de los pesos para el update del optimizer aunque compute en bf16.
- **Trampa real (Wan2.2)**: gradient checkpointing + FSDP2 `MixedPrecisionPolicy(bf16)` → `CheckpointError`
  por **mismatch de dtype**: el recompute en el backward corre fuera del autocast bf16 externo y los tensores
  reentran en fp32. Solución: que el bloque recomputado quede dentro del mismo autocast / castea explícito
  los inputs del checkpoint, o usa `use_reentrant=False` y verifica el dtype en la frontera del bloque.

## Receta base (full-finetune DiT de video)
```
estrategia   = FSDP2 full_shard (o HSDP si multi-nodo con red lenta)
precision    = bf16, master weights fp32, sin loss scaling
checkpointing= activation checkpointing en cada transformer block
encoders     = T5 + VAE congelados, shardeados (ZeRO-3 / fully_shard), sin grad
batch        = micro-batch 1 + gradient accumulation; seq partido si no cabe (→ [[234-context-sequence-parallel-video]])
guardado     = checkpoint shardeado (DCP / zero_to_fp32) — NO juntes a fp32 en cada save
```

## Gotchas que muerden
1. Guardar el checkpoint **consolidado** en cada step revienta CPU/RAM en modelos grandes → guarda shardeado y consolida al final.
2. `full_shard` sobre links inter-nodo lentos = comm-bound → pasa a **HSDP**.
3. Offload a CPU "para que quepa" puede dejar la GPU al 20% esperando el bus; mide antes de celebrarlo.
4. Mezclar el wrapper de DeepSpeed y el de FSDP en el mismo `accelerate` config = caos silencioso.
5. Olvidar checkpointing en video → OOM no en los pesos sino en las **activaciones** del primer batch.

Cruza con [[237-dreambooth-fullfinetune-diffusion]] y [[13-multi-gpu-distribuido]].
