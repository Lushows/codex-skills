# 19 — Calendario y estacionalidad LatAm

Lee este módulo cuando estés planeando el año, cuando se acerque una fecha fuerte (madres, BFCM, navidad) y no sepas cómo preparar las campañas, o cuando tu CPA se disparó un día sin razón aparente (pista: probablemente un pico estacional movió la subasta, ver 01). La demanda en Google **sube y baja con el calendario**, y como Google captura demanda existente, tu trabajo es estar listo cuando esa demanda llega — y no malgastar cuando se va. Smart Bidding se adapta solo a la mayoría de los ciclos, pero los **picos cortos y predecibles** sí requieren tu mano.

## Fechas clave Colombia / LatAm 2026 (con contexto de pauta)

| Fecha | Cuándo (2026) | Qué pasa en la subasta | Acción |
|---|---|---|---|
| **Día de la Madre (CO)** | Domingo **10 de mayo** | Pico fuerte de regalos; competencia y CPCs altos | Campañas/ofertas específicas 2-3 sem antes |
| **Día del Padre (CO)** | Domingo **21 de junio** | Pico medio | Igual que madres, menor intensidad |
| **Prima de mitad de año** | Pago hasta **30 junio** | Sube poder de compra; más demanda | Sube presupuesto, prepara oferta |
| **Amor y Amistad (CO)** | Sábado **19 de septiembre** | El "San Valentín" colombiano; pico de regalos | Oferta de regalo; empieza 2 sem antes |
| **Día sin IVA (CO)** | Fechas que fija el gobierno (1-2/año, suelen anunciarse con semanas) | Pico altísimo de retail; CPCs caros | Solo si tu producto califica; presupuesto extra ese día |
| **Halloween** | 31 octubre | Pico de disfraces, dulces, fiestas, restaurantes | Según sector |
| **Black Friday / Cyber Monday** | Vie **27** + Lun **30 de noviembre** | El pico más caro y competido del año | Plan dedicado (ver 77) |
| **Navidad / fin de año** | Dic 1-24 | Demanda alta sostenida; sube CPC | Presupuesto alto todo diciembre |
| **Prima de fin de año** | Pago hasta **20 diciembre** | Segundo golpe de poder de compra | Mantén presupuesto alto |
| **Día de Reyes** | 6 enero | Última ola de regalos (LatAm) | Cierre de temporada |
| **Regreso a clases** | Ene-feb (CO) | Útiles, uniformes, tecnología, gastronomía escolar | Según sector |
| **Quincenas** | 15 y 30 de cada mes | Micro-picos: la gente compra cuando le pagan | Sube presupuesto en quincenas si tu producto lo siente |

**Contexto LatAm clave:** el ciclo de **quincena** (pago los días 15 y 30, y a fin de mes) marca micro-estacionalidad mensual **real** en Colombia. Mucha conversión se concentra esos días; las búsquedas de compra suben y los carritos abandonados a mitad de quincena se cierran cuando entra el sueldo. No es folclore: míralo en tu reporte de horas/días (ver 60) y ajústalo. Para un negocio gastronómico, además, pesan los **fines de semana, quincenas y fechas de celebración** más que las de regalo.

## Seasonality adjustments de Smart Bidding

Para picos **cortos y conocidos** (1-7 días: día sin IVA, BFCM, lanzamiento) existen los **seasonality adjustments** (ajustes de estacionalidad): le avisas a Smart Bidding "en estas fechas espero una tasa de conversión X% más alta/baja" y el algoritmo **puja más agresivo desde el inicio del evento** en vez de tardar días en darse cuenta y perder la ola.

| Característica | Detalle |
|---|---|
| Para qué sirve | Eventos **cortos** (≤7 días) con cambio brusco esperado de conversión |
| Para qué NO sirve | Cambios largos o graduales (temporada navideña entera) — Smart Bidding ya los aprende solo |
| Cómo se usa | Defines fechas + % de ajuste de conversion rate esperado + campañas afectadas |
| Cuándo configurarlo | **Antes** del evento, no durante |
| Riesgo si abusas | Lo metes para todo y desinformas al algoritmo; úsalo solo en picos genuinos |

**No uses seasonality adjustment para diciembre entero** — eso Smart Bidding lo digiere solo. Úsalo para el **día sin IVA** o el **Black Friday**: 24-48h donde la conversión se multiplica y no quieres que el algoritmo reaccione tarde. Y recuerda: el seasonality adjustment es **mejor que mover el tCPA a mano**, porque ajustar el target a mano resetea aprendizaje justo cuando necesitas estabilidad (ver 13, 15). Hay también **data exclusions** (excluir datos) para lo contrario: si tuviste un día roto de tracking, le dices al algoritmo "ignora esas conversiones" para que no aprenda basura.

## Planear el año: el ritmo de trabajo

1. **Marca el calendario** con las fechas de arriba según tu sector (un restaurante siente Amor y Amistad, diciembre, fines de semana y quincenas; un B2B siente menos los regalos, más las primas y el arranque de año).
2. **2-3 semanas antes** de un pico: prepara oferta, creativos y landing (rutea diseño a `desingweb-lushows`, marca/arte a `directorcreativo_lushows`, guion de oferta a `ventas_lushows`).
3. **No lances cambios grandes justo antes del pico**: la fase de aprendizaje (~2 semanas, ver 13) te dejaría volátil en el peor momento. **Estabiliza antes**: si vas a lanzar una campaña nueva para navidad, lánzala a inicios de noviembre, no el 1 de diciembre.
4. **Sube presupuesto en escalones** entrando al pico (≤20-30% por paso), no de golpe (ver 18, 74).
5. **Configura el seasonality adjustment** para los picos cortos, días antes.
6. **Post-pico**: la demanda cae; baja presupuesto a tiempo para no pagar CPCs altos sin la conversión que los justificaba. El 1-2 de enero y el lunes después de BFCM son trampas de gasto sin retorno.
7. Cuida la **atribución**: en picos con ciclo de decisión más largo (regalos caros que se piensan), amplía la ventana de conversión si la compra tarda (ver 16, 58).

### Cronograma tipo para un pico (ej. Amor y Amistad)

| Semanas antes | Acción |
|---|---|
| 3-4 | Definir oferta, brief de creativo y landing; estabilizar campañas (sin cambios grandes nuevos) |
| 2 | Subir genérico, lanzar grupo/anuncio de la oferta, primer escalón de presupuesto |
| 1 | Configurar seasonality adjustment si el pico es corto; segundo escalón de presupuesto |
| Día(s) del pico | Vigilar gasto e impression share; no tocar el target |
| Después | Bajar presupuesto, apagar grupo de oferta, volver a baseline |

## Errores comunes — blacklist

- **Llegar tarde al pico**: preparas la oferta el mismo día de madres en vez de 2-3 semanas antes; pierdes la ola.
- **Lanzar campaña nueva 3 días antes de BFCM**: entra en aprendizaje y va volátil en el día más caro del año (ver 13, 77).
- **Usar seasonality adjustment para temporadas largas** (diciembre entero): desinformas al algoritmo que ya sabía adaptarse solo.
- **Mover el tCPA a mano para el pico** en vez de usar seasonality adjustment: reseteas aprendizaje cuando más necesitas estabilidad (ver 15).
- **No bajar presupuesto post-pico**: sigues pagando CPCs inflados cuando la demanda ya se fue (ver 18).
- **Ignorar las quincenas** en Colombia: hay micro-picos reales los 15 y 30 que no estás aprovechando (ver 60).
- **Subir el presupuesto +300% de golpe** para el pico: reseteas aprendizaje justo cuando necesitas estabilidad (ver 13, 74).
- **Mismo presupuesto todo el año** ignorando el calendario: gastas igual en temporada muerta que en pico, desperdiciando en ambos extremos.
- **No usar data exclusions** tras un día de tracking roto: el algoritmo aprende de conversiones fantasma y se descalibra.
