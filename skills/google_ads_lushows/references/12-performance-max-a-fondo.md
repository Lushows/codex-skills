# 12 — Performance Max a fondo

Lee este módulo cuando vas a lanzar PMax, cuando un PMax te está reportando un ROAS sospechosamente bueno, o cuando intuyes que "algo se está comiendo" tus ventas de marca. Performance Max (PMax) es la campaña de IA de Google: tú le das presupuesto, objetivo y unos insumos creativos, y el algoritmo reparte el gasto entre **toda la red** —Search, Shopping, Display, YouTube, Gmail, Discover, Maps— buscando tu conversión. Es poderosa y, mal usada, te miente. El marco no cambia: PMax es buenísima **capturando** demanda cuando ya tienes señal limpia que la guíe; pésima como primera apuesta a ciegas.

## Qué es y cómo se arma por dentro

PMax no tiene keywords ni grupos de anuncios. Tiene **asset groups** (grupos de recursos): paquetes de creativos organizados por tema/audiencia. Sus insumos clave:

| Insumo | Qué es | Cuánto pesa |
|---|---|---|
| **Assets** (recursos) | Titulares, descripciones, imágenes, logos, video | Si no subes video, Google **autogenera** uno (feo); súbelo tú (ver 32) |
| **Audience signals** (señales de audiencia) | Pistas de a quién dirigir: tus listas, intereses, demográficos | Son **sugerencias, no límites**: el algoritmo arranca ahí y sale. NO es segmentación dura |
| **Search themes** (temas de búsqueda) | Frases tipo "captura intención parecida a esto" | Guían la parte Search de PMax; complementan, no reemplazan, tu Search |
| **Final URL expansion** | Deja que PMax mande tráfico a otras URLs de tu sitio | Apágalo si no quieres que invente destinos |

PMax necesita comida: idealmente **≥30 conversiones/mes** para calibrar (ver 13). Con menos, da bandazos y quema en Display a frío.

## Qué controlas vs qué cedes

Esta es la decisión de fondo. PMax es una caja parcialmente negra:

| LO QUE SÍ controlas (úsalo siempre) | LO QUE CEDES (vives con ello) |
|---|---|
| **Negativos a nivel de cuenta** (account-level negatives) | Reparto exacto del gasto por canal |
| **Exclusiones de marca** (brand exclusions) — clave para no canibalizar | En qué placement de Display/YouTube exacto cae |
| Objetivo de puja y target (tCPA/tROAS, ver 15) | Qué búsqueda exacta disparó (reporte de términos parcial) |
| Calidad de los assets que subes (ver 32) | Cuándo prioriza Shopping vs Search vs Display |
| Exclusión de URLs, contenido sensible, final URL expansion | El crédito real por canal (atribución mezclada, ver 16) |
| **Channel reporting** (ver gasto/conv por canal) | El detalle fino dentro de cada canal |

**Controles 2026**: PMax ya trae **reporte por canal** (channel-level reporting: ves cuánto gastó y convirtió en Search vs Display vs YouTube), **brand exclusions** maduras, y en cuentas elegibles la posibilidad de pedir exclusión/limitación de algunos canales. La opacidad bajó respecto a 2023 pero sigue siendo el costo de entrada. **AI Max for Search** es un primo de PMax que vive *dentro* de Search (ver 90); no lo confundas con PMax.

## Cuándo PMax SÍ y cuándo CANIBALIZA

**PMax SÍ cuando:**
- Tienes **e-commerce con catálogo** y Merchant Center: PMax retail es su mejor caso de uso, lejos (ver 35).
- Ya tienes **Search funcionando con conversiones limpias** y quieres expandir alcance sin abrir cinco campañas.
- Manejas **muchos SKUs** y no puedes estructurar Search keyword por keyword.
- Tienes **≥30 conv/mes** para alimentarlo.

**PMax CANIBALIZA cuando:**
- No tienes **brand exclusions** activadas: PMax se mete en las búsquedas de tu propia marca, gana esas conversiones baratísimas (que ya ibas a tener gratis o por Search marca) y **reporta un ROAS inflado** que no es incremental (ver 65). Parece un héroe; es un ladrón de crédito.
- Lo lanzas **antes que Search genérico**: te roba la intención clara y la mezcla con tráfico de Display de baja calidad; nunca sabes qué funcionó.
- Tu volumen es bajo (<30 conv/mes): no calibra y desperdicia en Display a frío.

## Reglas de oro para domar PMax

1. **Siempre** corre Search de marca en paralelo + activa **brand exclusions** en PMax. Así PMax no toca tu marca y Search marca la defiende barata (ver 39).
2. Mide **incrementalidad**, no ROAS reportado: ¿subieron las ventas TOTALES al prender PMax, o solo se movió el crédito? (ver 65). Haz un lift test o un on/off geográfico.
3. Sube **tus propios assets y video** (ver 32); no dejes que autogenere — un video feo daña la marca (rutea calidad creativa a `directorcreativo_lushows`).
4. Carga **audience signals** con tus mejores listas (clientes, visitantes recientes, similares), pero entiende que son pistas, no muros (ver 23, 25).
5. **Apaga final URL expansion** al inicio si vendes algo específico; ábrelo solo cuando confíes.
6. Triangula con backend/CRM: ¿los leads de PMax cierran o son basura? Sube las ventas reales vía OCI con gclid (ver 53, 64, 66).
7. **Revisa el channel report mensual**: si Display se está comiendo el 60% del gasto con conversiones flojas, es bandera roja — ajusta assets/señales o considera Search puro.

### Estructura recomendada de asset groups

| Asset group | Cuándo separarlo |
|---|---|
| Uno por **línea de producto/categoría** con audiencia y creativos propios | Cuando los productos hablan a públicos distintos |
| Uno por **margen/prioridad** (alta vs baja rentabilidad) | Para empujar lo que más deja con tROAS distinto |
| **No** un asset group por SKU | Fragmenta la señal igual que el SKAG (ver 10) |

## PMax vs Search puro: cuándo NO vale la pena

Si eres un negocio LatAm pequeño que **vende un servicio o un producto digital específico** (no catálogo), con <30 conv/mes, **PMax casi siempre rinde peor que Search bien armado + AI Max**. La razón: sin catálogo que mostrar en Shopping, PMax se va a Display/YouTube de baja intención y te trae tráfico flojo. En ese perfil, queda Search genérico + marca + (cuando crezcas) AI Max, y reservas PMax para cuando tengas catálogo o volumen real.

## Errores comunes — blacklist

- **PMax sin brand exclusions**: canibaliza marca y reporta ROAS falso; la trampa #1 (ver 39, 65).
- **PMax como primera campaña** sin Search que genere señal limpia: caja negra alimentada con datos sucios (ver 11, 14).
- **Confundir audience signals con segmentación dura**: crees que limitas a tu público y el algoritmo gasta donde quiere; son sugerencias.
- **No subir video**: Google autogenera uno horrible que daña la marca (rutea a `directorcreativo_lushows`).
- **Juzgar PMax por su ROAS reportado** sin prueba de incrementalidad: te felicitas por ventas que ya tenías (ver 65).
- **Lanzar PMax con <30 conversiones/mes** de señal: no calibra, da bandazos, quema en Display (ver 13).
- **Dejar final URL expansion abierto** sin querer: PMax manda tráfico a URLs que no elegiste y ensucia la conversión.
- **Mezclar en un PMax leads B2B + venta retail + marca**: objetivos opuestos, señal contaminada (ver 14, 27).
- **Ignorar el channel report**: no ves que Display se come el presupuesto con conversiones basura.
- **Un asset group por SKU**: fragmentas la señal como en los viejos SKAG (ver 10).
