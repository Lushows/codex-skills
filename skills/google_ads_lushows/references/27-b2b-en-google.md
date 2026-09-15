# 27 — B2B en Google

Lee este módulo cuando vendes a empresas, no a consumidores: software para negocios, servicios profesionales, mayoreo, herramientas para restaurantes (como la calculadora a un dueño de restaurante). Google es **excelente para B2B** porque captura intención: cuando alguien busca "software de inventario para restaurante", está trabajando, está evaluando, tiene presupuesto. El reto del B2B en Google no es encontrar a la empresa — es **filtrar al consumidor suelto** que usa palabras parecidas y no es tu cliente, y **medir leads de calidad**, no volumen de formularios. Frame: Google captura la intención profesional en el momento exacto de evaluación; tu trabajo es no contaminarla con curiosos ni optimizar hacia el lead basura.

## Keywords de alta intención B2B

El B2B tiene su propio lenguaje de búsqueda. Las keywords ganadoras llevan señales de "soy una empresa decidiendo":

| Señal B2B | Modificador | Ejemplo |
|---|---|---|
| Categoría profesional | "software", "sistema", "plataforma", "solución", "herramienta" | "software de costos para restaurante" |
| Para-negocio | "para empresas", "para restaurantes", "para negocios", "B2B", "mayorista" | "plantilla de costos para restaurante" |
| Evaluación | "mejor", "precios", "comparativa", "vs", "demo", "cotización" | "mejor sistema de inventario gastronómico precios" |
| Sustitución | "alternativa a [competidor]", "como [competidor]" | "alternativa a [software conocido]" |
| Problema-negocio | "como reducir [costo/merma/desperdicio]", "controlar food cost" | "como controlar el food cost de mi restaurante" |

Estas convierten porque mezclan **intención comercial + contexto profesional**. El CPC en B2B suele ser más caro que en B2C ($2.000–$8.000 COP por clic en categorías de software gastronómico 2026; más competencia, ticket mayor), pero un solo cliente B2B vale mucho más — modela el LTV antes de asustarte por el CPC. Si un cliente paga $80.000 COP/mes y se queda 14 meses, su LTV es $1.120.000; un CPA de $120.000 por adquirirlo es excelente. La viabilidad económica la valida `economist_lushows`.

## Audiencias custom para B2B (sitios y búsquedas de competidores)

Aquí brilla el **segmento personalizado (custom segment)** — ver 23. En B2B puedes definir audiencias por:

- **Búsquedas de competidores:** "gente que buscó en Google [nombre del competidor B2B]". Esa persona está en modo evaluación de tu categoría: oro puro.
- **Sitios que visitan:** "gente que visita sitios de software gastronómico / asociaciones de restaurantes / medios del sector / portales de proveedores de cocina".
- **Apps que usan:** apps de gestión de negocios, contabilidad, punto de venta (POS).

Estos custom segments los usas en:
- **Search:** en observación, para subir puja a quien encaja (ver 23).
- **YouTube/Demand Gen:** como targeting de público para llegar a decisores con video o display (ver 40, 41) — clave en B2B donde la decisión es lenta y necesitas presencia repetida durante semanas. El video de 30s que explica "cómo este restaurante recuperó $2M/mes controlando su food cost" calienta al decisor antes de que busque.

Customer Match (ver 25) también es potente en B2B: sube tu lista de leads que NO cerraron y úsala como semilla o para remarketing con mensaje distinto.

## Exclusiones para filtrar al consumidor

El mayor desperdicio en B2B es pagar clics de consumidores finales que buscan algo parecido pero no son empresas. Filtros:

1. **Negativos de consumidor (ver 22):** niega "casero", "para mi casa", "personal", "estudiante", "tarea", "gratis", "DIY", "receta", "como cocinar". Si vendes a restaurantes, niega términos de cocina doméstica.
2. **Audiencias de exclusión:** excluye segmentos in-market de consumo masivo que no aplican.
3. **Keywords con modificador profesional obligatorio:** prioriza "para restaurante" / "para negocio" en tus keywords para que el filtro venga desde la palabra misma.
4. **Geo + horario:** B2B suele buscar en horario laboral. Mira el reporte de horas (ver 19) — si las conversiones B2B llegan de lunes a viernes 8am-6pm, ajusta puja a esa franja.

## OCI: medir leads CALIFICADOS, no formularios

El error mortal del B2B en Google: optimizar por "formularios enviados". Google entonces te trae el máximo de formularios — y la mayoría son basura (curiosos, competidores, estudiantes). Tu CPL (costo por lead) se ve genial y tus ventas no suben.

La solución es **OCI = Offline Conversion Import** (importación de conversiones offline) — ver 53. Funciona así:

1. Capturas el **GCLID** (el identificador de clic de Google) cuando alguien llena tu formulario (Google lo agrega a la URL; lo guardas como campo oculto en el form y lo mandas a tu CRM).
2. Ese lead pasa por tu proceso de ventas (lo califica tu equipo o tú — ver `ventas_lushows`).
3. Cuando el lead se vuelve "calificado" o "cliente", subes ESE evento de vuelta a Google con su GCLID y su valor real en COP.
4. Google aprende a traer leads que se PARECEN a los que cierran, no los que solo llenan formularios.

Esto cambia todo: el Smart Bidding (ver 13) deja de optimizar volumen de leads y empieza a optimizar **calidad** de leads. Es la diferencia entre una cuenta B2B que parece funcionar y una que de verdad genera clientes. Asigna valores distintos por etapa (lead = $0 o valor bajo, calificado = valor medio, cliente cerrado = LTV real) para que el algoritmo persiga el dinero, no el formulario. También considera Enhanced Conversions for Leads como alternativa más simple si no tienes CRM robusto (ver 28, 53).

## Errores comunes — blacklist

1. **Optimizar por formularios en vez de leads calificados.** Google te dará volumen basura. Sube las conversiones offline (OCI) para que aprenda calidad (ver 53).
2. **No filtrar al consumidor con negativos.** "Para mi casa", "casero", "gratis", "receta" entran y queman tu presupuesto B2B. Niégalos desde el día 1 (ver 22).
3. **Asustarte por el CPC alto sin mirar el LTV.** Un cliente B2B vale 10-100x un B2C. Modela el valor antes de bajar pujas (valida con `economist_lushows`).
4. **No usar custom segments de competidores.** Quien busca a tu competidor B2B está evaluando tu categoría. Es la audiencia más caliente y casi nadie la usa.
5. **Esperar conversión inmediata.** B2B tiene ciclos largos. Configura ventanas de conversión amplias (60-90 días) y remarketing con memoria larga (ver 24), o subestimarás tu rendimiento real.
6. **Ignorar el horario laboral.** Si tus leads buenos llegan en horario de oficina, pujar igual a las 3am desperdicia. Ajusta por franja (ver 19).
7. **Mandar el lead a una landing genérica.** B2B necesita prueba, casos, demo, cotización clara. Una landing débil mata el lead calificado que tanto costó (manda CRO a `desingweb-lushows`, cierre a `ventas_lushows`).
8. **No capturar el GCLID en el formulario.** Sin GCLID no hay OCI posible; te quedas optimizando a ciegas por formularios. Es el primer paso técnico del B2B serio en Google (ver 53).
