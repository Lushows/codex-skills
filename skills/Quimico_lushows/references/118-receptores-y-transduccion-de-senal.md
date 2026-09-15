# 118 — Receptores y transducción de señal (qué significa realmente "se une a un receptor")

Todo mecanismo de acción serio termina en la misma frase: esta molécula se une a este blanco y eso
desencadena esta cascada. Este módulo te da las familias de receptores y cómo se traduce la unión en un
efecto celular, para que puedas leer un paper de farmacología sin creerte todo y para que sepas exactamente
qué preguntar cuando alguien afirma que su ingrediente "activa un receptor". El error caro que evita:
aceptar un mecanismo receptor-dependiente sin exigir la afinidad y sin comparar esa afinidad con la
concentración plasmática real que la dosis del producto alcanza.

Términos: **receptor (receptor)** = proteína que reconoce una molécula señal y traduce esa unión en un
cambio celular. **Ligando (ligand)** = la molécula que se une. **Transducción de señal (signal
transduction)** = la cadena de eventos entre la unión y el efecto. **Segundo mensajero (second messenger)**
= molécula intracelular que amplifica la señal (AMPc, Ca2+, IP3, DAG). **Constante de disociación Kd** =
concentración de ligando a la que se ocupa la mitad de los receptores; menor Kd = mayor afinidad.

## Las cinco familias que necesitas conocer

| Familia | Ejemplos relevantes | Velocidad de respuesta | Cómo transducen |
|---|---|---|---|
| GPCR (G protein-coupled receptor) | CB1, CB2, 5-HT2A, receptores opioides | segundos | Proteína G → AMPc, Ca2+, β-arrestina |
| Canales iónicos (ligand-gated ion channels) | nicotínico, GABA-A, 5-HT3 | milisegundos | Abren un poro, entra o sale ion |
| Receptores con actividad enzimática | insulina, TrkA (el receptor de NGF) | minutos | Autofosforilación en tirosina → cascada |
| Receptores nucleares | PPARα/γ, PXR, receptor de vitamina D | horas | Se unen al ADN y cambian transcripción |
| Receptores inmunes de reconocimiento de patrones | Dectin-1, TLR2/6, CR3 | minutos–horas | Reclutan quinasas (Syk), activan NF-κB |

Los GPCR son la familia más importante en farmacología: se estima que alrededor de un tercio de los
medicamentos aprobados actúa sobre ellos (dato de literatura, verificar la cifra vigente antes de citarla).
Aquí caen el sistema endocannabinoide (`129`) y el 5-HT2A de la psilocina (`128`).

Dectin-1 y CR3 son la puerta de entrada del mecanismo propuesto de β-glucanos y por eso se tratan aparte
en `130`, con su nivel de evidencia real.

## De la unión al efecto: la cascada

```
Ligando + Receptor  ⇌  Complejo LR      (gobernado por Kd)
        │
        ▼  cambio conformacional
Transductor (proteína G, quinasa, canal)
        │
        ▼  amplificación
Segundos mensajeros (AMPc ↑/↓, Ca2+ ↑, IP3/DAG)
        │
        ▼
Efectores (PKA, PKC, CaMK) → fosforilan proteínas
        │
        ▼
Efecto celular (secreción, contracción, transcripción, proliferación)
```

Dos consecuencias prácticas de la amplificación:

1. **Ocupar poco receptor puede bastar.** Por la reserva de receptores (spare receptors), un agonista puede
   dar efecto máximo ocupando una fracción pequeña. Por eso EC50 ≠ Kd (ver `120`).
2. **La señal se apaga sola.** Desensibilización, internalización y regulación a la baja (downregulation)
   explican por qué el uso repetido reduce el efecto — la tolerancia al THC vía CB1 es el ejemplo clásico
   `[clínico]` (ver `205`).

## Sesgo de señalización, en cristiano

Un mismo receptor puede activar dos rutas distintas (por ejemplo proteína G vs β-arrestina), y un ligando
puede preferir una. Eso se llama **agonismo sesgado (biased agonism)**. Importa porque explica cómo dos
moléculas que se unen al mismo receptor producen perfiles de efecto distintos. No es magia: se mide con
ensayos separados por ruta y se reporta como factor de sesgo.

## Cómo se mide

| Pregunta | Método | Unidad | Nivel |
|---|---|---|---|
| ¿Se une? ¿Con qué afinidad? | Radioligando de competencia, SPR, TR-FRET | Ki o Kd en nM | `[in vitro]` |
| ¿Activa o bloquea? | Ensayo funcional: AMPc, movilización de Ca2+, reclutamiento de β-arrestina | EC50 / IC50, %Emáx | `[in vitro]` |
| ¿Qué tan selectivo es? | Panel de receptores (screening de 40–80 dianas) | ratio de Ki | `[in vitro]` |
| ¿Ocupa el receptor en un cerebro vivo? | PET con radiotrazador | % de ocupación | `[clínico fase 1]` |
| ¿Produce el efecto esperado? | ECA con desenlace preespecificado | según desenlace | `[clínico fase 2/3]` |

**La pregunta que casi nadie hace:** ¿la Ki reportada (digamos 50 nM) es alcanzable con la dosis oral del
producto? Si la Cmax plasmática es 5 nM y encima el 99 % va unido a proteínas, la fracción libre no llega.
Ese cruce entre `120` (afinidad) y `121` (exposición) es lo que separa farmacología de folleto.

## Ejemplo aplicado — leer un dossier de melena de león

El proveedor afirma "activa la vía del NGF". La cadena que hay que verificar, eslabón por eslabón:

1. NGF actúa sobre **TrkA**, un receptor tirosina-quinasa. ¿El extracto se une a TrkA? Normalmente no: lo
   que se propone es que induce la *síntesis* de NGF en astrocitos, no que active TrkA.
2. ¿A qué concentración? En los ensayos citados, del orden de 1–50 µg/mL de extracto en el pozo
   **(ILUSTRATIVO)** → `[in vitro]`.
3. ¿Qué concentración plasmática alcanza una hericenona tras 1 g oral? Prácticamente no hay dato publicado
   de farmacocinética humana de hericenonas ni erinacinas. Ese hueco es el que decide la conversación.
4. Conclusión honesta para el expediente: mecanismo propuesto `[in vitro]` + algunos ensayos clínicos
   pequeños con desenlaces cognitivos autorreportados `[clínico fase 2]`, heterogéneos, con material poco
   caracterizado. Se comunica como tal, sin nombrar ninguna enfermedad (ver `225`, `226`, `248`, `268`).

## Errores comunes

- Confundir "se une" con "activa": un antagonista se une con altísima afinidad y no hace nada por sí solo.
- Tomar EC50 de un ensayo celular como si fuera la dosis humana. Son universos distintos.
- Olvidar la unión a proteínas plasmáticas: solo la fracción libre puede llegar al receptor.
- Ignorar la desensibilización: efectos que existen en dosis única desaparecen con uso crónico.
- Citar afinidad por un receptor sin panel de selectividad. Sin panel no sabes qué más está tocando.
- Traducir la activación de un receptor a un beneficio de salud concreto. Ese salto necesita clínica.

## Conexión con otros módulos

→ `120-afinidad-eficacia-y-agonismo-parcial.md` — Kd, EC50, Emáx y agonismo parcial, en detalle.
→ `128-serotonina-y-receptor-5ht2a.md` — el GPCR de la psilocina.
→ `129-sistema-endocannabinoide.md` — CB1, CB2 y lo que no está demostrado.
→ `130-inmunomodulacion-y-beta-glucanos.md` — Dectin-1 y CR3 con evidencia honesta.
→ `119-farmacodinamia-y-dosis-respuesta.md` — la curva que resume todo esto.