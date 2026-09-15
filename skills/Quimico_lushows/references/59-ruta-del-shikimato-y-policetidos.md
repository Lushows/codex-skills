# 59 — Ruta del shikimato y policétidos (aromáticos, hericenonas y el anillo del cannabinoide)

Los anillos aromáticos de la naturaleza salen de dos fábricas: la **ruta del shikimato**, que produce los
aminoácidos aromáticos y de ahí los fenoles vegetales y el triptófano —precursor de la psilocibina—, y la
**ruta policétida**, que ensambla cadenas de acetato y las cicla para dar aromáticos con un patrón de
oxigenación característico. En tu negocio ambas están presentes: el anillo del cannabinoide es policétido,
las hericenonas de la melena de león son policétidos prenilados, y el triptófano de las triptaminas fúngicas
viene del shikimato. Saber de qué ruta viene cada anillo te permite predecir el patrón de sustituyentes y
detectar cuándo un perfil no cuadra.

Términos: **shikimato (shikimate)** = intermediario central que da los aminoácidos aromáticos.
**Policétido (polyketide)** = compuesto formado por condensación repetida de unidades de acetato/malonato.
**PKS (polyketide synthase)** = la enzima que hace policétidos; hay tipo I, II y III. **Aglicona
policétida** = el núcleo aromático resultante. **Prenilado (prenylated)** = con una cadena isoprenoide
añadida (`58`).

## Ruta del shikimato: los aromáticos "del lado vegetal"

```
Fosfoenolpiruvato (PEP) + eritrosa-4-fosfato
   → DAHP → 3-deshidroquinato → ÁCIDO SHIKÍMICO → corismato          (punto de bifurcación)
        ├── prefenato → FENILALANINA y TIROSINA
        └── antranilato → TRIPTÓFANO

Desde FENILALANINA (ruta fenilpropanoide, en plantas):
   Phe --[PAL]--> ácido cinámico → ácido p-cumárico → cumaril-CoA
        → + 3 malonil-CoA (chalcona sintasa, que es una PKS tipo III)
        → CHALCONA → FLAVONOIDES (`51`)  ← ruta MIXTA: shikimato + policétido
        → lignanos, ligninas, ácidos hidroxicinámicos

Desde TRIPTÓFANO (en hongos):
   Trp → (descarboxilación, N-metilaciones, 4-hidroxilación, fosforilación)
        → familia de las 4-sustituidas: norbaeocistina, baeocistina, PSILOCIBINA (`50`, `253`)
   Trp → serotonina, auxinas, alcaloides indólicos en plantas
```

Dato clave que casi nadie usa: **la ruta del shikimato no existe en animales**. Por eso los aminoácidos
aromáticos son esenciales en la dieta humana, y por eso el glifosato —que inhibe la EPSP sintasa de esta
ruta— actúa sobre plantas y microorganismos. Relevancia analítica: residuos de glifosato en materia prima
vegetal se buscan con métodos específicos (LC-MS/MS con derivatización o LC-MS de intercambio iónico), porque
**no aparece en los paneles multiresiduo estándar** (`102`, `64`).

## Ruta policétida: cadenas de acetato que se doblan

```
Unidad inicial (acetil-CoA, hexanoil-CoA, benzoil-CoA...)
   + n × malonil-CoA   --[PKS]-->  cadena poli-β-cetónica
   → ciclación (aldólica o Claisen) → ANILLO AROMÁTICO con OH en posiciones ALTERNAS

Firma diagnóstica: los policétidos aromáticos tienen los oxígenos en posiciones 1,3,5 (meta),
porque vienen de los carbonilos alternos de la cadena. Los fenoles del shikimato tienen patrón
1,2 o 1,4 (orto/para), por hidroxilación del anillo ya formado.
→ Mirando dónde están los OH puedes inferir de qué ruta salió el anillo. Es un truco real de trabajo.
```

Tipos de PKS y qué hacen:

| Tipo | Organismos | Ejemplo de producto |
|---|---|---|
| PKS I (modular, tipo graso) | Bacterias, hongos | Macrólidos, **aflatoxinas** (micotoxinas, `101`) |
| PKS II (iterativa, disociada) | Bacterias | Tetraciclinas, antraquinonas |
| **PKS III** (tipo chalcona sintasa) | Plantas, hongos, bacterias | Chalconas, **ácido olivetólico** del cannabis |

## Los tres casos que te importan

**1. El anillo del cannabinoide es policétido.** Hexanoil-CoA + 3 malonil-CoA por la tetracétido sintasa
(TKS, una PKS III) y ciclación por la olivetolic acid cyclase (OAC) dan **ácido olivetólico**, que luego se
prenila con GPP para dar CBGA (`58`, `172`). Detalles con consecuencia:

- Sin OAC, la ciclación espontánea da **olivetol** (sin -COOH), que no sirve como precursor del cannabinoide
  ácido. Por eso en biosíntesis heteróloga (levaduras modificadas) hacen falta las dos enzimas.
- Si la unidad de partida es **butiril-CoA** (C4) en vez de hexanoil-CoA (C6), se obtiene ácido divarínico y
  toda la línea de **varinas**: THCVA/THCV, CBDVA/CBDV, con cadena propilo en vez de pentilo (`178`).
- Con unidades más largas se llega a homólogos como el **THCP** (cadena heptilo), reportado en literatura
  reciente (`179`).

**2. Las hericenonas son policétidos prenilados.** En el **cuerpo fructífero** de *Hericium erinaceus* se
encuentran las **hericenonas**: núcleo aromático de origen policétido (tipo resorcinol/orcinol), con una
cadena grasa y una prenilación. En el **micelio** se encuentran las **erinacinas**, que son diterpenos
cyathanos de la ruta MVA (`58`). Dos rutas, dos órganos, dos analitos distintos:

| | Hericenonas | Erinacinas |
|---|---|---|
| Origen biosintético | Policétido + prenilación | Terpénico (GGPP, MVA) |
| Órgano | Cuerpo fructífero | Micelio |
| Polaridad | Media-baja (lipofílicas) | Media |
| Extracción | Alcohólica / solvente orgánico | Alcohólica |
| Evidencia de actividad | [in vitro] sobre NGF; clínica limitada | [in vitro]/[animal]; clínica limitada |

Consecuencia comercial directa: **un producto de micelio no puede declarar hericenonas y uno de cuerpo
fructífero no puede declarar erinacinas.** Si el COA dice ambas en el mismo material, hay que preguntar muy
en serio qué se midió y contra qué patrón (`226`, `217`).

**3. Las micotoxinas también son policétidos.** Aflatoxinas, ocratoxina A y patulina salen de PKS fúngicas.
Por eso el riesgo de micotoxinas no es "contaminación de afuera": es metabolismo de hongos filamentosos que
crecen en materia prima mal secada o mal almacenada (`101`, `244`).

## Cómo se comprueba el origen biosintético

| Pregunta | Herramienta | Lectura |
|---|---|---|
| ¿Policétido o shikimato? | Patrón de oxigenación por RMN (1,3,5 vs 1,2/1,4) | Diagnóstico estructural |
| Confirmación experimental | Marcaje con ¹³C-acetato y RMN ¹³C | Enriquecimiento en carbonos alternos = policétido |
| ¿Está la enzima? | Búsqueda de genes PKS en el genoma | Clúster biosintético |
| ¿Qué compuestos hay realmente? | HRMS no dirigido + desreplicación en bases de datos | Perfil metabolómico (`104`) |
| Cuantificar hericenonas | HPLC-DAD/LC-MS con patrón (escasez de patrones certificados) | mg/g base seca (`226`) |

Advertencia de honestidad: para hericenonas y erinacinas **los patrones certificados comerciales son
escasos y caros**. Muchos "análisis de hericenonas" del mercado son semicuantitativos, expresados como
equivalentes de un patrón sustituto. Si te dan un número, pregunta contra qué patrón y con qué pureza (`70`).

## Ejemplo aplicado — auditar "extracto de melena de león estandarizado"

```
Ficha del proveedor (ILUSTRATIVO): "Estandarizado a 0,5 % de hericenonas y erinacinas. Micelio y
  cuerpo fructífero. Polisacáridos 30 %."

Preguntas, con la biosíntesis en la mano:
  1. ¿Qué proporción de micelio y de cuerpo fructífero? Son analitos de rutas distintas (`58`).
  2. ¿El 0,5 % es la SUMA de ambos? ¿Contra qué patrón se expresó cada uno? ¿Pureza del patrón?
  3. ¿Método? Se espera HPLC-DAD o LC-MS con cromatograma adjunto, no un valor suelto.
  4. "Polisacáridos 30 %" no dice nada: se pide β-glucano y α-glucano por K-YBGL (`52`, `221`).
  5. ¿Micelio sobre qué sustrato? El α-glucano lo revela (`218`, `220`).
Si las cinco no se responden por escrito con informes de laboratorio, el "estandarizado" es decorativo.
```

## Errores comunes

- Suponer que todo fenol es "polifenol vegetal". Muchos aromáticos fúngicos son policétidos y se comportan
  distinto en extracción y en detección.
- Buscar glifosato en un panel multiresiduo estándar. No está: requiere método propio (`102`).
- Comprar "hericenonas" en un producto de micelio. Biosintéticamente no encaja.
- Aceptar un valor de hericenonas sin saber contra qué patrón se expresó ni su pureza.
- Olvidar que las micotoxinas son policétidos fúngicos y que el control real es el secado y el almacenamiento,
  no solo el análisis final (`244`).
- Confundir olivetol con ácido olivetólico en una discusión de biosíntesis o de compra de precursores.

## Conexión con otros módulos

→ `58-rutas-biosinteticas-mevalonato-y-mep.md` — la otra mitad: los isoprenoides.
→ `226-hericenonas-y-erinacinas-analisis.md` — el análisis en detalle.
→ `51-polifenoles-y-flavonoides.md` — los productos mixtos shikimato+policétido.
→ `101-analisis-de-micotoxinas.md` — policétidos que sí hay que controlar.
→ `50-alcaloides.md` — el triptófano como precursor de las triptaminas.