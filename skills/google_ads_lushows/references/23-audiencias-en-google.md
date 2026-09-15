# 23 — Audiencias en Google

Lee este módulo cuando quieres decirle a Google "muéstrame a estas personas" y no entiendes por qué en Search "agregar una audiencia" no las restringe. La gran trampa mental: en Meta la audiencia ES el targeting (ver `facebook_ads_lushows`). En **Google Search la keyword es el targeting** — la audiencia es una **capa de señal**, no una jaula. Entender esto evita que estrangules tus campañas o que esperes resultados que la configuración por defecto nunca iba a dar. Frame: Google captura intención por la búsqueda; la audiencia solo te dice *quién además* es esa persona, para priorizarla, no para invitarla.

## Los tipos de audiencia — qué es cada una

| Tipo | Qué es | Ejemplo gastro |
|---|---|---|
| In-market (en el mercado) | Gente que Google detecta **comprando ahora** en una categoría | "software/herramientas para restaurantes" |
| Affinity (afinidad) | Intereses y estilo de vida de largo plazo | "entusiastas de la gastronomía", "dueños de pequeños negocios" |
| Custom segments (segmentos personalizados) | Tú los defines: por palabras que buscan, apps que usan, o sitios web que visitan | gente que buscó "abrir un restaurante" o visita sitios de proveedores de cocina |
| Data segments (datos propios) | Tu remarketing: visitantes de tu sitio, tu lista de clientes (ver 24, 25) | quien vio tu landing y no compró |
| Detailed demographics | Estado civil, hijos, educación, propiedad de negocio | "propietarios de pequeñas empresas" |
| Life events | Momentos vitales | "acaba de abrir un negocio", "se mudó" |

In-market y custom (por intención de búsqueda) son las más potentes para capturar demanda. Affinity es más de marca/awareness — sirve más en YouTube/Demand Gen (ver 40, 41) que en Search. **Custom segments por intención de búsqueda** son tu mejor arma fuera de Search: defines "gente que buscó en Google estas frases" o "que visita estos sitios", y se la das a YouTube/Demand Gen. Es lo más cercano a capturar intención en formatos visuales.

## Observación vs Segmentación — la decisión que más se equivoca

Cuando agregas una audiencia tienes dos modos:

| Modo | Qué hace | Cuándo |
|---|---|---|
| **Observación** | Tu anuncio sigue saliendo a TODOS los que buscan tu keyword. La audiencia solo **mide y permite ajustar puja**. No restringe. | Default en Search. Casi siempre el correcto. |
| **Segmentación (targeting)** | Tu anuncio SOLO sale a quien busca tu keyword **Y** está en la audiencia. Restringe fuerte. | Solo cuando sabes exactamente qué haces y quieres acotar. |

**La regla de oro en Search: usa Observación.** Por defecto déjalo en observación. Si pones segmentación sin pensar, reduces tu alcance brutalmente — porque exiges keyword + audiencia a la vez, y la mayoría de tus compradores válidos pueden no estar etiquetados en esa audiencia (las audiencias de Google son incompletas; nadie está en todos los segmentos que le corresponderían). Has visto cuentas que "dejaron de funcionar" tras alguien poner segmentación creyendo que "afinaba".

Cómo usar observación bien — proceso de 4 pasos:
1. Agrega 3–5 audiencias relevantes en **observación** a tu campaña de Search (in-market de tu categoría + un par de custom segments por intención).
2. Deja correr 2–4 semanas (necesitas volumen para que el dato sea señal, no ruido).
3. Mira qué audiencia convierte mejor en los reportes (Audiencias → columna de conversiones/CPA por segmento).
4. Sube la puja (ajuste de puja, ver 15) a las que convierten +20%/+40%; baja a las que no −20%. Sigues saliéndole a todos, pero pujas más fuerte por los buenos.

Así la audiencia es una **señal que afina la puja**, no un muro que estrangula el alcance. Con Smart Bidding (tCPA/tROAS) el ajuste manual se vuelve una señal más que el algoritmo pondera, no una regla dura — pero la observación igual te da el reporte por audiencia, que es información valiosísima para entender a quién le compras (ver 13, 15).

## Cómo no estrangular Search (y dónde sí restringir)

- **Search:** observación + ajustes de puja. La intención ya viene en la keyword; la audiencia solo prioriza.
- **Performance Max / Demand Gen / YouTube:** aquí las audiencias pesan más como **señal de público** porque no hay keyword. En PMax das "audience signals" (señales de audiencia) para que el algoritmo arranque sabiendo a quién parecerse — pero **ojo:** en PMax las señales NO restringen, solo orientan el aprendizaje; el algoritmo puede salirse de ellas (ver 12, 90). En Demand Gen el targeting de audiencia sí acota más.
- **Display:** ahí sí la audiencia es casi todo el targeting (no hay búsqueda ni señal de intención fresca).

La mejor semilla de audiencia que tienes es tu propia data: visitantes (ver 24) y Customer Match (ver 25). Esa data alimenta tanto la observación en Search como las señales en PMax, y en el mundo post-cookie de 2026 es tu activo más difícil de copiar.

## Cómo construir un custom segment que sí funcione

El segmento personalizado es la audiencia más infrautilizada y la más potente fuera de Search. Se arma en Audience Manager → Segmentos personalizados, con dos insumos:

1. **Frases de búsqueda:** "personas que buscaron alguno de estos términos en Google". Aquí pones tus keywords de alta intención, las de competidores y las de problema-negocio. Ejemplo gastro: `software costeo restaurante`, `como controlar food cost`, `abrir dark kitchen`, `[nombre competidor]`. Mientras más específicas, más limpia la audiencia.
2. **URLs / sitios y apps:** "personas con interés en sitios como estos". Pones dominios de competidores, asociaciones del sector (Acodres en Colombia), medios gastronómicos, portales de proveedores de cocina.

Plantilla de custom segment para la calculadora gastro:
```
Tipo: por intención de búsqueda
Frases: costeo de recetas, food cost restaurante, calcular precio de plato,
        plantilla de costos restaurante, margen de ganancia restaurante
URLs:   sitios de software POS gastronómico, blogs de gestión de restaurantes
Uso:    Search (observación, subir puja) + Demand Gen/YouTube (targeting)
```

**Combinar capas en observación:** puedes apilar in-market ("software para empresas") + custom segment (por intención) + data segment (visitantes) en la misma campaña de Search, todas en observación. Después lees cuál de las tres convierte mejor y ajustas puja por capa. No es "elige una"; es "obsérvalas todas y deja que los datos te digan a quién subirle". Eso sí: si no vas a leer el reporte de audiencias cada 2–4 semanas, no las apiles — observación sin lectura es decoración.

## Errores comunes — blacklist

1. **Poner Segmentación en vez de Observación en Search.** Estrangulas el alcance sin darte cuenta. Default = observación, siempre, salvo que sepas exactamente por qué restringes.
2. **Creer que la audiencia reemplaza la keyword en Search.** No. La keyword manda; la audiencia ajusta puja. Si tus keywords están mal, ninguna audiencia te salva (ver 20, 22).
3. **Usar affinity esperando conversión directa en Search.** Affinity es awareness; rinde en YouTube/Demand Gen. Para capturar compra usa in-market y custom por intención.
4. **No esperar datos antes de ajustar pujas por audiencia.** 2–4 semanas mínimo. Decidir con 5 clics es ruido, no señal.
5. **Olvidar dar señales de audiencia a PMax.** Sin señales, PMax arranca a ciegas y desperdicia presupuesto aprendiendo (ver 12). Pero no confundas señal con restricción: PMax igual explora fuera.
6. **No tener remarketing (data segments) configurado.** Es la audiencia que más convierte y la más barata de ignorar. Móntala ya (ver 24).
7. **Apilar 15 audiencias en observación y no leer ninguna.** Observación solo sirve si después LEES los datos y ajustas. Si no vas a mirar, no las pongas.
8. **Construir custom segments con frases demasiado anchas.** "comida" como intención trae a todo el mundo; usa frases largas y específicas ("software costeo restaurante", "abrir dark kitchen Bogotá") para que la señal sea limpia.
