# 87 — Solventes residuales: qué quedó de tu extracción y cuánto es demasiado

Todo extracto hecho con solvente arrastra algo de ese solvente al producto final. La pregunta no es "¿quedó
o no quedó?" —siempre queda algo— sino **"¿cuánto quedó y está por debajo del límite que corresponde a su
clase de toxicidad?"**. Es uno de los cuatro análisis de contaminantes que un producto extraído no puede
saltarse (junto con metales, pesticidas y micotoxinas) y es de los más baratos. También es donde más se
miente en el mercado de concentrados, porque un COA de solventes residuales sin la matriz correcta es un
papel bonito y nada más.

Términos:
- **Solvente residual (residual solvent)** = solvente orgánico que queda en el producto tras la extracción o
  la purificación.
- **PDE (permitted daily exposure)** = exposición diaria permitida, en mg/día. Es el número toxicológico
  base; el límite en ppm se deriva de él.
- **ppm** = partes por millón = **µg/g** = mg/kg. Siempre con base declarada.
- **Headspace-GC (HS-GC)** = la técnica: se calienta el vial sellado y se inyecta la fase gas (`86`).
- **Clase 1 / 2 / 3** = clasificación toxicológica de ICH Q3C, adoptada por USP <467>.
- **LOQ (limit of quantitation)** = mínimo cuantificable del método (`73`).

## Las tres clases, y qué significan de verdad

A agosto de 2026 el marco vigente es **ICH Q3C(R9)** (guía de solventes residuales, con actualizaciones
periódicas de PDE) y su implementación farmacopeica en **USP <467> Residual Solvents** y en el capítulo
2.4.24 de la Farmacopea Europea. Verifica siempre la versión vigente en `database.ich.org` y en `uspnf.com`
antes de meter un límite en una especificación.

| Clase | Definición | Regla | Ejemplos |
|---|---|---|---|
| **Clase 1** | Cancerígenos conocidos o de riesgo ambiental grave | **Evitar.** Solo si son indispensables, con límite muy bajo | Benceno, tetracloruro de carbono, 1,2-dicloroetano, 1,1-dicloroeteno, 1,1,1-tricloroetano |
| **Clase 2** | Toxicidad significativa; efectos no genotóxicos | **Limitar** según PDE | Metanol, acetonitrilo, diclorometano, hexano, tolueno, cloroformo, piridina |
| **Clase 3** | Baja toxicidad potencial | Aceptables hasta **5000 ppm (0,5 %)** sin justificación | Etanol, acetona, acetato de etilo, isopropanol, heptano, pentano, 1-propanol |

Límites de Clase 1 (concentración límite, según USP <467> / ICH Q3C — verifica la versión vigente):

```
CLASE 1 (concentracion limite):
  Benceno 2 ppm | Tetracloruro de carbono 4 ppm | 1,2-dicloroetano 5 ppm
  1,1-dicloroeteno 8 ppm | 1,1,1-tricloroetano 1500 ppm

CLASE 2 (PDE mg/dia -> limite en ppm con dosis de 10 g/dia):
  Metanol .......... PDE 30 mg/dia   ->  3000 ppm
  Acetonitrilo ..... PDE 4,1 mg/dia  ->   410 ppm
  Diclorometano .... PDE 6,0 mg/dia  ->   600 ppm
  n-Hexano ......... PDE 2,9 mg/dia  ->   290 ppm
  Tolueno .......... PDE 8,9 mg/dia  ->   890 ppm
  Cloroformo ....... PDE 0,6 mg/dia  ->    60 ppm

CLASE 3 (todos): 5000 ppm = 0,5 % p/p, salvo justificacion de dosis alta.
```

## La fórmula que casi nadie aplica bien

```
Concentracion limite (ppm) = 1000 * PDE (mg/dia) / dosis diaria (g/dia)

La "Opcion 1" de USP <467> ASUME una dosis diaria de 10 g/dia. De ahi salen
los ppm de la tabla. Si tu producto se consume en 1 g/dia, el limite en ppm
es 10 VECES MAS PERMISIVO. Si se consume en 30 g/dia, es 3 veces mas estricto.

Ejemplo (ILUSTRATIVO):
  Aceite de CBD, dosis diaria declarada 0,5 g/dia. Solvente: n-hexano.
  Limite = 1000 * 2,9 / 0,5 = 5800 ppm
  vs el limite de tabla (Opcion 1, 10 g/dia) = 290 ppm

  OJO: no puedes usar la Opcion 2 sin declarar y sostener la dosis diaria
  maxima real en tu expediente. La practica sensata en suplementos es
  cumplir la Opcion 1 y punto.
```

## El método: headspace-GC, procedimientos A, B y C

USP <467> describe un esquema de tres procedimientos que conviene conocer para leer un COA:

| Procedimiento | Qué hace | Resultado |
|---|---|---|
| **A** | Screening por HS-GC-FID/MS en una columna tipo G43 (6 % cianopropilfenil, tipo 624) | Si nada supera el límite → **cumple**, se acabó |
| **B** | Confirmación en una columna de **selectividad distinta** (G16, tipo wax) | Si el pico de A era una coelución, aquí se ve |
| **C** | Cuantificación del solvente confirmado | Número final en ppm |

```
Condiciones tipicas del Procedimiento A (ILUSTRATIVO — el metodo oficial manda):

  Columna    : G43 / tipo 624, 30 m x 0,32 mm x 1,8 um
  Diluyente  : agua, o DMSO / DMF / DMA si la muestra no es soluble en agua
  Vial HS    : muestra + diluyente, sellado; equilibrio 80 C, 60 min
               (o 105 C, 45 min segun la variante)
  Inyeccion  : headspace estatico, split
  Horno      : 40 C (20 min) -> 10 C/min -> 240 C (20 min)
  Deteccion  : FID (y/o MS para confirmar identidad)
  Aptitud    : S/N >= 5 para benceno; S/N >= 3 para los demas (77)

Costo (ILUSTRATIVO): COP 200.000-500.000 por muestra (panel estandar);
COP 350.000-800.000 (panel ampliado de cannabis). Tiempo: 3-8 dias habiles.
```

## Cannabis: por qué este análisis es obligatorio en concentrados

En cannabis la extracción se hace con etanol (`187`), hidrocarburos (butano, propano — `188`), CO₂ (`189`) o
sin solvente (`190`). El riesgo cambia por completo según la ruta:

| Ruta | Solventes a vigilar | Riesgo real |
|---|---|---|
| Etanol | Etanol (Clase 3), y **metanol** si es desnaturalizado o de mala calidad | El metanol es la trampa: entra como impureza del etanol, no como solvente de proceso |
| Hidrocarburos (BHO/PHO) | n-butano, isobutano, propano, y **n-hexano/pentano** si el gas es industrial | Gas de baja pureza trae hexano y compuestos azufrados |
| CO₂ supercrítico | Casi ninguno; a veces co-solvente etanol | El más limpio en este aspecto |
| Solventless (rosin) / destilación | Ninguno / heptano, pentano, acetona | El rosin no requiere el ensayo (sí microbiología); la purificación sí |

A agosto de 2026 no existe un límite único mundial para solventes residuales en cannabis: **cada
jurisdicción publica su propia tabla**. Estados de EE. UU. tienen listas que incluyen butano y propano —que
no están en ICH Q3C porque no son solventes farmacéuticos típicos— con límites del orden de miles de ppm. En
Colombia, para cannabis medicinal, la referencia es la farmacopea adoptada y lo que exija el INVIMA para la
forma farmacéutica; **confirma el requisito vigente antes de fijar tu especificación** (`210`, `201`).

## Ejemplo aplicado — un COA de destilado de CBD que no sirve

```
COA recibido:
  "Solventes residuales: PASA. Metodo: GC-MS. Etanol < 500 ppm."

Lo que falta y por que importa:
  1. QUE solventes buscaron: un panel de 1 no descarta metanol, hexano ni benceno.
  2. El LOQ de cada uno. "< 500 ppm" para benceno seria absurdo: el limite es
     2 ppm, asi que un LOQ de 500 ppm no demuestra nada.
  3. LA MATRIZ DE CALIBRACION. Un destilado oleoso retiene los volatiles mucho
     mas que el agua: calibrar en agua sesga el resultado a la baja (86). Se
     exige matrix-matched o adicion de estandar (72).
  4. La dosis usada para derivar el limite (Opcion 1 vs Opcion 2).
  5. El blanco de metodo: acetona y etanol son ubicuos en un laboratorio.

Lo que deberia decir un COA correcto (ILUSTRATIVO):
  Metodo: HS-GC-MS segun USP <467>, procedimientos A y C; calibracion en
  matriz (aceite de MCT); 24 analitos.
  Benceno   < 1 ppm (LOQ 1)      Metanol   38 ppm (LOQ 10)   limite 3000
  n-Hexano  < 10 ppm (LOQ 10)    Etanol   410 ppm (LOQ 50)   limite 5000
  n-Butano  < 50 ppm (LOQ 50)    Propano  < 50 ppm (LOQ 50)
  Cumple. Recuperacion del spike 88-107 %.
```

## Qué preguntarle al laboratorio

1. ¿**Cuántos y cuáles** solventes incluye el panel? ¿Está el metanol? ¿Está el benceno?
2. ¿Cuál es el **LOQ de cada analito** y es lo bastante bajo frente a su límite?
3. ¿Calibran **en matriz** (aceite, resina, polvo) o en agua/DMSO?
4. ¿Aplican **Procedimiento B** para confirmar antes de reportar un positivo?
5. ¿Qué **límite** usan como criterio y de dónde lo sacan (USP <467>, norma local de cannabis, otra)?
6. ¿Corren **blanco de método** y **blanco de vial**?
7. ¿El ensayo está en su **alcance acreditado** para mi matriz? (`107`)

## Errores comunes

- **Aceptar "pasa" sin la lista de analitos y sin LOQ.** Es el COA vacío más frecuente del mercado.
- **Calibrar en agua para medir en aceite.** Subestima sistemáticamente. Punto crítico en concentrados.
- **Olvidar el metanol** cuando se extrae con etanol desnaturalizado o de grado industrial.
- **Usar la Opción 2 (dosis real) sin sostenerla en el expediente.** Es válida solo con justificación
  documentada y dosis máxima declarada.
- **Creer que "sin solventes" exime de contaminantes.** Exime de este, no de metales ni microbiología.
- **Repetir hasta que dé.** Si el secado no eliminó el solvente, la solución es secar mejor (`149`), no
  cambiar de laboratorio (`113`).
- **Confundir ppm con mg por porción.** ppm es por gramo; la exposición diaria depende de la dosis (`04`).

## Conexión con otros módulos

→ `85-cromatografia-de-gases.md` y `86-gc-ms-y-headspace.md` — la técnica que lo mide.
→ `63-quimica-verde-y-solventes.md` — elegir solventes que no te creen este problema.
→ `73-lod-loq-y-rango-lineal.md` — por qué el LOQ define si el COA prueba algo.
→ `135-noael-ida-y-limites-de-exposicion.md` — de dónde salen los PDE.
→ `149-concentracion-y-evaporacion.md` — cómo se elimina el solvente en la práctica.
→ `187`, `188`, `189` — extracción con etanol, hidrocarburos y CO₂: las rutas que generan cada riesgo.
→ `201-solventes-residuales-en-cannabis.md` — límites y práctica específicos de cannabis.
→ `280-farmacopeas-usp-ep-y-monografias.md` — dónde vive el capítulo <467> y cómo citarlo.
