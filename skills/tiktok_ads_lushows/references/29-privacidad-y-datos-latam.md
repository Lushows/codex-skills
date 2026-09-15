# 29 — Privacidad y datos LatAm

La **privacidad de datos** es el conjunto de reglas legales sobre cómo puedes recolectar, usar y compartir información de personas. Lee este módulo antes de instalar el Pixel (ver 14), subir listas de clientes (ver 28) o crear públicos personalizados (ver 21). No es el módulo del abogado aburrido: en LatAm una multa por mal manejo de datos te cuesta más que toda tu pauta del año, y un mal manejo puede costarte la **cuenta publicitaria** entera. Aquí está cómo cumplir SIN matar tu medición — porque, contra la intuición, cumplir bien mide mejor en 2026.

## Las leyes que te tocan

| País | Ley | Qué exige (resumen) |
|---|---|---|
| **Colombia** | Habeas Data — Ley 1581 de 2012 (vigila la SIC) | Autorización previa, informada y expresa del titular para tratar sus datos; finalidad clara; derecho a conocer/actualizar/suprimir |
| **Brasil** | LGPD — Lei 13.709 (vigila la ANPD) | Base legal para el tratamiento (consentimiento u otra), transparencia, derechos del titular, multas que pueden llegar a millones |
| **México** | LFPDPPP | Aviso de privacidad, consentimiento, derechos ARCO (acceso, rectificación, cancelación, oposición) |
| **Resto LatAm** | Leyes locales similares (Perú, Chile, Argentina) | Mismo espíritu: consentimiento + finalidad + derechos del titular |

El denominador común: **necesitas consentimiento** para usar datos personales con fines de marketing, debes decir para qué los usas, y la persona puede pedir que los borres. No es opcional ni "para empresas grandes": aplica a tu negocio desde el primer dato que captures.

## Los cuatro pilares para cumplir sin perder medición

1. **Consentimiento al recolectar.** En tu web/formulario/checkout, una casilla o aviso claro: "Autorizo el tratamiento de mis datos para fines de marketing según la política de privacidad". Sin esto, no subas esos datos a TikTok (ver 28). La casilla NO puede venir pre-marcada ni escondida. El AGENTE GASTROWHATS ya tiene `/privacy` (ver CLAUDE.md) — asegúrate de que el texto cubra explícitamente el uso publicitario y el compartir con TikTok/Meta.

2. **Política de privacidad publicada.** Una página accesible que explique qué datos recoges, para qué, con quién los compartes (TikTok, Meta) y cómo ejercer derechos. Meta y TikTok la **exigen** para aprobar tu pixel y tus campañas; tus usuarios tienen derecho a ella por ley. Sin política publicada, te expones a rechazo de la plataforma Y a sanción legal.

3. **No toques datos sensibles.** Salud, orientación sexual, religión, datos de menores, datos biométricos, etc. están especialmente protegidos. No los recolectes para pauta, no los subas, no segmentes por ellos. En TikTok, además, la segmentación por categorías sensibles está restringida por política de la plataforma.

4. **Hashing al compartir.** Cuando subes listas (ver 28), TikTok las hashea (SHA-256) para cruzarlas sin ver el dato crudo. Usa el flujo oficial de Customer File / Customer Match; nunca mandes correos/teléfonos en claro por correo, WhatsApp o canales inseguros a terceros.

## Cómo NO matar la medición mientras cumples

Cumplir privacidad y medir bien NO son opuestos. La clave en 2026:

| Mecanismo | Qué hace | Por qué te ayuda |
|---|---|---|
| **Events API / server-side** (ver 14, 57) | Manda eventos desde tu servidor, no solo desde el navegador | Resistente a bloqueadores y pérdida de cookies; más señal con consentimiento |
| **First-party data** (ver 28) | Datos que el cliente te dio con permiso | No depende de cookies de terceros que están muriendo |
| **Consentimiento bien pedido** | Casilla clara, no engañosa | Más gente acepta cuando entiende el valor; más datos legítimos para medir |
| **Modo de consentimiento / señales de consentimiento** | Pasas a la plataforma si el usuario aceptó o no | Modela conversiones perdidas sin violar la elección del usuario |

La paradoja útil de 2026: las marcas que cumplen bien (consentimiento claro + datos propios + server-side) terminan midiendo **MEJOR** que las que dependían de cookies de terceros que ya casi no funcionan. Cumplir es la jugada de medición, no contra ella. El que no se adapta no solo arriesga multas — mide cada vez peor mientras el rastreo de terceros se apaga.

## Checklist antes de instalar Pixel o subir datos

1. ¿Tienes política de privacidad publicada y accesible? (sí/no — si no, hazla primero).
2. ¿El formulario/checkout pide autorización de tratamiento con finalidad de marketing, con casilla NO pre-marcada? (sí/no).
3. ¿Esa autorización está documentada (sabes de dónde salió cada dato y cuándo)? (sí/no).
4. ¿Estás seguro de NO incluir datos sensibles ni de menores? (sí/no).
5. ¿Usas el flujo oficial hasheado de TikTok para subir listas? (sí/no).
6. ¿Tu política menciona que compartes datos con TikTok/Meta para publicidad? (sí/no).
7. ¿Tienes un proceso para atender solicitudes de borrado/actualización del titular? (sí/no).

Si algo es "no", resuélvelo antes de seguir. Si dudas del encuadre legal de un modelo de negocio (ej. si puedes o no captar ciertos datos), valida con `economist_lushows` la viabilidad y, para temas legales finos, **un abogado real** — esto es orientación práctica, no asesoría jurídica.

## El costo real de no cumplir

- **Multa SIC (Colombia)**: puede llegar a montos en miles de millones de pesos para casos graves; para una pyme, una sanción menor ya supera el presupuesto de pauta de meses.
- **Pérdida de la cuenta publicitaria**: TikTok y Meta suspenden cuentas que suben datos sin base legal o violan políticas de datos. Recuperarla es lento e incierto (ver el módulo de cuentas baneadas en la suite).
- **Daño de marca**: una queja pública por uso indebido de datos pesa más que cualquier campaña, sobre todo en B2B donde la confianza es el producto (ver 27).

Cumplir cuesta una tarde de configuración; no cumplir puede costar el negocio.

## Errores comunes — blacklist

1. **Subir listas de clientes sin consentimiento.** Riesgo de multa de la SIC/ANPD y de perder la cuenta publicitaria; el ahorro de "saltarse la casilla" no compensa.
2. **No tener política de privacidad publicada.** Meta y TikTok la exigen, y la ley también; sin ella estás expuesto por partida doble.
3. **Recolectar o segmentar por datos sensibles.** Prohibido; solo correo/teléfono con autorización de marketing.
4. **Casilla pre-marcada o consentimiento engañoso.** No es consentimiento válido; debe ser claro, opcional y no escondido.
5. **Mandar correos/teléfonos en claro.** Usa siempre el flujo hasheado oficial (ver 28).
6. **Creer que cumplir mata la medición.** Al revés: server-side + first-party + consentimiento miden mejor en el mundo post-cookie.
7. **Copiar la política de privacidad de otra empresa sin adaptarla.** Debe reflejar TUS datos, finalidades y a quién se los compartes.
8. **No tener proceso de borrado.** El titular puede exigir que elimines sus datos; ignorarlo es una infracción adicional.
