# 262 — Set, setting y diseño de estudio (por qué esta es la ciencia clínica más difícil de hacer bien)

"Set y setting" —la mentalidad de la persona y el entorno— dejó de ser jerga contracultural para convertirse
en un problema metodológico central: son variables que **modifican el desenlace** y que, a diferencia de la
dosis, no se pueden estandarizar del todo. Sumado a que estas sustancias son imposibles de cegar bien, el
resultado es que los ensayos con psicodélicos son de los más difíciles de diseñar de toda la medicina. Este
módulo explica los problemas y las soluciones metodológicas que se están usando.

**Alcance:** metodología de investigación clínica. No es una guía de preparación de sesiones fuera de un
protocolo autorizado.

Términos: **set** = estado mental, expectativas y personalidad del participante. **setting** = ambiente
físico y social, incluido el equipo. **cegamiento (blinding)** = ocultar la asignación. **placebo activo
(active placebo)** = comparador que produce efectos perceptibles para dificultar la adivinación.
**expectancy** = efecto de lo que el participante espera que ocurra.

## Los cinco problemas metodológicos

### 1. El cegamiento no funciona

Con dosis plenas, prácticamente todos los participantes adivinan si recibieron sustancia o placebo. Un
ensayo "doble ciego" en el que el 90 % adivina correctamente **no es funcionalmente doble ciego**. Esto
infla el efecto por expectativa en el brazo activo y lo deprime en el placebo.

Soluciones parciales, ninguna perfecta:

| Estrategia | Cómo funciona | Límite |
|---|---|---|
| Placebo activo bajo (1 mg) | Produce algo perceptible | Muchos siguen distinguiendo |
| Comparador de dosis (25 vs 10 vs 1 mg) | Todos reciben sustancia; se compara la dosis | No hay grupo sin sustancia |
| Comparador activo (niacina, metilfenidato) | Genera efectos somáticos | No imita el efecto psicodélico |
| Medir el cegamiento | Preguntar qué cree que recibió y **reportarlo** | No lo arregla, pero lo hace transparente |
| Cegar al evaluador | Evaluador independiente que no estuvo en la sesión | Es lo más efectivo y a menudo se omite |

La práctica mínima exigible hoy: **preguntar y reportar la adivinación**. Un ensayo que no lo reporta está
escondiendo su limitación principal.

### 2. La expectativa es enorme

Los participantes de estos estudios suelen llegar con expectativas altísimas, alimentadas por prensa. La
expectativa es un predictor documentado de desenlace en este campo. Se maneja midiéndola al inicio y
ajustando por ella en el análisis, no ignorándola.

### 3. La terapia está dentro del paquete

Cada protocolo incluye preparación, acompañamiento e integración. Eso significa que el ensayo prueba
**"psilocibina + acompañamiento psicológico"**, no psilocibina sola. Los reguladores lo saben; por eso el
producto en desarrollo se evalúa junto con su modelo de administración. Cuando alguien dice "la psilocibina
hace X", el enunciado correcto lleva el acompañamiento adentro.

### 4. El entorno no está estandarizado

Sala, música, iluminación, antifaz, número de facilitadores, estilo de acompañamiento: todo varía entre
centros y todo puede afectar el desenlace. En los ensayos multicéntricos se manualiza el procedimiento y se
entrena a los equipos, pero la variabilidad residual es alta comparada con, digamos, administrar una
inyección.

### 5. El desenlace es autorreportado

MADRS, BDI y las escalas de experiencia dependen de lo que la persona dice. Con cegamiento roto y
expectativa alta, esa combinación es exactamente donde más sesgo se cuela. La mitigación estándar:
**evaluadores independientes ciegos** que califican por entrevista remota.

## Cómo se comprueba la calidad metodológica de un estudio

```
Checklist para leer un ensayo con psicodélicos (si falla ≥ 3, la conclusión se cita con reservas):
[ ] ¿Está preregistrado (ClinicalTrials.gov / ISRCTN) y coincide el desenlace primario?
[ ] ¿Qué comparador se usó y por qué?
[ ] ¿Se midió y REPORTÓ la eficacia del cegamiento?
[ ] ¿Los evaluadores de desenlace eran independientes y ciegos?
[ ] ¿Se midió la expectativa basal?
[ ] ¿Está manualizado el acompañamiento? ¿Se reporta el entrenamiento del equipo?
[ ] ¿Se reportan eventos adversos y experiencias difíciles (CEQ), no solo los positivos?
[ ] ¿Cuánto duró el seguimiento? ¿Hubo pérdidas diferenciales entre brazos?
[ ] ¿Tamaño de efecto con intervalo de confianza, no solo p?
[ ] ¿Conflictos de interés y financiación declarados?
```

## Diseños que el campo está usando

| Diseño | Ventaja | Desventaja |
|---|---|---|
| Paralelo con dosis-comparador (fase 3 de COMP360: 25 vs 10 vs 1 mg) | Todos reciben algo; escalable | Sin brazo verdaderamente inactivo |
| Cruzado (crossover) | Cada quien es su propio control | Efectos de arrastre; el ciego se rompe aún más |
| Comparador activo (p. ej. frente a un antidepresivo establecido) | Pregunta clínicamente relevante | Muy caro y largo |
| Ensayo de "dosis-respuesta" | Buena información farmacológica | No responde si hay efecto vs no tratamiento |
| Autocegado por el participante (self-blinding) | Barato, escalable, usado en microdosis (`264`) | Solo válido si el protocolo de cegado es riguroso |

## Ejemplo aplicado (ILUSTRATIVO) — dos lecturas del mismo resultado

```
Resultado: en un ensayo, el brazo de dosis alta mejora 8 puntos más en MADRS que el brazo de 1 mg.

Lectura ingenua:  "la sustancia produce 8 puntos de mejoría".
Lectura rigurosa: "en este diseño, la diferencia entre 25 mg y 1 mg, con acompañamiento
psicológico idéntico en ambos brazos, fue de 8 puntos a la semana 6; el 88 % de los
participantes adivinó correctamente su asignación, por lo que parte de esa diferencia puede
atribuirse a expectativa. El intervalo de confianza fue [x, y]."
```

La segunda es la que un químico —o cualquier persona seria con datos— debe escribir.

## Errores comunes

- **Llamar "doble ciego" a un estudio donde todos adivinaron.** Hay que reportar la adivinación.
- **Atribuir el efecto a la molécula sola.** El paquete incluye acompañamiento.
- **No preregistrar y cambiar el desenlace primario después.** Es la fuente clásica de falsos positivos.
- **Reportar solo lo positivo.** Sin CEQ ni eventos adversos, el retrato está incompleto.
- **Comparar entre estudios con settings distintos** como si fueran la misma intervención.
- **Confundir "n grande" con "bien diseñado".** Un estudio grande y mal cegado sigue estando mal cegado.

## Conexión con otros módulos

→ `261-psicometria-meq30-5d-asc-y-escalas.md` — los instrumentos de desenlace.
→ `259-dosis-en-investigacion-clinica.md` y `260-screening-de-seguridad-y-contraindicaciones.md`.
→ `264-microdosis-que-dice-la-evidencia.md` — donde el cegamiento sí se puede lograr, y qué salió.
→ `288-como-disenar-un-estudio-piloto.md` y `287-diseno-de-experimentos-doe.md`.
→ `289-etica-de-la-investigacion-y-consentimiento.md` — consentimiento en un estado alterado.
→ `11-como-leer-un-paper-cientifico.md` y `12-niveles-de-evidencia.md`.
