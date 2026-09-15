# 209 · XTTS-v2 / Coqui self-hosted (clon 17 idiomas, pero NON-COMMERCIAL)

> XTTS-v2 clona con ~6s, hace 17 idiomas (incl. español) y tiene streaming ~200ms.
> Pero la **Coqui Public Model License es non-commercial** y la empresa **cerró** — es legado. Léelo antes de enamorarte.

## Advertencia primero (no la entierres)
- **Licencia: Coqui Public Model License (CPML) → NO comercial** sin acuerdo. Para BIO-SETA está **vetado** igual que F5-TTS.
- **Coqui (la empresa) cerró**: el modelo sigue en HF (`coqui/XTTS-v2`) pero **sin soporte ni parches**. Para un proyecto nuevo prefiere **Chatterbox (MIT)** o **CosyVoice2 (Apache)** → [[211-chatterbox-serving]], [[210-cosyvoice-fish-speech-serving]].
- Documentado aquí porque mucho tutorial viejo lo recomienda; necesitas saber **por qué NO** usarlo en producción comercial.

## Qué ofrece (si fuera usable)
| Atributo | Valor |
|---|---|
| Params | ~0.4B |
| Idiomas | **17, incl. español** |
| Clonación | zero-shot, **~6s** de referencia |
| Streaming | sí, **<200ms** TTFB (chunked) |
| VRAM | **4-6GB** (entry hosting ~8GB, ej. RTX 3060Ti) |
| Licencia | **CPML non-commercial** ⛔ |

## Serving (para uso NO comercial / interno)
XTTS trae **servidor HTTP propio** y soporta **streaming chunked** para bajar el time-to-first-byte. Patrón:

```
POST /tts_stream {text, speaker_wav, language} → chunks de audio
  carga XTTS + speaker embedding UNA vez (warm)
  language: 'es' para español
  speaker_wav: ~6s limpio de la voz a clonar
```

- **Warm state**: el cómputo del **speaker latent** desde el `speaker_wav` se puede cachear por voz → no lo recalcules en cada request (es lo que mata latencia si lo repites).
- **VRAM 4-6GB**: T4/L4/3060 sobra. La gracia es el streaming, no el tamaño.
- **Cold-start serverless**: pesos en **Network Volume** [[113-network-volume-modelos-grandes]].

## Latencia / streaming
- **<200ms TTFB** en modo streaming chunked — de lo mejor que tuvo el open antes de CosyVoice2.
- Hoy **CosyVoice2 (~150ms, Apache)** lo supera en latencia Y licencia → para real-time nuevo, ve allá.

## es-CO
- 17 idiomas con **español** de base; el acento fino sale del `speaker_wav`. Clona con audio es-CO real para acento colombiano (mismo principio que F5/Chatterbox).

## Gotchas
1. **NON-COMMERCIAL**: el error #1. No lo despliegues para una tienda. Es legado.
2. **Sin mantenimiento** (Coqui cerró): dependencias y bugs no se arreglan upstream; te quedas con forks comunitarios.
3. **No recachear el speaker latent** por request destroza la latencia; cachéalo por voz.
4. **Para producción comercial nueva, simplemente no lo elijas** — Chatterbox/CosyVoice2 cubren lo mismo con licencia limpia y soporte vivo.

Cruza con [[05-tts-voice-cloning-2026]].
