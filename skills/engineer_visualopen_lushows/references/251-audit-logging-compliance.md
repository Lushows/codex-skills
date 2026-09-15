# 251 · Audit logging de generaciones: quién, qué, cuándo (compliance)

> Cuando alguien pregunte "¿quién generó este deepfake con mi servicio y cuándo?", tu única respuesta
> defendible es un log inmutable. Sin trazabilidad no hay compliance, no hay forense, no hay defensa legal.

## Por qué el audit log no es opcional
Tres presiones lo exigen a la vez:
- **Legal/forense**: responder a un abuso (deepfake, NSFW, suplantación) requiere reconstruir el evento.
- **EU AI Act Art. 50** (transparencia de contenido sintético, en vigor **2-ago-2026**): donde el watermark
  no alcanza, debes mantener **logs/huellas** que permitan trazar el contenido a su origen IA. Aplica global
  si sirves a usuarios de la UE.
- **Privacidad** ([[250-privacy-biometric-data]]): demostrar que hubo consentimiento exige registrar **cuándo
  y qué versión** se aceptó.

## Qué loguear por cada generación
Un registro por job, idealmente ligado al `job_id` del orquestador ([[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]]):

| Campo | Por qué |
|---|---|
| `who` | user_id, tenant, IP/origen, método de auth. Atribución. |
| `when` | timestamp UTC de submit y de finalización. |
| `what` | modelo + **revisión/sha** de pesos, parámetros, prompt (o su hash si es sensible). |
| `inputs` | hash de la imagen/audio de entrada (no el blob), su origen, resultado del filtro SSRF. |
| `consent_ref` | versión + timestamp del consentimiento biométrico aceptado. |
| `safety` | veredicto del pre-filtro y del post-moderador ([[249-adversarial-jailbreak-image-models]]), score. |
| `output_ref` | hash del resultado, manifest C2PA/watermark emitido, dónde se guardó. |
| `cost/infra` | GPU, duración, worker_id. Cruza con FinOps y SLO. |

Loguea **prompts bloqueados** también: son la señal temprana de abuso.

## Inmutabilidad: un log que se puede editar no es evidencia
- **Append-only**: destino que no permita borrar/editar (object-lock/WORM en S3/R2, o sink dedicado).
- **Encadenado por hash** (cada registro incluye el hash del anterior) → detectas manipulación. Para alto
  valor, anclar el hash periódicamente a algo externo (timestamp firmado).
- **Separación de poderes**: quien opera el worker **no** puede borrar el audit log. El sink vive en otra cuenta/rol.
- **Reloj confiable**: NTP; un timestamp falsificable no sirve de evidencia.

## Provenance del output: C2PA + watermark (no es lo mismo que el log)
El audit log es **interno** (tu trazabilidad). La **provenance** viaja **con el archivo** para el mundo:
- **C2PA / Content Credentials**: manifest firmado criptográficamente —quién y cuándo generó— incrustado en
  el medio. Satisface la parte "machine-readable" del AI Act.
- **Watermark imperceptible** (estilo SynthID): sobrevive a recortes/recompresión donde el metadato se borra.
- AI Act pide **capas**: etiqueta visible + manifest C2PA + watermark invisible. C2PA solo **no** basta.
- Emite el manifest **en el worker, al generar**, y registra su id en el log → el output es trazable aunque le quiten el metadato.

## PII en los propios logs (el auto-gol clásico)
El audit log puede convertirse en sí mismo en un repositorio de datos sensibles:
- **No guardes el biométrico crudo** en el log → guarda **hashes/refs**, no la cara/voz.
- Prompts pueden traer PII → hashea o tokeniza si la política lo exige; controla acceso al log (RBAC, audita el acceso al audit).
- Aplica la **misma retención** y derecho al olvido que al dato: si borras al usuario, su registro debe
  poder anonimizarse sin romper la cadena de hash (guarda el hash, borra el contenido).

## Checklist
1. Un registro append-only por job con who/what/when/inputs/safety/output. 2. Encadenado por hash + WORM.
3. Sink separado del operador. 4. C2PA + watermark en el output, id en el log. 5. Refs/hashes, no biométrico
crudo. 6. Retención y anonimización alineadas con privacidad. 7. Logueo de bloqueos para forense.

Cruza con [[62-analytics-product-tracking]] y [[159-monitoreo-slo-servicio-gpu]].
