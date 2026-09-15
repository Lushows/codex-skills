# 133 — Estrés oxidativo y antioxidantes (por qué ORAC no se usa y por qué "antioxidante" no es un beneficio)

Durante veinte años "antioxidante" fue el argumento de venta universal, y en ese mismo periodo la ciencia se
movió en dirección contraria: los ensayos grandes de suplementación con antioxidantes no confirmaron los
beneficios esperados, y algunos mostraron señales de daño. Este módulo te explica la bioquímica real de las
especies reactivas de oxígeno, por qué los ensayos en tubo (ORAC, DPPH, FRAP) no predicen nada en una
persona, y qué se puede medir de verdad. El error caro que evita: pagar por un valor ORAC que no significa
nada y usarlo como argumento central.

Términos: **ROS (reactive oxygen species)** = especies reactivas de oxígeno: superóxido, peróxido de
hidrógeno, radical hidroxilo. **Estrés oxidativo (oxidative stress)** = desequilibrio entre producción de
ROS y capacidad de manejarlos, con daño a lípidos, proteínas y ADN. **Antioxidante (antioxidant)** =
sustancia que retrasa o previene la oxidación de un sustrato. **ORAC (oxygen radical absorbance capacity)**
= ensayo químico de capacidad de captación de radicales en tubo. **Hormesis (hormesis)** = respuesta
adaptativa favorable a un estrés leve.

## La bioquímica real

Las ROS no son un accidente: son producto normal del metabolismo (fuga de electrones en la cadena
respiratoria mitocondrial) **y señales fisiológicas legítimas**. El peróxido de hidrógeno actúa como
segundo mensajero; el estallido respiratorio de los neutrófilos es un mecanismo de defensa que usa ROS a
propósito.

El cuerpo tiene su propio sistema, que es enzimático y muy potente:

| Defensa | Qué hace | Nota |
|---|---|---|
| Superóxido dismutasa (SOD) | Superóxido → H2O2 | Requiere Cu/Zn o Mn |
| Catalasa | H2O2 → H2O + O2 | Extremadamente rápida |
| Glutatión peroxidasa | H2O2 y peróxidos lipídicos → agua | Requiere selenio |
| Glutatión (GSH) | Reductor intracelular principal | mM en el citosol; se recicla |
| Tiorredoxina / peroxirredoxinas | Control redox de proteínas | Sistema principal de señalización redox |
| Vía Nrf2 | Sensor que **induce** todas las anteriores | Ver abajo |

**Nrf2 cambia la conversación.** Muchos fitoquímicos "antioxidantes" no actúan captando radicales en el
cuerpo (sus concentraciones plasmáticas son demasiado bajas para eso, ver `125`), sino activando la vía
Nrf2, que sube la producción de las enzimas antioxidantes propias `[in vitro]` / `[animal]`. Es decir, el
mecanismo plausible es **hormético e indirecto**: un estrés leve que induce defensa, no una esponja de
radicales. Esta distinción es la más importante del módulo.

## Por qué ORAC, DPPH y FRAP no sirven como argumento

Estos ensayos miden la reacción de un extracto con un radical artificial en un tubo, en condiciones que no
existen en el cuerpo. Sus problemas:

1. **No hay relación demostrada con efecto in vivo.** El USDA retiró su base de datos de valores ORAC de
   alimentos en 2012 precisamente porque los valores se estaban usando de forma engañosa y **no hay
   evidencia de que se traduzcan en beneficio en humanos**. Ese retiro es un hecho histórico y sigue siendo
   la referencia a citar.
2. **Ignoran la biodisponibilidad.** Un extracto con ORAC altísimo cuyos fenoles se conjugan en fase II no
   deja nada en circulación (`125`).
3. **Responden a interferentes.** Azúcares reductores, ácido ascórbico, proteínas y hasta el color del
   extracto alteran la lectura.
4. **No distinguen mecanismo.** Captar un radical en tubo no es lo mismo que modular una vía redox.
5. **Son manipulables.** Cambiar solvente de extracción o base de cálculo multiplica el número. Se ven
   valores incomparables entre laboratorios para el mismo material.

En Europa, además, las alegaciones genéricas de "antioxidante" sin especificar el mecanismo y el nutriente
no están autorizadas; solo hay claims autorizados para nutrientes concretos con función definida
(por ejemplo, contribución a la protección de las células frente al daño oxidativo para ciertos minerales y
vitaminas) — verificar la lista vigente de EFSA a la fecha antes de usar cualquiera (`277`).

## Lo que la evidencia clínica grande mostró

Este es el párrafo que hay que decir aunque incomode:

- Ensayos de gran tamaño con **beta-caroteno** en fumadores mostraron aumento de incidencia de cáncer de
  pulmón en el grupo suplementado `[clínico fase 3]`. Es el caso histórico más citado de que "antioxidante"
  no equivale a "seguro".
- Ensayos con **vitamina E** y con **vitamina E + selenio** no confirmaron los beneficios esperados y
  algunos reportaron señales adversas `[clínico fase 3]`.
- Se ha propuesto que la suplementación antioxidante de alta dosis puede **atenuar adaptaciones al
  ejercicio**, porque las ROS son parte de la señal de adaptación `[clínico fase 2]`, con literatura mixta.

Conclusión honesta: más capacidad antioxidante no es automáticamente mejor. El sistema redox es de
equilibrio, no de acumulación.

## Cómo se mide (lo que sí tiene sentido)

| Nivel | Qué se mide | Método | Utilidad real |
|---|---|---|---|
| Producto | Capacidad en tubo (ORAC/DPPH/FRAP) | Espectrofotometría | **Solo control de proceso**: comparar lotes propios entre sí |
| Producto | Contenido de compuestos específicos | HPLC-DAD / LC-MS/MS | Sí: identidad y dosis |
| Producto | Ergotioneína (relevante en hongos) | LC-MS/MS | Sí, marcador propio (`235`) |
| Persona | Daño lipídico: F2-isoprostanos en orina | LC-MS/MS | El biomarcador más aceptado |
| Persona | Daño a ADN: 8-OHdG | LC-MS/MS o ELISA (menos fiable) | Aceptable con buen método |
| Persona | Estado redox: GSH/GSSG | HPLC con detección electroquímica | Muy sensible a preanalítica |
| Persona | Capacidad antioxidante total del plasma (TAC) | Varios | Poco informativo: domina el ácido úrico |

Ese último renglón es una trampa clásica: la "capacidad antioxidante total del plasma" sube mucho con el
ácido úrico, así que un aumento puede reflejar cualquier cosa menos el efecto del producto.

## Ejemplo aplicado — un COA de chaga con ORAC

COA recibido **(ILUSTRATIVO)**: "ORAC 146.000 µmol TE/100 g. El antioxidante más potente de la naturaleza."

Cómo se audita:

1. ¿Sobre qué material y qué base? Si es sobre extracto seco y se compara contra fruta fresca, la
   comparación está viciada por el agua (`07`).
2. ¿Qué método exacto y qué laboratorio? ORAC tiene variantes (hidrofílico, lipofílico) que dan números
   distintos.
3. ¿El extracto es intensamente coloreado? El chaga lo es; hay interferencia real.
4. ¿Qué significa para una persona? Nada demostrable. El USDA retiró su base de datos justamente por esto.
5. Qué hacer: usar el ORAC solo internamente como control de consistencia entre lotes, y comunicar hacia
   afuera lo medible: contenido de β-glucano (`221`), ergotioneína, identidad por ITS y —muy importante en
   chaga— **oxalato y radiocesio**, que son los riesgos reales de esa especie (`230`).

## Errores comunes

- Usar ORAC como argumento de venta. Es indefendible y ya hay precedente regulatorio en contra.
- Comparar ORAC de un extracto seco contra un alimento fresco. Base distinta, comparación falsa.
- Decir "antioxidante" como si fuera un beneficio de salud. No lo es sin desenlace ni mecanismo.
- Asumir que más antioxidante es mejor. Los ensayos grandes dicen que no siempre.
- Ignorar que el mecanismo plausible de muchos fitoquímicos es Nrf2 (hormesis), no captación directa.
- Medir TAC del plasma y atribuir el cambio al producto cuando lo mueve el ácido úrico.

## Conexión con otros módulos

→ `24-oxido-reduccion.md` — la química redox de base.
→ `125-metabolismo-de-fase-ii.md` — por qué los polifenoles no llegan libres.
→ `235-ergotioneina.md` — el compuesto de hongos con mejor caso como protector celular.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — los riesgos reales del chaga.
→ `277-efsa-y-health-claims.md` — qué claims antioxidantes están autorizados y cuáles no.