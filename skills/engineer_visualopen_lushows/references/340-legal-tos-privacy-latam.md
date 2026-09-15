# 340 · Legal para SaaS LatAm: ToS, privacidad, Habeas-Data y GDPR

> No soy abogado y esto no es asesoría legal — es el mapa de ingeniería para no construir
> ilegalidad por defecto. Un SaaS que toca datos de colombianos sin autorización previa y
> expresa ya nace con multa potencial de hasta 2000 SMLMV. Diseña el consentimiento, no lo parchees.

## Los dos documentos base
- **Términos de Servicio (ToS)**: contrato de uso. Define límites de responsabilidad, propiedad del output (clave en gen-AI: ¿de quién es el video generado?), cláusula de uso aceptable, terminación, ley aplicable y jurisdicción. Sin ToS no podés banear ni limitar responsabilidad.
- **Política de Privacidad**: cómo recolectás, usás, compartís y retenés datos. **Obligatoria** si capturás cualquier dato personal (email cuenta como dato personal). Meta/WhatsApp y stores la exigen para publicar.

## Colombia — Ley 1581 de 2012 (Habeas Data) [verificado]
Aplica a **todo** el que trate datos de personas en Colombia. Reglas no negociables:
- **Autorización previa, expresa e informada** antes de recolectar/tratar. Un checkbox pre-marcado NO es consentimiento válido; debe ser acción afirmativa con finalidad clara.
- **Finalidad específica**: solo usás el dato para lo que autorizó. Reusarlo para marketing sin nueva autorización = violación.
- **Datos sensibles** (salud, biometría, orientación): protección reforzada, autorización explícita; biometría facial/voz en avatares cae acá (cruza con [[250-privacy-biometric-data]]).
- **Derechos del titular**: conocer, actualizar, rectificar, suprimir, revocar. Necesitás un canal real para ejercerlos (no un email muerto).
- **Registro Nacional de Bases de Datos (RNBD)** ante la SIC para ciertas bases.
- **Sanciones**: la SIC multa hasta **2000 SMLMV (~$180 millones COP en 2026)**; ha impuesto multas de >6.000 millones COP a telcos/salud/e-commerce (2022-2024).
- **Reforma en curso [no verificado, en trámite]**: proyecto de ley de agosto 2025 introduce **evaluaciones de impacto de privacidad** obligatorias cuando hay alto riesgo o tecnologías avanzadas (IA); omitirlas sería sancionable.

## GDPR (si tocás usuarios en la UE)
Aplica por **ubicación del usuario**, no de tu empresa. Si un europeo usa STUDIO, GDPR aplica:
- **Base legal** para cada tratamiento (consentimiento, contrato, interés legítimo).
- **DPA (Data Processing Agreement)** con cada subprocesador (RunPod, OpenAI, Anthropic, Stripe).
- Derechos: acceso, portabilidad, **olvido** (borrado real), oposición.
- **Transferencias internacionales** (datos saliendo de UE a tus GPUs US) requieren SCCs o mecanismo equivalente.
- Multas hasta **4% de la facturación global anual** o €20M, lo que sea mayor.

## Patrones de ingeniería para cumplir
| Requisito | Implementación |
|---|---|
| Consentimiento granular | tabla `consents`: timestamp, versión del ToS/privacy, finalidad, IP |
| Versionado de políticas | guardá QUÉ versión aceptó; al cambiarla, re-pedí consentimiento |
| Derecho al borrado | borrado **real** en cascada (DB + storage + backups + logs), no soft-delete |
| Retención | TTL por tipo de dato; purga automática; no guardes "por si acaso" |
| Subprocesadores | lista pública y actualizada; DPA firmado con cada uno |
| Datos biométricos | consentimiento explícito separado; cifrado en reposo (ref [[250-privacy-biometric-data]]) |

## Otras jurisdicciones LatAm (no solo Colombia)
| País | Ley | Autoridad | Nota |
|---|---|---|---|
| México | LFPDPPP | INAI (en transición) | aviso de privacidad obligatorio, derechos ARCO |
| Brasil | LGPD | ANPD | calcada de GDPR; multas hasta 2% facturación BR (tope R$50M/infracción) |
| Argentina | Ley 25.326 (en reforma) | AAIP | adecuación a estándar GDPR en curso |
| Chile | Ley 21.719 (2024) | nueva Agencia | régimen moderno tipo GDPR, multas significativas |

Si vendés cross-LatAm, el **mínimo común denominador es: consentimiento previo expreso + finalidad + derechos del titular + canal para ejercerlos**. Cúmplelo y cubrís casi todas.

## Consentimiento de IA generativa (lo que muerde en STUDIO)
- Si entrenás o ajustás con datos de usuarios, necesitás autorización **explícita y separada** para ese fin; usar contenido subido "para mejorar el modelo" sin avisar es violación de finalidad.
- El **output generado** (video con cara/voz de una persona): asegurá derechos de imagen y consentimiento del retratado; un avatar de alguien sin permiso es problema civil **y** de datos biométricos.
- Subprocesadores de IA (Anthropic, OpenAI, RunPod): verificá su política de **retención y no-entrenamiento** sobre tus datos; decláralos en tu lista de subprocesadores (ref [[39-legal-ia-generativa]]).

## Gotchas
1. **Checkbox pre-marcado** = consentimiento inválido bajo 1581 y GDPR.
2. **Soft-delete como "borrado"** → el dato sigue ahí; incumple derecho al olvido. Borra de verdad, incluido el storage de media.
3. **Logs con PII** (emails, prompts con datos personales) → son una base de datos no declarada; anonimiza o purga.
4. **Olvidar los subprocesadores** → cada API externa que recibe datos del usuario necesita DPA; sin eso, transferencia ilegal.
5. **Prompts/outputs de IA con datos sensibles** → si el modelo procesa fotos de cara/voz, es biometría: tratamiento reforzado.
6. **Copiar un ToS genérico de internet** → puede declarar jurisdicción ajena o ceder derechos que no querés; ajústalo a tu ley aplicable real.

**Fuentes:** funcionpublica.gov.co (Ley 1581 de 2012) · resguard-solutions.com (Habeas Data guide) · dernegocios.uexternado.edu.co (modernización Ley 1581) · SIC (régimen sancionatorio).

Cruza con [[39-legal-ia-generativa]] y [[250-privacy-biometric-data]].
