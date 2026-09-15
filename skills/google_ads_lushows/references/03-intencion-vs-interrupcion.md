# 03 — Intención vs interrupción

Esta es la idea más importante de toda la skill, y la que casi nadie entiende: **Google CAPTURA demanda que ya existe; Meta GENERA demanda que no existía.** Confundir esto hace que la gente pierda meses y plata pautando en el canal equivocado. Lee este módulo cuando no sepas si tu negocio es para Google o para Meta, cuando "Google no me funciona" (quizás nadie busca tu categoría), o para diseñar el funnel completo.

## Las dos lógicas

| | **Intención (Google)** | **Interrupción (Meta → `facebook_ads_lushows` / TikTok → `tiktok_ads_lushows`)** |
|---|---|---|
| El usuario… | **busca** activamente una solución | está scrolleando, **no buscaba** nada |
| Tú… | **apareces** cuando ya hay deseo | **creas** el deseo con creativo |
| Temperatura | caliente (listo o casi) | frío (hay que calentar) |
| Palanca clave | keywords + negativas + Quality Score | creativo + audiencia + oferta |
| Pregunta que valida | "¿la gente escribe esto en Google?" | "¿puedo mostrar algo que provoque deseo?" |
| Ejemplo | "calculadora de costos para restaurante" | un Reel mostrando lo fácil que es calcular costos |
| Métrica de validación | volumen en Keyword Planner | hook/retención del creativo |

Regla mental: **Google = demanda que ya existe. Meta/TikTok = demanda que tú generas.** No son rivales; son dos partes del mismo embudo (ver 97). Una manera de verlo: Meta y TikTok **siembran**, Google **cosecha**. Si apagas la siembra, con el tiempo se seca lo que cosechas (ver 65, incrementalidad).

## Cuándo NO es Google (aunque te insistan)

Google Search solo rinde si hay **volumen de búsqueda con intención**. Si tu categoría es nueva, impulsiva o nadie sabe que existe, Google Search no tiene a quién mostrarte.

| Situación | ¿Google? | Qué hacer |
|---|---|---|
| Categoría conocida, la gente la busca | **Sí, Search-first** | ver 11, 20 |
| Producto nuevo que nadie nombra | **No (todavía)** | genera demanda en Meta/TikTok/Demand Gen (ver 41), luego captura tu marca en Google (ver 39) |
| Compra impulsiva visual (moda, deco) | Meta/TikTok primero | redes para descubrir; Google para marca/remarketing |
| Servicio local urgente ("cerrajero ya", "domicilio") | **Sí, fuerte** | Search + Local Services (ver 50, 81) |
| B2B de nicho con búsqueda baja | Search mixto | Search marca/genérico + LinkedIn/Meta para generar (ver 27) |
| Volumen en Keyword Planner ≈ 0 | **No** | no fuerces Google; es señal de que no hay demanda capturable |

Verificación obligatoria antes de pautar: **Keyword Planner** (ver 20). Si no hay búsquedas, la conclusión honesta es "Google no es tu canal hoy", no "súbele el presupuesto". **Más presupuesto no fabrica demanda que no existe.**

## El matiz 2026: informacional vs comercial

AI Overviews cambió el juego de las búsquedas informacionales. Distinguir el tipo de intención es ahora parte del diagnóstico:

| Tipo de búsqueda | Ejemplo | ¿Clickea anuncios en 2026? |
|---|---|---|
| **Informacional** | "qué es food cost", "cómo calcular costos" | poco — AI Overviews responde sin clic (ver 92) |
| **Comercial / transaccional** | "comprar plantilla food cost", "calculadora costos restaurante Colombia", "software costos cocina precio" | **sí** — la intención de compra sostiene el clic |
| **Navegacional / marca** | "GastroLatam", "[tu marca] calculadora" | sí — barato y alta conversión (ver 39) |

Conclusión: en 2026 prioriza keywords **comerciales y de marca**; deja las informacionales para contenido orgánico (fuera de esta skill). No pagues por curiosos que AI Overviews ya satisface gratis.

## El funnel completo Google + Meta

Lo potente no es elegir uno; es **orquestar ambos**. Caso típico LatAm:

```
META/TIKTOK (genera demanda)         GOOGLE (captura demanda)
  Reels/feed/videos muestran         Marca: capturas a quien ya te
  el producto a frío        ──────►  busca por nombre (ver 39)
  (despiertan interés)               Genérico: capturas a quien busca
                                     la solución (ver 11, 20)
                                           │
                                           ▼
                                  Lead llega al WhatsApp
                                           │
                                           ▼
                           Humano cierra (ver `ventas_lushows`)
                                           │
                                           ▼
                       Venta real → OCI de vuelta a Google (ver 53)
```

- Meta/TikTok abren la categoría y crean recordación; parte de esa gente luego **te busca en Google** → ahí Google "se lleva el crédito" de una venta que la red social inició. Por eso se miran juntos (incrementalidad, ver 65).
- En LatAm el cierre casi nunca es checkout web: es **WhatsApp o llamada**. La venta cerrada debe volver a Google vía **Offline Conversion Import (OCI)** o el algoritmo optimiza hacia "clics a WhatsApp" baratos en lugar de ventas reales (ver 53, 54). OCI usa el **gclid** (el id que Google pega a cada clic) igual que en Meta el `ctwa_clid` cierra el clic-a-WhatsApp.
- La orquestación omnicanal completa vive en el módulo 97 y cruza con `facebook_ads_lushows` y `tiktok_ads_lushows`. La landing donde aterriza el clic la diseña `desingweb-lushows`; el guion que cierra el lead, `ventas_lushows`.

## Cómo decidir el canal en 60 segundos (tabla maestra)

| Pregunta | Respuesta → canal |
|---|---|
| ¿Keyword Planner muestra volumen comercial? | Sí → Google Search · No → Meta/TikTok |
| ¿La compra es por necesidad/urgencia o por impulso visual? | Necesidad → Google · Impulso → Meta/TikTok |
| ¿La gente sabe que tu categoría existe? | Sí → Google · No → genera en redes primero |
| ¿Es servicio local "ya"? | Sí → Google Search + LSA |
| ¿El producto se ve increíble en video? | Aprovéchalo en redes; captura marca en Google |

## Errores comunes — blacklist

- **Forzar Google para un producto que nadie busca.** Terminas en Display/PMax (interrupción cara y mala). Fix: valida volumen en Keyword Planner; si no hay, vete a Meta/TikTok (ver 20, 41).
- **Esperar que Google "dé a conocer" la marca.** Google no crea deseo de la nada; muestra a quien ya busca. Fix: la generación es de Meta/TikTok/Demand Gen (ver 41, 97).
- **Pautar marca y genérico revueltos.** No sabes qué de Google es venta nueva y qué es gente que ya te conocía por Meta. Fix: separa campañas marca vs genérico (ver 39).
- **Pagar por keywords informacionales en 2026.** AI Overviews ya las responde gratis; quemas budget en curiosos. Fix: prioriza intención comercial y de marca (ver 92, 20).
- **Medir el clic a WhatsApp como conversión final.** Optimizas hacia curiosos. Fix: importa la venta real con OCI (ver 53, 54).
- **Ver Google y Meta como competidores y apagar uno "para ahorrar".** Apagar Meta seca la demanda que Google luego cosecha. Fix: míralos como un solo embudo; evalúa incrementalidad (ver 65, 97).
- **Asumir que más presupuesto arregla la falta de demanda.** Si nadie busca, más plata = más desperdicio. Fix: el problema no es budget, es canal (ver 00).
