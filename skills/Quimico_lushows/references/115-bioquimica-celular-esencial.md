# 115 — Bioquímica celular esencial (dónde ocurre todo lo que un producto puede tocar)

Cuando alguien te dice que su extracto "actúa a nivel celular", está diciendo nada: todo lo que entra al
cuerpo actúa a nivel celular, incluida el agua y la sal. Este módulo te da el mapa mínimo de la célula para
que puedas preguntar lo único que importa: **qué molécula, en qué compartimento, sobre qué blanco, a qué
concentración**. Sin ese mapa no puedes evaluar si un mecanismo propuesto es plausible o es marketing.
El error caro que evita: pagar por un "mecanismo de acción" que ocurre en un compartimento al que la
molécula nunca llega en la vida real por vía oral.

Términos: **membrana plasmática (plasma membrane)** = bicapa de lípidos que separa el interior celular del
exterior y decide qué entra. **Citosol (cytosol)** = el líquido acuoso donde flotan los organelos.
**Organelo (organelle)** = compartimento interno con función propia (mitocondria, retículo, núcleo).
**Homeostasis (homeostasis)** = mantener condiciones internas estables pese a que afuera cambien.
**Blanco molecular (molecular target)** = la proteína concreta (receptor, enzima, transportador) con la que
una molécula interactúa.

## El compartimento manda

La biología no es una sopa: es una casa con cuartos. Una molécula solo puede hacer algo donde llega.

| Compartimento | Qué se hace ahí | Consecuencia práctica |
|---|---|---|
| Membrana plasmática | Receptores de superficie, canales, transportadores | Una molécula grande y polar puede actuar aquí sin entrar |
| Citosol | Glucólisis, síntesis de proteínas, señalización | Requiere atravesar la membrana |
| Mitocondria | Ciclo de Krebs, cadena respiratoria, ATP | Doble membrana: barrera adicional |
| Retículo endoplásmico | Síntesis de lípidos, plegado de proteínas, **CYP450** | Aquí vive el metabolismo de fármacos (ver `124`) |
| Aparato de Golgi | Glicosilación, empaque y envío | Relevante para proteínas terapéuticas |
| Lisosoma | Digestión enzimática, pH ácido (~4,5–5,0) | Muchas moléculas se degradan aquí |
| Núcleo | ADN, transcripción | Blanco de receptores nucleares (PPAR, PXR) |

Regla dura: si un paper dice que un compuesto "inhibe la enzima X" y la enzima X vive en el citosol, tienes
que preguntar si el compuesto entra a la célula. Muchos polisacáridos (β-glucanos, ver `130`) **no entran**
— y por eso su mecanismo propuesto es de superficie, no citosólico.

## La membrana: por qué la polaridad decide el destino

La bicapa lipídica es una capa grasa. Cruzar por difusión pasiva favorece moléculas:

- pequeñas (< ~500 Da),
- suficientemente lipofílicas (logP aproximadamente entre 1 y 3),
- poco cargadas al pH del sitio,
- con pocos donadores/aceptores de puente de hidrógeno.

Esa es la base de la "regla de los 5" de Lipinski, que es una regla de dedo para orientarse, no una ley.
Un β-glucano de 200 kDa no cruza. Un cannabinoide (~314 Da, muy lipofílico) cruza demasiado bien y por eso
se acumula en grasa (ver `121`). La psilocina (~204 Da) cruza; la psilocibina (fosforilada, más polar) es
un profármaco que debe desfosforilarse primero (ver `258`).

Ver `17-polaridad-y-fuerzas-intermoleculares.md` y `30-extraccion-liquido-liquido-y-logp.md` para la parte
fisicoquímica.

## Las cuatro familias de macromoléculas

```
Proteínas      ← aminoácidos      → enzimas, receptores, transportadores, anticuerpos
Ácidos nucleicos ← nucleótidos    → ADN (archivo), ARN (copia de trabajo)
Carbohidratos  ← monosacáridos    → energía (glucógeno, almidón) y estructura (celulosa, quitina, β-glucano)
Lípidos        ← ácidos grasos    → membranas, reserva de energía, señalización (endocannabinoides)
```

Para hongos: la pared celular fúngica es **quitina + β-glucanos**, no celulosa. Eso explica por qué un
extracto acuoso de hongo trae glucanos y por qué el análisis de "polisacáridos totales" se contamina con
almidón del grano de cultivo (ver `220`, `222`).

## Señal, no combustible

Hay dos formas de que una molécula haga algo en el cuerpo:

1. **Como sustrato/combustible** — se metaboliza y aporta materia o energía (glucosa, aminoácidos).
2. **Como señal** — se une a un blanco y cambia el comportamiento de la célula sin consumirse en masa
   apreciable (hormonas, cannabinoides, la mayoría de los "activos" de suplementos).

Casi todo lo que se vende como suplemento funcional pretende ser señal. Las señales tienen dos exigencias
brutales: **llegar** (farmacocinética, `121`) y **encajar** (afinidad, `120`). Si un ingrediente no puede
demostrar ninguna de las dos, el mecanismo es una historia.

## Cómo se comprueba

No se "comprueba la bioquímica celular" en un COA. Lo que se comprueba es cada eslabón, y cada uno tiene
su técnica y su nivel de evidencia:

| Pregunta | Cómo se responde | Nivel que da |
|---|---|---|
| ¿La molécula entra a la célula? | Ensayo de permeabilidad Caco-2 o PAMPA | `[in vitro]` |
| ¿Se une al blanco? | Ensayo de unión con radioligando o SPR | `[in vitro]` |
| ¿Cambia algo en la célula? | Reportero, western blot, qPCR, citometría | `[in vitro]` |
| ¿Llega a sangre en un animal? | PK en roedor, LC-MS/MS en plasma | `[animal]` |
| ¿Llega a sangre en humanos? | Estudio de biodisponibilidad | `[clínico fase 1]` |
| ¿Hace algo medible en personas? | ECA con desenlace preespecificado | `[clínico fase 2/3]` |

Un mecanismo `[in vitro]` **no** es una afirmación de efecto en personas. Nunca lo presentes así (ver `12`).

## Ejemplo aplicado — BIO-SETA

Un proveedor manda un dossier de su extracto de melena de león que dice: "estimula la síntesis de NGF a
nivel celular". Lo que hay detrás, cuando lo pides:

- Ensayo en células PC12 de rata, hericenona C a 10 µg/mL **(ILUSTRATIVO)**, incremento de NGF ~2× frente
  a control → `[in vitro]`.
- Ninguna medida de concentración plasmática humana de hericenona tras dosis oral.

Traducción honesta: hay un mecanismo propuesto `[in vitro]` con un compuesto lipofílico que, además, casi
nunca se cuantifica en el producto terminado (ver `226`). Sin dato de exposición humana no hay puente entre
el ensayo y la persona. Lo que se puede escribir en la etiqueta es otra conversación completamente distinta
y va por `267` y `268` — y nunca incluye mencionar una enfermedad.

## Errores comunes

- Decir "actúa a nivel celular" como si fuera un mecanismo. Es una frase vacía y en auditoría se cae sola.
- Tomar una concentración de ensayo `[in vitro]` (µM en el pozo) como si fuera alcanzable en plasma humano.
  Casi siempre es 10–1.000 veces mayor de lo que la vía oral logra.
- Asumir que una molécula grande y polar entra a la célula porque el paper dice "actividad intracelular".
- Confundir "aumenta la expresión de un gen en cultivo" con "hace algo en una persona".
- Ignorar el compartimento: proponer inhibición de una enzima del retículo con una molécula que no cruza.
- Traducir cualquier hallazgo celular a lenguaje de enfermedad. Eso es claim prohibido, no ciencia (`268`).

## Conexión con otros módulos

→ `116-enzimas-y-cinetica-de-michaelis-menten.md` — cómo se cuantifica lo que hace una enzima.
→ `118-receptores-y-transduccion-de-senal.md` — el blanco de superficie y qué pasa después.
→ `121-farmacocinetica-adme.md` — si no llega, el mecanismo no importa.
→ `12-niveles-de-evidencia.md` — la regla de oro para no sobrevender un ensayo celular.
→ `52-polisacaridos-y-glucanos.md` — la química de la pared fúngica.
