# 124 — Citocromo P450 e interacciones (donde un suplemento se vuelve peligroso de verdad)

La mayoría de los suplementos naturales son inocuos por sí solos y peligrosos cuando se combinan con un
medicamento. El punto de choque casi siempre es el mismo: el sistema **citocromo P450**, la familia de
enzimas hepáticas e intestinales que metaboliza la mayor parte de los fármacos. Este módulo te explica cómo
funciona, cuáles son las isoformas que importan, y por qué el CBD y la hierba de San Juan son los dos
ejemplos que todo el mundo debería conocer. El error caro que evita: lanzar un producto sin advertencia de
interacción y que un cliente que toma anticoagulante o inmunosupresor sufra un evento evitable.

Términos: **CYP450 (cytochrome P450)** = familia de enzimas oxidativas de fase I, principalmente en retículo
endoplásmico del hígado y en pared intestinal. **Inhibición (inhibition)** = el suplemento frena la enzima →
sube la concentración del fármaco → más riesgo de toxicidad. **Inducción (induction)** = el suplemento hace
que se produzca más enzima → baja la concentración del fármaco → **fallo terapéutico**. **Sustrato
(substrate)** = el fármaco que la enzima metaboliza. **P-gp (P-glycoprotein)** = bomba de expulsión que
saca compuestos de la célula; se induce y se inhibe igual que los CYP.

## Las isoformas que importan

| Isoforma | Fracción aproximada de fármacos que metaboliza | Sustratos típicos | Notas |
|---|---|---|---|
| CYP3A4 | La mayor de todas (reportado en torno a la mitad de los fármacos de uso clínico) | Estatinas, inmunosupresores (tacrolimus, ciclosporina), muchos antivirales, benzodiacepinas | También está en el intestino: por eso la toronja actúa ahí |
| CYP2D6 | Alta | Antidepresivos, antipsicóticos, tamoxifeno, codeína | Muy polimórfica: hay metabolizadores lentos y ultrarrápidos |
| CYP2C9 | Media | **Warfarina (S-warfarina)**, AINE, fenitoína | Ventana terapéutica estrecha = alto riesgo |
| CYP2C19 | Media | Clopidogrel (profármaco), omeprazol, clobazam | Polimórfica |
| CYP1A2 | Media | Cafeína, teofilina, clozapina | Se induce con humo de tabaco y crucíferas |
| CYP2E1 | Baja | Etanol, paracetamol (vía tóxica) | Relevante en hepatotoxicidad |

## Inhibición vs inducción: la asimetría que hay que entender

```
INHIBICIÓN  →  el fármaco se acumula  →  toxicidad
   Aparece rápido (horas–días). Puede ser reversible o irreversible.

INDUCCIÓN   →  el fármaco se degrada más rápido  →  el tratamiento deja de funcionar
   Tarda días–semanas en instalarse y días–semanas en revertir tras suspender.
```

La inducción es la más traicionera porque el paciente no siente nada: simplemente su anticonceptivo,
su antirretroviral o su inmunosupresor deja de alcanzar concentración eficaz.

## Los dos casos que hay que saber de memoria

### Hierba de San Juan (*Hypericum perforatum*) — inductor potente
Es el ejemplo clásico y mejor documentado de interacción planta-fármaco `[clínico]`. Sus preparados activan
el receptor nuclear **PXR** y con ello inducen **CYP3A4 y P-gp**. El grado de inducción se ha correlacionado
con el contenido de **hiperforina** del preparado, lo que significa que dos productos con el mismo nombre
en la etiqueta pueden comportarse muy distinto según su composición química. Consecuencias reportadas en la
literatura clínica: caída de concentración plasmática de ciclosporina, de antirretrovirales, de
anticonceptivos orales y **reducción del INR en pacientes con warfarina**, con casos que se normalizaron al
suspender la planta.

Lectura de químico: aquí el "producto natural" no es un placebo caro. Es un modulador enzimático real.

### CBD — inhibidor
El CBD inhibe **CYP3A4 y CYP2C19** (y se ha descrito actividad sobre CYP2C9 y UGT), lo que puede aumentar
la concentración de sustratos como clobazam (interacción bien documentada `[clínico]`), warfarina,
tacrolimus y algunos ISRS. La interacción CBD–warfarina está documentada en reportes de caso con elevación
del INR `[clínico, series/casos]`. Es exactamente la dirección opuesta a la hierba de San Juan.

Otros de la lista corta, con distinto peso de evidencia:

| Producto natural | Efecto sobre CYP/transportadores | Nivel de evidencia |
|---|---|---|
| Jugo de toronja | Inhibe CYP3A4 intestinal (irreversible, dura ~24 h o más) | `[clínico]` |
| Piperina (pimienta negra) | Inhibe glucuronidación y P-gp | `[clínico]` |
| Ginkgo, ajo, ginseng | Señales mixtas y a menudo no replicadas | `[in vitro]` / `[clínico]` inconsistente |
| Extractos de hongos funcionales | Datos escasos, mayormente `[in vitro]` | Insuficiente para descartar riesgo |

Ese último renglón es el honesto y el incómodo: **la ausencia de datos de interacción no es evidencia de
ausencia de interacción.** Para hongos funcionales, la literatura de interacción con CYP es pobre. Eso se
declara tal cual, no se maquilla como "sin interacciones conocidas" (ver `250`).

## Cómo se mide

| Pregunta | Método | Unidad | Nivel |
|---|---|---|---|
| ¿Inhibe una isoforma? | Microsomas hepáticos humanos + sustrato sonda + LC-MS/MS | IC50 / Ki (µM) | `[in vitro]` |
| ¿Inhibición dependiente del tiempo? | Preincubación con NADPH, IC50 shift | k_inact, K_I | `[in vitro]` |
| ¿Induce? | Hepatocitos humanos primarios, mRNA + actividad; ensayo de activación de PXR | veces de inducción | `[in vitro]` |
| ¿Importa en la vida real? | Estudio de interacción humano con sustrato sonda (midazolam para 3A4) | cociente de AUC | `[clínico fase 1]` |

La guía de la FDA sobre interacciones medicamentosas (marco vigente a agosto de 2026; verificar la versión
actual antes de citarla en un expediente) clasifica la magnitud clínica por el cociente de AUC: cambios
≥5× se consideran fuertes, 2–5× moderados y 1,25–2× débiles.

## Ejemplo aplicado — advertencia de etiqueta que sí protege

Producto: cápsulas de extracto de reishi. Cliente que escribe: "estoy en tratamiento con warfarina".

Respuesta correcta desde la química, sin claim y sin diagnóstico:

> No tenemos estudios de interacción de este extracto con warfarina, y la literatura publicada sobre
> interacción de hongos funcionales con enzimas hepáticas es limitada. Por eso la recomendación es
> consultar con su médico tratante antes de usarlo, y no iniciar el producto sin esa consulta.

Lo que **no** se hace: decir "es natural, no interactúa". Es falso, no es verificable y traslada un riesgo
real a una persona con ventana terapéutica estrecha.

## Errores comunes

- Escribir "sin interacciones conocidas" cuando lo cierto es "no se ha estudiado". No es lo mismo.
- Asumir que inhibir es el único riesgo. La inducción causa fallo terapéutico silencioso, que puede ser peor.
- Ignorar el CYP3A4 **intestinal**: la toronja actúa ahí y no en el hígado.
- Olvidar el rebote: al suspender un inductor, la concentración del fármaco sube y puede pasarse de rango.
- No advertir en productos con potenciadores de absorción (piperina): potencian todo, incluido el fármaco.
- Suponer que la dosis de suplemento es "muy baja para importar" sin haber calculado la exposición.

## Conexión con otros módulos

→ `125-metabolismo-de-fase-ii.md` — la otra mitad del metabolismo (conjugación).
→ `139-interacciones-planta-farmaco.md` — el catálogo aplicado, planta por planta.
→ `121-farmacocinetica-adme.md` — dónde encaja el metabolismo en el ADME.
→ `206-farmacologia-del-cbd.md` — el detalle farmacológico del CBD.
→ `250-seguridad-e-interacciones-de-hongos.md` — qué se sabe y qué no, en hongos.
