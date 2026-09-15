# 75 — Troubleshooting: CPA disparado (checklist de emergencia)

Ayer vendía, hoy no. El CPA (costo por venta/conversación) se disparó y el pánico toca la puerta. Lee este módulo EN ORDEN — los pasos van del diagnóstico más probable al menos probable, y la mitad de las veces el culpable está en los pasos 0-1, no en "el algoritmo". Trabaja la lista antes de tocar UNA sola cosa en Ads Manager. La verdad estadística de 2026: cuando un CPA estable se rompe de verdad (no por un día), **la causa #1 con enorme diferencia es FATIGA creativa** (frequency arriba, thumbstop/CTR abajo). El resto del checklist existe para descartar los autogoles y los fantasmas antes de llegar ahí.

## PASO 0 — Calma estadística: ¿es 1 día o 3+?

- **¿El CPA feo lleva 1 día?** → Es ruido con altísima probabilidad. La varianza diaria es normal (ver 70). NO toques nada. Re-evalúa mañana.
- **¿Lleva 3+ días consecutivos?** → Es señal. Continúa al Paso 1.
- Compara contra la semana pasada completa, no contra tu mejor día histórico (ese día también fue varianza, pero a favor).
- A presupuesto micro (ver 79) sube el umbral: con 2 conversiones/día, "3 días malos" todavía puede ser ruido. Mira la tendencia de 1-2 semanas.

## PASO 1 — ¿Cambió algo TUYO? (el 50% de los desastres son autogol)

Abre tu bitácora (ver 70) y responde con honestidad brutal:

- ¿Tocaste presupuesto, puja, creativo o audiencia en los últimos 3-5 días? → probable reseteo de aprendizaje (ver 13). Fix: NO toques más; espera 3-5 días a que re-estabilice. (¿Subiste el presupuesto >30%? ahí está, ver 72.)
- ¿Editaste la landing o la web? ¿Alguien más del equipo lo hizo? → revisa que cargue, que el botón funcione, que el formulario envíe.
- ¿Se acabó el stock o venció la oferta/promoción? → el anuncio promete algo que ya no existe.
- ¿Link roto? Haz clic en TU PROPIO anuncio desde el celular, ahora mismo. Recorre el flujo completo hasta el final (hasta el WhatsApp si es CTWA).
- ¿Cambió el precio, el costo de envío, el mensaje de bienvenida del bot?

Si algo de esto aparece: ahí está tu culpable. Corrige y dale 48-72h. No sigas bajando la lista "por si acaso".

## PASO 2 — ¿Medición rota? (el desastre fantasma)

Un píxel caído **parece** un desastre de CPA sin serlo: las ventas siguen ocurriendo pero Meta no las ve, así que reporta CPA infinito y además optimiza a ciegas (ver 62).

- Events Manager → tu píxel → ¿están llegando eventos HOY? Compara el volumen con el de la semana pasada.
- ¿CAPI (API de Conversiones, la medición servidor-a-servidor) caída? Revisa el estado de la integración y el EMQ (Event Match Quality, ver 06).
- Contraste rápido: ¿tus ventas/conversaciones REALES (WhatsApp, pasarela, pedidos) cayeron igual que las que reporta Meta? Si vendes igual pero Meta reporta cero → es medición, no rendimiento. Arregla el píxel ANTES que cualquier otra cosa.

## PASO 3 — ¿Plataforma?

- **¿Anuncio desaprobado o "entrega limitada"?** Revisa la columna de entrega de cada ad. Un ganador desaprobado deja todo el gasto en los mediocres.
- **¿Learning reset visible?** Columna "Entrega" dice "En aprendizaje" en un ad set que llevaba semanas estable → algo lo reseteó (ver Paso 1).
- **¿Evento de optimización mal configurado?** Revisa que el ad set siga optimizando por el evento correcto (ver 14); un cambio accidental de evento dispara el CPA reportado.
- **Account Quality** (calidad de la cuenta): ¿restricciones, advertencias, anuncios rechazados acumulados? (ver 08, 93).

## PASO 4 — ¿Mercado / subasta? (mira Auction Insights)

- **¿Subió el CPM de TODA la cuenta** (no solo una campaña)? CPM = costo por mil impresiones, el precio del inventario. CPM general arriba ≠ tú hiciste algo mal — el inventario se encareció.
- **Auction Insights / competencia**: revisa Ad Library de tus competidores (ver 94). ¿Alguien nuevo pujando fuerte en tu nicho? Más competidores en tu subasta = CPM arriba sin que tú cambiaras nada.
- **Temporada**: fechas calientes (BF, madrugón, día de la madre, navidad, prima de diciembre, ver 19 y 77) inflan CPMs 30-80%.
- **Evento país**: elecciones, paro, partido de la selección, tragedia nacional → la atención se va a otro lado por días.
- **Estacionalidad de demanda**: ¿tu producto simplemente vende menos esta época? (paraguas en verano). No es la pauta, es el calendario.
- Fix realista: aguantar, ajustar oferta, o pausar hasta que pase si el margen no resiste. El mercado no se "optimiza".

## PASO 5 — ¿Fatiga? (la causa más probable de todas)

- **Frequency** (veces promedio que cada persona vio tu anuncio) subiendo + **CTR / thumbstop** bajando, en un anuncio con semanas corriendo → fatiga creativa clásica (ver 39). La misma gente ya vio tu anuncio demasiadas veces y dejó de frenar el scroll.
- Señal dura: frequency >2.5-3 en 7 días con CTR cayendo respecto a su línea base.
- Fix: creativos nuevos / ángulos nuevos (ver 38, 73), no más presupuesto al fatigado. Subirle plata a un ad fatigado solo acelera la quema.
- Si llegaste hasta aquí y los pasos 0-4 no encontraron nada, este es tu culpable en ~70% de los casos. Empieza a producir.

## Tabla diagnóstico → acción

| Paso | Síntoma | Fix | Módulo |
|---|---|---|---|
| 0 | 1 solo día malo | Nada. Esperar. | 70 |
| 1 | Cambio reciente en bitácora / link roto / sin stock | Corregir el autogol; esperar 48-72h | 70, 13 |
| 2 | Events Manager sin eventos; ventas reales OK | Reparar píxel/CAPI ya | 62, 06 |
| 3 | Ad desaprobado / learning reset / evento mal / cuenta restringida | Apelar/corregir; revisar Account Quality | 08, 93, 14 |
| 4 | CPM de toda la cuenta arriba / competidor nuevo | Aguantar o ajustar oferta; no es tu culpa | 19, 77, 94 |
| 5 | Frequency ↑ + CTR/thumbstop ↓ en ads viejos | Refresh creativo (causa #1) | 39, 38, 73 |

## Qué NO hacer en pánico

- **Apagar todo**: reseteas el aprendizaje de campañas que mañana iban a estar bien (si era ruido del Paso 0, acabas de pagar doble).
- **Cambiar 5 cosas a la vez**: presupuesto + creativo + audiencia + puja en una noche = jamás sabrás cuál era el problema, y sumaste 4 reseteos.
- **Duplicar campañas como pollo sin cabeza**: clones nuevos en learning compitiendo entre sí contra el mismo público = CPMs aún más caros.
- **Bajar el precio a lo loco**: decisión de negocio tomada en pánico a las 11pm. Consulta el margen primero (skill **economist_lushows**).
- **Saltar directo al Paso 5** sin descartar 0-4: a veces sí es fatiga, pero matar el creativo cuando el culpable era un píxel caído no arregla nada.

## Errores comunes — blacklist

- Saltarse el Paso 0 y "arreglar" un día de ruido.
- No revisar la bitácora (o peor: no tener bitácora) y culpar al algoritmo del propio autogol.
- No probar el link/flujo propio desde un celular real.
- Confundir píxel caído con campaña muerta y matar campañas sanas.
- Ignorar el CPM de cuenta y "optimizar" contra una subida de mercado.
- Apagar un ganador histórico el primer día malo.
- Diagnosticar y aplicar 3 fixes simultáneos "por si acaso".
- Olvidar que la fatiga creativa es la causa #1 y perder días buscando culpables exóticos.
