# 116 · Clonación de voz en producción: retención, reuso y resiliencia

> Clonar una voz por API (MiniMax/ElevenLabs vía fal) tiene trampas de producción que no salen en el
> "hello world": retención, reuso barato, y muestras sucias. Lo resuelto en AGENTE STUDIO.

## Patrón clone-once-reuse (clave de costo)
La clonación NO es por cada audio: clonas **una vez** → obtienes un `voice_id` → lo **reusas** para
cada TTS (barato). Guarda el `voice_id` de forma persistente.
```
1ª vez:  voice-clone(audio_url) -> custom_voice_id  (guardar)  + speak(texto, voice_id)
luego:   speak(texto, voice_id)                                  (solo TTS, centavos)
```
- TTS MiniMax speech-02-hd ≈ **$0.03/1k chars**. Clonado ≈ una vez (~$1.5 aprox, verifica en tu panel).
- **Presets vs clon**: las voces preset (p.ej. `Spanish_Narrator`) son `voice_id` nativos del proveedor;
  un clon es un `custom_voice_id`. Misma ruta de `speak`, distinto id.

## Retención: el voice_id caduca (¡y rompe en silencio!)
**MiniMax borra la voz clonada a los ~7 días si no la usas** al menos una vez en ese periodo. El timer
**se reinicia con cada uso**. Implicaciones:
- Si usas la voz seguido (diario/semanal) → nunca se borra → pagas el clonado UNA vez.
- Si la abandonas >7 días → al volver, `speak(voice_id)` **falla** porque el id ya no existe.

## Resiliencia: re-clonado automático
Guarda también la **muestra** (audio de referencia). Si `speak` falla porque la voz ya no existe y
tienes la muestra → **re-clona solo** y guarda el id nuevo:
```js
function esVozBorrada(e){ const m=String(e?.message||e).toLowerCase();
  return /voice/.test(m) && /(not found|invalid|exist|no existe|deleted|expired)/.test(m); }

async function generate({ text, refAudioUrl, voiceId, deps }) {
  if (!voiceId) { const id = await cloneVoice(refAudioUrl, deps);
                  return { ...await speak(text,id,deps), voiceId:id, cloned:true }; }
  try { return { ...await speak(text,voiceId,deps), voiceId, cloned:false }; }
  catch (e) { if (refAudioUrl && esVozBorrada(e)) {           // re-clona solo si la voz se borró
                const id = await cloneVoice(refAudioUrl, deps);
                return { ...await speak(text,id,deps), voiceId:id, cloned:true }; }
              throw e; }                                       // error transitorio -> NO malgastar un clonado
}
```
**Conservador a propósito**: re-clonar solo si el error MENCIONA la voz. Un timeout/rate-limit NO debe
disparar un clonado de ~$1.5. El server guarda el id nuevo (`if r.voiceId !== guardado -> persistir`).

## Calidad de la muestra (sin ffmpeg en el server)
El clon depende de una muestra LIMPIA. Si no puedes correr ffmpeg en el server, usa los flags del
proveedor:
```
voice-clone(audio_url, model='speech-02-hd', noise_reduction=true, need_volume_normalization=true)
```
Esto limpia y nivela la muestra ANTES de clonar (aplica el best-practice de [[01-audio-avatar-pipeline]]
sin pipeline local). Pide al usuario: muestra **limpia, una sola persona, 30-60s, sin música/ruido**.

## Elegir motor para LatAm
- Voces preset inglesas leyendo español = acento gringo. Para LatAm, voces **nativas** (MiniMax
  `Spanish_*`) ganan en naturalidad **y** costo (~1/3 de ElevenLabs). Ver [[05-tts-voice-cloning-2026]].
- Sinergia: la voz TTS limpia es el mejor input para el lip-sync del avatar (audio limpio → mejor sync).
