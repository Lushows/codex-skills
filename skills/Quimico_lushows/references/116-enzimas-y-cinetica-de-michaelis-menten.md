# 116 — Enzimas y cinética de Michaelis-Menten (cómo se mide de verdad "inhibe la enzima X")

"Nuestro extracto inhibe la alfa-amilasa" es la clase de frase que suena a ciencia y casi nunca viene con
el número que la hace verificable. Este módulo te da el vocabulario mínimo —Km, Vmax, IC50, Ki— para poder
pedirle a un proveedor o a un laboratorio el dato que convierte una afirmación en una medición. El error
caro que evita: pagar por un ingrediente "inhibidor" cuya IC50 está en concentraciones que jamás se alcanzan
en el intestino ni en la sangre de una persona real.

Términos: **enzima (enzyme)** = proteína que acelera una reacción sin consumirse. **Sustrato (substrate)** =
la molécula sobre la que actúa. **Km (Michaelis constant)** = concentración de sustrato a la que la enzima
va a la mitad de su velocidad máxima; mide afinidad aparente (Km bajo = alta afinidad). **Vmax** = velocidad
máxima cuando la enzima está saturada. **IC50 (half-maximal inhibitory concentration)** = concentración de
inhibidor que reduce la actividad a la mitad **en esas condiciones**. **Ki (inhibition constant)** =
constante de disociación del inhibidor, independiente del sustrato usado.

## La ecuación y qué te está diciendo

```
        Vmax · [S]
v  =  ───────────────
        Km  +  [S]
```

- Cuando `[S] << Km`, la velocidad es casi proporcional al sustrato (cinética de primer orden).
- Cuando `[S] >> Km`, la enzima está saturada y `v ≈ Vmax` (cinética de orden cero).

Esto no es trivia académica: **la eliminación del etanol es de orden cero** en humanos (por eso se elimina a
tasa fija, aprox. 0,10–0,15 g/L por hora, reportado en la literatura) y la de casi todos los fármacos es de
primer orden. Cuál de las dos aplica cambia por completo cómo se acumula una sustancia (ver `126`).

## Los tipos de inhibición (y por qué el tipo cambia el dato que pides)

| Tipo | Qué le pasa a Km aparente | Qué le pasa a Vmax | Cómo se supera |
|---|---|---|---|
| Competitiva | Sube | Igual | Con más sustrato |
| No competitiva | Igual | Baja | No se supera con sustrato |
| Acompetitiva (uncompetitive) | Baja | Baja | No |
| Mixta | Sube o baja | Baja | Parcialmente |
| Irreversible / basada en mecanismo | — | Baja permanentemente | No: hay que sintetizar enzima nueva |

La irreversible importa mucho en interacciones planta-fármaco: una inhibición irreversible de CYP3A4 dura
días, no horas, porque hay que reponer la proteína (ver `124`, `139`).

## IC50 no es una propiedad de la molécula

Este es el punto que más se abusa en los dossiers comerciales. La IC50 depende de:

- la **concentración de sustrato** usada (en inhibición competitiva, más sustrato → IC50 más alta),
- la **concentración de enzima**,
- el **pH**, la temperatura, el buffer, el tiempo de preincubación,
- si el ensayo es colorimétrico y el extracto es **de color** (interferencia clásica en extractos de chaga
  o reishi: el propio color falsea la lectura).

Por eso la relación de Cheng-Prusoff convierte IC50 en Ki para inhibición competitiva:

```
             IC50
Ki  =  ─────────────────
        1  +  ([S] / Km)
```

**Pide Ki, no solo IC50.** Y si te dan IC50, exige `[S]`, Km y las condiciones. Sin eso el número no se
compara entre laboratorios.

## Cómo se mide

| Qué quieres saber | Método | Unidad típica | Nivel de evidencia que da |
|---|---|---|---|
| Actividad enzimática | Ensayo espectrofotométrico continuo (UV-Vis, `90`) | µmol/min/mg (U/mg) | `[in vitro]` |
| Km y Vmax | Curva de v vs [S] con ajuste no lineal (nunca Lineweaver-Burk como método primario) | mM, µmol/min | `[in vitro]` |
| IC50 | Curva dosis-respuesta de 8–10 puntos, ajuste sigmoidal de 4 parámetros | µg/mL o µM | `[in vitro]` |
| Tipo de inhibición | Matriz [S] × [I], ajuste global | — | `[in vitro]` |
| Inhibición de CYP | Microsomas hepáticos humanos + sustrato sonda + LC-MS/MS | µM | `[in vitro]` |
| Interacción real | Estudio de interacción en humanos con AUC | ratio AUC | `[clínico fase 1]` |

Regla de oro: reportar IC50 en **µg/mL de extracto** es casi inútil para comparar, porque no sabes qué
molécula lo está haciendo ni a qué concentración. Reportar en **µM del compuesto puro identificado** sí es
un dato. Si el proveedor solo tiene el primero, tiene un extracto, no un mecanismo.

## Ejemplo aplicado — un extracto de hongo "inhibidor de alfa-glucosidasa"

Dossier recibido **(ILUSTRATIVO)**:

```
Extracto acuoso de Ganoderma lucidum
IC50 alfa-glucosidasa = 180 µg/mL   [in vitro]
Control acarbosa      = 120 µg/mL   [in vitro]
```

Preguntas que se hacen, en este orden:

1. ¿Qué sustrato y a qué concentración? (Sin eso no hay Ki.)
2. ¿Enzima de levadura o intestinal de mamífero? Es la trampa más común: la de levadura da IC50 bonitas y
   no predice nada del intestino humano.
3. ¿Se corrigió por color del extracto? Un extracto pardo a 180 µg/mL absorbe en la región de lectura.
4. ¿Qué concentración de extracto llega al lumen intestinal con la dosis real de 1 g/día? Ese cálculo va a
   `Matematicas_lushows` o a `lab-tools/unidades.py`, no a la cabeza.

Y el cierre no negociable: aunque todo lo anterior salga bien, sigue siendo `[in vitro]`. No se traduce a
lenguaje de glucemia, diabetes ni control de azúcar en una etiqueta. Eso es claim de enfermedad (`268`).

## Errores comunes

- Reportar IC50 sin `[S]`, sin Km y sin condiciones: número no comparable, sirve solo para el folleto.
- Usar enzima de levadura o de bacteria y extrapolar a fisiología humana.
- Ensayos colorimétricos con extractos coloreados sin blanco de matriz: se mide el color, no la inhibición.
- Ajustar Km y Vmax con Lineweaver-Burk (doble recíproco): distorsiona el error de los puntos bajos. Se usa
  para ilustrar, no para cuantificar; el ajuste va no lineal.
- Confundir "inhibe en el tubo" con "inhibe en la persona". Falta exposición (ver `121`, `122`).
- Olvidar el tiempo de preincubación en inhibición basada en mecanismo: sin él se subestima 10× o más.

## Conexión con otros módulos

→ `27-catalisis-y-enzimas.md` — la base fisicoquímica de la catálisis.
→ `26-cinetica-de-reaccion.md` — órdenes de reacción, de donde sale todo esto.
→ `124-citocromo-p450-e-interacciones.md` — las enzimas que deciden las interacciones con fármacos.
→ `120-afinidad-eficacia-y-agonismo-parcial.md` — el análogo para receptores.
→ `91-metodos-colorimetricos-y-enzimaticos.md` — cómo se monta el ensayo en el laboratorio.