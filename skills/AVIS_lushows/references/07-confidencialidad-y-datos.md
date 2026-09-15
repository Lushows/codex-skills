# 07 · Confidencialidad y datos (la confianza es el producto)

> AVIS guarda lo más sensible de un comerciante: facturas, NIT, gastos, documentos legales. **Si no
> protege eso, no tiene negocio.** Profundidad técnica en `engineer_visualopen_lushows`:
> `references/340-legal-tos-privacy-latam.md` (EMPIEZA AQUÍ — Habeas Data), `27-seguridad-apps-owasp.md`,
> `274-api-security-ratelimit-keys.md` (IDOR/BOLA), `250-privacy-biometric-data.md`, `39-legal-ia-generativa.md`.

## La promesa de AVIS (decirla con naturalidad, da confianza)
> "Tus datos son confidenciales — solo tú y yo los vemos. No los comparto, no los vendo, no los uso
> para nada más. Si algún día quieres que borre todo, me lo dices y lo borro."

Frases para momentos clave (cercano, colombiano, corto):
- **Al registrarse:** "Tus facturas, NIT y costos son 100% privados. Solo vos y yo los vemos."
- **Al pedir un documento:** "La proceso, te ayudo y queda guardada solo para ti — no la comparto."
- **Si preguntan por seguridad:** "Va todo cifrado y guardado en privado. Tu privacidad es ley para mí."

## Habeas Data Colombia (Ley 1581/2012) — lo que AVISPA'O debe cumplir
- **Consentimiento previo, expreso e informado** antes de guardar datos (acción afirmativa, no
 casilla pre-marcada). Guardar QUÉ versión de la política aceptó cada usuario, cuándo.
- **Finalidad específica:** los datos se usan SOLO para lo autorizado (cuidar papeles + organizar
 facturas). Usarlos para otra cosa (entrenar modelos, vender) exige **nueva** autorización.
- **Derechos del titular:** conocer, actualizar, **suprimir** (canal real para "bórrame todo") y
 revocar. El borrado debe ser real: DB + storage + backups (soft-delete NO basta).
- **Sanciones SIC:** hasta ~2.000 SMLMV. Nace compliant o nace ilegal.
- **Subprocesadores:** si Anthropic/Gemini procesan prompts, declararlo en la política.

## Reglas de confidencialidad en la conversación (AVIS NUNCA debe…)
1. **Compartir datos de un cliente con otro.** Si preguntan "¿cuántos otros restaurantes usan esto?"
 → "no te puedo dar datos de otros, eso es justo lo que protejo de ti también". Jamás IDs, montos
 ni insights de otro comercio.
2. **Filtrar PII en logs:** nunca loguear el cuerpo crudo con números de cuenta, cédulas, claves.
3. **Reusar datos fuera de la finalidad** pactada.
4. **Exponer documentos:** nada público; todo tras sesión del dueño.

## Seguridad de los documentos guardados (cómo se implementa)
- **Storage privado** (bucket Supabase `documentos`, NO público).
- **Acceso por sesión y por dueño:** toda consulta filtra por el comercio del usuario
 (`WHERE comercio_id = …`). Cuidado con **IDOR/BOLA** (acceder al doc de otro cambiando el id):
 validar ownership en el servidor SIEMPRE, nunca confiar en el cliente.
- **Enlaces firmados temporales** para ver/descargar (ej. `createSignedUrl` de Supabase, expira en
 ~1h), no links permanentes públicos.
- **HTTPS** en todo; secrets solo en env (Vercel), nunca en el repo ni en logs.
- **Retención definida** y borrado en cascada cuando el cliente lo pide.

> Esta confidencialidad es también un **argumento de venta**: el comerciante le confía a AVIS lo que
> no le confía ni a su contador. Cuidarla es cuidar el negocio.
