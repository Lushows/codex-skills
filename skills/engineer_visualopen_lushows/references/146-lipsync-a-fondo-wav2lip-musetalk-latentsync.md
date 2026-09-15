# 146 · Lip-sync a fondo: Wav2Lip · MuseTalk · LatentSync (sin gestos)

> Lip-sync puro = solo re-genera la BOCA sobre un video/imagen existente. No mueve cabeza, ojos ni
> manos. Más barato, más rápido y más controlable que un avatar completo — cuando ya tienes el video base.

## Cuándo lip-sync puro vs avatar completo
- **Lip-sync puro**: ya tienes metraje real (un presentador grabado, un clip de stock con cara) y solo
  quieres cambiar lo que dice. Preserva iluminación, textura de piel y movimiento de cabeza originales.
- **Avatar completo** (SadTalker/LongCat/talking-head): partes de **una sola foto** y necesitas generar
  pose, parpadeo y gestos desde cero. Cruza con [[119-avatares-talking-head-self-hosted-2026]].
- Regla: si tienes video → lip-sync. Si tienes una foto → avatar. Mezclar (avatar para el plano,
  lip-sync para refinar boca) es válido pero rara vez necesario.

## Los modelos (verificado 2026)

| Modelo | Arquitectura | Resolución cara | VRAM inf. | Velocidad | Licencia | Boca |
|---|---|---|---|---|---|---|
| Wav2Lip | GAN (2020) | 96×96 (¡baja!) | ~4-6 GB | muy rápida | repo académico, pesos no-comercial | sincro fuerte, **borrosa/wobbly en HD** |
| Wav2Lip-HD / -HQ | Wav2Lip + GFPGAN/ESRGAN post | upscaled | +restaurador | media | derivado, depende de pesos | nítida pero "pegada" |
| MuseTalk 1.5 | Inpainting en espacio latente | 256×256 | ~6-8 GB | **30fps+ realtime (V100)** | **MIT** (código y pesos, comercial OK) | buena, identidad consistente |
| LatentSync 1.5 | Stable Diffusion + SyncNet | 256×256 | **8 GB** | lenta (difusión) | **OpenRAIL++** (comercial con atribución) | la más nítida y temporal |
| LatentSync 1.6 | idem, mejor temporal | 256×256 | ~18 GB | lenta | OpenRAIL++ | top calidad |
| VideoReTalking | 3 etapas (expr+lip+enhance) | medio | ~10 GB | lenta | repo académico, revisar términos | edita video "in the wild" |
| Diff2Lip | Difusión en espacio de píxeles | medio | alto | muy lenta | académico | sharp, supera Wav2Lip en FID/MOS |

> LatentSync 2 aparece en forks (cog-LatentSync-2, ~6.5 GB) pero el release oficial estable de
> ByteDance a 2026 es 1.5/1.6. Trata "LatentSync 2" como [no verificado] para producción.

## El pipeline real (los 3 pasos que nadie documenta bien)
1. **Face detection + crop**: se detecta la cara por frame (S3FD en Wav2Lip; detectores más nuevos en
   MuseTalk/LatentSync), se recorta y alinea a la resolución del modelo (96 o 256). **Aquí mueren los
   resultados**: detección inestable → boca que salta de tamaño/posición entre frames (jitter).
   - Suaviza la caja de la cara entre frames (smoothing temporal del bbox) para matar el jitter.
   - Caras de perfil, oclusiones (mano/micro) y caras pequeñas rompen la detección → recorta el plano.
2. **Inferencia de boca**: el modelo genera la región inferior de la cara condicionada al audio
   (mel-spectrogram). Wav2Lip lo hace a 96px → de ahí la borrosidad al pegarla en 1080p.
3. **Blend + paste-back**: la boca generada se funde de vuelta en el frame original (máscara suave en
   el borde). Bordes duros = "máscara visible" alrededor de la boca.

## Restauración de cara post (clave para HD)
Wav2Lip genera a 96px → **siempre** se ve blando en HD. La cura estándar es pasar GFPGAN/CodeFormer
**solo a la región de la cara** después del paste-back (Wav2Lip-HD/-HQ son exactamente esto).
- Riesgo: el restaurador puede **cambiar la identidad** o "limar" la sincronía → aplicar con fidelidad
  alta y solo si la boca quedó borrosa. MuseTalk/LatentSync a 256px casi no lo necesitan.
- Todo el detalle (w de CodeFormer, frame-by-frame, artefactos) en [[148-face-restoration-output-avatar]].

## Cómo elegir
- **Realtime / muchos videos / comercial sin fricción legal** → **MuseTalk 1.5** (MIT, 30fps).
- **Máxima calidad de boca, batch offline** → **LatentSync 1.5/1.6** (difusión, OpenRAIL++).
- **Editar un video real preservando todo menos la boca** → VideoReTalking o LatentSync.
- **Legacy/ultraligero o baseline rápido** → Wav2Lip **+ GFPGAN obligatorio** si el output es HD.
- Diff2Lip: mejor FID que Wav2Lip pero muy lento → solo si la nitidez justifica el costo de difusión.

## Trampas de costo/calidad
- No subas la resolución del crop esperando más detalle: el modelo genera a su tamaño nativo (96/256),
  el resto es upscale. Más resolución útil = restaurador o modelo de difusión, no el crop.
- Audio: usa el sample rate que espera el modelo (16 kHz mel). Audio sucio → sincronía pobre; limpia/
  normaliza antes. Cruza con [[01-audio-avatar-pipeline]].
- Pesos no-comerciales (Wav2Lip original, VideoReTalking) son trampa legal en producción de cliente:
  prefiere MuseTalk (MIT) o LatentSync (OpenRAIL++) para Lushows/AGENTE STUDIO.

Cruza con [[119-avatares-talking-head-self-hosted-2026]], [[01-audio-avatar-pipeline]] y [[148-face-restoration-output-avatar]].
