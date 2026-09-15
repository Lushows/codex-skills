# 23 — Retargeting que no quema

**Retargeting** (o remarketing) es mostrar anuncios a gente que ya te conoce: visitó tu web, vio tu producto, dejó el carrito. Es el dinero más barato de la cuenta cuando se hace bien, y la forma más rápida de fastidiar gente cuando se hace mal. Lee este módulo cuando vayas a montar tu primera campaña de retargeting o cuando la que tienes tenga frecuencia 15 y la gente te comente "ya déjame en paz".

## El cambio de 2026 que TIENES que saber primero

El **12-ene-2026 Meta quitó las ventanas view-through de 7 y 28 días del Ads Insights API**. Solo quedan ventanas por **clic**. Esto golpea directo al retargeting, porque históricamente el retargeting inflaba su ROAS atribuyéndose vistas (alguien vio el ad, no clickeó, y compró igual → se lo cobraba). Con view-through fuera del reporte, tu retargeting va a **mostrar menos conversiones atribuidas** — y eso es bueno: es más cerca de la verdad. No te asustes ni subas presupuesto para "recuperar" esas conversiones fantasma; nunca fueron tuyas. Estándar de medición hoy: **7d-click / 1d-view**. Si quieres saber cuánto vende DE VERDAD el retargeting, mídelo con un geo-holdout o prueba de apagado (ver 65/84), no con el reporte de plataforma.

## Ventanas por temperatura

La **ventana** es cuántos días hacia atrás incluyes. Regla: a mayor intención mostrada, ventana más corta y mensaje más directo.

| Público | Ventana | Temperatura | Qué hizo |
|---|---|---|---|
| Visitó el sitio (cualquier página) | 30-60d | Tibio | Curioseó |
| Vio producto (ViewContent) | 14-30d | Tibio-caliente | Miró algo concreto |
| Agregó al carrito (AddToCart) | 7-14d | Caliente | Casi |
| Inició checkout (InitiateCheckout) | 7d | Muy caliente | Lo frenó algo puntual |
| Engagers IG/FB, video viewers 50%+ | 30d | Tibio | Te conoce de contenido (ver 21) |

Después de la ventana, esa persona vuelve a ser fría: déjala ir (la recuperas con prospecting o email/WhatsApp, ver 96).

## Mensaje por etapa: NO repitas el ad de prospecting

El error #1 del retargeting es mostrarle a todos el mismo anuncio con el que llegaron. Ya lo vieron; no funcionó. Cada etapa necesita un trabajo distinto:

- **Visitó/vio producto → RECORDAR + diferenciar**: prueba social ("4.8★ de 600 clientes"), el diferenciador clave, contenido que profundiza. No grites "¡COMPRA YA!" a quien solo curioseó.
- **Carrito → REBATIR LA OBJECIÓN**: ¿por qué no compró? Casi siempre: precio/envío/desconfianza. Anuncio que responde eso: "Envío gratis a toda Colombia", "Pagas al recibir (contraentrega)", "Garantía de 30 días o te devolvemos la plata". En LatAm, la contraentrega rebate la desconfianza mejor que cualquier copy.
- **Checkout → EMPUJÓN FINAL**: urgencia honesta (stock real, fecha real de cierre), testimonio espejo (alguien IGUAL al cliente contando su resultado), o un incentivo pequeño si tu margen lo aguanta. Cuidado con entrenar a la gente a abandonar el carrito para recibir descuento: úsalo con moderación o sin cupón.

Para e-com con catálogo: usa **DPA** (dynamic product ads, ver 56) — Meta le muestra a cada persona EXACTAMENTE el producto que vio, automático. Es el retargeting de carrito en piloto automático.

### Mini-swipe de retargeting por etapa (e-com $120k COP, contraentrega)

- **Vio producto (tibio)**: "Más de 600 colombianos ya lo usan a diario ⭐ 4.8/5. Esto cambió para ellos: [carrusel de 3 reseñas]. ¿Dudas? Escríbenos."
- **Carrito (caliente)**: "Tu pedido sigue esperando 👀 Pagas cuando lo recibes — contraentrega en toda Colombia. Sin tarjeta, sin riesgo."
- **Checkout (muy caliente)**: "Despachamos esta semana y quedan pocas unidades. 30 días de garantía: si no te sirve, te devolvemos la plata. Termina aquí 👇"

## Frecuencia: la línea entre presencia y acoso

**Frecuencia** = impresiones ÷ personas alcanzadas (cuántas veces vio tu ad la misma persona). Vigílala en Ads Manager (columna "Frequency", mírala por semana, no de por vida; Meta recortó la retención de frecuencia a 6 meses en 2026, así que miras tramos recientes igual).

- BOFU (fondo de embudo: carrito/checkout): **3-6 por semana** es tolerable — está decidiendo, recordarle ayuda.
- Tibio (visitantes/engagers): 2-4 por semana.
- Señales de quemado: frecuencia >6-8/semana + CTR cayendo + comentarios negativos → baja presupuesto, rota creativos o acorta la ventana. Recuerda que la vida útil del ad bajó a 2-4 semanas (Entity ID, ver 20): rota antes de que fatigue.

## Exclusiones: SIEMPRE

Toda campaña de retargeting excluye **compradores** (evento Purchase o customer list, ver 24 y 28). La ventana de exclusión depende del ciclo de recompra:

- Producto de compra única o ciclo largo (muebles, equipos): excluye 180d.
- Consumible con recompra (suplementos, comida, cosmética): excluye 30-60d y luego déjalos reentrar — o mejor, campaña/flujo de recompra aparte con mensaje de reposición ("¿se te está acabando?").

Caso WhatsApp-first (sin web): tu "carrito abandonado" es el que preguntó precio y desapareció. Eso no se retargetea con ads sino con seguimiento directo en el chat (guiones de follow-up en **ventas_lushows**); el ad de retargeting cubre a los engagers que nunca escribieron (ver 21 y 51). Si corres CTWA, la ventana gratis de 72h del chat (ver 53) es tu mejor "retargeting": responder y reabrir conversación gratis dentro de esa ventana vence a cualquier ad pagado.

## ¿Vale la pena como campaña separada? (la pregunta del tamaño)

El retargeting como campaña aparte necesita volumen: con públicos de menos de ~1.000-2.000 personas, el ad set no sale de aprendizaje, la frecuencia se dispara y micro-gestionas $20k COP/día. Regla práctica:

- **Tráfico chico** (< 5-10k visitas/mes): NO montes campaña de retargeting separada. Tu campaña broad/Advantage+ Sales (ver 12) ya re-alcanza a tus visitantes solita — el remarketing vive DENTRO de ella. Dedica tu energía a prospecting y creativos.
- **Tráfico medio-alto**: campaña separada con **10-20% del presupuesto total** (ver 18). Más que eso = estás cobrando ventas que iban a pasar igual y dejando de llenar el embudo.

## El argumento honesto del retargeting (incrementalidad)

El ROAS del retargeting es engañosamente bonito porque cobra ventas que el prospecting ya sembró. Antes el view-through inflaba esto; ahora que se fue (ene-2026), la inflación baja pero no desaparece (el click-through también incluye gente que compraba igual). La única forma de saber cuánto **causa** tu retargeting es la incrementalidad: apaga el retargeting en una región y compara ventas totales vs. la región donde sigue activo (geo-holdout, ver 65). Muchas cuentas descubren que la mitad de su "ROAS de retargeting" era inevitable. No es para que lo apagues — es para que no le robes presupuesto al prospecting que sí trae gente nueva.

## Errores comunes — blacklist

- Repetir el creativo de prospecting en retargeting: ya lo vieron y no compraron; necesitas otro ángulo, no otra impresión.
- Retargeting sin excluir compradores: pagas por perseguir a quien ya pagó, y lo irritas.
- Ventanas de 180d "para tener más audiencia": le hablas como caliente a alguien que ya te olvidó.
- 50% del presupuesto en retargeting porque "ahí está el ROAS": el ROAS bonito del retargeting vive de las ventas que el prospecting siembra; si dejas de sembrar, en 3 semanas no hay a quién retargetear.
- Inflar el retargeting con view-through: ya no existe en el API desde ene-2026; juzga por click y valida con holdout.
- Públicos diminutos en campaña aparte (300 personas en carrito): frecuencia 20, CPM altísimo, cero aprendizaje. Métela en el broad.
- Atribuirle al retargeting ventas que eran inevitables: si alguien inició checkout, quizá compraba igual sin tu ad. Mide con prueba de apagado si dudas (ver 84).
- Urgencia falsa ("¡última unidad!" todos los días): la gente lo nota, Meta lo penaliza y un reporte te puede costar el ad (ver 93).
