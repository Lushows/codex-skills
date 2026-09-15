# 75 — Troubleshooting CPA disparado

Lee este módulo cuando una campaña que venía bien de repente se daña: el CPA se duplicó, el ROAS se cayó, las ventas se secaron — y no sabes por qué. La regla #1: **no toques las pujas en pánico.** Cambiar el target o el presupuesto antes de diagnosticar suele empeorar todo (metes la campaña en aprendizaje encima del problema). Primero diagnosticas, luego actúas. Este es el checklist en orden, de la causa más común a la menos.

Antes de empezar: confirma que es una **tendencia real** (3–7 días), no un día malo aislado. El rendimiento diario oscila muchísimo (ver 60-metricas). Si es solo ayer, espera y vuelve a mirar. Marco: Google captura demanda; un CPA disparado casi siempre es una de seis cosas concretas, y cinco de las seis NO se arreglan tocando la puja.

## El checklist de diagnóstico (en orden de frecuencia)

| # | Revisa | Dónde / qué buscar | Si es esto, haces |
|---|---|---|---|
| 1 | **Conversión rota** | GA4, Enhanced Conversions, Consent Mode, tag disparando | Arreglar tracking — NUNCA optimices a ciegas |
| 2 | **Landing caída/lenta** | Abre la página tú mismo, en móvil; velocidad | Avisar/arreglar web (`desingweb-lushows`) |
| 3 | **Search terms basura** | Reporte de términos de búsqueda (broad/PMax/AI Max) | Añadir negativas (ver 22-negativas) |
| 4 | **IS Lost subió** | Impression Share perdido (rank vs budget) | Ver causa abajo |
| 5 | **Competidor nuevo** | Auction Insights (ver 94) | Defender QS/puja o aguantar |
| 6 | **Seasonality** | Calendario, fechas, contexto | Esperar / ajustar (ver 77-Q4) |

### 1. ¿La conversión se rompió? (la causa #1, de lejos)
Lo más frecuente y lo más engañoso: el CPA no subió — **dejaste de registrar conversiones** que sí ocurren. Un cambio en la web, un tag que se cayó, GA4 reconfigurado, Consent Mode v2 mal puesto, un deploy que rompió el evento de compra. Síntoma típico: las conversiones caen a casi cero de un día para otro mientras el tráfico (clics/impresiones) sigue igual. **Verifica GA4 y Enhanced Conversions ANTES que nada** (ver 14-conversion). Cómo confirmar rápido: usa Google Tag Assistant / la vista en tiempo real de GA4 y haz tú mismo una conversión de prueba. Si optimizas con la conversión rota, todo lo que hagas es a ciegas.

### 2. ¿La landing está caída o lenta?
Ábrela tú mismo, en móvil, con datos (no solo wifi). Si no carga, carga lento (>3–4 s), da error, o le cambiaron algo (formulario roto, botón de pago caído, pop-up que tapa el CTA), el tráfico llega pero no convierte — y el CPA se dispara aunque la campaña esté perfecta (ver `desingweb-lushows`). Revisa también si hubo un deploy reciente en la web que coincida con la fecha del problema.

### 3. ¿Los términos de búsqueda se llenaron de basura?
Mira el reporte de términos de búsqueda. Con concordancia amplia (broad), PMax o **AI Max for Search** (la capa de IA 2026 que expande concordancia, ver `actualizacion-2026-06`), Google a veces empieza a traer búsquedas irrelevantes que gastan sin convertir. Síntoma: clics arriba, conversiones igual o abajo, CTR raro. Solución: añadir negativas a los términos basura (ver 22-negativas). Esto es mantenimiento normal, especialmente en broad/PMax/AI Max — revísalo semanal, no solo cuando explota.

### 4. ¿Subió tu Impression Share perdido?
Si el IS Lost por **rank** subió, alguien te está ganando las subastas (peor posición → peores clics → peor CPA, o QS que bajó). Si subió el IS Lost por **budget**, te quedaste corto de presupuesto en horas clave y solo apareces para las búsquedas más caras (ver 72-esc-vertical). Distinguir cuál subió te dice si el problema es competitividad (rank) o plata (budget).

### 5. ¿Entró un competidor nuevo?
Abre **Auction Insights** (ver 94-auction-insights): muestra con quién compartes subastas y su Impression Share. Si apareció un competidor nuevo o uno subió su agresividad, los CPCs suben para todos. No siempre hay "solución" inmediata — a veces toca defender Quality Score (ver 36-QS), mejorar la oferta/landing, ajustar el target con disciplina, o aceptar que la subasta se encareció estructuralmente.

### 6. ¿Es seasonality?
¿Llegó temporada alta/baja? ¿Quincena, fin de mes, festivo colombiano, prima de diciembre, Black Friday, Hot Sale? Los CPCs y la conversión cambian con el calendario (ver 19-calendario, 77-Q4). A veces el "problema" es que el mercado entero se movió y no hay nada roto — el CPA mayor en temporada puede seguir siendo rentable si la conversión acompaña.

## Árbol de decisión rápido

| Lo que ves | Causa más probable |
|---|---|
| Conversiones se cayeron, tráfico igual | Conversión rota (1) o landing (2) |
| Clics subieron, conversiones igual | Search terms basura (3) |
| CPC subió, todo lo demás igual | Competidor (5) o seasonality (6) |
| Impresiones cayeron | IS Lost rank/budget (4) o target muy apretado (ver 74) |
| Todo cayó de golpe en una fecha | Deploy de web / tag roto (1, 2) |

## La regla: diagnostica, no dispares

El orden importa porque **arreglar la causa equivocada empeora**. Si subes el presupuesto porque "el CPA está caro" pero el problema real era la conversión rota, ahora gastas más con tracking malo. Si aprietas el target por un competidor nuevo, ahogas la entrega. Encuentra la causa, arregla **esa**, y solo entonces —si hace falta— ajusta pujas con disciplina (pasos ≤20%, ver 70-reglas, 74-tROAS-escalar). Si el problema es que los leads llegan bien pero no cierran, no es Google: es cierre (ver `ventas_lushows`). Si el CPA viable simplemente no existe para tu margen, es viabilidad (ver `economist_lushows`).

## Errores comunes — blacklist

- **Tocar las pujas/presupuesto en pánico antes de diagnosticar.** Metes la campaña en aprendizaje encima del problema real; ahora tienes dos problemas (ver 70-reglas).
- **No revisar la conversión primero.** La causa #1 de "CPA disparado" es tracking roto, no la campaña. Verifica GA4/Enhanced Conversions antes de nada (ver 14-conversion).
- **Reaccionar a un solo día malo.** Confirma tendencia de 3–7 días; el ruido diario imita una crisis (ver 60-metricas).
- **Ignorar el reporte de términos de búsqueda.** En broad/PMax/AI Max la basura se acumula sola; sin negativas el CPA se infla solo (ver 22-negativas).
- **Olvidar mirar la landing.** Una web caída o lenta dispara el CPA sin que la campaña tenga culpa (ver `desingweb-lushows`).
- **No usar Auction Insights.** Te pierdes que un competidor nuevo encareció toda la subasta y culpas a tu configuración (ver 94-auction-insights).
- **Confundir seasonality con avería.** A veces nada está roto: el mercado se movió. Ajustar agresivo contra el calendario quema plata (ver 77-Q4).
- **Duplicar la campaña para "empezar limpio".** No diagnostica nada y tiras el aprendizaje pagado; arregla la causa dentro de la campaña (ver 76-mitos).
