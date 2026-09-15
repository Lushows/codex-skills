# 43 — Display y banners

Lee este módulo cuando alguien te ofrezca "millones de impresiones baratísimas" en la Red de Display y quieras saber si es oro o basura, o cuando una campaña de banners te esté gastando plata sin una sola venta y necesites entender adónde se fue. Display es la red de **banners** de Google: tus anuncios gráficos aparecen en millones de sitios web, apps y YouTube. Es alcance barato — y ahí está la trampa: barato no es lo mismo que rentable. Display **no captura intención** (eso es Search); su mejor uso es **recordar** a quien ya te conoce (remarketing, ver 24), no buscar clientes nuevos a ciegas. Para generación de demanda visual moderna, Demand Gen (ver 41) ya hace mejor el trabajo que el Display de prospección.

## Qué es y qué tipos hay

La **Red de Display de Google (GDN)** son los espacios de banner en sitios, apps, Gmail y YouTube donde Google coloca publicidad gráfica — más de 2 millones de sitios y apps. Hay dos formas de armar el anuncio:

| Tipo | Qué es | Cuándo |
|---|---|---|
| Responsive Display Ad (RDA) | Subes imágenes, logos, títulos y descripciones; Google arma y ajusta el banner a cada espacio automáticamente | Lo estándar hoy — usa este |
| Banner subido (imagen fija) | Tú diseñas el banner en cada tamaño (300×250, 728×90, etc.) | Solo si necesitas control de marca exacto |

El RDA es lo práctico: das los insumos (la dirección de arte va en `directorcreativo_lushows`) y Google los combina. Pero "automático" no significa "sin vigilancia": Google, si lo dejas suelto, te pone donde sea con tal de gastar.

### Specs del RDA (jun-2026)

| Asset | Proporción | Tamaño | Notas |
|---|---|---|---|
| Imagen horizontal | 1.91:1 | 1200×628 px | obligatoria |
| Imagen cuadrada | 1:1 | 1200×1200 px | obligatoria |
| Logo cuadrado | 1:1 | 1200×1200 px | + opcional 4:1 (1200×300) |
| Títulos | hasta 5, ≤30 caracteres | — | |
| Título largo | 1, ≤90 caracteres | — | |
| Descripciones | hasta 5, ≤90 caracteres | — | |
| Video (opcional) | 16:9 / 1:1 / 9:16 | ≤30s | mejora alcance |

Sube **mínimo 2–3 imágenes por proporción** para que Google tenga con qué combinar y aprender.

## Dónde Display SÍ vale — y dónde es plata quemada

**Sí vale: remarketing.** Mostrarle un banner a alguien que ya visitó tu landing o vio tu video es barato, relevante y rentable. La persona te conoce; el banner solo le recuerda que vuelva. Ese es el 80% del valor real de Display (ver 24). CPM de remarketing en Colombia: típicamente **$3.000–$10.000 COP** por mil impresiones — más barato que el alcance frío y mucho más rentable.

**Es alcance basura:** Display "de prospección" sin audiencia afinada —"llega a 5 millones de personas en Colombia por $200.000"— suena increíble y casi siempre lo es: te llenas de impresiones en sitios y apps que nadie mira de verdad, con clics accidentales y cero ventas. El alcance barato sin segmentación es el clásico hueco de presupuesto del anunciante novato.

El peor enemigo son los **placements basura**:

- **Apps móviles de juegos/linterna/wallpaper:** los banners se tocan por accidente. Clics que pagas y no valen nada.
- **MFA sites** (*Made For Advertising*, sitios hechos solo para mostrar anuncios): páginas de pura publicidad, contenido robado o autogenerado por IA, existen únicamente para cobrarte impresiones. Tráfico tóxico — y en 2026 proliferan más por el contenido autogenerado.

## Cómo blindar Display: exclusiones obligatorias

Si vas a correr Display, configúralo a la defensiva desde el día uno:

1. **Excluir apps móviles.** En la configuración de la campaña, excluye la categoría de aplicaciones (`mobileappcategory::69500` es el ID que excluye TODAS las apps). Para la mayoría de negocios que venden por web/WhatsApp, las apps solo traen clics accidentales.
2. **Excluir placements basura por nombre.** Revisa el reporte "Dónde se mostraron los anuncios" (placements) cada semana y excluye manualmente los sitios/apps con muchas impresiones y cero conversiones, y cualquier MFA.
3. **Exclusiones de contenido (content/topic exclusions):** quita contenido sensible, juegos, política, tragedias, contenido para adultos, y temas que no quieres asociar a tu marca. Excluye también contenido parqueado y de baja calidad ("below the fold", "parked domains").
4. **Frequency cap (límite de frecuencia):** que la misma persona no vea tu banner 40 veces al día — molesta y desperdicia impresiones. Pon 3–5 impresiones/día como techo.
5. **Listas de exclusión de placements compartidas:** mantén una lista negra a nivel cuenta que crece con el tiempo y aplícala a todas tus campañas Display.

Sin estas exclusiones, Display gastará tu presupuesto donde más fácil es para Google, no donde más te conviene a ti.

## Companion banner + product feed

Dos extras que dan valor sin producción nueva:

- **Companion banner:** el banner pequeño que acompaña a un video en YouTube (escritorio). Da un segundo punto clicable junto al video sin costo extra de producción (ver 45).
- **Product feed:** conectar un feed de Merchant Center a Display/Demand Gen para mostrar productos con precio. Clave si vendes varios SKU; para un producto único aporta poco (ver 41, 45).

## Regla práctica para Colombia

Con presupuesto chico (menos de $1.500.000 COP/mes): **Display solo para remarketing.** Nada de prospección en Display. Tu plata de captura va a Search (intención caliente) y tu generación de demanda a Demand Gen/Meta (ver 41, 46). Display es el recordatorio barato para quien ya pasó por tu puerta — ni más ni menos. Y nota: Demand Gen (ver 41) ya cubre lo visual de generación de demanda mejor que Display de prospección; rara vez necesitarás Display suelto para conseguir clientes nuevos.

## Plantilla de configuración defensiva

```
CAMPAÑA DISPLAY — checklist de blindaje
[ ] Objetivo: remarketing (no prospección fría)
[ ] Audiencia: visitantes web (24) / Customer Match (25), NO "intereses amplios"
[ ] Excluir apps: mobileappcategory::69500
[ ] Exclusiones de contenido: juegos, parqueado, adultos, sensible
[ ] Frequency cap: 3–5/día
[ ] Frecuencia de revisión de placements: SEMANAL → excluir basura
[ ] Lista negra a nivel cuenta aplicada
[ ] Destino: landing congruente con el banner (48), no la home
[ ] Assets RDA: ≥2 imágenes 1.91:1 + ≥2 imágenes 1:1 + logo
```

## Errores comunes — blacklist

1. **Comprar "millones de impresiones baratas" como prospección.** Alcance barato sin segmentar = impresiones fantasma y clics accidentales. Cero ventas.
2. **No excluir apps móviles.** Los banners en juegos se tocan sin querer; pagas clics que no valen nada. Excluye la categoría de apps de entrada.
3. **No revisar el reporte de placements.** Display sin vigilar termina en MFA sites y basura. Revisa y excluye semanal.
4. **Usar Display para capturar demanda nueva.** Display no lee intención; Search sí. Pides peras al olmo. Para demanda visual, Demand Gen (41).
5. **Sin límite de frecuencia.** Quemas impresiones y molestas mostrando el mismo banner decenas de veces a la misma persona.
6. **Banners feos o genéricos.** El RDA combina lo que le des; si los insumos son malos, el banner es malo. Dirección de arte en `directorcreativo_lushows`.
7. **Mandar el clic de Display a una landing incongruente.** El banner promete una cosa y la página dice otra; el clic ya caro se pierde (ver 48). Construcción de landing en `desingweb-lushows`.
8. **Confiar en el targeting "optimizado" sin exclusiones.** El optimized targeting de Display amplía la audiencia por defecto; sin exclusiones te lleva a placements basura. Vigílalo.
