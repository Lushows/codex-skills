# 281 — Métodos oficiales AOAC: el número que hay que exigirle al laboratorio

Cuando le pides un análisis a un laboratorio, la pregunta que separa un resultado defendible de un número
bonito es una sola: **¿con qué método?** Y la mejor respuesta posible es un código: *AOAC 2015.01*,
*AOAC 2018.11*. Ese código significa que el método pasó por un estudio colaborativo entre laboratorios y que
su desempeño está documentado. La alternativa —"método interno"— no es inválida, pero te obliga a pedir el
expediente de validación. Este módulo enseña a leer el sistema AOAC, cuáles son los métodos que importan en
cannabis y hongos, y —muy importante— **dónde no existe método oficial**, que es justo donde vive el fraude.

Términos: **AOAC INTERNATIONAL** = organización que desarrolla y valida métodos analíticos. · **OMA
(Official Methods of Analysis)** = el compendio de métodos oficiales. · **SMPR (Standard Method Performance
Requirements)** = el pliego de desempeño que un método debe cumplir antes de existir. · **First Action /
Final Action** = las dos etapas de adopción de un método. · **ERP (Expert Review Panel)** = el panel que
decide. · **CASP (Cannabis Analytical Science Program)** = el programa de AOAC para cannabis.

## 1. Cómo nace un método oficial

```
1. Alguien define QUÉ hay que medir y con qué desempeño   → SMPR (exactitud, precisión, LOQ, rango)
2. Se convoca a métodos candidatos
3. Un Expert Review Panel los evalúa                       → adopción como FIRST ACTION
4. Se acumula evidencia de uso y estudios colaborativos    → FINAL ACTION
5. El método entra al compendio OMA con su número y año    → "AOAC 2015.01"
```

El número lleva el año de adopción codificado: **2018.11** es el método 11 adoptado en 2018. Eso te dice de
entrada qué tan reciente es. Un método de los años noventa no está mal por viejo —muchos son excelentes—
pero sí conviene saber para qué matriz se validó.

**Lo más importante de un método oficial es su ALCANCE (scope):** para qué analito, en qué matriz y en qué
rango se validó. Usar un método fuera de su alcance lo convierte, en la práctica, en un método interno.

## 2. Cannabis: CASP y los métodos que sí existen

AOAC creó el **Cannabis Analytical Science Program (CASP) en 2019** para desarrollar estándares, métodos
oficiales, formación y ensayos de aptitud (proficiency testing) para la comunidad de laboratorios de
cannabis. Sus grupos de trabajo cubren contaminantes microbiológicos, productos de consumo, formación y
ensayos de aptitud. Fuente: `aoac.org` → *Cannabis Analytical Science Program*; consultado agosto de 2026.

| Método / estándar | Qué hace | Detalle verificado |
|---|---|---|
| **AOAC OMA 2018.11** | Cannabinoides por **LC-DAD**, con detección por masas opcional | Determina Δ9-THC y THCA por separado, de modo que se pueden reportar individualmente **o como THC total**. Aplicable a concentrados, aceites y todo material vegetal de *Cannabis* sp., incluido el cáñamo |
| **SMPR de cannabinoides en cáñamo** (CASP, 2019) | Pliego de desempeño para métodos de THC en cáñamo | Referenciado en la guía del **USDA Hemp Program** (Interim Final Rule) como el estándar recomendado que deben cumplir los laboratorios al elegir método para analizar THC |

Fuente: `aoac.org`, notas de prensa sobre la aprobación del método oficial de cannabinoides en cáñamo y
sobre el estándar de cannabinoides en las guías del USDA. **Verifica si 2018.11 sigue en First Action o ya
pasó a Final Action, y si hay métodos posteriores, en el OMA vigente.**

Por qué 2018.11 le importa a cualquiera que venda cannabis: reporta el ácido y el neutro **por separado**.
Eso permite aplicar el factor 0,877 correctamente y discutir un resultado de "THC total" con números, no con
opiniones (`174`, `175`).

## 3. Contaminantes: los métodos transversales

| Método | Analitos | Matriz y notas |
|---|---|---|
| **AOAC 2015.01** | Arsénico, cadmio, plomo y mercurio por **ICP-MS** tras digestión por microondas | *Heavy Metals in Food*, First Action 2015. Validado en matrices como chocolate, jugo, pescado, fórmula infantil y arroz, con LOQ del orden de ≤10 µg/kg en sólidos. Es el método que se cita para metales pesados en alimentos y el que la industria adapta a botánicos |
| Métodos multirresiduo tipo **QuEChERS** | Plaguicidas | Extracción rápida + LC-MS/MS y GC-MS/MS. Ver `102` y `200` |
| Métodos de micotoxinas con columna de inmunoafinidad | Aflatoxinas, ocratoxina A | HPLC con detección de fluorescencia o LC-MS/MS. Ver `101`, `244` |
| Métodos de microbiología de alimentos | Aerobios, levaduras y mohos, *E. coli*, *Salmonella* | Alternativa: métodos de farmacopea (`280`) |

Ojo con el detalle que decide un caso: **AOAC 2015.01 mide arsénico total, no arsénico inorgánico.** La
toxicidad y los límites regulatorios modernos se refieren al **inorgánico**, que requiere **especiación**
(HPLC-ICP-MS). Si tu resultado de arsénico total está alto, la especiación puede salvarte el lote — y si tu
límite regulatorio es de inorgánico, reportar total es reportar otra cosa. Ver `88` y `136`.

**Los números de método distintos de los citados arriba no los afirmo de memoria: pídele al laboratorio el
código exacto y verifícalo contra el OMA vigente en `aoac.org`.**

## 4. Hongos: el hueco que hay que conocer

Aquí va el dato incómodo y central de este módulo, y hay que decirlo sin adornos:

> **A agosto de 2026 no me consta la existencia de un Método Oficial de AOAC para beta-glucano en hongos o
> micelio.**

Lo que sí existe:

| Método | Alcance real |
|---|---|
| **AOAC 995.16** | Beta-glucano de **enlace mixto** en **avena y cebada**. Adoptado como método oficial para esos cereales. **No está validado para hongos, micelio ni otros granos** |
| **Ensayo enzimático de McCleary (Megazyme K-YBGL)**, con etapas adicionales de amiloglucosidasa e invertasa para hidrolizar los α-glucanos antes de medir el β-glucano | Es el procedimiento que la industria de hongos usa como estándar de facto. Publicado como *Measurement of β-Glucan in Mushrooms and Mycelial Products*, **Journal of AOAC International, 2016, vol. 99(2), p. 364** |

Fuentes: `academic.oup.com` (J AOAC Int 2016;99(2):364), Megazyme (`megazyme.com`), compilaciones sectoriales
2025. **Verifica en el OMA vigente si ya se adoptó un método oficial para hongos; es un vacío que la
industria lleva años pidiendo cerrar.**

Consecuencia práctica y directa para BIO-SETA: **no puedes escribir "beta-glucano según AOAC" en tu
especificación**, porque no existe para tu matriz. Lo correcto es:

```
Beta-glucano: >= XX % p/p base seca
Método: ensayo enzimático de glucano total menos alfa-glucano (McCleary, J AOAC Int 2016;99(2):364),
        kit tipo Megazyme K-YBGL, con reporte de glucano total, alfa-glucano y beta-glucano por separado
```

Y que el laboratorio **reporte los tres números**. Un COA que solo trae "beta-glucano 30 %" sin el glucano
total ni el alfa-glucano no permite auditar la resta. Ese es el hueco exacto donde vive el fraude del
micelio en grano (`218`, `220`, `222`).

## Cómo se comprueba

Las cinco preguntas que hay que hacerle a cualquier laboratorio, antes de pagar:

```
1. ¿Qué método usan, con número y año? (AOAC / USP / Ph. Eur. / interno)
2. ¿La MATRIZ de mi muestra está dentro del alcance del método?
3. Si es método interno, ¿me pasan el resumen de validación? (exactitud, precisión, LOD/LOQ, rango) → 75
4. ¿Cuál es el LOQ para mi analito en mi matriz? ("no detectado" sin LOQ no dice nada) → 73
5. ¿Están acreditados bajo ISO/IEC 17025 para ESE ensayo? (el alcance de acreditación es por ensayo) → 107
```

Si en las cinco preguntas el laboratorio duda, el problema no es el precio: es el resultado.

## Ejemplo aplicado (ILUSTRATIVO)

Dos COA del mismo lote de extracto de reishi, mismo número, distinto valor:

```
COA A: "Beta-glucano 32 %"            método: "interno"      → no auditable
COA B: "Glucano total 41,8 % p/p bs
        Alfa-glucano  9,6 % p/p bs
        Beta-glucano 32,2 % p/p bs"   método: enzimático McCleary, K-YBGL, base seca (humedad 6,1 %)
                                      → auditable: 41,8 − 9,6 = 32,2. Cuadra.
```

El COA B se puede impugnar, comparar entre lotes y usar en una especificación. El A es un folleto. Ejecuta
la resta y la conversión de base en código, no de cabeza: `lab-tools/base_seca.py` y
`lab-tools/betaglucano_dosis.py`, o rutea a `Matematicas_lushows`.

## Errores comunes

- **Pedir "análisis de beta-glucanos" sin especificar el método.** Te pueden mandar polisacáridos totales.
- **Escribir "según AOAC" para un analito o matriz sin método oficial.** Es inexacto y se cae en auditoría.
- **Usar un método fuera de su alcance validado.** El número existe, pero no es defendible.
- **Confundir arsénico total con inorgánico.** Distintos límites, distinta técnica (especiación).
- **Aceptar "no detectado" sin el LOQ.** Sin LOQ no es un resultado, es una frase.
- **Asumir que un laboratorio acreditado lo está para todos sus ensayos.** La acreditación es por ensayo.

## Conexión con otros módulos

→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método por dentro.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — el ensayo que sustituyen para engañar.
→ `280-farmacopeas-usp-ep-y-monografias.md` — la otra fuente de métodos oficiales.
→ `75-validacion-de-metodos-ich-q2-r2.md` — qué exigirle a un método interno.
→ `107-iso-17025-y-acreditacion.md` — qué significa realmente que un laboratorio esté acreditado.
→ `198-analisis-de-potencia-metodo.md` — potencia de cannabis en la práctica.
