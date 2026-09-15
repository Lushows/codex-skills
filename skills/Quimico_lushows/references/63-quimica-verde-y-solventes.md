# 63 — Química verde y elección de solvente (etanol, hexano o CO₂: cómo se decide con criterio)

Elegir solvente es la decisión más cara y más irreversible de una línea de extractos: determina qué activos
sacas, cuánto cuesta el equipo, qué análisis vas a tener que pagar para siempre, qué le puedes poner a la
etiqueta y si el producto puede entrar a Europa o a Estados Unidos. La mayoría de la gente lo decide por
YouTube. Este módulo te da el marco real: química verde para pensar el proceso completo, y la clasificación
ICH de solventes residuales para saber qué te van a exigir después. El error caro que evita: montar una
extracción con hexano porque rinde más, y descubrir en el registro que ahora cada lote necesita GC-headspace
y que el límite es 290 ppm.

Términos: **química verde (green chemistry)** = diseñar procesos para no generar el problema, en vez de
limpiarlo después. **Factor E (E-factor)** = kg de residuo por kg de producto. **Solvente residual (residual
solvent)** = el que queda en el producto terminado. **PDE (permitted daily exposure)** = exposición diaria
permitida, en mg/día, de donde salen los ppm. **CMR** = cancerígeno, mutagénico o tóxico para reproducción.

## Los principios de química verde que sí cambian tu decisión

De los doce principios clásicos, cuatro son los que mueven la aguja en extracción de productos naturales:

1. **Prevenir en vez de tratar.** El solvente que no usas no hay que recuperarlo, ni analizarlo, ni declararlo.
2. **Solventes más seguros.** Si dos solventes hacen el trabajo, gana el de menor toxicidad y menor clase ICH.
3. **Eficiencia energética.** Un proceso a 25 °C vale más que uno a 80 °C, y encima protege tus termolábiles (`62`).
4. **Materias primas renovables.** El etanol de caña es renovable; el hexano viene del petróleo. En Colombia
   eso además tiene un costo y una disponibilidad distintos.

Métricas que se pueden poner en un informe y no son marketing:

```
Factor E   = kg de residuo total / kg de producto        (menor es mejor)
Intensidad de solvente = L de solvente / kg de extracto  (el número que negocias con el maquilador)
Recuperación de solvente = % que vuelve al proceso       (define el costo real por lote)
Consumo energético = kWh / kg de extracto
```

Un extracto "artesanal" con factor E de 40 no es más verde que uno industrial con factor E de 6. La palabra
"natural" no es una métrica; estas sí.

## Los candidatos, lado a lado

| Solvente | Polaridad (E_T^N aprox.) | Qué extrae bien | Clase ICH | Seguridad de planta | Costo/complejidad | Etiqueta |
|---|---|---|---|---|---|---|
| **Agua** | 1,00 | Polisacáridos, β-glucanos, aminoácidos, sales | No aplica | Nula | Bajo; hay que secar después (`149`, `150`) | Impecable |
| **Etanol (alimentario)** | 0,65 | Triterpenos, cannabinoides, fenoles, alcaloides | **Clase 3** (5.000 ppm) | Inflamable: zona clasificada | Medio | Excelente; "extraído con etanol" vende |
| **Etanol/agua 40–70 %** | intermedia | Extracción dual pragmática (`146`) | Clase 3 | Igual | Medio | Excelente |
| **Acetato de etilo** | 0,23 | Fenoles medios, algunos terpenoides | **Clase 3** | Inflamable | Medio | Aceptable |
| **Isopropanol / acetona** | 0,55 / 0,36 | Limpieza, precipitación de polisacáridos | **Clase 3** | Inflamable | Medio | Aceptable con explicación |
| **n-Heptano** | 0,01 | Apolares; alternativa "menos mala" al hexano | **Clase 3** | Inflamable | Medio-alto | Mejor que hexano |
| **n-Hexano** | 0,01 | Lípidos, cannabinoides, ceras | **Clase 2 — 290 ppm** | Inflamable + neurotóxico (2,5-hexanodiona) | Medio | Mala: rechazo del consumidor y control obligatorio |
| **Butano / propano** | muy apolar | Cannabinoides y terpenos, extracción a baja T (`188`) | No están en Q3C como Clase 2; se controlan igual por norma de cannabis | **Alto riesgo de explosión**: sala certificada | Alto | Regulada y vigilada |
| **CO₂ supercrítico** | ajustable con presión y co-solvente | Apolares y, con etanol como modificador, semipolares (`148`) | No deja residuo relevante | Alta presión: riesgo mecánico | **Alto CAPEX** | Excelente: "libre de solventes" |
| **Metanol** | 0,76 | Solo análisis, nunca producto | **Clase 2 — 3.000 ppm** | Tóxico | — | Prohibido de facto en producto |
| **Diclorometano** | 0,31 | Análisis, fraccionamiento | **Clase 2 — 600 ppm** | CMR sospechoso | — | No en alimentos |

Nota importante: el solvente de **análisis** (acetonitrilo, metanol) y el de **producción** son mundos
distintos. En el laboratorio usas lo que dé mejor cromatografía; en producción usas lo que puedas defender
ante una autoridad y ante un cliente (`79`, `87`).

## La tabla que hay que memorizar: clases ICH Q3C

ICH Q3C es la guía de solventes residuales; la Farmacopea (USP <467>, Ph. Eur. 5.4) la implementa. A agosto
de 2026, verifica la versión vigente —la serie va por R8/R9 y se actualiza— pero la estructura de clases es
estable:

| Clase | Definición | Ejemplos | Límite |
|---|---|---|---|
| **Clase 1** | Deben evitarse: cancerígenos conocidos o peligro ambiental | Benceno **2 ppm**; tetracloruro de carbono **4 ppm**; 1,2-dicloroetano **5 ppm**; 1,1-dicloroeteno **8 ppm**; 1,1,1-tricloroetano **1.500 ppm** | Los citados, individuales |
| **Clase 2** | Deben limitarse: toxicidad no genotóxica o neurotoxicidad | **Hexano 290 ppm** (PDE 2,9 mg/día); metanol 3.000; diclorometano 600; acetonitrilo 410; tolueno 890 | Por PDE, para dosis diaria de 10 g |
| **Clase 3** | Baja toxicidad: sin riesgo a niveles habituales | Etanol, acetato de etilo, acetona, isopropanol, heptano, ácido acético | **≤ 5.000 ppm (0,5 %)** = PDE 50 mg/día |

```
Conversión que hay que saber hacer:
   Límite (ppm) = PDE (mg/día) × 1.000 / dosis diaria (g/día)

Verificación con hexano, dosis de referencia de 10 g/día:
   2,9 mg/día × 1.000 / 10 g/día = 290 ppm   ✔ coincide con la tabla ICH

Y aquí está el matiz que casi nadie aplica: si TU producto se toma a 2 g/día, el límite
"de opción 2" (por PDE real) sería 2,9 × 1.000 / 2 = 1.450 ppm; si se toma a 30 g/día, baja a 97 ppm.
El número de la tabla asume 10 g/día. Ejecutar en código (`Matematicas_lushows`), no de cabeza.
```

## Cómo se decide, en cuatro preguntas

```
1) ¿Qué activo quiero?  → mira su logP y su polaridad (`30`, `20`)
     β-glucanos, polisacáridos ............ AGUA caliente (`144`)
     Triterpenos, cannabinoides, fenoles .. ETANOL o etanol/agua (`145`)
     Solo apolares, sin residuo ........... CO₂ supercrítico (`148`)
     Ambos mundos ......................... EXTRACCIÓN DUAL: dos extractos y luego se mezclan (`146`)

2) ¿Qué me exige el mercado destino?  → EE. UU. y UE piden control de residuales; Clase 2 = análisis por lote

3) ¿Qué puedo operar con seguridad?  → inflamables exigen zona clasificada; hidrocarburos, sala certificada

4) ¿Qué puedo poner en la etiqueta sin sonrojarme?  → "extraído con agua y alcohol de caña" se defiende solo
```

Si dos opciones empatan técnicamente, gana la de menor clase ICH. Casi siempre es etanol/agua.

## Cómo se comprueba

Solventes residuales se miden por **GC con headspace** (`87`, `201`), con estándar interno y, cuando el
límite es Clase 1, con detector y método capaces de llegar a ppm bajos (a veces GC-MS). Lo que hay que pedirle
al laboratorio y verificar en el COA:

- Qué solventes se buscaron. Un "solventes residuales: cumple" sin lista de analitos no significa nada (`111`).
- El **LOQ** de cada uno frente al límite. Un LOQ de 500 ppm no puede demostrar cumplimiento de 290 ppm (`73`).
- Base y unidad: ppm = mg/kg de producto **tal cual**, y con la dosis diaria declarada si se usa opción 2.
- Recuperación del método en tu matriz: un extracto oleoso retiene solvente mucho más que un polvo.

## Ejemplo aplicado — extracto de reishi, etanol vs hexano

Decisión real de una marca pequeña **(ILUSTRATIVO)**:

```
Opción A: etanol 70 % (Clase 3)
  Rendimiento de triterpenos ....... 1,9 % p/p base seca
  Análisis por lote ................ etanol residual, opción "cumple ≤ 5.000 ppm": ensayo simple
  Costo analítico recurrente ....... bajo
  Etiqueta ......................... "extracción hidroalcohólica"
  Riesgo regulatorio ............... bajo

Opción B: hexano (Clase 2)
  Rendimiento de la fracción apolar . mayor para lípidos, irrelevante para el claim de triterpenos
  Análisis por lote ................. GC-headspace con LOQ ≤ 50 ppm frente a límite 290 ppm: obligatorio
  Costo analítico recurrente ........ alto, por lote, para siempre
  Etiqueta .......................... "extraído con hexano": objeción comercial garantizada
  Riesgo regulatorio ................ un lote fuera de límite es un lote perdido

Decisión: A. La diferencia de rendimiento no compra el pasivo analítico ni el problema de percepción.
```

Cuando el activo objetivo sí es apolar y el mercado paga la diferencia (aceites de cannabis premium), la
comparación real es **CO₂ supercrítico vs etanol**, no hexano vs etanol (`189`, `187`).

## Errores comunes

- Elegir el solvente por rendimiento en masa. El rendimiento que importa es el del **activo**, no el del bulto
  (`151`, `242`).
- Usar alcohol no alimentario o alcohol desnaturalizado con desnaturalizantes tóxicos. El desnaturalizante se
  queda en tu producto y no está en tu lista de análisis.
- Suponer que "Clase 3 = no hay que medir". Clase 3 tiene límite (5.000 ppm) y hay que demostrarlo al menos
  en la validación del proceso.
- Comparar un ppm de solvente contra un límite pensado para 10 g/día cuando tu dosis es otra, sin hacer la
  conversión de PDE.
- Creer que CO₂ supercrítico es "sin solvente" cuando se usó etanol como co-solvente. Entonces sí hay etanol
  residual que declarar.
- No pedir la lista de analitos ni los LOQ en el COA de residuales (`110`, `111`).
- Cambiar de proveedor de solvente sin control de cambios. Distinto grado, distintas impurezas (`169`).

## Conexión con otros módulos

→ `87-solventes-residuales.md` — el módulo dueño del análisis: GC-headspace, límites, cómo se reporta.
→ `201-solventes-residuales-en-cannabis.md` — el caso cannabis y sus listas regulatorias.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — Hansen, "lo semejante disuelve a lo semejante".
→ `30-extraccion-liquido-liquido-y-logp.md` — partición y por qué logP predice el solvente.
→ `145-extraccion-hidroalcoholica-y-tinturas.md` · `144-extraccion-acuosa-y-decoccion.md` — las operaciones.
→ `146-extraccion-dual-y-por-que-importa.md` — por qué en hongos casi siempre son dos extracciones.
→ `148-co2-supercritico.md` · `187-extraccion-con-etanol.md` · `188-extraccion-con-hidrocarburos.md`.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — qué sale con cada uno, en hongos.
