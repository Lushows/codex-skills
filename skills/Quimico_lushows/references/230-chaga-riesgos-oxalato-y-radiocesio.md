# 230 — Chaga: los riesgos que casi nadie pone en la ficha (oxalato y radiocesio)

El chaga (*Inonotus obliquus*) es el hongo de moda con el peor perfil de riesgo real del catálogo, y el
riesgo no es teórico: hay al menos dos casos publicados de daño renal en personas que lo tomaron a diario,
uno de ellos irreversible. La causa probable es el **oxalato**, que en chaga puede llegar a niveles que no
se parecen a nada más que se venda como suplemento. Además, por ser un material silvestre de bosques del
hemisferio norte, puede traer **cesio radiactivo**. Este módulo es la advertencia documentada. Si vendes
chaga y no lo has leído, estás vendiendo a ciegas.

Términos: **oxalato (oxalate)** = anión del ácido oxálico; forma cristales insolubles con calcio.
**nefropatía por oxalato (oxalate nephropathy)** = depósito de cristales de oxalato de calcio en el túbulo
renal, visible en biopsia. **base seca (dry basis, DM)** = sin agua. **radiocesio (radiocaesium)** = los
isótopos radiactivos ¹³⁴Cs y ¹³⁷Cs. **Bq/kg (becquerel por kilogramo)** = desintegraciones por segundo por
kilo; unidad de actividad. **espectrometría gamma (gamma spectrometry)** = medición de radionúclidos con
detector de germanio hiperpuro (HPGe).

## Parte 1 — Oxalato: los dos casos publicados

| Caso | Fuente | Persona | Exposición | Desenlace |
|---|---|---|---|---|
| ERC terminal | *Journal of Korean Medical Science*, 2020; 35(15):e122 | Hombre, 49 años | 3 g/día de polvo de chaga durante 4 años, luego 9 g/día un año más | Nefritis tubulointersticial crónica con cristales de oxalato en biopsia. Enfermedad renal terminal, hemodiálisis de mantenimiento, sin recuperación a 18 meses |
| Lesión renal aguda | *Medicine (Baltimore)*, 2022; PMC8913114 | Hombre, 69 años | 10–15 g/día de polvo de chaga + 500 mg/día de vitamina C, 3 meses | Nefropatía oxálica aguda con síndrome nefrótico. Requirió hemodiálisis y corticoide; recuperó (creatinina de 6,94 a 1,00 mg/dL en un mes) |

Nivel de evidencia: `[reporte de caso clínico]`. Dos casos no prueban causalidad poblacional, pero sí
establecen un mecanismo plausible con biopsia que lo respalda. Para una decisión de producto eso basta:
es un riesgo conocido, documentado y evitable.

Detalle que importa del segundo caso: el paciente también tomaba **vitamina C 500 mg/día**. El ácido
ascórbico se metaboliza parcialmente a oxalato, así que la combinación suma. Si tu cliente toma chaga y
vitamina C alta, el riesgo no se suma linealmente pero sí se suma.

## Cuánto oxalato trae realmente el chaga

Aquí está la parte incómoda: **los valores publicados difieren en dos órdenes de magnitud**.

| Fuente | Valor | Unidad y base |
|---|---|---|
| *J Korean Med Sci*, 2020 (el polvo que consumió el paciente) | 0,14 g oxalato por g de polvo = **14,2 % p/p** = 142 mg/g | base seca del polvo |
| Material ruso, recopilado en la revisión de oxalatos en chaga de la North American Mycological Association (M. Beug, namyco.org, 2023) | 3.904 mg oxalato soluble/kg + 960 mg insoluble/kg ≈ **0,49 % p/p total** | base seca |

Esa brecha (142 mg/g vs ~4,9 mg/g) no es un error de alguien: es la naturaleza de un material silvestre
sin estandarizar. Y es exactamente por eso que **el oxalato del chaga que TÚ vendes hay que medirlo**, no
buscarlo en un paper.

Traducido a exposición diaria (el cálculo se ejecuta, no se estima de memoria — `Matematicas_lushows`):

```
Porción tipica de un suplemento de chaga: 1,0 g/dia de polvo

Escenario alto (142 mg/g):   1,0 g x 142 mg/g = 142 mg oxalato/dia
Escenario bajo (4,9 mg/g):   1,0 g x 4,9 mg/g =   4,9 mg oxalato/dia
Factor entre escenarios: 29x

Reconstruccion del caso coreano (9 g/dia, polvo de 142 mg/g):
  9 g x 142 mg/g = 1.278 mg oxalato/dia solo del chaga

Referencia de contexto: la ingesta de oxalato de una dieta occidental tipica
se reporta en el orden de 100-200 mg/dia (literatura nutricional; verificar la
fuente vigente). El caso coreano multiplica ese orden de magnitud por si solo.
```

La lectura honesta: con un chaga del extremo bajo, una porción de 1 g/día aporta oxalato irrelevante frente
a la dieta. Con uno del extremo alto y una porción de 5–10 g/día, aportas varias veces la dieta completa.
**Sin el número de tu lote no sabes en cuál de los dos mundos estás.**

## Parte 2 — Radiocesio y radiactividad natural

El chaga crece durante años sobre abedules vivos y acumula lo que el árbol y el suelo le den, incluidos
radionúclidos depositados tras Chernóbil (1986) en Europa del Este, Escandinavia y Rusia occidental.

| Dato | Valor | Fuente |
|---|---|---|
| ¹³⁷Cs en hongos silvestres comestibles del noreste de Polonia (230 muestras, 19 especies) | 0,94–159,0 Bq/kg peso fresco; ninguna sobre el límite aplicado de 1.250 Bq/kg p.f. | *Toxics* (MDPI), 2025; 13(7):601 |
| ¹³⁷Cs en chaga de mercados ruso y chino | 11–13 Bq/kg base seca (valores bajos) | Estudio de acumulación y distribución de ⁴⁰K en chaga, PMC9157780 |
| Nivel máximo de comercio de alimentos en la UE tras contaminación | 600 Bq/kg (categoría general de alimentos) — la categoría de "alimentos menores" admite valores más altos | Reglamento (Euratom) 2016/52; el organismo alemán BfS aplica 600 Bq/kg |

A agosto de 2026, verifica el valor y la **categoría** que aplica a tu producto antes de fijar el límite de
tu especificación: no es lo mismo un alimento base que un suplemento consumido en gramos por día.

Dos matices técnicos:

- El chaga concentra **potasio**, y el potasio natural trae **⁴⁰K**, que es radiactivo por naturaleza y da
  señal en el espectro gamma. Un laboratorio que reporte "actividad detectada" sin separar ⁴⁰K de ¹³⁷Cs te
  va a asustar sin motivo. Pide el reporte por radionúclido (ver `38`).
- La evidencia disponible sugiere que el chaga de mercado suele traer ¹³⁷Cs bajo. Eso **no** te exime de
  medirlo si el origen es Siberia, Rusia occidental, Bielorrusia, Ucrania o el Báltico: el punto del análisis
  es descartar el lote malo, no confirmar el promedio.

## Cómo se mide / cómo se comprueba

| Riesgo | Método | Unidad y base | Nota práctica |
|---|---|---|---|
| Oxalato total | Enzimático con oxalato oxidasa (kit tipo Trinity/Megazyme) | `mg/g base seca` | El más accesible; pide que reporten total, no solo soluble |
| Oxalato soluble vs insoluble | Cromatografía iónica (IC) con detección de conductividad | `mg/g base seca` cada fracción | El soluble es el que más importa para absorción |
| Confirmación | HPLC o LC-MS/MS con patrón de ácido oxálico | `mg/g base seca` | Para dato que sostenga etiqueta o expediente |
| ¹³⁷Cs, ¹³⁴Cs, ⁴⁰K | Espectrometría gamma con detector HPGe, geometría calibrada | `Bq/kg base seca` (declara la base) | Laboratorio con acreditación en el alcance (`107`) |
| Metales pesados | ICP-MS tras digestión ácida | `mg/kg base seca` | Ver `243` |

Todo esto sobre el **material que vas a vender**, no sobre la materia prima antes de extraer. El extracto
concentra: si haces un 10:1 acuoso, el oxalato soluble viene con el agua.

## Ejemplo aplicado — decisión de porción para un chaga real (ILUSTRATIVO)

```
Lote CH-2026-003, esclerocio molido, origen declarado: Siberia

Resultado de oxalato total (enzimatico):  38 mg/g base seca
Porcion propuesta inicialmente:            3 g/dia
Aporte de oxalato:  3 g x 38 mg/g = 114 mg/dia  -> del orden de una dieta completa

Decision: bajar la porcion a 1 g/dia (38 mg/dia), declarar el dato,
e incluir advertencia para personas con antecedente de calculos renales
o funcion renal reducida, y para quienes toman dosis altas de vitamina C.

Sin el analisis, la porcion de 3 g/dia se habria puesto "porque asi lo hace
la competencia". Eso es exactamente como se llega a un caso publicado.
```

## Qué se puede y qué no se puede afirmar

- **Se puede** y **se debe** poner una advertencia de seguridad. Advertir no es un claim de enfermedad; es
  responsabilidad del fabricante y en Colombia forma parte de lo que INVIMA espera del rotulado (`266`, `272`).
- **Se puede** declarar el contenido de oxalato medido, con método, unidad y base.
- **No se puede** decir que el chaga trata, previene o cura nada. La literatura oncológica de chaga es
  `[in vitro]` (ver `229`, `268`).
- **No se puede** repetir "es seguro porque es natural". El oxalato de este material es natural y mandó a
  un hombre de 49 años a diálisis permanente.

## Errores comunes

- **No medir oxalato y copiar la porción de la competencia.** Es el error que produce los casos publicados.
- **Medir solo oxalato soluble** y reportarlo como total: subestimas.
- **Recomendar chaga a diario y sin tope de duración.** Los dos casos son de consumo crónico, no de una taza.
- **Ignorar la vitamina C concomitante** cuando se vende un stack de "antioxidantes".
- **Comprar material del este de Europa sin espectrometría gamma** y descubrirlo cuando el importador de
  destino lo pida.
- **Confundir ⁴⁰K natural con contaminación** y rechazar un lote bueno por leer mal el reporte (`38`).
- **Analizar la materia prima y no el extracto**, que es lo que el cliente se toma (`242`).

## Conexión con otros módulos

→ `229-chaga-inonotus-quimica.md` — la química del material, de donde viene este módulo.
→ `38-radiactividad-en-alimentos-y-plantas.md` — cómo se lee un reporte de espectrometría gamma.
→ `243-metales-pesados-en-hongos.md` — el otro riesgo de los acumuladores.
→ `134-toxicologia-basica-dosis-y-riesgo.md` — por qué la dosis y la duración definen el riesgo.
→ `250-seguridad-e-interacciones-de-hongos.md` — el panorama de seguridad del bloque.
→ `272-etiquetado-en-colombia.md` — dónde va la advertencia en la etiqueta.
