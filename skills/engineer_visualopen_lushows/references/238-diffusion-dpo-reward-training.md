# 238 · Alinear difusión a preferencia (Diffusion-DPO, reward models, RLHF visual)

> El fine-tune te da TU sujeto. Esto te da TU *gusto*: que el modelo prefiera lo que un humano
> prefiere (composición, anatomía, estética) sin recolectar miles de imágenes nuevas, solo *pares*.

## El problema que resuelve
Un base genera técnicamente correcto pero "feo" o desalineado: manos rotas, composición plana, ignora
matices del prompt. No lo arregla más data del sujeto — lo arregla enseñarle **qué salida es mejor**.
Tres familias, de menos a más complejas:

| Método | Señal | Coste | Estabilidad |
|---|---|---|---|
| **Reward-weighted / ReFL** | reward model puntúa, pesa el loss | medio | media |
| **Diffusion-DPO** | **pares** (ganador/perdedor), sin RM en el loop | bajo-medio | **alta** (el default 2026) |
| **DDPO / RL online** | reward + policy gradient sobre la trayectoria | alto | baja (frágil) |

**Diffusion-DPO** es el caballo de batalla: adapta DPO de LLMs a difusión. No necesitas un reward model
*durante* el training ni rollouts RL — solo un dataset de pares de preferencia (ej. Pick-a-Pic, 1M pares
de la misma caption con un voto humano). Entrenas el modelo a subir la verosimilitud del ganador y bajar
la del perdedor, **anclado a un modelo de referencia congelado** (`ref`) para no derivar.

## Diffusion-DPO: el loss y el β
Por cada par (mismo prompt, imagen ganadora `w` / perdedora `l`), en un timestep `t` ruidoso, comparas el
error de denoising del modelo entrenable vs el `ref` congelado, para ganador y perdedor:
```
L = -log σ( -β·T·( [‖ε_w−ε_θ(w)‖² − ‖ε_w−ε_ref(w)‖²]
                  − [‖ε_l−ε_θ(l)‖² − ‖ε_l−ε_ref(l)‖²] ) )
```
**β = la palanca clave** (temperatura): controla cuánto te alejas del `ref`.
- **SDXL: β ≈ 5000** (el valor del paper original). [verificado]
- **FLUX.1-dev: β ≈ 1000** (DiT rectified-flow, 12B). [verificado]
β bajo → diverge rápido y "fríe" estética; β alto → apenas se mueve. Empieza en el valor de referencia y
barre ×2 / ÷2.

## Hiperparámetros reales (SDXL, paper)
- **Optimizer Adafactor** (ahorra memoria, batch efectivo enorme).
- **Batch efectivo 2048 pares** = 16×A100, local batch 1 par, grad-accum 128. [verificado]
- lr ~1e-8 a 1e-5 según escala (DPO es sensible; lr alto destruye el `ref` anchor).
- Para casero: hazlo **LoRA-DPO** — DPO sobre pesos LoRA, batch chico + grad-accum, cabe en 24-48GB.
  No necesitas el batch de 2048 para un dominio estrecho (tu producto/estilo).

## Variantes 2026 (cuándo importan)
- **SmPO-Diffusion**: preferencias *suaves* vía PickScore en vez de binarias → reduce over-optimization
  (que el modelo explote la métrica y empeore lo demás). [verificado]
- **SDPO (importance-sampled)**: importance sampling + máscara/clip por timestep, concentra el update en
  pasos informativos; probado en FLUX.1-dev. [verificado]
- **Diffusion-NPO**: optimización de preferencia *negativa* — qué NO generar. [verificado, ICLR 2025]

## Reward models y RLHF visual (la otra rama)
Si quieres puntuar generaciones (no solo pares):
- **PickScore / HPSv2 / ImageReward**: RMs caption-aware entrenados en votos humanos. Sirven como *juez*
  (eval, ver [[164-evals-calidad-avatar-video]]) o como señal en **ReFL / reward-weighted fine-tune**.
- **DDPO**: trata el denoising como política RL, optimiza el reward con policy gradient. Potente pero
  **frágil** (reward hacking: genera artefactos que engañan al RM, no mejor calidad real). Necesita KL-penalty
  fuerte y early-stop. Prefiere DPO salvo que tengas un RM impecable y presupuesto de babysitting.

## Gotchas
1. **Over-optimization / reward hacking**: la métrica sube, la calidad real baja. Eval *out-of-distribution*
   con un juez DISTINTO al de training. Cruza con [[164-evals-calidad-avatar-video]].
2. **El `ref` debe ser el MISMO base sin tocar** — si entrenas DPO sobre un base ya fine-tuneado, ese
   fine-tune es tu `ref`, no el original.
3. **Datos de pares > cantidad**: 10k pares limpios y consistentes baten 1M ruidosos con votos contradictorios.
4. **DPO no enseña conceptos nuevos**, solo *reordena preferencia* sobre lo que el base ya sabe. Para sujeto
   nuevo, primero DreamBooth-LoRA (ver [[237-dreambooth-fullfinetune-diffusion]]), luego DPO para pulir.

## Fuentes
- https://arxiv.org/pdf/2311.12908 (Diffusion-DPO original)
- https://arxiv.org/pdf/2505.21893 (SDPO) · https://github.com/G-U-N/Diffusion-NPO

Cruza con [[164-evals-calidad-avatar-video]] y [[07-training-finetuning-a-fondo]].
