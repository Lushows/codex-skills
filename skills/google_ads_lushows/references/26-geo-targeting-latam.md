# 26 — Geo-targeting LatAm

Lee este módulo cuando vas a definir DÓNDE se muestran tus anuncios, especialmente si vendes físico, despachas a ciertas ciudades o haces contraentrega. El geo-targeting parece trivial — "elijo mi ciudad y ya" — pero esconde **la trampa más cara de Google**: una opción de ubicación mal puesta que te hace pagar clics de gente que ni vive donde vendes. En LatAm, con presupuestos ajustados en COP, esto define si tu cuenta es rentable o un colador. Google captura intención, sí, pero la intención de alguien en otro país no te sirve si no le puedes entregar.

## La trampa: "presence" vs "presence or interest"

Cuando configuras ubicaciones, Google esconde una opción crítica en "Opciones de ubicación". Tiene dos modos:

| Opción | A quién le muestra | Veredicto |
|---|---|---|
| **Presence** (Presencia: personas EN tu ubicación) | Solo a quien ESTÁ físicamente en tu zona objetivo | ✅ El correcto casi siempre |
| **Presence or interest** (Presencia O interés) | A quien está EN tu zona **+ a quien la MENCIONA o muestra interés** aunque esté en otro país | ⚠️ La trampa |

El default de Google suele ser **"presence or interest"** — y casi nadie lo cambia. ¿El problema? "Interest" trae a alguien en México que buscó "restaurantes en Bogotá" para un viaje, o a un curioso en Argentina que mencionó "Medellín". Le pagas el clic y jamás te compra porque no está donde vendes.

**Acción exacta:** al crear la campaña → sección Ubicaciones → "Opciones de ubicación" (hay que desplegarla, está colapsada) → en "Target" elige **"Presence: people in or regularly in your targeted locations"**. Haz lo mismo en "Excluded" eligiendo presencia. Esto solo ya ahorra 10–30% de presupuesto desperdiciado en muchas cuentas. Excepción legítima: si vendes turismo, eventos o algo donde el interés remoto SÍ compra (un hotel en Cartagena le vende a quien busca desde Bogotá), ahí "presence or interest" tiene sentido.

## Ciudades, radios y exclusiones

Formas de definir el dónde:

- **Por ciudad/región:** escribe "Bogotá", "Medellín", "Cali". Lo más común. Puedes apilar varias.
- **Por radio:** un punto en el mapa + X km alrededor. Útil para negocio local con despacho por zona ("5 km alrededor de mi cocina"). Ideal para dark kitchens y domicilios.
- **Por país:** solo si vendes digital a toda Colombia (como la calculadora a $10.000 COP, que es descarga: ahí sí "Colombia" entero tiene sentido).
- **Por código postal / DANE:** Colombia tiene cobertura parcial; en ciudades grandes puedes acotar por sectores. Útil para contraentrega zonificada.

**Exclusiones:** igual de importantes que incluir. Si despachas a Bogotá pero NO a zonas rurales lejanas, o quieres evitar una ciudad donde tuviste mala experiencia, exclúyela. También excluye países enteros si solo vendes en Colombia — evita que el algoritmo (sobre todo en PMax/Demand Gen) se vaya a buscar clics baratos en otro lado. Caso típico de fuga: PMax encuentra clics baratísimos en Venezuela o India y se va para allá; si no excluiste, pagaste tráfico inútil toda la semana.

## Ajustes por ubicación y la realidad del despacho

Una vez corriendo, mira el **reporte de ubicaciones** (Campaña → Configuración → Ubicaciones → reporte por "Ubicaciones de los usuarios" — esto muestra dónde ESTABA la persona, no a dónde la dirigiste):

| Hallazgo | Acción |
|---|---|
| Bogotá convierte al doble que el resto | Ajuste de puja +30% para Bogotá (ver 15) |
| Una ciudad gasta y no convierte | Bájale la puja −30% o exclúyela |
| Entran clics de un país que no targeteaste | Revisa "presence or interest" — seguro está mal puesto |
| Una zona convierte barato y no la tenías | Súbela como ubicación propia con su puja |

**Despacho y contraentrega — lo concreto para LatAm:**
- Si haces **contraentrega/pago contra entrega**, geo-targetea SOLO las zonas a las que tu transportadora llega con esa modalidad (Coordinadora, Servientrega, Interrapidísimo cubren distinto). Pagar clics de pueblos sin cobertura es tirar plata.
- Si despachas nacional por transportadora, Colombia entero está bien, pero ajusta pujas a las ciudades que más convierten (suelen ser Bogotá, Medellín, Cali, Barranquilla por volumen).
- Si es **digital puro** (descarga, acceso online), la ubicación importa menos para entrega pero MUCHO para idioma/moneda/intención — sigue acotando a tu país para no pagar clics de otros mercados donde tu oferta en COP no aplica (alguien en España no te paga $10.000 COP).

Ajuste de programación horaria también es "geo en el tiempo": si vendes a dueños de restaurante, las conversiones llegan fuera de su hora pico de servicio (mañanas, media tarde, noche tras cerrar). Cruza geo con horario (ver 19) para no pujar igual a las 3am.

## Estructura geo por escala de negocio

No todos los negocios geo-targetean igual. Elige según tu modelo:

| Modelo | Cómo estructurar el geo | Por qué |
|---|---|---|
| Dark kitchen / domicilio local | Radio de 5–10 km alrededor de la cocina, presence, exclusión de todo lo demás | Solo entregas en tu radio; cada clic afuera es pérdida garantizada |
| Tienda física con tráfico | Radio + extensiones de ubicación (Google Business Profile) + pujas más altas cerca | El que está cerca y busca, va; prioriza proximidad |
| Contraentrega regional | Ciudades específicas con cobertura de transportadora, presence | Cobranza solo donde llega tu courier con esa modalidad |
| Nacional físico (transportadora) | País entero, presence, ajustes de puja por ciudad según conversión | Despachas a todo el país pero no todas las ciudades rinden igual |
| Digital puro (la calculadora) | País entero, presence, idioma español, excluir otros países | La entrega es online; lo que importa es moneda/idioma/intención local |

**Campañas separadas por geo de alto valor:** si Bogotá representa el 50% de tus ventas y tiene dinámica de subasta propia, vale la pena una campaña SOLO Bogotá con su presupuesto y su tCPA (ver 13), separada del "resto del país". Así no dejas que una ciudad cara se coma el presupuesto de las que convierten barato, y puedes escribir anuncios con mención local ("Entrega en Bogotá") que suben el CTR y bajan el CPC vía Quality Score (ver 36). Para presupuestos chicos no fragmentes de más — Smart Bidding necesita ~30 conversiones/mes por campaña para aprender bien; si partes en 5 campañas geo con 6 conversiones cada una, ninguna aprende. Consolida hasta tener volumen.

## Errores comunes — blacklist

1. **Dejar "presence or interest" por default.** La trampa #1. Cambia a "Presence" siempre, salvo que vendas turismo o algo donde el interés remoto sí compre. Esto solo ya te ahorra plata.
2. **No excluir otros países.** En PMax/Demand Gen el algoritmo se va a clics baratos en el extranjero si no lo cierras. Excluye explícitamente Venezuela, India y compañía si solo vendes en Colombia.
3. **Targetear zonas a las que no despachas.** Con contraentrega, pagar clics de pueblos sin cobertura es desperdicio garantizado. Acota a tu zona de entrega real.
4. **Confundir "ubicaciones de usuarios" con "ubicaciones de interés" en el reporte.** Para decisiones reales usa "dónde estaba la persona", no "qué buscó".
5. **Radio demasiado grande para negocio local.** 50 km alrededor cuando solo entregas a 8 km = clics inútiles. Ajusta al radio de entrega real.
6. **No ajustar pujas por ciudad teniendo los datos.** Si Bogotá convierte el doble, debería tener más puja. Geo plano deja rendimiento sobre la mesa.
7. **Olvidar que con Smart Bidding los ajustes por ubicación funcionan distinto.** Con tCPA/tROAS, los ajustes manuales se vuelven señales, no reglas duras; igual configura presencia y exclusiones, que esas SÍ mandan (ver 13, 15).
8. **No revisar el reporte de ubicaciones nunca.** La fuga geográfica es silenciosa: gastas semanas en ciudades que no convierten sin enterarte. Míralo mensual.
