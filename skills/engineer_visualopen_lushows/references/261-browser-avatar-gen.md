# 261 · Avatar parlante en el navegador (privacidad, latencia, límites reales)

> El sueño: un avatar que habla y hace lip-sync 100% en el tab del cliente, sin RunPod, sin que la voz salga.
> La realidad 2026: el **avatar 3D rigged** sí corre en browser; el **video generativo de cara** (LongCat, etc.) NO.

## La división que define todo
| Enfoque | Qué es | ¿En browser hoy? |
|---|---|---|
| **Avatar 3D rigged + visemas** | malla GLB, blendshapes movidos por fonemas | **SÍ**, en producción |
| **2D talking-head generativo** | difusión/flow que genera píxeles de la cara (SadTalker, LongCat) | **NO** en browser — VRAM/tiempo prohibitivos → servidor (ver skill principal) |

Si el cliente pide "avatar en la web sin costo de GPU", la respuesta realista es el **3D rigged**, no generar el video on-device.

## El stack que SÍ funciona (TalkingHead, met4citizen)
Avatar 3D full-body que habla y hace lip-sync en **tiempo real**, todo en el browser, sin APIs ni cuentas:
- **HeadTTS** (voces neuronales Kokoro): TTS en inglés que emite **viseme IDs + timestamps a nivel fonema**, corre entero en browser vía WebGPU.
- **HeadAudio**: lip-sync **audio-driven** en un AudioWorklet — detecta visemas del audio en tiempo real, **sin transcripción ni timestamps**. Ideal para voz en vivo.
- **whisper-web** (ASR) + **WebLLM** (Llama 3.2) → pipeline conversacional completo sin servidor.
- Render: Three.js / WebGL anima los blendshapes de la malla GLB con los visemas. Animaciones de cuerpo vía Mixamo (FBX).

```
audio/texto → (HeadTTS visemas | HeadAudio del audio) → blendshapes GLB → Three.js render
```

## Por qué esto gana en su nicho
- **Privacidad como producto**: voz y texto **nunca salen del tab**. Crítico para salud, legal, datos sensibles.
- **Latencia sin red**: visemas calculados localmente → labios sincronizados sin viaje al servidor.
- **Costo cero de GPU por usuario**: corre en la GPU del cliente (ver [[259-webgpu-transformers-js]]).
- **Escala infinita**: no hay cola de jobs ni endpoint que saturar; cada cliente es su propio worker.

## Límites duros (decir la verdad al cliente)
- **No es fotorrealista**: es un avatar 3D estilizado, no una persona real generada. Para realismo de cara → pipeline servidor (LongCat/SadTalker en RunPod, ver skill principal).
- **TTS limitado en idiomas**: HeadTTS/Kokoro fuerte en inglés; visemas para español pueden requerir mapeo extra o TTS server.
- **WebGPU ~70% soporte**: Safari/iOS y navegadores corporativos pueden caer a WASM (más lento) o no soportar.
- **Descarga inicial**: malla GLB + modelos TTS/ASR son MBs; cachear en OPFS/Cache API o el primer load duele.
- **Térmica/batería móvil**: render 3D + inferencia sostenida calienta y drena; degradar calidad en móvil.

## Árbol de decisión
1. ¿Necesitas **fotorrealismo de cara real**? → servidor GPU (skill principal), no browser.
2. ¿Privacidad/latencia/costo-cero mandan y aceptas avatar 3D? → **TalkingHead en browser**.
3. ¿Conversacional completo offline? → whisper-web + WebLLM + HeadTTS + TalkingHead, todo client-side.
4. ¿Móvil débil / sin WebGPU? → considera servidor o avatar 2D simple pre-renderizado.

Cruza con [[259-webgpu-transformers-js]], [[147-avatar-realtime-streaming-baja-latencia]] y [[73-edge-computing-wasm]].
