# 257 — Farmacología de la psilocibina (qué hace la molécula, y hasta dónde llega lo que sabemos)

La psilocina —recuerda: la activa es la psilocina, no la psilocibina (`251`)— actúa principalmente como
**agonista del receptor de serotonina 5-HT2A**. Ese hecho está sólidamente establecido: bloquear el 5-HT2A
con ketanserina elimina casi por completo los efectos subjetivos en humanos. Lo que viene después —cómo se
traduce esa activación en cambios sostenidos del estado de ánimo— es donde la ciencia todavía discute, y este
módulo distingue con cuidado lo demostrado de lo hipotético.

**Alcance (línea roja):** farmacología descriptiva de investigación. No hay aquí guía de uso, de dosis
personal ni de manejo de sustancia. Las dosis de investigación clínica están en `259`, con su advertencia.

Términos: **agonista (agonist)** = molécula que activa un receptor. **agonista parcial (partial agonist)** =
lo activa menos que el ligando natural aun ocupándolo todo. **sesgo de señalización (biased agonism)** = el
mismo receptor produce señales distintas según qué ligando lo active. **neuroplasticidad (neuroplasticity)** =
capacidad de las neuronas de cambiar sus conexiones.

## El perfil de receptores

| Receptor | Afinidad relativa de psilocina | Relevancia |
|---|---|---|
| 5-HT2A | Alta — la diana principal | Responsable de los efectos subjetivos; demostrado por bloqueo con ketanserina `[clínico]` |
| 5-HT2C | Alta | Contribuye a efectos periféricos y posiblemente al ánimo |
| 5-HT1A | Moderada | Puede modular la respuesta |
| 5-HT2B | Moderada | Relevante para seguridad: agonismo crónico se asocia a valvulopatía (`260`) |
| 5-HT7, 5-HT6, 5-HT5 | Menor | Poco caracterizado funcionalmente |
| Dopamina D2 | Baja/indirecta | La psilocina no es un agonista dopaminérgico directo relevante |

Ese renglón de 5-HT2B es el que más importa desde el punto de vista de seguridad regulatoria, y no por la
psilocibina en sí sino por precedente histórico: la fenfluramina y la dexfenfluramina, agonistas
serotoninérgicos de uso **crónico diario**, se retiraron del mercado en 1997 por valvulopatía cardíaca. Por
eso la exposición repetida y frecuente (es decir, el patrón de microdosis, `264`) tiene una preocupación
teórica de seguridad que la dosis única supervisada no tiene en el mismo grado.

## Qué pasa en el cerebro

Lo establecido `[clínico]` / `[preclínico robusto]`:

- La activación de 5-HT2A ocurre sobre todo en **neuronas piramidales de capa 5 de la corteza**, densas en
  este receptor.
- En neuroimagen humana se observa **desincronización de redes funcionales**, incluida la red neuronal por
  defecto (default mode network, DMN), con aumento de conectividad entre redes que normalmente están
  segregadas.
- El bloqueo previo del 5-HT2A **anula** los efectos subjetivos, lo que cierra la cadena causal.

Lo plausible pero no cerrado `[preclínico]` / `[hipótesis]`:

- **Neuroplasticidad**: en roedores y cultivos se ha documentado aumento de espinas dendríticas y de
  marcadores plásticos tras psicodélicos. La extrapolación directa a humanos es una inferencia, no un dato.
- **"Ventana de plasticidad"** que explicaría por qué el efecto clínico dura semanas tras una sola dosis:
  hipótesis atractiva, no demostrada en humanos.
- **Relación entre experiencia mística y resultado clínico**: hay correlación reportada con MEQ30 (`261`),
  pero correlación no es mecanismo, y el debate sobre si la experiencia subjetiva es necesaria sigue abierto.

Punto de honestidad: **no se sabe si el efecto subjetivo es causa o acompañante del efecto clínico.** Es una
de las preguntas abiertas más importantes del campo, y se están desarrollando análogos no alucinógenos
justamente para responderla.

## Tolerancia y lo que NO hace

| Fenómeno | Qué se sabe |
|---|---|
| Tolerancia aguda | Marcada y rápida; dosis repetidas en días sucesivos producen mucho menos efecto (regulación a la baja de 5-HT2A) |
| Dependencia física | No se ha descrito síndrome de abstinencia fisiológico |
| Potencial de abuso | Bajo en comparación con estimulantes u opioides, según revisiones de farmacodependencia |
| Neurotoxicidad directa | No demostrada a dosis de investigación |
| Riesgo agudo principal | Psicológico (ansiedad intensa, conducta de riesgo) y cardiovascular por aumento de presión y frecuencia |

## Cómo se comprueba (farmacología no es opinión)

| Pregunta | Ensayo |
|---|---|
| ¿Se une al receptor? | Ensayo de unión con radioligando (Ki) sobre receptor recombinante |
| ¿Lo activa y cuánto? | Ensayos funcionales: IP1/calcio (Gq), β-arrestina; da EC50 y eficacia |
| ¿El efecto humano depende de ese receptor? | Estudio con antagonista (ketanserina) en humanos `[clínico]` |
| ¿Qué hace en el cerebro? | fMRI, MEG, PET con radioligandos de 5-HT2A |
| ¿Cuánta ocupación de receptor a qué dosis? | PET de ocupación con dosis escalonadas |
| ¿Hay plasticidad? | Preclínico: imagen de espinas dendríticas, marcadores moleculares |

## Ejemplo aplicado — leer una afirmación con criterio

```
Afirmación de folleto: "La psilocibina reinicia el cerebro y cura la depresión."
Traducción técnica honesta:
  - "Reinicia el cerebro" no es un término farmacológico; describe una metáfora de neuroimagen.
  - El efecto sobre síntomas depresivos se ha evaluado en ensayos clínicos, incluidos dos
    estudios fase 3 con psilocibina sintética (263). "Cura" no es lo que reportan.
  - El mecanismo por el cual un efecto agudo produce cambio sostenido NO está establecido.
Lo que sí se puede afirmar:
  "La psilocina es agonista de 5-HT2A; el bloqueo de ese receptor elimina sus efectos subjetivos
   en humanos [clínico]. Se está investigando su efecto en depresión resistente al tratamiento."
```

Y, para dejarlo escrito: en cualquier producto comercial, escribir que algo "cura", "previene" o "trata"
depresión es un claim de enfermedad, prohibido (`268`, `276`).

## Errores comunes

- **Decir que la psilocibina actúa sobre el receptor.** La que actúa es la psilocina.
- **Presentar la neuroplasticidad como hecho humano.** Es sólido en preclínico, inferido en humanos.
- **Confundir "no genera dependencia física" con "no tiene riesgos".** El riesgo agudo es psicológico y real.
- **Ignorar el 5-HT2B en esquemas de uso repetido.** Es la preocupación teórica más citada (`260`, `264`).
- **Extrapolar de dosis alta supervisada a microdosis.** Farmacológicamente no son la misma situación.
- **Confundir correlación (MEQ30 y desenlace) con mecanismo.**

## Conexión con otros módulos

→ `128-serotonina-y-receptor-5ht2a.md` — el receptor en detalle.
→ `118-receptores-y-transduccion-de-senal.md`, `120-afinidad-eficacia-y-agonismo-parcial.md`.
→ `258-farmacocinetica-de-psilocibina.md` — cómo llega y cuánto dura.
→ `259-dosis-en-investigacion-clinica.md` y `260-screening-de-seguridad-y-contraindicaciones.md`.
→ `261-psicometria-meq30-5d-asc-y-escalas.md` — cómo se mide el efecto subjetivo.
→ `263-estado-clinico-y-regulatorio-2026.md` — el estado del desarrollo clínico.
