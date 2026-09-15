# 23 — Retargeting que no quema

**Retargeting** (remarketing) = mostrarle anuncios a quien YA tuvo contacto contigo: vio tu video, entró a la web, dejó el carrito. Lee este módulo cuando tengas tráfico de prospección corriendo (ver 20) y quieras recuperar a los que no compraron a la primera. La trampa: el retargeting mal hecho **quema** — le martillas el mismo anuncio 15 veces a las mismas 800 personas, te empiezan a odiar, el CTR colapsa y el CPA se dispara. Aquí está cómo hacerlo sin incendiar tu audiencia, con las ventanas, frecuencias y exclusiones exactas.

## Antes que nada: ¿tienes con qué?

El retargeting solo funciona si la prospección llena el embudo. En TikTok (descubrimiento puro, ver 20) la fuente de tibios es:

- **Video viewers** (vieron 25/50/75/95% de tus videos, ver 21) — los más abundantes y baratos.
- **Engagement** (interactuaron con perfil/posts, orgánicos incluidos).
- **Web/Pixel** (visitaron, vieron producto, agregaron al carrito, ver 14).
- **Shop** (abandonos de carrito, ver 50).

Si tu prospección es chica, el retargeting es chico. Primero alimenta el embudo; el retargeting es el segundo piso, no los cimientos. Una cuenta que gasta $30.000 COP/día en prospección genera muy pocos tibios diarios — no esperes un retargeting robusto hasta que el descubrimiento mueva volumen real.

## Ventanas y mensaje por etapa

No a todos el mismo anuncio. Cada etapa pide otra conversación:

| Audiencia | Ventana | Mensaje del creativo | Oferta |
|---|---|---|---|
| Video viewers 50-95% | 7-30 días | Profundiza el beneficio que ya vieron; prueba social | CTA suave, sin descuento aún |
| Visitó web / vio producto | 7-14 días | Resuelve la objeción que lo frenó (precio, confianza, envío) | Garantía, testimonios |
| Agregó al carrito / inició checkout | 1-7 días | "Te falta poco"; urgencia real | Envío gratis o descuento puntual |
| Abandono de carrito Shop | 1-3 días | Recordatorio directo del producto exacto | Incentivo de cierre |

Mientras más caliente, más corta la ventana y más directa la oferta. Al video viewer de hace 25 días le hablas suave (apenas te recuerda); al de carrito abandonado de ayer le das el empujón final con urgencia real, no inventada. Regla práctica: la urgencia falsa ("¡últimas horas!" cada día) quema confianza; usa escasez genuina (stock real, fecha real, bono que sí vence).

## Frecuencia: el termómetro anti-quema

La **frecuencia** es cuántas veces ve tu anuncio la misma persona en un periodo. En retargeting es el número que más vigilas:

- **Frecuencia sana en retargeting**: ~1.5-3 cada 7 días. Por encima de 4-5 en una semana, estás martillando y la audiencia se satura.
- Si la frecuencia sube y el CTR baja → fatiga (ver 39). Refresca creativo o amplía la ventana para meter aire fresco.
- **Cap de frecuencia**: configúralo en el ad group cuando la audiencia es chica (límite de cuántas veces puede aparecer por persona por X días).
- Audiencia chica + presupuesto alto = frecuencia explota matemáticamente. Si tienes 1.500 personas y le metes $50.000 COP/día, las saturas en 48 horas. Baja presupuesto o amplía la ventana ANTES de quemar, no después.

Regla de bolsillo: el retargeting rara vez aguanta más de 15-20% del presupuesto total — es audiencia chica, y forzar plata sube la frecuencia sin subir las ventas.

## Exclusiones obligatorias (o pagas dos veces)

Todo ad group de retargeting DEBE excluir:

1. **Compradores** (Shop/GMV o lista, ver 24) — salvo que vendas recompra/recurrente (ver 25).
2. **Etapas más calientes ya cubiertas por otro ad group** — si tienes un ad group para "carrito abandonado", exclúyelo del ad group de "visitó web", o pujas por el mismo ojo dos veces (ver 24).
3. **Leads ya capturados** (ver 21) si tu objetivo era el lead, no la venta.

Sin exclusiones, el solapamiento te sube el costo y distorsiona qué etapa funciona de verdad.

## Estructura recomendada (acciones exactas)

1. Campaña separada "RETARGETING" (no mezclada con prospección; quieres ver su CPA aislado, no contaminado por el frío).
2. Ad groups en escalera de temperatura, del más caliente al más frío, con exclusión descendente:
   - **AG1**: carrito/checkout 1-7d → excluye compradores.
   - **AG2**: visitó web 7-14d → excluye compradores + AG1.
   - **AG3**: video viewers 95% 7-30d → excluye compradores + AG1 + AG2.
3. Creativo distinto por etapa (no el mismo de prospección reciclado; el tibio ya lo vio).
4. Cap de frecuencia si las audiencias son chicas.
5. Presupuesto modesto: el retargeting cierra a poca gente; no le metas el grueso del budget (eso va a prospección/descubrimiento, ver 25).

### Plantilla de mensaje por etapa (e-com LatAm)

- **Carrito 1-7d**: "¿Se te quedó en el carrito? Hoy con envío gratis a [ciudad]. Te llega en 48h." + testimonio corto.
- **Visitó web 7-14d**: "La duda #1 que nos hacen: ¿y si no me funciona? Por eso tienes garantía de [X]." (mata la objeción que lo frenó).
- **VV 95% 7-30d**: testimonio fuerte + demo del resultado, sin presión. Lo acerca, no lo cierra a la fuerza.

## Dónde termina el retargeting

El retargeting trae el clic de vuelta; el cierre lo hace la conversación o la landing. Para que el tibio que escribe por WhatsApp cierre, rutea a `ventas_lushows`. Para que la landing convierta el clic recuperado, `desingweb-lushows`. Si dudas de si el retargeting paga (audiencia pequeña + ticket bajo a veces no justifica el esfuerzo), valida la unidad económica con `economist_lushows`. Si vienes de Meta, la lógica es parecida pero las ventanas y la dependencia del creativo cambian — ver `facebook_ads_lushows`.

## Errores comunes — blacklist

1. **Mismo anuncio que prospección, repetido.** El tibio ya lo vio; necesita otro ángulo que resuelva su objeción.
2. **Una sola ventana para todos.** El de carrito de ayer y el video viewer de hace un mes no son lo mismo.
3. **Ignorar la frecuencia.** Por encima de 4-5/semana en audiencia chica, los quemas y el CPA explota.
4. **No excluir compradores.** Pagas por venderle a quien ya tiene el producto.
5. **No excluir etapas entre ad groups.** Pujas dos veces por el mismo ojo (ver 24).
6. **Meter el grueso del presupuesto en retargeting.** Es audiencia chica; el volumen y el CPA escalable viven en el descubrimiento/prospección.
7. **Hacer retargeting sin prospección sana.** Sin embudo lleno, el retargeting se queda sin gente y se quema solo.
8. **Urgencia falsa permanente.** "Últimas horas" todos los días entrena a tu audiencia a no creerte; usa escasez real.
