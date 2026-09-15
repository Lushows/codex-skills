# 85 — Cromatografía de gases: la técnica del aroma, los solventes y los terpenos

La cromatografía de gases es la hermana caliente del HPLC: en vez de empujar la muestra con un líquido, la
vaporiza y la arrastra con un gas por un tubo capilar largo y delgado. Es imbatible en todo lo que se
evapora —terpenos, solventes residuales, ácidos grasos, aromas— y es la técnica equivocada para todo lo que
se descompone con el calor. Entender esa frontera te evita el error más caro del análisis de cannabis:
pedir potencia por GC y recibir un resultado que borró las formas ácidas (`79`).

Términos:
- **GC (gas chromatography)** = cromatografía de gases.
- **Gas portador (carrier gas)** = helio, hidrógeno o nitrógeno; es la fase móvil.
- **Columna capilar (capillary column)** = tubo de sílice fundida de 10–60 m con la fase líquida en la pared
  interna.
- **Volátil / semivolátil (volatile, semi-volatile)** = compuesto que pasa a fase gas sin descomponerse
  dentro del rango del horno.
- **Split / splitless** = el inyector descarta parte de la muestra (split, para concentradas) o la manda toda
  (splitless, para trazas).
- **Índice de retención de Kovats (Kovats retention index, RI)** = escala de retención referida a n-alcanos;
  permite comparar entre equipos.
- **Derivatización (derivatization)** = modificar químicamente el analito para hacerlo volátil o estable.

## Cómo funciona y qué lo limita

```
   MUESTRA (1 uL liquido, o gas de headspace)
       |
   [ INYECTOR 200-300 C ]  vaporiza  -> aqui es donde se descarboxila el THCA
       |
   [ COLUMNA CAPILAR en HORNO con rampa 40 -> 320 C ]
       |
   [ DETECTOR: FID / MS / ECD / TCD ]

REQUISITO ABSOLUTO: el analito debe llegar a fase gas y sobrevivir 250-300 C.
Si no, no hay GC posible sin derivatizar.

NO son analizables directamente por GC: azucares y polisacaridos (beta-glucanos,
219); aminoacidos, peptidos y proteinas; sales y metales (para eso ICP-MS, 88);
psilocibina (el fosfato es termolabil y polar, se degrada — 251, 256); y
cannabinoides ACIDOS sin derivatizar (se descarboxilan — 174).
```

## Columnas de GC: la fase decide todo

| Fase | Polaridad | Nombre comercial típico | Se usa para |
|---|---|---|---|
| 100 % dimetilpolisiloxano | Apolar | DB-1, HP-1, Rtx-1 | Hidrocarburos, análisis general |
| 5 % fenil-95 % metilpolisiloxano | Ligeramente polar | **DB-5ms, HP-5ms, Rtx-5** | El caballo de batalla: terpenos, pesticidas, screening por GC-MS |
| 6 % cianopropilfenil | Media | DB-624, Rtx-624 | **Solventes residuales USP <467>** (`87`) |
| Polietilenglicol (wax) | Polar | DB-WAX, Carbowax | Alcoholes, ácidos grasos, aromas |
| Fases quirales (ciclodextrinas) | — | Rt-βDEXsm | Separar enantiómeros de terpenos (`43`, `182`) |

Dato práctico: cuando cotices **solventes residuales**, el laboratorio debe mencionar una columna tipo 624 o
equivalente y el método USP <467>; si te habla de una DB-5 genérica, probablemente adaptó un método de otra
cosa (`87`).

## Detectores de GC

| Detector | Qué mide | Sensibilidad típica | Cuándo |
|---|---|---|---|
| **FID (flame ionization)** | Carbono orgánico quemado en llama de H₂ | ng | Cuantificación robusta y barata: terpenos, solventes. Respuesta casi proporcional al carbono |
| **MS (mass spectrometry)** | m/z, con EI y biblioteca | pg–ng | Identificación + cuantificación (`86`) |
| **ECD (electron capture)** | Compuestos halogenados | fg–pg | Pesticidas organoclorados |
| **NPD / TSD** | Nitrógeno y fósforo | pg | Pesticidas organofosforados |
| **TCD (thermal conductivity)** | Cambio de conductividad térmica | µg | Gases fijos; poco sensible |

La combinación **GC-FID para cuantificar + GC-MS para identificar** sigue siendo el estándar en perfiles de
terpenos: el FID da áreas estables y baratas, el MS confirma quién es quién.

## El error caro: GC y las formas ácidas del cannabis

Ya se explica en `79`, y vale repetirlo desde el lado del GC porque es el punto donde la técnica te traiciona:

```
En el inyector a 250-280 C:
      THCA  --(-CO2)-->  D9-THC        CBDA --(-CO2)--> CBD

Consecuencias:
  1. El COA por GC reporta "THC" alto y "THCA no detectado", aunque la planta
     este llena de THCA, y pierdes la informacion que define legalmente
     muchos productos crudos.
  2. Ese "THC" es en realidad THC total, con una eficiencia de conversion que
     NO es 100 % y varia con inyector, liner y matriz: un sesgo incontrolable.

Salidas legitimas:
  a) HPLC-DAD sin calor  -> ve THCA y THC por separado. ES LA CORRECTA (79, 198).
  b) GC CON DERIVATIZACION (sililacion con BSTFA/MSTFA + TMCS, ver 64):
     se protege el -COOH como ester de trimetilsililo, el THCA se vuelve
     volatil y estable, y se ven ambas formas. Funciona, pero agrega un paso,
     reactivos sensibles a humedad y mas incertidumbre.
  c) GC con inyector "cool on-column": reduce la descarboxilacion, no la elimina.

Regla de compra: para POTENCIA de cannabinoides pide HPLC.
```

## Dónde GC sí es la herramienta correcta en nuestro mundo

| Análisis | Técnica exacta | Unidad de reporte | Módulo |
|---|---|---|---|
| Perfil de terpenos en cannabis | HS-GC-MS o GC-FID con inyección líquida | mg/g o % p/p | `182`, `199` |
| Solventes residuales | **Headspace-GC-FID/MS**, USP <467> | ppm (µg/g) | `87`, `201` |
| Pesticidas volátiles y organoclorados | GC-MS/MS | µg/kg | `102`, `200` |
| Perfil de ácidos grasos | GC-FID de ésteres metílicos (FAME, previa transesterificación) | % del total de ácidos grasos | `53` |
| Esteroles y triterpenos (previa sililación) | GC-MS | mg/g | `55`, `238` |
| Compuestos de aroma en un extracto | HS-SPME-GC-MS | área relativa o mg/kg | `86` |
| Ergosterol como marcador de biomasa fúngica | GC-MS o HPLC-UV | mg/g base seca | `238` |

## Ejemplo aplicado — perfil de terpenos de una flor

```
Metodo (ILUSTRATIVO, formato de laboratorio de cannabis):

  Preparacion : 200 mg de flor molida (67) + 10 mL de etanol o isopropanol
                con estandar interno (n-tridecano o 4-fluoroanisol),
                vortex 1 min, sonicacion 10 min, filtro 0,22 um.
                O bien headspace estatico a 80 C, 20 min (86).
  Columna     : DB-5ms 30 m x 0,25 mm x 0,25 um
  Gas         : helio 1,0 mL/min (o hidrogeno, mas rapido y mas barato)
  Inyector    : 250 C, split 20:1
  Horno       : 60 C (1 min) -> 5 C/min -> 180 C -> 20 C/min -> 300 C (3 min)
  Deteccion   : FID para cuantificar (curva por terpeno) + MS para confirmar
  Analitos    : 15-40 terpenos (mirceno, limoneno, pineno alfa/beta,
                linalool, cariofileno, humuleno, terpinoleno, ocimeno...)
  Reporte     : mg/g de flor, o % p/p, SIEMPRE con la base declarada.

Ordenes de magnitud reportados en la literatura para flor seca: terpenos
totales 0,5-3 % p/p; los monoterpenos volatiles se pierden mucho en el secado
y el curado (186). Verifica con tu lote.

Costo (ILUSTRATIVO): COP 250.000-550.000 por muestra; 4-8 dias habiles.
```

Advertencia de interpretación: un perfil de terpenos **cambia con el secado, el curado, el envase y el
tiempo**. Comparar el perfil de una flor fresca con el de la misma flor tres meses después y concluir que
"el proveedor cambió la genética" es un error clásico (`186`, `61`).

Nota práctica 2026: por el precio del helio, muchos laboratorios migraron a **hidrógeno** generado in situ.
Es más rápido y barato, pero **cambia los tiempos de retención**. Si comparas resultados históricos de un
laboratorio que migró, los tR no coinciden: no es un error, es el gas. Que te lo declaren.

## Qué preguntarle al laboratorio

1. ¿Qué **columna** (fase, largo, diámetro, película) y qué **gas portador**?
2. Para cannabinoides: ¿por qué GC y no HPLC? ¿**Derivatizan**? (Si no, ya sabes qué te van a reportar.)
3. ¿Usan **estándar interno**? ¿Cuál? (En GC es casi obligatorio por la variabilidad de la inyección.)
4. ¿Cuántos terpenos cuantifican y **cada uno tiene su patrón**, o algunos van por respuesta relativa?
5. ¿Qué temperatura de inyector y qué tipo de liner? (Determina la degradación térmica.)
6. ¿Confirmaron identidad por **índice de retención** además del espectro? (`86`)

## Errores comunes

- **Pedir potencia de cannabinoides por GC** y luego pelear con el proveedor por un número que el método
  fabricó.
- **Comparar perfiles de terpenos** entre laboratorios con inyección líquida vs headspace: dan proporciones
  distintas por diseño.
- **Cuantificar 30 terpenos con 5 patrones.** Se puede, pero hay que declarar los factores de respuesta.
- **Ignorar la pérdida de volátiles en la molienda.** Moler caliente evapora monoterpenos antes de medir (`67`).
- **Inyectar extractos grasos sin limpiar**: ensucian el liner y la columna, y los resultados derivan durante
  la secuencia.
- **Usar áreas relativas (%) como si fueran concentración.** "12 % de limoneno del total de terpenos" no dice
  cuántos mg/g hay.

## Conexión con otros módulos

→ `29-destilacion-y-equilibrio-liquido-vapor.md` — volatilidad, que es el requisito de entrada.
→ `31-principio-de-la-cromatografia.md` — la teoría común con LC.
→ `64-derivatizacion-para-analisis.md` — cómo se vuelve analizable lo que no es volátil.
→ `79-hplc-y-uhplc.md` — la alternativa correcta para formas ácidas.
→ `86-gc-ms-y-headspace.md` — el detector MS y la inyección por espacio de cabeza.
→ `87-solventes-residuales.md` — la aplicación regulada más importante del GC.
→ `182-terpenos-del-cannabis.md` y `199-analisis-de-perfil-de-terpenos.md` — la química y el método aplicados.
