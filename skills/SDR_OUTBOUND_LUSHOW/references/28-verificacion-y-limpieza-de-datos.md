# 28 — Verificación y limpieza de datos

Antes de que un solo correo salga, tu lista pasa por el filtro de higiene: **verificar** que cada correo existe y **limpiar** duplicados, roles genéricos y basura. Este paso invisible es el que protege tu deliverability (que tus correos lleguen a la bandeja y no a spam, ver `40`): un rebote alto le grita a Gmail/Outlook "este que envía es un spammer" y te hunde para siempre. Saltarte la verificación es la forma #1 de arruinar un dominio recién calentado (`43`). Este módulo: qué verificar, con qué herramientas y el estándar de limpieza antes de enviar.

## El principio: el bounce rate mata la reputación

**Bounce (rebote)** = el correo no se pudo entregar. Dos tipos:
- **Hard bounce:** la dirección no existe / rechazo permanente. El veneno — cada uno le dice a los proveedores que no cuidaste tu lista.
- **Soft bounce:** rechazo temporal (buzón lleno, servidor caído). Menos grave.

Los proveedores de correo miden tu **bounce rate** como señal de salud. Umbral crítico: mantén el **hard bounce < 2–3 %** por campaña. Por encima, tu **inbox placement** (cuánto llega a bandeja principal) se desploma y puedes terminar en **blacklists** (`46`, `114`). Verificar baja el bounce de ~10–20 % (lista cruda) a <2 % (lista limpia). No es opcional.

## Los estados de un correo (qué te devuelve el verificador)

| Estado | Qué significa | Acción |
|---|---|---|
| **Valid / Deliverable** | Existe y acepta correo | Enviar ✅ |
| **Invalid / Undeliverable** | No existe → hard bounce seguro | **Descartar** ❌ |
| **Catch-all / Accept-all** | El servidor acepta TODO sin confirmar si la casilla existe | Zona gris — ver abajo |
| **Risky / Unknown** | No se pudo determinar | No enviar, o reverificar con otro proveedor |
| **Role / Genérico** | `info@`, `ventas@`, `soporte@` (no es una persona) | Segmentar aparte; menor prioridad |
| **Disposable** | Correo temporal/basura (mailinator, etc.) | Descartar |

### El problema del catch-all
Un dominio **catch-all** acepta cualquier dirección (`loquesea@dominio.com`), así que el verificador **no puede confirmar** si el correo real existe. Muchos dominios corporativos son catch-all. Qué hacer:
- **No los mezcles** con los "valid" limpios en el mismo envío inicial.
- Envíales en un segmento aparte, con volumen bajo, después de tener buena reputación.
- Un verificador bueno (o un waterfall, `130`) reduce la incertidumbre; herramientas como MillionVerifier tienen un modo específico para catch-all.

## Las herramientas de verificación

| Herramienta | Fuerte en | Precio aprox. 2026 |
|---|---|---|
| **NeverBounce** | Precisión alta, integra con casi todo, verificación en tiempo real | ~$0,003–0,008/correo, packs |
| **ZeroBounce** | Verificación + scoring de actividad + detección de abuse/spam-trap | Pago por créditos, ~$16/2k |
| **MillionVerifier** | Barato, bueno con **catch-all**, ilimitado en planes anuales | Muy económico por volumen |
| **Bouncer** | Preciso, GDPR-friendly (Europa) | Por créditos |
| **Verificador nativo de Apollo/Instantly/Smartlead** | Ya integrado en tu flujo de envío | Incluido/créditos |

Recomendación: **MillionVerifier** por costo/volumen para limpiar listas grandes; **NeverBounce/ZeroBounce** cuando quieres máxima precisión o scoring extra. Idealmente verifica **doble** (dos proveedores) los correos clave/caros de tu tier A (`16`).

## Limpieza completa — checklist antes de enviar

Verificar el correo es solo una parte. La higiene total de la lista:

```
[ ] 1. Deduplicar por correo Y por dominio (no escribas 2 veces a la misma persona
       ni satures la misma empresa con 5 correos a la vez).
[ ] 2. Verificar todos los correos → quitar INVALID y DISPOSABLE.
[ ] 3. Separar CATCH-ALL en su propio segmento (envío cauto).
[ ] 4. Separar ROLE/genéricos (info@, ventas@) → menor prioridad.
[ ] 5. Normalizar: tildes/ñ fuera, minúsculas, sin espacios, formato E.164 en teléfonos.
[ ] 6. Quitar la lista de SUPRESIÓN (quien pidió opt-out, clientes actuales,
       competidores, correos que ya rebotaron antes). Ver `49`.
[ ] 7. Validar campos mínimos llenos (nombre, empresa, ángulo de personalización).
[ ] 8. Marcar email_status en cada fila (valid/catch-all/role/invalid).
```

La lista de **supresión** (supression list) es crítica: nunca re-contactes a quien rebotó o pidió salir; guárdalos en una hoja aparte y crúzala en cada campaña.

## Ejemplo real: limpieza de una lista scrapeada de 1.200

```
Lista cruda scrapeada (Maps + Apollo) = 1.200 correos.
1. Dedup por correo/dominio → 1.050.
2. MillionVerifier → Valid 640 | Catch-all 260 | Invalid 120 | Role 30.
3. Descartar 120 invalid. Role (30) a segmento aparte.
4. Envío 1 (semana 1): SOLO los 640 valid, en dominios calentados (`43`).
   Bounce esperado < 2%. ✅
5. Catch-all (260): segmento 2, envío cauto tras 2 semanas de buena reputación.
Resultado: proteges el dominio y no quemas 3 semanas de warmup.
```

## Errores comunes (qué NO hacer)

- **Enviar sin verificar** "porque son pocos" → un puñado de hard bounces basta para dañar un dominio nuevo.
- **Mezclar catch-all con valid** en el primer envío de un dominio recién calentado.
- **No deduplicar** → la misma empresa recibe 4 correos = queja de spam.
- **Verificar una vez y reusar la lista 6 meses después** → los datos caducan (~30 %/año); reverifica (`139`).
- **Ignorar la lista de supresión** → re-contactas a quien pidió salir = queja/legal (`49`).

## Siguiente paso

Con la lista verificada y segmentada (valid / catch-all / role), enriquécela para personalizar el mensaje (`29`), luego configura el envío seguro: dominios (`41`), warmup (`43`) y volumen (`44`). El estándar completo de deliverability arranca en `40`. Recuerda: verificar es de la máquina; **cerrar** al que responde → `ventas_lushows`.
