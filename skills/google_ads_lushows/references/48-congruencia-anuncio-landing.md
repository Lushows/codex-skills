# 48 — Congruencia anuncio→landing

Lee este módulo cuando tus anuncios tengan buen CTR (mucha gente hace clic) pero pocas ventas, o cuando sospeches que estás pagando clics que rebotan en la página. El problema casi siempre es el mismo: **el clic no perdona el salto de mensaje.** La persona hizo clic porque el anuncio prometió algo; si la landing no le devuelve esa misma promesa en el primer segundo, se va — y pagaste el clic para nada. A esto se le llama **message match** (coincidencia de mensaje): que lo que prometió el anuncio sea lo primero que ve y entiende en la página. La **construcción de la landing** es oficio de `desingweb-lushows`; aquí defines qué debe contener para no quemar el clic. La voz/tono que debe mantenerse viene de 47; el sistema de marca, de `directorcreativo_lushows`.

## Qué es message match y por qué el clic se pierde sin él

Imagina la cabeza de quien hizo clic: "vi un anuncio que decía *Calculadora de costos para tu restaurante, $10.000, descarga hoy*". Llega a la página y… ve un texto de "Soluciones integrales de gestión empresarial gastronómica". En medio segundo piensa "esto no es lo que vi" y cierra. El anuncio y la landing tienen que ser **la misma conversación**:

| El anuncio prometió… | La landing debe mostrar (arriba, sin scroll)… |
|---|---|
| El producto exacto | Ese producto, con su nombre tal cual |
| El precio ($10.000 COP) | El mismo precio visible de una vez |
| El beneficio principal | El mismo beneficio como titular (H1) |
| La acción (descargar/WhatsApp) | Ese botón, arriba, sin buscarlo |
| El tono (colombiano práctico) | El mismo tono (ver 47) |
| La oferta/urgencia ("hoy", "pago único") | La misma oferta, sin letra chica que la contradiga |

Si las filas coinciden, el clic "aterriza suave". Si una sola se rompe —sobre todo precio o producto— el clic rebota. Y un clic en Search transaccional no es barato: en Colombia un clic de intención caliente cuesta fácil **$800–$4.000 COP**; cada rebote por incongruencia es plata literal en la basura.

## Message match no es solo Search

La congruencia aplica a **todos** los formatos, no solo a la búsqueda:

- **Video (YouTube/Demand Gen):** si el video dice "$10.000 y te lo enviamos hoy por WhatsApp", el destino debe abrir justo en eso. Un video que promete WhatsApp y manda a un formulario de 6 campos traiciona el clic (ver 42, 45).
- **Display/banner:** el banner muestra el producto y un precio; la landing debe abrir con ese producto y ese precio, no con la home genérica (ver 43).
- **Demand Gen:** la pieza visual generó el interés con una promesa concreta; el destino la cumple o el lead se evapora (ver 41, 46).

La incongruencia más cara y común: mandar **todos** los anuncios a la **home** del negocio. La home le habla a todo el mundo y a nadie; cada anuncio necesita su página que continúe *su* promesa específica.

## Velocidad y móvil: la congruencia técnica (jun-2026)

El message match perfecto no sirve si la página tarda en cargar — el latino en móvil de gama media con datos lentos cierra antes de ver tu titular. La congruencia también es de velocidad:

- **LCP (Largest Contentful Paint) < 2.5s** en móvil. Si tu héroe (imagen + titular) tarda más, perdiste al impaciente. Mídelo en PageSpeed Insights.
- **Botón principal "above the fold"** en celular: el WhatsApp/comprar se ve sin scroll, dedo-amigable (mínimo 44px de alto).
- **Peso del héroe controlado:** imágenes comprimidas (WebP/AVIF), nada de videos autoplay pesados que traben la carga.
- **Una landing por oferta**, cargada en el mismo idioma/tono del anuncio.

La construcción técnica (Core Web Vitals, móvil, CRO) es de `desingweb-lushows`; tú exiges que el destino sea rápido y congruente.

## Cómo blindar la congruencia — checklist antes de pautar

1. **Mismo titular.** El H1 de la landing debe sonar al título del anuncio. Si el anuncio dice "calculadora de costos para restaurante", el titular lo repite.
2. **Mismo precio y oferta visibles arriba.** Si el anuncio puso precio, el precio se ve sin scroll. Nada de "cotiza para saber el precio" cuando el anuncio ya lo dijo.
3. **Mismo CTA y destino.** Si prometiste WhatsApp, el botón principal es WhatsApp. Si prometiste descarga, descarga.
4. **Mismo tono e idioma local** (ver 47). El anuncio en colombiano práctico no puede caer en una página corporativa fría.
5. **Una landing por oferta/anuncio**, no la home para todo. Carga rápida en celular (LCP <2.5s).
6. **Congruencia también protege tu cuenta:** en nichos sensibles (salud/finanzas), Google revisa la landing, no solo el anuncio. Si la página promete lo que el anuncio evitó, te suspende igual (ver 44, 93).

Bonus: la congruencia sube tu **Quality Score** y baja tu CPC (ver 36). Una landing relevante al anuncio no solo convierte más — te sale más barata cada subasta, porque el componente "experiencia de la página de destino" del Quality Score mejora.

## Ejemplo completo: anuncio → landing congruente (GastroLatam)

```
ANUNCIO DE BÚSQUEDA (RSA):
  Título 1: "Calculadora de Costos para Restaurante"
  Título 2: "$10.000 — Pago Único — Acceso Hoy"
  Descripción: "Sepa cuánto le cuesta cada plato. Pídala por WhatsApp."

LANDING (lo primero que se ve, sin scroll, en celular):
  H1: "Calculadora de Costos para tu Restaurante"   ← repite el título
  Sub: "Sepa cuánto le cuesta cada plato y cuánto le queda."  ← repite beneficio
  Precio: "$10.000 COP · pago único · acceso inmediato"  ← mismo precio
  Botón grande: "Pedirla por WhatsApp"   ← misma acción prometida
  Tono: usted, colombiano práctico   ← mismo tono (47)
  LCP: 1.9s en móvil   ← rápida
```

Cada elemento del anuncio tiene su espejo arriba en la landing. El clic aterriza suave, el Quality Score sube (ver 36) y la conversión no se fuga. Esto es lo que `desingweb-lushows` construye; tú lo exiges.

## El costo real de la incongruencia

Para que se sienta en el bolsillo: si tu clic de Search cuesta $2.000 COP y tu landing incongruente rebota al 70% de la gente, estás pagando $2.000 por cada 3 visitantes que se van sin mirar. Con 300 clics/mes ($600.000 COP), 210 rebotan por incongruencia: **$420.000 COP/mes tirados** que una landing congruente recuperaría en gran parte. Arreglar el message match suele ser la optimización de mayor retorno y menor esfuerzo de toda la cuenta — más que tocar pujas o keywords.

## Plantilla de auditoría de congruencia

```
ANUNCIO (texto/video):  "________________________"
  Producto nombrado: ________   Precio: ________   CTA: ________   Tono: ________
LANDING (sin scroll, en móvil):
  [ ] H1 repite el mensaje del anuncio        [ ] Mismo precio visible
  [ ] Mismo CTA/destino prometido             [ ] Mismo tono (47)
  [ ] LCP < 2.5s en móvil (PageSpeed)         [ ] Botón above the fold ≥44px
  [ ] Es landing específica, NO la home
  [ ] (nicho sensible) la página NO promete lo que el anuncio evitó (44)
SI FALLA ALGUNA → arréglalo antes de subir presupuesto. Cada rebote = $800–4.000 COP perdidos.
```

## Errores comunes — blacklist

1. **Mandar todos los anuncios a la home.** La home no continúa ninguna promesa específica; el clic rebota. Una landing por oferta.
2. **Romper el precio.** El anuncio dijo $10.000 y la página dice "cotiza" o un precio distinto. Es la incongruencia que más mata conversión.
3. **Cambiar el titular.** Si el H1 no suena al anuncio, la persona piensa "no es esto" y cierra en medio segundo.
4. **Prometer WhatsApp y entregar un formulario largo.** El destino traiciona la acción prometida; el lead se evapora (ver 45).
5. **Anuncio local, landing corporativa.** El salto de tono enfría el clic; mantén el español práctico de punta a punta (ver 47).
6. **Olvidar la congruencia en video/Display/Demand Gen.** El message match no es solo de Search; todo formato lo necesita (ver 42, 43, 46).
7. **Landing lenta en móvil.** LCP >4s y el impaciente cierra antes del titular. Exige <2.5s a `desingweb-lushows`.
8. **Construir la landing improvisada.** El destino decide la venta tanto como el anuncio; constrúyela bien en `desingweb-lushows`, no de afán.
