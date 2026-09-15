# 255 · TCO self-host vs API premium (punto de equilibrio por volumen)

> "Self-host es más barato" es falso por debajo de tu break-even — y el break-even está más alto de lo que crees.
> El TCO real corre 3-5× sobre la renta de GPU. La GPU al 10% de carga cuesta 10× más por unidad.

## El modelo de costo completo (no solo la GPU)
```
TCO_selfhost = renta_GPU/util + DevOps + ciclos_update + storage + egress + warm_pool_idle
costo_por_unidad_real = TCO_selfhost / unidades_servidas
```
La **utilización** es la palanca dominante: una GPU al 10% de carga infla el costo/1k tokens de ~$0.013 a ~$0.13 — más caro que la API premium. Self-host solo gana con utilización **sostenida alta** (>50%).

## Break-even por tipo de API (2026, verificar)
| Comparas contra | Break-even aprox. | Lectura |
|---|---|---|
| API premium (GPT-4o, Claude Sonnet) | ~5-10M tokens/mes | self-host gana antes |
| Frontier cerrado en GPU reservada | ~2-5M tokens/día | medio |
| API de modelo abierto (Together, DeepSeek) | ~50-100M tokens/mes | self-host gana muy tarde |

[no verificado — los umbrales bailan con precios de API y renta GPU]. Regla mental: **contra premium, self-host conviene pronto; contra API barata de modelo abierto, casi nunca**. Ejemplo citado: 500M tok/día Llama-70B self-host ≈ $4.4k/mes vs ~$22.5k/mes API → 5× a favor, pero solo a ese volumen y utilización.

## Los costos ocultos que mueven el break-even
- **DevOps**: ~$145k/año o 10-20 h/mes de ingeniería en monitoreo, on-call, troubleshooting. En proyecto pequeño esto solo ya supera la renta GPU.
- **Ciclos de update de modelo**: ~$12k en tiempo de ingeniería por actualización (re-eval, re-deploy, regresión).
- **Warm-pool idle**: pagas la GPU caliente 24/7 para matar cold-starts ([[30-finops-gpu]]) aunque no haya tráfico.
- **Storage + egress**: pesos en volumen (GB-mes), outputs servidos (GB egress).

## Para IA visual (avatar/video), el cálculo cambia
La unidad no es token sino **$/render** o **$/minuto-avatar**, y el cold-start (cargar 44GB a VRAM) es enorme. Con volumen bajo y esporádico, la API premium (fal/Replicate por-predicción) casi siempre gana: no pagas idle ni DevOps. Self-host de video se justifica con **cola densa y constante**, no con picos. El serverless GPU (RunPod) es el punto medio: por-segundo sin gestionar k8s, pero pagas cold-start por job.

## Marco de decisión
1. **Mide volumen real** (no proyectado) y **utilización alcanzable** con tu patrón de tráfico.
2. **Calcula costo/unidad** en ambos lados con TCO completo, no renta pelada.
3. **Considera no-costo**: latencia, privacidad de datos, control de modelo, dependencia de provider.
4. **Híbrido**: baseline self-host + overflow/fallback a API premium ([[160-disaster-recovery-cascada-fallback]]) — capa el costo y cubre outages.
5. **Re-evalúa trimestral**: precios de API y GPU caen rápido; el break-even de hoy no es el de en 6 meses.

## Gotchas
1. Comparar renta GPU pelada vs precio API ignora DevOps+idle → subestima self-host 3-5×.
2. Asumir 100% utilización; el patrón real (picos + valles) deja la GPU al 10-30% → costo/unidad se dispara.
3. Olvidar el costo de cambiar de modelo: API actualiza solo; self-host re-eval + re-deploy cada release.
4. Self-hostear por "ahorro" a volumen bajo: por debajo del break-even, la API es más barata Y menos trabajo.

**Fuentes:** braincuber.com/blog/self-hosted-llms-vs-api-based-llms · devtk.ai/en/blog/self-hosting-llm-vs-api-cost-2026 · sitepoint.com/local-llms-vs-cloud-api-cost-analysis-2026 · tokenmix.ai/blog/self-host-llm-vs-api.

Cruza con [[30-finops-gpu]], [[160-disaster-recovery-cascada-fallback]] y [[253-spot-reserved-arbitrage-gpu]].
