# La estructura para escalar (el criterio de negocio)

> **Frontera**: la arquitectura técnica de escalado —CBO/ABO, consolidación de conjuntos,
> exclusiones, ventanas de atribución, Advantage+— es mecánica de plataforma. **Para el detalle de
> configuración, invoca `facebook_ads_lushows`** o `tiktok_ads_lushows`. Aquí se decide **cuándo se
> escala, con qué munición creativa y contra qué número**.

## La pregunta que autoriza a escalar

No es "¿el ROAS es bueno?". Es: **¿el margen por pedido sigue siendo positivo después de subir el
CPA que el escalado va a provocar?**

| Concepto | Modelo México dic-2026 |
|---|---|
| ROAS de equilibrio | 1,95 |
| CAC objetivo | USD 10,54 |
| Techo de CAC | USD 30,73 |
| Holgura | 2,92x |

Escalar consume holgura. Si hoy estás en CAC 10,54 y tienes 2,92x de holgura, puedes tolerar que el
escalado te lleve a 15-18 sin morir. Si ya estás en 26, no tienes escalado: tienes una cuenta regresiva.

## Las tres condiciones para escalar

| Condición | Umbral | Por qué |
|---|---|---|
| **Consistencia** | 3 días seguidos con CPA bajo el objetivo | Un día bueno es azar |
| **Volumen mínimo** | ≥ 10-15 pedidos acumulados en el ganador | Menos que eso es ruido |
| **Munición creativa** | ≥ 3 variantes vivas del ángulo ganador (`263`) | Sin ellas el escalado dura 8 días y muere de fatiga (`264`) |

Las tres. Dos de tres no habilita. La tercera es la que más se ignora y la que más mata campañas
escaladas: subes presupuesto, el creativo se quema en una semana, y te quedas con el gasto alto y sin
qué poner.

## Las dos formas de crecer, y cuál primero

| | Vertical | Horizontal |
|---|---|---|
| Qué es | Más plata al mismo ganador | Más ganadores/ángulos/canales |
| Velocidad | Rápida | Lenta |
| Riesgo | Sube el CPA por saturación | Diluye atención y presupuesto |
| Cuándo | Primero, mientras el CPA aguante | Cuando el vertical toca techo |
| Techo | La audiencia del ángulo | Tu capacidad de producir creativo |

Orden correcto: **vertical hasta que el CPA suba 25-30% sobre el objetivo, luego horizontal**.
Detalle en `269`.

## Ritmo de escalado vertical

| Situación | Incremento | Frecuencia |
|---|---|---|
| Campaña estable, CPA 30%+ bajo objetivo | +20-30% | Cada 48-72 h |
| Campaña estable, CPA cerca del objetivo | +10-15% | Cada 72 h |
| Temporada alta con CPM subiendo (`270`) | +30-50% | Diario, vigilando margen |
| Cualquier duda | No subas | — |

Detalle de porcentajes y de por qué el sistema reacciona mal a saltos grandes: `244`.

## La estructura mental: tres cajones

Piensa tu cuenta como tres cajones con presupuestos separados, no como una lista de campañas:

| Cajón | % del presupuesto | Contenido | Métrica que lo gobierna |
|---|---|---|---|
| **Escala** | 60-70% | El ángulo ganador y sus variantes | CPA vs CAC objetivo |
| **Test** | 20-30% | Ángulos nuevos, hooks nuevos (`242`) | CTR y CPA de descubrimiento |
| **Retargeting** | 10-15% | Carrito abandonado, visitantes, compradores (`271`) | ROAS alto, volumen bajo |

Si el cajón de test se vacía porque "ahora hay que escalar", en 3-4 semanas no tienes con qué
reemplazar al ganador cuando se fatigue. El cajón de test nunca baja de 20%.

## Qué se rompe cuando escalas (y es normal)

| Se rompe | Magnitud típica | Es problema si |
|---|---|---|
| El CPA sube | +15-35% al duplicar presupuesto | Pasa el techo de CAC |
| El CTR baja | -10-25% (llegas a público menos afín) | Cae bajo 1,2% |
| El AOV baja un poco | -5-10% | Cae bajo el que sostiene el ROAS de equilibrio |
| La frecuencia sube | De 1,3 a 2,0-2,8 | Pasa de 3,0 sin variantes nuevas |

El cierre cae al escalar y **es normal**: estás comprando público menos caliente. El error es
interpretarlo como "el producto dejó de funcionar" y apagar todo.

## Escalado y operación: el cuello que nadie mira

| Volumen/día | Qué se rompe primero |
|---|---|
| 1-5 pedidos | Nada |
| 5-20 | Atención al cliente (WhatsApp sin plantillas) |
| 20-50 | Stock local y empaque; hay que reponer con 2-3 semanas de anticipación |
| 50+ | Pasarela (límites y retenciones), mensajería, devoluciones |

Escalar pauta sin escalar operación produce reseñas malas, contracargos y una cuenta de pasarela
congelada. Antes de duplicar presupuesto, pregúntate cuántos pedidos puedes despachar bien mañana.

## Cuándo NO escalar aunque los números den

| Señal | Razón |
|---|---|
| Stock para menos de 10 días al ritmo nuevo | Vender lo que no puedes entregar |
| Margen dependiente de un envío subsidiado | Se evapora con volumen |
| Un solo creativo vivo | Muere en días (`264`) |
| Semana de Black Friday con CPM 50-80% arriba y sin colchón | Ver `270` y `274` |
| Tasa de disputa o devolución > 3-4% | El volumen multiplica el problema |

## Relacionados
`242` estructura de test · `244` presupuestos y cómo subirlos · `262` volumen creativo · `263` iterar el ganador · `264` fatiga · `269` vertical y horizontal · `270` CPM de temporada
