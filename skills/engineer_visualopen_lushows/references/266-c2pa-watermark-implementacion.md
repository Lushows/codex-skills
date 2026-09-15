# 266 · Implementar C2PA + watermark invisible (EU AI Act)

> Desde el 2 de agosto de 2026 el Art. 50 del EU AI Act exige que TODO output de IA generativa sea marcado en formato legible por máquina [verificado].
> La respuesta técnica que la Comisión nombra por ejemplo es **C2PA Content Credentials**, y el borrador exige enfoque multicapa: manifiesto + watermark invisible.

## Qué obliga la ley (y desde cuándo)
- **Art. 50(2)**: outputs de IA generativa marcados como artificiales en formato **machine-readable**.
  Aplica desde **2-ago-2026**; sistemas ya en mercado tienen hasta **2-dic-2026** (acuerdo Omnibus, mayo 2026) [verificado].
- El **Code of Practice** (2º borrador mar-2026, final esperado jun-2026) declara que **"ninguna técnica de
  marcado activa basta sola"** → exige **multicapa**: provenance embebida (C2PA) **+** watermark invisible a
  nivel de píxel que sobreviva compresión, recorte y cambio de formato [verificado].

No es opcional para vender en la UE. Sancionable. Cruza con [[165-moderacion-safety-output-generado]] para el resto de obligaciones de safety.

## Las dos capas (complementarias, no alternativas)
| Capa | Qué es | Sobrevive a… | Falla cuando… |
|---|---|---|---|
| **C2PA manifest** (hard binding) | metadata firmada criptográficamente embebida en el archivo | validación, edición trazada | un re-encode/screenshot **borra** la metadata |
| **Watermark invisible** (soft binding) | patrón en los píxeles, ID recuperable | compresión, crop, format-conv, screenshot | edición agresiva/difusión puede degradarlo |

Juntas = **Durable Content Credentials**: el watermark lleva un ID que, si la metadata se pierde, **reencuentra**
el manifiesto en tu repositorio (lookup por soft-binding) [verificado].

## C2PA: cómo firmar (tooling open source)
Herramientas de la Content Authenticity Initiative (Apache-2.0/MIT) [verificado]:
- **`c2patool`** (CLI): lee/escribe manifiestos en imagen/audio/video.
- **`c2pa-python`** (Python 3.10+): crea, firma y embebe manifiestos desde el handler de generación.

Flujo en el worker, **post-generación, antes de subir a storage**:
1. Construye el **manifest** (JSON): `claim_generator` (tu app), assertions `c2pa.actions` con
   `c2pa.created` + `digitalSourceType: trainedAlgorithmicMedia` (declara "hecho por IA"), modelo/seed opcional.
2. **Firma** con tu certificado. Para producción real necesitas cert de una CA en la **trust list** de C2PA;
   para dev/test sirve un self-signed (no validará como confiable, pero embebe).
3. Embebe en el asset → el archivo sale ya con Content Credentials.

```bash
c2patool input.mp4 -m manifest.json -o output.mp4   # firma y embebe
c2patool output.mp4                                  # verifica/lee el manifiesto
```

## Watermark invisible: TrustMark
**TrustMark** (CAI, open source) encodea un ID aleatorio en los píxeles como **soft binding** del manifiesto
C2PA [verificado]. Pipeline:
1. Tras generar, aplica TrustMark con un ID único → guárdalo en tu DB junto al asset ([[263-asset-gallery-management.md]]).
2. Lista ese algoritmo en el `SoftBindingAlgorithmList` del manifiesto C2PA.
3. Si alguien recibe el archivo sin metadata, decodea el watermark → ID → lookup → recuperas la procedencia
   (Durable Content Credential).
Para **video**: marca frames (clave + muestreo); para **audio/TTS** hay watermarking espectral análogo.

## Dónde encaja en el pipeline
```
generar (GPU) → moderación output [[165]] → C2PA firmar → TrustMark watermark → derivados/thumb → subir storage → entregar
```
- Hazlo en el **worker**, no en el cliente (el cliente puede saltárselo).
- Re-aplica al **derivado servido** si el re-encode del thumbnail rompe la marca del original.
- Guarda el `watermark_id` y `manifest` en el registro del asset para auditoría y lookup.

## Errores que muerden
- Solo C2PA, sin watermark → un screenshot borra TODA la prueba; **no cumple** el requisito multicapa.
- Firmar con cert fuera de la trust list y creer que "valida" → embebe, pero los verificadores lo marcan no-confiable.
- Watermark en el original pero NO en el derivado que realmente sirves/posteas → distribuyes media sin marca.
- Asumir que free tier basta con watermark y de paso saltarse C2PA → el manifest es el requisito legible-máquina central.
- No registrar el ID del watermark → tienes la marca pero no puedes resolver a qué asset/prompt pertenece.

Cruza con [[38-watermarking-procedencia]] (fundamentos de la técnica) y [[165-moderacion-safety-output-generado]] (el resto del cumplimiento de output).
