# 53 — Live Shopping ads

Lee este módulo cuando un cliente venda moda, belleza o productos que se lucen en vivo, cuando quieras un canal de venta con urgencia real (no fabricada), o cuando alguien te diga "vi que en TikTok venden transmitiendo en vivo, ¿cómo hago eso?". Live Shopping es el canal más potente de TikTok Shop para ciertos productos — y el más exigente en ejecución. Solo aplica donde TikTok Shop existe (ver 50). El frame sigue siendo **descubrimiento** (ver 00): el live agarra a alguien que pasaba scrolleando y lo convierte en comprador en tiempo real, con demostración y conversación.

## Qué es Live Shopping y por qué funciona

**Live Shopping** = vender **en vivo**, mientras transmites, con productos comprables durante el live. El espectador ve el producto en uso, hace preguntas en el chat, y compra **sin salir de la transmisión** (el producto aparece etiquetado abajo, con su precio). Sumas **ads** (LIVE Shopping Ads) para llevar más gente al live mientras está activo.

Por qué vende más que un video en ciertos casos:

1. **Demostración real en tiempo real.** El espectador ve cómo queda la ropa puesta, cómo se aplica el producto, cómo funciona. Mata la duda antes de que aparezca.
2. **Urgencia genuina.** "Quedan 5 unidades", "solo durante el live", "precio de transmisión" — la escasez es real, no un banner falso.
3. **Conversación que cierra.** Las objeciones se responden en vivo, en el chat. Es venta + soporte + prueba social al mismo tiempo (el oficio de responder objeciones está en `ventas_lushows`).
4. **Sesiones largas = mucha exposición.** Un live de 1–2 horas expone el producto cientos de veces a una audiencia que ya paró a ver. El CPM del tiempo de atención es imbatible cuando el host es bueno.

A jun-2026, en mercados con Shop maduro (Sudeste Asiático, y creciendo en MX/BR), el Live es uno de los mayores generadores de GMV. En LatAm sin Shop, el live **orgánico** sigue sirviendo para crear deseo y cerrar por WhatsApp (ver abajo).

## La mecánica de un live que vende

Un live que vende NO es prender la cámara y esperar. Estructura mínima:

| Bloque | Qué pasa | Tiempo |
|---|---|---|
| **Gancho de entrada** | Anuncias la oferta del live, das razón para quedarse | Primeros minutos |
| **Demo + venta** | Muestras producto en uso, lo etiquetas, llamas a comprar | Cuerpo del live |
| **Manejo de chat** | Respondes objeciones, repites la oferta, nombras a quien compra | Continuo |
| **Urgencia / cierre** | "Últimas unidades", "el precio sube al cerrar" | Cierre |
| **Re-loop** | Repites el ciclo para los que recién entran | Cada 10–15 min |

El **re-loop** es clave: en un live, la gente entra y sale todo el tiempo. Cada 10–15 minutos arrancas el ciclo de nuevo (oferta → demo → urgencia) para el que acaba de llegar. Si solo lo dices una vez, el 90% no lo escuchó.

### Cómo impulsar el live con ads (LIVE Shopping Ads)

1. Lanzas un anuncio que lleva tráfico **al live mientras está en vivo** (LIVE promotion). El ad solo corre durante la transmisión.
2. Creativo nativo que diga "estoy en vivo AHORA, entra" — urgencia explícita (ver 30).
3. Coordina horario: el equipo de pauta debe lanzar/pausar el ad exactamente cuando empieza y termina el live.
4. Optimiza por **clics al live / vistas del live** o, si la cuenta lo permite, por **compra durante el live**.

Requisitos: TikTok Shop activo, catálogo sano con stock real (ver 56), y alguien con tablas frente a cámara — el host hace o rompe el live. Un host tímido o sin guion no vende ni con el mejor ad.

## Calendario y frecuencia (el live recompensa la constancia)

El live no es un evento único; es un canal que mejora con repetición. El algoritmo aprende tus horarios y tu audiencia se acostumbra a "el live de los jueves". Plantilla de arranque:

| Frecuencia | Para quién | Duración por live |
|---|---|---|
| 1–2 lives/semana | Marca que arranca | 45–90 min |
| 3–5 lives/semana | Marca con tracción | 60–120 min |
| Diario | Operación dedicada de live commerce | 90–180 min |

Mejores horarios suelen ser **noche** (7–10 pm) cuando la gente scrollea relajada. Prueba 2–3 franjas y mídelas con tus números reales (ver 57). Un solo live aislado casi nunca rinde — la primera semana es de aprendizaje.

## Cuándo el live gana (y cuándo no)

**El live gana cuando:**
- El producto **se luce mostrándose**: moda (ver 84), belleza, accesorios, gadgets, comida.
- Hay **inventario y stock real** para sostener urgencia.
- Tienes un **host con presencia** (creador o el dueño carismático).
- Puedes transmitir **con frecuencia** (el live recompensa la constancia, no el one-shot).

**El live NO es para:**
- High-ticket que necesita conversación 1:1 → lead calificado (ver 58).
- Negocios sin alguien cómodo frente a cámara.
- Países sin TikTok Shop → haz el live **orgánico** para crear deseo y cierra por WhatsApp (ver 55).
- Catálogos sin stock — la urgencia falsa quema la audiencia.

## Live sin Shop (LatAm / Colombia hoy)

Si no hay TikTok Shop (verifica, ver 50), el live sigue sirviendo, pero el cierre cambia:

1. Transmites en vivo mostrando el producto (orgánico, sin etiqueta de compra).
2. En pantalla y por voz repites: "escríbeme al WhatsApp que dejo fijado para apartarlo".
3. Mensaje prellenado "vengo del live de TikTok, quiero apartar X" (ver 55).
4. El cierre lo hace `ventas_lushows` (módulo 82). Para una web/landing con catálogo, `desingweb-lushows`.

No es tan fluido como el checkout en vivo, pero crea deseo igual de bien. El live es máquina de antojo aunque no haya Shop.

## Rutas a skills hermanas

- Host / creadores para el live (Spark Ads, Creator Marketplace) → 32.
- Cierre del chat y objeciones en vivo → `ventas_lushows`.
- Cierre por WhatsApp sin Shop → 55 + `ventas_lushows` (módulo 82).
- Moda en vivo (talla, color, devoluciones) → 84.
- Equivalente live commerce en otras plataformas → `facebook_ads_lushows` (Live de Meta).

## Errores comunes — blacklist

- **Prender la cámara sin guion ni oferta.** El live sin estructura no vende; arma bloques y re-loops cada 10–15 min.
- **Host sin presencia frente a cámara.** Mata el live; entrena al host o usa un creador (ver 32).
- **Urgencia falsa con stock infinito.** La audiencia lo huele; usa escasez real (ver 56).
- **Lanzar ads de LIVE promotion sin estar transmitiendo.** El ad solo sirve durante el live; coordina horarios al minuto.
- **Hacer un solo live y esperar resultados.** El live recompensa frecuencia; programa una rutina semanal.
- **Ignorar el chat.** Las objeciones sin responder se van sin comprar (ver `ventas_lushows`).
- **No re-loopear la oferta.** El que entró tarde no escuchó nada; repite el ciclo.
- **Intentar live shopping con checkout sin TikTok Shop activo.** No hay carrito en vivo; haz live orgánico y cierra por WhatsApp (ver 50, 55).
