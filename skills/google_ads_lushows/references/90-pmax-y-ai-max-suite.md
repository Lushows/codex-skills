# 90 — PMax y AI Max suite

Lee este módulo cuando vas a usar la automatización de IA de Google y quieres entender QUÉ delega y QUÉ controla, cuando un PMax te reporta números que no cuadran con tu caja, o cuando alguien te diga "activá AI Max for Search" y no sepas si es lo mismo que Performance Max. No son lo mismo. **PMax** (Performance Max) es una campaña aparte que reparte gasto por TODA la red de Google (Search, Shopping, Display, YouTube, Discover, Gmail, Maps) con una sola caja. **AI Max for Search** (lanzado 2025, generalmente disponible en 2026) es una *suite* de funciones que se prende DENTRO de una campaña de Search normal para que el algoritmo expanda tus keywords, escriba assets y elija URLs. Confundirlas cuesta plata. El marco mental de toda esta skill aplica aquí intacto: **Google CAPTURA intención** — la IA solo decide cómo reparte y combina lo que tú le diste para capturarla mejor (o peor).

## El mapa de Performance Max (anatomía 2026)

PMax (ver 12 a fondo) no tiene keywords ni grupos de anuncios al estilo Search. Su anatomía y tu control real:

| Pieza | Qué es | Tu control |
|---|---|---|
| **Asset group** (grupo de recursos) | Paquete de creativos por tema/audiencia/línea de producto | Total: tú los armas |
| **Audience signals** (señales de audiencia) | Pistas de a quién apuntar (Customer Match, intereses, datos propios) | Sugerencia, NO límite duro (ver 25) |
| **Search themes** (temas de búsqueda) | Frases "captura intención parecida a esto" | Guían, no reemplazan tu Search |
| **Channel-level reporting** (reporte por canal, 2025→2026) | Ves cuánto gastó y convirtió en Search vs Display vs YouTube vs Shopping | Lectura + algunas exclusiones de canal |
| **Brand exclusions** (exclusión de marca) | Que PMax NO toque tu propia marca | CRÍTICO, actívalo siempre (ver 39) |
| **Campaign-level negative keywords** (negativas a nivel campaña, 2026) | Ya puedes meter negativas directo en PMax, sin pedirlas a soporte | Úsalas: es el freno que faltaba (ver 22) |
| **Account-level exclusions** (exclusiones de cuenta) | Bloquea marcas, placements y temas sensibles para toda la cuenta | Brand safety transversal |

El reporte por canal y las **negativas a nivel campaña** fueron los avances grandes 2025-2026: antes PMax era una caja 100% negra y para meter una negativa tenías que escribirle a soporte de Google. Hoy ves el reparto, excluyes marca/canales y metes tu lista de veneno directo. La opacidad bajó, no desapareció (ver 16 atribución, 65 incrementalidad).

## AI Max for Search: qué activa y qué exige

AI Max es un interruptor (un grupo de opciones) que enciendes en una campaña de Search ya existente. Activa tres cosas y promete "más conversiones a igual o mejor CPA" — cierto en muchos casos, pero a cambio de control fino:

| Función | Qué hace | El riesgo |
|---|---|---|
| **Keyword expansion** (estilo broad+) | Captura búsquedas parecidas a tus keywords, aunque no las tengas escritas | Se estira a búsquedas que no compran si no la frenas (ver 21, 22) |
| **Asset automation** (automatización de assets) | Reescribe/genera titulares y descripciones desde tu landing con Gemini | Texto que no aprobaste, puede romper tu mensaje o inventar claims (ver 31, 91) |
| **Final URL expansion** (expansión de URL final) | Manda el clic a la página más relevante de tu sitio, no solo a la que pusiste | Si tu sitio tiene páginas pobres, manda tráfico pago a basura |

**Controles que AI Max sí te da (úsalos):** "locations of interest" (afina por dónde está la intención), "brand inclusions/exclusions" a nivel texto, reportes de search terms más detallados que el broad clásico, y la opción de **fijar (lock) ciertos assets** para que la IA no los reescriba. No es una caja negra total; es una caja con interruptores que la mayoría no toca.

**Blindaje obligatorio al activar AI Max (el mismo día, no después):**
1. **Negativos agresivos** (ver 22): es lo que MÁS se estira. Aplica tu lista de veneno universal (gratis, empleo, pdf, "como hacer", "qué es") y revisa términos de búsqueda **2 veces por semana** las primeras 4 semanas, no una.
2. **Final URL expansion controlada**: si tu sitio tiene páginas que no quieres como destino (blog viejo, "trabaja con nosotros", política de privacidad), **exclúyelas** en la configuración. No dejes que mande tráfico pago a cualquier rincón.
3. **Brand safety + revisar/fijar assets generados**: lee lo que la IA escribió antes de que corra. Si inventa un claim ("el #1", "garantizado") te expone a suspensión por misrepresentation (ver 08, 93) y daña marca. Fija a mano los titulares que SÍ representan tu propuesta.

## Qué automatizar y qué NO ceder nunca

La decisión de fondo es la misma en PMax y AI Max: la IA es buena repartiendo y combinando, mala cuidando tu negocio y tu marca.

| AUTOMATIZA (deja que la IA lo haga) | NO CEDAS NUNCA (control humano) |
|---|---|
| Combinar assets y encontrar la mejor mezcla | **Negativos** — tu freno de rentabilidad (ver 22) |
| Repartir presupuesto entre formatos/canales | **Brand exclusions** — que no canibalice marca (ver 39) |
| Ajustar pujas en tiempo real (Smart Bidding, ver 13, 15) | **Qué cuenta como conversión** (venta real, no clic a WhatsApp, ver 53, 64) |
| Probar variantes de titulares y descripciones | **Calidad final de assets/video** (rutea a `directorcreativo_lushows`) |
| Encontrar audiencias parecidas a tus compradores | **Brand safety / placements sensibles** |

Pregunta-guía: *¿este botón optimiza hacia MÁS gasto o hacia MÁS venta real para mí?* Si optimiza hacia gasto (expansión, alcance) → necesita freno humano. Si optimiza hacia tu conversión bien medida → déjalo correr ~2 semanas sin tocar (ver 13). Y antes de juzgar si "funcionó", pregúntate si subió la venta TOTAL o solo se movió el crédito (ver 65).

## Cómo decidir: PMax vs AI Max vs Search manual

| Tu situación | Recomendado |
|---|---|
| E-commerce con catálogo + Merchant Center | **PMax retail** (ver 35) es su mejor caso: usa el feed como combustible |
| Search funciona, quieres más alcance sin abrir campañas | **AI Max** sobre tu Search ganador, con blindaje del día 1 |
| Cuenta nueva, sin señal de conversión limpia | **NI uno ni otro** — primero Search manual exacto/frase que genere datos limpios (ver 11, 14, 98) |
| Pocos SKUs, intención clara, presupuesto chico (<$1M COP/mes) | **Search manual** con keywords y negativos; controlas todo |
| Lead-gen B2B que cierra por humano | Search manual + OCI (ver 53); cuidado con PMax/AI Max que traen leads basura sin freno |
| Producto de pago único (ej. calculadora $10.000 COP) | Search genérico + marca; PMax solo si ya hay volumen de conversión limpia y Customer Match para excluir compradores (ver 25) |

Nunca actives la automatización para "ahorrar trabajo" cuando aún no tienes señal de conversión confiable: la IA aprende de tus conversiones, y si le das datos sucios (clics contados como ventas), optimiza hacia el cliente equivocado a toda velocidad. Regla de presupuesto: PMax necesita oxígeno para salir de aprendizaje — con menos de ~$1.500.000 COP/mes y <30 conversiones/mes da bandazos. En presupuesto chico, Search manual rinde más por peso.

## Mini-pasos: activar AI Max sin quemarte

1. Toma tu campaña de Search **ganadora** (la que ya convierte, no la nueva).
2. Activa AI Max. En la misma sesión: pega tu lista maestra de negativos, excluye URLs pobres, fija tus mejores titulares.
3. Marca el calendario: revisar search terms lunes y jueves por 4 semanas.
4. A las 2 semanas compara CPA y volumen contra el periodo previo. Si CPA subió sin más volumen útil, recorta expansión o vuelve a Search puro.
5. Decide con la caja (MER, ver 97), no con el ROAS que la campaña se auto-atribuye.

## Errores comunes — blacklist

- **Confundir AI Max for Search con Performance Max.** AI Max vive DENTRO de Search; PMax es campaña aparte por toda la red. Tratarlas igual rompe la estructura (ver 11, 12).
- **Activar AI Max sin reforzar negativos el mismo día.** Es la función que MÁS se estira; sin freno, quema presupuesto en búsquedas que no compran (ver 22).
- **Dejar Final URL expansion libre con un sitio lleno de páginas pobres.** Mandas tráfico pago a tu blog viejo o a "trabaja con nosotros". Excluye lo que no vende.
- **No leer ni fijar los assets que la IA generó.** Un claim inventado ("garantizado", "el #1") te expone a suspensión y daña marca (ver 08, 91, 93).
- **PMax sin brand exclusions.** Canibaliza tu marca, reporta ROAS inflado no incremental; la trampa #1 (ver 39, 65).
- **No usar las negativas a nivel campaña que PMax ya permite en 2026.** Te quedaste sin el freno que Google por fin te dio (ver 22).
- **Juzgar la automatización por su ROAS reportado sin prueba de incrementalidad.** ¿Subieron las ventas TOTALES o solo se movió el crédito? (ver 65, 16).
- **Activar automatización con <30 conversiones/mes de señal limpia o presupuesto chico.** No calibra, da bandazos y gasta a frío (ver 13).
