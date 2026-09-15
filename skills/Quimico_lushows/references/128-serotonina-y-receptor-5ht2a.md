# 128 — Serotonina y el receptor 5-HT2A (la farmacología que hay detrás de los psicodélicos clásicos)

El receptor 5-HT2A es el blanco central de los psicodélicos clásicos —psilocina, LSD, mescalina, DMT— y por
eso entender su farmacología es requisito para hablar con seriedad de psilocibina. Este módulo cubre el
sistema serotoninérgico, qué hace el 5-HT2A y cómo se demostró que es el receptor responsable. **No incluye
dosis ni protocolos**: eso vive en el bloque 251–264 y en marco de investigación clínica. Aquí se construye
la base farmacológica. El error caro que evita: hablar de psicodélicos sin saber distinguir un receptor de
otro y terminar diciendo cosas falsas sobre seguridad.

Términos: **serotonina (serotonin, 5-HT)** = 5-hidroxitriptamina, neurotransmisor derivado del triptófano.
**5-HT2A** = receptor acoplado a proteína G (Gq) cuya activación es necesaria para el efecto psicodélico
clásico. **Agonista (agonist)** = ver `120`. **Ketanserina (ketanserin)** = antagonista de 5-HT2A usado en
investigación como herramienta de bloqueo. **Downregulation** = reducción del número de receptores tras
estimulación repetida.

## El sistema serotoninérgico, en corto

La serotonina se sintetiza desde triptófano:

```
Triptófano → (triptófano hidroxilasa, TPH) → 5-HTP → (descarboxilasa) → Serotonina (5-HT)
                                                                            │
                                                          (MAO-A) → ácido 5-hidroxiindolacético (5-HIAA)
```

Dato que casi nadie dice y que ordena la conversación: **la gran mayoría de la serotonina del cuerpo está
en el intestino**, en células enterocromafines, no en el cerebro (reportado en la literatura fisiológica en
torno al 90 %). La serotonina periférica no cruza la barrera hematoencefálica; el cerebro fabrica la suya
(ver `127`). Por eso "tomar serotonina" no tiene sentido farmacológico.

## La familia de receptores

| Receptor | Tipo | Dónde importa | Nota |
|---|---|---|---|
| 5-HT1A | GPCR (Gi) | Autorreceptor somatodendrítico, ansiedad | Blanco de buspirona; la psilocina también tiene afinidad |
| 5-HT2A | GPCR (Gq) | Corteza; **efecto psicodélico** | El eje de este módulo |
| 5-HT2B | GPCR (Gq) | Válvulas cardiacas | **Agonismo crónico se asocia a valvulopatía** `[clínico]` — riesgo real |
| 5-HT2C | GPCR (Gq) | Apetito, ansiedad | Contribuye al perfil de efectos |
| 5-HT3 | Canal iónico | Náusea, vómito | Blanco de ondansetrón |
| 5-HT4/6/7 | GPCR | Motilidad, cognición | Menos caracterizados en este contexto |

El renglón de 5-HT2B es el que más importa desde seguridad y el que menos se menciona en el discurso
entusiasta: la exposición crónica a agonistas de 5-HT2B se ha asociado a valvulopatía cardiaca en humanos
`[clínico]` con otros compuestos (el caso histórico de anorexígenos retirados del mercado). Es una de las
razones por las cuales la conversación sobre **microdosis** repetida no es trivialmente segura (ver `264`).

## Por qué se sabe que el 5-HT2A es el responsable

La evidencia es de las más limpias que hay en psicofarmacología:

1. **Correlación de afinidad**: la potencia de una serie de psicodélicos correlaciona con su afinidad por
   5-HT2A `[in vitro]`.
2. **Bloqueo farmacológico**: pretratar con ketanserina (antagonista 5-HT2A) atenúa o elimina los efectos
   subjetivos de la psilocibina en humanos `[clínico fase 1/2]`. Este es el experimento clave.
3. **Modelos animales**: ratones sin 5-HT2A no muestran la respuesta característica, y se restaura al
   reexpresar el receptor en corteza `[animal]`.
4. **Neuroimagen**: cambios de conectividad funcional asociados a la activación cortical `[clínico]`.

Eso es lo que se puede afirmar. Lo que **no** se puede afirmar es que la activación de 5-HT2A "cure" o
"trate" algo: los desenlaces clínicos son objeto de ensayos en curso y su estado está en `263`.

## Señalización y sesgo

La activación de 5-HT2A acopla a Gq → fosfolipasa C → IP3 + DAG → Ca2+ y PKC. También recluta β-arrestina.
Un tema de investigación activa es si el efecto psicodélico depende de una ruta específica, porque se han
descrito agonistas de 5-HT2A que no producen efecto psicodélico en modelos animales `[animal]` —lo que
alimenta la búsqueda de "no alucinógenos". A agosto de 2026 esto sigue siendo materia de investigación, no
un hecho establecido; trátalo como hipótesis, no como conclusión.

Otro fenómeno bien documentado: **tolerancia rápida (taquifilaxia)** por downregulation de 5-HT2A con
administración repetida `[clínico]`. Es la razón farmacológica por la cual el uso diario no reproduce el
efecto del primer día.

## Cómo se mide

| Pregunta | Método | Unidad | Nivel |
|---|---|---|---|
| Afinidad por 5-HT2A | Radioligando de competencia (p. ej. [³H]ketanserina) | Ki (nM) | `[in vitro]` |
| Activación funcional | Movilización de Ca2+, acumulación de IP1, β-arrestina | EC50, %Emáx | `[in vitro]` |
| Selectividad (incluye 5-HT2B) | Panel de receptores | cociente de Ki | `[in vitro]` |
| Ocupación en humanos | PET con radiotrazador de 5-HT2A | % ocupación | `[clínico fase 1]` |
| Papel causal del receptor | Bloqueo con ketanserina en diseño doble ciego | atenuación de escalas (`261`) | `[clínico fase 1/2]` |

## Ejemplo aplicado — leer un preprint con criterio

Llega un preprint **(ILUSTRATIVO)**: "Compuesto X, Ki 5-HT2A = 12 nM, EC50 = 40 nM, potente psicodélico."
Las preguntas obligatorias antes de creer nada:

1. ¿Cuál es la Ki en **5-HT2B**? Si es similar, hay una bandera roja de seguridad cardiaca.
2. ¿El ensayo funcional es en células que sobreexpresan el receptor? La sobreexpresión infla la potencia.
3. ¿Hay dato de paso de barrera hematoencefálica (`127`) y de exposición in vivo? Sin eso, la Ki es teórica.
4. ¿El descriptor "psicodélico" viene de humanos o de un proxy conductual en roedores (head-twitch
   response)? Son cosas muy distintas: el proxy es `[animal]`.
5. ¿Está publicado y revisado por pares, o es preprint? Se anota el estado (ver `11`).

## Errores comunes

- Hablar de "serotonina baja" como explicación de algo. Es un modelo simplificado que la literatura actual
  no sostiene como causa única, y usarlo lleva directo a claims de enfermedad.
- Ignorar 5-HT2B al evaluar seguridad de agonistas serotoninérgicos, sobre todo en uso repetido.
- Confundir afinidad con actividad funcional, y ambas con efecto en una persona (ver `120`).
- Presentar el head-twitch de roedores como si fuera un efecto psicodélico demostrado.
- Suponer que un antagonista de 5-HT2A "revierte" todo: la atenuación observada no es un interruptor.
- Saltar de farmacología de receptor a afirmaciones terapéuticas. El estado clínico real está en `263`.

## Conexión con otros módulos

→ `118-receptores-y-transduccion-de-senal.md` — cómo funciona un GPCR.
→ `120-afinidad-eficacia-y-agonismo-parcial.md` — Ki, EC50 y selectividad.
→ `127-barrera-hematoencefalica.md` — por qué la psilocina llega y otras moléculas no.
→ `257-farmacologia-de-la-psilocibina.md` — el detalle completo, incluida la línea roja del bloque.
→ `264-microdosis-que-dice-la-evidencia.md` — donde 5-HT2B y la tolerancia se vuelven decisivos.
