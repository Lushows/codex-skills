# 13 — Ruteo a otras skills (qué parte de tu problema no es química)

Casi ningún problema real es solo químico. "¿Puedo vender este extracto?" tiene una parte química
(¿qué tiene, medido cómo?), una parte de cumplimiento (¿qué permite la norma?), una parte de costos
(¿cuánto me sale el kilo de activo?), una parte de precio (¿a cuánto lo vendo?), una parte de etiqueta
(¿cómo se ve?) y una parte de venta (¿cómo lo explico?). Esta skill es dueña de la primera y de una
buena porción de la segunda; las demás tienen dueño propio. Rutear no es tercerizar: es evitar que un
químico opine de precios y que un vendedor invente un porcentaje. Cada dato debe salir de quien
responde por él.

Términos: **ruteo (routing)** = derivar una parte del problema a la skill dueña de ese tema.
**dueño del tema (topic owner)** = la skill que responde por ese dato y lo mantiene coherente.
**frontera (boundary)** = el punto exacto donde termina una responsabilidad y empieza otra.

## Tabla de ruteo (la de `SKILL.md`)

| Necesidad | Skill |
|---|---|
| Cualquier cálculo que sostenga una decisión | `Matematicas_lushows` |
| Costos, inventario, papeles contables, PILA | `contador_lushows` |
| Precio, viabilidad, unit economics, plan de negocio | `economist_lushows` |
| Cumplimiento operativo colombiano del negocio | `AVIS_lushows` |
| Etiqueta, empaque, identidad visual | `directorcreativo_lushows` |
| Cómo se le comunica al cliente / se vende | `ventas_lushows` |
| Web, landing, e-commerce | `desingweb-lushows` |

## Dónde está exactamente cada frontera

| Tema | Lo que hace Quimico_lushows | Lo que hace la otra skill |
|---|---|---|
| Cálculos | Plantea la ecuación, define unidades y base, interpreta el resultado | `Matematicas_lushows` ejecuta y verifica el número |
| Costos | Da el consumo real de materia prima, solvente y análisis por lote | `contador_lushows` lo vuelve costo unitario, inventario y asiento |
| Precio | Dice cuánto cuesta el kilo de activo y qué análisis son obligatorios | `economist_lushows` fija precio, margen y viabilidad |
| Cumplimiento sanitario | INVIMA, claims, registro, especificación, expediente técnico | `AVIS_lushows` lleva Cámara de Comercio, RUT, SG-SST, bomberos, papeles del local |
| Etiqueta | Define qué texto es legalmente sostenible y qué números van | `directorcreativo_lushows` la diseña y la maqueta |
| Comunicación | Traduce evidencia a frases honestas y su nivel | `ventas_lushows` construye el guion, la objeción y el cierre |
| Web | Aporta el contenido técnico verificado | `desingweb-lushows` construye la página |

Regla dura de esta skill: **los números de la etiqueta y los claims salen siempre de aquí**, aunque el
diseño y la venta los ejecute otra skill. Ningún porcentaje aparece en un empaque sin haber pasado por
método, unidad, base y fuente (ver `02`).

## Cálculos: la regla más estricta

Toda cuenta que sostenga una decisión —dosis por cápsula, rendimiento, vida útil, límite de
exposición, conversión de unidades— se **ejecuta en código**, no en la cabeza. Primero se intenta con
`lab-tools/`; si el cálculo es estadístico, financiero o de optimización, se rutea a
`Matematicas_lushows`. La aritmética mental está prohibida en esta skill, sin excepciones.

```
Ejecuta aquí (lab-tools/)              Rutea a Matematicas_lushows
-----------------------------------    ------------------------------------------
conversión de unidades y bases         pruebas estadísticas entre lotes
mg por cápsula y por porción           regresión, intervalos de confianza, potencia
THC total y descarboxilación           VPN, TIR, punto de equilibrio
rendimiento y ratio de extracción      diseño de experimentos y optimización
LOD/LOQ desde curva                    proyecciones y simulación
Arrhenius para vida útil                verificación cruzada de cualquier resultado
```

## Cómo se comprueba que ruteaste bien

```
[ ] ¿Algún número de dinero salió de esta skill sin pasar por contador/economist? (no debería)
[ ] ¿Algún porcentaje de activo salió de otra skill sin método y base? (no debería)
[ ] ¿El claim de la etiqueta lo aprobó el frente de cumplimiento sanitario? (267, 268, 272)
[ ] ¿El cálculo se ejecutó y se verificó por segunda vía?
[ ] ¿Cada skill recibió el contexto que necesita, no todo el problema?
```

## Cómo se pasa el balón (formato del handoff)

Cuando ruteas, entrega el dato ya limpio, no el problema entero:

```
A contador_lushows:
  "Por lote de 10 kg: 40 L de etanol 96 %, 3 análisis externos (β-glucano, metales, microbiología),
   rendimiento 23 % p/p. Necesito costo unitario por frasco de 60 cápsulas."

A economist_lushows:
  "Costo del kilo de β-glucano puro en mi extracto: USD 207 (ILUSTRATIVO). Porción diaria 221 mg.
   Necesito precio y margen para el canal de WhatsApp."

A directorcreativo_lushows:
  "Texto aprobado para etiqueta: 'β-glucanos (1,3;1,6) 220 mg por porción'. Prohibido cualquier verbo
   de enfermedad. Debe caber también el lote, la fecha de vencimiento y el registro."

A ventas_lushows:
  "Diferenciador real: analizamos β-glucano por método enzimático, no polisacáridos totales.
   Nivel de evidencia de los efectos: [in vitro] y [animal]. No se puede prometer efecto."
```

## Ejemplo aplicado (BIO-SETA)

Pregunta que llega: *"¿Lanzo el extracto de reishi a $89.000 el frasco?"*

Desarme y ruteo:

1. **Aquí (química)**: ¿cuánto β-glucano tiene el lote, medido por qué método y en qué base? ¿qué
   análisis obligatorios faltan (metales, microbiología)? ¿qué se puede decir en la etiqueta?
2. **`Matematicas_lushows`**: mg por porción, costo por mg de activo, intervalos entre lotes.
3. **`contador_lushows`**: costo real por frasco con materia prima, solvente, análisis, envase y merma.
4. **`economist_lushows`**: precio, margen, punto de equilibrio, comparación con la competencia.
5. **`AVIS_lushows`**: papeles del negocio, SG-SST de la planta, obligaciones del local.
6. **`directorcreativo_lushows`**: etiqueta con el texto aprobado.
7. **`ventas_lushows`**: cómo se explica el diferenciador sin prometer efectos.

Si intentas responder los siete frentes desde uno solo, o inventas números de los otros seis, el
error aparece siempre en el mismo lugar: un claim que no se puede sostener o un margen que no existía.

## Errores comunes

- **Pedirle precio al químico.** Va a darte costo, que no es precio.
- **Dejar que marketing escriba el porcentaje.** El número nace aquí o no nace.
- **Rutear el problema completo** en vez del dato específico; la otra skill pierde tiempo re-descubriendo.
- **Saltarse cumplimiento sanitario** y descubrir el problema con la etiqueta ya impresa.
- **Hacer la cuenta de memoria "porque es fácil".** Las fáciles son las que se equivocan sin que nadie
  las revise.
- **Confundir `AVIS_lushows` con cumplimiento sanitario de producto.** AVIS lleva los papeles del
  negocio; el registro sanitario y los claims viven aquí (ver `266`–`272`).

## Conexión con otros módulos

→ `01-como-usar-esta-skill.md` — los modos de trabajo y cómo se pide.
→ `02-ningun-dato-sin-metodo.md` — por qué el número no puede nacer fuera de aquí.
→ `14-como-trabajar-con-un-quimico-de-universidad.md` — el ruteo hacia una persona real.
→ `291-costos-de-analisis-y-presupuesto.md` — el dato que se le pasa a contabilidad.
→ `293-como-comunicar-ciencia-sin-mentir.md` — el puente hacia ventas y diseño.
→ `294-informe-tecnico-y-pdf.md` — el formato del entregable que se comparte.