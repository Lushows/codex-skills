# 63 — Google Ads como instrumento

Lee este módulo cuando abres la cuenta y te ahogas en columnas, cuando tardas 20 minutos en encontrar un dato que deberías ver en 30 segundos, o cuando quieres armar una vista que te diga en un vistazo "esto está bien, esto está mal". Una cuenta bien configurada se lee como el tablero de un carro: combustible, velocidad, temperatura, sin abrir el motor. Aquí afinamos el tablero.

Frame: Google Ads no es solo un lugar para gastar plata; es un **instrumento de medición de la intención que capturas**. La mayoría de cuentas usan la vista por defecto (clics, costo, impresiones) y se pierden el 90% de lo útil. Las métricas que deciden (ver 60) están ahí, escondidas en columnas que nadie activó. Vamos a sacarlas a la superficie.

## Columnas personalizadas: lo que importa, en pantalla

La vista por defecto esconde las métricas que deciden. Configúralas una vez y vívelas siempre.

En cualquier tabla → **Columns → Modify columns** → arrastra estas y guarda como vista:

| Grupo de columnas | Qué agregar | Por qué |
|---|---|---|
| **Competitive metrics** | Search IS, Lost IS (budget), Lost IS (rank), Top IS, Abs Top IS | Diagnóstico de techo (ver 60, 61, 94) |
| **Conversiones** | Conversions, Cost/conv (CPA), Conv. value, Conv. value/cost (ROAS), Conv. rate (CVR) | El resultado, no solo el gasto |
| **Calidad** | CTR, Avg. CPC, Quality Score (a nivel keyword) | Diagnóstico de eficiencia |

Guarda esto como un **conjunto de columnas con nombre** (ej. "Diagnóstico Lucho") para no rearmarlo cada vez. Tip: pon las competitivas y las de conversión juntas; así ves de un golpe "aparezco poco Y convierto mal" vs "aparezco bien pero no convierto". Esa lectura cruzada es el diagnóstico por capas de un vistazo (ver 61).

Columna avanzada que casi nadie pone: **"Conversions (by conv. time)"** vs **"Conversions"**. La primera atribuye la conversión al día en que ocurrió; la segunda al día del clic. Tenerlas lado a lado te explica por qué los últimos días parecen "flojos" (las conversiones de esos clics aún no han madurado — ver lag de conversión, 62).

## Segmentos: la misma data, partida donde duele

**Segmentar** = romper una fila en sub-filas por una dimensión. La misma campaña se ve distinta según cómo la partas. Botón **Segment** arriba de la tabla.

| Segmento | Qué revela | Cuándo usarlo |
|---|---|---|
| **Device** (dispositivo) | Que móvil convierte la mitad que desktop, por ejemplo | Casi siempre: el móvil suele tener landing peor (ver `desingweb-lushows`) |
| **Day of week / Hour** | Que los domingos gastas y no vendes | Para ajustar horarios/presupuesto |
| **Conversion action** | Qué conversión específica trae cada campaña | Cuando mides varias acciones (lead vs venta) |
| **Network** (Search vs partners) | Que los "search partners" te traen basura | Para apagar partners si rinden mal |
| **Top vs Other** | Si tus conversiones vienen de arriba o de abajo de la página | Para decidir si vale pagar Top IS |
| **Click type** | Si el gasto se va en extensiones/sitelinks vs el anuncio | Diagnóstico fino de gasto |

La revelación típica: segmentas por device y descubres que el 60% del gasto es móvil con CVR de 0.8% vs 3% en desktop. No es la campaña: es la landing móvil. Esa conclusión vale más que mil ajustes de puja.

## Search terms report: lo que la gente REALMENTE buscó

**Keyword** = lo que tú pujas. **Search term** = lo que la persona escribió de verdad. No son lo mismo, y la diferencia es donde se gana o se quema plata (sobre todo con concordancia amplia / broad match, que activa búsquedas que ni imaginaste).

Ve a la campaña → **Insights and reports → Search terms** (o el ícono de búsqueda en la keyword). Ahí ves cada búsqueda real que activó tus anuncios, con sus clics, costo y conversiones.

Tres acciones desde ahí (detalle en 68):
- Búsqueda relevante que convierte → agrégala como **keyword nueva**.
- Búsqueda irrelevante que gasta → agrégala como **negativo** (ver 22).
- Búsqueda relevante que no convierte → revisa landing/oferta (ver 61).

Este reporte es el más subusado y el más rentable de toda la plataforma. Revísalo cada semana. Nota 2026: con Performance Max y AI Max, una parte de los términos viene en categorías agregadas ("search categories") menos granulares — aún así, lo que sí ves manda señales valiosas (ver 68).

## Asset reporting y nuevas pestañas (2026)

El bloque de anuncios responsivos (RSA) y de Performance Max trae **asset reporting** con etiquetas **Best / Good / Low** por cada titular, descripción, imagen y video (detalle completo en 68). Búscalo en el anuncio → "View asset details" o pestaña **Assets**. Es el instrumento para saber qué creatividad gana sin adivinar.

## Report editor: tus propias vistas

El **Report editor** (Reports → ícono de gráficas, arriba a la izquierda) arma tablas y gráficas a la medida, arrastrando dimensiones (campaña, device, día) y métricas (CPA, ROAS). Úsalo para lo que la vista normal no da fácil:

- CPA por **día** en gráfica de línea (ver tendencia, no solo el total).
- ROAS por **campaña × device** en tabla cruzada (encuentra dónde se fuga la plata).
- Conversiones por **hora del día** (¿cuándo vale subir puja o presupuesto?).
- IS por campaña a lo largo del tiempo (¿estoy perdiendo terreno con un competidor? ver 94).

Para reportes ejecutivos a cliente/jefe, no uses esto crudo: pásalo a una plantilla limpia (ver 67) o a un dashboard de Looker Studio que se actualiza solo (ver 69). El Report editor es tu mesa de trabajo; el reporte ejecutivo es la versión presentable con decisión incluida.

## Recommendations y Optiscore: úsalos con criterio

La pestaña **Recommendations** y el **Optimization Score** (Optiscore) sugieren cambios. Algunos son oro (negativos obvios, conflictos de medición); muchos empujan a gastar más o ampliar concordancia sin que te convenga. **No apliques a ciegas para "subir el Optiscore"**: cada recomendación pasa por tu diagnóstico (ver 61). Aplica las que resuelven un problema real; descarta (dismiss) las que solo inflan el gasto. El Optiscore es de Google, optimizado para Google; tu rentabilidad es tuya.

## Errores comunes — blacklist

1. **Vivir en la vista por defecto.** Clics y costo no deciden nada. Sin las columnas competitivas y de conversión estás manejando sin tablero (ver 60).
2. **No segmentar por device nunca.** Es donde se esconde el problema más común (móvil que no convierte). Míralo antes de culpar a la campaña.
3. **Ignorar el search terms report.** Es el reporte más rentable y el más abandonado. Revísalo semanal (ver 68).
4. **Rearmar columnas cada vez.** Guarda conjuntos con nombre; perder 10 minutos por sesión rearmando es trabajo tonto.
5. **Confundir keyword con search term.** Pujas por una cosa, apareces en otra. Si no separas los conceptos, no entiendes dónde se va la plata.
6. **Usar el Report editor crudo como reporte para el cliente.** Genera confusión, no confianza. Tradúcelo a plantilla ejecutiva (ver 67) o dashboard (ver 69).
7. **No mirar "Top vs Other".** Pagas Abs Top IS carísimo asumiendo que la posición 1 convierte, sin verificar que tus conversiones de verdad vienen de arriba.
8. **Aplicar Recommendations a ciegas para subir el Optiscore.** Muchas empujan más gasto sin rentabilidad. Cada una pasa por tu diagnóstico, no por el medidor de Google.
