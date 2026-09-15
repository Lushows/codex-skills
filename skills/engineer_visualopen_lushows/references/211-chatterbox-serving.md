# 211 · Chatterbox self-hosted (MIT, clon desde 10s, control de emoción)

> El clon zero-shot **MIT** (comercial sin asteriscos) con un slider de emoción que ningún otro open tiene.
> Para BIO-SETA es la **elección por defecto** cuando necesitas clonar una voz legalmente. Watermark Perth incluido.

## Por qué es el default comercial
Cierra el dilema "los mejores clones son non-commercial": F5 (CC-BY-NC) y XTTS (Coqui CPML) están vetados → ver [[207-f5-tts-serving]], [[209-xtts-coqui-serving]]. **Chatterbox es MIT**: úsalo en producto comercial, modifícalo, redistribúyelo sin restricción. Hecho por Resemble AI (equipo de 3). En arenas 2026 supera a ElevenLabs en preferencia ciega [no verificado: % exacto — citado ~65% en una fuente].

## Las dos variantes
| Variante | Lanzada | Idiomas | Licencia |
|---|---|---|---|
| **Chatterbox** (EN) | may-2025 | inglés nativo | **MIT** ✅ |
| **Chatterbox Multilingual** | sep-2025 | **23 idiomas incl. español** | **MIT** ✅ |

23 idiomas: ar, da, de, el, **en, es**, fi, fr, he, hi, it, ja, ko, ms, nl, no, pl, pt, ru, sv, sw, tr, zh. El **español está out-of-the-box**.

## Lo que lo distingue: emoción explícita
- **`exaggeration`**: intensidad emocional, de monótono a dramático. **Único open con control de exageración explícito** — no dependes solo del tono del clip.
- **`cfg_weight`**: ritmo/pacing.
- Esto importa para marketing/marca: ajustas energía sin re-grabar la referencia.

## Serving
Hay servidor comunitario maduro (`devnen/Chatterbox-TTS-Server`): **Web UI, API OpenAI-compatible**, voces predefinidas, clonación, corre en **CUDA / ROCm / CPU**. Patrón propio:

```
POST /tts {text, audio_prompt_path?, exaggeration, cfg_weight, language} → wav
  audio_prompt_path: ~10s limpio de la voz a clonar (zero-shot, sin reentrenar)
  carga modelo UNA vez (warm)
```

- **VRAM**: ~6GB (orden 0.5B). T4/L4/RTX 3060 sobra. [no verificado: pico exacto VRAM en multilingual — medir].
- **Clonación zero-shot sin reentrenar**: clip corto captura el timbre; nada de finetune.
- **API OpenAI-compatible**: si tu app ya habla con la API de OpenAI TTS, el drop-in es casi gratis.
- **Cold-start serverless**: pesos en Network Volume [[113-network-volume-modelos-grandes]].

## Latencia
- Genera el clip **completo** (no es el campeón de streaming conversacional; para <150ms live usa CosyVoice2 [[210-cosyvoice-fish-speech-serving]]).
- Para **WhatsApp (nota de voz = archivo)** es ideal: calidad alta, licencia limpia, control de emoción.
- [no verificado: RTF en T4/L4 — mídelo].

## es-CO
- Español out-of-the-box, pero el **acento fino sale del clip** de referencia. Para colombiano: clona con 10s de voz es-CO real, limpia y normalizada.
- Combina con `exaggeration` para dar energía sin alterar el acento.

## Gotchas
1. **Watermark Perth** en TODO audio generado (inaudible, extraíble con su detector open). No es bug; tenlo presente si te preocupa la trazabilidad.
2. **Genera clip completo**, no streaming de baja latencia → no lo metas en llamada en vivo esperando 150ms.
3. **`exaggeration` alto** puede sonar caricaturesco; calíbralo con `cfg_weight`, no lo subas a ciegas.
4. **Ref sucia = clon sucio** (regla universal): limpia el clip antes (UVR, normaliza loudness).

Cruza con [[05-tts-voice-cloning-2026]].
