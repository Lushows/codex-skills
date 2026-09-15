# 29 — Privacidad y datos en LatAm

Pautar con datos de clientes (listas, Dataset/píxel, CAPI) tiene reglas: las de la LEY de tu país y las de META. Romper las primeras trae multas; romper las segundas trae algo más inmediato: cuenta restringida o baneada (ver 93). Lee este módulo antes de subir tu primera customer list (ver 28), instalar el Dataset (ver 14), o si vendes salud/bienestar/finanzas — las categorías donde más cuentas caen.

## Consentimiento: la base de todo

Para usar los datos de un cliente en publicidad (subirlo a una lista, retargetearlo), necesitas su **autorización** y un **aviso de privacidad** que mencione explícitamente que usas los datos para "publicidad, marketing y remarketing en plataformas como Meta". Sin esa frase, tu autorización "para enviarte la factura" NO cubre subirlo a Ads Manager.

Mínimo operativo:
- Aviso de privacidad publicado en tu web/link de WhatsApp Business, con finalidades que incluyan publicidad.
- En la captura (formulario, checkout, chat): referencia al aviso ("Al continuar aceptas nuestra política de datos: [link]").
- Registro de cuándo/cómo autorizó (el formulario con timestamp basta).

## 🔴 Data Source Declaration: el cambio que TIENES que mirar (rodando 2026)

Meta está rodando la **Data Source Declaration**: quien use remarketing/custom audiences deberá **declarar el origen del dato y probar consentimiento**. Las audiencias sin consentimiento demostrable quedan **inelegibles** (no las podrás usar). Esto convierte el "consentimiento" de buena práctica a requisito operativo de la plataforma. Acción: verifica el estado en tu Business Manager → Audiences, declara el origen de cada customer list, y asegúrate de que tu captura genere evidencia de autorización. Una lista de WhatsApp sin checkbox de consentimiento es justo lo que esto vuelve inservible.

## Habeas Data Colombia (Ley 1581 de 2012)

El marco colombiano de protección de datos personales. Lo que te toca como anunciante:

- **Autorización previa** del titular para tratar sus datos (ver arriba).
- **Finalidad**: solo usas los datos para lo que el aviso dice. Si el aviso no menciona publicidad, no pautes con ellos hasta actualizarlo.
- **Derecho de supresión**: si un cliente pide que lo borres, lo borras — de tu CRM Y de las customer lists subidas a Meta (re-sube la lista sin él, o usa la opción de remover).
- **Registro Nacional de Bases de Datos (RNBD)** ante la SIC: obligatorio según el tamaño/tipo de empresa — verifica si tu empresa aplica con los umbrales vigentes de la SIC (han cambiado; hoy aplica principalmente a sociedades con activos superiores a ciertos topes). Registrar es un trámite en línea, no un drama.
- Multas de la SIC: existen y se aplican (hasta ~2.000 SMMLV — con el salario mínimo 2026 son cientos de millones de COP). El caso típico sancionado: enviar publicidad a gente que nunca autorizó — exactamente lo que pasa con bases compradas.

**LGPD Brasil**: si vendes a Brasil, su ley (Lei Geral de Proteção de Dados) es más exigente y con multas serias (hasta 2% de facturación, tope ~R$50M por infracción). Necesitas base legal explícita para marketing y atender derechos de los titulares. **México** tiene la LFPDPPP (actualizada 2025) con lógica similar. Regla simple multi-país: **el estándar más alto de los países donde vendes es tu estándar**.

Nota EU: la disputa "consentir o pagar" / DMA (multa €200M a Meta, abr-2025) y la opción "Less Personalized Ads" en EEA **NO aplican para Colombia** — solo afectan audiencias residentes en la UE. No te confundas con titulares europeos que no tocan tu pyme.

## Lo que META prohíbe enviar por Dataset/CAPI

Independiente de la ley, Meta prohíbe que le envíes **datos sensibles** a través del Dataset/píxel o CAPI: condiciones de salud o diagnósticos, orientación sexual, religión, afiliación política/sindical, datos financieros detallados, datos de menores.

Ejemplo concreto (ver 83): un e-com de suplementos puede enviar `Purchase` con el valor y el ID de producto, pero **NO** un evento custom tipo `compro_tratamiento_ansiedad` ni URLs de parámetro que revelen condición de salud (`/checkout?condicion=diabetes`). Meta escanea los eventos y los nombres de página: detecta esto, bloquea los eventos (tu campaña se queda ciega) y puede restringir el negocio entero. Health & wellness es categoría vigilada desde 2025: muchos e-coms de salud tienen eventos de fondo de embudo limitados — verifica el estado de tu dominio en Events Manager.

Cómo nombrar sin pisar la línea: eventos estándar (`Purchase`, `Lead`, `AddToCart`), nombres de producto neutros en el catálogo, nada de diagnóstico en URLs ni parámetros.

## Categorías especiales (HEC + financiero): enforcement más duro

Meta endureció en 2025-2026 la detección automática de **categorías especiales** — vivienda, empleo, crédito (HEC) y la nueva categoría **"Financial Products and Services"** (14-ene-2025, US/US-targeted: banca, ahorro, seguros, inversión, préstamos). Estas restringen el targeting: sin radio/ZIP, sin edad/género, sin lookalikes, 18-65+. Correr una campaña que DEBÍA marcarse como especial y no marcarla es hoy **causa común de restricción de cuenta**. Si vendes algo cercano a crédito, vivienda, empleo o finanzas, verifica si te aplica ANTES de lanzar — es más barato declararla que recuperar una cuenta baneada (ver 93).

## Cookie banner y Dataset

Si tu web usa Dataset/píxel, el aviso de cookies que informe y permita rechazar es buena práctica (y exigible según el país del visitante — obligatorio estilo GDPR si vendes a Europa). Implementación técnica del banner y del consent mode: **desingweb-lushows módulo 32**. Mínimo: banner que mencione cookies de publicidad + link a tu política. Esto además alimenta la prueba de consentimiento que pedirá la Data Source Declaration.

## Buenas prácticas que protegen LA CUENTA (además de la ley)

1. **Minimiza**: captura y envía solo lo que usas. Menos datos = menos riesgo legal y menos superficie de baneo.
2. **NUNCA compres bases de datos**: ilegal (sin autorización de los titulares), match rate horrible (ver 28), y Meta reconoce el patrón de listas frías masivas → restricción. Pierdes tres veces.
3. **No subas listas de terceros** ("mi socio me pasó los clientes de su otra empresa"): la autorización no es transferible así; necesitarías que el aviso original lo permitiera.
4. Responde solicitudes de clientes (borrado, consulta) en serio y rápido: cada queja ante la SIC empieza por un cliente ignorado.
5. Documenta: aviso publicado + registro de autorizaciones + RNBD si aplica + declaración de origen de cada audiencia. Si un día la SIC o Meta pregunta, tienes respuesta.

Esto no es burocracia decorativa: las cuentas publicitarias longevas (ver 93) son las que nunca le dieron a Meta un motivo de datos para mirarlas feo.

## Checklist de cumplimiento en 15 minutos

1. ¿Aviso de privacidad publicado y menciona publicidad/remarketing? Si no: actualízalo HOY antes de subir listas.
2. ¿Captura con referencia al aviso (checkbox o texto en formulario/checkout/chat)?
3. ¿Cada custom audience tiene origen declarable y evidencia de consentimiento (Data Source Declaration)?
4. ¿Eventos del Dataset son estándar y sin datos sensibles en nombres/URLs? (Events Manager → revisa los eventos que llegan).
5. ¿Tu producto roza HEC/financiero? Verifica si debes marcar categoría especial.
6. ¿RNBD verificado (aplica/no aplica) con los umbrales vigentes de la SIC?
7. ¿Proceso para borrar a un cliente que lo pida (CRM + listas en Meta)?
8. ¿Cero bases compradas o de terceros en tus audiencias? Si hay alguna: bórrala hoy.

## Errores comunes — blacklist

- Comprar una base de 50.000 contactos "para arrancar": ilegal (Ley 1581), match del 15%, y patrón de baneo. La peor inversión posible.
- Aviso de privacidad que no menciona publicidad/remarketing: tu customer list queda sin soporte legal aunque el cliente "te dio el dato" — y la Data Source Declaration la vuelve inelegible.
- Evento custom con diagnóstico (`lead_tratamiento_diabetes`): Meta lo bloquea y marca tu dominio. Eventos estándar y nombres neutros.
- Correr un producto financiero/de crédito sin marcar categoría especial: causa común de restricción en 2026.
- Ignorar una solicitud de supresión "porque es un solo cliente": así empiezan las quejas ante la SIC.
- Asumir que el RNBD "no aplica para negocios chicos" sin verificar los umbrales vigentes: confírmalo en la SIC, toma 10 minutos.
- Dataset disparando en páginas con datos sensibles en la URL: audita tus URLs de checkout/gracias.
- Tratar esto como tema "legal aparte" de la pauta: la mitad de los baneos de cuentas de salud/bienestar empiezan por datos mal enviados, no por anuncios mal escritos (ver 93).
- Confundir reglas de la UE (consentir-o-pagar, DMA) con obligaciones en Colombia: no aplican a residentes colombianos.
