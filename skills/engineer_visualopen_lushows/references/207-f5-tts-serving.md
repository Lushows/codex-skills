# 207 · F5-TTS self-hosted (serving del mejor clon zero-shot open)

> F5-TTS clona una voz con 5-15s de referencia y rinde casi como API premium.
> El problema NO es la calidad: es la **licencia CC-BY-NC** y el cold-start del modelo de flow-matching.

## Qué es y por qué importa
F5-TTS (SWivid / Shanghai AI Lab) es un TTS por **flow-matching sobre un DiT** (no autoregresivo). Eso da dos cosas que importan al servir: el **time-to-first-audio es estable** sin importar el largo del texto (no acumula latencia como los AR), y la calidad de clonación zero-shot es de las mejores open de 2026. Base entrenada en **inglés y chino**; el español sale del **clip de referencia** o de finetunes comunitarios (no hay base es oficial). [no verificado: calidad es-CO de finetunes — probar con tu propio clip].

## Licencia — el muro real
| Variante | Licencia | Comercial |
|---|---|---|
| Pesos oficiales `SWivid/F5-TTS` | **CC-BY-NC-4.0** | ⛔ NO sin acuerdo |
| Finetunes/forks MIT-relicenciados | MIT (verificar caso a caso) | ✅ si el autor tiene derecho |

Regla: para BIO-SETA (comercial) **F5-TTS oficial está vetado**. Úsalo solo para prototipar calidad; en producción salta a **Chatterbox (MIT)** o **CosyVoice2 (Apache)** — ver [[211-chatterbox-serving]] y [[210-cosyvoice-fish-speech-serving]].

## Serving: cómo exponerlo
F5 trae un **Gradio** con endpoint REST-ish, pero para producción envuelve el path de inferencia CLI en **FastAPI** y maneja tú la cola. Patrón mínimo:

```
POST /tts {text, ref_audio_path, ref_text} → wav bytes
  carga modelo UNA vez al arranque (warm state global)
  ref_audio: 5-15s limpio, 16-24kHz, una sola voz
```

- **Warm state**: carga el checkpoint + vocoder (Vocos) en `startup`, NO por request — el cold de cargar a VRAM es lo caro, no la inferencia.
- **VRAM**: ~0.3B params → cabe holgado en **6-8GB**. Una T4/L4/RTX 3060 sobra. [no verificado: pico exacto VRAM — medir con tu batch].
- **Cold-start serverless**: el checkpoint + Vocos se re-baja en cada worker frío. Mónta los pesos en **Network Volume** y apunta `HF_HOME` ahí → ver [[113-network-volume-modelos-grandes]].

## Latencia / throughput
- Flow-matching = **N pasos NFE** (típico 16-32). Menos pasos = más rápido, menos fidelidad. Es tu palanca principal de latencia.
- No es streaming nativo de baja latencia conversacional; genera el clip **entero**. Para WhatsApp da igual (mensaje de voz = archivo completo). Para voz en vivo prefiere CosyVoice2 (~150ms) → [[210-cosyvoice-fish-speech-serving]].
- [no verificado: RTF concreto en T4/L4 — mídelo; depende fuerte de NFE y largo del texto].

## Calidad de clon es-CO
- El **acento sale del clip de referencia**, no del idioma base. Para colombiano: graba 10-15s de una voz real es-CO, limpia (sin música/ruido, separa con UVR si hace falta), normaliza loudness.
- Ref sucia = clon sucio: es el error #1. Filtra ruido ANTES.
- F5 hereda la **emoción del tono del clip**: graba la ref con la energía que quieres, no hay slider de emoción (a diferencia de Chatterbox).

## Gotchas
1. **CC-BY-NC mata el uso comercial** del modelo oficial. No lo despliegues para BIO-SETA "porque suena mejor" — es el error legal #1.
2. **Vocoder aparte**: F5 usa **Vocos**; si no cargas el vocoder bien, sale ruido. Verifica que el caché lo baje.
3. **NFE bajo + texto largo** degrada al final de la frase; sube NFE o trocea el texto.
4. **Cold-start re-baja pesos** en serverless → Network Volume obligatorio para economía.

Cruza con [[05-tts-voice-cloning-2026]] y [[116-voice-clone-produccion-retencion]].
