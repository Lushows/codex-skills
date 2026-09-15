# 129 — Sistema endocannabinoide (el sistema real, y el mito del "déficit endocannabinoide")

El sistema endocannabinoide existe, está bien caracterizado y es fascinante. Lo que no está demostrado es
casi todo lo que el marketing del CBD dice sobre él. Este módulo separa las dos cosas: la fisiología con
respaldo experimental por un lado, y por otro la hipótesis del "déficit endocannabinoide clínico", que
sigue siendo una hipótesis y se vende como si fuera un diagnóstico. El error caro que evita: construir un
producto sobre la idea de que la gente tiene una "deficiencia" que hay que "reponer" — una afirmación que
no se puede medir ni sostener.

Términos: **sistema endocannabinoide (endocannabinoid system, ECS)** = conjunto de receptores CB1/CB2, sus
ligandos endógenos y las enzimas que los fabrican y destruyen. **Anandamida (AEA)** = endocannabinoide
derivado de araquidónico, agonista parcial de CB1. **2-AG (2-arachidonoylglycerol)** = el endocannabinoide
más abundante, agonista pleno de CB1. **FAAH (fatty acid amide hydrolase)** = enzima que degrada anandamida.
**MAGL (monoacylglycerol lipase)** = enzima que degrada 2-AG. **Señalización retrógrada (retrograde
signaling)** = el mensajero va de la neurona postsináptica hacia la presináptica, al revés de lo habitual.

## Lo que sí está establecido

| Componente | Dónde predomina | Qué hace |
|---|---|---|
| CB1 | Sistema nervioso central (uno de los GPCR más abundantes del cerebro), también periferia | Reduce liberación de neurotransmisor en la presinapsis |
| CB2 | Células inmunes, bazo, microglía | Modula respuesta inmune |
| Anandamida (AEA) | Cerebro y periferia | Agonista parcial CB1; "tono" bajo y sostenido |
| 2-AG | Cerebro (más abundante) | Agonista pleno CB1; señal a demanda |
| FAAH / MAGL | Neuronas y glía | Terminan la señal |

Mecanismo central, bien documentado `[animal]` / `[in vitro]`: los endocannabinoides **se sintetizan a
demanda** (no se almacenan en vesículas), viajan **hacia atrás** por la sinapsis y frenan la liberación del
neurotransmisor de la neurona presináptica. Es un sistema de freno modulador, no un sistema que "da"
nada. Esa imagen —freno fino— es la que hay que usar cuando se explica.

Y una consecuencia farmacológica directa: el THC es agonista **parcial** de CB1 (`120`), mientras los
cannabinoides sintéticos de calle son agonistas plenos, lo que ayuda a explicar por qué su perfil de
toxicidad aguda es mucho peor `[clínico]`.

## El papel real del CBD (no es un agonista cannabinoide)

Esto tumba media publicidad del sector: **el CBD tiene afinidad ortostérica baja por CB1 y CB2**. Lo que la
literatura describe es un perfil multidiana y, en buena parte, `[in vitro]`:

| Blanco propuesto del CBD | Efecto descrito | Nivel |
|---|---|---|
| CB1 | Modulador alostérico negativo | `[in vitro]` |
| TRPV1, TRPA1 | Agonismo/desensibilización | `[in vitro]` |
| GPR55 | Antagonismo | `[in vitro]` |
| 5-HT1A | Agonismo a concentraciones altas | `[in vitro]` |
| PPARγ | Activación | `[in vitro]` |
| FAAH / transporte de AEA | Elevación de anandamida | `[in vitro]` / `[clínico]` limitado |
| **CYP3A4, CYP2C19** | **Inhibición** | `[clínico]` — el efecto mejor documentado |

Léelo dos veces: **el efecto del CBD con mejor respaldo clínico no es un beneficio, es una interacción
farmacológica** (ver `124`, `139`). Cualquiera que venda CBD y no advierta esto está siendo negligente.

## El mito: "déficit endocannabinoide clínico"

La hipótesis del **clinical endocannabinoid deficiency (CED)** fue propuesta por Ethan Russo en 2004 y
reformulada en 2016: postula que ciertos síndromes de difícil tratamiento (se suele citar la tríada
migraña, fibromialgia y síndrome de intestino irritable) compartirían un tono endocannabinoide bajo.

Lo que hay a favor y en contra, sin adornos:

**A favor**
- Diferencias reportadas en niveles de anandamida en líquido cefalorraquídeo en algunos grupos `[clínico,
  observacional]`.
- Estudios de imagen sugiriendo hipofunción del ECS en ciertas condiciones `[clínico, observacional]`.

**En contra / lo que falta**
- **No existe un valor de referencia clínico** de "tono endocannabinoide". No hay rango normal establecido.
- **No hay una prueba de laboratorio validada** que diagnostique el déficit en una persona. Ninguna.
- Los hallazgos son correlacionales; no se ha demostrado causalidad ni dirección.
- La hipótesis no se ha investigado con la profundidad que su popularidad comercial sugeriría, y no ha
  sido adoptada como entidad diagnóstica por ninguna autoridad sanitaria a agosto de 2026.

Conclusión de químico, tal cual: **CED es una hipótesis interesante y sin validación diagnóstica.** Usarla
como argumento de venta ("tu cuerpo tiene déficit de endocannabinoides, repóntelo") es vender un
diagnóstico inexistente, y además roza el claim de enfermedad — prohibido (`268`).

Prueba de fuego, y es sencilla: si alguien afirma que tienes déficit endocannabinoide, pregúntale **con qué
examen se mide, cuál es el rango normal y qué laboratorio acreditado lo hace**. No hay respuesta.

## Cómo se mide (lo que sí es medible)

| Qué | Método | Unidad | Nivel |
|---|---|---|---|
| AEA y 2-AG en plasma o LCR | LC-MS/MS con estándar interno deuterado | ng/mL o pmol/mL | Investigación; **no es prueba diagnóstica** |
| Densidad de CB1 in vivo | PET con radiotrazador de CB1 | unidades de unión | Investigación `[clínico]` |
| Actividad FAAH | Ensayo enzimático en tejido/plasma | nmol/min/mg | `[in vitro]` |
| Contenido de CBD/THC del producto | HPLC-DAD (`198`) | % p/p, mg/unidad | Rutina, exigible en COA |

Nota analítica importante: 2-AG es notoriamente inestable y se isomeriza a 1-AG durante el procesamiento de
la muestra. Cualquier dato de 2-AG sin control de preanalítica (congelación inmediata, inhibidores) es
sospechoso. Es un buen ejemplo de por qué el método importa más que el número (`02`).

## Ejemplo aplicado — reescribir una ficha de producto

Texto original de un cliente **(ILUSTRATIVO)**:
> "Nuestro aceite de CBD restaura el equilibrio de tu sistema endocannabinoide, que hoy está en déficit por
> el estrés moderno."

Problemas: afirma un déficit no medible, afirma restauración no demostrada, e induce a la idea de tratar
una condición. Versión defendible:

> "Aceite con CBD estandarizado: 30 mg de CBD por mL, verificado por HPLC-DAD, lote y COA disponibles,
> THC total por debajo del límite legal aplicable. Importante: el CBD puede interactuar con medicamentos
> metabolizados por el hígado; consulte con su médico si toma algún tratamiento."

La segunda versión vende menos fantasía y sostiene una auditoría. Cómo comunicarlo sin perder fuerza
comercial es trabajo de `ventas_lushows` y `293`, no de inventar ciencia.

## Errores comunes

- Vender CBD como "agonista cannabinoide". No lo es; su afinidad ortostérica por CB1/CB2 es baja.
- Usar el "déficit endocannabinoide" como si fuera un diagnóstico. No hay prueba ni rango de referencia.
- Omitir la advertencia de interacción CYP, que es justamente lo mejor documentado del CBD.
- Confundir CB2 con "sistema inmune reforzado". CB2 modula; no es un botón de refuerzo.
- Medir 2-AG sin controlar la preanalítica y reportar el número como si fuera confiable.
- Extrapolar de modelos animales de dolor a promesas humanas. Distinto nivel de evidencia (`12`).

## Conexión con otros módulos

→ `118-receptores-y-transduccion-de-senal.md` — CB1/CB2 son GPCR.
→ `120-afinidad-eficacia-y-agonismo-parcial.md` — por qué el THC parcial y el CBD alostérico no son lo mismo.
→ `124-citocromo-p450-e-interacciones.md` — la interacción real del CBD.
→ `205-farmacologia-del-thc.md` y `206-farmacologia-del-cbd.md` — el detalle por molécula.
→ `183-efecto-sequito-que-dice-la-evidencia.md` — otra hipótesis popular examinada con la misma vara.
