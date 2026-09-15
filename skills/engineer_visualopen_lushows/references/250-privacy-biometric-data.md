# 250 · Privacidad de datos biométricos: cara, voz y consentimiento

> Un avatar parlante procesa la **cara y la voz** de una persona: el dato más sensible que existe.
> En GDPR es "categoría especial"; en Colombia, "dato sensible" bajo Habeas Data. Pifiarlo = multas y demandas.

## Cara y voz son datos biométricos especiales
Bajo GDPR Art. 9, los datos biométricos usados para **identificar** a una persona son categoría especial:
prohibidos por defecto salvo base legal explícita (casi siempre **consentimiento explícito**). La voz cuenta
igual. En Colombia (Ley 1581/2012, Habeas Data) son **datos sensibles**: requieren autorización **previa,
expresa e informada** y nunca pueden ser obligatorios para acceder a un servicio. La SIC sancionó en 2025
con multas grandes por imponer reconocimiento facial obligatorio — precedente directo para un producto de avatares.

## Consentimiento: cómo hacerlo bien
No basta un checkbox enterrado en los términos. Mínimos:

| Requisito | Implementación |
|---|---|
| **Explícito y específico** | Consentimiento separado para "usar tu cara/voz para generar video". No agrupado con otros usos. |
| **Informado** | Qué generas, cuánto retienes, con quién compartes, cómo borrar. En lenguaje claro. |
| **Granular** | Opt-in por finalidad: generar ≠ entrenar el modelo con su dato ≠ marketing. |
| **Revocable** | Mecanismo para retirar el consentimiento y borrar (derecho al olvido, Art. 17 GDPR). |
| **Prueba de identidad de origen** | Que quien sube la cara/voz **sea** esa persona o tenga su autorización (anti-deepfake, [[249-adversarial-jailbreak-image-models]]). |

Guarda el consentimiento **versionado y con timestamp** en el audit log ([[251-audit-logging-compliance]]):
qué versión del texto aceptó, cuándo, desde dónde.

## Minimización y retención: lo que no guardas no te roban
- **No retengas el biométrico crudo** más de lo necesario. ¿Necesitas la foto original tras generar? Bórrala.
- **Separa** el dato biométrico del resto del perfil; cifra en reposo (KMS) y en tránsito.
- **Política de retención explícita** (ej. borrar input a las 24-72h, output según contrato) y **ejecútala**
  con un job, no "cuando me acuerde".
- En el worker GPU: la cara/voz pasa por VRAM/disco efímero → asegúrate de que el contenedor no persista ni
  cachee inputs en el Network Volume ([[248-container-gpu-isolation]]).

## DP y federated: qué resuelven y qué no
- **Differential Privacy**: añade ruido para que un individuo no sea reidentificable en agregados/entrenamiento.
  Útil **si entrenas/afinas** con datos de usuarios. **No** te exime de consentimiento para procesar el dato.
- **Federated Learning**: entrena sin centralizar el dato crudo. Reduce exposición, pero crea su **crisis de
  consentimiento**: borrar la influencia de un usuario de un modelo ya entrenado es matemáticamente caro
  (machine unlearning). Promete "borrado" solo si puedes cumplirlo.
- Para inferencia pura (el caso STUDIO: subo cara → genero video), DP/FL **no aplican**; lo que importa es
  consentimiento + minimización + retención + borrado.

## Transferencia internacional (el detalle que muerde a LatAm)
Si el worker corre en RunPod/US y el usuario es de Colombia/UE, hay **transferencia internacional** de dato
sensible. Necesitas base legal (consentimiento informado de la transferencia, o cláusulas tipo). Documenta
dónde se procesa físicamente la cara/voz. Habeas Data exige informar el destino; GDPR exige garantías adecuadas.

## Checklist mínimo
1. Consentimiento explícito, granular, versionado y revocable. 2. Prueba de identidad/autorización de origen.
3. Cifrado en reposo y tránsito. 4. Retención corta + borrado automatizado. 5. Sin persistencia de inputs en
el worker. 6. Base legal de transferencia internacional. 7. Todo trazado en audit log.

Cruza con [[39-legal-ia-generativa]] y [[165-moderacion-safety-output-generado]].
