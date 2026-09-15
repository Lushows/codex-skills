# 55 — Del clic al cierre

Lee este módulo cuando tus ads traigan clics pero no ventas, cuando no haya TikTok Shop y todo deba cerrarse por WhatsApp, o cuando un cliente te diga "me llegan mensajes pero no compran". Aquí vive el **handoff**: el puente entre el clic en TikTok y la venta cerrada. El media buyer construye el puente; el que cierra es `ventas_lushows` (módulo 82). Si el puente está roto, el mejor ad del mundo no vende. El frame: TikTok **descubre** (ver 00), WhatsApp **cierra**. El handoff es donde se conectan los dos mundos — y donde más plata se pierde en LatAm.

## El handoff TikTok → WhatsApp es donde se pierde la plata

En LatAm, cuando no hay TikTok Shop (verifica país, ver 50), el camino es **TikTok descubre → WhatsApp cierra**. El punto más frágil de toda la operación es ese salto. Lo que pasa mal:

- El usuario toca el ad, llega a WhatsApp, y no sabe **por qué** está ahí.
- Tiene que **escribir desde cero** qué quiere → fricción → se va.
- El negocio responde **horas después** → el lead ya está frío (ver 54).
- Nadie sabe de **qué ad** vino → no puedes optimizar (ver 57).

Cada una de esas fugas se arregla con diseño del handoff. No es trabajo de "ventas" — es trabajo de media buyer. Tú entregas un lead **tibio, contextualizado y rastreable**, no un número frío. En TikTok, el objetivo de campaña para esto suele ser **Tráfico** o **Interacción/Mensajes** llevando a un link `wa.me`, o **Lead Generation** con auto-mensaje (ver 54). Lo importante no es el objetivo de la plataforma: es que el evento que optimizas sea lo más cercano a la venta posible (ver 14, 57).

## Las cuatro palancas del handoff

**1. Mensaje pre-llenado (click-to-WhatsApp).** El ad lleva a un link de WhatsApp con texto ya escrito. El usuario solo le da enviar:

```
https://wa.me/57300XXXXXXX?text=Hola,%20vengo%20del%20video%20de%20TikTok%20y%20quiero%20info%20de%20la%20Calculadora%20de%20Costos
```

El texto prellenado hace tres cosas: baja la fricción (no escribe de cero), da contexto al negocio (sabe de qué viene), y sirve de **etiqueta de origen** (sabes que vino de TikTok). El espacio se codifica como `%20`; usa un acortador o un generador `wa.me` si te confunde la URL.

**2. Etiqueta de origen + click ID.** Usa un texto prellenado distinto por campaña o creativo ("vengo del video A", "vengo del video B"). Así sabes qué creativo trae los que **compran**, no solo los que escriben. Y captura el **identificador de clic de TikTok (`ttclid`)** en el link para poder cerrar el loop de medición (ver 57). Sin esto, optimizas a ciegas.

**3. Velocidad <5 min.** El primer toque debe ser en **menos de 5 minutos** (ver 54). Dispara un mensaje automático de bienvenida apenas escriben, mientras un humano toma la conversación. En GastroLatam el bot (Luis) da ese primer toque solo.

**4. Contexto al que cierra.** El que responde debe ver de qué creativo vino y qué quería, no empezar de cero. Pasa nombre + intención + origen.

| Palanca | Qué resuelve | Cómo |
|---|---|---|
| Mensaje pre-llenado | Fricción + contexto | `wa.me` con `?text=` |
| Etiqueta de origen + `ttclid` | Saber qué ad vende + medir | Texto distinto por creativo + click ID |
| Velocidad <5 min | Lead que se enfría | Auto-respuesta + humano |
| Contexto al cierre | Arrancar en frío | Pasar nombre+intención+origen |

## Plantilla de primer mensaje (auto-respuesta)

```
Hola [nombre] 👋 Vi que vienes del video de TikTok.
Te cuento rápido de la Calculadora de Costos Gastronómicos:
es un Excel para saber cuánto te cuesta de verdad cada plato
y dejar de vender a pérdida. Pago único $10.000 COP, acceso inmediato.
¿Te muestro cómo funciona?
```

Corto, en el idioma del cliente, con el próximo paso claro. El guion completo de cierre (objeciones, "está muy caro", negociación) NO va aquí — es `ventas_lushows`.

## Quién hace qué: el media buyer NO cierra

División de trabajo, clara:

- **Media buyer (tú, este skill):** trae el lead, lo contextualiza con mensaje prellenado, lo etiqueta con `ttclid`, lo mide, lo entrega tibio. Optimiza el ad por **conversación calificada / compra**, no por clic (ver 14, 57).
- **El que cierra (`ventas_lushows`, módulo 82 WhatsApp):** responde, califica, maneja objeciones, cierra. El oficio de vender por WhatsApp es de ese skill — no improvises el guion de cierre aquí.
- **La web/checkout** (si el cierre no es TikTok Shop): la construye `desingweb-lushows`. Que cargue rápido, sea vertical-friendly y congruente con el ad (ver 48).
- **Los números** (¿este CAC cierra contra el ticket?): `economist_lushows`.

Regla práctica: si te piden "mejorar las ventas" y el problema es el guion de WhatsApp, **rutea a `ventas_lushows`** — no es un problema de pauta. Si el problema es que llegan curiosos, **sí es tuyo**: ajusta creativo y evento de optimización (ver 57).

## Cómo saber dónde se rompe el puente

Diagnóstico por síntoma:

| Síntoma | Dónde está el problema | Quién lo arregla |
|---|---|---|
| Muchos clics, pocos mensajes | Link / mensaje prellenado / fricción | Media buyer (este módulo) |
| Muchos mensajes, pocas ventas | Guion de cierre, velocidad de respuesta | `ventas_lushows` |
| Llegan curiosos sin plata | Creativo / evento de optimización | Media buyer (ver 57, 58) |
| No sabes qué ad vende | Falta etiqueta de origen / `ttclid` | Media buyer (ver 57) |
| Web lenta, abandono | Landing | `desingweb-lushows` (ver 48) |

## Errores comunes — blacklist

- **Link de WhatsApp sin texto prellenado.** El usuario llega frío y mudo; usa `wa.me` con `?text=` (ver arriba).
- **Mismo texto prellenado para todas las campañas.** No sabes qué ad vende; etiqueta por creativo.
- **No capturar el `ttclid`.** No puedes cerrar el loop de medición; pierdes la optimización por compra (ver 57).
- **Responder horas después.** El lead se enfría; auto-respuesta en <5 min (ver 54).
- **Optimizar el ad por clic en vez de por conversación/compra.** Traes curiosos; sube la conversión real (ver 57).
- **Intentar arreglar el cierre desde la pauta.** El guion de WhatsApp es `ventas_lushows` (módulo 82).
- **Mandar a una web lenta o incongruente con el ad.** Rompe el puente; construye con `desingweb` (ver 48).
- **No medir qué creativo trae compradores.** Sin loop cerrado optimizas humo (ver 57).
