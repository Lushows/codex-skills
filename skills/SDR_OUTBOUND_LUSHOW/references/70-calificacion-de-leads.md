# 70 — Calificación de leads

Calificar (calificar = decidir si un lead vale el tiempo de una reunión de ventas, y capturar por qué) es el trabajo central del SDR una vez que el prospecto responde. Tu job no es cerrar (eso vive en `ventas_lushows`); tu job es filtrar y agendar solo lo que un vendedor (AE = Account Executive, el que cierra) puede convertir. Una reunión mal calificada le roba tiempo al AE, ensucia el pipeline y a la larga destruye la confianza en tu trabajo (ver `78`). Este módulo te da los tres marcos de calificación que un SDR realmente usa —BANT, CHAMP y MEDDIC-lite— y qué preguntar para calificar en 5–8 minutos, no en una demo de 40.

## El principio: calificas para PROTEGER el tiempo del AE

Un SDR promedio agenda todo lo que se mueve. Un SDR de élite agenda menos y mejor: su tasa de reuniones-que-avanzan (show → oportunidad) es la métrica que lo define, no el número bruto de reuniones. La calificación es el filtro. Regla mental: **antes de agendar, tienes que poder escribir 3 frases** — qué dolor tiene, por qué ahora, y quién decide. Si no puedes, no está calificado; sigue preguntando o recíclalo a nurture (ver `76`).

No confundas calificación con interrogatorio. Preguntas 4–6 cosas, con naturalidad, dentro de una conversación corta (ver `71`). El resto lo descubre el AE en la venta consultiva profunda.

## Los tres marcos — cuándo usar cada uno

| Marco | Qué mide | Cuándo te sirve |
|---|---|---|
| **BANT** | Budget, Authority, Need, Timing (presupuesto, autoridad, necesidad, tiempo) | Ventas transaccionales / PYME, ciclo corto. Simple y rápido |
| **CHAMP** | Challenges, Authority, Money, Prioritization (retos primero, luego autoridad, dinero, prioridad) | Cuando el dolor manda; empieza por el problema, no por el bolsillo |
| **MEDDIC-lite** | Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion | B2B mediano/grande, ciclo largo, varios decisores |

BANT es viejo pero funciona en tickets bajos. CHAMP es BANT invertido: pregunta el reto ANTES que el presupuesto (más humano, mejor para descubrimiento). MEDDIC-lite es lo que usa el SDR B2B serio: no lo llenas todo tú, pero identificas al menos el dolor, quién paga (economic buyer) y si hay un aliado interno (champion).

## Qué preguntar — el kit del SDR (traducido a lenguaje humano)

No preguntes "¿tienes presupuesto?". Preguntas envueltas:

- **Need / Challenge (dolor):** "¿Qué te hizo responder / qué estás tratando de resolver con esto ahora mismo?" → el disparador real.
- **Impact (métrica):** "¿Cómo lo están manejando hoy? ¿Cuánto te cuesta / cuánto tiempo se va en eso?" → cuantifica el dolor (ver `Matematicas_lushows` si hay que estimar ROI).
- **Authority (quién decide):** "Además de ti, ¿quién más estaría en esta conversación / mira este tipo de decisión?" → detecta al economic buyer sin decir "¿tú decides?".
- **Timing / Prioritization:** "¿Es algo que quieres resolver este trimestre o estás explorando para más adelante?" → separa *ahora* de *algún día* (los "algún día" van a `76`).
- **Money (suave):** casi nunca preguntas cifra. Basta con "¿han invertido en algo así antes?" o dejarlo para el AE. En PYME transaccional sí puedes anclar rango.

Regla: **1 pregunta de dolor + 1 de impacto + 1 de autoridad + 1 de timing = calificado.** Cuatro preguntas bien hechas superan a un formulario de veinte.

## Umbral de calificación — el semáforo

Define un mínimo escrito para que TODO SDR califique igual (esto es parte del SLA, ver `74`, y de la definición de SQL, ver `72`):

```
CALIFICA (agendar con AE) si cumple AL MENOS:
  ✅ Dolor real y nombrado (no "curiosidad")
  ✅ Encaja con el ICP (ver 10) — sector/tamaño/país correctos
  ✅ Autoridad o acceso al decisor
  ✅ Timing: quiere resolver en un horizonte razonable (no "en 2 años")

RECICLA a nurture (ver 76) si:
  ⏳ Buen fit pero "no ahora"
DESCARTA (o vuelve a marketing) si:
  ❌ No encaja el ICP, sin dolor, o busca otra cosa
```

## Ejemplo real — nota de calificación (LatAm)

Contexto: SDR de un software de gestión para restaurantes, prospecto respondió al cold email.

```
Lead: Andrea Gómez — Gerente, Grupo Sazón (3 restaurantes, Bogotá)
Dolor: pierde plata en inventario, hace el conteo a mano en Excel, no sabe su costo real de plato
Impacto: ~2 h/día del chef en conteos; sospecha 8-10% de merma
Autoridad: ella opera, el dueño (su papá) firma compras > $2M COP → economic buyer = el papá
Timing: quiere ordenarlo ANTES de abrir el 4º local (2 meses)
Veredicto: SQL ✅ — agendar con AE. Champion probable: Andrea.
```

Con eso, el AE entra sabiendo dónde apretar. Eso es un handoff que se agradece (ver `73`).

## Errores comunes

- **Calificar como si fueras el AE.** No hagas discovery profundo ni pitch de producto: solo filtras y agendas. La venta consultiva es de `ventas_lushows`.
- **Agendar por “buena vibra”.** Simpatía no es calificación. Sin dolor + fit + timing, no va.
- **Preguntar presupuesto de frente.** Espanta y rara vez es tu trabajo; el dinero lo aterriza el AE.
- **Sobre-calificar.** Si exiges los 6 campos de MEDDIC como SDR, no agendas nada. Identifica dolor + autoridad + timing y suelta.

## Siguiente paso

Aterriza estas preguntas dentro de la llamada corta del SDR en `71`. Fija con marketing y ventas qué cuenta como calificado en `72` (SQL/MQL/SAL) y `74` (SLA). Cuando esté calificado, pásalo bien en `73`.
