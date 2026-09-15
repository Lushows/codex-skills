# 10 — Estructura de cuenta 2026

Lee este módulo cuando vas a abrir una cuenta nueva o heredaste una con 40 campañas y 300 grupos de anuncios que nadie entiende. La estructura ya no es donde se gana la cuenta —eso lo hace Smart Bidding sobre buena señal de conversión (ver 13 y 14)— pero una mala estructura todavía la arruina: te fragmenta los datos, le quita comida al algoritmo y te impide leer qué funciona. La regla de 2026 es **consolidar**, no atomizar. Recuerda el marco de toda la skill: en Google **capturas** intención que ya existe; la estructura solo tiene que dejar que el algoritmo vea esa intención junta y limpia.

## Por qué murió el SKAG (single keyword ad group)

SKAG = un grupo de anuncios por cada palabra clave exacta. Era la moda 2015-2019, cuando pujabas manual y la concordancia exacta era de verdad exacta. Hoy está muerto por tres razones técnicas, no de opinión:

- La concordancia exacta ya **no es exacta**: Google la trata como "misma intención" e incluye variantes cercanas, sinónimos, reordenamientos y singular/plural (ver 20, 21). Aislar una keyword ya no aísla nada — dos SKAGs distintos terminan compitiendo por la misma búsqueda.
- **Smart Bidding necesita volumen junto**: pide ~15-30 conversiones/mes por estrategia para calibrar (ver 13). Si partes tus conversiones en 50 grupos SKAG, cada uno tiene 0-1 conversión/mes y el algoritmo nunca sale de aprendizaje.
- El RSA (responsive search ad) necesita **datos de impresiones por grupo** para rotar y aprender qué titular gana (ver 30). 50 grupos diluyen eso a polvo.

El reemplazo moderno es la **consolidación temática** (a veces llamada STAG, single theme ad group): agrupar por intención y tema, no por keyword individual. Menos grupos, más densos, mejor alimentados.

## Cuántas campañas y por qué

La campaña es la unidad de **presupuesto, estrategia de puja, geo, idioma y red** (ver 26 geo, 15 pujas). El grupo de anuncios es la unidad de **mensaje y landing**. La regla mecánica: separa en campañas distintas cuando cambia algo de la primera columna; deja en grupos de anuncios cuando solo cambia el mensaje.

| Separa en CAMPAÑAS distintas cuando… | Separa en GRUPOS DE ANUNCIOS cuando… |
|---|---|
| Distinto presupuesto o prioridad de gasto | Mismo presupuesto, distinto tema/intención |
| Distinto objetivo de CPA/ROAS (ver 15) | Distinta landing por grupo de keywords |
| Distinta geografía o idioma (ver 26) | Distinto ángulo de copy (ver 38) |
| Marca vs genérico (¡siempre separa esto!) | — |
| Distinto tipo de campaña (Search vs PMax, ver 11) | — |

**Cuenta típica de un negocio LatAm pequeño** (presupuesto 1.5-6M COP/mes ≈ USD 370-1.500):

| Campaña | Tipo | Para qué |
|---|---|---|
| `Search — Marca` | Search | Defender tu nombre, CPC bajísimo, no canibalizar |
| `Search — Genérico` | Search | Capturar intención de producto/servicio (ver 03) |
| `PMax — Catálogo` o `PMax — General` | PMax | Expandir a Display/YouTube/Gmail/Maps (ver 12) |

Tres campañas. No necesitas más para arrancar. **Más campañas = más fragmentación, menos comida por algoritmo.** Agrega una cuarta solo cuando una de estas tope presupuesto consistentemente y siga rentable (ver 72, 73, 74). En 2026, con Broad match + Smart Bidding + buenos negativos como default (ver 20, 22), una sola campaña genérica bien armada cubre muchísimo terreno que antes pedía cinco.

### Esqueleto de cuenta — plantilla lista para copiar

```
CUENTA
├── Search — Marca
│   └── Grupo: Marca exacta + frase  (5-10 KW de tu nombre y variantes)
├── Search — Genérico
│   ├── Grupo: Compra        (broad: "comprar X", "X precio")
│   └── Grupo: Comparación   (broad: "mejor X", "X vs Y")
└── PMax — General
    ├── Asset group: Producto estrella
    └── Asset group: Línea secundaria
        + Brand exclusions ACTIVADAS (ver 12)
        + Negativos a nivel de cuenta (ver 22)
```

Esta es la base sobre la que crece todo lo demás. No la complifiques antes de que los números te lo pidan.

## Temática por intención, no por producto

Estructura por **lo que la persona quiere hacer**, no por tu organigrama de productos. Tres niveles de intención (ver 03 detalle):

| Intención | Ejemplo keyword | Grupo de anuncios |
|---|---|---|
| Transaccional ("comprar ya") | "comprar calculadora costos restaurante" | `Genérico — Compra` |
| Comparación ("cuál es mejor") | "mejor plantilla food cost excel" | `Genérico — Comparación` |
| Informacional ("cómo hago") | "cómo calcular costo de un plato" | `Genérico — Educación` (si el volumen lo sostiene) |

Empieza solo con **transaccional + comparación**: ahí está la plata. Lo informacional convierte peor y se come presupuesto; entra después con remarketing capturando a quien leyó tu contenido (ver 24). Cada grupo de anuncios: **5-15 keywords del mismo tema, 1-2 RSA, 1-2 landings congruentes** (ver 30, 33, 48). Si un grupo necesita prometer dos cosas distintas en el anuncio, son dos grupos.

## Naming convention (no es vanidad, es operación)

Si no puedes leer la cuenta de un vistazo, no la puedes optimizar ni reportar (ver 60, 67). Usa un patrón fijo: `[Tipo] — [Tema] — [Geo/Variante]`.

| Bien | Mal |
|---|---|
| `Search — Genérico — Compra` | `Campaña 1 (copia) final` |
| `PMax — Catálogo — Bogotá` | `prueba juan` |
| `Search — Marca` | `nueva nueva 2` |

Sé consistente para siempre: la convención que elijas hoy la vas a leer en 8 meses con la cuenta llena. Mismo formato en UTMs y en el CRM para que la triangulación con backend cuadre (ver 16, 53). Cuando trabajes con varias marcas/clientes, ese prefijo `[Tipo] —` te deja filtrar y reportar en segundos.

## Cómo encaja con PMax y AI Max

La estructura clásica (campaña > grupo > keyword) vive en Search. **PMax no tiene esa jerarquía**: trabaja con asset groups y señales (ver 12). **AI Max for Search** (ver 90) es una capa de IA *dentro* de tu campaña Search que expande matching y crea assets — no es una campaña nueva ni rompe tu estructura, la potencia. La decisión estructural de 2026 no es "¿cuántos SKAGs?" sino "¿cuánto control cedo a la IA y dónde lo retengo?". Retén siempre: separación marca/genérico, negativos de cuenta y la campaña de marca propia. Cede el matching fino y la rotación de assets.

## Errores comunes — blacklist

- **Resucitar SKAG** porque "así me enseñaron": fragmenta conversiones y mata el aprendizaje de Smart Bidding (ver 13).
- **Mezclar marca y genérico** en la misma campaña: tu CPA real queda enmascarado por el CPC barato de marca; nunca sabrás si el genérico es rentable (ver 39, 64).
- **Una campaña por producto** cuando tienes 20 productos y 2M COP/mes: 20 campañas con 0 conversiones cada una; ninguna calibra (ver 18).
- **15+ keywords de temas distintos** revueltas en un grupo: el RSA no sabe qué prometer y la landing no congruye (ver 48).
- **Reestructurar la cuenta cada semana**: cada cambio de estructura reinicia aprendizaje (ver 13). Decide bien una vez y déjala correr ≥3-4 semanas.
- **Copiar la estructura de Meta**: en Meta generas demanda con creativos y públicos (rutea a `facebook_ads_lushows` / `tiktok_ads_lushows`); en Google capturas demanda con intención y keywords. Lógicas opuestas (ver 02).
- **Naming caótico** (`copia de copia final 2`): a los 6 meses no puedes leer ni reportar la cuenta (ver 67).
- **Ignorar la campaña de Marca** "porque ya me encuentran": un competidor puja sobre tu nombre y le pagas a Google el tráfico que era tuyo gratis. Marca cuesta centavos y la necesitas (ver 39).
- **Abrir PMax como cuarta campaña con presupuesto chico**: deja a Search genérico sin comida y ninguna de las dos calibra (ver 12, 18).
