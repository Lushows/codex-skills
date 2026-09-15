# 36 — Química inorgánica y metales relevantes (el hongo es un acumulador, y eso es un problema de negocio)

Este es el módulo que explica por qué un producto de hongos puede ser irreprochable en todo —identidad,
β-glucanos, microbiología— y aun así ser rechazado en aduana o en un registro sanitario. Los hongos son
biorremediadores naturales: absorben y concentran metales del sustrato con una eficiencia que la
agricultura envidiaría. Eso, que es una virtud ambiental, es un riesgo comercial directo. Si tu materia
prima creció sobre sustrato contaminado o en una zona minera, tu producto va a llevar cadmio y plomo, y
ningún proceso de extracción los quita: los **concentra**.

Términos: **metal pesado (heavy metal)** = en uso regulatorio, los elementos tóxicos controlados; en la
práctica, los cuatro grandes son Cd, Pb, As y Hg. **oligoelemento / elemento traza (trace element)** =
elemento necesario en cantidades pequeñas (Fe, Zn, Cu, Se, Mn). **bioacumulación (bioaccumulation)** =
acumular más concentración que el medio del que se toma. **factor de bioconcentración (BCF)** = cociente
entre concentración en el organismo y en el sustrato. **especiación (speciation)** = en qué forma química
está el elemento; determina su toxicidad. **quelante (chelator)** = molécula que atrapa el metal.

## Los cuatro grandes, y por qué cada uno importa

| Elemento | Fuente típica en tu cadena | Especiación relevante | Nota |
|---|---|---|---|
| Cadmio (Cd) | Suelo, fertilizantes fosfatados, sustrato; **los hongos lo acumulan mucho** | Cd²⁺ ligado a fitoquelatinas y metalotioneínas | El más problemático en hongos y en cannabis |
| Plomo (Pb) | Suelo, polvo industrial, pinturas, equipos viejos | Pb²⁺ | Sin nivel seguro conocido para exposición infantil |
| Arsénico (As) | Suelo, agua de riego, pesticidas históricos | **As inorgánico** (tóxico) vs arsenobetaína (poco tóxico) | Sin especiación, un "As total" alto puede ser falsa alarma |
| Mercurio (Hg) | Suelo, minería de oro (relevante en Colombia), pescado | Hg²⁺ vs metilmercurio | Zonas de minería aurífera son un riesgo real |

Los cuatro son los que exigen prácticamente todas las farmacopeas y regulaciones: USP <232>/<233> con los
límites de exposición diaria permitida (PDE), ICH Q3D para farmacéuticos, y los límites propios de cada
país para alimentos y suplementos. **A agosto de 2026** los valores concretos deben verificarse contra la
norma vigente del mercado de destino y la vía de administración; no se citan de memoria (`266`, `273`,
`280`).

## Por qué el hongo acumula: la química del asunto

El micelio produce **metalotioneínas** y péptidos ricos en cisteína (fitoquelatinas) cuyos grupos tiol
(–SH) tienen una afinidad enorme por metales blandos como Cd²⁺, Hg²⁺ y Pb²⁺ (química de ácidos y bases
duros y blandos: el azufre blando se une al metal blando). Es un mecanismo de defensa: el hongo secuestra
el metal para que no le dañe las enzimas. El resultado es que el metal queda **dentro** de la biomasa,
unido con fuerza.

```
Consecuencias prácticas:

1. Lavar la biomasa NO quita el metal. Está intracelular, unido a péptidos.
2. El factor de bioconcentración puede ser > 1 para Cd en varias especies: el hongo tiene MÁS
   concentración que su sustrato.
3. Extraer CONCENTRA. Si de 10 kg de biomasa sacas 1 kg de extracto, el Cd que salió con el
   extracto queda hasta 10 veces más concentrado (por eso el límite se aplica al PRODUCTO
   TERMINADO, no a la materia prima) (`151`, `243`).
4. Los metales unidos a péptidos hidrosolubles salen en la extracción acuosa — la misma que
   saca tus beta-glucanos (`19`, `144`).
```

Lo mismo aplica al cannabis: es una planta fitorremediadora reconocida, tan buena acumulando que se ha
estudiado para limpiar suelos contaminados. El mismo mecanismo la vuelve un vehículo de exposición si el
suelo está sucio (`202`).

## Los otros elementos que aparecen en tu operación

| Elemento | Rol | Dónde aparece / por qué te importa |
|---|---|---|
| Hierro (Fe), Cobre (Cu) | Catalizadores redox | Aceleran la oxidación de tus activos; entran por equipos y agua (`24`, `27`) |
| Zinc (Zn), Manganeso (Mn) | Cofactores enzimáticos | Nutrientes; en exceso, contaminante |
| Selenio (Se) | Cofactor; algunos hongos lo acumulan | Ventana estrecha entre necesidad y toxicidad |
| Potasio (K) | Muy abundante en hongos | Relevante para dietas restringidas; aparece en el análisis proximal |
| Calcio (Ca), Magnesio (Mg) | Dureza del agua | Precipitan con fosfato y con oxalato (`23`, `230`) |
| Níquel (Ni), Cromo (Cr) | Del acero inoxidable | Lixiviación de equipos mal seleccionados; usar 316 L |
| Aluminio (Al) | Envases, filtros | Contaminación por contacto (`163`) |
| Silicio (Si) | Tierras filtrantes | Puede aportar sílice y, si es ácida, catálisis no deseada (`27`) |

## Cómo se mide

| Pregunta | Método | Unidad / detalle |
|---|---|---|
| ¿Cuánto Cd, Pb, As, Hg tiene mi producto? | **ICP-MS** tras digestión ácida en microondas (HNO₃/H₂O₂) | mg/kg (ppm) o µg/kg (ppb) sobre producto terminado (`88`) |
| Alternativa de menor costo | Absorción atómica (AAS/GFAAS); Hg por vapor frío | mg/kg; menor sensibilidad y un elemento a la vez (`89`) |
| ¿Es arsénico inorgánico o no? | **Especiación** por HPLC-ICP-MS | mg/kg de As inorgánico; cambia por completo la evaluación |
| ¿El agua de proceso aporta? | ICP-MS del agua tipo II y del agua de red | µg/L (`106`) |
| ¿El equipo lixivia? | Blanco de proceso: correr el proceso sin biomasa y analizar | µg/L; identifica la fuente real |
| ¿El sustrato es la fuente? | ICP-MS del sustrato + cálculo del BCF | mg/kg en sustrato y en biomasa (`239`) |
| ¿Cuánto expone una porción? | mg/kg × gramos por porción, contra el PDE aplicable | µg/día; se calcula en código (`135`) |

Regla dura: el límite regulatorio aplica al **producto terminado en la forma en que se consume**, y la
comparación correcta es **exposición diaria** (µg/día por la dosis recomendada), no la concentración
suelta. Un extracto con 1,5 mg/kg de Cd puede ser aceptable a 500 mg/día e inaceptable a 5 g/día. Ese
cálculo se ejecuta, no se estima (`135`, `Matematicas_lushows`).

## Ejemplo aplicado — de dónde viene el cadmio del lote

Producto: extracto acuoso seco de reishi, 10:1. Un COA de importación reporta Cd por encima del límite del
comprador **(ILUSTRATIVO)**:

```
Muestra analizada (ICP-MS, digestión en microondas)     Cd (mg/kg)   Pb (mg/kg)
Sustrato de cultivo (aserrín + salvado)                    0,21         0,44
Cuerpo fructífero seco                                     0,58         0,19
Extracto acuoso seco 10:1                                  4,90         1,55
Agua de proceso (tipo II)                               < 0,0002     < 0,0005
Blanco de proceso (equipo sin biomasa)                     0,003        0,008

Factor de bioconcentración sustrato → hongo: 0,58 / 0,21 = 2,8
Factor de concentración hongo → extracto:    4,90 / 0,58 = 8,4  (coherente con el ratio 10:1)
Exposición a 1 500 mg/día del extracto: 4,90 mg/kg × 0,0015 kg = 7,4 µg de Cd/día
```

Diagnóstico defendible: el agua y el equipo están limpios (blancos bajos); el hongo concentró 2,8 veces lo
del sustrato, y la extracción concentró 8,4 veces más. **La causa raíz está en el sustrato**, y la solución
es la calificación del proveedor de sustrato con análisis de entrada, no un "lavado" ni un cambio de
proceso (`284`, `141`). La cifra de exposición diaria es la que se compara contra el límite aplicable, y
es la que hay que llevar a la conversación regulatoria (`135`, `266`).

## Errores comunes

- Analizar metales solo en la materia prima. El límite aplica al producto terminado, y el extracto concentra.
- Aceptar un "As total" alto como sentencia sin pedir especiación. Puede ser arsénico orgánico poco tóxico.
- Creer que lavar, hervir o filtrar quita los metales. Están unidos intracelularmente.
- Comparar concentraciones (mg/kg) entre productos con dosis diarias distintas. Se compara exposición.
- Usar acero 304 o equipos de aluminio y luego culpar a la materia prima. El blanco de proceso lo revela.
- Comprar biomasa silvestre sin conocer la zona. En Colombia, cercanía a minería aurífera implica Hg
  hasta que se demuestre lo contrario.
- Confiar en un COA de metales sin acreditación ISO 17025 ni LOD reportado. "No detectado" con un LOD de
  1 mg/kg no dice nada útil (`73`, `107`, `111`).

## Conexión con otros módulos

→ `243-metales-pesados-en-hongos.md` — el módulo dueño: especies, datos y límites en hongos.
→ `202-metales-pesados-en-cannabis.md` — el caso cannabis.
→ `88-icp-ms-y-metales-pesados.md` — la técnica analítica de referencia.
→ `136-toxicologia-de-metales-pesados.md` — qué hace cada metal en el cuerpo.
→ `135-noael-ida-y-limites-de-exposicion.md` — cómo se convierte mg/kg en riesgo.
→ `239-sustrato-cultivo-y-quimica-resultante.md` — la causa raíz está casi siempre aquí.
→ `24-oxido-reduccion.md` — Fe y Cu como catalizadores de degradación.
→ `284-auditoria-de-proveedor.md` — cómo se evita el problema desde la compra.
