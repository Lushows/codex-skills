# 10 — Estructura de cuenta 2026

Lee este módulo cuando vayas a armar tu cuenta de TikTok Ads desde cero, cuando tengas 8 campañas prendidas y no sepas cuál apagar, o cuando alguien te diga "crea una campaña por cada producto" y tu instinto te diga que algo huele mal. Aquí decidimos cómo se organiza el dinero para que el algoritmo aprenda en vez de adivinar. La estructura no es estética: es la cañería por donde corre la señal de conversión, y una cañería mal armada ahoga al mejor creativo del mundo.

## El frame: TikTok es DESCUBRIMIENTO, el creativo es el targeting

Antes de tocar un botón, graba esto: **en TikTok 2026 el creativo ES el targeting**. El video decide a quién le aparece tu anuncio más que cualquier público que selecciones. El algoritmo lee quién detiene el scroll, quién ve hasta el final, quién toca, quién compra — y va a buscar gente parecida. TikTok no es Google (donde la persona ya busca con intención) ni es del todo Meta (recolección): TikTok **crea el deseo** en gente que no sabía que te necesitaba. Eso cambia toda la arquitectura: en vez de fragmentar en 20 públicos, consolidas en pocas estructuras y metes volumen de creativos. La cuenta existe para alimentar creativos al algoritmo, no para micro-controlar a quién le llegan.

## La regla madre: pocas campañas, MUCHOS creativos

Por qué fragmentar te mata: cada **ad group** (grupo de anuncios, la capa donde vive el público y el presupuesto) necesita ~50 conversiones por semana del evento de optimización para salir de aprendizaje (ver 13). Si partes $80.000 COP/día en 6 ad groups, cada uno recibe ~$13.000, ninguno junta 50 conversiones, y los 6 quedan atrapados en *learning limited* (aprendizaje limitado, el sistema nunca estabiliza). Fragmentar **reparte la señal** hasta volverla ruido — y el ruido se traduce en CPA caro e inestable para siempre.

Estructura por defecto para una marca pequeña en Colombia (jun-2026):

| Capa | Cuántas | Qué define |
|---|---|---|
| Campaign | 1–2 | Objetivo (ver 11) + presupuesto si usas CBO |
| Ad group | 1–3 | Público, optimización, evento (ver 14) |
| Ad (creativo) | 6–15+ | El video. Aquí va TODO tu trabajo |

Tabla de decisión por presupuesto diario (la guía rápida que más se consulta):

| Gasto/día COP | Estructura recomendada |
|---|---|
| < $50.000 | 1 campaña Sales + 1 ad group broad + 6–10 creativos. No te compliques |
| $50.000–$300.000 | 1 campaña Sales + 1–2 ad groups (broad + retargeting) + 10+ creativos |
| $300.000–$1.000.000 | 1–2 campañas + Smart+ Web (ver 12) corriendo en paralelo a 1 manual + flujo de 2–5 creativos nuevos/sem |
| > $1.000.000 | Smart+ como motor + campaña de testing dedicada + retargeting separado (ver 18) |

Si gastas menos de ~$300.000 COP/día, casi siempre te basta **1 campaña Sales + 1 ad group broad + muchos creativos**. La consolidación no es pereza: es darle al algoritmo la masa crítica de señal que necesita.

## Campaign / Ad group / Ad: quién hace qué

- **Campaign:** define el objetivo (Sales, Leads, Traffic…) y, si activas CBO, el presupuesto. Es la "instrucción de qué quieres".
- **Ad group:** define a quién le llega (público), en qué *placement* (ubicación: TikTok feed, y opcionalmente la red de socios/Pangle), con qué puja (ver 15) y sobre qué **evento de optimización** (ver 14). Es el "cómo y dónde".
- **Ad:** el video + el copy + el CTA. Es donde se gana o se pierde la pauta — el 80% del resultado vive aquí (ver 17).

## CBO vs ABO: dónde pones el presupuesto

**CBO** = *Campaign Budget Optimization* (presupuesto a nivel campaña; TikTok reparte la plata entre ad groups según rendimiento). **ABO** = *Ad group Budget Optimization* (presupuesto fijo por ad group; tú mandas). En la interfaz 2026 TikTok lo llama "Campaign Budget Optimization" en el toggle de la campaña.

| | CBO (campaña) | ABO (ad group) |
|---|---|---|
| Quién reparte | TikTok | Tú |
| Bueno para | Escalar lo que ya jala, dejar correr | Testear con presupuesto garantizado por variante |
| Riesgo | Concentra el gasto en 1 ad group y "mata de hambre" a los otros | Sostienes ganadores muertos por terquedad |
| Cuándo | Cuenta con datos, ganadores claros | Fase de prueba, quieres dar piso parejo |

Regla práctica: **testea en ABO** (cada cosa recibe su presupuesto y comparas limpio), **escala en CBO** (dejas que el algoritmo concentre en el ganador). En Smart+ (ver 12) esta decisión la toma TikTok por ti — por eso Smart+ es el camino por defecto cuando ya tienes munición creativa y señal limpia.

## Cuándo SÍ separar en otra campaña / ad group

Separa solo cuando hay una razón **estructural**, no caprichosa. Cada separación que NO sea estructural es señal repartida:

1. **Objetivo distinto** — Sales y Leads no van en la misma campaña (optimizan eventos distintos, ver 11).
2. **Evento de optimización distinto** — *Complete payment* vs *Add to cart* viven separados (ver 14).
3. **Economía muy distinta** — un producto de $10.000 COP y uno de $400.000 COP no comparten ad group; sus CPA objetivo no se parecen y el algoritmo no puede servir a dos amos.
4. **Prospecting vs retargeting** — públicos fríos y calientes en ad groups distintos para no sobre-pagar por gente que ya te conoce (ver 18).
5. **Geografía o idioma real distinto** — Colombia vs México con creativo y precio distintos (un "parce" no le habla a un "wey").

Si la razón es "quiero ver cuál producto vende mejor", eso se resuelve con **creativos distintos dentro del mismo ad group** y mirando creative analytics (ver 68), no fragmentando la cuenta.

## Plantilla de nomenclatura (para no perderte a los 3 meses)

Cuando tengas varias campañas, nómbralas con un patrón fijo. Plantilla que funciona:

```
Campaña:  [Objetivo]_[Producto]_[Mes]   → SALES_ExcelGastro_Jun26
Ad group: [Publico]_[Evento]            → Broad_CompletePayment
Ad:       [Angulo]_[Hook]_[vNN]         → Dolor_FoodCostMata_v03
```

Así, leyendo el nombre, sabes qué hace cada cosa sin abrir nada. Esto se vuelve vital cuando escalas (ver 72) y tienes 5 ganadores corriendo.

## Errores comunes — blacklist

1. **Una campaña por producto/público "para tener control".** Repartes la señal, nadie llega a 50 conv/sem, todo queda en learning limited (ver 13).
2. **Mezclar Sales y Leads en la misma campaña** esperando que "el algoritmo entienda". Optimiza un solo evento; le das instrucciones contradictorias (ver 11).
3. **Demasiados ad groups con presupuesto chico.** $80.000/día en 6 ad groups = 6 fracasos. Mejor 1 ad group con los $80.000.
4. **Pocos creativos, muchos públicos.** Al revés de como funciona TikTok: el creativo es el targeting (ver 20). Pon 1 público broad y 10 videos.
5. **Usar CBO en fase de prueba** y luego no entender por qué TikTok solo gastó en 1 variante: CBO concentra, no reparte parejo. Para probar usa ABO.
6. **Duplicar la campaña ganadora 5 veces para escalar.** Compites contigo mismo en la subasta y subes tu propio CPM. Escala subiendo presupuesto o con CBO (ver 72).
7. **Reestructurar la cuenta cada semana.** Cada cambio grande resetea el aprendizaje (ver 13). La estructura se decide una vez y se respeta.
8. **Nombrar todo "Campaña 1", "Copia de Campaña 1".** A los 2 meses no sabes qué es qué; usa la plantilla de nomenclatura.
9. **Confundir la arquitectura con el resultado.** Una estructura perfecta con creativos malos no vende. La estructura es la cañería; el agua es el creativo (ver 17). Si dudas de la viabilidad del producto en sí, eso es `economist_lushows`, no estructura de cuenta.
