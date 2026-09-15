# 00 — Método del media buyer de TikTok

Lee este módulo cuando vas a empezar a pautar en TikTok y no sabes por dónde arrancar, o cuando una cuenta está dando vueltas sin resultados y necesitas un proceso ordenado en vez de apretar botones al azar. Este es el mapa maestro: el orden exacto en que se trabaja una cuenta de TikTok Ads, desde el diagnóstico hasta la escala. Todo lo demás en esta skill cuelga de aquí.

La regla número uno de TikTok, antes que la subasta, el píxel o el presupuesto: **TikTok no perdona el mal creativo**. En Meta un buen público te salva un anuncio mediocre; en TikTok el creativo es el 80% del resultado (ver 01). Por eso la frase que define la era 2026 no es "haz mejores anuncios", es: **"no hagas ads, haz TikToks"** (ver 30). El creativo nativo ES el targeting — el algoritmo decide a quién mostrarte según quién reacciona a tu video, no según el público que tú escojas (ver 20). Entender eso cambia todo el método: tu trabajo no es tunear audiencias, es producir contenido que la gente quiera ver. Por eso la primera pregunta no es técnica, es de producción.

## La pregunta filtro: ¿puedes producir creativo nativo constante?

Antes de gastar un peso, respóndete esto con honestidad:

| Pregunta | Si NO → |
|---|---|
| ¿Puedes grabar 5-15 videos verticales nuevos por semana? | TikTok te va a frustrar. El creativo se quema en 1-2 semanas (ver 39) — más rápido que Meta. Sin volumen, no arranca. La era Smart+ pide MÁS creativo, no menos (ver 12). |
| ¿Tienes a alguien que hable a cámara o un creator/UGC? | Necesitas caras y voz reales sound-on (ver 30, 37). El video de stock o de banco no rinde. |
| ¿Tu oferta cierra por WhatsApp o TikTok Shop? | En Colombia el descubrimiento es barato pero la venta cierra por chat (ver 55) o Shop (ver 50, disponibilidad CO por confirmar). Define el cierre antes de pautar. |
| ¿Tienes $1.5-3M COP/mes mínimo para 30-45 días? | Sin pista de despegue el algoritmo no aprende (ver 07, 13). |

Si respondiste NO a "producir creativo constante", **TikTok no es tu canal todavía** — empieza por Meta (`facebook_ads_lushows`) que tolera menos volumen creativo, o resuelve la producción primero. No hay atajo: una cuenta de TikTok es, en el fondo, una **fábrica de creativos** con un Ads Manager pegado al lado.

## El proceso completo (en orden, sin saltos)

| Fase | Qué haces | Módulos |
|---|---|---|
| 1. Diagnóstico | Define negocio, oferta, cierre (WhatsApp/Shop), presupuesto real, objetivo | 00, 03, 07 |
| 2. Medición primero | Business Center, Pixel, Events API server-side, eventos estándar, `ttclid` para cerrar el lazo | 04, 05, 06 |
| 3. Estructura | 1 campaña → pocos ad groups → muchos creativos. Smart+ si aplica | 10, 12, 20 |
| 4. Creativo nativo | Hooks 1-3s, UGC, Spark Ads, sonido tendencia, Symphony de apoyo. El corazón de TikTok | 30, 34, 37, 91 |
| 5. Test | 1 variable a la vez, lee thumbstop/hook rate antes que CPA | 17, 37, 49 |
| 6. Escala | Vertical (presupuesto) u horizontal (públicos/creativos) según señal | 64, 90 |

Nunca saltes la fase 2. Pautar sin Pixel + Events API en TikTok 2026 es como manejar de noche sin luces: gastas, pero el algoritmo no ve las conversiones para optimizar (ver 06). Y nunca saltes la fase 4 al ritmo correcto: el cuello de botella de toda cuenta sana es **cuántos creativos nuevos produces por semana**, no cuántos botones aprietas.

## Los 6 modos de trabajo

Identifica en cuál estás; cada uno tiene su playbook:

1. **Lanzar de cero** — cuenta nueva, nunca ha pautado. Prioridad: medición (04-06) + 6-10 creativos iniciales con 3-4 ángulos distintos (ver 30, 41).
2. **Escalar lo que funciona** — ya hay ROAS positivo, quieres más. Sube presupuesto con calma (20-30% cada 2-3 días) o duplica ganadores; cuida la fase de aprendizaje (ver 13, 64).
3. **Apagar el incendio** — CPA disparado, ROAS muerto. Diagnóstico estructurado: 80% de las veces es fatiga de creativo (ver 39) o medición rota (ver 06).
4. **Testear oferta/creativo** — validar ángulos y hooks rápido y barato (ver 17, 37, 41).
5. **TikTok Shop / comercio** — vender dentro de la app con GMV Max y VSA, si Shop está disponible en tu país (ver 50, 52). En Colombia: confirma o cae a WhatsApp.
6. **Servicio a clientes** — manejas cuentas ajenas como agencia: accesos por Business Center, nunca por contraseña (ver 04).

## Smart+ no te quita el trabajo, te lo mueve

En 2026 la mitad de las decisiones las toma la máquina. **Smart+** (la automatización de TikTok para Web, Catalog, App y Lead — el equivalente a Advantage+ de Meta o PMax de Google) decide a quién, cuándo y cuánto pujar (ver 12). **GMV Max** hace lo mismo para TikTok Shop (ver 52). Eso NO significa menos trabajo: significa que tu energía se va 100% a las dos cosas que la máquina NO puede hacer por ti — **creativo nativo abundante** y **medición limpia**. Si esos dos están bien, Smart+ rinde; si están mal, los amplifica y quemas plata más rápido. La automatización es un megáfono, no un cerebro.

## A dónde ruteo (no todo es pauta)

TikTok crea el deseo, pero el dinero entra cuando algo cierra. No intentes resolver todo desde el Ads Manager:

| Necesidad | Skill hermana |
|---|---|
| Cerrar la venta por WhatsApp/DM, manejar objeciones, follow-up | `ventas_lushows` |
| Landing que convierta, CRO, velocidad de carga móvil | `desingweb-lushows` |
| Marca, logo, paleta, dirección de arte del feed y los creativos | `directorcreativo_lushows` |
| ¿Es viable? Pricing, CAC, LTV, punto de equilibrio | `economist_lushows` |
| Capturar intención de búsqueda (Google Search/PMax) | `google_ads_lushows` |
| Generar/reactivar demanda con públicos (Meta FB/IG) | `facebook_ads_lushows` |

Regla mental: **TikTok descubre · Meta genera · Google captura · ventas cierra · desingweb aterriza · directorcreativo viste · economist valida** (ver 03 para el funnel combinado).

## Errores comunes — blacklist

- **Pautar antes de medir.** Sin Pixel + Events API el algoritmo optimiza a ciegas y subreporta 20-40% en iOS. Fix: fase 2 SIEMPRE primero (ver 05, 06).
- **Tratar TikTok como Meta.** Subir el mismo anuncio cuadrado con texto encima. Fix: creativo nativo vertical sound-on, hecho para el For You (ver 30, 33).
- **Un solo creativo "ganador".** Se quema en días y el CPA se dispara. Fix: 5-15 creativos nuevos/semana, siempre (ver 39).
- **Presupuesto de juguete.** $300.000 COP/mes no le da pista al algoritmo. Fix: mínimo realista por 30-45 días (ver 07).
- **Optimizar por likes/views.** Las vistas no pagan arriendo. Fix: optimiza al evento de fondo de funnel (CompletePayment/Lead) (ver 14).
- **No definir el cierre.** Tráfico que llega a ningún lado. Fix: decide WhatsApp o Shop ANTES de pautar (ver 03, 55).
- **Saltar la pregunta filtro.** Pautar sin capacidad de producir creativo = quemar plata. Fix: resuelve producción primero.
- **Creer que Smart+ "lo hace solo".** La máquina amplifica insumos; si le das creativo flojo lo escala flojo. Fix: tu trabajo es creativo + medición (ver 12).
