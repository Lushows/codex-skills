# 210 · CosyVoice2 / Fish-Speech self-hosted (Apache, real-time, multilingüe)

> Los dos motores open de 2026 que combinan **licencia Apache**, **clonación zero-shot** y **latencia real-time**.
> CosyVoice2 es el rey de la baja latencia (~150ms); Fish-Speech lidera ELO multilingüe. Ambos comerciales OK.

## Por qué estos dos juntos
Resuelven el dilema de [[207-f5-tts-serving]] y [[209-xtts-coqui-serving]]: **calidad alta + clonación SIN licencia non-commercial**. Son la elección por defecto para producción comercial cuando necesitas clonar o real-time. Para BIO-SETA: si quieres voz clonada legal, empieza aquí.

## Comparativa
| Atributo | **CosyVoice2-0.5B** | **Fish-Speech 1.5 / OpenAudio** |
|---|---|---|
| Origen | Alibaba FunAudioLLM | FishAudio |
| Params | 0.5B | ~0.5B (mini) |
| Licencia | **Apache-2.0** ✅ | **Apache-2.0** (Fish-Speech 1.x mini) ✅ — verifica la variante exacta |
| Clonación | **SÍ** zero-shot + cross-lingual | **SÍ** zero-shot |
| Idiomas | zh/en/jp/ko/yue + **es cross-lingual** | multilingüe, **1339 ELO** (top arena) |
| Streaming | **~150ms** first-chunk | TTFA ~**100ms**, RTF **0.195** (H200) |
| VRAM | **~8GB** (corre en Jetson-class) | modesta; throughput >3000 tok/s, RTF <0.5 en H200 |

[no verificado: RTF de CosyVoice2 en T4/L4 — los 150ms son del paper en GPU buena; mídelo en tu GPU].

## Serving CosyVoice2 (el de real-time)
Diseñado para **streaming**: LLM causal + quantización → emite chunks mientras genera. Patrón:

```
POST /tts_stream {text, prompt_wav, prompt_text, instruct?} → chunks
  modo zero-shot: prompt_wav (ref) + prompt_text
  modo instruct: 'habla con tono alegre', dialecto, emoción
  carga modelo + flow + hifigan UNA vez (warm)
```

- **3 modos**: zero-shot (clonar), cross-lingual (texto en otro idioma que la ref — sirve para es), e **instruct** (control de emoción/dialecto por texto).
- **TensorRT-LLM ~4×** vs transformers HF para el backbone → la palanca seria de throughput en producción.
- **VRAM ~8GB**: T4/L4 sirve; cabe en edge Jetson para borde.

## Serving Fish-Speech (el de ELO)
- **RTF 0.195 / TTFA ~100ms / >3000 tok/s** (medido en H200) → muy rápido, calidad tope en arenas.
- **OpenAudio S1** es la evolución; **verifica la licencia de la variante exacta** (no todas son Apache). El **mini de Fish-Speech 1.x sí es Apache** — ese es el seguro para comercial.

## Latencia: cuándo cuál
- **Voz en vivo / llamadas** (necesitas <200ms): **CosyVoice2**, el mejor open real-time. Ver [[213-streaming-tts-baja-latencia]].
- **Máxima naturalidad multilingüe** (archivo, no live): Fish-Speech/OpenAudio por ELO.
- **WhatsApp (archivo completo)**: cualquiera; la latencia de streaming no importa, elige por calidad de clon es.

## es-CO
- CosyVoice2 hace **español cross-lingual**; el acento sale del `prompt_wav`. Clona con voz colombiana real.
- Ambos heredan timbre/acento del clip de referencia, no del idioma base.

## Gotchas
1. **Verifica la variante de Fish-Speech/OpenAudio**: 1.x mini = Apache; otras pueden NO serlo. Es el error de licencia oculto aquí.
2. **150ms/100ms son de GPU buena** (paper/H200); en T4/L4 será mayor — mídelo, no lo prometas.
3. **CosyVoice2 carga 3 sub-modelos** (LLM + flow + hifigan); cold-start re-baja todo → Network Volume [[113-network-volume-modelos-grandes]].
4. **TensorRT-LLM** acelera pero complica el build; empieza con HF transformers y optimiza si la latencia aprieta.

Cruza con [[213-streaming-tts-baja-latencia]].
