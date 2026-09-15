# 41 — Demand Gen campaigns

Lee este módulo cuando quieras correr en Google una campaña que se sienta como Meta —visual, de generación de demanda, con destino lead o WhatsApp— y no sepas cuál es. La respuesta es **Demand Gen**. Es la pieza donde Google deja de solo *capturar* a quien te busca y empieza a *generar* interés en quien no te buscaba todavía, mostrándote dentro de superficies visuales propias. Es lo más cerca que Google llega a `facebook_ads_lushows`; la diferencia es que aquí no sales del ecosistema Google y aprovechas las señales de intención (búsquedas, historial, suscripciones) que Meta no tiene. Su uso afinado para Colombia y LatAm está en 46; aquí va la mecánica de cómo se arma por dentro.

## Qué es y qué reemplazó

A finales de 2023 / inicio de 2024 Demand Gen **reemplazó por completo a las campañas Discovery**, y para jun-2026 ese reemplazo ya está consolidado y madurado: Discovery no existe en ninguna cuenta. Si alguien todavía te habla de "Discovery", está leyendo tutoriales viejos. Demand Gen corre en las superficies más "scrolleables" de Google:

| Superficie | Qué es | Formato dominante |
|---|---|---|
| YouTube in-stream e in-feed | Video saltable y sugerencias de video | Video 16:9 + vertical |
| YouTube Shorts | Verticales tipo Reels | Video 9:16 |
| Gmail | Anuncios en pestañas Promociones/Social | Imagen 1:1 / 1.91:1 |
| Google Discover | El feed de contenido del celular (Android e iOS) | Imagen + video |

Son los lugares donde la gente *navega y descubre*, no donde *busca*. Por eso Demand Gen es visual (imagen y video mandan) y funciona para generación de demanda, no para captura de intención explícita como Search.

### Novedades jun-2026

- **Channel controls:** ya puedes elegir en qué superficies corre (por ejemplo, solo YouTube + Shorts, sin Gmail/Discover) — útil cuando un canal te trae leads chatarra.
- **Objetivo de "vistas" y de "lead"/WhatsApp** disponibles nativamente; el destino de mensajería (clic-a-WhatsApp) es lo que la vuelve el reemplazo natural de la campaña de mensajes de Meta en LatAm (ver 46).
- **Gemini** genera y adapta assets dentro del flujo de creación: variaciones de imagen, recortes y image-to-video (ver 91).
- **Reporting de assets** más granular (Mejor/Bueno/Bajo por pieza) para iterar limpio (ver 49).

## Cómo se arma — las tres piezas

Una Demand Gen vive de tres insumos. Si uno falla, la campaña no levanta.

1. **Assets visuales.** Necesitas video (skippable, idealmente con hook en 5s — ver 42) e imágenes en **varias proporciones obligatorias**. Specs jun-2026:

   | Tipo | Proporción | Tamaño recomendado | Límite |
   |---|---|---|---|
   | Imagen horizontal | 1.91:1 | 1200×628 px | ≥600×314 |
   | Imagen cuadrada | 1:1 | 1200×1200 px | ≥300×300 |
   | Imagen vertical | 4:5 / 9:16 | 960×1200 / 1080×1920 | — |
   | Logo | 1:1 y 4:1 | 1200×1200 / 1200×300 | — |
   | Video | 16:9, 1:1, 9:16 | ≥720p | 5s–60s+ |
   | Títulos | hasta 5, ≤40 caracteres | — | — |
   | Descripciones | hasta 5, ≤90 caracteres | — | — |

   Google arma combinaciones automáticamente; tú das el material crudo. La dirección de arte de ese material se trabaja en `directorcreativo_lushows`; con IA/Gemini puedes generar variaciones, incluso image-to-video de un asset estático (ver 91).

2. **Audiencias.** Demand Gen usa **segmentos similares** (el equivalente de Google a los lookalike de Meta): le das una lista-semilla (clientes, gente que convirtió) y Google busca gente parecida. También usas tus audiencias propias —remarketing (ver 24) y Customer Match (ver 25)— y segmentos por intereses/intención (ver 23). La combinación **lista-semilla + similares** es la que mejor rinde en LatAm (ver 46). A jun-2026 la lista-semilla mínima útil es de **~1.000 contactos**; con menos, los similares arrancan a ciegas.

3. **Product feed (si vendes catálogo).** Puedes conectar un feed de Merchant Center para que el anuncio muestre artículos concretos con precio (ver 45). Para un solo producto digital no es indispensable; para e-commerce con varios SKU, sí — convierte un video genérico en vitrina con precios.

El destino lo defines tú: sitio web, formulario de lead nativo (ver 52) o **WhatsApp/llamada** — y ese destino es justo lo que hace a Demand Gen el reemplazo natural de una campaña de mensajes de Meta en mercado colombiano.

## Cuándo usarla — y cuándo no

| Situación | ¿Demand Gen? |
|---|---|
| Quieres volumen de leads/WhatsApp con video, dentro de Google | Sí, es su terreno |
| Tienes buenos assets visuales (o los puedes producir/generar con IA) | Sí |
| Marca nueva sin tráfico ni lista de clientes | Sirve, pero arranca con segmentos similares amplios y paciencia (semilla pequeña = aprendizaje lento) |
| Solo tienes texto, cero video ni imágenes decentes | No — sin creativo visual no funciona. Vete a Search |
| Búsqueda transaccional caliente ("comprar X ya") | No es para eso — eso es Search (captura de intención) |
| Quieres diversificar y no depender solo de Meta | Sí, esa es la jugada (ver 46) |

**Regla honesta para Colombia:** Demand Gen **complementa** a Search y a Meta, no los reemplaza. Search captura al que ya decidió; Meta genera demanda fría masiva; Demand Gen genera demanda dentro de Google con tus assets y señales de intención. Si tienes poco presupuesto y cero creativo, **primero Search**. Demand Gen entra cuando ya tienes video y una lista de clientes para alimentar los similares.

### Presupuesto y arranque (jun-2026)

- **Mínimo operativo:** ~$30.000–$50.000 COP/día para que la puja inteligente reúna data en tiempo razonable. Por debajo de eso, aprende lento y los resultados son ruido.
- **Puja:** arranca con *Maximizar conversiones*; cuando tengas ~30 conversiones en 30 días, pasa a **tCPA** con tu costo objetivo (ver 13).
- **Periodo de aprendizaje:** 1–2 semanas. No la apagues a las 48h por pánico (ver 13, 61).

## Plantilla de brief Demand Gen

```
OBJETIVO: lead / WhatsApp / vistas / ventas
DESTINO: WhatsApp directo / lead form (52) / landing (33,48)
ASSETS:  video 16:9 ___  video 9:16 ___  imágenes 1:1 ___  1.91:1 ___  4:5 ___
         títulos (5) ___  descripciones (5) ___  CTA: "________"
AUDIENCIAS: Customer Match (lista ___ contactos) + similares + remarketing (24)
            + intereses: ________
PRESUPUESTO: $______/día   PUJA: Max conversiones → tCPA $______ COP
CONGRUENCIA destino: el video promete "____" y el destino abre con "____" (48)
```

## Errores comunes — blacklist

1. **Buscar "Discovery" en la cuenta.** Ya no existe; es Demand Gen desde 2024 y consolidado en 2026. Estás con tutoriales viejos.
2. **Lanzar sin video ni imágenes de calidad.** Demand Gen es 100% visual; sin assets buenos no rinde. El creativo es el 80% del resultado (dirección en `directorcreativo_lushows`).
3. **Esperar conversiones transaccionales inmediatas como en Search.** Es generación de demanda; la gente descubre, no busca comprar ese segundo. Mide con ventana de conversión más larga (ver 65).
4. **No darle audiencias-semilla (o darle <1.000 contactos).** Sin lista decente, los similares arrancan a ciegas. Sube tu Customer Match primero (ver 25).
5. **Mezclar Demand Gen con Search en el mismo reporte mental.** Tienen objetivos distintos (generar vs capturar); compararlas por el mismo CPA te lleva a apagar la que sí trabaja a largo plazo.
6. **Usar una sola imagen y un solo video.** Necesita variedad para combinar y aprender. Dale 3–5 piezas por tipo y proporción (ver 49 testing).
7. **Ignorar la congruencia anuncio→destino.** Si el video promete una cosa y la landing dice otra, el clic se pierde. El mensaje debe calzar de punta a punta (ver 48).
8. **Dejar todos los canales activos cuando uno trae basura.** Usa los channel controls (jun-2026) para apagar Gmail/Discover si te llenan de leads chatarra.
