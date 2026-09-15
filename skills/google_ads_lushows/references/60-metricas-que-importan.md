# 60 — Métricas que importan

Lee este módulo cuando abras la cuenta y no sepas en qué columna mirar primero, cuando alguien te pregunte "¿cómo va la pauta?" y solo sepas decir "bien", o cuando tengas 40 métricas en pantalla y ninguna te diga qué hacer mañana. Aquí separamos las métricas que **deciden algo** de las que solo decoran el reporte.

Marco mental: Google Ads es **captura de intención** — alguien ya está buscando lo que vendes y tú apareces en ese momento. Meta/TikTok son **generación de demanda** (ver `facebook_ads_lushows`, `tiktok_ads_lushows`). En captura la pregunta no es "¿les gustó el anuncio?" sino **"¿aparezco cuando me buscan, me hacen clic, y compran?"**. Cada métrica de abajo responde un eslabón de esa cadena. Si no entiendes la cadena, las métricas son ruido.

## La cadena: aparecer → clic → convertir → valer

Una venta en Search pasa por cuatro filtros. Si se rompe uno, no hay venta. Las métricas siguen ese orden — esto no es decorativo, es el orden en que debes diagnosticar (ver 61).

| Métrica | Qué significa (jerga explicada) | Qué decide |
|---|---|---|
| **Search Impression Share (IS)** | "Cuota de impresiones": de todas las búsquedas donde tu anuncio era elegible, qué % apareció. 60% = apareciste en 6 de cada 10 | ¿Cubres la demanda o solo un pedazo? |
| **Lost IS (budget)** | "IS perdido por presupuesto": % de veces que NO apareciste porque se acabó la plata | Alto → falta presupuesto, no rank (ver 94) |
| **Lost IS (rank)** | "IS perdido por ranking": % que NO apareciste porque tu Ad Rank fue muy bajo | Alto → mejora puja/calidad/anuncio, no plata |
| **Top IS** | % de tus impresiones que salieron **arriba** de los resultados orgánicos | ¿Sales arriba o enterrado? |
| **Abs Top IS** | "Absolute Top IS": % en la **posición 1 absoluta** | Posición premium (marca, términos calientes) |
| **CTR** | Clics ÷ impresiones ("click-through rate") | ¿El anuncio/keyword atrae o repele? (ver 61) |
| **CPC** | Costo por clic promedio | Qué tan cara está la subasta |
| **CVR** | "Conversion rate": conversiones ÷ clics | ¿La landing/oferta convierte? (ver 61) |
| **CPA** | "Cost per acquisition": gasto ÷ conversiones | ¿Cuánto cuesta un lead/venta? |
| **ROAS** | "Return on ad spend": valor de conversión ÷ gasto. ROAS 4 = $4 por cada $1 | Rentabilidad **de plataforma** (ojo, ver 64) |
| **Conv. value** | Valor total de las conversiones (ventas, no leads) | El número que de verdad importa en e-commerce |

Las fórmulas, escritas para que las repitas de memoria:

```
IS               = impresiones tuyas ÷ impresiones elegibles
CTR              = clics ÷ impresiones
CPC              = costo ÷ clics
CVR              = conversiones ÷ clics
CPA              = costo ÷ conversiones
ROAS             = valor de conversión ÷ costo
Conv. value      = Σ (valor de cada conversión)
```

Y un puente útil: **CPA = CPC ÷ CVR**. Esto explica por qué dos palancas mueven tu costo por venta: o bajas lo que pagas por clic (CPC), o haces que más clics conviertan (CVR). Si tu CPA está caro, esa división te dice cuál de las dos está rota.

Regla de oro: **IS y Lost IS te dicen el problema de techo** (¿por qué no apareces más?); **CTR/CVR te dicen el problema de eficiencia** (¿por qué no aprovechas lo que ya aparece?). Son dos diagnósticos distintos y se arreglan distinto.

## Rangos honestos (Colombia/LatAm, orientativos — jun-2026)

No hay benchmark universal: depende de industria, marca vs genérico y competencia. Pero para que no estés ciego:

| Métrica | Pésimo | Normal | Bueno | Notas |
|---|---|---|---|---|
| Search IS (genérico) | <20% | 30–60% | >70% | En marca propia debería ser >80% (ver 39) |
| CTR Search (genérico) | <2% | 3–6% | >8% | Marca propia: 15–40% es normal |
| CTR Search (marca) | <10% | 15–30% | >40% | Si tu CTR de marca es bajo, algo raro pasa |
| CVR | <1% | 2–5% | >7% | Lead capture > e-commerce; depende de oferta |
| CPC | — | varía 10x por nicho | — | Servicios (legal/seguros) carísimos; productos baratos |

Si tu CTR de **marca** está en 8%, no celebres el "número decente": para marca eso es bajísimo, probablemente un competidor te está pujando encima (ver 94) o tu anuncio de marca es débil. Un benchmark de internet jamás reemplaza tu propio histórico: tu mejor referencia es **tu mismo número el mes pasado**.

## Cómo leerlas juntas (no aisladas) — triangulación de síntomas

Una métrica sola miente. El oficio es cruzar dos o tres y leer la historia. Ejemplos reales:

- **IS 30% + Lost IS budget 55%** → no tienes problema de calidad, tienes problema de plata. Subir presupuesto es la palanca (valida viabilidad antes: ver `economist_lushows`).
- **IS 30% + Lost IS rank 60%** → subir plata NO sirve, te ganan por Ad Rank. Trabaja puja, Quality Score y anuncio.
- **CTR alto + CVR bajo** → el anuncio promete bien pero la landing/oferta decepciona. No es problema de Ads, es de la página (ver `desingweb-lushows`) o del precio.
- **CTR bajo + CVR alto** → cuando entran, convierten; pero entran pocos. Anuncio o keyword mal alineados; pierdes volumen.
- **CPA estable + conv. value cayendo** → te entran las mismas conversiones pero valen menos (ticket más bajo, mix de producto malo). Revisa valor de conversión, no el conteo.
- **ROAS de plataforma 6 pero el banco no cuadra** → el ROAS de Ads infla (cuenta ventas que ya iban a pasar). Triangula (ver 64) y mide incrementalidad (ver 65).

Plantilla mental de lectura semanal, en este orden: **(1)** ¿la medición está sana? (ver 62) → **(2)** ¿apareciste? (IS + Lost IS) → **(3)** ¿te hicieron clic? (CTR) → **(4)** ¿convirtieron? (CVR/CPA) → **(5)** ¿valió la pena de verdad? (conv. value / ROAS triangulado, ver 64). Nunca empieces por el ROAS: es la última pregunta, no la primera.

## Métricas que importan vs métricas de vanidad

Para el reporte ejecutivo (ver 67) y para tu propia cordura, separa:

| Importan (cambian una decisión) | Vanidad (decoran) |
|---|---|
| IS, Lost IS (budget/rank) | Impresiones solas |
| CPA, ROAS triangulado, conv. value | Posición media (deprecada por Google) |
| CVR, MER (ver 64) | Clics totales sin contexto |
| Search IS por marca vs genérico (ver 39) | "Interacciones" agregadas |

Si una métrica no cambia lo que vas a hacer mañana, no es una métrica: es decoración. Guárdala en tu hoja de trabajo, no en la cara del cliente.

## Errores comunes — blacklist

1. **Mirar solo CPA/ROAS y nunca IS.** Puedes tener CPA hermoso porque solo apareces en el 15% de las búsquedas fáciles. Estás dejando ventas sobre la mesa sin verlo.
2. **No distinguir Lost IS budget vs rank.** Es el error más caro: subes presupuesto cuando el problema era rank, o peleas calidad cuando solo faltaba plata (ver 61, 94).
3. **Celebrar CTR de marca de 8% como si fuera bueno.** En marca propia eso es señal de alarma (ver 94).
4. **Confiar en el ROAS de plataforma como verdad financiera.** Está inflado por atribución; el real se triangula con backend y MER (ver 64).
5. **Comparar tu CPA con un "benchmark de internet"** sin ajustar por industria, país y marca vs genérico. Tu único benchmark válido es tu propio histórico y tu rentabilidad.
6. **Obsesionarse con Abs Top IS en términos genéricos**, pagando carísimo la posición 1 cuando la 2–3 convierte igual más barato.
7. **Optimizar conv. value sin verificar que la medición esté sana** (ver 62). Un ROAS que sube puede ser una conversión doble-contada, no más ventas.
8. **Confundir CVR baja con "Ads no sirve".** CVR baja con CTR sano casi siempre vive fuera de Ads: landing, oferta o cierre (ver `desingweb-lushows`, `ventas_lushows`).
