# 228 · MIG · Multi-Instance GPU (cortar una A100/H100 en GPUs aisladas)

> Una A100/H100 entera es overkill para un worker de TTS o de imagen 512px. MIG la parte en
> instancias con VRAM y cómputo **dedicados y aislados** por hardware → varios workers chicos en una
> sola tarjeta, sin que uno mate al otro.

## Qué es
MIG particiona físicamente la GPU en hasta **7 instancias** (GPU Instances), cada una con su porción de
SM, su slice de HBM, su caché L2 y su ancho de banda de memoria **dedicados**. No es time-sharing: es
aislamiento de hardware. Un OOM o crash en una instancia **no afecta** a las demás. Disponible en
Ampere (A100/A30) y Hopper (H100/H200).

## Perfiles (la unidad clave)
Las instancias se nombran por `<cómputo>g.<memoria>gb`:
| Perfil A100-40GB | VRAM | Slices de cómputo |
|---|---|---|
| `1g.5gb` | 5GB | 1/7 |
| `2g.10gb` | 10GB | 2/7 |
| `3g.20gb` | 20GB | ~3/7 |
| `7g.40gb` | 40GB | tarjeta entera |

En H100 hay más perfiles (incluye variantes con/sin slice extra de memoria; las fuentes citan desde 7
GPU-instances hasta ~19 combinaciones contando profiles de memoria). [no verificado: número exacto
depende del modelo y versión de driver]. La memoria por slice es fija: **no** puedes pedir 1 SM con
20GB; cómputo y memoria escalan juntos.

## Cuándo usarlo (y cuándo no)
**Sí**: muchos modelos chicos que caben en ≤10GB (TTS, embeddings, clasificadores, SDXL cuantizado),
multi-tenant donde el aislamiento es requisito (un cliente no debe ver latencia/crash de otro), QoS
predecible. **No**: tu modelo necesita la VRAM/banda completa (LongCat-Avatar 44GB, LLM grande) —
partir solo lo estrangula. Tampoco si necesitas que una instancia crezca dinámicamente: el reparticionado
exige drenar la GPU.

## Costuras prácticas
- **Reparticionar = parar todo**: cambiar el layout MIG requiere que **ningún** proceso use la GPU.
  No es elástico en caliente. Decides el corte y vives con él hasta la próxima ventana.
- **No hay comunicación entre instancias** (sin NVLink/P2P entre slices): cada worker es una isla. Modelo
  multi-GPU dentro de MIG no aplica.
- **Cloud serverless**: la mayoría de proveedores no exponen MIG configurable al usuario; lo usan ellos
  para vender fracciones (ver fractional GPU). En tu propio Pod/nodo con driver tienes `nvidia-smi mig`.
- **Habilitar**: `nvidia-smi -mig 1`, luego crear GIs/CIs con `nvidia-smi mig -cgi ... -C`. Kubernetes via
  el device-plugin/MIG-manager de NVIDIA.

## Verificar y monitorear
- `nvidia-smi -L` lista las instancias con su UUID (`MIG-GPU-xxx/...`). Cada worker fija su instancia con
  `CUDA_VISIBLE_DEVICES=MIG-<uuid>` — apuntar por índice numérico no basta con MIG activo.
- `nvidia-smi mig -lgip` muestra los perfiles disponibles y cuántos quedan libres antes de crear.
- En métricas (DCGM), cada GI/CI reporta por separado: puedes ver utilización y memoria **por instancia**,
  no solo de la tarjeta. Útil para detectar un slice infrautilizado que debiste hacer más chico.

## Costo: ¿conviene partir?
La A100/H100 cuesta lo mismo partida o entera — pagas la **tarjeta**, no las instancias. MIG gana cuando
tienes ≥2 cargas chicas que de otro modo ocuparían tarjetas separadas: consolidas 7 modelos `1g.5gb` en
una sola GPU en vez de 7 GPUs. Si solo corres **un** modelo chico, MIG no ahorra (igual pagas la entera) —
ahí lo que quieres es alquilar una GPU más pequeña, no partir una grande.

## MIG vs las alternativas blandas
MIG da aislamiento **duro** (memoria + fallos) a costa de rigidez. Si necesitas compartir más flexible
sin fronteras fijas — o tu GPU no soporta MIG (Ada/RTX, L4, L40S) — bajas a MPS o time-slicing, que
comparten sin aislar la memoria. Combo común: MIG entre slices + time-slicing **dentro** de cada slice.

Cruza con [[131-runpod-a-fondo-serverless-pods-volumes]] y [[158-autoscaling-inferencia-gpu]].
