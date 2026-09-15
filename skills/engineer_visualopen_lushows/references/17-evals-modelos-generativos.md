# 17 — Evals de modelos generativos (imagen/video)

No se shippea un modelo generativo por vibes. Métricas automáticas para detección de regresión barata, PERO la
**preferencia humana es el ground truth**.

## Métricas automáticas — qué miden y cómo mienten
- **FID** (Fréchet Inception Distance): distancia entre distribuciones de features Inception real vs generado;
  proxy de calidad+diversidad, menor mejor. *Falla:* sensible al nº de samples y al resize/JPEG → usa **`clean-fid`**
  (evita el bug clásico de resize) y N fijo (≥10k).
- **FVD:** extensión de FID a video (backbone I3D); coherencia temporal, menor mejor. *Falla:* backbone/preproceso distintos → números absolutos incomparables entre papers.
- **CLIPScore:** similitud coseno embeddings CLIP imagen/texto; adherencia al prompt. *Falla:* satura, ciego a errores composicionales ("cubo rojo sobre esfera azul"), premia presencia de keywords.
- **Aesthetic / HPSv2(.1) / ImageReward / PickScore:** reward models entrenados en preferencia humana. *Falla:* heredan sesgos del training, se pueden gamear, derivan en estilos OOD.
- **Lip-sync (avatares): LSE-C / LSE-D** de **SyncNet**. LSE-D = distancia audio↔labio, *menor* mejor (Wav2Lip ~6-8); LSE-C = confidence, *mayor* mejor. *Falla:* SyncNet no es shift-invariant → crops/traslaciones de cara mueven el score; mantén la alineación constante.

## Por qué humano/Elo sigue siendo el rey
Todo lo anterior son proxies; correlacionan imperfecto con lo que el usuario prefiere. Corre **paneles de
preferencia A/B** (dos outputs, mismo prompt+seed) y computa **Elo / Bradley-Terry**. Las automáticas atrapan
*regresiones* barato; los humanos deciden *releases*.

## Golden eval set
Congela un set representativo de **prompts + seeds fijos** (+ audio de referencia para avatares). Córrelo en cada
candidato → resultados comparables. Versiónalo en Git; nunca lo edites en silencio (invalida la historia).
```python
from cleanfid import fid                                  # pip install clean-fid torch-fidelity
score = fid.compute_fid("out/v_new", "data/golden_real")
assert score <= BASELINE_FID * 1.05, f"FID regresó: {score}"
```

## LLM-as-judge para adherencia al prompt
Mete imagen+prompt a un VLM con rúbrica ("¿contiene X, Y en relación Z?") → score estructurado. Más barato que
humanos, atrapa misses composicionales que CLIPScore ignora. *Cuidado:* los jueces sesgan a verbosidad/su familia — calibra contra un subset humano.

## Eval-as-a-CI-gate
Enlaza el golden-set al pipeline (ref 16): el job renderiza el set, computa FID/CLIPScore/HPSv2/LSE-D, compara
con el champion, y **bloquea merge/deploy en regresión**. Renderiza un grid HTML/PDF para el reviewer.

## Gotchas
1. FID entre librerías/resize distintos = sin sentido — estandariza en `clean-fid`.
2. Pocas muestras → FID/FVD ruidoso; fija N y seeds.
3. Los reward models saturan — un +0.01 HPSv2 puede ser ruido; trackea varianza.
4. Las métricas LSE rompen si cambia el crop/alineación de cara entre runs.
5. No optimices directo contra UNA métrica automática — la overfitteas y degradas calidad real (Goodhart).

**Fuentes:** github.com/GaParmar/clean-fid · github.com/toshas/torch-fidelity · arxiv.org/pdf/2008.10010 (LSE-C/LSE-D).
