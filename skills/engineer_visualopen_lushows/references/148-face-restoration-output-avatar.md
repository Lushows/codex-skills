# 148 · Restaurar la cara del output del avatar (GFPGAN · CodeFormer · RestoreFormer)

> Los modelos de avatar/lip-sync generan la cara a baja resolución nativa (96-256px). En 1080p se ve
> blanda. La restauración de cara recupera detalle de piel, dientes y ojos — pero mal aplicada **cambia
> la identidad** o introduce parpadeo entre frames. Es un paso de afinado, no un botón mágico.

## Por qué hace falta
- Wav2Lip genera la boca a **96px** → al pegarla en un frame HD queda borrosa. MuseTalk/LatentSync a
  256px están mejor pero aún por debajo de 1080p nativo.
- El restaurador "alucina" detalle plausible (textura de piel, brillo de dientes) sobre la cara
  cropeada y la devuelve nítida. Cruza con [[146-lipsync-a-fondo-wav2lip-musetalk-latentsync]].

## Los tres modelos (verificado 2026)

| Modelo | Enfoque | Licencia | Control fidelidad | Fuerte en | Débil en |
|---|---|---|---|---|---|
| **GFPGAN** | GAN + prior facial (StyleGAN) | **Apache-2.0** (comercial OK) | no (un solo modo) | rápido, natural, identidad estable | degradación severa, dientes |
| **CodeFormer** | Codebook + Transformer | **S-Lab / NTU — NO comercial** | **sí: `w` 0→1** | degradación severa, control calidad/identidad | puede sobre-suavizar, licencia |
| **RestoreFormer** | Key-value pairs (ViT) | académica, revisar términos | no | mejor FID en datos reales | menos adoptado/soportado |

> **CodeFormer es no-comercial** (licencia S-Lab de NTU). Para producción de cliente
> (Lushows/AGENTE STUDIO) usa **GFPGAN (Apache-2.0)** salvo licencia comercial explícita de CodeFormer.
> [no verificado] que exista una vía comercial gratuita de CodeFormer a 2026.

## El parámetro que importa: `w` de CodeFormer (fidelity weight)
- `w` ∈ [0, 1] equilibra **calidad vs fidelidad**:
  - **w = 0** → máxima calidad/nitidez, pero **inventa** rasgos → puede no parecerse a la persona.
  - **w = 1** → máxima fidelidad a la cara original, pero menos "limpieza".
- Punto de partida práctico: **w ≈ 0.5-0.7**. Sube hacia 1 si la identidad se desvía; baja hacia 0.3
  solo si el input está muy degradado y la identidad importa poco.
- GFPGAN no tiene este dial: si la identidad se va, no hay perilla → cambia de modelo o baja la fuerza
  del blend.

## Aplicarlo frame-by-frame (el problema real: temporal flicker)
Restaurar **cada frame por separado** es la causa #1 de artefactos en video:
- Cada frame se restaura de forma independiente → el restaurador "alucina" detalle **distinto** por
  frame → **parpadeo** de textura de piel, dientes que cambian de forma, ojos que titilan.
- Mitigaciones:
  - **Solo la región de la boca/cara inferior** (la que el lip-sync tocó), no toda la cara → menos
    superficie para parpadear y preserva ojos/frente originales.
  - **Fidelidad alta** (w→1 en CodeFormer) reduce la alucinación frame-a-frame.
  - **Suavizado temporal** del bbox de la cara (mismo crop estable entre frames) reduce el salto.
  - Restauradores **de video** (temporalmente consistentes) > aplicar uno de imagen por frame, cuando
    el flicker es inaceptable. Cruza con [[138-upscaling-restauracion-realtime-escala]].

## Orden en el pipeline
```
lip-sync genera boca (96/256px) → paste-back en frame → CROP cara → restaurador (GFPGAN/CodeFormer)
→ blend de vuelta solo la cara → (opcional) upscale del frame completo
```
- Restaura **antes** del upscale general del frame: restaurador trabaja la cara, upscaler el resto.
- No restaures el frame entero: solo la cara cropeada, o pintarás artefactos en el fondo.

## Costo y cuándo NO usarlo
- Es **una pasada de red por frame de cara** → suma tiempo/GPU. En 30fps × minutos, no es trivial.
- En **realtime** añade latencia → en vivo suele saltarse (MuseTalk 256px se ve aceptable sin él).
  Cruza con [[147-avatar-realtime-streaming-baja-latencia]].
- Si usaste LatentSync/MuseTalk a 256px y el output final es ≤720p, puede **no hacer falta**: pruébalo
  sin restaurador primero. El restaurador es para HD o para tapar la borrosidad de Wav2Lip.

## Recomendación
- **Producción comercial, batch HD** → **GFPGAN** (Apache-2.0), solo región de cara, tras paste-back.
- **Calidad máxima, uso no comercial/investigación** → **CodeFormer** con `w ≈ 0.6`.
- **Flicker visible** → restaurar solo boca + fidelidad alta + considerar restaurador de video.
- **Realtime** → omitir; subir resolución vía modelo nativo de 256px, no vía post.

Cruza con [[08-upscaling-restauracion]], [[146-lipsync-a-fondo-wav2lip-musetalk-latentsync]] y [[138-upscaling-restauracion-realtime-escala]].
