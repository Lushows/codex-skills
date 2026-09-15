# 81 — Playbook servicios locales

Lee este módulo cuando vendes un **servicio local que requiere visita o cita**: plomeros, electricistas, cerrajeros, clínicas (dental, estética, veterinaria), talleres mecánicos, abogados, contadores, fumigación, mudanzas, instaladores, spa, peluquerías. Aquí la persona YA tiene el problema ("se me reventó un tubo", "necesito un abogado de tránsito") y busca quién se lo resuelve HOY. Google **captura** esa urgencia mejor que ningún otro canal — es el playbook donde Search rinde más limpio, porque la intención es máxima y la decisión es rápida. Lo que cierra el lead en la llamada o WhatsApp es `ventas_lushows`; aquí solo te traemos el teléfono sonando. Y si quieres GENERAR demanda donde aún no hay búsqueda (un servicio nuevo, una promo), eso es Meta (`facebook_ads_lushows`).

## Estructura de cuenta: LSA + Search local + Call

La jerarquía de captura para un servicio local, de mejor a complemento, con presupuestos de referencia en COP:

| Capa | Tipo | Puja | Presupuesto arranque | Rol |
|---|---|---|---|---|
| LSA | Local Services Ads | Pago por lead | $30.000–80.000/día | Lo más arriba, paga por llamada/mensaje real (ver 50) |
| Search local | Search | tCPA o Max. conv. | $25.000–60.000/día | Captura "cerca de mí" + categoría |
| Call ads | Search con objetivo llamada | tCPA | $15.000–35.000/día | Botón de llamar directo en móvil (ver 51) |
| Marca | Search | tCPA bajo | $5.000–12.000/día | Defensa, barato |

- **LSA primero — SI está en Colombia para tu categoría.** Pagas por *lead* (llamada o mensaje real), no por clic, y apareces arriba de todo con tu insignia y reseñas. Pero LSA en LatAm es despliegue parcial: **verifica en la cuenta antes de prometerlo** (ver 50). Si no está disponible para tu ciudad/oficio, el plan B rinde igual de bien: Search local + Maps + Call.
- **Search local es el caballo de batalla en Colombia hoy.** Captura "plomero cerca de mí", "abogado laboral Bogotá", "veterinaria 24 horas Medellín", "cerrajero urgente [barrio]". Vive del **radio geográfico** y del **Perfil de Empresa de Google** vinculado (asset de ubicación + llamada).
- **Call ads / asset de llamada** porque en servicios la gente quiere LLAMAR, no llenar un formulario. En móvil el botón de llamar convierte más que cualquier landing — el de un tubo reventado no quiere escribir un email, quiere marcar.

**Keywords tipo por capa de urgencia:** caliente ("plomero urgente 24 horas [ciudad]", "destape de cañería domicilio") → media ("plomero [barrio]", "reparación de fugas") → fría/informacional a filtrar ("cómo destapar un baño", "por qué gotea la llave" — esos buscan hacerlo solos, son negativos). El que pone "urgente", "24 horas", "ya", "domicilio", "cerca" es oro.

**Programación horaria y respuesta.** En urgencias (plomería, cerrajería, grúas) la búsqueda llega a cualquier hora — sube puja en noches/fines de semana si atiendes 24h, y baja donde no contestas (no pagues por un lead a las 3am si nadie va a responder). En servicios de cita (clínicas, talleres, contadores) concentra el presupuesto en horario laboral cuando el equipo puede agendar. El lead de servicio local se enfría en minutos: quien busca un cerrajero llama a tres y se va con el primero que contesta, así que el horario de pauta debe casar con tu horario de respuesta real.

## Geografía, reseñas y Google Guaranteed

El servicio local se gana o se pierde en tres cosas que no son la puja:

**Radio geográfico (ver 26 geo):** no pautes a todo el país ni a toda la ciudad. Cubre solo donde de verdad vas o atiendes. Un plomero en Chapinero pautando a toda Bogotá quema plata en zonas a las que no llega a tiempo y le cuesta la reseña mala. Configura segmentación por **presencia** ("personas en tu zona", NO "personas interesadas en tu zona"), para no aparecerle a alguien que solo "se interesó" en tu ciudad desde otra parte. Empieza con un radio chico (3–8 km del punto de operación) y amplía solo si te sobra capacidad.

**Reseñas = la palanca #1.** En LSA y en Maps, el orden en que apareces depende sobre todo de tus reseñas (cantidad, calificación y frescura). Pide reseña a cada cliente satisfecho, sistemáticamente, con un link directo. Sin reseñas frescas no rankeas, pagues lo que pagues. Es la diferencia entre el primer y el quinto lugar del paquete de mapas.

**Google Guaranteed / Screened** (si LSA aplica): la insignia (escudo verde) sube la confianza más que cualquier copy. Google Guaranteed es para oficios (plomero, electricista); Google Screened verifica licencias para profesionales (abogados, contadores). Completa la verificación apenas puedas (ver 50).

**Perfil de Empresa impecable:** horario REAL, teléfono que CONTESTA, fotos del trabajo, dirección/zona de servicio correcta, categoría bien elegida. Eso rankea tanto como el anuncio y es gratis.

## Medir el lead real: OCI de trabajo cerrado

Aquí está el error que arruina a la mayoría: medir **clics o "llamadas"** en vez de **trabajos cerrados**. Una llamada de 8 segundos donde preguntan precio y cuelgan NO es un cliente. Si optimizas a "llamadas", Google te trae llamadas basura.

**Cómo cerrar el loop (ver 53 OCI, 51 call, 54 cierre):**
1. Cuenta como conversión solo las **llamadas de cierto largo** (ej. >60 segundos = lead real, configurable en call ads / Google forwarding number).
2. Mejor aún: usa **OCI** (Offline Conversion Import = importar conversiones que pasaron offline). Cuando un lead se vuelve cliente y pagó, súbele ese dato a Google con su **GCLID**. Así Google aprende a traerte gente que CIERRA, no solo que llama. Es el mismo principio del `ctwa_clid` de Meta.
3. Si puedes, sube el **valor real del trabajo** (un destape de $80.000 vs una remodelación de $3.000.000) para que Smart Bidding optimice a los leads que más valen, no a los más baratos.
4. Activa **Enhanced Conversions for leads** (datos first-party hasheados): en 2026 es el piso de medición y mejora cuánta señal recibe Google (ver actualizacion-2026-06).

**Presupuesto desde el ticket, no desde la sensación:** en servicios el CPC puede ser alto (oficios de urgencia, abogados, estética: $2.000–8.000 por clic en COP) — pero un lead que cierra un trabajo de $500.000 justifica un costo por lead de $30.000–50.000. Calcula tu costo por lead máximo desde tu ticket y tasa de cierre (si cierras 1 de cada 4 leads y cada trabajo deja $200.000 de margen, puedes pagar hasta ~$50.000 por lead y seguir ganando), no desde el "se siente caro" (eso es `economist_lushows`).

## Errores comunes — blacklist

1. **Pautar a un radio enorme.** Apareces donde no llegas a tiempo y quemas plata. Cubre solo tu zona real, segmenta por presencia (ver 26).
2. **Prometer LSA sin verificar Colombia.** Despliegue parcial en LatAm; confirma en la cuenta. Si no está, Search local + Maps rinde igual (ver 50).
3. **Lanzar sin reseñas.** Es la palanca #1 en local; sin reputación no rankeas. Junta reseñas reales con un link directo primero.
4. **Optimizar a "llamadas" sin filtrar.** Traes llamadas de 8 segundos que preguntan y cuelgan. Cuenta solo llamadas largas o usa OCI de cierre (ver 53).
5. **Teléfono que no contesta.** El lead más caro es el que llamó y nadie atendió. Contesta en minutos o se va con el competidor (ver `ventas_lushows`).
6. **No vincular el Perfil de Empresa.** Pierdes el botón de mapa/llamar y los anuncios en Maps, que son gratis de activar como asset de ubicación.
7. **Medir por clic.** El clic no paga la nómina; el trabajo cerrado sí. Mide costo por lead válido y tasa de cierre (ver 60).
8. **No subir el valor del trabajo a Google.** Si un destape y una remodelación "valen igual" para el algoritmo, te llena de trabajitos. Sube el valor real con OCI (ver 53).
