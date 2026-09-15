# 238 — Ergosterol como marcador: la prueba de que ahí adentro sí hay hongo

Si solo pudieras pedir dos análisis para auditar un producto de hongos, serían β-glucano/α-glucano por
Megazyme (`221`) y **ergosterol**. La razón es simple: el ergosterol es el esterol de membrana de los hongos
y **prácticamente no existe en plantas ni en cereales**. Un polvo con mucho almidón y poco ergosterol es
grano disfrazado. Un extracto que dice ser de hongo y da ergosterol por debajo del límite de cuantificación
tiene que explicar por qué. Es el análisis más barato con mejor relación señal/ruido de todo el bloque.

Términos: **ergosterol (ergosterol)** = 3β-hidroxi-esteroide con tres dobles enlaces (5,7,22), el esterol
dominante de la membrana fúngica. **biomarcador (biomarker)** = compuesto cuya presencia indica de forma
razonablemente específica el origen del material. **saponificación (saponification)** = hidrólisis alcalina
que rompe los ésteres de esterol para medir el esterol total. **LOQ (limit of quantification)** = límite de
cuantificación del método.

## Por qué funciona como marcador

| Organismo | Esterol dominante de membrana |
|---|---|
| **Hongos** | **Ergosterol** |
| Plantas y cereales | Sitosterol, campesterol, estigmasterol |
| Animales | Colesterol |

Esa separación limpia es lo que hace útil al ergosterol. Se usa desde hace décadas en dos oficios distintos:

1. **Micología ambiental y control de granos**: estimar biomasa fúngica en un sustrato colonizado o detectar
   crecimiento de mohos en cereales y alimentos balanceados. Se combina con micotoxinas (`101`).
2. **Auditoría de suplementos de hongos**: confirmar que la etiqueta corresponde a material fúngico real y no
   a un vehículo de almidón (`218`).

Además, el ergosterol es el precursor de la vitamina D2 bajo UV (`236`), así que el mismo número te sirve
para dos decisiones distintas.

## Rangos reportados en la literatura

| Especie | Ergosterol reportado | Base |
|---|---|---|
| *Agaricus bisporus* | 6,4–6,8 mg/g | base seca |
| *Hygrophorus marzuolus* | 6,4–6,8 mg/g | base seca |
| *Pleurotus ostreatus* | 3,3–4,0 mg/g | base seca |
| *Calocybe gambosa* | 3,3–4,0 mg/g | base seca |
| *Lentinula edodes* | 3,3–4,0 mg/g | base seca |
| *Boletus edulis* | 3,3–4,0 mg/g | base seca |
| *Cantharellus cibarius* | 0,2–0,4 mg/g | base seca |
| *Lactarius deliciosus* | 0,2–0,4 mg/g | base seca |
| *Craterellus cornucopioides* | 0,2–0,4 mg/g | base seca |

Fuente: recopilación de composición en *Ergosterol as a Measure of Fungal Biomass* (Springer, 2020) y la
literatura primaria citada allí. Rango de trabajo razonable para cuerpo fructífero de hongo comestible:
**del orden de 0,2 a 8 mg/g base seca**, con enorme variación entre especies.

Ese rango tan ancho es la limitación principal del marcador: **el ergosterol no da un umbral universal**.
Lo que sí da es una comparación dentro de la misma especie y del mismo material, y una señal binaria muy
clara cuando el valor está en el suelo.

## Cómo se mide / cómo se comprueba

| Paso | Detalle |
|---|---|
| Extracción | Metanol, o metanol/KOH con **saponificación** en caliente para liberar el ergosterol esterificado |
| Partición | Extracción con n-hexano o pentano tras saponificar |
| Separación y detección | **HPLC en fase reversa con detección UV a 282 nm** (el ergosterol tiene un cromóforo de trieno conjugado muy característico) |
| Confirmación | Espectro completo con DAD (máximos a ~262, 271, 282 y 293 nm) o LC-MS |
| Patrón | Ergosterol de referencia con certificado (`70`) |
| Unidad y base | `mg/g base seca` o `µg/g base seca`; declarar la humedad (`07`, `98`) |
| Alternativas | Pirólisis flash con GC-MS; autofluorescencia del ergosterol para métodos rápidos; ATR-FTIR con quimiometría para estimaciones conjuntas de glucanos y ergosterol (PMC7230552) |

La firma UV de cuatro máximos es una ventaja poco aprovechada: con DAD puedes confirmar identidad de pico sin
espectrómetro de masas, cosa que con la mayoría de analitos de este bloque no puedes hacer (`80`).

**Cuidado con la degradación:** el ergosterol es un trieno conjugado, sensible a luz y oxígeno. Extractos
expuestos a luz pierden ergosterol y ganan fotoproductos, incluida la propia vitamina D2. Trabaja con vidrio
ámbar y analiza rápido (`61`).

## Ejemplo aplicado — el ergosterol como detector de grano (ILUSTRATIVO)

```
Producto auditado: "Reishi extract powder", 500 g, precio sospechosamente bajo

COA del proveedor:  "Polysaccharides 30 %"   (222: no dice nada)

Analisis propio:
  beta-glucano   7,2 % p/p base seca    (Megazyme K-YBGL)
  alfa-glucano  31,5 % p/p base seca    -> almidon (220)
  ergosterol     0,45 mg/g base seca

Lectura:
  El alfa-glucano alto ya grita grano. El ergosterol lo confirma con un
  segundo eje independiente: un cuerpo fructifero de Ganoderma no anda
  en 0,45 mg/g; ese valor es coherente con un producto donde la fraccion
  fungica real es pequena frente al soporte de cereal.

Estimacion de fraccion fungica (ILUSTRATIVA, orden de magnitud):
  si el cuerpo fructifero de referencia diera 4,0 mg/g de ergosterol,
  0,45 / 4,0 = 0,11  -> del orden del 11 % de biomasa fungica real.
  Es una ESTIMACION, no una medida: requiere el valor de referencia de tu
  propia cepa y material, medido, no supuesto. Ejecutar el calculo en
  Matematicas_lushows si va a sostener una decision de compra o una queja.
```

Ese cálculo es el argumento más fuerte que puedes llevar a una negociación con un proveedor: no le estás
diciendo "creo que me estafas", le estás diciendo "tu material tiene 0,45 mg/g de ergosterol y 31,5 % de
α-glucano; explícame de dónde sale eso" (`284`, `292`).

## Limitaciones honestas del marcador

- **No identifica especie.** Cualquier hongo da ergosterol, incluido un moho contaminante. Para especie,
  ITS (`245`).
- **Varía con la edad y el estado fisiológico** del material: micelio joven y cuerpo fructífero maduro no dan
  lo mismo.
- **Varía con el proceso.** Un extracto acuoso arrastra poco ergosterol (es lipofílico), así que un extracto
  acuoso legítimo puede dar bajo. **El valor esperado depende del tipo de extracto** (`241`).
- **Se degrada** con luz, oxígeno y calor prolongado (`61`).
- **No hay un umbral regulatorio.** Es un marcador técnico de auditoría, no un límite legal.

Por eso el ergosterol nunca se usa solo: se usa **junto con** β/α-glucano e ITS. Los tres juntos son muy
difíciles de falsificar a la vez.

## Qué se puede y qué no se puede afirmar

- **Se puede** reportar el ergosterol medido como dato de composición y como criterio de aceptación interno.
- **Se puede** usarlo como argumento de calidad frente a un comprador técnico: "nuestro material aporta
  X mg/g de ergosterol, coherente con cuerpo fructífero".
- **No se puede** presentarlo como "activo" con efecto en salud. El ergosterol no tiene claim; lo que tiene
  interés nutricional es su producto de fotoconversión, la vitamina D2 (`236`).
- **No se puede** usar un valor de ergosterol para afirmar la especie.

## Errores comunes

- **Pedir ergosterol sin saponificar** cuando el material tiene ergosterol esterificado: subestimas.
- **Comparar el ergosterol de un extracto acuoso contra el de materia prima entera.** Bases y materiales
  distintos (`242`).
- **Interpretar un ergosterol alto como pureza.** Un moho contaminante también aporta (`244`).
- **No proteger la muestra de la luz** y culpar al laboratorio del resultado bajo.
- **Usar un valor de referencia de otra especie** para estimar fracción fúngica. La referencia se mide.
- **Pedirlo solo, sin β/α-glucano.** Un eje se puede maquillar; dos ejes independientes, casi no.

## Conexión con otros módulos

→ `218-el-fraude-del-micelio-en-grano.md` — el fraude que este marcador destapa.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — el otro eje de la misma auditoría.
→ `236-vitamina-d2-y-tratamiento-uv.md` — qué pasa cuando este marcador se convierte en nutriente.
→ `55-esteroles-y-triterpenos.md` — la química de la familia.
→ `245-identidad-de-especie-por-its.md` — lo que el ergosterol no puede decirte.
→ `111-banderas-rojas-en-un-coa.md` — cómo se lee un COA que omite este dato a propósito.
