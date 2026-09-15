# 139 — CRM y pipeline

Cómo no perder ni una venta por olvido: un sistema simple para ver en qué etapa está cada oportunidad,
qué hacer hoy, y predecir cuánto vas a vender. Vale para B2B y para ventas grandes en B2C.

## Qué es un pipeline (en cristiano)
El **pipeline** (embudo de ventas) es la lista de todas tus oportunidades abiertas, cada una con una
**etapa** (qué tan cerca está de cerrarse) y un **valor estimado**. Es la "cuenta por cobrar del futuro":
te dice cuánto dinero está en juego y dónde se está atascando.

El **CRM** (Customer Relationship Management = gestión de relación con clientes) es solo la herramienta
donde guardas eso: quién es el cliente, qué hablaron, en qué etapa va y cuándo es el próximo seguimiento.
No necesitas software caro para empezar; necesitas **disciplina**.

## Las etapas del pipeline (define las tuyas)
La regla de oro: una etapa se define por una **acción del cliente**, no por una intención tuya. "Le mandé
propuesta" no es etapa; "el cliente recibió y pidió revisar la propuesta" sí.

Plantilla típica (ajústala a tu negocio):

| # | Etapa | Qué significa (acción del cliente) | Prob. cierre (ejemplo) |
|---|---|---|---|
| 1 | Lead / contacto nuevo | Mostró interés inicial | 10% |
| 2 | Calificado | Confirmaste que tiene dolor, presupuesto y autoridad (BANT, ver 134) | 25% |
| 3 | Reunión / demo hecha | Vio la solución atada a su problema | 40% |
| 4 | Propuesta enviada | Recibió oferta con precio y la está evaluando | 60% |
| 5 | Negociación | Discuten precio/condiciones, hay intención clara | 80% |
| 6 | Ganada (Won) | Firmó / pagó | 100% |
| — | Perdida (Lost) | Dijo no o se enfrió | 0% (y anota POR QUÉ) |

Las probabilidades son **tuyas**, no universales: revísalas cada trimestre con tus datos reales (ver 21).

## El CRM mínimo viable
No compres software el día 1. Arranca con una hoja de cálculo (Google Sheets) con estas columnas:

- **Cliente / contacto** y cómo contactarlo
- **Valor estimado** ($) del negocio
- **Etapa actual** (de la tabla de arriba)
- **Fecha de cierre estimada**
- **Próxima acción** y **fecha del próximo seguimiento** ← la columna más importante
- **Origen** (de dónde salió: referido, anuncio, etc. — conecta con CAC, ver 52)
- **Notas** de la última conversación

Pasa a un CRM de verdad (HubSpot gratis, Pipedrive, Zoho, Notion) cuando: lleves >20-30 oportunidades
abiertas a la vez, o tengas más de un vendedor. Antes de eso, la hoja sobra.

**Pregunta país/herramienta primero:** los precios y planes gratuitos de cada CRM cambian seguido y por
región; verifica el plan vigente antes de pagar.

## La regla anti-olvido: nunca dejes un trato sin "próxima acción"
La causa #1 de ventas perdidas no es el precio: es el **silencio**. El trato se enfría porque nadie hizo
el seguimiento. Norma de hierro:

> Toda oportunidad abierta DEBE tener una fecha de próxima acción futura. Si no la tiene, está muerta y no
> lo sabes.

Cada mañana abre el CRM y filtra por "próxima acción = hoy o vencida". Esa es tu lista de trabajo del día.
Si una lleva 30+ días sin movimiento, decide: la reactivas con un mensaje claro o la marcas como Perdida
(y liberas tu cabeza). Un pipeline lleno de zombis te miente sobre cuánto vas a vender.

## KPIs del pipeline (los números que importan)
1. **Valor total del pipeline** ($): suma de oportunidades abiertas. Tu "futuro visible".
2. **Pipeline ponderado** ($): cada trato × su probabilidad de etapa. Tu forecast realista.
3. **Win rate** (tasa de cierre): ganadas ÷ (ganadas + perdidas). Mide tu efectividad.
4. **Conversión por etapa**: % que pasa de una etapa a la siguiente. Te muestra **dónde se atasca** el
   embudo (si caen mucho entre "propuesta" y "negociación", tu precio o propuesta falla).
5. **Velocidad de venta** (ciclo promedio): días desde lead hasta cierre. Más corto = más caja.
6. **Cobertura de pipeline**: pipeline abierto ÷ meta del periodo. Sano: **3x-4x** la meta.
7. **Ticket promedio** (valor medio de un trato ganado).

## Ejemplo numérico (cifras ilustrativas, no datos de mercado)
Meta del trimestre: **$50.000.000 COP** en ventas nuevas (ejemplo).

Estado actual del pipeline:

| Etapa | # tratos | Valor total | Prob. | Valor ponderado |
|---|---|---|---|---|
| Calificado | 12 | $24.000.000 | 25% | $6.000.000 |
| Demo hecha | 6 | $18.000.000 | 40% | $7.200.000 |
| Propuesta | 4 | $16.000.000 | 60% | $9.600.000 |
| Negociación | 2 | $10.000.000 | 80% | $8.000.000 |
| **Total** | **24** | **$68.000.000** | — | **$30.800.000** |

Lectura:
- **Forecast realista (ponderado) = $30,8M** vs meta de $50M → **te faltan ~$19,2M**. No vas a llegar solo
  con lo que tienes; necesitas meter más leads arriba YA (ver 131).
- **Cobertura = $68M / $50M = 1,36x**. Muy bajo: lo sano es 3x-4x. Confirma que tu embudo está flaco.
- Si tu **win rate** histórico es 30% y ticket promedio $4M, para cerrar los $19,2M que faltan necesitas
  cerrar ~5 tratos más → necesitas ~**16 oportunidades nuevas** calificadas (5 ÷ 0,30).

Forecast por etapa también puede hacerse simple: "lo que está en negociación (80%) casi seguro entra este
mes; lo de calificado, no cuentes con ello este mes". Usa el ponderado para no engañarte.

## Forecast de ventas sin mentirte
- **Método ponderado** (el del ejemplo): bueno para ver el conjunto. Tiende a inflar si tienes zombis.
- **Método por compromiso**: clasifica cada trato en "Comprometido / Probable / Posible" según lo que el
  cliente realmente dijo, no tu optimismo. Suma solo Comprometido + parte de Probable.
- Compara forecast contra lo real cada cierre de mes. Si siempre fallas por arriba, baja tus
  probabilidades; eres demasiado optimista (sesgo clásico, ver 04).

## Errores comunes
- **Tratar el optimismo como dato.** "Este seguro cae" sin que el cliente lo haya confirmado infla el
  forecast y te hace gastar de más.
- **Pipeline sin limpiar.** Tratos de hace 4 meses "abiertos" que ya son no. Limpia semanal.
- **Una sola persona como contacto en B2B.** Si decide un comité y solo hablas con uno, vas ciego (ver 134).
- **No anotar por qué se pierde.** Sin la causa, repites el error. "Perdido por precio" vs "por tiempos"
  pide acciones distintas.
- **CRM como cementerio de datos.** Si nadie filtra por "próxima acción", el CRM no vende; solo archiva.
- **Saltarse etapas.** Mandar propuesta sin demo ni calificación = win rate bajo y descuentos para salvar.

## Cómo arrancar mínimo viable (esta semana)
1. Crea la hoja con las 7 columnas. Mete TODAS tus oportunidades abiertas hoy.
2. Asigna etapa y **próxima acción + fecha** a cada una. Las que no tengan acción, decídelas (reactivar o
   matar).
3. Define tu meta del periodo y calcula cobertura y forecast ponderado.
4. Bloquea 15 min cada mañana para trabajar la lista de "acciones de hoy". Eso es el 80% del resultado.

## Siguiente paso típico
Vuelca tus oportunidades en una hoja con etapas y "próxima acción + fecha", calcula tu forecast ponderado
contra la meta, y mira la conversión entre etapas para ver dónde se atasca el embudo (ver 134 para vender
B2B, 131 y 189 para alimentar el pipeline con más leads).
