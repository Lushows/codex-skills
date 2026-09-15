# 12 — Advantage+ Sales (ex Advantage+ Shopping / ASC)

La campaña de ventas hiper-automatizada de Meta: tú pones país, presupuesto y creativos; el algoritmo decide targeting, placements (ubicaciones donde aparece el anuncio) y reparto interno. Lee este módulo si tienes e-commerce y estás decidiendo entre automatizar o ir manual, o si tu campaña automatizada actual rinde raro.

> ⚠️ **Cambio de nombre 2026:** en feb-2026 Meta **fusionó ASC dentro del flujo unificado de Sales** y lo rebautizó **Advantage+ Sales** (ver 90 y `actualizacion-2026-06`). Ya no eliges "ASC vs manual" como dos botones: creas una campaña de **Sales** y la automatización viene **encendida por defecto, sección por sección** (audiencia, placements, presupuesto), con opción de **apagar** cada parte (opt-out). Una campaña de Sales "con todo en Advantage+" ES lo que antes llamábamos ASC. En este manual seguimos usando "Advantage+ Sales" para el caso totalmente automatizado.

## Qué cedes y qué ganas

| Pierdes | Ganas |
|---|---|
| Control de audiencias (no hay targeting manual, solo geo + edad mínima) | Algoritmo explora TODO el inventario de audiencias vía GEM (ver 92) |
| Breakdown fino (no ves rendimiento por interés/segmento) | Eficiencia: típicamente CPA igual o 5-15% mejor que manual equivalente* |
| Exclusiones detalladas | Setup en 10 minutos, menos micro-management |
| Separación prospecting/retargeting (mezcla ambos) | El **cap de clientes existentes** como único control de esa mezcla |

*Rango honesto: depende de la cuenta; en cuentas con poca señal puede rendir igual o peor que una manual broad. No es magia, es la misma subasta con menos palancas para que tú te equivoques.

## Cuándo usar Advantage+ Sales

- **Sí**: e-commerce con píxel/CAPI sazonado (≥30-50 compras/semana históricas), catálogo conectado, y capacidad de alimentar **10-20+ creativos distintos** con historial. Brilla con volumen de señal y de creativos (el creativo es el targeting, ver 30).
- **Sí, como campaña única**: si tu operación es simple (un país, un catálogo, un funnel), una sola Advantage+ Sales con todos tus creativos puede SER tu cuenta entera + un ad set de testing aparte (ver 17).
- **Todavía no**: cuenta nueva sin compras registradas, venta por WhatsApp sin eventos de compra (usa CTWA, ver 50), o presupuesto < ~$1M COP/mes (una manual broad consolidada hace lo mismo, ver 10).

## Cap de clientes existentes (existing customer budget cap)

Advantage+ Sales mezcla gente nueva y clientes actuales. Sin control, puede gastar 30-40% en gente que ya te compraba — ROAS lindo, crecimiento falso (auto-atribución, ver 16 y 24).

> 🔁 **Cambio 2026:** Meta ahora **sugiere un cap por defecto del 25-30%** para clientes existentes (antes lo dejaba abierto). Bájalo si quieres prospecting más puro. Configúralo así:

1. Ads Manager → Configuración de cuenta → **Audiencia de clientes existentes**: asigna una Custom Audience (lista de clientes subida con buen match, o evento Purchase 180d).
2. En la campaña, define el **cap**: % máximo de presupuesto para esos clientes. Receta: **0-10%** si quieres prospecting puro y estás escalando; 20-25% si tu producto tiene recompra fuerte (cosméticos, consumibles, café) y quieres reactivarlos dentro de la misma campaña.
3. Revisa el breakdown **"Audience segments"** (nuevo vs existente) semanalmente: es de los pocos desgloses que esta campaña sí te da, y es oro para saber si estás creciendo o reciclando.

## Cómo estructurar creativos dentro de la campaña

- Carga **10-20 anuncios activos** mínimo; el algoritmo reparte por rendimiento, los malos mueren solos sin resetear nada.
- **Diversidad real, no 12 variantes del mismo video** (Meta los colapsa bajo el mismo Entity ID, ver 10 y 30): mezcla UGC (contenido estilo usuario), demo de producto, testimonio, oferta directa, catálogo dinámico, before/after (ángulos en 30 y 41).
- Mete los ganadores de tu campaña de testing aquí; Advantage+ Sales es la "liga profesional", el testing pasa afuera (ver 17).
- Renueva **2-4 creativos al mes**: la fatiga creativa (ver 39) es la causa #1 de decaimiento, y los ganadores duran 2-4 semanas.

## Tabla de decisión: ¿automatizo o voy manual?

| Tu situación | Recomendación |
|---|---|
| ≥50 compras/sem, catálogo, 15+ creativos | Advantage+ Sales como campaña principal |
| 20-50 compras/sem | Advantage+ Sales + 1 manual broad de comparación, mide backend |
| < 20 compras/sem | Manual broad consolidada (más control mientras hay poca señal) |
| Venta por WhatsApp sin Purchase | Ni una ni otra: CTWA (ver 50) |
| Cuenta nueva, 0 compras | Manual broad o CTWA hasta tener señal |

## Automatizado vs manual broad en 2026: diferencias reales

Cada vez menores. Una campaña de Sales con audiencia **Advantage+ apagada y broad manual** (solo geo + edad) + Advantage+ placements es ~90% lo mismo que la totalmente automatizada. Diferencias que quedan: el cap de clientes existentes (solo en el flujo Advantage+ completo), límites de edad/género más finos en manual, exclusiones de audiencia en manual, y reporting algo distinto. Estrategia común en cuentas medianas/grandes: **Advantage+ Sales + 1 manual broad en paralelo**, comparando CPA real de backend (ver 16); quédate con la que gane o mantén ambas si no se canibalizan (revisa solapamiento de gasto vs resultados totales del negocio).

## Setup paso a paso

1. Crea campaña → objetivo **Sales** → deja la configuración Advantage+ encendida (revisa sección por sección qué dejas auto y qué apagas, ver 90).
2. Geo: Colombia (o ciudades si solo despachas a algunas — contraentrega manda).
3. Evento: **Purchase** (o tu proxy si no hay volumen, ver 14). Atribución default **7d-click / 1d-view** (ver 16; recuerda que en ene-2026 quitaron view-through del API, solo queda clic en reportes API).
4. Presupuesto diario: arranca con ≥ 3-5× tu CPA esperado/día. Puja: **Highest volume** para descubrir tu CPA; pasa a Minimum ROAS / ROAS Goal solo cuando tengas valor limpio y volumen (ver 15).
5. Define el cap de clientes existentes (paso anterior) — no lo dejes en el default sin pensarlo.
6. Carga 10+ creativos distintos con copy y links verificados (UTMs incluidos, ver 60).
7. No toques nada por 5-7 días salvo errores obvios. Evalúa con backend (ver 16), no solo con Ads Manager.

## Errores comunes — blacklist

- Lanzar con 3 creativos: le diste un Ferrari sin gasolina; GEM no tiene con qué explorar audiencias.
- Cargar 12 creativos casi idénticos: colapsan en un Entity ID, crees que diste variedad y no.
- Advantage+ Sales en cuenta nueva sin compras: no hay señal que automatizar; empieza manual broad o CTWA.
- Dejar el cap de clientes existentes en el default 25-30% sin revisarlo y celebrar ROAS inflado por recompradores.
- Apagar la campaña a los 3 días porque "no vende": las primeras conversiones tardan; evalúa a los 7 días con gasto suficiente (≥3× CPA, ver 13).
- Duplicar la campaña para escalar: sube el presupuesto de la existente ≤20% cada 72h (ver 13 y 72).
- Meter el creativo nuevo sin probar directo a la campaña principal y contaminarla: testea aparte primero (ver 17).
- Pelear contra el opt-out apagando TODO Advantage+ por costumbre: en 2026 la audiencia automática suele ganarle a tu segmentación manual; apaga con criterio (ver 90).
