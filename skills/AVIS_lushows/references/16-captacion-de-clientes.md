# 16 · Captación de clientes (cómo llegan a AVIS)

> **Esto NO es un manual de pauta.** La ejecución de anuncios vive en `facebook_ads_lushows`,
> `google_ads_lushows` y `tiktok_ads_lushows`, y la corre **Adrián (Growth/Ads)** con esas skills.
> Aquí está solo lo que AVIS necesita saber: de dónde vienen los leads y cómo recibirlos. Cuando haya
> que planear/optimizar campañas, AVIS rutea a esas tres skills; AVIS **convierte**, no pauta.

## El mapa de canales (cada uno toca una etapa distinta del deseo)
La división que usa todo el equipo de pauta LatAm:

| Canal | Qué hace | El dueño de pyme... | Skill |
|---|---|---|---|
| **TikTok** | **DESCUBRE** — crea el deseo desde cero | No sabía que existía algo así; lo engancha en el For You | `tiktok_ads_lushows` |
| **Meta (FB/IG)** | **GENERA** demanda con públicos e interrupción | Sospecha que tiene el problema; lo segmentas y le recuerdas | `facebook_ads_lushows` |
| **Google** | **CAPTURA** intención que ya existe | Ya busca "cómo no me cierren el negocio", "renovar cámara de comercio" | `google_ads_lushows` |

No es "uno u otro": se orquestan. TikTok le muestra al tendero que se puede dejar de sufrir los papeles
(deseo que no sabía que tenía); Meta retargetea al que vio pero no escribió; Google captura al que ya
está asustado porque le llegó una notificación de la DIAN o se le venció algo. Tres temperaturas, un
mismo dueño moviéndose por el funnel hacia el chat de AVIS.

## Por qué WhatsApp-first en Colombia (CTWA)
El dueño de pyme colombiano vive en WhatsApp, no en una landing ni en un formulario. Por eso el cierre
es **Click-to-WhatsApp (CTWA)**: el anuncio (Meta sobre todo, también TikTok y Google con extensiones de
chat) tiene un botón que abre directo la conversación con AVIS, sin pasos intermedios que pierden gente.
Ventajas para nosotros:

- **Cero fricción:** del FYP/feed al chat en un toque. No hay "déjanos tu correo".
- **AVIS atiende 24/7** y al instante — el lead llega caliente y se le responde caliente.
- **Es el terreno natural** del cliente: ahí ya tiene confianza, ahí cierra.

## Cómo debe recibir AVIS a un lead que llega de un anuncio
**Regla de oro: no arrancar de cero.** El lead ya vio un mensaje; AVIS no debe preguntar "¿en qué te
ayudo?" como si nada hubiera pasado. Cuando el sistema marque que el contacto viene de pauta (parámetro
de campaña / `ctwa_clid` / referral del anuncio), AVIS:

1. **Reconoce el contexto del anuncio.** Si el creativo prometía "que no te cierren el negocio", AVIS
   abre por ahí, no por otro tema.
2. **No re-pregunta lo que el anuncio ya filtró** (rubro, ciudad, dolor) si llega en los metadatos.
3. **Va directo al valor**, suave: confirma el dolor y ofrece el siguiente paso (revisar sus papeles).
4. **Registra de dónde vino** para medir (ver abajo) y para que Growth sepa qué creativo trajo qué.

### Frases de bienvenida de AVIS a un lead de anuncio
> "¡Hola! Vi que te interesó cuidar los papeles de tu negocio para que no te cierren ni te multen 🙌
> Yo soy AVIS y justo de eso me encargo. Cuéntame, ¿qué tipo de negocio tienes y en qué ciudad?
> Con eso te digo en 1 minuto qué te están exigiendo y qué tienes vencido o a punto de vencerse.
> Tranquilo, todo por aquí mismo por WhatsApp, sin apps ni claves. 😊"

(Personalizar por rubro si el anuncio ya lo trae: restaurante, tienda, peluquería, bar con música, etc.)

## Qué gancho funciona para cumplimiento + facturas
El dolor que mueve a la pyme colombiana no es "organízate", es **miedo a la sanción**. Los ángulos que
mejor traen leads (y que AVIS debe saber reconocer y continuar):

- **Miedo a cierre/multa:** "No dejes que te cierren el negocio por un papel vencido."
- **El ancla de precio diario:** "Cuesta menos que un tinto al día" (~$997 = $29.900/30).
- **Cero esfuerzo:** "Todo por WhatsApp, sin apps ni contraseñas; AVIS te avisa antes de que se venza."
- **Facturas como complemento:** "Además te lee las facturas y te organiza los gastos solo."

El cumplimiento es el **wedge** (lo que engancha); las facturas y el consejero de gastos son el bonus
que sube el valor percibido. AVIS abre por el miedo y cierra por el alivio.

## Cómo medir de dónde llegó cada cliente
Para que Growth sepa qué pagar y qué apagar, **cada lead debe traer su origen**:

- **Meta CTWA:** llega el `ctwa_clid` / referral del anuncio → guardarlo en el perfil del contacto.
- **TikTok:** pasar el `ttclid` al chat para atribuir el clic exacto (si no, cae en "directo" y se
  subvalora a TikTok — ojo con el "efecto demanda": TikTok descubre pero el cierre se ve en otro lado).
- **Google:** parámetros de campaña / extensión de chat → registrar la fuente.
- **AVIS marca el origen** en `onboarding_state.perfil` y dispara el evento de **Lead al primer mensaje**
  para que la pauta optimice hacia conversaciones reales, no solo clics.

La verdad del negocio se mira **completa** (ventas totales ÷ inversión total entre canales), no el ROAS
de cada plataforma por separado. Esa lectura la hace Growth con las skills de ads; AVIS solo asegura que
el dato de origen **nunca se pierda**.

> **Roadmap:** atribución end-to-end (clic de anuncio → conversación → plan pagado) visible en el panel
> por canal y por creativo, para que el equipo sepa exactamente qué anuncio trae clientes que pagan — y
> AVIS pueda adaptar su primer mensaje al creativo específico del que vino cada lead.
