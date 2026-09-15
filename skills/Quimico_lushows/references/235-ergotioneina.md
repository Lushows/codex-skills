# 235 — Ergotioneína: el marcador que sí distingue a un hongo, y lo que la evidencia realmente dice

La ergotioneína es el compuesto más interesante que tiene un hongo desde el punto de vista de diferenciación:
prácticamente **solo la fabrican hongos y algunas bacterias**, el cuerpo humano tiene un transportador
dedicado para absorberla y retenerla, y se mide con un método limpio y barato en comparación con los
polisacáridos. Para quien vende hongos, es una forma honesta de tener un número que la competencia no puede
inventar. Para quien audita, es un marcador de autenticidad difícil de falsificar con almidón.

Términos: **ergotioneína (ergothioneine, EGT)** = betaína derivada de la 2-tiol-L-histidina; en español se
escribe con "í" acentuada por costumbre editorial, aquí se usa "ergotioneína". **tautómero tiona/tiol
(thione/thiol tautomer)** = las dos formas en que puede existir el azufre de la molécula. **OCTN1 (SLC22A4)**
= transportador de cationes orgánicos que la introduce a las células. **novel food (nuevo alimento)** =
categoría regulatoria europea para ingredientes sin historia de consumo significativo antes de 1997.

## Química: por qué esta molécula es rara

La ergotioneína es un derivado del aminoácido histidina con un grupo azufrado en el anillo imidazol y el
nitrógeno trimetilado (betaína). Su particularidad es que **a pH fisiológico predomina el tautómero tiona,
no el tiol**. Consecuencia práctica enorme:

- Los tioles comunes (cisteína, glutatión) se autooxidan en solución acuosa con oxígeno y metales; por eso
  son inestables en un producto.
- La ergotioneína, al estar mayoritariamente en forma tiona, **no se autooxida en esas condiciones**. Es
  estable en agua, tolera calor moderado y sobrevive procesos de cocción y secado mucho mejor que el
  glutatión.

Esa estabilidad es la razón por la que un extracto acuoso de hongo conserva ergotioneína medible, y por la
que sirve como marcador de proceso.

| Propiedad | Comportamiento |
|---|---|
| Solubilidad | Alta en agua; sale en extracción acuosa (`241`) |
| Estabilidad térmica | Buena a temperaturas de cocción y secado moderado |
| Autooxidación | Muy baja frente a otros tioles, por el tautómero tiona |
| Absorción en humano | Vía transportador **OCTN1 (SLC22A4)**, presente en varios tejidos |
| Biosíntesis | Hongos, actinobacterias y cianobacterias. **Las plantas y los animales no la sintetizan**; la toman de la dieta o del suelo |

## Cuánta hay: rangos reportados por especie

| Material | Contenido reportado | Base | Fuente |
|---|---|---|---|
| Hongos en general | **0,4–2,0 mg/g** | base seca | Literatura de cuantificación por LC-MS en hongos cultivados (Dubost et al., *International Journal of Medicinal Mushrooms*, 2006, 8(3); y *Food Chemistry*, 2007) |
| *Pleurotus ostreatus* (orellana) | hasta **2,22 mg/g** — el valor más alto del estudio | base seca | Estudio de procesamiento térmico y ergotioneína |
| *Lentinula edodes* (shiitake) | **0,2–0,8 mg/g** (200–800 mg/kg) | base seca | Literatura de composición de *L. edodes* |
| *L. edodes* con manipulación de luz de cultivo | de 1,2 mg/g (control) a ≈2,8 mg/g bajo luz azul | base seca | Estudio de modulación por luz; verificar la fuente primaria antes de usarlo como especificación |
| *Agaricus bisporus* | en el extremo bajo del rango general | base seca | Ídem literatura general |

Dos advertencias antes de que uses cualquiera de estos números:

1. **Son rangos de literatura, no tu lote.** Cepa, sustrato, edad del cuerpo fructífero y secado los mueven
   con facilidad (`239`, `240`).
2. **Un extracto no tiene el mismo valor que la materia prima.** Si concentras 10:1 y la ergotioneína se
   recupera bien en agua, sube; si haces un extracto alcohólico, baja. Mide el material que vas a vender.

## Cómo se mide / cómo se comprueba

| Paso | Detalle |
|---|---|
| Extracción | Acuosa o hidrometanólica, con agitación; es hidrosoluble y estable, así que la extracción no es el cuello de botella |
| Separación | HPLC en fase reversa **con par iónico** (la molécula es zwitteriónica y no retiene bien en C18 solo), o columna HILIC |
| Detección de rutina | UV a ~254 nm |
| Detección de referencia | **LC-MS/MS** en MRM, con patrón de ergotioneína y, si es posible, estándar interno isotópico |
| Unidad y base | `mg/g base seca` o `mg/kg base seca`; declarar siempre humedad del material (`07`, `98`) |
| Confirmación de identidad | Relación de transiciones MRM y tiempo de retención vs patrón |

Notas de método: hay trabajos que documentan las dificultades reales de cuantificar ergotioneína (y
lovastatina) en distintas matrices de hongo y comparan enfoques analíticos —*On the Identification and
Quantification of Ergothioneine and Lovastatin in Various Mushroom Species: Assets and Challenges of
Different Analytical Approaches* (PMC8036957, 2021)—. La conclusión práctica: **LC-MS es el método de
elección** por resolución y tiempo de análisis; el HPLC-UV sirve para control de rutina si está validado
contra el LC-MS (`75`).

## Regulación, a agosto de 2026

| Marco | Situación |
|---|---|
| Unión Europea | La **l-ergotioneína sintética está autorizada como novel food**. EFSA evaluó la seguridad; NOAEL reportado de **800 mg/kg de peso corporal/día** en el estudio pivotal, y la dosis suplementaria evaluada para adultos es de **30 mg/día**. Hay una declaración adicional de EFSA sobre exposición en lactantes, niños pequeños y mujeres embarazadas o lactantes (PMC7010164) |
| Estados Unidos | Depende de la vía: ingrediente en la lista de sustancias reconocidas o notificación NDI según el caso (`275`) |
| Colombia | No hay una autorización específica de ergotioneína aislada; en un suplemento se maneja dentro del expediente de registro sanitario y del rotulado (`266`, `269`, `272`). **Verificar con INVIMA antes de declararla como ingrediente aislado** |

Importante: **los 30 mg/día de EFSA son un límite de seguridad, no una dosis eficaz**. Confundir esos dos
conceptos es el error de comunicación más frecuente con este ingrediente.

## Qué dice la evidencia (con su nivel)

- **Seguridad.** La suplementación en los estudios disponibles no alteró marcadores clínicos de seguridad
  `[clínico]`. El NOAEL de 800 mg/kg pc/día deja un margen amplio frente a 30 mg/día.
- **Ensayos en humanos.** En 2025 se publicó en *Nutraceuticals* el primer estudio aleatorizado, doble ciego,
  controlado con placebo y con rango de dosis en adultos mayores sanos, evaluando función cognitiva, calidad
  del sueño y biomarcadores fisiológicos `[clínico, piloto, muestra pequeña]`. Existe también un protocolo
  publicado de estudio piloto aleatorizado en personas con síndrome metabólico (ErgMS, PMC8555363), y un
  ensayo de 20 mg/día por 4 semanas en personas con ansiedad alta y quejas de sueño `[clínico piloto]`.
- **Mecanismo.** Capacidad antioxidante y acumulación tisular vía OCTN1 están bien descritas `[in vitro]` y
  `[animal]`.
- **Epidemiología.** Hay estudios observacionales que exploran asociaciones entre niveles plasmáticos de
  ergotioneína y desenlaces de salud. **Asociación no es causalidad**, y ninguno de esos trabajos autoriza
  un claim.

En 2025 hubo además debate público sobre el desfase entre la evidencia disponible y el marketing de
longevidad de la ergotioneína en el mercado chino (cobertura de prensa especializada, nutraingredients.com,
junio de 2025). Ese debate es exactamente la advertencia de este módulo.

## Ejemplo aplicado — usar ergotioneína como marcador de autenticidad (ILUSTRATIVO)

```
Dos ofertas de "extracto de shiitake 10:1":

Proveedor A: beta-glucano 30 % b.s., alfa-glucano 4 %, ergotioneina 0,9 mg/g b.s.
Proveedor B: "polisacaridos 30 %", sin alfa-glucano, ergotioneina no detectada (LOQ 0,05 mg/g)

Lectura:
  A tiene biomasa fungica real y un marcador secundario coherente con L. edodes.
  B no reporta alfa-glucano (probable almidon, 220) y la ergotioneina ND es una
  segunda bandera: un hongo de verdad, aunque sea poco, deberia dar algo.

Aporte por porcion en A (capsula de 500 mg, 2/dia):
  0,9 mg/g x 1,0 g/dia = 0,9 mg de ergotioneina/dia
  -> muy por debajo de los 30 mg/dia evaluados por EFSA. Se declara el dato,
     no se insinua un efecto.
```

## Errores comunes

- **Presentar los 30 mg/día de EFSA como dosis eficaz.** Es un límite de seguridad evaluado.
- **Declarar ergotioneína sin medirla**, asumiendo el promedio de la especie.
- **Medir en base húmeda y compararla con literatura en base seca** (`07`).
- **Usar C18 sin par iónico** y reportar un pico que en realidad coeluye con otra cosa.
- **Extraer con alcohol puro** y perder buena parte del contenido: es hidrosoluble (`241`).
- **Vender "antioxidante celular maestro"** o frases de longevidad. Eso no es un claim aprobado en ningún
  marco y en Colombia es riesgo sanitario (`267`, `276`).

## Conexión con otros módulos

→ `133-estres-oxidativo-y-antioxidantes.md` — qué significa de verdad "antioxidante" y qué no.
→ `238-ergosterol-como-marcador.md` — el otro marcador de autenticidad fúngica.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — con qué solvente se recupera.
→ `83-lc-ms-ms-y-mrm.md` — la técnica de referencia para cuantificarla.
→ `278-novel-food-hongos-y-cannabis.md` — el estatus europeo en detalle.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se cuenta esto sin caer en longevidad de fantasía.
