# 74 — tROAS/tCPA para escalar

Lee este módulo cuando quieras crecer en volumen **sin perder el control de la rentabilidad**. El tCPA (target CPA: el costo por conversión que le pides a Google) y el tROAS (target ROAS: el retorno por peso gastado que le exiges) son las dos palancas con las que le dices a Smart Bidding qué tan agresivo o conservador ser. Entender cómo mover el target es lo que separa al que escala con cabeza del que sube presupuesto a ciegas y se sorprende cuando el CPA explota.

La relación fundamental, que hay que tatuarse:

> **Aflojar el target = más volumen + más CPA. Apretar el target = menos CPA + menos volumen.**

No hay almuerzo gratis. Pedirle a Google más ventas por el mismo dinero es físicamente imposible: la demanda de alta intención es finita (Google captura, no genera — ver `facebook_ads_lushows`). Para conseguir más volumen, Google tiene que entrar a subastas más caras o menos calificadas, y eso sube el costo por conversión.

## tCPA vs tROAS: cuál usar

| Estrategia | Le dices a Google | Úsala cuando | Ejemplo |
|---|---|---|---|
| **tCPA** | "Consígueme conversiones a ~$X cada una" | Todas las conversiones valen casi lo mismo | Un lead, una descarga, la Calculadora de $10.000 |
| **tROAS** | "Devuélveme $Y por cada $1 gastado" (con valores de conversión) | Los tickets varían mucho | E-commerce con productos de $20.000 a $500.000 |

Para GastroLatam (producto único de $10.000 COP), tCPA es lo natural. Para una tienda con valores de pedido dispares, tROAS protege mejor la rentabilidad porque pondera por el valor real de cada venta, no solo cuenta. (Sobre qué CPA/ROAS es viable según tu margen, ver 64-ROAS-real y `economist_lushows`.)

> Nota 2026: "Maximizar conversiones" con un tCPA opcional y "Maximizar valor de conversión" con un tROAS opcional son las dos familias vigentes; el target es el límite que le pones. Sin target, Google gasta todo el presupuesto sin techo de CPA/ROAS (ver 13-smart-bidding).

## Cómo mover el target para escalar (sin ahogar la entrega)

La mecánica de escalar protegido es **aflojar el target en pasos pequeños** para abrir volumen sin romper el aprendizaje:

1. **Afloja el target ~10–15% por paso.** Si tu tCPA era $25.000 COP y quieres más volumen, súbelo a ~$28.000, no a $40.000. Apretar/aflojar de golpe sacude Smart Bidding y entra en aprendizaje (ver 13-smart-bidding). (Con tROAS es al revés: para más volumen *bajas* el tROAS — pides menos retorno por peso.)
2. **Asegúrate de que el presupuesto acompañe.** Aflojar el target sin presupuesto extra es inútil: Google quiere comprar más conversiones caras pero no tiene con qué. Afloja target Y verifica que el presupuesto no sea el cuello de botella (IS Lost budget, ver 72-esc-vertical). Pero **no cambies ambos de forma brusca el mismo día** — sube presupuesto en su paso del 20%, deja estabilizar, luego afloja target en su paso. Uno a la vez.
3. **Espera 1 ciclo de conversión** antes de juzgar. El volumen no salta al día siguiente; el modelo recalibra.
4. **Si el CPA real sube más de lo que esperabas** al aflojar, aprieta de vuelta un paso. Estás buscando el punto donde más volumen aún deja margen (ver `economist_lushows`).

### Tabla: qué pasa según muevas el target

| Mueves | tCPA | tROAS | Efecto en volumen | Efecto en CPA |
|---|---|---|---|---|
| Para CRECER | Subes (aflojas) | Bajas (aflojas) | ↑ Más | ↑ Sube |
| Para PROTEGER margen | Bajas (aprietas) | Subes (aprietas) | ↓ Menos | ↓ Baja |

El error inverso —**apretar el target buscando más volumen**— es de los más comunes y absurdos: apretar baja el CPA pero **mata la entrega** (Google deja de entrar a subastas, las impresiones caen, el volumen se desploma). Si tu campaña "casi no gasta", probablemente tienes el target demasiado apretado para tu mercado: aflójalo.

## Diagnóstico rápido por síntoma

| Síntoma | Causa probable | Acción |
|---|---|---|
| "La campaña no gasta el presupuesto" | tCPA muy apretado / tROAS muy alto | Aflojar target en pasos del 10–15% |
| "Gasta todo pero el CPA es carísimo" | Target muy flojo o demanda agotada | Apretar target; revisar IS Lost (ver 75) |
| "Subí presupuesto y nada cambió" | Target es el cuello, no el presupuesto | Aflojar target (Google no tenía permiso de comprar más caro) |
| "Aflojé target y el volumen no subió" | Presupuesto era el cuello | Subir presupuesto (ver 72) |

## Apretar para proteger margen (el otro sentido)

Aflojar es para crecer; apretar es para defender rentabilidad cuando el CPA se salió de control o el margen se apretó:

- **Aprieta el tCPA/tROAS ~10–15%** si el CPA real superó tu umbral de viabilidad y quieres recuperar margen, aceptando perder algo de volumen.
- Hazlo también en pasos, no de golpe — apretar brusco puede frenar la entrega casi por completo.
- Si apretaste y el volumen se fue al piso, te pasaste: el mercado no da ese CPA. Afloja de vuelta y replantea si Google es viable a ese margen (ver 79-micro, `economist_lushows`).

## El target en escalado y temporada

Cuando escalas vertical (más presupuesto) sin tocar el target, el CPA marginal sube solo porque compras conversiones más caras: si tu margen no aguanta, aprieta un poco el target para sostener rentabilidad mientras creces. En Q4 (ver 77) NO aprietes el target en pánico porque el CPC subió: la conversión también sube en temporada y el CPA mayor suele seguir siendo rentable. Usa seasonality adjustments para el pico, no cambios de target bruscos.

## Errores comunes — blacklist

- **Apretar el target esperando MÁS volumen.** Apretar reduce volumen; aflojar lo aumenta. Es la confusión más cara del bidding (ver 76-mitos).
- **Aflojar/apretar el target de golpe (30%+).** Reinicia el aprendizaje; la entrega se vuelve errática durante días (ver 13-smart-bidding).
- **Aflojar el target sin subir presupuesto.** Google quiere comprar más conversiones pero no tiene plata; no pasa nada y crees que la palanca no sirve.
- **Cambiar presupuesto Y target el mismo día.** Dos shocks juntos; imposible saber qué causó qué. Uno, estabiliza, el otro.
- **Juzgar el cambio de target con el dato de ayer.** El modelo recalibra en 1 ciclo de conversión; reaccionar a 24h te mantiene en aprendizaje permanente (ver 70-reglas).
- **Aflojar el target a un CPA que tu margen no aguanta.** Más volumen a pérdida no es escalar, es quemar plata más rápido. Valida el CPA máximo viable primero (ver 64-ROAS-real, `economist_lushows`).
- **Dejar el target tan apretado que la campaña "no gasta" y culpar a Google.** Si no entrega, casi siempre es target demasiado agresivo para tu mercado. Aflójalo en pasos.
- **Apretar el target en Q4 porque el CPC asusta.** El CPC sube para todos; juzga por CPA/ROAS final, no por el CPC (ver 77-Q4).
