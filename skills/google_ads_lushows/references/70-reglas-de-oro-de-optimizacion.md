# 70 — Reglas de oro de optimización

Lee este módulo cuando tengas la cuenta corriendo y la mano te pique por "mejorar algo": bajar un CPA, subir presupuesto, cambiar el target. La optimización no es tocar botones todos los días — es saber **cuándo tocar y cuándo no**. En la era de Smart Bidding (la puja automática de Google que ajusta cuánto ofreces en cada subasta según la probabilidad de conversión), el error más caro no es elegir mal: es **interrumpir el aprendizaje** del sistema con cambios impacientes. La cuenta que más rinde casi nunca es la que más se toca — es la que se toca con disciplina, en los momentos correctos, con la métrica correcta delante.

Recuerda el marco: Google **captura** demanda que ya existe (alguien buscando "calculadora de costos restaurante" ya decidió que tiene el problema). No la genera — eso es Meta (ver `facebook_ads_lushows`). Por eso aquí la disciplina pesa más que la creatividad: la demanda manda, tú solo afinas la captura. Optimizar en Google es sobre todo **no estorbarle al algoritmo y darle señales limpias.**

## La disciplina del aprendizaje de Smart Bidding (jun-2026)

Cada vez que cambias el target (tCPA/tROAS) o el presupuesto de forma brusca, Google reinicia o sacude su modelo de predicción y entra en **fase de aprendizaje** (learning): unos días donde la entrega es errática, el CPA salta y los datos NO son confiables para decidir nada. Las reglas duras que en 2026 siguen siendo el estándar:

| Regla | Número real | Por qué |
|---|---|---|
| Cambio máximo de target o presupuesto de un golpe | **≤ 15–20%** | Saltos mayores recalculan el modelo desde casi cero |
| Frecuencia máxima de cambios | cada **~2 semanas** | Cambiar más seguido = vivir en aprendizaje permanente |
| Ventana para juzgar resultados | **1 ciclo de conversión completo** (ver 16-atribucion) | Nunca "lo de ayer"; el dato diario es ruido |
| Conversiones para que Smart Bidding rinda | **≥ 30/mes** por estrategia (ver 13-smart-bidding) | Con menos, el modelo tiene poca señal y oscila |
| Cuántas conversiones para decidir una puja | **15–30** acumuladas | Menos que eso, "0 conversiones" no significa nada |

El "1 ciclo de conversión" es clave: si tu cliente promedio tarda 6 días entre el clic y la compra, juzgar la campaña con 2 días de datos es como pesarte después de tomar agua. En productos de impulso baratos (la Calculadora de $10.000 COP de GastroLatam) el ciclo es casi inmediato; en servicios de ticket alto puede ser 2–4 semanas. **Conoce tu ciclo antes de juzgar nada** — míralo en GA4: tiempo medio del clic a la conversión.

## El checklist de decisión: antes de tocar CUALQUIER cosa

Pregúntate, en orden, antes de mover un dedo. Si una respuesta te frena, paras ahí:

1. **¿Tengo datos suficientes?** Mínimo 1 ciclo de conversión cerrado y, para decisiones de puja, 15–30 conversiones. Si no, no tocas: esperas.
2. **¿La conversión está midiendo bien?** Si el tracking está roto (ver 14-conversion), estás optimizando con datos basura. Verifica GA4 / Enhanced Conversions / Consent Mode v2 PRIMERO, SIEMPRE. Es la causa #1 de decisiones erradas.
3. **¿El cambio es ≤ 20%?** Si quieres subir presupuesto 50%, no: hazlo en dos o tres pasos del 20% separados por días (ver 72-esc-vertical).
4. **¿Ya pasaron ~2 semanas desde mi último cambio?** Si no, probablemente sigues en aprendizaje. Espera.
5. **¿El problema es real o es ruido?** Un día malo no es una tendencia. Mira 7–14 días, no 24 horas (ver 60-metricas, 61-diagnostico).
6. **¿Es UN solo cambio?** Nunca dos a la vez (presupuesto + target). Si haces dos, no sabrás cuál causó qué.

Si las respuestas no te dejan pasar, **la acción correcta es no hacer nada.** No hacer nada es una decisión activa y válida — la más rentable muchos días.

## Tabla de decisión: ¿qué hago hoy?

| Síntoma | NO hagas | SÍ haz |
|---|---|---|
| CPA subió ayer | Tocar puja en pánico | Esperar 3–7 días, confirmar tendencia (ver 75) |
| Campaña va bien, quiero más | Subir presupuesto +50% | Revisar IS Lost budget; subir +20% si hay espacio (ver 72) |
| Campaña "no gasta" | Subir presupuesto | Probablemente el target está muy apretado: aflojarlo (ver 74) |
| Entran búsquedas basura | Pausar la campaña | Añadir negativas (ver 22) |
| Un competidor bajó precio | Apretar tu target | Diagnosticar con Auction Insights (ver 94) |
| Quiero "resetear" el aprendizaje | Duplicar la campaña | Diagnosticar y arreglar dentro (ver 76) |

## Qué SÍ puedes tocar sin romper el aprendizaje

No todo reinicia el learning. Estos ajustes son "seguros" y puedes hacerlos con más libertad y frecuencia:

- **Negativas** (palabras clave negativas, ver 22-negativas): añadir términos basura que viste en el reporte de términos de búsqueda. Esto casi siempre ayuda, casi nunca daña. Es la optimización más rentable y más ignorada.
- **Texto de anuncios (RSA)**: probar nuevos titulares y descripciones, mejorar el Ad Strength. No toca la puja directamente.
- **Extensiones / activos** (sitelinks, llamadas, ubicaciones, imágenes): añadir mejora el Ad Rank (ver 36-QS) sin afectar el bidding.
- **Mejorar la landing** (velocidad, claridad, prueba social): sube conversión sin reiniciar nada (ver `desingweb-lushows`).

Y lo que NUNCA tocas a la ligera: target de puja, presupuesto, estrategia de puja, estructura de campañas. Esos sí reinician y cuestan días de datos. En PMax y AI Max (ver `actualizacion-2026-06`), donde el algoritmo manda aún más, la disciplina es todavía más estricta: tu trabajo es alimentarlo con conversiones limpias y activos buenos, no micro-gestionarlo.

## La cadencia sana: un calendario, no un impulso

- **Diario (2 min):** ¿algo se rompió de forma evidente? (gasto en cero, conversión en cero). Si no, no tocas.
- **Semanal:** revisar términos de búsqueda → negativas; revisar Ad Strength; ver tendencia de 7 días.
- **Quincenal:** decisiones de puja/presupuesto, con 1 ciclo de datos cerrado.
- **Mensual:** estructura, expansión (ver 73), incrementalidad si hay escala (ver 65).

Cuándo subir el caso a una hermana: viabilidad del CPA/margen → `economist_lushows`; landing que no convierte → `desingweb-lushows`; cierre del lead por WhatsApp → `ventas_lushows`; falta de DEMANDA (nadie busca) → generar en `facebook_ads_lushows` o `tiktok_ads_lushows`.

## Errores comunes — blacklist

- **Optimizar a diario mirando el dato de ayer.** Smart Bidding necesita ciclos completos; reaccionar a 24 horas garantiza que vivas en aprendizaje permanente y nunca veas el rendimiento real.
- **Cambiar target y presupuesto el mismo día.** Dos shocks juntos = aprendizaje doble y diagnóstico imposible. Un cambio, esperas, mides, luego el otro.
- **Subir presupuesto 50–100% "porque va bien".** Saltos grandes reinician el modelo; el rendimiento empeora justo cuando creías escalar (ver 72-esc-vertical).
- **Optimizar con la conversión rota.** Si GA4 o Enhanced Conversions no miden bien, todo cambio es a ciegas. Verifica el tracking antes que nada (ver 14-conversion).
- **Apretar el tCPA porque un competidor bajó precios ayer.** Reaccionar al ruido del mercado con cambios de puja te ahoga la entrega. Diagnostica primero (ver 75-troubleshoot, 94-auction-insights).
- **Borrar/pausar campañas con pocas conversiones sin darles 1 ciclo.** Matar antes de tiempo es desperdiciar el dinero ya gastado en aprendizaje (ver 71-kill).
- **Tratar la optimización como "tocar algo cada día para sentir que trabajo".** La mejor optimización muchas veces es paciencia disciplinada + negativas + mejor landing (ver `desingweb-lushows`).
- **Micro-gestionar PMax/AI Max como si fuera Search manual.** Esos formatos premian señales limpias y activos buenos, no toqueteo; pelear con el algoritmo rinde peor (ver `actualizacion-2026-06`).
