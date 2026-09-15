# 219 · Super-resolución y bandwidth extension de audio

> Una grabación de teléfono o de WhatsApp llega con banda recortada a ~4-8 kHz: suena apagada, sin
> "aire". Super-res reconstruye las frecuencias altas que nunca se grabaron → la voz recupera brillo.

## Qué es (y qué no)
**Bandwidth extension / audio super-resolution**: tomar audio de baja tasa/banda estrecha (8 kHz, voz
telefónica) y **sintetizar** el contenido de alta frecuencia ausente, llevándolo a 16/24/48 kHz reales.
No es resamplear: `ffmpeg -ar 48000` solo interpola, no **crea** información — la voz sigue sonando sorda.
Super-res sí inventa armónicos plausibles con un modelo entrenado.

Distinción con vecinos:
- **denoise** ([[218-audio-denoise-enhance-deepfilternet]]) quita ruido; no añade banda.
- **super-res** añade banda; no quita ruido (denoisea **antes**, o el modelo amplifica el hiss).

## Cuándo usarla en el avatar
Solo si la **fuente es pobre de banda**: audio de llamada, voz de cámara barata, archivo viejo a 8/11 kHz.
Si ya tienes una muestra a 24/48 kHz limpia, **sáltatela** — no aporta y arriesga artefactos.

## Herramientas open (2026)
| Opción | Enfoque | Notas |
|---|---|---|
| **DeepFilterNet3** | denoise **con** upsampling a 48k integrado | el camino fácil: limpia y sube banda en un paso, no generativo |
| **Resemble-Enhance** | enhancer generativo, reconstruye alta frecuencia | mejor "brillo" en voz muy degradada; GPU; vigila el timbre |
| **AudioSR / NU-Wave2 / diffusion BWE** | super-res por difusión, propósito general | calidad alta, más lento; útil para casos extremos |

Pragmático: para una muestra de avatar, **DeepFilterNet3** (upsample integrado) o **Resemble-Enhance**
cubren el 90%. Reserva los modelos de difusión (AudioSR) para fuentes realmente malas.

## Hands-on
```bash
# camino simple: limpiar + subir a 48k
deepFilter telefono_8k.wav -o out/      # denoise + upsample

# fuente muy degradada → enhancer generativo reconstruye banda
resemble-enhance in/ out/               # denoise + enhance (incluye reconstrucción de HF)
```
Después, normaliza y lleva al sample rate del clonador con ffmpeg.

## Detalles que muerden
- **Orden**: denoise → super-res. Subir banda sobre ruido = ruido brillante y agresivo.
- **Alucinación de armónicos**: la difusión inventa HF que puede no coincidir con la voz real →
  compara A/B; si "sisea" o suena artificial, baja la intensidad o quédate sin super-res.
- **No multiplica info**: de 4 kHz reales a 48 kHz hay mucho inventado. Gestiona expectativas: mejora
  inteligibilidad y brillo, no convierte una llamada en estudio.
- **Costo/latencia**: difusión es cara; offline en preparación de muestra, nunca en caliente.

Cruza con [[218-audio-denoise-enhance-deepfilternet]].
