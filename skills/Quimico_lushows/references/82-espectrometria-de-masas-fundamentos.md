# 82 — Espectrometría de masas: qué es pesar una molécula y por qué eso te da identidad

La espectrometría de masas es la técnica que convierte un pico anónimo en una molécula con nombre. Mientras
el detector UV solo dice "aquí absorbió algo" (`80`), el espectrómetro de masas dice "aquí pasó algo que
pesa 315,23 y que al romperse produce estos fragmentos". Esa diferencia es la que permite buscar
contaminantes a partes por billón, confirmar que un cannabinoide es el que dice ser y detectar adulterantes
que nadie estaba buscando. También es la técnica donde más fácil se engaña uno solo si no entiende el
efecto matriz.

Términos:
- **Espectrometría de masas (mass spectrometry, MS)** = separar iones según su relación masa/carga y
  contarlos.
- **m/z (mass-to-charge ratio)** = masa dividida por carga. Es lo que el equipo mide, no la masa a secas.
- **Ionización (ionization)** = volver la molécula un ion; sin carga, el equipo no la ve.
- **Ion molecular / ion precursor (molecular ion, precursor ion)** = el ion que representa la molécula
  entera (protonada, desprotonada o con aducto).
- **Fragmento / ion producto (fragment, product ion)** = pedazo que resulta de romper el precursor.
- **Analizador de masas (mass analyzer)** = la parte que separa los iones (cuadrupolo, trampa, TOF,
  Orbitrap).
- **Efecto matriz (matrix effect)** = otras sustancias de la muestra suprimen o realzan la señal del analito.

## Las tres piezas de cualquier MS

```
   MUESTRA ---> [ FUENTE DE IONES ] ---> [ ANALIZADOR ] ---> [ DETECTOR ]
                 vuelve iones           separa por m/z      cuenta iones
                 (ESI, APCI, EI)        (Q, TOF, Orbitrap)

Todo ocurre en ALTO VACIO (10^-5 a 10^-10 torr) en el analizador: si hubiera aire,
los iones chocarian con moleculas de gas antes de llegar al detector.
```

## Fuentes de ionización: la decisión que define qué puedes ver

| Fuente | Cómo ioniza | Se acopla a | Buena para | Espectro |
|---|---|---|---|---|
| **ESI (electrospray ionization)** | Se rocía el líquido con alto voltaje; la molécula sale ya cargada | LC | Compuestos polares, ionizables, termolábiles: psilocibina, micotoxinas, pesticidas | Suave: casi solo el precursor |
| **APCI (atmospheric pressure chemical ionization)** | Descarga corona ioniza el solvente, que transfiere carga | LC | Compuestos poco polares: cannabinoides neutros, esteroles | Suave |
| **APPI (photoionization)** | Fotones UV | LC | Muy apolares (hidrocarburos, carotenos) | Suave |
| **EI (electron ionization, 70 eV)** | Bombardeo de electrones en vacío | GC | Volátiles y semivolátiles: terpenos, solventes residuales | Duro: fragmenta mucho → **huella espectral buscable en bibliotecas** |
| **ICP (inductively coupled plasma)** | Plasma de argón a ~7000 K que atomiza todo | Metales | Elementos: Cd, Pb, As, Hg (`88`) | Iones atómicos, no moléculas |

La diferencia práctica más importante: **EI produce un espectro reproducible entre equipos** — por eso
existen bibliotecas como NIST y Wiley con cientos de miles de espectros y por eso un GC-MS puede identificar
un terpeno desconocido por comparación (`86`). **ESI no fragmenta**, así que no hay biblioteca universal:
la identidad se construye con transiciones MRM (`83`) o con masa exacta y fragmentación controlada (`84`).

## Aductos: por qué el número que ves no es el peso molecular

```
Psilocibina: formula C12H17N2O4P, masa monoisotopica 284,0926 Da

En ESI positivo se detecta como:
   [M+H]+   = 285,0999    <- el habitual
   [M+Na]+  = 307,0818    <- si hay sodio en el solvente o el vidrio
   [M+NH4]+ = 302,1264    <- si la fase movil lleva formiato de amonio

En ESI negativo:
   [M-H]-   = 283,0853

Si el metodo busca 285,1 y tu muestra ioniza como aducto de sodio, la senal
se reparte y la recuperacion cae. Por eso los metodos ESI controlan la
composicion de la fase movil y evitan sodio y potasio (81).
```

Regla que evita malentendidos: **el equipo no pesa la molécula neutra; pesa el ion que le presentaste.** Un
laboratorio serio te dice qué aducto usa.

## Resolución de masa: la diferencia entre "unidad" y "exacta"

| Tipo | Resolución típica (FWHM) | Qué distingue | Equipos |
|---|---|---|---|
| **Baja / unidad** | 1000–2000 (± 0,5 Da) | Distingue 285 de 286, no 285,10 de 285,15 | Cuadrupolo simple, triple cuadrupolo (`83`) |
| **Alta (HRMS)** | 20.000–500.000 | Distingue 285,0999 de 285,1284 → asigna fórmula molecular | Q-TOF, Orbitrap (`84`) |

```
Ejemplo del poder de la masa exacta:
   C12H17N2O4P  [M+H]+ = 285,0999
   C16H13N2O3   [M+H]+ = 281,0921
   Dos compuestos que un cuadrupolo veria casi igual, un Orbitrap los separa
   y le asigna formula a cada uno. Eso es la diferencia entre "hay algo" y
   "es esta molecula".
```

## Modos de adquisición

| Modo | Qué hace | Uso |
|---|---|---|
| **Full scan** | Barre todo el rango de m/z | Screening, buscar lo desconocido |
| **SIM (selected ion monitoring)** | Vigila solo unos m/z | Más sensible, menos información |
| **MRM / SRM (multiple / selected reaction monitoring)** | Selecciona precursor, lo rompe, mide un fragmento | Cuantificación de trazas — el estándar (`83`) |
| **DDA / DIA (data-dependent / independent acquisition)** | Fragmenta los picos intensos, o todo por ventanas | Identificación no dirigida y reanálisis retrospectivo (`84`) |

## Efecto matriz: el error que más resultados falsos produce en MS

Cuando tu analito sale del LC junto con azúcares, lípidos, clorofila o sales, esos compañeros compiten por
la carga en la fuente ESI. Resultado: **la señal del analito baja (supresión iónica) o sube (realce)**, y la
cuantificación se corre sin que nada se vea raro en el cromatograma.

```
Como se mide (ILUSTRATIVO):

  Factor de matriz = area del analito en extracto fortificado
                     -------------------------------------------
                     area del analito en solvente puro, misma conc.

  1,00 = sin efecto | 0,60 = supresion del 40 % | 1,35 = realce del 35 %

Criterio comun en metodos de residuos: |efecto| <= 20 %, o si no,
se COMPENSA con estandar interno isotopico (72).

En hongos y cannabis los efectos de matriz de 30-70 % de supresion son
normales por la carga de pigmentos y lipidos. Un metodo LC-MS/MS sin
estandar interno marcado, o sin calibracion en matriz (matrix-matched),
NO es defendible en estas matrices.
```

Esta es la pregunta que hay que hacerle a todo laboratorio que cotice LC-MS/MS: **¿calibran en matriz o en
solvente, y usan estándar interno isotópicamente marcado?** Si calibran en solvente puro y no usan
estándar interno, tus micotoxinas pueden salir 40 % bajas (`101`).

## Costos y tiempos (orden de magnitud, ILUSTRATIVO)

| Equipo | Precio de compra | Costo por muestra en servicio | Para qué se contrata |
|---|---|---|---|
| GC-MS simple cuadrupolo | USD 60.000–110.000 | COP 150.000–400.000 | Terpenos, solventes residuales, screening |
| LC-MS/MS triple cuadrupolo | USD 200.000–400.000 | COP 300.000–900.000 | Micotoxinas, pesticidas, psilocibina, farmacocinética |
| Q-TOF / Orbitrap (HRMS) | USD 450.000–900.000 | COP 600.000–2.500.000 | Identificación de desconocidos, adulterantes |
| ICP-MS | USD 150.000–300.000 | COP 200.000–600.000 | Metales pesados (`88`) |

## Ejemplo aplicado — un extracto de melena de león con un pico raro

```
Situacion: HPLC-DAD muestra un pico a 8,3 min que no corresponde a ninguna
hericenona conocida. El proveedor dice "es un compuesto natural del hongo".

Ruta analitica sensata y su costo (ILUSTRATIVO):
  1. LC-MS full scan (baja resolucion) .... COP 400.000
     Resultado: [M+H]+ = 384,2 -> hay una molecula de masa nominal 383.
  2. HRMS Q-TOF ........................... COP 1.200.000
     Resultado: 384,2537 -> formula C22H33NO4 (error 1,2 ppm).
     Ya no es "algo": es una formula concreta.
  3. MS/MS de fragmentacion + busqueda en biblioteca/base de datos.
     Si coincide con un aditivo, un plastificante o un farmaco, se acabo
     la discusion (246).

Sin MS, esa conversacion se queda en "confia en mi".
```

## Errores comunes

- **Creer que MS = certeza.** MS mal usada da falsos positivos con la misma facilidad; la identidad exige
  criterios (masa, fragmentos, razón de iones, tiempo de retención — ver `83`, `84`).
- **Pedir LC-MS/MS y calibrar en solvente** en matrices sucias. Es el error #1 en micotoxinas y pesticidas.
- **Suponer que "no detectado" en MS significa ausencia.** Significa por debajo del LOD del método (`73`).
- **Usar TFA en la fase móvil y acoplar a ESI**: suprime la señal brutalmente. Se usa ácido fórmico o
  formiato de amonio (`79`).
- **Comparar un espectro ESI con una biblioteca EI.** Son mundos distintos; no se comparan.
- **Confundir masa nominal con masa exacta** al negociar un informe de identificación.

## Conexión con otros módulos

→ `31-principio-de-la-cromatografia.md` — el frente de separación que alimenta la fuente.
→ `72-estandar-interno-y-adicion-de-estandar.md` — la herramienta que corrige el efecto matriz.
→ `83-lc-ms-ms-y-mrm.md` — la cuantificación de trazas en la práctica.
→ `84-hrms-qtof-orbitrap-e-identificacion.md` — masa exacta e identificación de desconocidos.
→ `86-gc-ms-y-headspace.md` — la variante con EI y bibliotecas.
→ `88-icp-ms-y-metales-pesados.md` — la variante elemental.
→ `104-metabolomica-y-huella-quimica.md` — MS aplicada a comparar materiales completos.
