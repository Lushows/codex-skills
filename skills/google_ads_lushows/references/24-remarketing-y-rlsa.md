# 24 — Remarketing y RLSA

Lee este módulo cuando quieres recuperar a la gente que ya te visitó y no compró, o cuando tu Search funciona pero sientes que dejas dinero en la mesa con quien estuvo a punto. El **remarketing** vuelve a mostrarle anuncios a quien ya interactuó contigo. Es casi siempre el tráfico más barato y de mayor conversión que tendrás — porque ya te conocen. En captura de demanda (Google) el remarketing es el cierre del círculo: alguien buscó, llegó, dudó; tú lo traes de vuelta. En jun-2026, con las cookies de terceros degradándose, el remarketing se apoya cada vez más en tus datos propios y en Consent Mode bien puesto (ver 25, 28, 29) — sin consentimiento, tus listas dejan de crecer.

## Las dos familias: remarketing visual vs RLSA

Hay dos formas muy distintas, y se confunden:

| | Remarketing visual | RLSA |
|---|---|---|
| Dónde aparece | Display, YouTube, Demand Gen, Gmail | Resultados de **búsqueda** (Search) |
| Qué hace | Te persigue con banners/videos por la web | Cuando tu visitante **vuelve a buscar**, ajusta tu puja o muestra anuncios distintos |
| Necesita que la persona | Solo haya visitado | **Vuelva a buscar en Google** algo relevante |
| Formato | Imagen / video | Texto en la búsqueda |
| Tamaño mínimo de lista | ~100 usuarios (Display) | ~1.000 usuarios (Search) |

**RLSA = Remarketing Lists for Search Ads** (listas de remarketing para anuncios de búsqueda). Es la joya que poca gente usa bien.

## RLSA: por qué es tan potente

RLSA no te muestra anuncios "porque sí". Espera a que tu visitante **vuelva a buscar** en Google algo relacionado — o sea, sigue habiendo intención fresca — pero como ya te conoce, puedes:

1. **Pujar más alto por él.** Vale más que un desconocido: ya pasó por tu sitio. Ajuste de puja +30%, +50%, +100% según convierta (ver 15).
2. **Pujar por keywords más amplias y caras** que con un desconocido no te arriesgarías. Ejemplo: por la keyword genérica "calculadora de costos" (cara, ambigua) normalmente no pujas fuerte; pero a alguien que YA visitó tu landing, sí — porque sabes que encaja. Esto se llama "RLSA broad": abres keywords amplísimas pero SOLO para visitantes, segmentando la lista (no en observación). Es de las jugadas más rentables que existen.
3. **Mostrarle un anuncio distinto:** "¿Volviste? Llévate la calculadora hoy con 10% off" en vez del mensaje frío inicial.

Modo de uso: agrega tu lista de remarketing a la campaña de Search en **observación** (ver 23) para subir puja, o crea una campaña RLSA aparte con segmentación + keywords amplias solo para visitantes. Para RLSA necesitas que la lista tenga tamaño mínimo (~1.000 usuarios activos para Search). Si tu tráfico es bajo, tardarás en juntarla; paciencia — mientras tanto el remarketing visual (umbral más bajo) sí corre.

## Ventanas, listas y exclusiones de compradores

**Ventanas (membership duration):** cuántos días alguien permanece en la lista tras visitarte. Define por ciclo de compra:
- Producto de decisión rápida y barata ($10.000 COP): 7–30 días basta.
- Producto caro o de decisión lenta (B2B, ver 27): 90–180 días, hasta 540 máximo.

**Listas que deberías tener armadas** (Audience Manager → Segmentos de datos):
- Todos los visitantes (la base).
- Visitantes de la landing que NO llegaron a "gracias por tu compra" (los que dudaron — tu lista más rentable).
- Visitantes que pasaron X tiempo o vieron varias páginas (más calientes).
- Carrito/checkout abandonado, si tienes ecommerce.
- Compradores (para EXCLUIR o para vender otra cosa).

Plantilla de regla para "abandonadores": `visitó /landing` Y `NO visitó /gracias`, ventana 30 días. Esa es la que más convierte por peso invertido.

**Exclusión de compradores — clave y olvidada:** si alguien ya compró, EXCLÚYELO del remarketing de ese mismo producto. Perseguir con anuncios a quien ya pagó es quemar plata y molestar. Excepción: si tienes un segundo producto o recompra, móntale una campaña aparte que SÍ le hable a compradores (ver 25 para listas de clientes, 97 omnicanal).

Para configurar listas necesitas el **Google tag** bien instalado en todo el sitio (ver 14, 28) y Consent Mode v2 funcionando (ver 29). Sin eso, no hay remarketing — es lo primero que debes verificar. En 2026, sin consentimiento del usuario, ni siquiera entra a la lista.

## Dónde corre cada uno

- **RLSA:** dentro de tus campañas de Search existentes (capa de observación) o campaña RLSA-broad dedicada (segmentación).
- **Remarketing visual:** campaña de Display dedicada, o dentro de Demand Gen (ver 41) y YouTube (ver 40). Demand Gen es hoy el mejor hogar del remarketing visual: combina formatos de imagen y video en los inventarios premium de Google (YouTube, Discover, Gmail).
- **PMax** ya hace remarketing por dentro automáticamente — por eso a veces compite con tus campañas de remarketing dedicadas; vigila el solapamiento (ver 12). Si PMax y tu remarketing pujan por el mismo usuario, te encareces solo.

El cierre final del visitante recuperado — cuando ya hizo clic y escribe — lo trabaja `ventas_lushows`; la landing que lo recibe, `desingweb-lushows`. El remarketing solo lo trae de vuelta; cerrar es otro oficio.

## Escalera de remarketing por temperatura

No le hables igual a todos los que volvieron. Arma una escalera de listas con mensaje y puja distintos según qué tan caliente está cada uno:

| Temperatura | Quién es | Mensaje / oferta | Puja |
|---|---|---|---|
| Caliente | Abandonó checkout / carrito en últimas 72h | "Termina tu compra hoy, te queda 1 paso" | +100% / agresiva |
| Tibio | Vio la landing, no compró, últimos 7 días | Resolver la objeción típica (precio, confianza) | +50% |
| Frío | Visitó hace 8–30 días | Recordatorio de valor + prueba social | +20% |
| Reactivación | Visitó hace 30–90 días, nunca compró | Oferta de regreso o ángulo nuevo | observación |

Cada peldaño merece su creatividad: el caliente recibe urgencia, el frío recibe recordatorio, el de reactivación recibe una razón nueva para volver. Esto se monta combinando listas de distinta ventana (ver arriba) con exclusiones entre ellas (el de 72h NO debe recibir también el mensaje de 30 días — exclúyelo de la lista más fría para que cada uno reciba un solo mensaje). Para producto de ticket bajo como la calculadora ($10.000 COP), no inviertas en 4 escalones — basta caliente (abandonó) + tibio (visitó); la complejidad solo se paga sola con ticket o ciclo más alto (B2B, ver 27).

## Errores comunes — blacklist

1. **No tener remarketing montado.** Es el tráfico más barato y de mayor conversión. No tenerlo es regalar dinero. Instala el Google tag y arma las listas hoy.
2. **No excluir a los compradores.** Persigues con anuncios a quien ya pagó: plata quemada y mala experiencia. Excluye o véndele algo distinto, nunca lo mismo.
3. **Confundir RLSA con remarketing visual.** RLSA es en BÚSQUEDA y necesita que la persona vuelva a buscar. Si esperabas banners, eso es Display/Demand Gen.
4. **Ventana de membresía mal calibrada.** 180 días para un producto de compra inmediata = perseguir gente que ya perdió interés. Ajusta al ciclo real.
5. **Esperar RLSA con tráfico minúsculo.** Necesita ~1.000 usuarios en la lista para Search. Con poco tráfico, no se activa; genera volumen o usa remarketing visual mientras.
6. **No subir la puja a los visitantes que vuelven.** RLSA en observación sin ajuste de puja = no estás usando RLSA, solo mirándolo. El valor está en pujar MÁS por quien ya te conoce.
7. **Olvidar que PMax ya hace remarketing.** Puedes estar duplicando esfuerzo y compitiendo contra ti mismo. Revisa solapamiento antes de montar otra campaña.
8. **No tener Consent Mode v2.** Sin consentimiento las listas dejan de crecer y el remarketing se seca (ver 29). Verifícalo antes de culpar al algoritmo.
