# 11 — Cómo leer un paper científico (en 20 minutos, sin ser científico)

Un artículo científico está escrito para otros científicos, pero se puede desarmar con una rutina fija.
No necesitas entender cada ecuación: necesitas responder cinco preguntas —qué midieron, en quién,
cuánto, comparado con qué, y quién lo pagó— y con eso ya puedes decidir si esa referencia sostiene o
no lo que quieres decir de tu producto. Esto importa porque el 90 % de los "estudios" que circulan en
el marketing de suplementos, al abrirlos, resultan ser ensayos en células a concentraciones que jamás
se alcanzan en sangre, o en ratones a dosis que serían 40 g diarios en un humano.

Términos: **abstract (resumen)** = síntesis del artículo. **métodos (methods)** = cómo se hizo.
**n** = número de sujetos o réplicas. **p-valor (p-value)** = probabilidad de ver ese resultado si no
hubiera efecto real; p < 0,05 es la convención de "significativo". **tamaño del efecto (effect size)**
= qué tan grande es la diferencia, no solo si existe. **doble ciego (double-blind)** = ni el sujeto ni
el investigador saben quién recibió el activo. **conflicto de interés (conflict of interest)** =
relación económica que puede sesgar.

## La rutina de 20 minutos, en orden

```
minuto 0-2    TÍTULO + ABSTRACT: ¿de qué especie, qué compuesto, qué modelo, qué resultado?
minuto 2-5    MÉTODOS, sección de material: ¿qué extracto exactamente? ¿cuerpo fructífero o micelio?
              ¿qué solvente? ¿estandarizado a qué? Si no lo dicen, el estudio no es replicable.
minuto 5-9    MÉTODOS, diseño: modelo (célula / animal / humano), n, control, ciego, aleatorización,
              duración, dosis y vía de administración.
minuto 9-14   RESULTADOS: mirar las FIGURAS y TABLAS antes que el texto. ¿Hay barras de error?
              ¿Cuál es la magnitud del cambio, no solo el asterisco?
minuto 14-17  DISCUSIÓN, primer y último párrafo: qué dicen los autores que significa, y qué
              limitaciones reconocen (esa parte es oro).
minuto 17-20  FINANCIACIÓN Y CONFLICTOS + revista + año. Escribir una frase con el alcance real.
```

Regla dura: **el abstract exagera casi siempre**. La verdad está en métodos y en las limitaciones.

## Las cinco preguntas que deciden si te sirve

| Pregunta | Qué buscar | Bandera roja |
|---|---|---|
| ¿Qué midieron? | El analito y el desenlace concreto | Desenlaces cambiados a mitad del estudio |
| ¿En quién / en qué? | Célula, animal, humano; y qué especie | Extrapolar in vitro a humano sin decirlo |
| ¿Cuánta dosis y por qué vía? | mg/kg, duración, oral vs intraperitoneal | Dosis inalcanzable; vía que no es la de tu producto |
| ¿Comparado con qué? | Control, placebo, grupo paralelo | Sin control; comparación contra el mismo grupo antes/después |
| ¿Quién lo pagó? | Sección de funding y COI | Financiado por quien vende el ingrediente, sin declararlo |

## El material del estudio: donde se cae la mitad de las citas de hongos

Un artículo sobre "Hericium erinaceus" puede referirse a: cuerpo fructífero seco, extracto acuoso,
extracto etanólico, micelio en cultivo líquido, micelio en grano, o un compuesto aislado (erinacina A).
**Son productos químicamente distintos.** Si el estudio usó extracto etanólico de micelio en cultivo
líquido y tú vendes cuerpo fructífero en polvo, el estudio no habla de tu producto. Lo mismo en
cannabis: un ensayo con CBD aislado a 300 mg/día no respalda un aceite de espectro completo con 20 mg.

Antes de citar, escribe esta línea: *"El estudio usó [material exacto] a [dosis] por [vía] durante
[tiempo] en [modelo, n=X]."* Si no puedes completarla, no puedes citarlo.

## Significancia estadística no es relevancia práctica

`p < 0,05` dice que probablemente el efecto no es azar. No dice que sea grande ni que le importe a
nadie. Con n grande, diferencias minúsculas salen "significativas". Con n = 8 ratones, un p bonito
puede ser ruido afortunado.

Lo que hay que mirar: **magnitud del cambio** (¿mejoró 3 % o 30 %?), **intervalo de confianza** (si
cruza el cero, cuidado) y si el desenlace es clínicamente relevante o es un marcador intermedio.
Para pruebas y comparaciones, ruteo a `Matematicas_lushows`.

## Cómo se comprueba que la referencia aguanta

```
[ ] Tengo el PDF completo, no el abstract ni el post que lo resume
[ ] El material del estudio coincide con mi producto (especie, parte, tipo de extracto)
[ ] La dosis es alcanzable con mi porción diaria, por la misma vía
[ ] Hay grupo control y, si es humano, aleatorización y ciego
[ ] El n es razonable y las limitaciones están declaradas
[ ] Sé quién financió el estudio
[ ] Puedo escribir la frase con nivel de evidencia marcado, sin claim de enfermedad
```

## Ejemplo aplicado (BIO-SETA)

Encuentras un artículo: extracto etanólico de micelio de *Hericium erinaceus*, 500 mg/kg vía oral,
28 días, ratones, n = 10 por grupo, mejora en una prueba de memoria espacial frente a control
`[animal]` **(ILUSTRATIVO)**.

Traducción a tu realidad:

- La dosis en ratón no se convierte a humano multiplicando por el peso. Hay factores de conversión
  alométrica y aun así son estimaciones (ver `134`). El resultado no autoriza a decir "tome 2 cápsulas".
- El material es **micelio** en extracto etanólico; tú vendes cuerpo fructífero en extracto acuoso. La
  química no es la misma (ver `217`, `241`).
- Es `[animal]`, no clínico. No se puede insinuar efecto en personas.
- Es citable como contexto de investigación, no como respaldo del producto.

Frase que sí puedes usar: *"Hericium erinaceus es objeto de investigación activa; se han reportado
efectos sobre marcadores neuronales en estudios de laboratorio y en modelos animales `[in vitro]`
`[animal]`. La evidencia en humanos aún es limitada."* Sin promesa, sin enfermedad, con alcance
(ver `268`, `293`).

## Errores comunes

- **Citar el abstract.** Ahí está la versión optimista; los métodos cuentan otra historia.
- **Ignorar el material.** Micelio ≠ cuerpo fructífero ≠ compuesto aislado.
- **Convertir dosis de animal a humano de memoria.** Es un cálculo con supuestos, no una regla de tres.
- **Confundir p pequeño con efecto grande.**
- **Tomar un estudio único como establecido.** Sin réplica independiente, es una pista.
- **No mirar la financiación.** No invalida el estudio, pero cambia cuánto peso le das.
- **Citar revistas depredadoras.** Si publica en 48 horas por pago, no hubo revisión real.

## Conexión con otros módulos

→ `03-honestidad-cientifica-y-fuentes.md` — jerarquía de fuentes y cómo citar.
→ `12-niveles-de-evidencia.md` — la escala que le pones al hallazgo.
→ `10-glosario-quimico-esencial.md` — los términos que aparecerán en métodos.
→ `119-farmacodinamia-y-dosis-respuesta.md` — por qué la dosis manda.
→ `134-toxicologia-basica-dosis-y-riesgo.md` — conversión de dosis y seguridad.
→ `248-evidencia-clinica-de-hongos-funcionales-2026.md` — el estado del arte, ya filtrado.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se traduce a lenguaje de cliente.